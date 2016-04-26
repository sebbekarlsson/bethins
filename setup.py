from distutils.core import setup
import setuptools


setup(
    name='bethins',
    version='1.0',
    install_requires=[
        'flask',
        'flask-wtf',
        'wtforms',
        'pymongo'
    ],
    packages=[
        'bethins'
    ],
    entry_points={
        "console_scripts": [
        ]
    },
   )
