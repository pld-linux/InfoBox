# TODO:
#	- check BRs, R:gtk+2 probably to be removed
#
Summary:	InfoBox - notification tool
Summary(pl):	InfoBox - system powiadomieñ
Name:		InfoBox
Version:	0.9
Release:	0.9
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/fvwm-crystal/%{name}-%{version}.tar.bz2
# Source0-md5:	738a95010d115c6d460e15e8a736b067
URL:		http://developer.berlios.de/project/showfiles.php?group_id=1595
Patch0:		%{name}-doc.patch
Requires:	dbus-X11
Requires:	gtk+2 >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
InfoBox is a notification tool based on specifications from
<http://www.galago-project.org/>. It was inspired by FVWM-Crystal's
InformationBox. It's meant for FVWM-Crystal, but should work with
other window managers.

%description -l pl
InfoBox jest systemem powiadomieñ opartym o specyfikacjê
<http://www.galago-project.org/>. Projektowany by³ dla powiadomieñ
D-BUS, i potrafi je wy¶wietlaæ. Wzorowany jest na InformationBox z
FVWM-Crystal. Przeznaczony by³ dla FVWM-Crystal ale powinien pracowaæ
ze wszystkimi ¶rodowiskami.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--prefix=%{_prefix}

%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/infobox-%{version}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/infoboxd
%{_sysconfdir}/dbus-1/system.d/%{name}d.conf
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service
