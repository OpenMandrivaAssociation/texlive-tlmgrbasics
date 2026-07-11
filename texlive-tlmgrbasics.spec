%global tl_name tlmgrbasics
%global tl_revision 75236

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A simplified documentation for tlmgr
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tlmgrbasics
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tlmgrbasics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tlmgrbasics.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides simplified documentation for tlmgr, the TeX Live
Manager. It describes the most commonly-used actions and options in a
convenient format.

