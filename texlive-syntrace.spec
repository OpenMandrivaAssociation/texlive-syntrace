Name:		texlive-syntrace
Version:	15878
Release:	1
Summary:	Labels for tracing in a syntax tree
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/syntrace
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package adds support for for traces in trees created using
either the synttree or the qtree package. The package provides
two commands (\traceLabel and \traceReference) to set and use a
trace.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/syntrace/syntrace.sty
%doc %{_texmfdistdir}/doc/latex/syntrace/README
%doc %{_texmfdistdir}/doc/latex/syntrace/syntrace.pdf
#- source
%doc %{_texmfdistdir}/source/latex/syntrace/syntrace.dtx
%doc %{_texmfdistdir}/source/latex/syntrace/syntrace.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
