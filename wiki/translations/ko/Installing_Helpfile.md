# Installing Helpfile/ko
## 도움말 모듈 

**유의사항:** 아래에 설명되고 있는, 프리캐드의 시스템에 있던 오프라인 도움말은 은퇴 된 상태 입니다. 이제는 프리캐드에 관한 도움말을 [Addon manager](Std_AddonMgr.md)를 통해서 설치하고 [Help Addon](https://github.com/yorikvanhavre/FreeCAD-Help) 에 의해 유지 할 수 있습니다. 추가 기능 도움말 도구를 통해 \'내려받기가 필요하지 않는 온라인 도움말\'에 접속 하거나, 내려받기 할 수 있는 도움말 문서의 복사본인 오프라인 도움말을 추가 기능 매니저를 통해서 설치하고, 접속 할 수 있습니다.

## FreeCAD Helpfiles 

The FreeCAD offline documentation is built from the FreeCAD wiki by using scripts. It has grown to a file size over 220 MB. These big files are not part of installers and executables of FreeCAD, but can be installed separately as documented here.

Translations from the community are encouraged, so the offline documentation is now also available in French and Italian. Other languages may be in different stages of completeness.

## Download Helpfiles 

A working offline documentation consist of at least two files: **freecad.qhc** the Qt-helpfile-configuration and **freecad.qch** the compressed Qt-helpfile. They are put together in a ZIP-archive.

The helpfiles can be downloaded here: <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z>

As a future option they can be installed from within FreeCAD with the [Addon Manager](Std_AddonMgr.md).

The help files do always have the same names: **freecad.qhc** and **freecad.qch**. In order to have different version of the helpfiles, these need to be installed in different directories. In case of a manual download, just store the zip-file locally and extract the archive into the wanted directory.

## Register the Documentation 

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
⏵ [documentation index](../README.md) > Installing Helpfile/ko
