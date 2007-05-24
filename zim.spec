%include	/usr/lib/rpm/macros.perl
Summary:	Desktop wiki & notekeeper
Summary(pl.UTF-8):	Wiki na pulpicie i notatnik
Name:		Zim
Version:	0.19
Release:	0.1
License:	GPL or Artistic
Group:		X11/Applications/Editors
Source0:	http://pardus-larus.student.utwente.nl/%7Epardus/downloads/Zim/Zim-%{version}.tar.gz
# Source0-md5:	cfe31ce36602e1f6c203d1a3ef00498c
URL:		http://www.pardus.nl/projects/zim/
BuildRequires:	perl-File-BaseDir
BuildRequires:	perl-File-DesktopEntry
BuildRequires:	perl-File-MimeInfo >= 0.12
BuildRequires:	perl-Gtk2 >= 1.040
BuildRequires:	perl-Gtk2-Spell
BuildRequires:	perl-Gtk2-TrayIcon
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zim is a WYSIWYG text editor written using Gtk2-Perl which aims to
bring the concept of a wiki to your desktop. Every page is saved as a
text file with wiki markup. Pages can contain links to other pages,
and are saved automatically. Creating a new page is as easy as linking
to a non-existing page. Pages are ordered in a hierarchical structure
that gives it the look and feel of an outliner. This tool is intended
to keep track of TODO lists or to serve as a personal scratch book.

%description -l pl.UTF-8
Zim to edytor tekstu WYSIWYG napisany z użyciem biblioteki Gtk2-Perl,
mający na celu przeniesienie idei wiki na pulpit. Każda strona jest
zapisywana jako plik tekstowy ze znacznikami wiki. Strony mogą
zawierać odnośniki do innych stron i są zapisywane automatycznie.
Tworzenie nowej strony jest tak łatwe jak utworzenie odniesienia do
nieistniejącej strony. Strony są uporządkowane w hierarchiczną
strukturę zachowującą się jak szkicownik. To narzędzie jest
przeznaczone do śledzenia list TODO albo własnych notatek.

%prep
%setup -q
chmod -x share/zim/dates.list share/zim/plugins/*
sed -i 's/\r//' share/zim/plugins/Subversion.pl

# We're not running on Win32.  Really :)
rm ./lib/Zim/Win32.pm

%build
%{__perl} Build.PL \
	installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT \
	create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes ExamplePlugin.pl
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*
%{_datadir}/zim
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_mandir}/man[13]/*.[13]*
