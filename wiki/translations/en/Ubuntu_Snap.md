# Ubuntu Snap/en
{{TOCright}}

## Introduction

An [Ubuntu Snap](Ubuntu_Snap.md) package, or just [Snap](Ubuntu_Snap.md) is a distribution format similar to [AppImage](AppImage.md) in that it is intended to be a \"universal installable package\" to deploy software on Linux systems. Snaps were introduced by Ubuntu but they are intended to run on all Linux distributions as long as the Snap daemon, or `snapd`, is available on the target system.

A Snap package has two main characteristics:

-   Programs are sandboxed so they do not interfere with the rest of the operating system.
-   Programs are updated automatically in the background in order to get the newest version of the application.

For other ways of installing the software, see [Installing on Linux](Installing_on_Linux.md).

## Installation

The use of Snaps is experimental. The current Snaps are generated and hosted by volunteers.

On all systems where Snaps are to be installed, the Snap daemon must be installed first. The package is normally called `snapd`.

### Debian/Ubuntu

For Debian/Ubuntu and similar systems which use the APT manager the daemon is installed as follows:


{{Code|lang=bash|code=
sudo apt install snapd
}}

To install the stable version of the Snap use:


{{Code|lang=bash|code=
sudo snap install freecad
}}

To install the development version of the Snap use:


{{Code|lang=bash|code=
sudo snap install --edge freecad
}}

### Manjaro

To install the stable version of the Snap use:


{{Code|lang=bash|code=
snap install freecad
}}

To install the development version of the Snap use:


{{Code|lang=bash|code=
snap install --edge freecad
}}

## Notes

#### What FC version am I running 

To figure out which development version is installed type the following in the Command-line interface:


{{Code|lang=bash|code=
snap info freecad
}}

#### Changing between different Snaps 

Starting from the tail end of the v0.20 release cycle, the FreeCAD snap maintainers added the ability to test experimental FreeCAD builds. Snaps allow for this by easily toggling between different snaps (terminology is \'[channels or tracks](https://snapcraft.io/docs/channels)\'). For example:

Testing the Topological Naming (\'toponaming\') branch (created at the start of the v0.21/v1.0 release cycle):


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge/toponaming
}}

Using the `refresh` command will switch and update the snap channel you\'re switching to:


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge/toponaming
}}

Toggling back to the nightly \'edge\' channel:


{{code|lang=bash|code=
snap refresh freecad --channel=latest/edge
}}

## Advanced

The following commands are geared towards users that are familiar with `git` and have a locally cloned repository of the upstream FreeCAD repository.


{{Code|lang=bash|code=
git clone https://github.com/FreeCAD/FreeCAD
cd FreeCAD/
}}

To find out the latest upstream revision number (also known as \'HEAD\'):


{{Code|lang=bash|code=
git pull upstream master  # first make sure we have the most up-to-date commits
git rev-list --count HEAD # 'HEAD' refers to the current commit you are viewing (tip of the master branch)
}}

To translate the current snap development version in to a revision number (make sure you\'re within your cloned FreeCAD repository as mentioned above):


{{Code|lang=bash|code=
snap info freecad <nowiki>|</nowiki>\
grep -e '^\s\+latest/edge' <nowiki>|</nowiki>\
awk -F ' ' '{ print $2 }' <nowiki>|</nowiki>\
xargs -I{} git rev-list --count {}
}}

**Note:** the above bash script 1 liner assumes user has \'edge\' (nightly) installed

The difference between HEAD and the snap edge revision numbers indicates the amount of revisions trailing behind upstream the snap development (edge) is.

Taking it a step further, if you want a short summary of the commits between the current snap edge and HEAD:


{{Code|lang=bash|code=
snap info freecad <nowiki>|</nowiki>\
grep -e '^\s\+latest/edge' <nowiki>|</nowiki>\
awk -F ' ' '{ print $2 }' <nowiki>|</nowiki>\
xargs -I{} git log --oneline --ancestry-path {}..HEAD
}}

**Note:** The output will indicate what commits **are not** in the current \'edge\' (but will be on the next nightly update).

## Links

More information about the current efforts to deal with Snaps:

-   [0.19 Snap Preview needs \"testers\"](https://forum.freecadweb.org/viewtopic.php?f=4&t=46044), older Snap by **vejmarie**. (deprecated)
-   [Discussion: State of the snap (Snap Packaging)](https://forum.freecadweb.org/viewtopic.php?f=42&t=46853), newer version of the Snap by **ppd**. (deprecated)

### Repositories

-   <https://github.com/FreeCAD/FreeCAD-snap>
-   <https://snapcraft.io/freecad>

### Maintainer(s)

-   ppd ([forum](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=24042), [github](https://github.com/ppd))
-   luzpaz ([forum](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=12229), [github](https://github.com/luzpaz))

## Related

-   [AppImage](AppImage.md) - another self-contained \'binary\' like format to run FreeCAD
-   [Flatpak](Flatpak.md) packages



---
![](images/Button_right.svg) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > [Testing](Category_Testing.md) > Ubuntu Snap/en
