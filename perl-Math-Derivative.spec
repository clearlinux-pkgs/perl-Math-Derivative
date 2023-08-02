#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Derivative
Version  : 1.01
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/J/JG/JGAMBLE/Math-Derivative-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JG/JGAMBLE/Math-Derivative-1.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-derivative-perl/libmath-derivative-perl_1.01-1.debian.tar.xz
Summary  : 'Numeric 1st and 2nd order differentiation.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Math-Derivative-license = %{version}-%{release}
Requires: perl-Math-Derivative-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Math::Utils)

%description
Math-Derivative, version 1.01, 9 August 2017
Numeric 1st and 2nd order differentiation.

%package dev
Summary: dev components for the perl-Math-Derivative package.
Group: Development
Provides: perl-Math-Derivative-devel = %{version}-%{release}
Requires: perl-Math-Derivative = %{version}-%{release}

%description dev
dev components for the perl-Math-Derivative package.


%package license
Summary: license components for the perl-Math-Derivative package.
Group: Default

%description license
license components for the perl-Math-Derivative package.


%package perl
Summary: perl components for the perl-Math-Derivative package.
Group: Default
Requires: perl-Math-Derivative = %{version}-%{release}

%description perl
perl components for the perl-Math-Derivative package.


%prep
%setup -q -n Math-Derivative-1.01
cd %{_builddir}
tar xf %{_sourcedir}/libmath-derivative-perl_1.01-1.debian.tar.xz
cd %{_builddir}/Math-Derivative-1.01
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Math-Derivative-1.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Derivative
cp %{_builddir}/Math-Derivative-1.01/LICENSE %{buildroot}/usr/share/package-licenses/perl-Math-Derivative/d20876af29feb11cd2018d05085f5b74a2a9d91e
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Derivative/233d7dbd23bbd625947a02fb2f4af90343cbcf79
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Derivative.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Derivative/233d7dbd23bbd625947a02fb2f4af90343cbcf79
/usr/share/package-licenses/perl-Math-Derivative/d20876af29feb11cd2018d05085f5b74a2a9d91e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
