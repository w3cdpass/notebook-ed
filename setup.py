from setuptools import setup, find_packages

setup(
    name='py2nb',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'py2nb=py2nb.converter:main',
        ],
    },
    install_requires=[
        'nbformat',
        'colorama'
    ],
    author='w3cdpass',
    author_email='kupasva663@gmail.com',
    description='A package to convert .py files to .ipynb and delete the original .py files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/w3cdpass/py2nb.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
