The Hiligaynon morphology and tools
==========================================

[![GitHub issues](https://img.shields.io/github/issues-raw/giellalt/lang-hil)](https://github.com/giellalt/lang-hil/issues)
[![Build Status](https://divvun-tc.thetc.se/api/github/v1/repository/giellalt/lang-hil/main/badge.svg)](https://github.com/giellalt/lang-hil/actions)
[![License](https://img.shields.io/github/license/giellalt/lang-hil)](https://github.com/giellalt/lang-hil/blob/main/LICENSE)

This repository contains finite state source files for the Hiligaynon language,
for building morphological analysers, proofing tools
and dictionaries. The data and implementation are licenced under __LICENCE__
licence, also detailed in the
[LICENSE](https://github.com/giellalt/lang-hil/blob/main/LICENSE). The
authors named in the AUTHORS file are available to grant other licencing
choices.

Install proofing tools and [keyboards](https://github.com/giellalt/keyboard-hil)
for the Hiligaynon language by using the [Divvun Installer](http://divvun.no)
(some languages are only available via the nightly channel).

Spell-checker accuracy:

[![Speller
Accuracy](https://img.shields.io/badge/Speller_Accuracy-XX_%25-green.svg)](https://giellalt.github.io/lang-hil/speller-report.html)
[![Spell-checking accuracy development
graph](https://giellalt.github.io/lang-hil/speller-report.svg)](https://giellalt.github.io/lang-hil/speller-report.svg)



Documentation
-------------

Documentation can be found at:

- [In source documentation generated with github
   pages](https://gilellalt.github.io/lang-hil/)
-   <https://giellalt.uit.no/lang/hildoc/index.html>
-   <https://giellalt.uit.no/index.html>

Core dependencies
-----------------

In order to compile and use Hiligaynon language morphology and
dictionaries, you need:

- an FST compiler: [HFST](https://github.com/hfst/hfst), [Foma](https://github.com/mhulden/foma) or [Xerox Xfst](https://web.stanford.edu/~laurik/fsmbook/home.html)
- [VislCG3](https://visl.sdu.dk/svn/visl/tools/vislcg3/trunk) Constraint Grammar tools

To install VislCG3 and HFST, just copy/paste this into your Terminal on **Mac OS X**:

```
curl https://apertium.projectjj.com/osx/install-nightly.sh | sudo bash
```

or terminal on **Ubuntu, Debian or Windows Subsystem for Linux**:

```
wget https://apertium.projectjj.com/apt/install-nightly.sh -O - | sudo bash
sudo apt-get install cg3 hfst
```

or terminal on **RedHat, Fedora, CentOS or Windows Subsystem for Linux**:

```
wget https://apertium.projectjj.com/rpm/install-nightly.sh -O - | sudo bash
sudo dnf install cg3 hfst
```

Alternatively, the Apertium wiki has good instructions on how to [install the dependencies for Mac
OS X](https://wiki.apertium.org/wiki/Apertium_on_Mac_OS_X) and how to [install
the dependencies on
linux](https://wiki.apertium.org/wiki/Installation_of_grammar_libraries)

Further details and dependencies are described on the GiellaLT [Getting Started](https://giellalt.uit.no/infra/GettingStarted.html) pages.

Downloading
-----------

Using Git:
```
git clone https://github.com/giellalt/lang-hil
```

Using Subversion:
```
svn checkout https://github.com/giellalt/lang-hil.git/trunk lang-hil
```

Building and installation
-------------------------

[INSTALL](https://github.com/giellalt/lang-hil/blob/main/INSTALL)
describes the GNU build system in detail, but for most users it is the usual:

```sh
./autogen.sh # This will automatically clone or check out other GiellaLT dependencies
./configure
make
(as root) make install
```
