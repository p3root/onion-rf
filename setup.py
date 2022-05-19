from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='onion-rf',
    version='0.9.7',
    author='Patrik',
    author_email='patrik.pfaffenbauer@p3-software.eu',
    description='Sending and receiving 433/315MHz signals with low-cost GPIO RF modules on a Onion Omega 2+',
    long_description=long_description,
    url='https://github.com/p3root/rpi-rf',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=[
        'rpi',
        'raspberry',
        'raspberry pi',
        'rf',
        'gpio',
        'radio',
        '433',
        '433mhz',
        '315',
        '315mhz',
        'onion',
        'omega'
    ],
    install_requires=['onion-gpio-sysfs'],
    scripts=['scripts/onion-rf_send', 'scripts/onion-rf_receive'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
