%global major 1
%define libname %mklibname nvidia-egl-wayland2
%define devname %mklibname -d nvidia-egl-wayland2
%define lib32name %mklib32name nvidia-egl-wayland2
%define dev32name %mklib32name -d nvidia-egl-wayland2

%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

Name:		egl-wayland2
Version:	1.0.0
Release:	0.rc
Group:		System/Libraries
Summary:	Wayland EGL External Platform library for nvidia GPUs
License:	MIT
URL:		https://github.com/NVIDIA/egl-wayland2
Source0:	https://github.com/NVIDIA/egl-wayland2/archive/1.0.0-rc/%{name}-1.0.0-rc.tar.gz

BuildSystem:	meson
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(eglexternalplatform)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(libffi)
%if %{with compat32}
BuildRequires:	devel(libdrm)
BuildRequires:	devel(libEGL)
BuildRequires:	devel(libwayland-server)
BuildRequires:	devel(libwayland-client)
BuildRequires:	devel(libffi)
%endif
Requires:	%{libname} >= %{EVRD}
# Required for directory ownership
Requires:	libglvnd-egl

%description
%{summary}.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Provides:	%{name} = %{EVRD}
# Renamed after 6.0 2025/07/24

%description -n %{libname}
%{summary}.

%package -n %{devname}
Summary:	Wayland EGL External Platform library development package
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Wayland EGL External Platform library development package.

%package -n %{lib32name}
Summary:	%{summary} (32-bit)
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{lib32name}
%{summary}.

%package -n %{dev32name}
Summary:	Wayland EGL External Platform library development package (32-bit)
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
Wayland EGL External Platform library development package (32-bit).

%files -n %{libname}
%doc README.md
%license COPYING


%files -n %{devname}


%if %{with compat32}
%files -n %{lib32name}

%files -n %{dev32name}

%endif
