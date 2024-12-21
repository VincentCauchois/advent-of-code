from setuptools import setup, find_packages

# Package (minimal) configuration
setup(
    name="advent_of_code",
    version="1.0.0",
    description="Python library for 'Advent of Code' solvers",
    packages=find_packages(),  # __init__.py folders search
    install_requires=[],
)