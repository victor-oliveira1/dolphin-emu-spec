%define  timestamp %(date -u +%%Y%%m%%d%%H%%M%%S)
%define  debug_package %{nil}

Name:       dolphin-emu
Summary:    A GameCube and Wii Emulator
Version:    %{timestamp}
Release:    git%{?dist}
Group:      System/Emulators/Other
License:    GPL-2.0
URL:        https://%{name}.org/
BuildArch:	x86_64 amd64

BuildRequires:	git
BuildRequires:  mesa-libGL-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libevdev-devel
BuildRequires:  systemd-devel
BuildRequires:  pugixml-devel
BuildRequires:  enet-devel
BuildRequires:  zlib-devel
BuildRequires:  lzo-devel
BuildRequires:  libpng-devel
BuildRequires:  libusb-devel
BuildRequires:  SFML-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  mbedtls-devel
BuildRequires:  libcurl-devel
BuildRequires:  hidapi-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  qt5-devel

%description
Dolphin-emu is an emulator for two Nintendo video game consoles, GameCube and the Wii.
It allows PC gamers to enjoy games for these two consoles in full HD with several enhancements such as compatibility with all PC controllers, turbo speed, networked multiplayer, and more.
Most games run perfectly or with minor bugs.

%prep
%{__git} clone --depth 1 https://github.com/%{name}/dolphin.git .

%build
%cmake . -DBUILD_SHARED_LIBS:BOOL=OFF -DUSE_SHARED_ENET=ON
%make_build

%install
%make_install

# Removing discord development stuff
rm -rf %{buildroot}%{_libdir}/*
rm -rf %{buildroot}%{_includedir}/*

%files
%license license.txt
%doc Readme.md
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun Sep 30 2018 Victor Oliveira <victor.oliveira@gmx.com>
- Complete rewrite of spec file according to RPM Packaging guide
