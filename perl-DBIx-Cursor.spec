%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Cursor
Summary:	DBIx::Cursor - Perl extension for easy DBI-access to a single table
Summary(pl):	DBIx::Cursor - rozszerzenie do ³atwego dostêpu DBI do pojedynczych tabel
Name:		perl-DBIx-Cursor
Version:	0.13
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class DBIx::Cursor represents a cursor for a single
Database-table. You can select, update, insert or delete entries in a
table easier than creating SQL-statements. It does not use any
specific features of any database, so it should work with every
DBD-driver.

%description -l pl
Klasa DBIx::Cursor reprezentuje kursor dla pojedynczej tabeli bazy
danych. Mo¿na wykonywaæ operacje select, update, insert, delete na
elementach w tabeli ³atwiej od tworzenia wyra¿eñ SQL. Modu³ nie u¿ywa
¿adnych cech specyficznych dla danej bazy, wiêc powinien dzia³aæ z
ka¿dym sterownikiem DBD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
