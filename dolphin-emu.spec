Name:       dolphin-emu
Summary:    Dolphin Emulator
Version:    5.0
Release:    %(date +%s)
Group:      System/Emulators/Other
License:    GPL-2.0
URL:        https://dolphin-emu.org/
BuildArch:  x86_64 armv7l aarch64

%define  debug_package %{nil}

BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)

%if 0%{?fedora}
BuildRequires:  libusb-devel
BuildRequires:  lzo-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  openal-soft-devel
BuildRequires:  mbedtls-devel
BuildRequires:  SDL2-devel
BuildRequires:  SFML-devel
BuildRequires:  SOIL-devel
BuildRequires:  soundtouch-devel
BuildRequires:  systemd-devel
BuildRequires:  libevdev-devel
BuildRequires:	libSM-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	qt5-devel
%endif

%description
Dolphin is an emulator for two Nintendo video game consoles, GameCube and the Wii.
It allows PC gamers to enjoy games for these two consoles in full HD with several
enhancements such as compatibility with all PC controllers, turbo speed,
networked multiplayer, and more.
Most games run perfectly or with minor bugs.

%prep
curl -Lo master.zip https://github.com/dolphin-emu/dolphin/archive/master.zip
unzip master.zip
rm -rf master.zip
mv dolphin-master/* ./
rm -rf dolphin-master

%build
export CCFLAGS='%{optflags}'
cmake . -DCMAKE_INSTALL_PREFIX=/usr -DENABLE_WX=OFF
make %{?_smp_mflags}

%install
export CCFLAGS='%{optflags}'
make %{?_smp_mflags} install DESTDIR="%{?buildroot}"

%files
%defattr(-,root,root,-)
%doc license.txt Readme.md
%{_bindir}/*
%{_datadir}/*
%{_mandir}/*

%clean
rm -rf %{buildroot}

%changelog
