# aurpm &middot; [![GitHub license](https://img.shields.io/github/license/harvey298/aurpm.svg)](https://github.com/harvey298/aurpm/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/harvey298/aurpm.svg)](https://github.com/harvey298/aurpm/stargazers)

## Overview

[aurpm](https://github.com/harvey298/aurpm/) is an AUR-helper written by [harvey298](https://www.github.com/harvey298/) for easy management of packages installed from the [Arch User Repository](https://aur.archlinux.org/).

## Table of Contents

1. [Install](#install)
   - [Prerequisites](#prerequisites)
   - [Installation Instructions](#installation-instructions)
2. [License](#license)
3. [Contributing](#contributing)

### Out of Date!!

### Current useability
As for right now I am refactoring aurpm and current can only install packages

How to Install:
`aurpm -S [PKG Name]`

if you are currently having issues with this beta release (Yes I'm calling it a beta release) please feel free to use the code in the old directory!!

you can find a UNTESTED build of aurpm in the dist directory!

## Config
In this version of aurpm we have a config (optional)

the config can grant some more features such as using /tmp as its work directory
it can be found along side the source code.

To note by default (default being their is no config present)
all in testing features are disabled such as using /tmp

if you wish to use the new features, just copy the config to the accepted config directorys they being
`$HOME/.config/aurpm/aurpm.conf`
and
`$HOME/.aurpm/aurpm.conf`


## Install

### Prerequisites

 - Git
 - [Python 3.7+](https://www.python.org/downloads/)
 - [Pyinstaller](https://www.pyinstaller.org/) (make)
 - [harvey's colour-lib](https://github.com/harvey298/colour-lib) (make)

### Make Instructions

you must have Pyinstaller to make this, you can execute the make file using make or running Bash -x makefile

this is meant to replace the file index.py!!

### Installation Instructions

TBD

## License

This product is licensed under the [MIT License](https://github.com/harvey298/aurpm/blob/main/LICENSE). This project is available for commercial use, modification, distribution, and private use.

## Contributing

Pull requests are encouraged. For major changes with the project please open an issue about what you would like to change. Thank you for participating in the development of this AUR package manager!
