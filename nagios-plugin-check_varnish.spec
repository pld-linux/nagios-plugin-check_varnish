%define		plugin	check_varnish
Summary:	Nagios plugin for Varnish
Name:		nagios-plugin-%{plugin}
Version:	1.0
Release:	1
License:	BSD
Group:		Networking
Source0:	http://dl.sourceforge.net/project/varnish/nagios-varnish-plugin/1.0/nagios-varnish-plugin-%{version}.tar.gz
# Source0-md5:	2426831061d0a793eca93321dec0ace8
URL:		http://varnish.projects.linpro.no/
BuildRequires:	varnish-devel
Requires:	nagios-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios plugin to check Varnish.

%prep
%setup -q -n nagios-varnish-plugin-%{version}

cat > nagios.cfg <<'EOF'
# Usage:
# %{plugin}
define command {
	command_name    %{plugin}
	command_line    %{plugindir}/%{plugin} $ARG1$
}
EOF

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -a nagios.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
