# 📓 Software Bill-of-Materials for `vcpkg` manifests.

[![Python Version](https://img.shields.io/pypi/pyversions/vcpkg-sbom.svg)](https://pypi.org/project/vcpkg-sbom)
[![PyPI](https://img.shields.io/pypi/v/vcpkg-sbom.svg)](https://pypi.org/project/vcpkg-sbom)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/vcpkg-sbom)
![PyPI - Status](https://img.shields.io/pypi/status/vcpkg-sbom)
[![GitHub Release Date](https://img.shields.io/github/release-date/moverseai/vcpkg-sbom)](https://github.com/moverseai/vcpkg-sbom/releases)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/vcpkg-sbom?style=plastic&logo=python&logoColor=magenta&color=magenta&link=https%3A%2F%2Fpypi.org%2Fproject%2Fvcpkg-sbom%2F)](https://pypi.org/project/vcpkg-sbom/)

![GitHub repo size](https://img.shields.io/github/repo-size/moverseai/vcpkg-sbom)
[![PyPI - License](https://img.shields.io/pypi/l/vcpkg-sbom)](https://github.com/moverseai/vcpkg-sbom/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Black Format](https://github.com/moverseai/rerun-animation/actions/workflows/black.yaml/badge.svg)](https://github.com/moverseai/vcpkg-sbom/actions/workflows/black.yaml)
[![Discord](https://dcbadge.limes.pink/api/server/bQc7B6qSPd?style=flat)](https://discord.gg/bQc7B6qSPd)

___

<!-- [![Downloads](https://static.pepy.tech/badge/rerun-animation/month)](https://pepy.tech/project/rerun-animation) -->

>A python command line tool to extract a combined software bill of materials and license info from a vcpkg manifest.

## Installation

### :snake: [PyPi](https://pypi.org/project/vcpkg-sbom/)

Open a command line and run:
```py
pip install vcpkg-sbom
```

---

### :octocat: Local

Downlaod the repo:
```sh
git clone https://github.com/moverseai/vcpkg-sbom vcpkg-sbom
cd vcpkg-sbom
```

From the repo's root path run:

```py
pip install .
```

For an editable install run:

```py
pip install -e .
```

## :keyboard: Usage

```sh
vcpkg-sbom PATH/TO/PROJECT/vcpkg_installed
```

| ID | Package |
|:---:|:---|
| 0  | package name #1 |
| 1  | package name #2 |
| 2  | package name #3 |
| ... | package name #N |

Merging spdx:  ━━━━━━━━━━━━━━━━━━ 100% 0:00:00

Extracting & merging copyrights ...      

Merging copyrights:  ━━━━━━━━━━━━━━━━━━   0% -:--:--

> [!NOTE]  
> The output file is a `SPDX-2.3` `SPDXRef-DOCUMENT` that merges all available `*.spdx.json` files from the manifest's installed packages.

> [!TIP]  
> The default `triplet` is `x64-windows` and is appended to the cmd line given path before searching for all installed packages.

> [!IMPORTANT]  
> The output files (`*.spdx.json`, and optionally, `*_license_info.json` and `*_EULA.txt`) are written to the current working directory from where the command was executed.

---

### 🔧 Command Line API

```bash
$ vcpkg-sbom --help
usage: A software bill of materials extracter and merger for `vcpkg` manifest projects.

positional arguments:
  vcpkg_root            Path to the `vcpkg_installed` folder of your manifest project.

options:
  -h, --help            show this help message and exit
  -t TRIPLET, --triplet TRIPLET
                        The `vcpkg` triplet to use.
  -p PROJECT, --project PROJECT
                        The project's name that will be used for the merged output files.
  -n NAMESPACE, --namespace NAMESPACE
                        The software's namespace to use for the `spdx` file.
  -o ORGANIZATION, --organization ORGANIZATION
                        The organization or company name to use for the `spdx` file.
  -e EMAIL, --email EMAIL
                        The email to use for the `spdx` file.
  -c, --copyright       Additionally extract and merge all copyright files in a `*.txt` file.
  -l, --license         Additionally extract and merge all license types in a `*.json` file.
```

> [!IMPORTANT]
> Default values:
>   - `triplet`: _x64-windows_
>   - `project`: _project_
>   - `namespace`: _https://spdx.org/spdxdocs/_
>   - `organization`: _org_
>   - `email`: _info@org.com_
>   - `copyright`: flag to enable copyright file merging
>   - `license`: flag to enable license info merging


> [!TIP]  
> Info on how to choose a proper namespace can be found [here](https://spdx.github.io/spdx-spec/v2-draft/document-creation-information/#65-spdx-document-namespace-field)

## Acknowledgements / Material

- vcpkg` spdx [info](https://learn.microsoft.com/en-us/vcpkg/reference/software-bill-of-materials) and [discussion](https://github.com/microsoft/vcpkg/discussions/40700) @ Microsoft docs
- The merging code was adapted from https://github.com/philips-software/SPDXMerge
- The `jq` script [here](https://edgebit.io/blog/merge-two-sboms/) is a nice alternative
- [licensecpp](https://github.com/cenit/licencpp/tree/master) is another approach starting from the `vcpkg` manifest.json file.

## Disclaimer / Limitations

> [!WARNING]
> As indicated at the `vcpkg` [docs](https://learn.microsoft.com/en-us/vcpkg/reference/vcpkg-json#license):
> _The licensing information provided for each package in the vcpkg registry represents Microsoft's best understanding of the licensing requirements. However, this information may not be definitive. Users are advised to verify the exact licensing requirements for each package they intend to use, as it is ultimately their responsibility to ensure compliance with the applicable licenses._

While `vcpkg` offers a lot of information about licensing, this information should be scrutinized. Any tool that builds on top of this information provided by `vcpkg` is reliant on the legibility of the provided data, and should thus, be also scrutinized for correctness.