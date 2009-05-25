%define	module	Module-Install
%define	name	perl-%{module}
%define version 0.90
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Standalone, extensible Perl module installer
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Devel::PPPort) >= 3.16
BuildRequires:	perl(ExtUtils::Install) >= 1.52
BuildRequires:	perl(ExtUtils::ParseXS) >= 2.1802
BuildRequires:	perl(File::Spec) >= 3.2701
BuildRequires:	perl(File::Remove)
BuildRequires:  perl(JSON)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(Module::ScanDeps)
BuildRequires:	perl(PAR::Dist)
BuildRequires:	perl(Test::Harness) >= 3.13
BuildRequires:	perl(Test::More) >= 0.86
BuildRequires:	perl(YAML)
BuildRequires:	perl(YAML::Tiny)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides a drop-in replacement for ExtUtils::MakeMaker. For
first-time users, Brian Ingerson's Creating Module Distributions with
Module::Install in June 2003 issue of The Perl Journal
(http://www.tpj.com/issues/) provides a gentle introduction to how this
module works.

%prep
%setup -q -n %{module}-%{version}

%build
chmod 644 Changes
find lib -type f | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# this one requires a working CPAN configuration
rm -f t/03_autoinstall.t
%__make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Module
%{perl_vendorlib}/inc/Module
%{perl_vendorlib}/auto/share/dist/Module-Install
%{_mandir}/man3/*
