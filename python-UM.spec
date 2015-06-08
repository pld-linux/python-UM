# Conditional build:
%bcond_without	doc		# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python3 # CPython 3.x module

%define 	module	UM
%define		snap	20150608
Summary:	Framework for building 3D printing related applications
Name:		python-%{module}
Version:	0.1
Release:	0.%{snap}.1
License:	AGPL v3+
Group:		Libraries/Python
Source0:	Uranium-%{snap}.tar.bz2
# Source0-md5:	9772a194ea2dd8f03a5ce17cd8583b88
URL:		https://github.com/Ultimaker/Uranium
BuildRequires:	cmake
BuildRequires:	rpm-pythonprov
Requires:	python3-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uranium framework for building 3D printing related applications.

%prep
%setup -q -n Uranium
# -n %{module}-%{version}

sed -i -e 's#CMAKE_INSTALL_LIBDIR#CMAKE_INSTALL_DATADIR#g' CMakeLists.txt

%build
install -d build
cd build
%{cmake} ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{_datadir}/uranium
