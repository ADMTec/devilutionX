%define debug_package %{nil}

Name:		devilutionx
Version:	0.5.0
Release:	1%{?dist}
Summary:	Diablo I engine for modern operating systems

License:	Unlicensed
URL:		https://github.com/Vitexus/devilutionX
Source0:	https://github.com/Vitexus/devilutionX/archive/%{version}.tar.gz
Source1:	devilutionx.desktop

BuildRequires:	cmake gcc gcc-c++ libstdc++-static glibc desktop-file-utils
BuildRequires:  glibc-devel SDL2-devel SDL2_ttf-devel SDL2_mixer-devel libsodium-devel libasan
Requires:	SDL2_ttf SDL2_mixer libsodium

%description
Diablo I devolved - magic behind the 1996 computer game
Note: Devilution requires an original copy of diabdat.mpq. None of the Diablo 1 game assets are provided by this package! 

%prep
%setup -q -n devilutionX-%{version}

%build
mkdir -p build
rm -rf build/*
cd build
export CXXFLAGS="-DTTF_FONT_PATH=\"/usr/share/fonts/truetype/CharisSILB.ttf\""
cmake ..
cmake --build .
cd ..

%install
cd build
make INSTALL_ROOT=%{buildroot}
cd ..
mkdir -p %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -p -D -m644 Packaging/resources/16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -D -m644 Packaging/resources/Diablo_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -D -m644 Packaging/resources/Diablo_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

install -m 755 build/devilutionx %{buildroot}%{_bindir}/%{name}
desktop-file-install --remove-category="Qt" --dir=%{buildroot}%{_datadir}/applications %{SOURCE1} 

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/fonts/truetype/CharisSILB.ttf
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%post
# print info
cat <<BANNER
-------------------------------------------------------------------------

Thank you for trying devilutionx!

Please make sure that you have the game assets (specifically diabdat.mpq)
of Diablo I at hand!

The game assets need to be in ~/.local/share/diasurgical/devilution.
This directory should be created automatically on launch by the binary.

However, you can do this step manually by executing:

	mkdir -p ~/.local/share/diasurgical/devilution

------------------------------------------------------------------------
BANNER



%changelog
* Tue Apr 16 2019 Michael Seevogel <michael (at) michaelseevogel.de> - 0.3.1-2
- Updated packaging files
- added icon to desktop file

* Mon Apr 15 2019 Michael Seevogel <michael (at) michaelseevogel.de> - 0.3.1-1
- Initial release for Fedora
