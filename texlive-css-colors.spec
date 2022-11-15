Name:		texlive-css-colors
Version:	54512
Release:	1
Summary:	Named colors for web-safe design
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/css-colors
License:	lppl gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/css-colors.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/css-colors.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines web-safe colors for use with D.P.
Carlisle's color package. It is intended for both authors and
package writers (e.g. to create Beamer color themes).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/css-colors
%doc %{_texmfdistdir}/doc/latex/css-colors

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
