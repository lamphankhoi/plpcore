from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in plpcore/__init__.py
from plpcore import __version__ as version

setup(
	name='plpcore',
	version=version,
	description='PLPCORE',
	author='PLP',
	author_email='lamphankhoi@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
