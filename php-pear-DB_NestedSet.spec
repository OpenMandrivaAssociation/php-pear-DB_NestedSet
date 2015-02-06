%define		_class		DB
%define		_subclass	NestedSet
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.4.1
Release:	6
Summary:	API to build and query nested sets
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_NestedSet/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
DB_NestedSet lets you create trees with infinite depth inside a
relational database. The package provides a way to:
- create/update/delete nodes
- query nodes, trees and subtrees
- copy (clone) nodes, trees and subtrees
- move nodes, trees and subtrees
- call event handlers on specific events like on node deletion
- output the tree with
  - PEAR::HTML_TreeMenu
  - TigraMenu (http://www.softcomplex.com/products/tigra_menu/)
- It also features caching of SQL queries using PEAR::Cache.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-3mdv2012.0
+ Revision: 741841
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2
+ Revision: 679284
- mass rebuild

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.1-1mdv2011.0
+ Revision: 569595
- update to new version 1.4.1

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0RC1-5mdv2010.1
+ Revision: 479292
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.4.0RC1-4mdv2010.0
+ Revision: 440991
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4.0RC1-3mdv2009.1
+ Revision: 321952
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0RC1-2mdv2009.0
+ Revision: 236822
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 09 2007 Adam Williamson <awilliamson@mandriva.org> 1.4.0RC1-1mdv2008.1
+ Revision: 107115
- new release 1.4.0RC1

* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-9mdv2008.0
+ Revision: 53887
- fix deps

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-8mdv2008.0
+ Revision: 15405
- rule out the PHPUnit.php dep


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-7mdv2007.0
+ Revision: 81485
- Import php-pear-DB_NestedSet

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-1mdk
- initial Mandriva package (PLD import)

