Summary:	Application launcher
Name:		synapse
Version:	0.2.10
Release:	0.1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://launchpad.net/synapse-project/0.2/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	de0e05350f8a7d557092489baf14d039
URL:		http://synapse.zeitgeist-project.com/
# The dependencies are listed in Makefile
BuildRequires:	vala >= 1:0.15.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synapse is a semantic launcher written in Vala that you can use to
start applications as well as find and access relevant documents and
files by making use of the Zeitgeist engine. 

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%files
%defattr(644,root,root,755)
