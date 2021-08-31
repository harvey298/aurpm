# aurpm &middot; [![GitHub license](https://img.shields.io/github/license/harvey298/aurpm.svg)](https://github.com/harvey298/aurpm/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/harvey298/aurpm.svg)](https://github.com/harvey298/aurpm/stargazers)

## Overview

[aurpm](https://github.com/harvey298/aurpm/) is an AUR-helper written by [harvey298](https://www.github.com/harvey298/) for easy management of packages installed from the [Arch User Repository](https://aur.archlinux.org/).

## Table of Contents

1. [Install](#install)
   - [Prerequisites](#prerequisites)
   - [Installation Instructions](#installation-instructions)
2. [License](#license)
3. [Contributing](#contributing)

### Current useability
As for right now I rewriting aurpm in Rust, it works (ish)
its working directory is `$HOME/.aurpm/work`

If you find any issues please do make a issue with the error message!

How to Install a package:
`aurpm -S [package Name]`

## Install

### Prerequisites

 - Git
 - [Rust - Arch Linux Package](https://archlinux.org/packages/?name=rust) (make) | [Rust - Website](https://www.rust-lang.org/) (make)

### Make Instructions

you can run `cargo build --release` or you can run `make`

### Installation Instructions

TBD

## License

This product is licensed under the [MIT License](https://github.com/harvey298/aurpm/blob/main/LICENSE). This project is available for commercial use, modification, distribution, and private use.

## Contributing

Pull requests are encouraged. For major changes with the project please open an issue about what you would like to change. Thank you for participating in the development of this AUR package manager!