%define debug_package %{nil}

Name:       qt-cross-compile 
Version:    1.1.0
Release:    2
Group:      Development/Languages/Other
License:    GPL-3.0
Summary:    Qt cross compile tools
Url:        https://github.com/psaxioti/qt-cross-compile

BuildArch:  noarch

Requires:   cmake
Requires:   mingw32-cross-gcc
Requires:   mingw32-cross-gcc-c++
Requires:   mingw64-cross-gcc
Requires:   mingw64-cross-gcc-c++
Requires:   mingw32-libqt5-qtbase-devel
Requires:   mingw32-cross-libqt5-qmake
Requires:   mingw64-libqt5-qtbase-devel
Requires:   mingw64-cross-libqt5-qmake
Requires:   msitools

%description
Scripts and toolchain files in order to cross compile with mingw.

%prep
%setup -q -n %{_sourcedir}/%{name}-%{version} -T -D

%build

%install
install -Dm755 find_dlls   %{buildroot}%{_bindir}/find_dlls
install -Dm755 make_msi    %{buildroot}%{_bindir}/make_msi
install -Dm755 qt_install  %{buildroot}%{_bindir}/qt_install

install -Dm644 win32-mingw.cmake %{buildroot}%{_datadir}/%{name}/win32-mingw.cmake
install -Dm644 win64-mingw.cmake %{buildroot}%{_datadir}/%{name}/win64-mingw.cmake

%files
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
