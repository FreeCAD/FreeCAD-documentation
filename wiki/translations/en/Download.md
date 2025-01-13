# Download/en
## Current stable version 

The 1.0 release of FreeCAD was published on 2024-11-18. To find out what\'s new, see the [release notes](Release_notes_1.0.md).

You can find SHA256 checksums to verify the integrity of your download on the [1.0.0 release page](https://github.com/FreeCAD/FreeCAD/releases/tag/1.0.0).

Previous versions can be downloaded from the [releases](https://github.com/FreeCAD/FreeCAD/releases) page.

+::+::+::+
| ![](images/Windows.png )                                                                                                          | ![](images/Mac.png )                                                                                                            | ![](images/Linux_with_text.png )                                                                                  |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [Install instructions](Installing_on_Windows.md)                                                                                | [Install instructions](Installing_on_Mac.md)                                                                              | [Install instructions](Installing_on_Linux.md)                                                                          |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-installer-1.exe)       | [ARM (M-series) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-arm64-py311.dmg) | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage)   |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-py311.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-x86_64-py311.dmg)         | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-aarch64-py311.AppImage) |
++++

### Notes for Windows users 

-   The following Windows versions are supported: 64-bit 8/10/11.
-   The package can also be installed from the [Chocolatey](https://chocolatey.org/packages/freecad) manager. The Chocolatey package is currently not up-to-date.

### Notes for macOS users 

-   MacOS 10.12 Sierra is the minimum supported version.

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

-   For development builds and development source code, see the [weekly builds](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) page. Weekly builds are available for Linux, MacOS, and Windows there. For Linux, daily builds are also available: use the [snap package](Ubuntu_Snap.md)\'s edge channel or the [FreeCAD daily PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) (the latter only for Debian-based distributions).
-   To compile the latest source code, see [compiling](Compiling.md).

## Additional modules and macros 

The FreeCAD community provides many additional modules and macros. They can be easily installed from within FreeCAD using the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr.md).



---
⏵ [documentation index](../README.md) > Download/en
