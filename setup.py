from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in click_app/__init__.py
from click_app import __version__ as version

setup(
	name='click_app',
	version=version,
	description='CliCK Customizations',
	author='mrosero@clickcg.co',
	author_email='mrosero@clickcg.co',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
