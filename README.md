[![PyPi](https://img.shields.io/pypi/v/pyup-django.svg)](https://pypi.python.org/pypi/pyup-django)
[![Travis](https://img.shields.io/travis/pyupio/pyup-django.svg)](https://travis-ci.org/pyupio/pyup-django)

# About

Displays a red warning banner if you are running an insecure Django release.

![insecure](insecure.png)

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

# How does it work?

`pyup-django` extends the admin base template and checks [https://pyup.io/api/v1/insecure/django/](https://pyup.io/api/v1/insecure/django/)
if the currently installed Django release is insecure.

Requests to the API are cached for 24 hours and won't leak any sensitive
information other than the servers IP address.


# Support

If you are using `pyup-django` in one of your projects, please consider getting a paid
[pyup.io](https://pyup.io) account. This is what makes projects like this possible.
