# Release notes 1.0
**FreeCAD 1.0 is under development, there is no expected released date yet.**


{{Message|
Are features missing? Mention them in the [https   *//forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Release notes for v1.0] forum thread.


See [Help FreeCAD](Help_FreeCAD.md) for ways to contribute to FreeCAD.
}}


{{Message|All images on this page must use the **_relnotes_1.0** suffix}}

 

**FreeCAD 1.0** was released on **DD MM 2023**, get it from the [Download](Download.md) page. This page lists all new features and changes.

Older FreeCAD release notes can be found in the [Feature list](Feature_list#Release_notes.md).

Placeholder for an eye-catching image selected by the admins from the [user showcases forum](https   *//forum.freecadweb.org/viewforum.php?f=24).

## General

## User interface 

### Further user interface improvements 

## Core system and API 

### Core

### API

#### New Python API 

#### Changed Python API 

## Addon Manager 

## Arch Workbench 

## Draft Workbench 

### Further Draft improvements 

## FEM Workbench 

### Further FEM improvements 

## Export

## Mesh

### Further Mesh improvements 

## OpenSCAD Workbench 

## Part Workbench 

### Further Part improvements 

## PartDesign Workbench 

### Further PartDesign improvements 

## Path Workbench 

-   Camotics integration. If camotics (version 1.2.2 or later) is installed, a new icon will be added to the Path toolbar. Select a Path Job and press the button to open the Camotics dialog. Then drag the slider to generate a simulated solid at any point in the job. You can also launch the full camotics application to run the animated simulaton. This results in a silent post-processing of the job and creation of a camotics project file. [Pull request \#6637](https   *//github.com/FreeCAD/FreeCAD/pull/6637)

-   Additional substitution strings for automatic output naming. If output is being split into multiple files, the filenames can automatically substitute the toolcontroller label, WCS, or operation label. This is in addition to the other existing substitution strings like date, job name, etc.

## Plot module 

## Sketcher Workbench 

### Further Sketcher improvements 

## Spreadsheet Workbench 

### Further Spreadsheet improvements 

## TechDraw Workbench 

### Further TechDraw improvements 

## Web

## External workbenches 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Compilation

Since this release FreeCAD can only be compiled using Qt 5.x and Python 3.x. The lowest supported Python version is 3.8 according to the [FreeCAD 1.0 development goals](FreeCAD_1.0_Development_Cycle.md).

To compile FreeCAD see the instructions for [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) and [MacOS](Compile_on_MacOS.md).

The supported operating systems are   *

-   Windows 7, 8, 10 and 11
-   Linux Ubuntu Focal Fossa (20.04) and newer
-   MacOS   * 10.12 Sierra or newer

## Known Limitations 

### 32bit Windows 

Since FreeCAD 0.19 we no longer officially support 32bit Windows. FreeCAD might work on these systems, but no support is given.

### Remote Desktop under Windows 

Depending on the OpenGL graphics capabilities of a computer, it might be that one encounters a crash when running FreeCAD via remote desktop. To fix this upgrade your OpenGL driver. Only if this doesn\'t help   *

-   Download [this](https   *//downloads.fdossena.com/geth.php?r=mesa64-latest) OpenGL library for 64bit Windows and extract it.
-   Rename the DLL file to *opengl32sw.dll* and copy it to the *bin* subfolder of FreeCAD\'s installation folder (overwrite the existing DLL there).



[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0
