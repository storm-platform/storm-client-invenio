# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# invenio-client is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Client for Invenio RDM instances"""

import os
from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "pytest-invenio>=1.4.0",
]

extras_require = {
    "docs": [
        "Sphinx>=3,<4",
    ],
    "tests": tests_require,
}

extras_require["all"] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = [
    "Babel>=2.8",
]

install_requires = [
    "httpx>=0.19.0",
    "pydash>=5.1.0",
    "aiofiles>=0.7.0",
    "cachetools>=4.2.4",
    "typeguard>=2.13.0",
    # Storm dependencies
    "storm-hasher @ git+https://github.com/storm-platform/storm-hasher",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("invenio_client", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="invenio-client",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords=["Storm Platform", "Invenio RDM", "Client library"],
    license="MIT",
    author="Felipe Menino Carlos",
    author_email="felipe.carlos@inpe.br",
    url="https://github.com/storm-platform/invenio-client",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={},
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
)
