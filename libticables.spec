%define version 3.9.7
%define release %mkrel 1

%define major 3
%define libname %mklibname ticables %{major}

Summary:	Library to handle the different TI link cables
Name:		libticables
Version:	%{version}
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/tilp/%{name}-%{version}.tar.bz2
License:	LGPL
Group:		Communications
Url:		http://tilp.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libusb-devel
Requires:	%{libname} = %{version}


%description
The TiCables library is a part of the TiLP project and constitutes with
the other libraries a complete framework for developping and/or linking
TI files oriented applications.

It is able to handle the different link cables designed for TI's graphing
calculators (also called handheld), without worrying about different link
cables characteristics as well as different platforms.

It supports all the currently available link cables:
- home-made parallel (aka $5-cable)
- home-made serial (aka $4-cable)
- TI's BlackLink
- TI's GrayLink
- TI's SilverLink
- AVRlink

It also supports some 'virtual' link cables for connection with emulators:
- Virtual TI (VTi)
- (Gtk)TiEmu

%package	-n %{libname}
Group:		Communications
Summary:	Library to handle different TI link cables
Requires:	%{name} = %{version}

%description	-n %{libname}
The TiCables library is a part of the TiLP project and constitutes with
the other libraries a complete framework for developping and/or linking
TI files oriented applications.

It is able to handle the different link cables designed for TI's graphing
calculators (also called handheld), without worrying about different link
cables characteristics as well as different platforms.

It supports all the currently available link cables:
- home-made parallel (aka $5-cable)
- home-made serial (aka $4-cable)
- TI's BlackLink
- TI's GrayLink
- TI's SilverLink
- AVRlink

It also supports some 'virtual' link cables for connection with emulators:
- Virtual TI (VTi)
- (Gtk)TiEmu

%package	-n %{libname}-devel
Summary:	Development related files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description	-n %{libname}-devel
This package contains headers and other necessary files to develop or compile
applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x --enable-static=yes --enable-logging=yes
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std gnulocaledir=${RPM_BUILD_ROOT}%{_datadir}/locale

%find_lang %{name}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*



* Tue Jun 28 2005 Olivier Thauvin <nanardon@mandriva.org> 3.9.2-1mdk
- 3.9.2

* Thu Feb  3 2005 Abel Cheung <deaddog@mandrake.org> 3.8.7-1mdk
- New version

* Sun May 30 2004 Abel Cheung <deaddog@deaddog.org> 3.8.4-1mdk
- New version

* Sat Oct 11 2003 Abel Cheung <deaddog@deaddog.org> 3.7.7-2mdk
- Add missing locale files

* Sat Oct 11 2003 Abel Cheung <deaddog@deaddog.org> 3.7.7-1mdk
- 3.7.7
- License is LGPL
- More verbose description
- mklibname
- Remove unnecessary buildrequires
- Build static library
- Enable logging

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 3.7.6-1mdk
- 3.7.6
- drop useless Prefix tag
- quiet setup
- use %%makeinstall_std macro
- use %%configure macro

* Sat Apr 26 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.7.2-1mdk
- 3.7.2

* Fri Feb 07 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.6.3-1mdk
- 3.6.3

* Thu Dec 19 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.5.3-2mdk
- fix provides

* Thu Dec 19 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.5.3-1mdk
- 3.5.3
- update desc

* Sun Nov 24 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.4.9-1mdk
- 3.4.9

* Tue Sep 03 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.4.5-1mdk
- 1st mdk package
