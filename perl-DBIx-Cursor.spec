#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	DBIx
%define		pnam	Cursor
%include	/usr/lib/rpm/macros.perl
Summary:	DBIx::Cursor - Perl extension for easy DBI-access to a single table
Summary(pl.UTF-8):	DBIx::Cursor - rozszerzenie do łatwego dostępu DBI do pojedynczych tabel
Name:		perl-DBIx-Cursor
Version:	0.14
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	80d518eafb9854b4a31d9a4c658c6af8
URL:		http://search.cpan.org/dist/DBIx-Cursor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class DBIx::Cursor represents a cursor for a single
Database-table. You can select, update, insert or delete entries in a
table easier than creating SQL-statements. It does not use any
specific features of any database, so it should work with every
DBD-driver.

%description -l pl.UTF-8
Klasa DBIx::Cursor reprezentuje kursor dla pojedynczej tabeli bazy
danych. Można wykonywać operacje select, update, insert, delete na
elementach w tabeli łatwiej od tworzenia wyrażeń SQL. Moduł nie używa
żadnych cech specyficznych dla danej bazy, więc powinien działać z
każdym sterownikiem DBD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
