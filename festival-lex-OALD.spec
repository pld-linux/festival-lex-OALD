Summary:	British English Lexicon
Summary(pl):	Leksyka brytyjskiej odmiany jêzyka angielskiego
Name:		festival-lex-OALD
Version:	0.4
Release:	3
License:	non-commercial use
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festlex_OALD.tar.gz
# Source0-md5:	45a03689025849d02ec963a5b338ef37
Requires:	festival-lex-POS
Provides:	festival-lex-english
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an British English Lexicon and letter to sound
rules derived from the Oxford Advanced Learners' Dictionary of Current
English.

%description -l pl
Ten pakiet zawiera leksykê brytyjskiej odmiany jêzyka angielskiego
i zasady konwersji liter na d¼wiêki opracowane na podstawie Oxford
Advanced Learners' Dictionary of Current English.

%prep
%setup -q -c %{name}-%{version}

%build

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
%doc festival/lib/dicts/oald/COPYING
%doc festival/lib/dicts/oald/README.oald
%{_datadir}/festival/lib/dicts/oald
