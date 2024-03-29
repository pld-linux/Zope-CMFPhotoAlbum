%define		zope_subname	CMFPhotoAlbum
%define		sub_ver rc2
Summary:	A Zope product providing Photo Album in your CMF
Summary(pl.UTF-8):	Dodatek dla Zope umożliwiający operacje na zdjęciach w CMF
Name:		Zope-%{zope_subname}
Version:	0.4
Release:	0.%{sub_ver}.3
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}%{sub_ver}.tar.gz
# Source0-md5:	5b1157ccdbd7638495481db8c3aefcbe
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope >= 2.6.1
Requires:	Zope-BTreeFolder2 >= 0.5
Requires:	Zope-CMF >= 1:1.4
Requires:	Zope-CMFPhoto
Requires:	Zope-CMFPlone >= 1.0.1
Conflicts:	CMF
Conflicts:	Plone
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CMFPhotoAlbum is a Zope product that provides Photo Album in your CMF.

%description -l pl.UTF-8
CMFPhotoAlbum jest dodatkiem dla Zope umożliwiającym operacje na
zdjęciach w CMF.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,i18n,skins,*.py,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt README.txt
%{_datadir}/%{name}
