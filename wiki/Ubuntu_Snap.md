# Ubuntu Snap
 

## Introduction

An [Ubuntu Snap](Ubuntu_Snap.md) package, or just [Snap](Ubuntu_Snap.md) is a distribution format similar to [AppImage](AppImage.md) in that it is intended to be a \"universal installable package\" to deploy software in Linux systems. Snaps were introduced by Ubuntu but they are intended to run in all Linux distributions as long as the Snap daemon, or `snapd`, is available in the target system.

A Snap package has two main characteristics:

-   Programs are sandboxed so they do not interfere with the rest of your operating system.
-   Programs are updated automatically in the background in order to get the newest version of the application.

For other ways of installing the software, see [Installing on Linux](Installing_on_Linux.md).

## Installation

As of v0.19 the use of Snaps is experimental. The current Snaps are generated and hosted by volunteers.

In all systems where Snaps are to be installed, the Snap daemon must be installed first. The package is normally called `snapd`.

For Debian/Ubuntu and similar systems which use the APT manager the daemon is installed as follows:  {{Code|lang=bash|code=
sudo apt install snapd
}}

To install the stable version of the Snap use:  {{Code|lang=bash|code=
sudo snap install freecad
}}

To install the development version of the Snap use:  {{Code|lang=bash|code=
sudo snap install --edge freecad-ppd
}}

## Links

More information about current efforts to deal with Snaps.

-   [0.19 Snap Preview needs \"testers\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=46044), older Snap by **vejmarie**
-   [Discussion: State of the snap (Snap Packaging)](https://forum.freecadweb.org/viewtopic.php?f=42&t=46853), newer version of the Snap by **ppd**

 
