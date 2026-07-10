%global tl_name css-colors
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	Named colors for web-safe design
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/css-colors
License:	lppl gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/css-colors.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/css-colors.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines web-safe colors for use with D.P. Carlisle's color
package. It is intended for both authors and package writers (e.g. to
create Beamer color themes).

