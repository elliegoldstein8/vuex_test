from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vuex_test/__init__.py
from vuex_test import __version__ as version

setup(
	name="vuex_test",
	version=version,
	description="testing vuex to vuejs",
	author="rse",
	author_email="joyjoyolata@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
