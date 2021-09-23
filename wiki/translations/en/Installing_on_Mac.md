# Installing on Mac/en
FreeCAD can be installed on macOS from a .dmg package which you can drag and drop into your Applications folder:


{{DownloadMacStable}}

and the weekly build can be downloaded from

<img alt="" src=images/Nightly.png  style="width:30px;">[Weekly](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

You can also use a package manager such as HomeBrew to keep your software updated. Instructions to install HomeBrew can be seen [here](https://brew.sh/). When HomeBrew installed you can simply install FreeCAD 0.18.4 through your bash terminal with


```python
brew install --cask freecad
```

and to use the latest version available (0.19pre) on HomeBrew you may run


```python
brew install freecad
```

If there are any issues with the HomeBrew Cask or Formula you may report them to [here](https://github.com/FreeCAD/homebrew-freecad).

This page describes the usage and features of the FreeCAD installer. It also includes uninstallation instructions. Once installed, you can [get started](Getting_started.md)!

## Simple installation 

The FreeCAD installer is provided as a app package (.app) enclosed in a disk image file.

You can download the latest installer from the [Download](Download.md) page. After downloading the file, just mount the disk image, then drag it to the Application folder or a folder of your choice.

![](images/mac_installer_1.png )

That\'s it.Just click on the app to launch FreeCAD. If you have this message \"FreeCAD can\'t be open as it is from unidentified developer. \" Open the folder (Application) and right click on the app then click open and accept to open the application.

## Uninstallation

There currently isn\'t an uninstaller for FreeCAD installed with dmg package. To completely remove FreeCAD and all installed components, drag the following files and folders to the Trash:

-   In /Applications:
    -   FreeCAD

If you installed FreeCAD with homebrew simply use the `brew uninstall freecad` command. That\'s it.

---
[documentation index](../README.md) > Installing on Mac/en
