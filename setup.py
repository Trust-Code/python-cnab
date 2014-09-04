# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='cnab240',
    version='0.01',
    author='Tracy Web Technologies',
    author_email='contato@tracy.com.br',
    url='https://github.com/TracyWebTech/cnab240',
    packages=find_packages(),
    package_data={
        'cnab240': ['bancos/*/*/*.json']
    },
    zip_safe=False,
    install_requires=[],
    provides=[
        'cnab240'
    ],
    license='MIT',
    description='Classe para gerar arquivo de remessa e leitura de retorno no '
                                                            'padrão CNAB240',
    long_description=open('README.md', 'r').read(),
    download_url='https://github.com/TracyWebTech/cnab240',
    scripts=[],
    classifiers=[],
    platforms='any',
    test_suite='',
    tests_require=[],
)
