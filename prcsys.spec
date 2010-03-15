%define name prcsys
%define version 0.0.3

Summary: Parallel init for Mandriva
Name: %{name}
Version: %{version}
Release: %mkrel 6
# SVN snapshot from http://zarb.org/users/svn/trem/prcsys/trunk/
Source0: %{name}-%{version}.tar.bz2
Patch0: prcsys-0.0.3-LDFLAGS.diff
# (fc) 0.0.3-5mdv add support for plymouth
Patch1: prcsys-0.0.3-plymouth.patch
License: GPL
Group: System/Base
Url: http://www.zarb.org/~couriousous/boot/
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


