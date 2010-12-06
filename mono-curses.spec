%define name mono-curses
%define version 0.2
%define svn r128192
%define release %mkrel 0.%svn.4

Summary: Mono library for writing simple curses UIs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{svn}.tar.bz2
#gw this is automatically generated at build time by attrib, but this does
# not work in iurt
Source1: constants.cs
Patch: monotorrent-curses-makefile.patch
License: MIT
Group: Development/Other
Url: http://www.mono-project.com/MonoCurses
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: libncurses-devel
BuildRequires: monodoc
Provides: monotorrent-curses
Obsoletes: monotorrent-curses

%description
This is a library for writing curses UIs in Mono.

%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9
Provides: monotorrent-curses-doc
Obsoletes: monotorrent-curses-doc


%description doc
This package contains the API documentation for the %name in
Monodoc format.

%prep
%setup -q -n mono-curses
%patch
cp %SOURCE1 .

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall 
%if %_lib != lib
mkdir -p %buildroot%_libdir
mv %buildroot%_prefix/lib/{*.so,pkgconfig} %buildroot%_libdir

%endif

%post doc
%_bindir/monodoc --make-index > /dev/null
%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS
%_libdir/libmono-curses.so
%_libdir/pkgconfig/mono-curses.pc
%_prefix/lib/mono/gac/mono-curses
%_prefix/lib/mono/mono-curses



%files doc
%defattr(-,root,root)
%doc ChangeLog
%_prefix/lib/monodoc/sources/mono-curses.*
