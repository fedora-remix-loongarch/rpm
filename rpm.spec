%define with_python_version     2.5%{nil}
%define with_apidocs            1%{nil}

%define rpmhome /usr/lib/rpm

Summary: The RPM package management system
Name: rpm
Version: 4.4.2.3
Release: 3%{?dist}
Group: System Environment/Base
Url: http://www.rpm.org/
Source: http://rpm.org/releases/rpm-4.4.x/%{name}-%{version}.tar.gz
Patch1: rpm-4.4.2.3-prereq.patch
Patch2: rpm-4.4.2-ghost-conflicts.patch
Patch3: rpm-4.4.2-trust.patch
Patch4: rpm-4.4.2.2-devel-autodep.patch
Patch5: rpm-4.4.2-rpmfc-skip.patch
Patch6: rpm-4.4.2.2-matchpathcon.patch
Patch7: rpm-4.4.2.1-no-popt.patch
Patch8: rpm-4.4.2.3-nss.patch
Patch9: rpm-4.4.2.2-autofoo.patch
Patch10: rpm-4.4.2.2-pkgconfig-path.patch
Patch11: rpm-4.4.2.3-queryformat-arch.patch
Patch12: rpm-4.4.2.3-no-order-rescan-limit.patch
Patch13: rpm-4.4.2.3-fix-find-requires.patch
Patch14: rpm-4.4.2.3-addsignature.patch
Patch15: rpm-4.4.2.3-bzip-uncompress.patch
Patch16: rpm-4.4.2.3-cloexec.patch
Patch17: rpm-4.4.2.3-find-lang-man.patch
Patch18: rpm-4.4.2.3-headerload-err.patch
Patch19: rpm-4.4.2.3-nodirtokens.patch
Patch20: rpm-4.4.2.3-no-jar-exclude.patch
Patch21: rpm-4.4.2.3-no-rdtsc.patch
Patch22: rpm-4.4.2.3-proxy.patch
Patch23: rpm-4.4.2.3-sigpipe.patch
Patch50: rpm-4.4.2.3-rc1-sparc-mcpu.patch

# XXX Beware, this is one murky license, partially GPL/LGPL dual-licensed
# and several different components with their own licenses included...
# SourceLicense: (GPLv2+ and LGPLv2+ with exceptions) and BSD and MIT and Sleepycat
License: GPLv2+

Requires(post): coreutils
Requires: popt >= 1.10.2.1
Requires: crontabs
Requires: logrotate

# XXX for autoreconf due to popt removal
BuildRequires: autoconf automake libtool
# XXX generally assumed to be installed but make it explicit as rpm
# is a bit special...
BuildRequires: redhat-rpm-config
BuildRequires: gawk
BuildRequires: elfutils-devel >= 0.112
BuildRequires: elfutils-libelf-devel-static
BuildRequires: readline-devel zlib-devel
BuildRequires: nss-devel
# The popt version here just document an older known-good version, not
# necessarily accurate
BuildRequires: popt-devel >= 1.10.2 
BuildRequires: sqlite-devel
BuildRequires: gettext-devel
BuildRequires: libselinux-devel
BuildRequires: ncurses-devel
BuildRequires: bzip2-devel >= 0.9.0c-2
BuildRequires: python-devel >= %{with_python_version}

BuildConflicts: neon-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package libs
Summary:  Libraries for manipulating RPM packages
Group: Development/Libraries
License: GPLv2+ and LGPLv2+ with exceptions
Requires: rpm = %{version}-%{release}

%description libs
This package contains the RPM shared libraries.

%package devel
Summary:  Development files for manipulating RPM packages
Group: Development/Libraries
License: GPLv2+ and LGPLv2+ with exceptions
Requires: rpm = %{version}-%{release}
Requires: nss-devel 
Requires: sqlite-devel
Requires: libselinux-devel
Requires: elfutils-libelf-devel
Requires: popt-devel

%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

%package build
Summary: Scripts and executable programs used to build packages
Group: Development/Tools
Requires: rpm = %{version}-%{release}
Requires: elfutils >= 0.128 binutils
Requires: findutils sed grep gawk diffutils file patch >= 2.5
Requires: zip gzip bzip2 cpio

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

