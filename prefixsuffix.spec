Summary:	PrefixSuffix - batch renaming of files
Summary(pl.UTF-8):	PrefixSuffix - zbiorcza zmiana nazw plików
Name:		prefixsuffix
Version:	0.6.6
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/prefixsuffix/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	1c8b90091be8c8ce37216edd9c2c7544
URL:		https://github.com/murraycu/prefixsuffix
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	gtkmm3-devel >= 3.0
BuildRequires:	intltool >= 0.35
BuildRequires:	libstdc++-devel
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PrefixSuffix is a GUI application that renames batches of files by
changing the beginning or end of their names.

%description -l pl.UTF-8
PrefixSuffix to aplikacja z graficznym interfejsem użytkownika służąca
do zmiany nazw wielu plików naraz poprzez zmianę początku lub końca
ich nazwy.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/prefixsuffix
%{_desktopdir}/prefixsuffix.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.prefixsuffix.gschema.xml
%{_pixmapsdir}/prefixsuffix.png
%{_datadir}/prefixsuffix
