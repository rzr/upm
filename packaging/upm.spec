Name:           upm
Version:        0.1.8
Release:        0
License:        TODO
Summary:        TODO
Url:            https://github.com/intel-iot-devkit/upm
Group:          System/Libraries
# X-Vc-Url:     https://github.com/intel-iot-devkit/upm
Group:          Contrib
Source:         %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(mraa)
BuildRequires:  fdupes

%description
TODO

%package devel
Summary:    TODO
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
TODO

%prep
%setup -q


%build

%cmake . \
 -DCMAKE_INSTALL_PREFIX:PATH=/usr

%__make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_libdir}/*.so.*



%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%exclude %{_prefix}/lib/debug
%exclude %{_prefix}/lib/debug/*
%exclude %{_prefix}/lib/debug/*/*
%exclude %{_prefix}/lib/debug/*/*/*
%exclude %{_prefix}/demos/demos-manifest.xml
%exclude %{_libdir}/*/examples/*
%exclude %{_prefix}/tests/*/*/*
