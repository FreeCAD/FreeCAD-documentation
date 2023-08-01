# Splash screen
## Description

The **splash screen** is an image that appears during the startup of FreeCAD. For each new release, it\'s selected in an open voting from user contributions. You can disable the splash screen in the [Preferences Menu](Preferences_Editor.md) by unchecking the option \"Enable splash screen at startup\".

## Custom splash screen 

To use a custom splash screen, you have to place an image named `splash_image.png` in one of the following directories depending on the operating system:

-   **Linux:** `$XDG_DATA_HOME/FreeCAD/Gui/images/` (normally this corresponds to `~/.local/share/FreeCAD/Gui/images/`)
-   **Windows:** `%APPDATA%\FreeCAD\Gui\images\` (typically `C:\Users\username\AppData\Roaming\FreeCAD\Gui\images\`)
-   **MacOS:** `~/Library/Application Support/FreeCAD/Gui/images/`

The directory can be found using the `App.getUserAppDataDir()` command in the [Python console](Python_console.md). The `Gui` and `images` folders may have to be created first. The same custom splash screen will be used for all versions of FreeCAD on a given computer.



---
⏵ [documentation index](../README.md) > Splash screen
