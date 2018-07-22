"""Setup for {{cookiecutter.project_slug}} package."""

from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.project_version }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=open("README.md").read(),
    license="MIT",
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],
)
