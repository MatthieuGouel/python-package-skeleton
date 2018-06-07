"""Setup for {{cookiecutter.project_slug}} package."""
import uuid

from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

INSTALL_REQS = parse_requirements('requirements.txt', session=uuid.uuid1())
REQS = [str(ir.req) for ir in INSTALL_REQS]

setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.project_version }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}",
    description="{{ cookiecutter.project_short_description }}",
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
    include_package_data=True,
    packages=find_packages(),
    install_requires=REQS
)
