%global common_desc \
This package contains a Sphinx extension for BibTeX style citations.\
This extension allows BibTeX citations to be inserted into documentation\
generated by Sphinx, via a bibliography directive, and a cite role,\
which work similarly to LaTeX thebibliography environment and cite command.

Name:           python-sphinxcontrib-bibtex
Version:        0.4.0
Release:        4
Summary:        Sphinx extension for BibTeX style citations
License:        BSD
URL:            https://github.com/mcmtroffaes/sphinxcontrib-bibtex
Source0:        https://github.com/mcmtroffaes/sphinxcontrib-bibtex/archive/%{version}/sphinxcontrib-bibtex-%{version}.tar.gz
BuildArch:      noarch
# Use orderedset instead of oset; the latter has a dead upstream
Patch0000:      %{name}-orderedset.patch

BuildRequires:  python2-coverage python2-devel python2-latexcodec python2-nose python2-orderedset
BuildRequires:  python2-pybtex python2-pybtex-docutils python2-setuptools python2-six
BuildRequires:  python2-sphinx python2-sphinx-testing
BuildRequires:  python3-coverage python3-devel python3-latexcodec python3-nose python3-orderedset
BuildRequires:  python3-pybtex python3-pybtex-docutils python3-setuptools python3-six
BuildRequires:  python3-sphinx python3-sphinx-testing


%description
%common_desc

%package -n python2-sphinxcontrib-bibtex
Summary:        Sphinx extension for BibTeX style citations
Requires:       python2-latexcodec python2-orderedset python2-pybtex python2-pybtex-docutils python2-six
Provides:       bundled(jquery)
Provides:       bundled(js-underscore)
%{?python_provide:%python_provide python2-sphinxcontrib-bibtex}

%description -n python2-sphinxcontrib-bibtex
%common_desc

%package -n python3-sphinxcontrib-bibtex
Summary:        Sphinx extension for BibTeX style citations
Requires:       python3-latexcodec python3-orderedset python3-pybtex python3-pybtex-docutils python3-six
Provides:       bundled(jquery)
Provides:       bundled(js-underscore)
%{?python_provide:%python_provide python3-sphinxcontrib-bibtex}

%description -n python3-sphinxcontrib-bibtex
%common_desc

%package help
Summary:       Provides help and documentation for python-sphinxcontrib-bibtex
Obsoletes:     python-sphinxcontrib-bibtex-doc < %{version}-%{release}
Provides:      python-sphinxcontrib-bibtex-doc = %{version}-%{release}

%description help
Help and documentation for python-sphinxcontrib-bibtex.

%prep
%setup -q -c
cd sphinxcontrib-bibtex-%{version}
%patch0000
cd -

rm -rf sphinxcontrib-bibtex-%{version}/test/{test_issue1.py,issue1}

cp -a sphinxcontrib-bibtex-%{version} python3-sphinxcontrib-bibtex-%{version}

%build
cd sphinxcontrib-bibtex-%{version}
%py2_build
cd -

cd python3-sphinxcontrib-bibtex-%{version}
%py3_build
cd -

cd python3-sphinxcontrib-bibtex-%{version}
PYTHONPATH=$PWD sphinx-build-%{python3_version} doc html
rm -rf html/{.buildinfo,.doctrees}
cd -

%install
cd sphinxcontrib-bibtex-%{version}
%py2_install
cd -

cd python3-sphinxcontrib-bibtex-%{version}
%py3_install
cd -

%check
cd sphinxcontrib-bibtex-%{version}
PYTHONPATH=$PWD nosetests-%{python2_version} -v
cd -

cd python3-sphinxcontrib-bibtex-%{version}
PYTHONPATH=$PWD nosetests-%{python3_version} -v
cd -

%files -n python2-sphinxcontrib-bibtex
%license sphinxcontrib-bibtex-%{version}/LICENSE.rst
%{python2_sitelib}/sphinxcontrib/
%{python2_sitelib}/sphinxcontrib_bibtex*

%files -n python3-sphinxcontrib-bibtex
%license python3-sphinxcontrib-bibtex-%{version}/LICENSE.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_bibtex*

%files help
%doc python3-sphinxcontrib-bibtex-%{version}/html/*

%changelog
* Tue Mar 10 2020 tianhang <1748215448@qq.com> - 0.4.0-4
- Package init
