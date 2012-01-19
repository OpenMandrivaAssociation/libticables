%define oname libticables2

%define major 5
%define libname %mklibname ticables %{major}
%define develname %mklibname -d ticables

Summary:	Library to handle the different TI link cables
Name:		libticables
Version:	1.3.3
Release:	%mkrel 1
Epoch:		1
License:	LGPLv2+
Group:		Communications
Url:		http://tilp.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/tilp/%{oname}-%{version}.tar.bz2
Patch0:		libticables2-buildfix.patch
BuildRequires:	libusb-devel
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n %{libname}
Summary:	Library to handle different TI link cables
Group:		System/Libraries
Provides:   %{name} = %epoch:%version-%release

%description -n %{libname}
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

%package -n %{develname}
Summary:	Development related files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{epoch}:%{version}-%{release}

%description -n %{develname}
This package contains headers and other necessary files to develop or compile
applications that use %{name}.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0

%build
%configure2_5x \
	--enable-logging \
	--disable-rpath \
	--enable-threads=pth

%make

%install
rm -rf %{buildroot}
%makeinstall_std gnulocaledir=%{buildroot}%{_datadir}/locale

%find_lang %{oname}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname} -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
# %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*


%changelog
* Wed Mar 18 2009 Olivier Thauvin <nanardon@mandriva.org> 1:1.2.0-6mdv2009.1
+ Revision: 357079
- resurrect provides libticables
- rebuild

* Sat Feb 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.2.0-4mdv2009.1
+ Revision: 343712
- bump tag
- fix requires on devel subpackage

* Sat Feb 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.2.0-2mdv2009.1
+ Revision: 343694
- move locales to devel subpackage

* Sat Feb 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.2.0-1mdv2009.1
+ Revision: 343665
- remove stupid redefines
- add missing buildrequires on glib2-devel
- nuke rpath
- spec file clean

  + Zombie Ryushu <ryushu@mandriva.org>
    - Increment Epoch
    - Increment Epoch
    - corrected files section

* Thu Feb 05 2009 Zombie Ryushu <ryushu@mandriva.org> 3.9.7-5mdv2009.1
+ Revision: 337902
- Fix Unrevisioned Obsoletes

* Sun Jul 27 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.9.7-5mdv2009.0
+ Revision: 250599
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 25 2008 Emmanuel Andry <eandry@mandriva.org> 3.9.7-3mdv2008.1
+ Revision: 189881
- Fix lib group

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Funda Wang <fundawang@mandriva.org> 3.9.7-2mdv2008.1
+ Revision: 116813
- New license policy
- New devel package policy

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill changelog left by repsys


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-14 16:59:55 (41121)
- 3.9.7

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-07-14 16:45:50 (41120)
- Import libticables

* Tue Jun 28 2005 Olivier Thauvin <nanardon@mandriva.org> 3.9.2-1mdk
- 3.9.2

* Thu Feb 03 2005 Abel Cheung <deaddog@mandrake.org> 3.8.7-1mdk
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

