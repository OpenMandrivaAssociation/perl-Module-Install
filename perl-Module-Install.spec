%define	upstream_name	 Module-Install
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Standalone, extensible Perl module installer
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Devel::PPPort) >= 3.16
BuildRequires:	perl(ExtUtils::Install) >= 1.52
BuildRequires:	perl(ExtUtils::ParseXS) >= 2.19
BuildRequires:	perl-PathTools >= 3.270.100
BuildRequires:	perl(File::Remove)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(Module::ScanDeps)
BuildRequires:	perl(PAR::Dist)
BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(Test::Harness) >= 3.13
BuildRequires:	perl(Test::More) >= 0.86
BuildRequires:	perl(YAML)
BuildRequires:	perl(YAML::Tiny)

BuildArch:	noarch

%description
This module provides a drop-in replacement for ExtUtils::MakeMaker. For
first-time users, Brian Ingerson's Creating Module Distributions with
Module::Install in June 2003 issue of The Perl Journal
(http://www.tpj.com/issues/) provides a gentle introduction to how this
module works.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
chmod 644 Changes
find lib -type f | xargs chmod 644
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# this one requires a working CPAN configuration
rm -f t/03_autoinstall.t
%make test

%install
%__rm -rf %{buildroot}
%makeinstall_std

%files
%doc README Changes META.yml
%{perl_vendorlib}/Module
%{perl_vendorlib}/inc/Module
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-3mdv2012.0
+ Revision: 765488
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1
+ Revision: 659961
- update to new version 1.01

* Thu Jul 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 553568
- adding missing buildrequires:
- update to 1.00

* Thu Mar 11 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.950.0-1mdv2010.1
+ Revision: 518079
- update to 0.95

* Wed Feb 24 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.940.0-1mdv2010.1
+ Revision: 510523
- update to 0.94

* Mon Feb 08 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.930.0-1mdv2010.1
+ Revision: 502102
- update to 0.93

* Fri Jan 22 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.1
+ Revision: 494933
- update to 0.92

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.910.0-2mdv2010.0
+ Revision: 409059
- force rebuild

* Thu May 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.910.0-1mdv2010.0
+ Revision: 380352
- adding missing buildrequires:
- updated to 0.91
- fixing pathtools buildrequires:
- fixing version in buildrequires:
- fixing perl versions in requires
- fixing buildrequires:
- update to new version 0.90

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.89-1mdv2010.0
+ Revision: 378233
- update to new version 0.89

* Fri May 15 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.88-1mdv2010.0
+ Revision: 376054
- update to new version 0.88

* Thu May 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.87-1mdv2010.0
+ Revision: 372851
- update to new version 0.87

* Sat May 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.86-1mdv2010.0
+ Revision: 370491
- update to new version 0.86

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.80-1mdv2009.1
+ Revision: 357702
- update to new version 0.80

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.79-1mdv2009.1
+ Revision: 337663
- new release

* Mon Jan 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.78-1mdv2009.1
+ Revision: 333641
- new version

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.77-1mdv2009.0
+ Revision: 270392
- update to new version 0.77

* Sun Jul 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.76-1mdv2009.0
+ Revision: 239114
- new version

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2009.0
+ Revision: 214528
- update to new version 0.75

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.74-1mdv2009.0
+ Revision: 212216
- update to new version 0.74

* Sun May 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.73-1mdv2009.0
+ Revision: 211240
- don't run autoinstall test, it requires a working CPAN configuration
- fix build dependencies
- update to new version 0.73
- update to new version 0.72
- fix build dependencies
- fix build dependencies

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-1mdv2008.1
+ Revision: 104561
- update to new version 0.68

* Mon Jul 02 2007 Funda Wang <fwang@mandriva.org> 0.67-1mdv2008.0
+ Revision: 46971
- New version


* Tue Sep 26 2006 Scott Karns <scottk@mandriva.org> 0.64-1mdv2007.0
- New version 0.64

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-1mdv2007.0
- New version 0.63

* Fri May 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.62-1mdk
- New release 0.62

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-1mdk
- 0.61
- rpmbuildupdate aware
- drop patch, merged upstream

* Sun Mar 12 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.60-1mdk
- 0.60

* Tue Mar 07 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.59-1mdk
- 0.59

* Thu Mar 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.57-1mdk
- 0.57

* Mon Feb 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.56-1mdk
- 0.56

* Tue Jan 31 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.55-1mdk
- 0.55
- Rediff patch 0
- Fix perms

* Fri Jan 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.54-1mdk
- 0.54

* Tue Jan 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.52-1mdk
- 0.52

* Thu Dec 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.50-1mdk
- 0.50

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.45-1mdk
- 0.45

* Tue Dec 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.43-1mdk
- 0.43

* Mon Dec 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.42-1mdk
- 0.42

* Wed Dec 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.40-1mdk
- 0.40
- don't try to install CPANPLUS (patch 0)

* Fri Dec 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.39-1mdk
- Initial MDV package

