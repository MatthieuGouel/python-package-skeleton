"""Setup file for skeleton package."""
import uuid

from setuptools import setup, find_packages, find_version
from pip.req import parse_requirements

INSTALL_REQS = parse_requirements('requirements.txt', session=uuid.uuid1())
REQS = [str(ir.req) for ir in INSTALL_REQS]

setup(
    name="skeleton",
    version=find_version('skeleton', '__init__.py'),
    author="Matthieu Gouel",
    author_email="matthieu.gouel@gmail.com",
    description="Skeleton for Python3 projects",
    long_description=open('README.md').read(),
    license='MIT',
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'License :: OSI Approved :: MIT License',
    ],
    url="https://github.com/matthieugouel/python-package-skeleton",
    include_package_data=True,
    packages=find_packages(),
    install_requires=REQS
)
