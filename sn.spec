# TODO
# - inetd or tcpserver (+ news user?)
# - makefile patch for cc/cflags/destdir
Summary:	The sn NNTP Server
Name:		sn
Version:	0.3.8
Release:	0.1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://patrik.infa.fi/sn/files/%{name}-%{version}.tar.bz2
# Source0-md5:	157276c0ef8adff5031b0d3950b5a32f
URL:		http://patrik.infa.fi/sn/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sn is a small news system for small sites serving perhaps a few dozen
newsgroups, and with a slow connection to the internet. It is similar
to Leafnode. The target user is a home or SOHO with a single modem
connection to the Internet, maybe running IP masq or similar, and
serving a few workstations.

%prep
%setup -q

%build
%{__make} cc-flags \
	PREFIX=%{_prefix}

echo %{rpmcflags} >> cc-flags

%{__make} -C lib libstuff.a \
	CC="%{__cc}" \
	LD="%{__cc}" \

%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL.notes INSTALL.notes2 INSTALL.run INSTALL.upgrade INTERNALS README* THANKS TODO
%attr(755,root,root) %{_sbindir}/SNHELLO
%attr(755,root,root) %{_sbindir}/SNPOST
%attr(755,root,root) %{_sbindir}/dot-outgoing.ex
%attr(755,root,root) %{_sbindir}/sncancel
%attr(755,root,root) %{_sbindir}/sncat
%attr(755,root,root) %{_sbindir}/sndelgroup
%attr(755,root,root) %{_sbindir}/sndumpdb
%attr(755,root,root) %{_sbindir}/snexpire
%attr(755,root,root) %{_sbindir}/snfetch
%attr(755,root,root) %{_sbindir}/snget
%attr(755,root,root) %{_sbindir}/sngetd
%attr(755,root,root) %{_sbindir}/snlockf
%attr(755,root,root) %{_sbindir}/snmail
%attr(755,root,root) %{_sbindir}/snnewgroup
%attr(755,root,root) %{_sbindir}/snntpd
%attr(755,root,root) %{_sbindir}/snprimedb
%attr(755,root,root) %{_sbindir}/snscan
%attr(755,root,root) %{_sbindir}/snsend
%attr(755,root,root) %{_sbindir}/snsplit
%attr(755,root,root) %{_sbindir}/snstore
%{_mandir}/man8/sn.8*
%{_mandir}/man8/sncancel.8*
%{_mandir}/man8/sncat.8*
%{_mandir}/man8/sndelgroup.8*
%{_mandir}/man8/sndumpdb.8*
%{_mandir}/man8/snexpire.8*
%{_mandir}/man8/snfetch.8*
%{_mandir}/man8/snget.8*
%{_mandir}/man8/sngetd.8
%{_mandir}/man8/snmail.8*
%{_mandir}/man8/snnewgroup.8*
%{_mandir}/man8/snntpd.8*
%{_mandir}/man8/snprimedb.8*
%{_mandir}/man8/snscan.8*
%{_mandir}/man8/snsend.8*
%{_mandir}/man8/snsplit.8*
%{_mandir}/man8/snstore.8*
