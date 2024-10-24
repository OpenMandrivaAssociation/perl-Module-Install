%define	modname	Module-Install

Summary:	Standalone, extensible Perl module installer
Name:		perl-%{modname}
Version:	1.21
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Module::Install
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Devel::PPPort) >= 3.16
BuildRequires:	perl(ExtUtils::Install) >= 1.52
BuildRequires:	perl(ExtUtils::ParseXS) >= 2.19
BuildRequires:	perl-PathTools
BuildRequires:	perl(File::Remove)
BuildRequires:	perl(JSON)
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(Module::ScanDeps)
BuildRequires:	perl(PAR::Dist)
BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(Test::Harness) >= 3.13
BuildRequires:	perl(Test::More) >= 0.86
BuildRequires:	perl(YAML)
BuildRequires:	perl(YAML::Tiny)

%description
This module provides a drop-in replacement for ExtUtils::MakeMaker. For
first-time users, Brian Ingerson's Creating Module Distributions with
Module::Install in June 2003 issue of The Perl Journal
(http://www.tpj.com/issues/) provides a gentle introduction to how this
module works.

%prep
%autosetup -p1 -n %{modname}-%{version}
chmod 644 Changes
find lib -type f | xargs chmod 644

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# this one requires a working CPAN configuration
rm -f t/03_autoinstall.t
%make test

%install
%make_install

%files
%doc README Changes META.yml
%{perl_vendorlib}/Module
%{perl_vendorlib}/inc/Module
%{_mandir}/man3/*
