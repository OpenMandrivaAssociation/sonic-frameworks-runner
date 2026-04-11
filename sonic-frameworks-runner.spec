%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname SonicFrameworksRunner
%define devname %mklibname SonicFrameworksRunner -d
#define git 20240217

Name: sonic-frameworks-runner
Version: 6.25.0
Release: %{?git:0.%{git}.}1
URL:     https://github.com/Sonic-DE/sonic-frameworks-runner
# %if 0%{?git:1}
# Source0: https://invent.kde.org/frameworks/krunner/-/archive/master/krunner-master.tar.bz2#/krunner-%{git}.tar.bz2
# %else
Source0: %url/archive/%version/%name-%version.tar.gz
# %endif
Summary: Framework for providing different actions given a string query
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries

BuildSystem:   cmake
BuildOption: 	-DBUILD_QCH:BOOL=ON
BuildOption: 	-DBUILD_WITH_QT6:BOOL=ON
BuildOption: 	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6ThreadWeaver)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)

# pending rename
# BuildRequires: cmake(KF6WindowSystem)
BuildRequires: %{_lib}SonicFrameworksWindowSystem-devel

Conflicts:     kf6-krunner

Requires: %{libname} = %{EVRD}

%description
Framework for providing different actions given a string query

%package -n %{libname}
Summary: Framework for providing different actions given a string query
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts: %{_lib}KF6Runner

%description -n %{libname}
%summary

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts: %{_lib}KF6Runner-devel

%description -n %{devname}
%summary

%files
%{_datadir}/qlogging-categories6/krunner.*

%files -n %{devname}
%{_includedir}/KF6/KRunner
%{_libdir}/cmake/KF6Runner
%{_datadir}/dbus-1/interfaces/kf6_org.kde.krunner1.xml
%{_datadir}/kdevappwizard/templates/runner6.tar.bz2
%{_datadir}/kdevappwizard/templates/runner6python.tar.bz2

%files -n %{libname}
%{_libdir}/libKF6Runner.so*
