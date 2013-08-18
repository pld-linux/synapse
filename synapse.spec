Summary:	Application launcher
Name:		synapse
Version:	0.2.10
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://launchpad.net/synapse-project/0.2/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	ac1c075c01f1c179f32fd6651bd184f8
Patch0:		%{name}-mate.patch
URL:		http://synapse.zeitgeist-project.com/
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtkhotkey-devel >= 0.2.1
BuildRequires:	json-glib-devel >= 0.10.0
BuildRequires:	libgee0.6-devel >= 0.5.2
BuildRequires:	libnotify-devel
BuildRequires:	libunique-devel >= 1.0
BuildRequires:	rest-devel
BuildRequires:	vala >= 0.14.0
BuildRequires:	vala-libgee >= 0.6.4
BuildRequires:	vala-zeitgeist >= 0.3.18
BuildRequires:	zeitgeist-devel >= 0.3.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synapse is a semantic launcher written in Vala that you can use to
start applications as well as find and access relevant documents and
files by making use of the Zeitgeist engine. 

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
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
