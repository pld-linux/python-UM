# TODO
# - rename .spec to python3 if python2 is never to be supported
%define		rel		2
%define		snap	20150608
%define 	module	UM
Summary:	Framework for building 3D printing related applications
Name:		python-%{module}
Version:	0.1
Release:	0.%{snap}.%{rel}
License:	AGPL v3+
Group:		Libraries/Python
Source0:	Uranium-%{snap}.tar.bz2
# Source0-md5:	9772a194ea2dd8f03a5ce17cd8583b88
URL:		https://github.com/Ultimaker/Uranium
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uranium framework for building 3D printing related applications.

%package -n python3-%{module}
Summary:	Framework for building 3D printing related applications
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Uranium framework for building 3D printing related applications.

%prep
%setup -qc
mv Uranium/* .

sed -i -e 's#CMAKE_INSTALL_LIBDIR#CMAKE_INSTALL_DATADIR#g' CMakeLists.txt

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{_datadir}/uranium
