# Download/cs
{{TOCright}}

## Current stable version 

The 0.20.2 release of FreeCAD (29603) was published on 2022-12-07. To find out what\'s new, see the [release notes](Release_notes_0.20.md).

You can find SHA256 checksums to verify the integrity of your download on the [0.20.2 release page](https://github.com/FreeCAD/FreeCAD/releases/tag/0.20.2).

Previous versions can be downloaded from the [releases](https://github.com/FreeCAD/FreeCAD/releases) page.

+::+::+::+
| ![](images/Windows.png )                                                                                         | ![](images/Mac.png )                                                                                                             | ![](images/Linux_with_text.png )     |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                 | [Install on Mac](Installing_on_Mac.md)                                                                                     | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD-0.20.2-WIN-x64-installer-3.exe) | [macOS 64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD_0.20.2-2022-12-27-conda-macOS-x86_64-py310.dmg) | [AppImage 64-bit](AppImage.md)             |
++++

### Notes for Windows users 

-   The following Windows versions are supported: 64-bit 7/8/10/11. 32-bit Windows is not supported.
-   A portable version that doesn\'t need installation is available on the [releases](https://github.com/FreeCAD/FreeCAD/releases/) page.
-   The package can also be installed from the [Chocolatey](https://chocolatey.org/packages/freecad) manager.

### Notes for macOS users 

macOS 10.12 Sierra is the minimum supported version.

### Notes for GNU/Linux users 

Most distributions carry FreeCAD in their official repositories, however, if the distribution doesn\'t follow a rolling release model the version they provide might be outdated. Instead you can download the AppImage above, mark it as executable and launch it without installation.

Please see the [Installing on Linux](Installing_on_Linux.md) page for more installation options, including daily packages for Ubuntu and derivatives.

A portable version that doesn\'t need installation can be achieved by starting FreeCAD with these commands:


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

More information about FreeCAD\'s environment variables can be found on [the configuration page](Start_up_and_Configuration#Environment_variables.md).

## Development versions 

FreeCAD\'s development is active.

-   For development builds and development source code, see the [weekly builds](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) page.
-   To compile the latest source code, see [compiling](Compiling.md).

## Additional modules and macros 


<div class="mw-translate-fuzzy">

The FreeCAD community provides a wealth of additional modules and macros. They can now easily be installed directly from within FreeCAD using the [Addon Manager](Std_AddonMgr.md).


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Download/cs
