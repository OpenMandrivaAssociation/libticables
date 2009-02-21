%define oname libticables2

%define major 1
%define libname %mklibname ticables %{major}
%define develname %mklibname -d ticables

Summary:	Library to handle the different TI link cables
Name:		libticables
Version:	1.2.0
Release:	%mkrel 3
Epoch:		1
License:	LGPLv2+
Group:		Communications
Url:		http://tilp.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/tilp/%{oname}-%{version}.tar.bz2
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
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
