#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	DBIx
%define		pnam	Simple
Summary:	DBIx::Simple - Very complete easy-to-use OO interface to DBI
Name:		perl-DBIx-Simple
Version:	1.37
Release:	1
License:	Any from http://www.opensource.org/licenses/alphabetical
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eb53ef4a93be7ebf043cd49075e81913
URL:		https://metacpan.org/release/DBIx-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-DBI >= 1.21
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

This module is aimed at rapid development and easy maintenance. Query
preparation and execution are combined in a single method, the result
object (which is a wrapper around the statement handle) provides easy
row-by-row and slurping methods.

The query method returns either a result object, or a dummy object.
The dummy object returns undef (or an empty list) for all methods and
when used in boolean context, is false. The dummy object lets you
postpone (or skip) error checking, but it also makes immediate error
checking simply $db->query(...) or die $db->error.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBIx/Simple.pm
%{perl_vendorlib}/DBIx/Simple
%{_mandir}/man3/DBIx::Simple*.3*
