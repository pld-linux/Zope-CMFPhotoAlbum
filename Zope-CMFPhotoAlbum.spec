%include	/usr/lib/rpm/macros.python
%define		zope_subname	CMFPhotoAlbum
Summary:	CMFPhotoAlbum - a Zope product providing Photo Album in your CMF
Summary(pl):	CMFPhotoAlbum - dodatek dla Zope umo¿liwiaj±cy operacje na zdjêciach w CMF
Name:		Zope-%{zope_subname}
Version:	0.2
Release:	2
License:	GNU
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	2951e810674200854db370d9f3197bcb
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	CMF
Requires:	Plone
Requires:	Zope
Requires:	Zope-BTreeFolder2
Requires:	Zope-CMFPhoto
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
CMFPhotoAlbum is a Zope product that provides Photo Album in your CMF.

%description -l pl
CMFPhotoAlbum jest dodatkiem dla Zope umo¿liwiaj±cym operacje na
zdjêciach w CMF.

%prep
%setup -q -c %{zope_subname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}

cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/*.txt
# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/*.txt
%{product_dir}/%{zope_subname}
