[![PyPi](https://img.shields.io/pypi/v/pyup-django.svg)](https://pypi.python.org/pypi/pyup-django)
[![Travis](https://img.shields.io/travis/pyupio/pyup-django.svg)](https://travis-ci.org/pyupio/pyup-django)

# About

Checks your installed Django release for known security vulnerabilities and displays a warning in the admin area.

# Installation

Install `pyup-django` with pip:

```
pip install pyup-django
```

and add it to your `INSTALLED_APPS`, before `django.contrib.admin`

```
INSTALLED_APPS = [
    'pyup_django',
    'django.contrib.admin',
]
```

# Screenshot

![insecure](insecure.png)

# Support

If you are using `pyup-django` in one of your projects, please consider getting a paid
[pyup.io](https://pyup.io) account. This is what makes projects like this possible.
