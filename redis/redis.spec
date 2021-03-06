Summary: Redis key-value database.
Name: redis
Version: 2.6.11
Release: 1%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://code.google.com/p/redis/

Source0: http://mirror.abiquo.com/sources/redis-%{version}.tar.gz
Source1: redis.conf
Source2: redis.logrotate
Source3: redis.init

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make
Requires(post): /sbin/chkconfig /usr/sbin/useradd
Requires(preun): /sbin/chkconfig, /sbin/service
Requires(postun): /sbin/service
Provides: redis

%description
Redis is a key-value database. It is similar to memcached but the dataset is
not volatile, and values can be strings, exactly like in memcached, but also
lists and sets with atomic operations to push/pop elements.

In order to be very fast but at the same time persistent the whole dataset is
taken in memory and from time to time and/or when a number of changes to the
dataset are performed it is written asynchronously on disk. You may lose the
last few queries that is acceptable in many applications but it is as fast
as an in memory DB (beta 6 of Redis includes initial support for master-slave
replication in order to solve this problem by redundancy).

Compression and other interesting features are a work in progress. Redis is
written in ANSI C and works in most POSIX systems like Linux, *BSD, Mac OS X,
and so on. Redis is free software released under the very liberal BSD license.


%prep
%setup

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
make install PREFIX=%{buildroot}%{_prefix}

%{__install} -Dp -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/redis
%{__install} -Dp -m 0755 %{SOURCE3} %{buildroot}%{_initrddir}/redis
%{__install} -Dp -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/redis.conf
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/lib/redis
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/log/redis
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/run/redis

# Fix non-standard-executable-perm error
chmod 755 %{buildroot}%{_bindir}/%{name}-*

# Ensure redis-server location doesn't change
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/%{name}-server %{buildroot}%{_sbindir}/%{name}-server


%pre
/usr/sbin/useradd -c 'Redis' -u 499 -s /bin/false -r -d %{_localstatedir}/lib/redis redis 2> /dev/null || :

%preun
if [ $1 = 0 ]; then
    # make sure redis service is not running before uninstalling

    # when the preun section is run, we've got stdin attached.  If we
    # call stop() in the redis init script, it will pass stdin along to
    # the redis-cli script; this will cause redis-cli to read an extraneous
    # argument, and the redis-cli shutdown will fail due to the wrong number
    # of arguments.  So we do this little bit of magic to reconnect stdin
    # to the terminal
    term="/dev/$(ps -p$$ --no-heading | awk '{print $2}')"
    exec < $term

    /sbin/service redis stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del redis
fi

%post
/sbin/chkconfig --add redis

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/redis-*
%{_bindir}/redis-*
%{_initrddir}/redis
%config %{_sysconfdir}/redis.conf
%{_sysconfdir}/logrotate.d/redis
%dir %attr(0770,redis,redis) %{_localstatedir}/lib/redis
%dir %attr(0755,redis,redis) %{_localstatedir}/log/redis

%changelog
* Tue Mar 26 2013 Abel Boldú <abel.boldu@abiquo.com> - 2.6.11-1
- Bumped version to 2.6.11, new config

* Wed Jan 09 2013 Abel Boldú <abel.boldu@abiquo.com> - 2.6.7-1
- Bumped version to 2.6.7

* Wed Mar 14 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0.4-2
- Fixed pidfile bug

* Fri Dec 10 2010 Sergio Rubio <srubio@abiquo.com> - 2.0.4-1
- updated to redis 2.0.4

* Tue Oct 06 2010 - Sergio Rubio <srubio@abiquo.com> 2.0.2-3
- update redis.conf

* Tue Oct 06 2010 - Sergio Rubio <srubio@abiquo.com> 2.0.2-2
- replace default redis.conf

* Tue Oct 05 2010 - Sergio Rubio <srubio@abiquo.com> 2.0.2-1
- updated to upstream 2.0.2

* Thu May 27 2010 - Carlos Laviola <carlos.laviola@corp.globo.com> 2.0.0.rc1
- redis updated to version 2.0.0-rc1 (development release form GitHub)

* Wed May 05 2010 - brad at causes dot com 1.3.9-1
- redis updated to version 1.3.9 (development release from GitHub)
- extract config file from spec file
- move pid file from /var/run/redis/redis.pid to just /var/run/redis.pid
- move init file to /etc/init.d/ instead of /etc/rc.d/init.d/

* Fri Sep 11 2009 - jpriebe at cbcnewmedia dot com 1.0-1
- redis updated to version 1.0 stable

* Mon Jun 01 2009 - jpriebe at cbcnewmedia dot com 0.100-1
- Massive redis changes in moving from 0.09x to 0.100
- removed log timestamp patch; this feature is now part of standard release

* Tue May 12 2009 - jpriebe at cbcnewmedia dot com 0.096-1
- A memory leak when passing more than 16 arguments to a command (including
  itself).
- A memory leak when loading compressed objects from disk is now fixed.

* Mon May 04 2009 - jpriebe at cbcnewmedia dot com 0.094-2
- Patch: applied patch to add timestamp to the log messages
- moved redis-server to /usr/sbin
- set %config(noreplace) on redis.conf to prevent config file overwrites
  on upgrade

* Fri May 01 2009 - jpriebe at cbcnewmedia dot com 0.094-1
- Bugfix: 32bit integer overflow bug; there was a problem with datasets
  consisting of more than 20,000,000 keys resulting in a lot of CPU usage
  for iterated hash table resizing.

* Wed Apr 29 2009 - jpriebe at cbcnewmedia dot com 0.093-2
- added message to init.d script to warn user that shutdown may take a while

* Wed Apr 29 2009 - jpriebe at cbcnewmedia dot com 0.093-1
- version 0.093: fixed bug in save that would cause a crash
- version 0.092: fix for bug in RANDOMKEY command

* Fri Apr 24 2009 - jpriebe at cbcnewmedia dot com 0.091-3
- change permissions on /var/log/redis and /var/run/redis to 755; this allows
  non-root users to check the service status and to read the logs

* Wed Apr 22 2009 - jpriebe at cbcnewmedia dot com 0.091-2
- cleanup of temp*rdb files in /var/lib/redis after shutdown
- better handling of pid file, especially with status

* Tue Apr 14 2009 - jpriebe at cbcnewmedia dot com 0.091-1
- Initial release.

