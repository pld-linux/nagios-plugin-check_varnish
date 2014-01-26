%define		plugin	check_varnish
Summary:	Nagios plugin to monitor Varnish instances
Name:		nagios-plugin-%{plugin}
Version:	1.1
Release:	1
License:	BSD
Group:		Networking
Source0:	http://repo.varnish-cache.org/source/varnish-nagios-%{version}.tar.gz
# Source0-md5:	d9a5477f9143187ffe6314ddecb03015
Source1:	%{plugin}.cfg
URL:		http://www.varnish-cache.org/
BuildRequires:	pkgconfig
BuildRequires:	varnish-devel
Requires:	nagios-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios plugin to check Varnish.

%prep
%setup -qn varnish-nagios-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
