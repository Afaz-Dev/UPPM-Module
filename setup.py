from setuptools import setup, find_packages

setup(
    name='uppm',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'curl_cffi'
    ],
)
