from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='notebook-ed',
    version='0.1.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'notebook-ed=notebook_ed.converter:main',
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
    url='https://github.com/w3cdpass/notebook-ed.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
