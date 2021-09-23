# Download/hr
{{TOCright}}


<div class="mw-translate-fuzzy">

### Trenutna stabilna verzija FreeCAD-a 


</div>

The first 0.19.2 release of FreeCAD (24291) was published on 2021-04-22. To find out what\'s new, see the [release notes](Release_notes_0.19.md).

You will find SHA256 checksums to verify the integrity of your download on the [0.19.2 release page](https://github.com/FreeCAD/FreeCAD/releases/tag/0.19.2).

Previous versions can be downloaded from the [releases](https://github.com/FreeCAD/FreeCAD/releases) page

+:----------------------------------------------------------------------------------------------------------------------------------------:+---+:------------------------------------------------------------------------------------------------------------------------------------------------------:+---+:-----------------------------------------------------------------------:+
| ![](images/Windows.png )                                                                                                           |   | ![](images/Mac.png )                                                                                                                                 |   | ![](images/AppImage-logo.png )                              |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| Install on Windows                                                                                                                       |   | Install on Mac                                                                                                                                         |   | Install on Linux                                                        |
|                                                                                                                                          |   |                                                                                                                                                        |   |                                                                         |
| [64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-installer1.exe) (includes installer) |   | [macOS](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD_0.19-24291-macOS-x86_64-conda.dmg) 64-bit |   | [AppImage](AppImage.md) 64-bit |
+------------------------------------------------------------------------------------------------------------------------------------------+---+--------------------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------------+


<div class="mw-translate-fuzzy">

#### Upute za Windows korisnike 

-   32-Bit installer (x86) podržava slijedeće Windows verzije: 7/8/10.
-   64-Bit installer (x64) podržava slijedeće Windows verzije: 7/8/10.


</div>

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

FreeCAD zajednica pruža mnogo dodatnih modula i makronaredbi. Od 0.17 mogu se lako instalirati iz sustava FreeCAD pomoću [Uređivač Dodataka](Addon_Manager/hr.md)<img alt="" src=images/AddonManager.svg  style="width:22px;">.

---
[documentation index](../README.md) > Download/hr
