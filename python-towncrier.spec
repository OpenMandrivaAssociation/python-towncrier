Name:		python-towncrier
Version:	24.8.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/towncrier/towncrier-%{version}.tar.gz
Summary:	Building newsfiles for your project.
URL:		https://pypi.org/project/towncrier/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(incremental)
BuildRequires:	python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(toml)
BuildSystem:	python
BuildArch:	noarch

%description
Building newsfiles for your project.

%prep
%autosetup -p1 -n towncrier-%{version}

%files
%{_bindir}/towncrier
%{py_sitedir}/towncrier
%{py_sitedir}/towncrier-*.*-info
