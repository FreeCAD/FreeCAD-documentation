# Download/ko
{{TOCright}}


<div class="mw-translate-fuzzy">

## 현재 안정 버전 


</div>

The 0.20 release of FreeCAD (29177) was published on 2022-06-14. To find out what\'s new, see the [release notes](Release_notes_0.20.md).

You can find SHA256 checksums to verify the integrity of your download on the [0.20 release page](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.20).

Previous versions can be downloaded from the [releases](https   *//github.com/FreeCAD/FreeCAD/releases) page.

+   *   *+---+   *   *+---+   *   *+
| ![](images/Windows.png )                                                                                                  |   | ![](images/Mac.png )                                                                                |   | ![](images/AppImage-logo.png )         |
|                                                                                                                                 |   |                                                                                                       |   |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                          |   | [Install on Mac](Installing_on_Mac.md)                                                        |   | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                                 |   |                                                                                                       |   |                                                    |
| [64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20/FreeCAD-0.20.0-WIN-x64-installer-1.exe) (includes installer) |   | [macOS 64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20/FreeCAD-0.20.0-OSX-i386.dmg) |   | [AppImage 64-bit](AppImage.md)             |
++---++---++

### Notes for Windows users 

-   The following Windows versions are supported   * 64-bit 7/8/10/11. 32-bit Windows is not supported.
-   A portable version that doesn\'t need installation is available on the [releases](https   *//github.com/FreeCAD/FreeCAD/releases/) page.
-   The package can also be installed from the [Chocolatey](https   *//chocolatey.org/packages/freecad) manager.

### Notes for Mac OS X users 

Mac OS X 10.12 Sierra is the minimum supported version.

### Notes for GNU/Linux users 

Most distributions carry FreeCAD in their official repositories, however, if the distribution doesn\'t follow a rolling release model the version they provide might be outdated. Instead you can download the AppImage above, mark it as executable and launch it without installation.

Please see the [Installing on Linux](Installing_on_Linux.md) page for more installation options, including daily packages for Ubuntu and derivatives.

A portable version that doesn\'t need installation can be achieved by starting FreeCAD with these commands   * <small>(v0.19)</small>  
```python
cd path/to/directory_containing_AppImage/
chmod +x ./FreeCAD-0.20.0-Linux-x86_64.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./FreeCAD-0.20.0-Linux-x86_64.AppImage
```

More information about FreeCAD\'s environment variables can be found on [the configuration page](Start_up_and_Configuration#Environment_variables.md).

## Development versions 

FreeCAD\'s development is active.

-   For Linux users, check out the development [AppImage](AppImage.md).
-   For MacOS and Windows development builds and development source code, see the [weekly builds](https   *//github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds) page.
-   To compile the latest source code, see [compiling](Compiling.md).

## Additional modules and macros 

The FreeCAD community provides many additional modules and macros. Since 0.17 they can be easily installed from within FreeCAD using the [Addon manager](Std_AddonMgr.md) <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;">.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Download/ko
