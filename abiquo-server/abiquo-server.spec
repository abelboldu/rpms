%define abiquo_basedir /opt/abiquo

Name:           abiquo-server
Version:        2.4.0
Release:        1%{?dist}%{?buildstamp}
Url:            http://www.abiquo.com/
License:        Multiple
Group:          Development/Tools
Summary:        Abiquo Server Enterprise Edition 
Source0:        abiquo.properties.server
Source1:        abiquo-accounting.cron
Source2:	%{?abiquo_binaries_url}database/kinton-schema.sql
Source3:	%{?abiquo_binaries_url}database/kinton-%{version}-delta.sql
Source4:        kinton-delta-disable-wizard
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       abiquo-core abiquo-client-premium nfs-utils sos wget ruby ntp libvirt-client redis 
Requires:       /usr/sbin/sendmail /usr/bin/which
BuildRequires:  /usr/bin/unzip
BuildArch: 	noarch

%description
Next Generation Cloud Management Solution

This package contains the server enterprise component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%prep
# Abiquo wizard fix
cat %{SOURCE4} >> %{SOURCE3}

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/database
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/examples
mkdir -p $RPM_BUILD_ROOT%{abiquo_basedir}
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/
mkdir -p %{buildroot}/%{_sysconfdir}/cron.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
cp %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}/database/
cp -r %{SOURCE0} $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/
cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/cron.d/abiquo-accounting
cp %{SOURCE3} $RPM_BUILD_ROOT%{_docdir}/%{name}/database/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_docdir}/%{name}
%{_sysconfdir}/cron.d/abiquo-accounting
%{abiquo_basedir}/config/examples/abiquo.properties.server

%changelog
* Wed Dec 05 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.4.0-1
- Bumped version to 2.4.0

* Tue Oct 23 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.3.0-1
- bumped version to 2.3.0

* Fri Oct 05 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.2.0-2
- Accounting refactor added

* Fri Aug 31 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.2.0-1
- new versioning

* Fri Jun 08 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.2-1
- Bumped version to 2.2

* Tue May 29 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0-8
- Added HF3 delta

* Thu May 24 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0-7
- 2.0-HF3 Bump

* Wed Apr 11 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0-6
- update to include 2.0 -> 2.0 HF1 delta

* Fri Mar 16 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0-5
- release bump

* Thu Mar 15 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0-4
- bumped release

* Wed Mar 14 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0-3
- Added redis

* Thu Mar 08 2012 Abel Boldú <abel.boldu@abiquo.com> - 2.0-2
- Added 1.8.5 to 2.0 deltas

* Mon Dec 19 2011 Sergio Rubio <srubio@abiquo.com> - 2.0-1
- bumped version to 2.0

* Fri Nov 18 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8.5-7
- HF4

* Fri Nov 04 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-6
- include 1.8.5-HF3 db delta
- update DB schema

* Thu Oct 27 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8.5-5
- abiquo-server.spec

* Mon Oct 10 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-4
- updated to include 1.8.5 -> 1.8.5 HF1 delta

* Fri Oct 07 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-3
- updated to include 1.8.0 -> 1.8.5 HF1 delta

* Fri Sep 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-2
- updated delta and schema

* Fri Sep 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8.5-1
- bumped version to 1.8.5

* Mon Jul 04 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8-2
- added new database delta

* Tue Jun 14 2011 Sergio Rubio <rubiojr@frameos.org> - 1.8-1
- add tomcat default context config

* Fri Apr 15 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.6-2
- fixed install section

* Wed Apr 13 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.6-1
- bumped version

* Tue Apr 05 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-4
- readed deltas and schemas
- add ABICLOUDPREMIUM-1464 patches

* Mon Mar 28 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-3
- bumped release
- removed abiquo-server-tools dep

* Wed Mar 23 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7.5-2
- bumped release
- 1.7.5 db delta fixed

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- added 1.7.0 to 1.7.5 delta 
- bumped version to 1.7.5

* Wed Feb 16 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-27
- fix release string

* Thu Feb 03 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-26.GA
- upstream fixes

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-25.GA
- GA build

* Mon Jan 31 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-24
- updated 1.6.8 to 1.7 delta
- updated database schema

* Fri Jan 28 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-23
- updated 1.6.8 to 1.7 delta

* Fri Jan 28 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-22
- updated database schema
- updated 1.6.8 to 1.7 delta

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-21
- added new premium delta

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-20
- updated database schema
- updated 1.6.8 to 1.7 delta

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-19
- updated database schema

* Thu Jan 27 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-18
- updated 1.6.8 to 1.7 delta
- updated database schema

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-17
- updated 1.6.8 to 1.7 delta

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-16
- updated 1.6.8 to 1.7 delta

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-15
- updated database schema

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-14
- updated database schema

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-13
- moved properties template to /opt/abiquo/config/examples

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-12
- fix files section

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-11
- moved properties template to /usr/share/doc

* Wed Jan 19 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-10
- updated default properties

* Tue Jan 18 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-9
- updated default properties

* Tue Jan 18 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-8
- updated db schema

* Fri Jan 14 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-7
- updated db schema
- updated server properfies template

* Thu Jan 13 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-6
- updated db schema

* Mon Jan 10 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-5
- Use the WAR as Source0

* Mon Dec 20 2010 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- require abiquo-client-premium instead of abiquo-client

* Fri Dec 17 2010 Sergio Rubio <rubiojr@frameos.org> - 1.7-3
- kinton-premium-schema removed

* Tue Dec 14 2010 Sergio Rubio <rubiojr@frameos.org> - 1.7-2
- use the new build system

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Fri Nov 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-2
- added accounting cron file

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Tue Sep 14 2010 Sergio Rubio srubio@abiquo.com 1.6.5-2
- removed tools

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Tue Jul 20 2010 Sergio Rubio srubio@abiquo.com 1.6-3
- Removed abiquo-server init script

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- Added buildstamp to the package

* Mon Jul 05 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Updated to upstream 1.6

* Tue May 18 2010 Sergio Rubio srubio@abiquo.com 1.5.1-1
- Initial Release
