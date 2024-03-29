#
# Conditional build:
%bcond_without	appindicator	# build without appindicator support
%bcond_with	zeitgeist	# build with zeitgeist support (causes stability issues)

Summary:	Application launcher
Name:		synapse
Version:	0.2.99.4
Release:	2
License:	GPL v3+
Group:		X11/Applications
Source0:	https://launchpad.net/synapse-project/0.3/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	38105c87200d82cf2066fb70cc9af59f
Patch0:		%{name}-mate.patch
Patch1:		ayatana-indicator.patch
URL:		https://launchpad.net/synapse-project
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gtk+3-devel
BuildRequires:	json-glib-devel >= 0.10.0
BuildRequires:	keybinder3-devel
%{?with_appindicator:BuildRequires:	libayatana-appindicator-gtk3-devel}
BuildRequires:	libgee-devel >= 0.5.2
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	rest-devel >= 0.7
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 0.16.0
%{?with_appindicator:BuildRequires:	vala-libayatana-appindicator-gtk3}
BuildRequires:	vala-libgee >= 0.6.4
%if %{with zeitgeist}
BuildRequires:	vala-zeitgeist >= 0.9.14
BuildRequires:	xz
BuildRequires:	zeitgeist-devel >= 0.9.14
%endif
Requires:	glib2 >= 1:2.28.0
Requires:	json-glib >= 0.10.0
Requires:	libgee >= 0.5.2
Requires:	rest >= 0.7
%if %{with zeitgeist}
Requires:	zeitgeist-libs >= 0.9.14
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synapse is a semantic launcher written in Vala that you can use to
start applications as well as find and access relevant documents and
files by making use of the Zeitgeist engine.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-librest=yes \
	%{__enable_disable appindicator indicator} \
	%{__enable_disable zeitgeist}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/synapse
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_desktopdir}/*.desktop
%{_mandir}/man1/synapse.*
