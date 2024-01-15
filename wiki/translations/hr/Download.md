# Download/hr
### Trenutna stabilna verzija 

The 0.21.2 release of FreeCAD was published on 2023-11-14. To find out what\'s new, see the [release notes](Release_notes_0.21.md).

You can find SHA256 checksums to verify the integrity of your download on the [0.21.2 release page](https://github.com/FreeCAD/FreeCAD/releases/tag/0.21.2).

Previous versions can be downloaded from the [releases](https://github.com/FreeCAD/FreeCAD/releases) page.

+::+::+::+
| ![](images/Windows.png )                                                                                                | ![](images/Mac.png )                                                                                                | ![](images/Linux_with_text.png )                                                                        |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [Install instructions](Installing_on_Windows.md)                                                                      | [Install instructions](Installing_on_Mac.md)                                                                  | [Install instructions](Installing_on_Linux.md)                                                                |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-WIN-x64-installer-1.exe)        | [ARM (M1/M2) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-arm64.dmg)  | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-x86_64.AppImage)   |
|                                                                                                                               |                                                                                                                       |                                                                                                                       |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Windows-x86_64.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-macOS-intel-x86_64.dmg) | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/0.21.2/FreeCAD-0.21.2-Linux-aarch64.AppImage) |
++++

### Notes for Windows users 


<div class="mw-translate-fuzzy">

#### Upute za Windows korisnike 

-   Slijedeće Windows verzije su podržane: 7/8/10.
-   Portabl verzija ([64-bit](https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD-0.19.2.7b5e18a-WIN-x64-portable1.7z)) kojoj nije potrebna instalacija je na stranici izdanja.
-   Paketi mogu biti instalirani sa [Chocolatey](https://chocolatey.org/packages/freecad).


</div>

### Notes for macOS users 

-   MacOS 10.12 Sierra is the minimum supported version.
-   For macOS 12 and older the \"Unsigned Intel disk image\" should be used, the signed version does not work on those systems.

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

FreeCAD zajednica pruža mnogo dodatnih modula i makronaredbi. Od 0.17 mogu se lako instalirati iz sustava FreeCAD pomoću [Uređivač Dodataka](Std_AddonMgr/hr.md)<img alt="" src=images/Std_AddonMgr.svg  style="width:24px;">.


</div>



---
⏵ [documentation index](../README.md) > Download/hr
