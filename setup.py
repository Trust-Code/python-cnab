# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='python-cnab',
    version='0.1.2',
    author='Trustcode',
    author_email='suporte@trustcode.com.br',
    url='https://github.com/Trust-Code/python-cnab',
    keywords=['cnab', 'cnab240'],
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    install_requires=[
        'setuptools-git'
    ],
    license='MIT',
    description='Lib para gerar arquivo CNAB - Integração bancária',
    long_description=open('README.md', 'r').read(),
    download_url='https://github.com/kmee/cnab',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock',
    ],
)
