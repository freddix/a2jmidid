Summary:	Daemon for exposing ALSA sequencer applications
Name:		a2jmidid
Version:	8
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://download.gna.org/a2jmidid/%{name}-%{version}.tar.bz2
# Source0-md5:	9cf4edbc3ad2ddeeaf6c8c1791ff3ddd
BuildRequires:	jack-audio-connection-kit-devel
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
daemon for exposing legacy ALSA sequencer applications
in JACK MIDI system.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}"		\
CXXFLAGS="%{rpmcxxflags}"	\
./waf configure -d release --nocache --prefix=%{_prefix}
./waf build -j2 -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install --destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service
%{_mandir}/man1/*.1*

