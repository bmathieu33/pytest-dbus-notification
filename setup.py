# coding=utf-8
from __future__ import absolute_import

from setuptools import setup
import codecs

def read(filename):
    return unicode(codecs.open(filename, encoding='utf-8').read())


long_description = '\n\n'.join([read('README.rst'),
                                read('CHANGES.rst')])

classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Desktop Environment',
    'Topic :: Software Development :: Testing',
    'Topic :: Utilities',
    ]

setup(
    author="Bertrand Mathieu",
    author_email="bert.mathieu at gmail.com",
    url='https://github.com/bmathieu33/pytest-dbus-notification',
    version='1.0.0',
    description="D-BUS notifications for pytest results.",
    long_description=long_description,
    name="pytest-dbus-notification",
    keywords="pytest, pytest-, dbus, py.test",
    classifiers=classifiers,
    py_modules=['pytest_dbus_notification'],
    install_requires=[
        'pytest'
        ],
    entry_points={
        'pytest11': ['pytest_dbus_notification = pytest_dbus_notification',]
        },)
