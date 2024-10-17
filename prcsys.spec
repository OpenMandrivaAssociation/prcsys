%define name prcsys
%define version 0.0.3

Summary: Parallel init for Mandriva
Name: %{name}
Version: %{version}
Release: %mkrel 9
# SVN snapshot from http://zarb.org/users/svn/trem/prcsys/trunk/
Source0: %{name}-%{version}.tar.bz2
Patch0: prcsys-0.0.3-LDFLAGS.diff
# (fc) 0.0.3-5mdv add support for plymouth
Patch1: prcsys-0.0.3-plymouth.patch
License: GPL
Group: System/Base
Url: https://www.zarb.org/~couriousous/boot/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts: initscripts < 8.38

%description
A parallel init implementation for Mandriva.
It should be LSB compliant.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .LDFLAGS
%patch1 -p1 -b .plymouth

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/sbin
install -m755 prcsys $RPM_BUILD_ROOT/sbin/

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS Changelog
%defattr(755,root,root)
/sbin/prcsys




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-8mdv2011.0
+ Revision: 667820
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-7mdv2011.0
+ Revision: 607205
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-6mdv2010.1
+ Revision: 520201
- rebuilt for 2010.1

* Thu Aug 13 2009 Frederic Crozat <fcrozat@mandriva.com> 0.0.3-5mdv2010.0
+ Revision: 416057
- Patch1: add support for plymouth

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-4mdv2009.1
+ Revision: 317125
- use %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.0.3-3mdv2009.0
+ Revision: 225046
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-2mdv2008.1
+ Revision: 179284
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jan 02 2007 Olivier Blin <oblin@mandriva.com> 0.0.3-1mdv2007.0
+ Revision: 103088
- new upstream snapshot

* Tue Aug 29 2006 Couriousous <couriousous@mandriva.org> 0.0.2-1mdv2007.0
+ Revision: 58243
- new snapshot (add logging to prcsys)

* Fri Aug 18 2006 Olivier Blin <oblin@mandriva.com> 0.0.1-1mdv2007.0
+ Revision: 56505
- Import prcsys

* Fri Aug 18 2006 Olivier Blin <blino@mandriva.com> 0.0.1-1mdv2007.0
- initial Mandriva release of prcsys based on parallel-init spec file

* Fri Dec 16 2005 Couriousous <couriousous@mandriva.org> 0.0.1-1mdk
- add a parallel init to cooker

