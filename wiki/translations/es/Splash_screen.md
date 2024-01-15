# Splash screen/es
## Description


<div class="mw-translate-fuzzy">

La **pantalla de bienvenida** es una imagen que aparece durante el inicio de FreeCAD. Puedes desactivar la pantalla de bienvenida en el menú Preferencias de FreeCAD eliminando la opción \"Activar la pantalla de bienvenida al inicio\".


</div>

## Custom splash screen 

To use a custom splash screen, you have to place an image named **splash_image.png** in one of the following directories depending on the operating system:

-   **Linux:** **$XDG_DATA_HOME/FreeCAD/Gui/images/** (normally this corresponds to **~/.local/share/FreeCAD/Gui/images/**)
-   **Windows:** **%APPDATA%\FreeCAD\Gui\images\** (normally **C:\Users\username\AppData\Roaming\FreeCAD\Gui\images\**)
-   **MacOS:** **~/Library/Application Support/FreeCAD/Gui/images/**

The directory can be found using the {{Incode|App.getUserAppDataDir()}} command in the [Python console](Python_console.md). The {{Incode|Gui}} and {{Incode|images}} folders may have to be created first. The same custom splash screen will be used for all versions of FreeCAD on a given computer.



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > Splash screen/es
