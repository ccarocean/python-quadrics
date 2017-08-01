# -* coding: utf-8 -*-
# pylint: disable=invalid-name
"""Build, test, and install quadrics."""

import os
import re
from setuptools import setup


PWD = os.path.dirname(__file__)

version = re.search(
    r"^__version__\s*=\s*'(.*)'",
    open('quadrics/__init__.py').read(),
    re.M).group(1)

with open('README.rst', 'r') as f:
    long_desc = f.read()


def load_requirements_file(filename):
    requirements = []
    with open(filename) as file:
        for line in file:
            if line.startswith('-r'):
                requirements.extend(load_requirements_file(
                    os.path.join(os.path.dirname(filename), line.split()[1])))
            elif line.startswith('#') or line.startswith('-'):
                pass
            else:
                requirements.append(line.rstrip('\n'))
    return sorted(requirements)


extras_require = {}
for filename in os.listdir(os.path.join(PWD, 'requirements')):
    extras_require[os.path.splitext(filename)[0]] = (
        load_requirements_file(os.path.join(PWD, 'requirements', filename)))
install_requires = extras_require.pop('default')
tests_require = extras_require.pop('tests', [])
del extras_require['dev']


setup(
    name='quadrics',
    version=version,
    description='Solve for and compute properties of quadric surfaces.',
    author='Michael R. Shannon',
    author_email='mrshannon.aerospace@gmail.com',
    license='MIT',
    url='https://github.com/ccarocean/python-quadrics',
    download_url=('https://github.com/ccarocean/python-quadrics/'
                  'archive/master.zip'),
    long_description=long_desc,
    packages=['quadrics'],
    platforms=['any'],
    keywords=['math', 'geometry', 'plotting'],
    install_requires=install_requires,
    extras_require=extras_requires,
    test_suite='tests',
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    zip_safe=True
)
