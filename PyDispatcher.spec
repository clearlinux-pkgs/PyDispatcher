#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyDispatcher
Version  : 2.0.5
Release  : 6
URL      : https://files.pythonhosted.org/packages/cd/37/39aca520918ce1935bea9c356bcbb7ed7e52ad4e31bff9b943dfc8e7115b/PyDispatcher-2.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/cd/37/39aca520918ce1935bea9c356bcbb7ed7e52ad4e31bff9b943dfc8e7115b/PyDispatcher-2.0.5.tar.gz
Summary  : Multi-producer-multi-consumer signal dispatching mechanism
Group    : Development/Tools
License  : BSD-3-Clause
Requires: PyDispatcher-python3
Requires: PyDispatcher-license
Requires: PyDispatcher-python
BuildRequires : buildreq-distutils3

%description
PyDispatcher is an enhanced version of Patrick K. O'Brien's
        original dispatcher.py module.  It provides the Python
        programmer with a robust mechanism for event routing within
        various application contexts.
        
        Included in the package are the robustapply and saferef
        modules, which provide the ability to selectively apply
        arguments to callable objects and to reference instance
        methods using weak-references.

%package license
Summary: license components for the PyDispatcher package.
Group: Default

%description license
license components for the PyDispatcher package.


%package python
Summary: python components for the PyDispatcher package.
Group: Default
Requires: PyDispatcher-python3
Provides: pydispatcher-python

%description python
python components for the PyDispatcher package.


%package python3
Summary: python3 components for the PyDispatcher package.
Group: Default
Requires: python3-core

%description python3
python3 components for the PyDispatcher package.


%prep
%setup -q -n PyDispatcher-2.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534700439
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/PyDispatcher
cp license.txt %{buildroot}/usr/share/doc/PyDispatcher/license.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/PyDispatcher/license.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
