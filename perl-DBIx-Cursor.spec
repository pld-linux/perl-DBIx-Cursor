%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Cursor
Summary:	DBIx::Cursor - Perl extension for easy DBI-access to a single table
Summary(pl):	DBIx::Cursor - rozszerzenie do �atwego dost�pu DBI do pojedynczych tabel
Name:		perl-DBIx-Cursor
Version:	0.14
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
danych. Mo�na wykonywa� operacje select, update, insert, delete na
elementach w tabeli �atwiej od tworzenia wyra�e� SQL. Modu� nie u�ywa
�adnych cech specyficznych dla danej bazy, wi�c powinien dzia�a� z
ka�dym sterownikiem DBD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
