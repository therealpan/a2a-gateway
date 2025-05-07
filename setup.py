# setup.py
from setuptools import setup

setup(
    name='a2a-gateway',
    version='0.1.0',
    py_modules=['a2a_gateway_cli'],
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'a2a-gateway = a2a_gateway_cli:main'
        ]
    },
    author='Innoturismo',
    author_email='info@innoturismo.com',
    description='CLI tool to interact with A2A Gateway for interoperable AI agents',
    url='https://github.com/therealpan/a2a-gateway',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
