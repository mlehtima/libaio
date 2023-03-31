Name: libaio
Version: 0.3.113
Release: 1
Summary: Linux-native asynchronous I/O access library
License: LGPLv2+
Source: %{name}-%{version}.tar.gz

%description
The Linux-native asynchronous I/O facility ("async I/O", or "aio") has a
richer API and capability set than the simple POSIX async I/O facility.
This library, libaio, provides the Linux-native API for async I/O.
The POSIX async I/O facility requires this library in order to provide
kernel-accelerated async I/O capabilities, as do applications which
require the Linux-native async I/O API.

%package devel
Summary: Development files for Linux-native asynchronous I/O access
Requires: %{name} = %{version}-%{release}

%description devel
This package provides header files to include and libraries to link with
for the Linux-native asynchronous I/O facility ("async I/O", or "aio").

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
# This package uses ASMs to implement symbol versioning and is thus
# incompatible with LTO
%define _lto_cflags %{nil}

%make_build

%install
%make_install libdir=%{_libdir}

find %{buildroot} -name '*.a' -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libaio.so.*

%files devel
%{_includedir}/*
%{_libdir}/libaio.so
