from setuptools import setup, find_packages

setup(
    name='swmm5-api',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='SWMM5 runner',
    long_description=open('README.md').read(),
    install_requires=[''],
    url='https://https://github.com/carldata/swmm5-api',
    author='Jakub Wenta',
    author_email='jakubwenta@gmail.com'
)