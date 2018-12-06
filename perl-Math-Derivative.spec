#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Derivative
Version  : 1.01
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/J/JG/JGAMBLE/Math-Derivative-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JG/JGAMBLE/Math-Derivative-1.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-derivative-perl/libmath-derivative-perl_1.01-1.debian.tar.xz
Summary  : 'Numeric 1st and 2nd order differentiation.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Math-Derivative-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Math::Utils)

%description
Math-Derivative, version 1.01, 9 August 2017
Numeric 1st and 2nd order differentiation.

%package dev
Summary: dev components for the perl-Math-Derivative package.
Group: Development
Provides: perl-Math-Derivative-devel = %{version}-%{release}

%description dev
dev components for the perl-Math-Derivative package.


%package license
Summary: license components for the perl-Math-Derivative package.
Group: Default

%description license
license components for the perl-Math-Derivative package.


%prep
%setup -q -n Math-Derivative-1.01
cd ..
%setup -q -T -D -n Math-Derivative-1.01 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Math-Derivative-1.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Derivative
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Math-Derivative/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/Math/Derivative.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Derivative.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Derivative/LICENSE
