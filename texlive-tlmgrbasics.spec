Name:		texlive-tlmgrbasics
Version:	70175
Release:	1
Summary:	A simplified documentation for tlmgr
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tlmgrbasics
License:	gpl2+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlmgrbasics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tlmgrbasics.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides simplified documentation for tlmgr, the
TeX Live Manager. It describes the most commonly-used actions
and options in a convenient format.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/support/tlmgrbasics

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
