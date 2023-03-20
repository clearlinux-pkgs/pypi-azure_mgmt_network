#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-azure_mgmt_network
Version  : 22.3.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/78/9f/c864eabb2c08a4cde3d87b04452dcbbcd8c2b8d02cd9c718443231e0ffb2/azure-mgmt-network-22.3.0.zip
Source0  : https://files.pythonhosted.org/packages/78/9f/c864eabb2c08a4cde3d87b04452dcbbcd8c2b8d02cd9c718443231e0ffb2/azure-mgmt-network-22.3.0.zip
Summary  : Microsoft Azure Network Management Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-azure_mgmt_network-license = %{version}-%{release}
Requires: pypi-azure_mgmt_network-python = %{version}-%{release}
Requires: pypi-azure_mgmt_network-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(azure_common)
BuildRequires : pypi(azure_mgmt_core)
BuildRequires : pypi(msrest)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Microsoft Azure SDK for Python
This is the Microsoft Azure Network Management Client Library.
This package has been tested with Python 3.7+.
For a more complete view of Azure libraries, see the [azure sdk python release](https://aka.ms/azsdk/python/all).

%package license
Summary: license components for the pypi-azure_mgmt_network package.
Group: Default

%description license
license components for the pypi-azure_mgmt_network package.


%package python
Summary: python components for the pypi-azure_mgmt_network package.
Group: Default
Requires: pypi-azure_mgmt_network-python3 = %{version}-%{release}

%description python
python components for the pypi-azure_mgmt_network package.


%package python3
Summary: python3 components for the pypi-azure_mgmt_network package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_network)
Requires: pypi(azure_common)
Requires: pypi(azure_mgmt_core)
Requires: pypi(msrest)

%description python3
python3 components for the pypi-azure_mgmt_network package.


%prep
%setup -q -n azure-mgmt-network-22.3.0
cd %{_builddir}/azure-mgmt-network-22.3.0
pushd ..
cp -a azure-mgmt-network-22.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679325703
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-azure_mgmt_network
cp %{_builddir}/azure-mgmt-network-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-azure_mgmt_network/7aea571d641549de89730da8e7ff5a6940c5526b || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-azure_mgmt_network/7aea571d641549de89730da8e7ff5a6940c5526b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