%package python
Summary: Python bindings for apps which will manipulate RPM packages
Group: Development/Libraries
Requires: rpm = %{version}-%{release}

%description python
The rpm-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python
programs that will manipulate RPM packages and databases.

%if %{with_apidocs}
%package apidocs
Summary: API documentation for RPM libraries
Group: Documentation
BuildRequires: doxygen

%description apidocs
This package contains API documentation for developing applications
that will manipulate RPM packages and databases.
%endif

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .prereq
%patch2 -p1 -b .ghostconflicts
%patch3 -p1 -b .trust
%patch4 -p1 -b .develdeps
%patch5 -p1 -b .fcskip
%patch6 -p1 -b .matchpathcon
%patch7 -p1 -b .no-popt
%patch8 -p1 -b .nss
%patch9 -p1 -b .autofoo
%patch10 -p1 -b .pkgconfig-path
%patch11 -p1 -b .qfmt-arch
%patch12 -p1 -b .no-order-limit
%patch13 -p1 -b .requires
%patch14 -p1 -b .addsig
%patch15 -p1 -b .bzip
%patch16 -p1 -b .cloexec
%patch17 -p1 -b .findlang
%patch18 -p1 -b .hdrload
%patch19 -p1 -b .nodirtoken
%patch20 -p1 -b .jar
%patch21 -p1 -b .nordtsc
%patch22 -p1 -b .proxy
%patch23 -p1 -b .sigpipe

%patch50 -p1 -b .sparc-mcpu

# force external popt
rm -rf popt/

# XXX for popt removal 
autoreconf

%build

