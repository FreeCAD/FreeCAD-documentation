# Installing Helpfile/ru
{{TOCright}}

## Help module 

**Note:** The FreeCAD offline help files, described below, are being retired. The help system of FreeCAD is now managed by the [Help Addon](https://github.com/yorikvanhavre/FreeCAD-Help), which you can install via the [Addon manager](Std_AddonMgr.md). The Help Addon is able to access online documentation, without the need to download anything, or an offline, downloadable copy of the documentation, which can also be installed via the Addon manager.

## Файлы помощи FreeCAD 

The FreeCAD offline documentation is built from the FreeCAD wiki by using scripts. It has grown to a file size over 220 MB. These big files are not part of installers and executables of FreeCAD, but can be installed separately as documented here.

Translations from the community are encouraged, so the offline documentation is now also available in French and Italian. Other languages may be in different stages of completeness.

## Загрузка файлов помощи 

A working offline documentation consist of at least two files: **freecad.qhc** the Qt-helpfile-configuration and **freecad.qch** the compressed Qt-helpfile. They are put together in a ZIP-archive.

The helpfiles can be downloaded here: <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z>

As a future option they can be installed from within FreeCAD with the [Addon Manager](Std_AddonMgr.md).

The help files do always have the same names: **freecad.qhc** and **freecad.qch**. In order to have different version of the helpfiles, these need to be installed in different directories. In case of a manual download, just store the zip-file locally and extract the archive into the wanted directory.

## Регистрация документации 

The documentation system of FreeCAD uses Qt Assistant. You should install this program first, if you don\'t have it.

The actual organization of the offline help allow only one helpfile to be active. It is therefore not possible to have helpfiles in different languages accessible from FreeCAD at the same time.

In order to make another FreeCAD documentation active the following steps have to be applied:

-   Click inside FreeCAD in the menu **Help  → Help**. The program Qt-assistant should open.
-   In Qt-assistant click in the menu **Edit → preferences**.
-   In the preferences dialog click on the **Documentation** tab.
-   In the list registered documentation select `org.freecad.usermanual` and click on the button **Remove**.
-   Close the dialog with **OK**, but do not close the Qt-assistant. This is important as otherwise another helpfile will not be registered.
-   Open again the preferences dialog via the menu **Edit → preferences**.
-   Select the tab documentation and click the button **Add...**
-   In the dialog navigate to your new helpfile and select **freecad.qch**
-   close the dialog by confirming your selection. In the **Documentation** tab in the preferences there should now be a line with `org.freecad.usermanual`.
-   Close the **Preferences** with **OK**.
-   You should now have the new documentation available in the Qt-assistant, which is accessible from within FreeCAD.

## A Note About Ubuntu 

Difficulties may arise when trying to install the documentation packages on Ubuntu (for example, `freecad-doc` or `freecad-daily-doc`). If this is found to be the case, then executing the following steps will enable you to have offline documentation.

-   Download the **freecad.qhc** and **freecad.qch** help files from <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z> and extract them using 7zip.
-   Alternatively, you can instead get the development versions of the **freecad.qhc** and **freecad.qch** help files from [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Doc). You will need to [concatenate](http://man7.org/linux/man-pages/man1/cat.1.html) the .part files together: `cat freecad.qch.part00 freecad.qch.part01 freecad.qch.part02 freecad.qch.part03 > freecad.qch`.
-   With administrative privileges (e.g., `sudo`), copy or move **freecad.qhc** and **freecad.qch** to **/usr/share/doc/freecad-doc/**. If you are using `freecad-daily`, this will instead be **/usr/share/doc/freecad-daily-doc/**.



---
![](images/Button_right.svg) [documentation index](../README.md) > Installing Helpfile/ru
