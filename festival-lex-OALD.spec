Summary:	British English Lexicon
Summary(pl.UTF-8):	Leksyka brytyjskiej odmiany języka angielskiego
Name:		festival-lex-OALD
Version:	0.4
Release:	4
License:	non-commercial use
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festlex_OALD.tar.gz
# Source0-md5:	45a03689025849d02ec963a5b338ef37
# newer source (2.4) is just repacked, so tarball md5 is different (but contents are equal)
#Source0:	http://www.cstr.ed.ac.uk/downloads/festival/2.4/festlex_OALD.tar.gz
URL:		http://www.cstr.ed.ac.uk/projects/festival/
Requires:	festival-lex-POS
Provides:	festival-lex-english
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an British English Lexicon and letter to sound
rules derived from the Oxford Advanced Learners' Dictionary of Current
English.

%description -l pl.UTF-8
Ten pakiet zawiera leksykę brytyjskiej odmiany języka angielskiego
i zasady konwersji liter na dźwięki opracowane na podstawie Oxford
Advanced Learners' Dictionary of Current English.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/dicts/oald

cd festival/lib/dicts/oald
install oald-0.4.out oald_lts_rules.scm oaldlex.scm \
	$RPM_BUILD_ROOT%{_datadir}/festival/lib/dicts/oald

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/dicts/oald/{COPYING,README.oald}
%{_datadir}/festival/lib/dicts/oald
