%define		zope_subname	CMFPhotoAlbum
%define		sub_ver rc2
Summary:	A Zope product providing Photo Album in your CMF
Summary(pl):	Dodatek dla Zope umo¿liwiaj±cy operacje na zdjêciach w CMF
Name:		Zope-%{zope_subname}
Version:	0.4
Release:	0.%{sub_ver}.2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}%{sub_ver}.tar.gz
# Source0-md5:	5b1157ccdbd7638495481db8c3aefcbe
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope-CMF >= 1.3
Requires:	Zope-CMFPlone >= 1.0.1
Requires:	Zope >= 2.6.1
Requires:	Zope-BTreeFolder2 >= 0.5
Requires:	Zope-CMFPhoto
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF
Conflicts:	Plone

%description
CMFPhotoAlbum is a Zope product that provides Photo Album in your CMF.

%description -l pl
CMFPhotoAlbum jest dodatkiem dla Zope umo¿liwiaj±cym operacje na
zdjêciach w CMF.

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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt README.txt
%{_datadir}/%{name}
