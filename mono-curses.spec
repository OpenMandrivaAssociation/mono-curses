%define svn r128192

Summary:	Mono library for writing simple curses UIs
Name:		mono-curses
Version:	0.2
Release:	0.%{svn}.6
License:	MIT
Group:		Development/Other
Url:		https://www.mono-project.com/MonoCurses
Source0:	%{name}-%{svn}.tar.bz2
#gw this is automatically generated at build time by attrib, but this does
# not work in iurt
Source1:	constants.cs
Patch:		monotorrent-curses-makefile.patch

BuildRequires:	mono-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	monodoc

%description
This is a library for writing curses UIs in Mono.

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Other
Requires(post): mono-tools
Requires(postun): mono-tools >= 1.1.9


%description doc
This package contains the API documentation for the %{name} in
Monodoc format.

%prep
%setup -q -n mono-curses
%patch
cp %SOURCE1 .

%build
./configure --prefix=%{_prefix}
make

%install
%makeinstall 
%if %{_lib} != lib
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/{*.so,pkgconfig} %{buildroot}%{_libdir}
%endif

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%doc README AUTHORS
%{_libdir}/libmono-curses.so
%{_libdir}/pkgconfig/mono-curses.pc
%{_prefix}/lib/mono/gac/mono-curses
%{_prefix}/lib/mono/mono-curses

%files doc
%doc ChangeLog
%{_prefix}/lib/monodoc/sources/mono-curses.*

