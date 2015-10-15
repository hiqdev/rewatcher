from setuptools import setup, find_packages

setup(
    name='rewatcher',
    version='0.0.1',
    author='Andrii Vasyliev',
    author_email='sol@hiqdev.com',
    packages=find_packages(),
    description='Repositories watcher',
    long_description=(
        "Scans directory tree recursively to find unsynced repositories."
    ),
    scripts=['bin/rewatcher'],
)
