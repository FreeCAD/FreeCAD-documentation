# Interface Customization/es
{{TOCright}}

## Introducción

La interfaz de FreeCAD está basada en el moderno kit de herramientas [Qt](http://en.wikipedia.org/wiki/Qt_(toolkit)) y tiene una organización a nivel de la técnica . Algunos aspectos de la interfaz pueden ser personalizados. Puedes, por ejemplo, añadir barras de herramientas personalizadas, con herramientas de varios ambientes de trabajo o herramientas definidas en macros, y puedes crear tus propios atajos de teclado. Pero los menús y las barras de herramientas por defecto que vienen con FreeCAD y sus ambientes de trabajo no se pueden cambiar.

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*El cuadro diálogo Personalizar*

## Utilización

1.  Los comandos disponibles en el cuadro de diálogo Personalizar dependen de los ambientes de trabajo que se hayan cargado en la sesión actual de FreeCAD. Así que deberías cargar primero todos las ambientes de trabajo a cuyos comandos quieras tener acceso.
2.  Hay varias formas de invocar el <img alt="" src=images/Std_DlgCustomize.svg  style="width:16px;"> [Std DiálogoPersonalizar](Std_DlgCustomize/es.md) comando:
    -   Seleccione la opción **Herramientas → <img src="images/Std_DlgCustomize.svg" width=16px> Personalizar...** en el menú.
    -   Haga clic con el botón derecho en un área de la barra de herramientas y elija **<img src="images/Std_DlgCustomize.svg" width=16px> Personalizar...** en el menú contextual.
3.  Se abre el cuadro de diálogo Personalizar. Para más información, consulte [Opciones](#Opciones.md).
4.  El botón **Ayuda** no funciona en este momento.
5.  Pulse el botón **Cerrar** para cerrar el cuadro de diálogo.

## Opciones

En el cuadro de diálogo Personalizar están disponibles las siguientes pestañas:

### Commandos

![](images/Std_DlgCustomize_tab_Commands.png ) 
*La pestaña Comandos*

En esta pestaña puede examinar los comandos disponibles.

#### Comandos navegación 

1.  Seleccione una categoría de comandos en el panel **Categoría** de la izquierda. Algunas categorías coinciden con las entradas del menú.
2.  Las herramientas disponibles en la categoría seleccionada se muestran en el panel de la derecha.
3.  Pase el ratón por un comando: aparece su información sobre la herramienta.
4.  Seleccione un comando: el texto de su barra de estado se muestra debajo de los dos paneles.


{{Top}}

### Teclado

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*La pestaña del teclado*

En esta pestaña se pueden definir atajos de teclado personalizados. Los atajos de teclado para los comandos de macros se pueden definir en la pestaña [Macros](#Macros.md).

#### Añadir un atajo personalizado 

1.  Select a command category from the **Category** dropdown list.
2.  Select a command from the **Commands** panel.
3.  The **Current shortcut** box displays the current short cut, if available.
4.  Enter a new shortcut in the **Press new shortcut** input box. Shortcuts can be up to 4 inputs long. Each input is either a single character, a combination of one or more special keys or a combination of one or more special keys and a character. Use **Backspace** to correct mistakes.
5.  If the shortcut is already in use, a dialog box will ask you if you want to override it, and the command the shortcut is assigned to will appear in the **Currently assigned to** panel.
6.  Press the **Assign** button to assign the new shortcut.
7.  Press the **Clear** button to remove the entered shortcut. This will also remove the content of the **Current shortcut** box. Note that default shortcuts are not permanently removed. They will be restored upon restarting FreeCAD.

#### Eliminar un atajo personalizado 

1.  Select a command category from the **Category** dropdown list.
2.  Select a command from the **Commands** panel.
3.  Press the **Reset** button.

#### Eliminar todo atajos personalizado 

1.  Pulse el botón **Reiniciar todo**.

#### Notas (Teclado) 

-   Shortcuts only work if their commands appear in the standard menu or in the menu of a workbench that has been loaded in the current FreeCAD session, or if their commands appear on a *visible* toolbar.

-   In V0.19 there is an issue with some Draft commands. Their default shortcuts do not work and/or custom shortcuts cannot be assigned to them.
-   To reassign a default shortcut a new shortcut has to be assigned to its original command first.


{{Top}}

### Ambientes de trabajo 

![](images/Std_DlgCustomize_tab_Workbenches.png ) 
*La pestaña Ambientes de trabajo*

On this tab the [Workbench selector](Std_Workbench.md) list can be changed. The **Enabled workbenches** list shows the workbenches as they will appear in the Workbench selector.

#### Desactivar un ambiente de trabajo 

1.  Select a workbench in the **Enabled workbenches** list.
2.  Press the **<img src="images/Button_left.svg" width=16px>** button.
3.  The workbench will be moved to the **Disabled workbenches** list

#### Habilitar un ambiente de trabajo 

1.  Select a workbench in the **Disabled workbenches** list.
2.  Press the **<img src="images/Button_right.svg" width=16px>** button.
3.  The workbench will be moved to the **Enabled workbenches** list

#### Habilitar todo ambientes de trabajo 

1.  Press the **<img src="images/Button_add_all.svg" width=16px>** button.

#### Cambiar la posición de un ambiente de trabajo 

1.  Select a workbench in the **Enabled workbenches** list.
2.  Press the **<img src="images/Button_up.svg" width=16px>** button or the **<img src="images/Button_down.svg" width=16px>** button.
3.  Optionally repeat this until the workbench is in the correct position.

#### Ordenar los ambinetes de trabajo alfabéticamente 

1.  Press the **<img src="images/Button_sort.svg" width=16px>** button.


{{Top}}

### Barras Herramientas 

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*La pestaña Barras Herramientas*

En esta pestaña se pueden crear y modificar barras de herramientas personalizadas.

#### Seleccione el ambiente de trabajo 

1.  In the dropdown list on the right select the workbench whose custom toolbars you want to modify. The {{Value|Global}} option is there for custom toolbars that should be available in all workbenches.

#### Crear una barra herramientas 

1.  Press the **New...** button.
2.  Enter a name in the dialog box that opens.
3.  Press the **OK** button.
4.  The new toolbar will appear in the panel on the right.

#### Renombrar una barra herramientas 

1.  Select a toolbar in the panel on the right.
2.  Press the **Rename...** button.
3.  Enter a new name in the dialog box that opens.
4.  Press the **OK** button.

#### Eliminar una barra herramientas 

1.  Select a toolbar in the panel on the right.
2.  Press the **Delete** button.

#### Desactivar una barra herramientas 

1.  Uncheck the checkbox in front of the toolbar name in the panel on the right.
2.  A disabled toolbar will be invisible in the FreeCAD interface.

#### Añadir un comando 

1.  At least one custom toolbar is required. See [Create a toolbar](#Create_a_toolbar.md).
2.  Select the correct toolbar in the panel on the right. If no toolbar is selected, the command will be added to the first toolbar in the list.
3.  Select a category from the dropdown list on the left. Macro commands that have been set up on the [Macros](#Macros.md) tab appear in the \'Macros\' category.
4.  Select a command from the panel on the left.
5.  Or select \'\' to add a separator (a line between two toolbar buttons).
6.  Press **<img src="images/Button_right.svg" width=16px>** button.

#### Elimina un comando 

1.  If required, expand the toolbar in the panel on the right.
2.  Select a command.
3.  Press **<img src="images/Button_left.svg" width=16px>** button.

#### Cambiar la posición de un position comando 

1.  If required, expand the toolbar in the panel on the right.
2.  Select a command.
3.  Press the **<img src="images/Button_up.svg" width=16px>** button or the **<img src="images/Button_down.svg" width=16px>** button.
4.  Optionally repeat this until the command is in the correct position.

#### Notas (Barras Herramienta) 

-   Toolbars belonging to the current workbench are updated immediately, but after disabling/re-enabling a toolbar a workbench change is required (switch to a different workbench and then switch back).
-   To update global toolbars a workbench change (if commands have been added or removed) or a restart (if the order of a toolbar has changed or a toolbar was renamed) is required.

-   In V0.19 there is an issue with some Draft commands. After adding them to a custom toolbar and exiting the FreeCAD application the {{FileName|user.cfg}} file must be manually edited for these commands. Search for the name of the custom toolbar and in that section change the content of the `FCText` items that start with `gui_` to `DraftTools`.


{{Top}}

### Macros

![](images/Std_DlgCustomize_tab_Macros.png ) 
*La pestaña Macros*

On this tab user macro commands can be set up. Once set up, they can be added to custom toolbars. FreeCAD uses a dedicated folder for user macros and only macros in that folder can be set up. Use the <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Std DlgMacroExecute](Std_DlgMacroExecute.md) command to find this folder on your system.

If you download a macro with the <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr.md) then make sure that you also download its icon image file. Most macros have an image link on the information page that appears in the Addon Manager. You can for example put this image file in the user macros folder.

If you want to use a macro downloaded from a different source you will have to install it manually. See [How to install macros](How_to_install_macros.md) for more information.

#### Añadir un macrocomando 

1.  In the **Macro** dropdown list select a macro.
2.  Enter a **Menu text**. This will be the name used to identify the macro command and will also appear in the toolbar if there is no icon.
3.  Optionally enter a **Tool tip**. This text will appear near the location of the mouse when you hover the toolbar icon.
4.  Optionally enter a **Status text**. This text will appear in the [status bar](Status_bar.md) when you hover the toolbar icon.
5.  Optionally enter the wiki page for the macro, if available, in the **What\'s this** input box. Enter the page name, not the full URL.
6.  Optionally enter a shortcut in the **Accelerator** input box. See [Keyboard](#Keyboard.md) for more information.
7.  To add an icon:
    1.  Press the **Pixmap** **...** button.
    2.  The Choose Icon dialog box opens.
    3.  If required press the **Icon folders...** button to add an icon folder.
    4.  Select an icon from the panel. The Choose Icon dialog box closes automatically.
8.  Press the **Add** button.
9.  The macro command appears in the panel on the left.
10. The macro command can now be selected on the [Toolbars](#Toolbars.md) tab.

#### Elimina un macrocomando 

1.  Select the macro command in the panel on the left.
2.  Press the **Remove** button.

#### Cambiar un macrocomando 

1.  Double-click the macro command in the panel on the left.
2.  Make the required changes. Note that you cannot remove the icon, you can only replace it.
3.  Press the **Replace** button.


{{Top}}

### Movimiento Bola Espacial 

This tab is blank if no Spaceball is detected. See: [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

### Botones Bola Espacial 

This is tab is blank if no Spaceball is detected. See: [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

## Temas

FreeCAD supports complete theming of the interface, via .qss stylesheets. The [qss format](https://doc.qt.io/qt-5/stylesheet-syntax.html) is very similar to the [css format](https://en.wikipedia.org/wiki/CSS) used in web pages, it basically adds methods to reference the different widgets and elements of the Qt interface. You can change the default theme (which simply takes the style defined by your desktop system) by selecting a **style sheet** in the [FreeCAD preferences](Preferences_Editor#General.md).

You can also create your own theme if you are not satisfied with the themes that are bundled with FreeCAD, for example by editing an [existing style sheet](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Your new style must be placed in a specific folder for it to be found by FreeCAD:

-    {{FileName|%APPDATA%/FreeCAD/Gui/Stylesheets}}(on Windows). The {{FileName|%APPDATA%}} folder can be retrieved by entering {{Incode|App.getUserAppDataDir()}} in the [Python console](Python_console.md).

-    {{FileName|$HOME/.FreeCAD/Gui/Stylesheets}}(on Linux).

-    {{FileName|$HOME/Library/Preferences/FreeCAD/Gui/Stylesheets}}(on MacOS).


{{Top}}

## Complementos

Los complementos ofrecen otra forma de personalizar la interfaz de uso. A continuación se muestran algunos complementos creados por usuarios de la comunidad de FreeCAD. Pueden descargarse a través del <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Gestor Complementos](Std_AddonMgr/es.md) (nota: están listados en la pestaña ambientes de trabajo).

### MenúCubo

-   Repositorio de Github: <https://github.com/triplus/CubeMenu>

### Glass

-   Repositorio de Github: <https://github.com/triplus/Glass>.

### TemasIconos

-   Repositorio de Github: <https://github.com/triplus/IconThemes>

### Arranquer

-   Repositorio de Github: <https://github.com/triplus/Launcher>

### PieMenú

-   Repositorio de Github: <https://github.com/triplus/PieMenu>

### RemBanco

-   Repositorio de Github: <https://github.com/triplus/RemBench>

### Atajo

-   Repositorio de Github: <https://github.com/triplus/ShortCuts>


{{Top}}





{{Std Base navi

}} {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Interface Customization/es
