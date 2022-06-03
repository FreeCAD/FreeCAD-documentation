# LuxCoreRender/en
**LuxCoreRender is not officially supported by the [Raytracing Workbench](Raytracing_Workbench.md), it is instead supported by the by the new [https   *//github.com/FreeCAD/FreeCAD-render Render Workbench], which is intended as its replacement. The Render Workbench can be installed through the [Addon Manager](Std_AddonMgr.md).**

# Description

[LuxCoreRender](https   *//luxcorerender.org) is a physically based rendering engine, reboot of the now outdated [LuxRender](LuxRender.md). It is not officially supported by the [Raytracing Workbench](Raytracing_Workbench.md), although it might work.

# Installation

## Raytracing Workbench 


**Officially the [Raytracing workbench](Raytracing_Workbench.md) does not work with LuxCoreRender, only with the outdated [LuxRender](LuxRender.md). Also the [Raytracing workbench](Raytracing_Workbench.md) is being superseded by the new [https   *//github.com/FreeCAD/FreeCAD-render Render Workbench], which is intended as its replacement. The Render Workbench can be installed through the [Addon Manager](Std_AddonMgr.md). The information here is provided because by default FreeCAD is still shipped (as of 0.19-24276) with the Raytracing Workbench**

### Stable Version 

LuxCoreRender is under active development, so to know which is the [latest stable version check on GitHub](https   *//github.com/LuxCoreRender/LuxCore/releases/latest).

#### Linux

***Compiled binaries***

If your distribution has it in the official repositories, you can install LuxCoreRender and all the relative dependencies through the package manager. Such distributions include   * [Arch Linux (AUR)](https   *//aur.archlinux.org/packages/?O=0&SeB=nd&K=luxcorerender), [Fedora](https   *//src.fedoraproject.org/rpms/luxcorerender).

Otherwise it is possible to download the official binaries of the [latest stable release from GitHub](https   *//github.com/LuxCoreRender/LuxCore/releases/latest). The file will be something like *luxcorerender-{version number}-linux64.tar.bz2*. The faster solution (although not the best practice) is to extract the content of the archive in a suitable location, like *\~/LuxCoreRender*. If needed change the file permissions so that your user can execute the files you just extracted.

***Compiling from source***

If your distributions does not have LuxCoreRender in the repositories and the official binaries do not work on your computer, or you wish to, it is possible to compile LuxCoreRender from source. [The latest stable release](https   *//github.com/LuxCoreRender/LuxCore/releases/latest) includes the source, that will be something like \'luxcorerender-{version number}.tar.bz2\'\'

***Configuring FreeCAD***

After installing LuxCoreRender, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Raytracing Workbench](Preferences_Editor#Unloaded_Workbenches.md), and go to the [Raytracing Preferences](Raytracing_Preferences.md).

Set the Luxrender executable path to point to your installation of LuxCoreRender, usually it is */usr/bin/luxcoreui* (or if you installed it manually something like *\~/LuxCoreRender/luxcoreui*), and apply.

#### macOS

[Check on GitHub for the latest stable release](https   *//github.com/LuxCoreRender/LuxCore/releases/latest), scroll down to the *Assets* section (expand it if needed) and download the macOS file. It will be something like *luxcorerender-{version number}-mac64.dmg*.

#### Windows

[Check on GitHub for the latest stable release](https   *//github.com/LuxCoreRender/LuxCore/releases/latest), scroll down to the *Assets* section (expand it if needed) and download the Windows file. It will be something like *luxcorerender-{version number}-win64.zip*.

Then check in the note above the assets if there are any notes about dependencies for Windows user. For example to [use LuxRender 2.5](https   *//github.com/LuxCoreRender/LuxCore/releases/tag/luxcorerender_v2.5) you are required to install the [Microsoft Visual C++ Redistributable for Visual Studio 2017](https   *//aka.ms/vs/15/release/vc_redist.x64.exe) and the [Intel C++ redistributable](https   *//software.intel.com/sites/default/files/managed/59/aa/ww_icl_redist_msi_2018.3.210.zip).

After installing dependencies, extract the downloaded archive in a suitable folder, like *C   *Tools\\LuxCoreRender*. Avoid using system folders like *C   *Program Files* or *C   *Program Files (x86)*.

After installing LuxCoreRender, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Raytracing Workbench](Preferences_Editor#Unloaded_Workbenches.md), and go to the [Raytracing Preferences](Raytracing_Preferences.md).

Set the Luxrender executable path to point to your installation of LuxCoreRender, that will be something like *C   */Tools/LuxCoreRender/luxcoreui.exe*, and apply.

### Development Version 

LuxCoreRender is under active development, so to know which is the [latest development version](https   *//github.com/LuxCoreRender/LuxCore/releases) you have to manually check on GitHub for the latest marked as Pre-release.

#### Linux 

***Compiled binaries***

If your distribution has it in the official repositories, you can install LuxCoreRender development version and all the relative dependencies through the package manager. Such distributions include   * [Arch Linux (AUR)](https   *//aur.archlinux.org/packages/?O=0&SeB=nd&K=luxcorerender).

Otherwise it is possible to download the official binaries of the [latest development version, marked as Pre-release, from GitHub](https   *//github.com/LuxCoreRender/LuxCore/releases). The file will be something like *luxcorerender-{version number}-linux64.tar.bz2* or *luxcorerender-latest-linux64.tar.bz2*. The faster solution (although not the best practice) is to extract the content of the archive in a suitable location, like *\~/LuxCoreRender*. If needed change the file permissions so that your user can execute the files you just extracted.

***Compiling from source***

If your distributions does not have LuxCoreRender development in the repositories and the official binaries do not work on your computer, or you wish to, it is possible to compile LuxCoreRender from source. [Check GitHub for the latest development version, marked as Pre-release](https   *//github.com/LuxCoreRender/LuxCore/releases) that includes the source, that will be something like \'luxcorerender-{version number}.tar.bz2\'\'

***Configuring FreeCAD***

After installing LuxCoreRender, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Raytracing Workbench](Preferences_Editor#Unloaded_Workbenches.md), and go to the [Raytracing Preferences](Raytracing_Preferences.md).

Set the Luxrender executable path to point to your installation of LuxCoreRender, usually it is */usr/bin/luxcoreui* (or if you installed it manually something like *\~/LuxCoreRender/luxcoreui*), and apply.

#### macOS 

[Check on GitHub for the latest development version](https   *//github.com/LuxCoreRender/LuxCore/releases), marked as Pre-release, scroll down to the *Assets* section (expand it if needed) and download the Windows file. It will be something like *luxcorerender-{version number}-mac64.dmg* or *luxcorerender-latest-mac64.dmg*.

#### Windows 

[Check on GitHub for the latest development version](https   *//github.com/LuxCoreRender/LuxCore/releases), marked as Pre-release, scroll down to the *Assets* section (expand it if needed) and download the Windows file. It will be something like *luxcorerender-{version number}-win64.zip* or *luxcorerender-latest-win64.zip*.

Then check in the note above the assets if there are any notes about dependencies for Windows user. For example to [use LuxRender 2.5rc1](https   *//github.com/LuxCoreRender/LuxCore/releases/tag/luxcorerender_v2.5rc1) you are required to install the [Microsoft Visual C++ Redistributable for Visual Studio 2017](https   *//aka.ms/vs/15/release/vc_redist.x64.exe) and the [Intel C++ redistributable](https   *//software.intel.com/sites/default/files/managed/59/aa/ww_icl_redist_msi_2018.3.210.zip).

After installing dependencies, extract the downloaded archive in a suitable folder, like *C   *Tools\\LuxCoreRender*. Avoid using system folders like *C   *Program Files* or *C   *Program Files (x86)*.

After installing LuxCoreRender, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Raytracing Workbench](Preferences_Editor#Unloaded_Workbenches.md), and go to the [Raytracing Preferences](Raytracing_Preferences.md).

Set the Luxrender executable path to point to your installation of LuxCoreRender, that will be something like *C   */Tools/LuxCoreRender/luxcoreui.exe*, and apply.

## Render Workbench 

As of now there are no significant differences between the Raytracing Workbench and the Render Workbench in the part regarding the installation of the external software, so refer to the [Raytracing Workbench section](LuxCoreRender#Raytracing_Workbench.md) to install LuxCoreRender and to this section for the Render Workbench configuration.

First of all install the Render Workbench through the [Addon Manager](Std_AddonMgr.md) and restart FreeCAD.

#### Linux 

After installing the Render Workbench and LuxCoreRender, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Render Workbench](Preferences_Editor#Unloaded_Workbenches.md), and go to the Render Preferences.

Set the LuxCore UI path to point to your installation of LuxCoreRender, usually it is */usr/bin/luxcoreui* (or if you installed it manually something like *\~/LuxCoreRender/luxcoreui*), and apply.

#### Windows 

After installing the Render Workbench and LuxCoreRender, launch FreeCAD, open the [Preferences Editor](Preferences_Editor.md), [load the Render Workbench](Preferences_Editor#Unloaded_Workbenches.md), and go to the Render Preferences.

Set the LuxCore command (cli) path, something like *C   */Tools/LuxCore/pyluxcoretool.exe* and LuxCore UI path, something like *C   */Tools/LuxCore/luxcoreui.exe*, then apply.



---
![](images/Right_arrow.png) [documentation index](../README.md) > LuxCoreRender/en
