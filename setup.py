# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='python-cnab',
    version='0.1.20',
    author='Trustcode',
    author_email='suporte@trustcode.com.br',
    url='https://github.com/Trust-Code/python-cnab',
    keywords=['cnab', 'cnab240'],
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    package_data={
        'cnab240': [
            'bancos/banco_brasil/specs/*.json',
            'bancos/bradesco/specs/*.json',
            'bancos/bradesco_cobranca_400/specs/*.json',
            'bancos/bradesco_cobranca_retorno_400/specs/*.json',
            'bancos/bradescoPagFor/specs/*.json',
            'bancos/cecred/specs/*.json',
            'bancos/cef/specs/*.json',
            'bancos/hsbc/specs/*.json',
            'bancos/itau/specs/*.json',
            'bancos/itauSispag/specs/*.json',
            'bancos/santander/specs/*.json',
            'bancos/sicoob/specs/*.json',
            'bancos/sicredi/specs/*.json',
        ],
    },
    install_requires=[
        'setuptools-git==1.1'
    ],
    license='MIT',
    description='Lib para gerar arquivo CNAB - Integração bancária',
    long_description=open('README.md', 'r').read(),
    download_url='https://github.com/Trust-Code/python-cnab',
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
