# Splash screen/pt-br
## Description


<div class="mw-translate-fuzzy">

A **tela de abertura** (splash screen) é uma imagem que aparece durante a inicialização do FreeCAD. Você pode desabilitar a tela de abertura no menu *Editar / Preferências* do FreeCAD removendo a opção \"Mostrar a tela de splash ao iniciar\".


</div>


<small>(v1.0)</small> 

: The splash screen image is picked randomly from multiple images including user models and selected add-on workbenches.

## Custom splash screen 

To use a custom splash screen, you have to place an image named **splash_image.png** in one of the following directories depending on the operating system:

-   **Linux:** **$XDG_DATA_HOME/FreeCAD/Gui/images/** (normally this corresponds to **~/.local/share/FreeCAD/Gui/images/**)
-   **Windows:** **%APPDATA%\FreeCAD\Gui\images\** (normally **C:\Users\username\AppData\Roaming\FreeCAD\Gui\images\**)
-   **MacOS:** **~/Library/Application Support/FreeCAD/Gui/images/**

The directory can be found using the {{Incode|App.getUserAppDataDir()}} command in the [Python console](Python_console.md). The {{Incode|Gui}} and {{Incode|images}} folders may have to be created first. The same custom splash screen will be used for all versions of FreeCAD on a given computer.



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > Splash screen/pt-br
