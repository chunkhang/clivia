from setuptools import setup, find_packages
from clivia import constants

setup(
	name = 'clivia',
	packages = ['clivia', 'clivia.text'],
	python_requires='>=3',
	version = constants.VERSION,
	description = 'A library for simple CLI development in Python',
	author = 'Marcus Mu',
	author_email = 'chunkhang@gmail.com',
	license = 'UNLICENSE',
	url = 'https://github.com/chunkhang/clivia',
	keywords = [
		'clivia'
	], 
	classifiers = [
		'Intended Audience :: Developers',
		'Environment :: Console',
		'Programming Language :: Python :: 3 :: Only'
	]
)