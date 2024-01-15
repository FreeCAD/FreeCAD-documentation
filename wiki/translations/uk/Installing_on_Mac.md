# Installing on Mac/uk
FreeCAD can be installed on macOS from a .dmg package which you can drag and drop into your Applications folder, see the [Download](Download.md) page.

If you would like to download a development version, which may be unstable, see the [Weekly builds download](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds) page.

You can also use a package manager such as HomeBrew to keep your software updated. Instructions to install HomeBrew can be seen [here](https://brew.sh/). When HomeBrew installed you can simply install FreeCAD through your bash terminal with


```python
brew install --cask freecad
```

and to use the latest version available on HomeBrew you may run


```python
brew install freecad
```

If there are any issues with the HomeBrew Cask or Formula you may report them to [here](https://github.com/FreeCAD/homebrew-freecad).

This page describes the usage and features of the FreeCAD installer. It also includes uninstallation instructions. Head to [Getting started](Getting_started.md) once installation is complete.

## Simple installation 

The FreeCAD installer is provided as a app package (.app) enclosed in a disk image file.

You can download the latest installer from the [Download](Download.md) page. After downloading the file, just mount the disk image, then drag it to the Application folder or a folder of your choice.

![](images/mac_installer_1.png )

That\'s it.Just click on the app to launch FreeCAD. If you have this message \"FreeCAD can\'t be open as it is from unidentified developer.\" Open the folder (Application) and right click on the app then click open and accept to open the application.

## Uninstallation

There currently isn\'t an uninstaller for FreeCAD installed with dmg package. To completely remove FreeCAD and all installed components, drag the following files and folders to the Trash:

-   In the Applications directory:
    -   /Applications/FreeCAD.app
-   In the Users Home Library directory
    -   \$HOME/Library/Application Support/FreeCAD
    -   \$HOME/Library/Preferences/FreeCAD
    -   \$HOME/Library/Preferences/com.freecad.FreeCAD.plist
    -   \$HOME/Library/Caches/FreeCAD

If you installed FreeCAD with homebrew, then use the `brew uninstall freecad` command to uninstall /Applications/FreeCAD.app. The related files and directories in the user home Library will still need to be removed manually.



---
⏵ [documentation index](../README.md) > Installing on Mac/uk
