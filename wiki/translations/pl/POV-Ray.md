# POV-Ray/pl
**The development of POV-Ray seems to be halted. The latest stable version is 3.7.0.8 (2018-05-27), the latest development version is 3.8.0-x (2019-02-19), the [https   *//github.com/POV-Ray/povray/ official project on GitHub] has been edited the last time on 2019-03-08. Please remove this warning if the situation changes**

# Description

POV-Ray (The Persistence of Vision Raytracer) is one of the two renderers supported by the [Raytracing workbench](Raytracing_Workbench.md) together with [LuxRender](LuxRender.md). It is also supported by the new [Render Workbench](https   *//github.com/FreeCAD/FreeCAD-render), together with [LuxCoreRender](LuxCoreRender.md), Appleseed, Blender Cycles and Intel Ospray Studio (experimental).

# Installation

## Raytracing Workbench 


**The [Raytracing workbench](Raytracing_Workbench.md) is being superseded by the new [https   *//github.com/FreeCAD/FreeCAD-render Render Workbench], which is intended as its replacement. The Render Workbench can be installed through the [Addon Manager](Std_AddonMgr.md). The information here is provided because by default FreeCAD is still shipped (as of 0.19-24276) with the Raytracing Workbench**

### Stable Version 

The latest stable version of POV-Ray to be provided with binaries is 3.7.0.0 (2013-11-06), the first to be free software, released under the AGPL3 (or later). The latest stable version of POV-Ray, released only as source code is 3.7.0.8 (2018-05-27).

#### Linux

***Compiled binaries***

If your distribution has it in the official repositories, you can install POV-Ray and all the relative dependencies through the package manager. Such distributions include   * [Arch Linux](https   *//archlinux.org/packages/community/x86_64/povray/), [Debian](https   *//packages.debian.org/search?keywords=povray), [Gentoo](https   *//packages.gentoo.org/packages/media-gfx/povray), [openSUSE](https   *//software.opensuse.org/package/povray), [Ubuntu](https   *//packages.ubuntu.com/search?keywords=povray).

***Compiling from source***

If your distributions does not have POV-Ray in the repositories, or you wish to, it is possible to compile POV-Ray from source. [Download the source code of POV-Ray 3.7.0.8 from GitHub](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.7.0.8.tar.gz).

***Configuring FreeCAD***

After installing POV-Ray, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Raytracing Workbench](Preferences_Editor#Available_Workbenches.md), and go to the [Raytracing Preferences](Raytracing_Preferences.md).

Set the POV-Ray executable path to point to your installation of POV-Ray, usually it is */usr/bin/povray*, and apply.

#### macOS

There is no official binary of POV-Ray 3.7 or newer for macOS, if you want to compile it from source, probably you are on your own.

The [most recent available binaries](http   *//www.povray.org/redirect/www.povray.org/ftp/pub/povray/Old-Versions/Official-3.62/Macintosh/povpmac.zip) are of the old closed source POV-Ray 3.6x.

#### Windows

The latest stable version of POV-Ray to have compiled Windows binaries is POV-Ray 3.7.0.0. [Download it from GitHub](https   *//github.com/POV-Ray/povray/releases/download/v3.7.0.0/povwin-3.7-agpl3-setup.exe), launch the installer and follow the proposed steps.

By default the destination folder is *C   *Program Files\\POV-Ray\\v3.7*, with documents and scenes in *C   *Users\\{your user}\\Documents\\POV-Ray\\v3.7*.

After installing POV-Ray, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Raytracing Workbench](Preferences_Editor#Unloaded_Workbenches.md), and go to the [Raytracing Preferences](Raytracing_Preferences.md).

Set the POV-Ray executable path to point to your installation of POV-Ray, usually it is *C   */Program Files/POV-Ray/v3.7/bin/pvengine64.exe*, and apply.

Then, before trying to render something, start POV-Ray separately and [set I/O restrictions according to POV-Ray documentation](https   *//wiki.povray.org/content/Documentation   *Windows_Section_2.1), otherwise rendering will not work properly (or will not work at all).

### Development Version 

Development seems to be halted, nonethless the latest experimental builds and source code are available. As it is experimental, you are adviced against using it in production environments.

#### Linux 

There are no official POV-Ray development binaries, you should compile it from source. The latest release of the official development branch is [POV-Ray v3.8.0-alpha.10064268](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-alpha.10064268.tar.gz).

The latest development releases (not part of the official development branch) are [POV-Ray v3.8.0-x.freetype.3](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.freetype.3.tar.gz) and [POV-Ray v3.8.0-x.10064738](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.10064738.tar.gz).

#### macOS 

There hasn\'t been a macOS build of POV-Ray since the closed source 3.6x version. You can try to compile it from source, but be advised that it might not even be possible.

The latest release of the official development branch is [POV-Ray v3.8.0-alpha.10064268](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-alpha.10064268.zip).

The latest development releases (not part of the official development branch) are [POV-Ray v3.8.0-x.freetype.3](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.freetype.3.zip) and [POV-Ray v3.8.0-x.10064738](https   *//github.com/POV-Ray/povray/archive/refs/tags/v3.8.0-x.10064738.zip).

#### Windows 

First of all you need to install POV-Ray 3.7, see [the install instructions for the stable version](POV-Ray#Windows.md). Then open POV-Ray install directory, by default *C   *Program Files\\POV-Ray\\v3.7*, and in the *bin* subdirectory rename the POV-Ray executable, so that you do not replace it. For example rename it to BAK-pvengine64.exe.

Then download the development build of POV-Ray you want to use. The latest release of the official development branch is [POV-Ray v3.8.0-alpha.10064268-av69](https   *//github.com/POV-Ray/povray/releases/download/v3.8.0-alpha.10064268/povray-3.8.0-alpha.10064268-av691-Win64.7z).

The latest development releases (not part of the official development branch) are [POV-Ray v3.8.0-x.freetype.3-av693](https   *//github.com/POV-Ray/povray/releases/download/v3.8.0-x.freetype.3/povray-3.8.0-x.freetype.3-av693-Win64.7z) and [POV-Ray v3.8.0-x.10064738-av694](https   *//github.com/POV-Ray/povray/releases/download/v3.8.0-x.10064738/povray-3.8.0-x.10064738-av694-Win64.7z).

Extract the downloaded archive (if you don\'t have a suitable software use [7-Zip](https   *//www.7-zip.org/)) and copy the POV-Ray executable in the *bin* folder of your POV-Ray 3.7 installation.

## Render Workbench 

As of now there are no significant differences between the Raytracing Workbench and the Render Workbench in the part regarding the installation of the external software, so refer to the [Raytracing Workbench section](POV-Ray#Raytracing_Workbench.md) to install POV-Ray and to this section for the Render Workbench configuration..

First of all install the Render Workbench through the [Addon Manager](Std_AddonMgr.md) and restart FreeCAD.

#### Linux 

After installing the Render Workbench and POV-Ray, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Render Workbench](Preferences_Editor#Available_Workbenches.md), and go to the Render Preferences.

Set the POV-Ray executable path to point to your installation of POV-Ray, usually it is */usr/bin/povray*, and apply.

#### Windows 

After installing the Render Workbench and POV-Ray, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Render Workbench](Preferences_Editor#Available_Workbenches.md), and go to the Render Preferences.

Set the POV-Ray executable path to point to your installation of POV-Ray, usually it is *C   */Program Files/POV-Ray/v3.7/bin/pvengine64.exe*, and apply.

Then, before trying to render something, start POV-Ray separately and [set I/O restrictions according to POV-Ray documentation](https   *//wiki.povray.org/content/Documentation   *Windows_Section_2.1), otherwise rendering will not work properly (or will not work at all).



---
![](images/Right_arrow.png) [documentation index](../README.md) > POV-Ray/pl
