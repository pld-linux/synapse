%define		rev	594
#
Summary:	Application launcher
Name:		synapse
Version:	0.2.99
Release:	0.%{rev}.1
License:	GPL v3+
Group:		X11/Applications
Source0:	%{name}-%{version}-r%{rev}.tar.gz
# Source0-md5:	3fcd00e82bc89cd55a9eb3c75f9ce7c7
Patch0:		%{name}-mate.patch
URL:		http://synapse.zeitgeist-project.com/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gtk+3-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	json-glib-devel >= 0.10.0
BuildRequires:	keybinder3-devel
BuildRequires:	libgee-devel >= 0.5.2
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	rest-devel >= 0.7
BuildRequires:	vala >= 0.16.0
BuildRequires:	vala-libgee >= 0.6.4
BuildRequires:	vala-zeitgeist >= 0.9.14
BuildRequires:	zeitgeist-devel >= 0.9.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synapse is a semantic launcher written in Vala that you can use to
start applications as well as find and access relevant documents and
files by making use of the Zeitgeist engine. 

%prep
%setup -q
%patch0 -p1
%{__mkdir} m4

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-librest=yes \
	--enable-zeitgeist=yes
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
