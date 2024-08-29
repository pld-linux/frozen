#
# Conditional build:
%bcond_without	tests	# unit tests
#
Summary:	Header-only, constexpr alternative to gperf for C++14 users
Summary(pl.UTF-8):	Składająca się z samych nagłówków, wykorzystująca constexpr alternatywa dla gperfa dla C++14
Name:		frozen
Version:	1.1.1
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/serge-sans-paille/frozen/tags
Source0:	https://github.com/serge-sans-paille/frozen/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9c498c6845e4e33ea686770d3d429aa2
Patch0:		%{name}-gcc.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-fix-arch-in-cmake.patch
URL:		https://github.com/serge-sans-paille/frozen
BuildRequires:	cmake >= 3.8
BuildRequires:	libstdc++-devel >= 6:5
%if %{with tests}
BuildRequires:	libstdc++-devel >= 6:7
%endif
BuildRequires:	rpmbuild(macros) >= 1.605
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Header-only library that provides 0 cost initialization for immutable
containers, fixed-size containers, and various algorithms.

Frozen provides:
- immutable (a.k.a. frozen), constexpr-compatible versions of
  std::set, std::unordered_set, std::map and std::unordered_map.
- fixed-capacity, constinit-compatible versions of std::map and 
  std::unordered_map with immutable, compile-time selected keys mapped
  to mutable values.
- 0-cost initialization version of std::search for frozen needles
  using Boyer-Moore or Knuth-Morris-Pratt algorithms.

%description -l pl.UTF-8
Składająca się z samych nagłówków biblioteka zapewniająca bezkosztowe
inicjowanie niezmiennych kontenerów, kontenery o stałym rozmiarze i
różne algorytmy.

W tym:
- niezmienne (czyli zamrożone - frozen), zgodne z constexpr wersje
  std::set, std::unordered_set, std::map, std::unordered_map.
- stałej pojemności, zgodne z constinit wersje std::map i
  std::unordered_map z niezmiennymi, wybieranymi w czasie kompilacji
  kluczami odwzorowywanymi na zmienne wartości.
- wersja std::search o bezkosztowym inicjowaniu dla niezmiennych
  wartości wyszukiwanych, wykorzystująca algorytmy Boyera-Moore'a i
  Knuta-Morrisa-Pratta.

%package devel
Summary:	Header-only, constexpr alternative to gperf for C++14 users
Summary(pl.UTF-8):	Składająca się z samych nagłówków, wykorzystująca constexpr alternatywa dla gperfa dla C++14
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:5

%description devel
Header-only library that provides 0 cost initialization for immutable
containers, fixed-size containers, and various algorithms.

Frozen provides:
- immutable (a.k.a. frozen), constexpr-compatible versions of
  std::set, std::unordered_set, std::map and std::unordered_map.
- fixed-capacity, constinit-compatible versions of std::map and 
  std::unordered_map with immutable, compile-time selected keys mapped
  to mutable values.
- 0-cost initialization version of std::search for frozen needles
  using Boyer-Moore or Knuth-Morris-Pratt algorithms.

%description devel -l pl.UTF-8
Składająca się z samych nagłówków biblioteka zapewniająca bezkosztowe
inicjowanie niezmiennych kontenerów, kontenery o stałym rozmiarze i
różne algorytmy.

W tym:
- niezmienne (czyli zamrożone - frozen), zgodne z constexpr wersje
  std::set, std::unordered_set, std::map, std::unordered_map.
- stałej pojemności, zgodne z constinit wersje std::map i
  std::unordered_map z niezmiennymi, wybieranymi w czasie kompilacji
  kluczami odwzorowywanymi na zmienne wartości.
- wersja std::search o bezkosztowym inicjowaniu dla niezmiennych
  wartości wyszukiwanych, wykorzystująca algorytmy Boyera-Moore'a i
  Knuta-Morrisa-Pratta.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_TESTING=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS README.rst
%{_includedir}/frozen
%{_datadir}/cmake/frozen
