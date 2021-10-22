# Download/en
{{TOCright}}

## Current stable version 

The first 0.19.2 release of FreeCAD (24291) was published on 2021-04-22. To find out what\'s new, see the [release notes](Release_notes_0.19.md).

You will find SHA256 checksums to verify the integrity of your download on the [0.19.2 release page](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).

Previous versions can be downloaded from the [releases](https://github.com/FreeCAD/FreeCAD/releases) page

+:----------------------------------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------------------------------------------------------------------------------------------------------------------:+---+:-----------------------------------------------------------------------:+
| ![](images/Windows.png )                                                                                                           |   | ![](images/Mac.png )                                                                                                                                 |   | ![](images/AppImage-logo.png )                              |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| Install on Windows                                                                                                                       |   | Install on Mac                                                                                                                                         |   | Install on Linux                                                        |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| _ 64-bit |
+------------------------------------------------------------------------------------------------------------------------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------------+

### Notes for Windows users 

-   The following Windows versions are supported: 7/8/10.
-   A portable version ([64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-portable1.7z)) that doesn\'t need installation is on the release page.
-   The package may also be installed from the [Chocolatey](https://chocolatey.org/packages/freecad) manager.

### Notes for Mac OS X users 

Mac OS X 10.12 *Sierra* is the minimum supported version.

### Notes for GNU/Linux users 

Most distributions carry FreeCAD in their official repositories, however, if the distribution doesn\'t follow a rolling release model the version they provide might be outdated. Instead you can download the AppImage above, mark it as executable and launch it without installation.

Please see the [Installing on Linux](Installing_on_Linux.md) page for more installation options, including daily packages for Ubuntu and derivatives.

A portable version that doesn\'t need installation can be achieved by starting FreeCAD with these commands: <small>(v0.19)</small>  
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD_0.19-23756-Linux-Conda_glibc2.12-x86_64.AppImage
```

More information about FreeCAD\'s environment variables can be found on [the configuration page](Start_up_and_Configuration#Environment_variables.md).

## Development versions 

FreeCAD\'s development is active.

-   For Linux users, check out the development [AppImage](AppImage.md).
-   For MacOS and Windows development builds and development source code, see the [weekly builds](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds) page.
-   To compile the latest source code, see [compiling](Compiling.md).

## Additional modules and macros 

The FreeCAD community provides many additional modules and macros. Since 0.17 they can be easily installed from within FreeCAD using the [Addon manager](Addon_Manager.md) <img alt="" src=images/AddonManager.svg  style="width:22px;">.

---
[documentation index](../README.md) > Download/en
