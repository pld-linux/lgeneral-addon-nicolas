Summary:	LGeneral game - Nicolas campaign for Panzer General
Summary(pl.UTF-8):	Gra Linux General - kampania Nicolas dla gry Panzer General
Name:		lgeneral-addon-nicolas
Version:	1.0
Release:	1
License:	unknown
Group:		Applications/Games
Source0:	http://lgames.sourceforge.net/LGeneral/addons/nicolas.zip
# Source0-md5:	7195a813c33599ff7cd99aeb1b154e40
URL:		http://lgames.sourceforge.net/LGeneral/addons.php
Requires:	lgeneral
Requires:	lgeneral-data-pg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains Nicolas campaign for Panzer General.
This small campaign features the first scenarios of Panzer General but
this time historically more correct, focusing on 'real' order of
battle.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera kampanię Nicolas dla gry Panzer General. Jest to
mała kampania zawierająca pierwsze scenariusze gry Panzer General, ale
tym razem bardziej poprawne historycznie, skupiające się na prawdziwym
przebiegu bitwy.

%prep
%setup -q -n nicolas

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -a gfx maps scenarios units $RPM_BUILD_ROOT%{_datadir}/lgeneral

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/lgeneral/gfx/units/nicolas.bmp
%{_datadir}/lgeneral/maps/nicolas
%{_datadir}/lgeneral/scenarios/nicolas
%{_datadir}/lgeneral/units/nicolas.udb
