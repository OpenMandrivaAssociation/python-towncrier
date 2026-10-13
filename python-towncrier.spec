Name:		python-towncrier
Version:	26.9.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/towncrier/towncrier-%{version}.tar.gz
Summary:	Building newsfiles for your project.
URL:		https://pypi.org/project/towncrier/
License:	None
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(jinja2)
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
