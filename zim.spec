Summary:	Desktop wiki & notekeeper
Summary(pl.UTF-8):	Wiki na pulpicie i notatnik
Name:		zim
Version:	0.60
Release:	1
License:	GPLv2+ and LGPLv3+
Group:		X11/Applications/Editors
Source0:	http://zim-wiki.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	f781cefa9f8c669b1a664e03361977e2
URL:		http://zim-wiki.org/
BuildRequires:	python-devel >= 2.5
Requires(post,postun):  shared-mime-info
Requires:	python >= 2.5
Requires:	python-modules-sqlite
Requires:	python-pygobject
Requires:	python-pygtk-gtk
Requires:	python-pyxdg
Requires:	xdg-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zim is a WYSIWYG text editor written using PyGTK which aims to
bring the concept of a wiki to your desktop. Every page is saved as a
text file with wiki markup. Pages can contain links to other pages,
and are saved automatically. Creating a new page is as easy as linking
to a non-existing page. Pages are ordered in a hierarchical structure
that gives it the look and feel of an outliner. This tool is intended
to keep track of TODO lists or to serve as a personal scratch book.

%description -l pl.UTF-8
Zim to edytor tekstu WYSIWYG napisany z użyciem biblioteki PyGTK,
mający na celu przeniesienie idei wiki na pulpit. Każda strona jest
zapisywana jako plik tekstowy ze znacznikami wiki. Strony mogą
zawierać odnośniki do innych stron i są zapisywane automatycznie.
Tworzenie nowej strony jest tak łatwe jak utworzenie odniesienia do
nieistniejącej strony. Strony są uporządkowane w hierarchiczną
strukturę zachowującą się jak szkicownik. To narzędzie jest
przeznaczone do śledzenia list TODO albo własnych notatek.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
    --optimize=2 \
    --root=$RPM_BUILD_ROOT

#%%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database

%postun
%update_desktop_database_postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE.txt CHANGELOG.txt README.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/zim
%{_datadir}/mime/application/*
%{_datadir}/mime/packages/*
%{_datadir}/mime/text/*
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_pixmapsdir}/*
%{_mandir}/man[13]/*.[13]*
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-*.egg-info