# XXX pull in updated config.guess and config.sub as done by %%configure
# which cannot be used to build rpm itself due to makefile brokenness
for i in $(find . -name config.guess -o -name config.sub) ; do 
    [ -f /usr/lib/rpm/redhat/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/lib/rpm/redhat/$(basename $i) $i 
done 

# XXX rpm 4.4.2.1 can't be built with %%configure due to makefile brokenness
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
./configure --prefix=%{_usr} \
            --sysconfdir=%{_sysconfdir} \
            --localstatedir=%{_var} \
            --infodir=%{_infodir} \
            --mandir=%{_mandir} \
            --with-python=%{with_python_version} \
            --enable-posixmutexes

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR="$RPM_BUILD_ROOT" install

# Clean up useless symlinks
for i in rpme rpmi rpmu; do
    rm -f $RPM_BUILD_ROOT%{_bindir}/$i
done

# Save list of packages through cron
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily
install -m 755 scripts/rpm.daily ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/rpm

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -m 644 scripts/rpm.log ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/rpm

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm

mkdir -p $RPM_BUILD_ROOT/var/spool/repackage
mkdir -p $RPM_BUILD_ROOT/var/lib/rpm
for dbi in \
        Basenames Conflictname Dirnames Group Installtid Name Packages \
        Providename Provideversion Requirename Requireversion Triggername \
        Filemd5s Pubkeys Sha1header Sigmd5 \
        __db.001 __db.002 __db.003 __db.004 __db.005 __db.006 __db.007 \
        __db.008 __db.009
do
    touch $RPM_BUILD_ROOT/var/lib/rpm/$dbi
done

%find_lang %{name}

# copy db and file/libmagic license info to distinct names
cp -p db/LICENSE LICENSE-bdb
cp -p file/LEGAL.NOTICE LEGAL.NOTICE-file
cp -p lua/COPYRIGHT COPYRIGHT-lua

# Get rid of unpackaged files
{ cd $RPM_BUILD_ROOT
  rm -f .%{_libdir}/lib*.{a,la}
  rm -f .%{rpmhome}/{Specfile.pm,cpanflute,cpanflute2,rpmdiff,rpmdiff.cgi,sql.prov,sql.req,tcl.req,rpm.*}
  rm -rf .%{_mandir}/{fr,ko}
  rm -f .%{_libdir}/python%{with_python_version}/site-packages/*.{a,la}
  rm -f .%{_libdir}/python%{with_python_version}/site-packages/rpm/*.{a,la}
  rm -f .%{_libdir}/python%{with_python_version}/site-packages/rpmdb/*.{a,la}
}

find $RPM_BUILD_ROOT/%{_libdir}/python%{with_python_version} -name "*.py"|xargs chmod 644

%clean
rm -rf $RPM_BUILD_ROOT

%post
# XXX Detect (and remove) incompatible dbenv files during upgrade.
# XXX Removing dbenv files in %%post opens a lock race window, a tolerable
# XXX risk compared to the support issues involved with upgrading Berkeley DB.
[ -w /var/lib/rpm/__db.001 ] &&
/usr/lib/rpm/rpmdb_stat -CA -h /var/lib/rpm 2>&1 |
grep "db_stat: Program version ... doesn't match environment version" 2>&1 > /dev/null &&
        rm -f /var/lib/rpm/__db*
                                                                                
exit 0

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%define rpmdbattr %attr(0644, root, root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace)

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGES GROUPS COPYING LICENSE-bdb LEGAL.NOTICE-file CREDITS ChangeLog
%doc COPYRIGHT-lua doc/manual/[a-z]*

%{_sysconfdir}/cron.daily/rpm
%config(noreplace,missingok)    %{_sysconfdir}/logrotate.d/rpm
%dir                            %{_sysconfdir}/rpm
# XXX teach rpm to skip .rpmnew etc first...
#%ghost %config(noreplace,missingok)   %{_sysconfdir}/rpm/platform
#%ghost %config(noreplace,missingok)   %{_sysconfdir}/rpm/macros.tscolor

%dir /var/lib/rpm
%rpmdbattr /var/lib/rpm/*
%dir /var/spool/repackage
%dir %{rpmhome}

/bin/rpm
%{_bindir}/rpm2cpio
%{_bindir}/gendiff
%{_bindir}/rpmdb
%{_bindir}/rpmsign
%{_bindir}/rpmquery
%{_bindir}/rpmverify

%{rpmhome}/config.guess
%{rpmhome}/config.sub
%{rpmhome}/convertrpmrc.sh
%{rpmhome}/freshen.sh
%{rpmhome}/mkinstalldirs
%{rpmhome}/rpm2cpio.sh
%{rpmhome}/rpm[deiukqv]
%{rpmhome}/tgpg
%{rpmhome}/rpmdb_*
%{rpmhome}/rpmfile

%{rpmhome}/macros
%{rpmhome}/rpmpopt*
%{rpmhome}/rpmrc

%ifarch i386 i486 i586 i686 athlon geode pentium3 pentium4 x86_64
%{rpmhome}/i[3456]86*
%{rpmhome}/athlon*
%{rpmhome}/geode*
%{rpmhome}/pentium*
%endif
%ifarch alpha alphaev5 alphaev56 alphapca56 alphaev6 alphaev67
%{rpmhome}/alpha*
%endif
%ifarch sparc sparcv8 sparcv9 sparc64
%{rpmhome}/sparc*
%endif
%ifarch ia64
%{rpmhome}/ia64*
%endif
%ifarch powerpc ppc ppciseries ppcpseries ppcmac ppc64
%{rpmhome}/ppc*
%endif
%ifarch s390 s390x
%{rpmhome}/s390*
%endif
%ifarch %{arm}
%{rpmhome}/arm*
%endif
%ifarch mips mipsel
%{rpmhome}/mips*
%endif
%ifarch x86_64
%{rpmhome}/x86_64*
%{rpmhome}/amd64*
%{rpmhome}/ia32e*
%endif
%{rpmhome}/noarch*

%{_mandir}/man1/gendiff.1*
%{_mandir}/man8/rpm.8*
%{_mandir}/man8/rpm2cpio.8*

# XXX this places translated manuals to wrong package wrt eg rpmbuild
%lang(ja) %{_mandir}/ja/man[18]/*.[18]*
%lang(pl) %{_mandir}/pl/man[18]/*.[18]*
%lang(ru) %{_mandir}/ru/man[18]/*.[18]*
%lang(sk) %{_mandir}/sk/man[18]/*.[18]*

%files libs
%defattr(-,root,root)
%{_libdir}/librpm*-*.so

%files build
%defattr(-,root,root)
%{_usrsrc}/redhat
%{_bindir}/rpmbuild
%{rpmhome}/brp-*
%{rpmhome}/check-buildroot
%{rpmhome}/check-files
%{rpmhome}/check-prereqs
%{rpmhome}/check-rpaths*
%{rpmhome}/cross-build
%{rpmhome}/debugedit
%{rpmhome}/find-debuginfo.sh
%{rpmhome}/find-lang.sh
%{rpmhome}/find-prov.pl
%{rpmhome}/find-provides
%{rpmhome}/find-provides.perl
%{rpmhome}/find-req.pl
%{rpmhome}/find-requires
%{rpmhome}/find-requires.perl
%{rpmhome}/get_magic.pl
%{rpmhome}/getpo.sh
%{rpmhome}/http.req
%{rpmhome}/javadeps
%{rpmhome}/magic.prov
%{rpmhome}/magic.req
%{rpmhome}/mono-find-provides
%{rpmhome}/mono-find-requires
%{rpmhome}/osgideps.pl
%{rpmhome}/perldeps.pl
%{rpmhome}/perl.prov
%{rpmhome}/perl.req
%{rpmhome}/pythondeps.sh
%{rpmhome}/rpm[bt]
%{rpmhome}/rpmdeps
%{rpmhome}/trpm
%{rpmhome}/u_pkg.sh
%{rpmhome}/vpkg-provides.sh
%{rpmhome}/vpkg-provides2.sh

%{rpmhome}/config.site
%{rpmhome}/magic
%{rpmhome}/magic.mgc
%{rpmhome}/magic.mime
%{rpmhome}/magic.mime.mgc

%{_mandir}/man8/rpmbuild.8*
%{_mandir}/man8/rpmdeps.8*

%files python
%defattr(-,root,root)
%{_libdir}/python%{with_python_version}/site-packages/rpm

%files devel
%defattr(-,root,root)
%{_includedir}/rpm
%{_libdir}/librp*[a-z].so
%{_mandir}/man8/rpmcache.8*
%{_mandir}/man8/rpmgraph.8*
%{rpmhome}/rpmcache
%{_bindir}/rpmgraph

%if %{with_apidocs}
%files apidocs
%defattr(-,root,root)
%doc apidocs
%endif

%changelog
* Fri Dec 12 2008 Panu Matilainen <pmatilai@redhat.com> 4.4.2.3-3
- abort transaction on python callback crash
- package signing fixes (#442761, #463482)
- fix uncompress macro wrt bzip
- force cloexec all open descriptors on scriptlet execution
- make find-lang --with-man brp-compress friendly
- handle headerLoad() failure in rpmReadHeader() correctly
- fix --nodirtokens build option (#462391)
- drop no longer necessary jar.so.debug kludge (#442264)
- remove buggy, i386-specific RDTSC timing code (#435309)
- fix retrieval of multiple package through a proxy (#450205)
- ensure default SIGPIPE handler for --pipe (#444389)

* Fri Apr 18 2008 Bill Nottingham <notting@redhat.com> 4.4.2.3-2
- fix find-requires (#443015)

* Tue Apr 01 2008 Panu Matilainen <pmatilai@redhat.com> 4.4.2.3-1
- update to 4.4.2.3 final
- resolves #436770, #431009, #435620, #433188, #430428, #432496
- adjust dependency printing wrt prereq (#431721)
- rediff nss patch to fix fuzz brokenness

* Sun Mar 30 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.2.3-0.5.rc1
- actually apply sparc optflags patch

* Thu Mar 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.2.3-0.4.rc1
- Fix sparc optflags

* Wed Mar 12 2008 Panu Matilainen <pmatilai@redhat.com> 4.4.2.3-0.3.rc1
- Continue ordering loop elimination as long as progress is made (#437041)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.4.2.3-0.2.rc1
- Autorebuild for GCC 4.3

* Fri Jan 25 2008 Panu Matilainen <pmatilai@redhat.com> 4.4.2.3-0.1.rc1
- update to 4.4.2.3-rc1 
- merge nss-related patches into one
- change default queryformat to include arch 
- resolves (documentation): #159638, #233232, #332271, #350401
- resolves (build): #124300, #140597, #124995, #147383, #220449
- resolves (query): #244236, #323221, #60288
- resolves (general): #223931, #164021, #83006, #205080, #217258, #428979

* Fri Jan 11 2008 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-13
- lose the useless rpm user+group, use root:root like everything else
- install x86 arch macros on x86_64 (#194123)
- dont mess up target os+arch on rpmrc include (#232429)
- set pkg-config path based on target (#212522)
- fix funky automake breakage from nss libraries moving to /lib*

* Fri Jan 04 2008 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-12
- fix segfault in devel symlink dependency generation from Mark Salter (#338971)
- fix debugedit build with gcc 4.3
- drop popt-static build dependency

* Thu Nov 15 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-11
- Unbreak debugedit (missing crypto initialization)

* Thu Nov 15 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-10
- Initialize NSS as early as possible (#382091)

* Wed Nov 14 2007 Paul Nasrat <pauln@truemesh.com> 4.4.2.2-9
- Fix base64 assumption of signed char, from Tomas Mraz (#380911)

* Mon Nov 12 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-8
- Use NSS instead of beecrypt for cryptography, from Tomas Mraz (#348131)
- Update build + other dependencies accordingly

* Wed Oct 24 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-7
- Use package NEVRA everywhere for rpmProblems (#349091)
- The python problem addressed in -6 was related but a different issue...

* Wed Oct 24 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-6
- Don't mess up problem pkgNEVR in python ts.check() (#349091)

* Mon Oct 22 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-5
- add missing popt-devel dependency to rpm-devel

* Thu Oct 18 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-4
- debugedit fixes from Roland McGrath (#336951, #337011)

* Fri Oct 12 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-3
- add OSGi dependency generator script

* Thu Oct 11 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-2
- merge review: remove static libraries (#226377)
- merge review: remove comment causing doxygen to emit non-utf output (#226377)
- other minor spec cleanups

* Wed Oct 03 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-1
- update to 4.4.2.2 final
- update matchpathcon patch to work better when selinux disabled
- resolves #251400, #315271, #296731, #308171, #305221, #295941

* Tue Sep 11 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-0.5.rc2
- 4.4.2.2-rc2
- resolves #180996, #281611, #259961, #277161, #155079
- drop debugedit-names patch now that it's really upstream

* Wed Sep 05 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-0.4.rc1
- remove duplicated libraries from rpm-devel (#278151)

* Tue Sep 04 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-0.3.rc1
- require gawk, not awk, doh

* Tue Sep 04 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-0.2.rc1
- add back accidentally dropped debugedit patch until upstreamed
- add a bunch of previously implicit dependencies for rpm-build

* Tue Aug 28 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.2-0.1.rc1
- update to 4.4.2.2-rc1
- remove no longer needed hacks
- drop patches merged upstream

* Fri Aug 24 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-10
- split apidocs to separate package (they're huge)
- use system macros for bindir etc instead of defining our own
- remove NPTL-related LD_ASSUME_KERNEL stuff, no longer functional anyway
- remove various hacks that are no longer needed
- ensure correct permissions of debug sources
- follow fedora guidelines for user/group manipulation 
- clean up any non-matching bdb environment on post, not just 4.3
- visual cleanup of spec

* Fri Aug 24 2007 Panu Matilainen <pmatilai@redhat.com> 
- include sys-specific macros for all ARM variants (Lennert Buytenhek)

* Fri Aug 24 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2.1-9
- remove internal popt, buildrequire popt-devel and popt-static (#249352)
- move the versioned beecrypt dependency to libs where it belongs
- license clarification according to latest guidelines: libs and devel
  are dual gpl/lgpl licensed with exceptions, other binaries are gpl
- convert pl and sk manuals to utf-8
- buildrequire gawk

* Wed Aug 15 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2.1-8
- improved perl dependency extraction (#198033, #249135) by Ville Skyttä
  and John Owens
- make find-lang --with-gnome pick up .omf files (#251400) by Matthias Clasen

* Mon Aug 13 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2.1-7
- another debugedit fix and updated find-debuginfo script from Roland McGrath
- make popt provide popt-devel to further ease split-off transition
- skip ESTALE and EACCESS on mountpoints from Jeff Johnson (#190496, #220991)

* Sun Aug 12 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2.1-6
- debugedit buildid thinko fix from Roland McGrath
- loosen up popt-dependency to prepare for splitting it off

* Thu Aug  9 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2.1-5
- avoid unnecessary .rpmsave / .rpmnew files by Tomas Mraz (#29470, #128622)
- stricter docdir checking by Ralf S. Engelschall (#246819)
- add lua license to docs

* Thu Aug  9 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2.1-4
- fix new find-debuginfo.sh on noarch packages by Roland McGrath

* Wed Aug  8 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2.1-3
- make peace with new glibc checks on open() wrt internal bdb and rpm itself

* Wed Aug  8 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2.1-2
- ARM-related typo fixes from Lennert Buytenhek
- License clarifications

* Mon Aug  6 2007 Roland McGrath <roland@redhat.com>
- new find-debuginfo.sh script, requires elfutils >= 0.128

* Mon Jul 23 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-1
- 4.4.2.1 final
- reintroduce disttag
- include full ChangeLog as doc
- use up-to-date config.guess for ARM support (#246803)
- ARM EANBI gnu/gnuenabi fix from Lennert Buytenhek (#246803)

* Sat Jul 21 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-0.6.rc3
- dont mess up python exit codes

* Fri Jul 20 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-0.5.rc3
- require logrotate (#248629)
- allow checking for pending signals from python (#181434)
- add hook to python for cleaning up on unclean exit (#245389)

* Mon Jul 09 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-0.4.rc3
- 4.4.2.1-rc3

* Wed Jul 04 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-0.4.rc2
- 4.4.2.1-rc2

* Thu Jun 28 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-0.3.rc1
- don't hang because of leftover query iterators (#246044)

* Tue Jun 26 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-0.2.rc1
- patch popt version to 1.10.2.1 for clean upgrade path
- popt release follows main package release again

* Mon Jun 25 2007 Panu Matilainen <pmatilai@redhat.com> 4.4.2.1-0.1.rc1
- update to 4.4.2.1-rc1
- patch shuffle, most have been merged upstream
- drop mono-scripts, it comes from upstream now
- popt isn't upgrading here so it needs its own release

* Tue Jun 19 2007 Panu Matilainen <pmatilai@redhat.com> - 4.4.2-47
- spec / package (review) cleanups:
- use find_lang instead of manually listing translations
- remove useless rpm 3.x upgrade check from preinstall script
- use Fedora recommended buildroot
- don't include useless, ancient GPG keys
- add rpm, db and file licenses to docs
- use scriptlet dependency markers instead of PreReq
- post scriptlet requires coreutils
- main package doesn't require patch, rpm-build does
- buildrequire doxygen once more to resurrect apidocs
- remove useless/doubly packaged files from /usr/lib/rpm
- fix bunch of file permissions

* Tue May 01 2007 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-46
- Configurable policy for prefered ELF (#235757)

* Mon Apr 23 2007 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-45
- Fix debugedit for relative paths (#232222)

* Mon Apr 16 2007 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-44
- Set default verify flags for %%doc (#235353)
- Revert to old configure line 

* Mon Apr 16 2007 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-43
- Log failures for fork failing (OLPC)
- Gendiff enhancement from Enrico Scholz (#146981)

* Wed Apr 04 2007 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-42
- Remove ppc64 inline asm (#233145)

* Tue Mar 13 2007 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-41
- Fix potential segfault when no rpmloc_path (#231146)
- Fix debugedit for relative paths (#232222)
- Spec cleanup

* Mon Feb 19 2007 Jeremy Katz <katzj@redhat.com> - 4.4.2-40
- rpm-build should require findutils

* Wed Jan 17 2007 Deepak Bhole <dbhole@redhat.com> 4.4.2-39%{?dist}
- Added a missing BR for elfutils-libelf-devel-static (needed for -lelf)

* Mon Dec 11 2006 Jeremy Katz <katzj@redhat.com> - 4.4.2-38
- python: dbmatch keys can be unicode objects also (#219008)

* Wed Dec  6 2006 Jeremy Katz <katzj@redhat.com> - 4.4.2-37
- rebuild for python 2.5

* Mon Nov 20 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-36
- Fix ordering issues (#196590)

* Tue Oct 31 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-35
- Flush query buffer patch from jbj (#212833)

* Tue Oct 31 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-34
- Debuginfo extraction with O0

* Wed Oct 25 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-33
- Fix for ordering (#202540, #202542, #202543, #202544)

* Thu Sep 07 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-32
- Various debuginfo fixes (#165434, #165418, #149113, #205339)

* Fri Jul 21 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-31
- Apply matchpathcon patch

* Wed Jul 19 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-30
- Fix debugedit for ppc relocations (#199473)

* Fri Jul 14 2006 David Cantrell <dcantrell@redhat.com> - 4.4.2-29
- Fixed null pointer problem in rpmfcELF() DT_GNU_HASH handling

* Tue Jul 11 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-28
- Detect and provide a requirement for DT_GNU_HASH 

* Wed Jul 05 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-27
- IPv4/6 and EPSV support by Arkadiusz Miskiewicz <misiek@pld.org.pl>

* Wed Jun 28 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-26
- Force CHANGELOGTIME to be a list in rpm-python

* Wed Jun 28 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-25
- Remove SELinux context verification (#193488)

* Thu May 04 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-24
- File classification with autoReq off (#190488)

* Thu May  4 2006 Jeremy Katz <katzj@redhat.com> - 4.4.2-23
- make rpm-libs requires on base package stronger

* Wed May  3 2006 Jeremy Katz <katzj@redhat.com> - 4.4.2-22
- put in simple workaround for per-file deps with autoreq off (#190488) 
  while pnasrat works on a real fix

* Fri Apr 28 2006 Jeremy Katz <katzj@redhat.com> - 4.4.2-21
- run ldconfig in -libs subpackage %%post, not main package
- add patch to generate shared lib deps by following symlinks so that 
  -devel packages sanely depend on main libs

* Thu Apr 27 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-20
- Update --trusted stubs for rpmk breakage

* Tue Apr 25 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-19
- Add --trusted stubs from upstream

* Wed Apr 12 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-18
- Resurrect doxygen (#187714)

* Tue Apr 11 2006 Jeremy Katz <katzj@redhat.com> - 4.4.2-17
- remove redundant elfutils-libelf buildrequires
- rpm-python doesn't require elfutils (related to #188495)

* Fri Mar 31 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-16
- Skipdirs on erase again (#187308)
- Make fcntl lock sensitive to --root (#151255)
- Fix netshared path comparison (#52725)
- Fix rpm vercmp (#178798)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.4.2-15.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.4.2-15.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-15
- Rebuild for newer neon
- Fix scriptlet deadlock (#146549)

* Wed Jan 18 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-14
- Don't emit perl(main) (#177960)

* Wed Jan 11 2006 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-13
- Don't mmap large files

* Mon Jan  9 2006 Alexander Larsson <alexl@redhat.com> - 4.4.2-12
- Add mono req/provides support

* Thu Dec 01 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-11
- Remove rpm .la files (#174261)
- Cron job use paths (#174211)

* Tue Nov 29 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-10
- Ignore excluded size (#89661)

* Tue Nov 29 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-9
- Don't skipDirs on erasures (#140055)

* Mon Nov 28 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-8
- Add elfutils Build Requires to rpmbuild (#155129)
- Don't do conflicts if both files %%ghost(#155256)
- Fix popt charset for various languages (#172155)
- Don't include .la file (#174261)

* Tue Nov  8 2005 Tomas Mraz <tmraz@redhat.com> - 4.4.2-7
- rebuilt with new openssl

* Sun Oct 09 2005 Florian La Roche <laroche@redhat.com>
- rebuild for sqlite changes

* Thu Sep 22 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-5
- Actually fix context verification where matchpathcon fails (#162037)

* Fri Aug 26 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-4
- Fix build with CFLAGS having --param
- Fix for context verification in /tmp (#162037)

* Wed Jul 27 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-3
- popt minor version requires

* Tue Jul 26 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-2
- popt minor version bump
- revert to perl.req/perl.prov for now

* Thu Jul 21 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.2-1
- Upgrade to upstream release

* Tue May 24 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-21
- Update translations (#154623)

* Sat May 21 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-20
- Drop signature patch
- dangling unpackaged symlinks

* Tue May 17 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-19
- Check for symlinks in check-files (#108778)
- Move zh_CN (#154623)
- Test fix for signing old rpms (#127113)

* Wed May 04 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-18.1
- Fix typo
- Fix typo

* Wed May 04 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-18
- Add missing fsm.c from matchpathcon patches 

* Tue May 03 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-17
- Fix typo

* Tue May 03 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-16
- Yet more matchpathcon

* Tue May 03 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-15
- Some more matchpathcon work

* Mon May 02 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-14
- matchpathcon fixup

* Mon May 02 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-13
- Use matchpathcon (#151870)

* Sat Apr 30 2005 Miloslav Trmac <mitr@redhat.com> - 4.4.1-12
- Remove $RPM_BUILD_ROOT and $RPM_BUILD_DIR from distribued .la files (#116891)
- Don't ship static version of _rpmdb.so
- BuildRequires: readline-devel

* Wed Apr 27 2005 Paul Nasrat <pnasrat@redhat.com> - 4.4.1-11
- Fix for (pre,postun) (#155700)
- Erase ordering

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 4.4.1-10
- add patch to fix segfault with non-merged hdlists

* Thu Mar 31 2005 Thomas Woerner <twoerner@redhat.com> 4.4.1-9
- enabled prereqs again

* Mon Mar 21 2005 Paul Nasrat <pnasrat@redhat.com> 4.4.1-8
- Add devel requires libselinux-devel
- Fileconflicts as FC3 (#151609)

* Wed Mar  9 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-7
- rebuild against renamed sqlite package (#149719).

* Mon Mar  7 2005 Jeremy Katz <katzj@redhat.com> - 4.4.1-6
- fix build with new glibc

* Mon Mar  7 2005 Jeremy Katz <katzj@redhat.com> - 4.4.1-5
- disable hkp by default

* Tue Mar  1 2005 Jeremy Katz <katzj@redhat.com> - 4.4.1-4
- fix build with gcc 4

* Mon Feb 28 2005 Jeremy Katz <katzj@redhat.com> - 4.4.1-3
- fix posttrans callback check being backwards (#149524)

* Sun Feb 13 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-1
- don't classify files in /dev (#146623).
- don't build with sqlite3 if <sqlite3.h> is missing.

* Sat Feb 12 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.24
- zlib: uniqify certain symbols to prevent name space pollution.
- macosx: include <sys/types.h> so that python sees the u_char typedef.
- macosx: change to --prefix=/usr rather than /opt/local.
- use waitpid rather than SIGCHLD reaper.
- rip out DB_PRIVATE revert if not NPTL, it's not the right thing to do.

* Fri Feb 11 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.22
- permit build scriptlet interpreters to be individually overridden.

* Thu Feb 10 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.20
- perform callbacks as always (#147537).

* Wed Feb  2 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.16
- fix: length of gpg V4 hash seed was incorrect (#146896).
- add support for V4 rfc-2440 signatures.

* Mon Jan 31 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.14
- add sqlite internal (build still expects external sqlite3-3.0.8).
- sqlite: revert to original narrow scoping of cOpen/cClose.

* Fri Jan 28 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.12
- python: force dbMatch() h# key to be 32 bit integer (#146477).

* Tue Jan 25 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.10
- more macosx fiddles.
- move global /var/lock/rpm/transaction to dbpath.
- permit fcntl path to be configured through rpmlock_path macro.
- add missing #if defined(ENABLE_NLS) (#146184).

* Mon Jan 17 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.8
- changes to build on Mac OS X using darwinports neon/beecrypt.
- add https://svn.uhulinux.hu/packages/dev/zlib/patches/02-rsync.patch

* Sun Jan  9 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.7
- build against external/internal neon.

* Tue Jan  4 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.6
- mac os x patches (#131943,#131944,#132924,#132926).
- mac os x patches (#133611, #133612, #134637).

* Sun Jan  2 2005 Jeff Johnson <jbj@jbj.org> 4.4.1-0.5
- upgrade to db-4.3.27.
- revert MAGIC_COMPRESS, real fix is in libmagic (#143782).
- upgrade to file-4.12 internal.

* Tue Dec  7 2004 Jeff Johnson <jbj@jbj.org> 4.4.1-0.3
- use package color as Obsoletes: color.

* Mon Dec  6 2004 Jeff Johnson <jbj@jbj.org> 4.4.1-0.2
- automagically detect and emit "python(abi) = 2.4" dependencies.
- popt 1.10.1 to preserve newer.

* Sun Dec  5 2004 Jeff Johnson <jbj@jbj.org> 4.4.1-0.1
- force *.py->*.pyo byte code compilation with brp-python-bytecompile.
