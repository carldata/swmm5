from setuptools import setup, find_packages

setup(
    name='swmm5',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    license='MIT',
    description='SWMM5 runner',
    long_description=open('README.md').read(),
    install_requires=[''],
    url='https://github.com/carldata/swmm5',
    author='Jakub Wenta',
    author_email='jakubwenta@gmail.com'
)