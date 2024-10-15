# Copyright 2024-present, Moverse
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import io
import logging
import os

from setuptools import find_packages, setup

logger = logging.getLogger()
logging.basicConfig(format="%(levelname)s - %(message)s")


def get_readme():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_requirements():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    requirements = []
    with open(os.path.join(base_dir, "requirements.txt"), encoding="utf-8") as f:
        requirements.extend(line.strip() for line in f.readlines())
    return requirements


PACKAGE_NAME = "vcpkg-sbom"
VERSION = "0.0.6"
AUTHOR = "Moverse P.C."
EMAIL = "info@moverse.ai"
LICENSE = "MIT"
URL = "https://github.com/moverseai/vcpkg-sbom/"
CODE_URL = "https://github.com/moverseai/vcpkg-sbom/"
DOCS_URL = "https://github.com/moverseai/vcpkg-sbom/"
DESCRIPTION = "A python CLI tool to extract a merged software bill of materials and license info from a vcpkg manifest."
KEYWORDS = [
    "software-bill-of-materials",
    "developer-tools",
    "sbom",
    "spdx",
    "vcpkg",
    "license",
    "eula",
    "cpp",
    "c++",
    "dependencies",
    "oss",
]

if __name__ == "__main__":
    logger.info(f"Installing {PACKAGE_NAME} (v{VERSION}) ...")
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=EMAIL,
        description=DESCRIPTION,
        long_description=get_readme(),
        long_description_content_type="text/markdown",
        keywords=KEYWORDS,
        licence_file="LICENSE",
        url=URL,
        project_urls={
            "Documentation": DOCS_URL,
            "Source": CODE_URL,
        },
        packages=find_packages(exclude=("docs", "data", "build", "dist", "scripts")),
        install_requires=get_requirements(),
        include_package_data=True,
        python_requires=">=3.8",
        package_dir={"vcpkg_sbom": "vcpkg_sbom"},
        package_data={},
        entry_points={
            "console_scripts": [
                "vcpkg-sbom=vcpkg_sbom.__init__:run",
            ],
        },
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "License :: OSI Approved :: MIT License",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Build Tools",
            "Topic :: System :: Software Distribution",
            "Environment :: Console",
        ],
    )
