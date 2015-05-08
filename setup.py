from setuptools import setup 

setup(
	name="racpider",
	version="0.1",
	author="Shadow Cun",
	author_email="vinthony@gmail.com",
	description=("my web spider framewark"),
	license = "MIT",
	keywords = "spider crawling",
	url="http://vinthony.github.io/racpider/",
	packages=['src'],
	install_requires = [
				'beautifulsoup4>=4.0',
				'requests>=2.7',
 				'click>=3.3',
 				'redis',
 				'watchdog',
 				'pymongo',
 				'bitarray'
				],
	entry_points={
        'console_scripts': [
            'racpider=src.entry:cli'
        ]
    },
			
	)