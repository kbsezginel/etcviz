"""
Setup file for ETC Video Synthesizer Mode Development Python package.
"""
from setuptools import setup, find_packages


setup(
    name="etcviz",
    version="0.1.0",
    description="Tools for ETC video synthesizer mode development",
    author="Kutay B. Sezginel",
    author_email="kutaybs@gmail.com",
    url='https://github.com/kbsezginel/etcviz',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['pygame', 'imageio'],
    entry_points={
        'console_scripts': ['etcviz=etcviz.cli:main']
    }
)
