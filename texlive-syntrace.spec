%global tl_name syntrace
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Labels for tracing in a syntax tree
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/syntrace
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/syntrace.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package adds support for traces in trees created using either the
synttree or the qtree package. The package provides two commands
(\traceLabel and \traceReference) to set and use a trace.

