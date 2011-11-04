# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/syntrace
# catalog-date 2007-03-13 15:26:21 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-syntrace
Version:	1.1
Release:	1
Summary:	Labels for tracing in a syntax tree
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/syntrace
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package adds support for for traces in trees created using
either the synttree or the qtree package. The package provides
two commands (\traceLabel and \traceReference) to set and use a
trace.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/syntrace/syntrace.sty
%doc %{_texmfdistdir}/doc/latex/syntrace/README
%doc %{_texmfdistdir}/doc/latex/syntrace/syntrace.pdf
#- source
%doc %{_texmfdistdir}/source/latex/syntrace/syntrace.dtx
%doc %{_texmfdistdir}/source/latex/syntrace/syntrace.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
