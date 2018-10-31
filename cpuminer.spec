Name:		cpuminer
Version:	2.3.2
Release:	6
Summary:	multi-threaded CPU miner for Litecoin and Bitcoin
License:	GPLv2+
Group:		Monitoring
URL:		https://github.com/pooler/cpuminer
Source0:	https://github.com/downloads/pooler/cpuminer/pooler-%{name}-%{version}.tar.gz 

BuildRequires:	pkgconfig(libcurl)

%description
This is a multi-threaded CPU miner for Litecoin and Bitcoin,
fork of Jeff Garzik's reference cpuminer.

%prep
%setup -q

%build
%ifarch %arm
%global optflags %{optflags} -O3 -mfpu=neon
%else
%global optflags %{optflags} -O3
%endif

%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README AUTHORS NEWS
%{_bindir}/minerd
