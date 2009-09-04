%define name    lbdb
%define version 0.35.1
%define release %mkrel 4

Summary:    The Little Brother's Database
Name:       %{name}
Version:    %{version}
Release:    %{release}
Source0:    http://www.spinnaker.de/debian/%{name}_%{version}.tar.bz2
License:  GPL
Group:      Databases
URL:        http://www.spinnaker.de/lbdb/
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   mawk
# need these so that all the modules get built
BuildRequires: abook yp-tools finger gnupg perl libvformat-devel
Obsoletes: %{name}-mutt
Provides: %{name}-mutt

%description 
This package was inspired by the Big Brother Database package
available for various Emacs mailers, and by Brandon Long's "external
query" patch for the Mutt mail user agent. (Note that this patch has
been incorporated into the main-line mutt versions as of mutt 0.93.)

The package doesn't use any formal database libraries or languages,
although it should be quite easy to extend it to use, e.g., an
installed PostgreSQL server as it's back end.

lbdb can be used to extract e-mail addresses from your incoming mail
stream into some kind of address-book which you can access via mutt's
query function.

Install this package if you are using mutt, an email program, and
want to get easy access to your collection of email addresses.

%package abook
Summary:    The Little Brother's Database - abook modules
Group:      Databases
Requires:   %name abook

%description abook
This lbdb module uses the program abook, a text based address book 
application to search for addresses.

%package bbdb
Summary:    The Little Brother's Database - BBDB module
Group:      Databases
Requires:   %name emacs

%description bbdb
This lbdb module searches for addresses in your (X)Emacs BBDBi
(big brother database). It doesn't access ~/.bbdb directly (yet) but calls
(x)emacs with a special mode to get the information (so don't expect too much
performance in this module). You can configure the EMACS variable to tell this
module which emacsen to use. Otherwise it will fall back to emacs or xemacs.

%package finger
Summary:    The Little Brother's Database - Finger module
Group:      Databases
Requires:   %name finger

%description finger
This lbdb module will use finger to find out something more about a person.
The list of hosts do be asked is configurable.

%package gpg
Summary:    The Little Brother's Database - Gpg module
Group:      Databases
Requires:   %name gnupg

%description gpg
This lbdb module scans your GnuPG public key ring for data.  It uses the
gpg program to get the data.

%package ldap 
Summary:    The Little Brother's Database - Ldap module
Group:      Databases
Requires:   %name perl-ldap 

%description ldap 
This lbdb module queries an LDAP server using the Net::LDAP Perl modules
from CPAN. It can be configured using an external resource file (for more
details please refer to the mutt_ldap_query(1) manual page).

%package palm
Summary:    The Little Brother's Database - Palm module
Group:      Databases
Requires:   %name perl-p5-Palm

%description palm
This lbdb module searches the Palm address database using the Palm::PDB and
Palm::Address Perl modules from CPAN. It searches in the variable
$PALM_ADDRESS_DATABASE or if this isn't set in
$HOME/.jpilot/AddressDB.pdb.

%package yppasswd
Summary:    The Little Brother's Database - yppasswd module
Group:      Databases
Requires:   %name yp-tools

%description yppasswd
This lbdb module searches for matching entries in the NIS password database
using the command ``ypcat passwd''.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%configure

%make

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_bindir}/lbdb-fetchaddr
%{_bindir}/lbdbq
%{_bindir}/lbdb_dotlock
%{_bindir}/nodelist2lbdb
%{_libdir}/lbdb_bbdb_query.el
%{_libdir}/lbdb_lib
%{_libdir}/lbdb-munge
%{_libdir}/fetchaddr
%{_libdir}/munge
%{_libdir}/munge-keeporder
%{_libdir}/m_fido
%{_libdir}/m_getent
%{_libdir}/m_gnomecard
%{_libdir}/m_inmail
%{_libdir}/m_muttalias
%{_libdir}/m_passwd
%{_libdir}/m_pine
%{_libdir}/m_wanderlust
%{_libdir}/qpto8bit
%{_libdir}/m_vcf
%{_libdir}/vcquery
%{_mandir}/man1/lbdb-fetchaddr.1.*
%{_mandir}/man1/lbdbq.1.*
%{_mandir}/man1/lbdb_dotlock.1.*
%{_mandir}/man1/nodelist2lbdb.1.*
%doc COPYING README TODO
%config(noreplace) %{_sysconfdir}/lbdb.rc

%files abook
%defattr(-,root,root)
%_libdir/m_abook

%files bbdb
%defattr(-,root,root)
%_libdir/m_bbdb
%_libdir/lbdb_bbdb_query.el

%files finger
%defattr(-,root,root)
%_libdir/m_finger

%files gpg
%defattr(-,root,root)
%_libdir/m_gpg

%files ldap
%defattr(-,root,root)
%_libdir/m_ldap
# yes it has a stupid name
%_libdir/mutt_ldap_query
%{_mandir}/man1/mutt_ldap_query.1.*
%config(noreplace) %{_sysconfdir}/lbdb_ldap.rc

%files palm
%defattr(-,root,root)
%_libdir/m_palm
%_libdir/palm_lsaddr

%files yppasswd
%defattr(-,root,root)
%_libdir/m_yppasswd

