Summary: The GNU chess program
Name: gnuchess
Version: 5.07
Release: 14.1%{?dist}
License: GPLv2+
Group: Amusements/Games
URL: ftp://ftp.gnu.org/pub/gnu/chess/
Source: ftp://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz
#Source1: http://ftp.gnu.org/pub/gnu/chess/book_1.01.pgn.gz
# use precompiled book.dat:
Source1: book_1.01.dat.gz
Patch0: gnuchess-5.07-gcc4.patch
Patch1: gnuchess-5.06-bookpath.patch
Patch2: gnuchess-5.07-getline.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides: chessprogram
BuildRequires: flex

%description
The gnuchess package contains the GNU chess program.  By default,
GNU chess uses a curses text-based interface.  Alternatively, GNU chess
can be used in conjunction with the xboard user interface and the X
Window System for play using a graphical chess board.

Install the gnuchess package if you would like to play chess on your
computer.  If you'd like to use a graphical interface with GNU chess, 
you'll also need to install the xboard package and the X Window System.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .gcc
%patch1 -p1 -b .bp
%patch2 -p1 -b .getline
gzip -dc %{SOURCE1} > book/book.dat

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/games/gnuchess $RPM_BUILD_ROOT%{_bindir}
install -m 755 -p src/gnuchess $RPM_BUILD_ROOT%{_bindir}
install -m 644 -p book/book.dat $RPM_BUILD_ROOT%{_var}/lib/games/gnuchess

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(2755,root,games) %{_bindir}/gnuchess
%dir %{_var}/lib/games/gnuchess
%attr(664,root,games) %{_var}/lib/games/gnuchess/book.dat
%doc doc/* COPYING AUTHORS NEWS TODO 

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 5.07-14.1
- Rebuilt for RHEL 6

* Thu Sep 10 2009 Karsten Hopp <karsten@redhat.com> 5.07-14
- fix name collision of getline function

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Chris Ricker <kaboom@oobleck.net> 5.07-11
- Rebuild for GCC 4.3
- Fix license

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 5.07-10
- Bump and rebuild

* Wed Feb 15 2006 Chris Ricker <kaboom@oobleck.net> 5.07-9
- Bump and rebuild

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 5.07-8%{?dist}
- Add dist tag

* Thu May 26 2005 Chris Ricker <kaboom@oobleck.net> 5.07-7
- Patch to compile with gcc4

* Fri May 20 2005 Chris Ricker <kaboom@oobleck.net> 5.07-6
- Update for Fedora Extras
- Copyright -> License
- Don't strip binaries
- Preserve time stamps
- Update BuildRoot
- Drop unapplied patch

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 5.07-5
- Rebuilt for new readline.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 04 2004 Karsten Hopp <karsten@redhat.de> 5.07-3 
- update and rebuild book.dat to fix #122431

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 14 2004 Karsten Hopp <karsten@redhat.de>
- update to 5.07

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 05 2003 Karsten Hopp <karsten@redhat.de> 5.06-1
- update
- precompile book.dat

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild for all arches

* Sat Jul 27 2002 Karsten Hopp <karsten@redhat.de>
- compress SRPM with bzip2 to save some space

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 30 2002 Karsten Hopp <karsten@redhat.de>
- remove obsolete Obsoletes: gnuchess

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jan 25 2002 Karsten Hopp <karsten@redhat.de>
- Fix buffer overflow

* Wed Jan 23 2002 Karsten Hopp <karsten@redhat.de> (5.02-4)
- remove ExcludeArch Alpha

* Wed Dec 19 2001 Karsten Hopp <karsten@redhat.de> 5.02-2
- fix #57687  (book.dat not writable)

* Wed Nov 28 2001 Karsten Hopp <karsten@redhat.de>
- Update gnuchess to 5.02
- added URL (#54612)
- ExcludeArch alpha until the compiler is fixed

* Wed Jul 07 2001 Karsten Hopp <karsten@redhat.de>
- dir /usr/lib/games/gnuchess owned by this package

* Sat Jul 07 2001 Karsten Hopp <karsten@redhat.de>
- add BuildRequires  (#45026)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 10 2000 Bill Nottingham <notting@redhat.com>
- rebuid in new environment

* Mon Apr  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Rebuild with new ncurses
- do NOT update to 5.00 because it sucks: The UI is gone, the print
  tools are gone, and the Makefile contains DOS-specific instructions.

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Sat Aug 14 1999 Bill Nottingham <notting@redhat.com>
- provide chessprogram, don't require xboard

* Fri Jul 29 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0pl80

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Mon Jan 23 1999 Michael Maher <mike@redhat.com>
- changed group name

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- rebuilt for 6.0, cleaned up spec file.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- BuildRoot'ed

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
