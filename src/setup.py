from setuptools import setup, find_packages

setup(
    name='PyOxfordDictionary',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT License',
    description='Python Package that pulls information from the Oxford Dictionary API',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/hvrlxy/PyOxfordDictionary',
    author='Ha Le',
    author_email='le.ha1@northeastern.edu'
)