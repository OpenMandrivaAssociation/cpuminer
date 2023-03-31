Name:		cpuminer
Version:	2.5.1
Release:	2
Summary:	multi-threaded CPU miner for Litecoin and Bitcoin
License:	GPLv2+
Group:		Monitoring
URL:		https://github.com/pooler/cpuminer
Source0:	https://github.com/pooler/cpuminer/releases/download/v%{version}/pooler-cpuminer-%{version}.tar.gz

BuildRequires:	pkgconfig(libcurl)

%description
This is a multi-threaded CPU miner for Litecoin and Bitcoin,
fork of Jeff Garzik's reference cpuminer.

%prep
%autosetup -p1

%build
%ifarch %arm
%global optflags %{optflags} -O3 -mfpu=neon
%else
%global optflags %{optflags} -O3
%endif

%configure
%make_build

%install
%make_install

%files
%doc README AUTHORS NEWS
%{_bindir}/minerd
%{_mandir}/man1/minerd.1*
