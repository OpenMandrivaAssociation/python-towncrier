# Created by pyp2rpm-3.3.5
%global pypi_name towncrier

Name:           python-%{pypi_name}
Version:        19.2.0
Release:        2
Summary:        Building newsfiles for your project
Group:          Development/Python
License:        MIT
URL:            https://github.com/hawkowl/towncrier
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(incremental)
BuildRequires:  python3dist(incremental)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toml)

%description
Hear ye, hear ye, says the towncrier towncrier is a utility to produce useful,
summarised news files for your project. Rather than reading the Git history as
some newer tools to produce it, or having one single file which developers all
write to, towncrier reads "news fragments" which contain information useful to
end users.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/towncrier
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
