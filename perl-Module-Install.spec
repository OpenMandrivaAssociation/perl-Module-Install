%define	upstream_name	 Module-Install
%define upstream_version 0.93

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Standalone, extensible Perl module installer
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Devel::PPPort) >= 3.16
BuildRequires:	perl(ExtUtils::Install) >= 1.52
BuildRequires:	perl(ExtUtils::ParseXS) >= 2.19
BuildRequires:	perl-PathTools >= 3.270.100
BuildRequires:	perl(File::Remove)
BuildRequires:  perl(JSON)
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
