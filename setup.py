from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='roygbiv',
    version='0.1',
    description='',
    author='Micah Walter Studio',
    url='https://github.com/micahwalterstudio/roygbiv',
    requires=['colormath'],
    install_requires=['colormath'],
    packages=packages,
    scripts=[],
    download_url='https://github.com/micahwalterstudio/roygbiv/tarball/master',
license='MIT')