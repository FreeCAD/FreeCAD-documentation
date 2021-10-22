# Interface Customization/zh-cn
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

由于FreeCAD界面是基于现代的[Qt](http://en.wikipedia.org/wiki/Qt_(toolkit))工具包制作，因此它具有最先进的组织架构。widget部件、菜单、工具栏与其他工具都可修改、移动、在工具台之间共享，还可设置、修改快捷键，并记录和执行宏（macro）。通过**Tools → Customize**菜单即可进行窗口的定制：


</div>

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*The Customize dialog box*

## Usage

1.  The commands available in the Customize dialog box depend on the workbenches that have been loaded in the current FreeCAD session. So you should first load all workbenches whose commands you want to have access to.
2.  There are several ways to invoke the <img alt="" src=images/Std_DlgCustomize.svg  style="width:16px;"> [Std DlgCustomize](Std_DlgCustomize.md) command:
    -   Select the **Tools → <img src="images/Std_DlgCustomize.svg" width=16px> Customize...** option from the menu.
    -   Right-click a toolbar area and choose **<img src="images/Std_DlgCustomize.svg" width=16px> Customize...** from the context menu.
3.  The Customize dialog box opens. For more information see [Options](#Options.md).
4.  The **Help** button does not work at this time.
5.  Press the **Close** button to close the dialog box.

## Options

In the Customize dialog box the following tabs are available:

### Commands

![](images/Std_DlgCustomize_tab_Commands.png ) 
*The Commands tab*

On this tab you can browse the available commands.

#### Browse commands 

1.  Select a command category in the **Category** panel on the left. Some categories match menu entries.
2.  The tools available in the selected category are shown in the panel on the right.
3.  Hover a command: its tooltip appears.
4.  Select a command: its status bar text is displayed below the two panels.


{{Top}}

### Keyboard

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*The Keyboard tab*

On this tab custom keyboard shortcuts can be defined. Shortcuts for macro commands can be defined on the [Macros](#Macros.md) tab.

#### Add a custom shortcut 

1.  Select a command category from the **Category** dropdown list.
2.  Select a command from the **Commands** panel.
3.  The **Current shortcut** box displays the current short cut, if available.
4.  Enter a new shortcut in the **Press new shortcut** input box. Shortcuts can be up to 4 inputs long. Each input is either a single character, a combination of one or more special keys or a combination of one or more special keys and a character. Use **Backspace** to correct mistakes.
5.  If the shortcut is already in use, a dialog box will ask you if you want to override it, and the command the shortcut is assigned to will appear in the **Currently assigned to** panel.
6.  Press the **Assign** button to assign the new shortcut.
7.  Press the **Clear** button to remove the entered shortcut. This will also remove the content of the **Current shortcut** box. Note that default shortcuts are not permanently removed. They will be restored upon restarting FreeCAD.

#### Remove a custom shortcut 

1.  Select a command category from the **Category** dropdown list.
2.  Select a command from the **Commands** panel.
3.  Press the **Reset** button.

#### Remove all custom shortcuts 

1.  Press the **Reset All** button.

#### Notes (Keyboard) 

-   Shortcuts only work if their commands appear in the standard menu or in the menu of a workbench that has been loaded in the current FreeCAD session, or if their commands appear on a *visible* toolbar.

-   In V0.19 there is an issue with some Draft commands. Their default shortcuts do not work and/or custom shortcuts cannot be assigned to them.
-   To reassign a default shortcut a new shortcut has to be assigned to its original command first.


{{Top}}

### Workbenches

![](images/Std_DlgCustomize_tab_Workbenches.png ) 
*The Workbenches tab*

On this tab the [Workbench selector](Std_Workbench.md) list can be changed. The **Enabled workbenches** list shows the workbenches as they will appear in the Workbench selector.

#### Disable a workbench 

1.  Select a workbench in the **Enabled workbenches** list.
2.  Press the **<img src="images/Button_left.svg" width=16px>** button.
3.  The workbench will be moved to the **Disabled workbenches** list

#### Re-enable a workbench 

1.  Select a workbench in the **Disabled workbenches** list.
2.  Press the **<img src="images/Button_right.svg" width=16px>** button.
3.  The workbench will be moved to the **Enabled workbenches** list

#### Re-enable all workbenches 

1.  Press the **<img src="images/Button_add_all.svg" width=16px>** button.

#### Change a workbench position 

1.  Select a workbench in the **Enabled workbenches** list.
2.  Press the **<img src="images/Button_up.svg" width=16px>** button or the **<img src="images/Button_down.svg" width=16px>** button.
3.  Optionally repeat this until the workbench is in the correct position.

#### Sort workbenches alphabetically 

1.  Press the **<img src="images/Button_sort.svg" width=16px>** button.


{{Top}}

### Toolbars

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*The Toolbars tab*

On this tab custom toolbars can be created and modified.

#### Select the workbench 

1.  In the dropdown list on the right select the workbench whose custom toolbars you want to modify. The {{Value|Global}} option is there for custom toolbars that should be available in all workbenches.

#### Create a toolbar 

1.  Press the **New...** button.
2.  Enter a name in the dialog box that opens.
3.  Press the **OK** button.
4.  The new toolbar will appear in the panel on the right.

#### Rename a toolbar 

1.  Select a toolbar in the panel on the right.
2.  Press the **Rename...** button.
3.  Enter a new name in the dialog box that opens.
4.  Press the **OK** button.

#### Delete a toolbar 

1.  Select a toolbar in the panel on the right.
2.  Press the **Delete** button.

#### Disable a toolbar 

1.  Uncheck the checkbox in front of the toolbar name in the panel on the right.
2.  A disabled toolbar will be invisible in the FreeCAD interface.

#### Add a command 

1.  At least one custom toolbar is required. See [Create a toolbar](#Create_a_toolbar.md).
2.  Select the correct toolbar in the panel on the right. If no toolbar is selected, the command will be added to the first toolbar in the list.
3.  Select a category from the dropdown list on the left. Macro commands that have been set up on the [Macros](#Macros.md) tab appear in the \'Macros\' category.
4.  Select a command from the panel on the left.
5.  Or select \'\' to add a separator (a line between two toolbar buttons).
6.  Press **<img src="images/Button_right.svg" width=16px>** button.

#### Remove a command 

1.  If required, expand the toolbar in the panel on the right.
2.  Select a command.
3.  Press **<img src="images/Button_left.svg" width=16px>** button.

#### Change a command position 

1.  If required, expand the toolbar in the panel on the right.
2.  Select a command.
3.  Press the **<img src="images/Button_up.svg" width=16px>** button or the **<img src="images/Button_down.svg" width=16px>** button.
4.  Optionally repeat this until the command is in the correct position.

#### Notes (Toolbars) 

-   Toolbars belonging to the current workbench are updated immediately, but after disabling/re-enabling a toolbar a workbench change is required (switch to a different workbench and then switch back).
-   To update global toolbars a workbench change (if commands have been added or removed) or a restart (if the order of a toolbar has changed or a toolbar was renamed) is required.

-   In V0.19 there is an issue with some Draft commands. After adding them to a custom toolbar and exiting the FreeCAD application the {{FileName|user.cfg}} file must be manually edited for these commands. Search for the name of the custom toolbar and in that section change the content of the `FCText` items that start with `gui_` to `DraftTools`.


{{Top}}

### Macros

![](images/Std_DlgCustomize_tab_Macros.png ) 
*The Macros tab*

On this tab user macro commands can be set up. Once set up, they can be added to custom toolbars. FreeCAD uses a dedicated folder for user macros and only macros in that folder can be set up. Use the <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Std DlgMacroExecute](Std_DlgMacroExecute.md) command to find this folder on your system.

If you download a macro with the <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr.md) then make sure that you also download its icon image file. Most macros have an image link on the information page that appears in the Addon Manager. You can for example put this image file in the user macros folder.

If you want to use a macro downloaded from a different source you will have to install it manually. See [How to install macros](How_to_install_macros.md) for more information.

#### Add a macro command 

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

#### Remove a macro command 

1.  Select the macro command in the panel on the left.
2.  Press the **Remove** button.

#### Change a macro command 

1.  Double-click the macro command in the panel on the left.
2.  Make the required changes. Note that you cannot remove the icon, you can only replace it.
3.  Press the **Replace** button.


{{Top}}

### Spaceball Motion 

This tab is blank if no Spaceball is detected. See: [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

### Spaceball Buttons 

This is tab is blank if no Spaceball is detected. See: [3Dconnexion input devices](3Dconnexion_input_devices.md). {{Top}}

## Themes

FreeCAD supports complete theming of the interface, via .qss stylesheets. The _.

You can also create your own theme if you are not satisfied with the themes that are bundled with FreeCAD, for example by editing an [existing style sheet](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Your new style must be placed in a specific folder for it to be found by FreeCAD:

-    {{FileName|%APPDATA%/FreeCAD/Gui/Stylesheets}}(on Windows). The {{FileName|%APPDATA%}} folder can be retrieved by entering {{Incode|App.getUserAppDataDir()}} in the [Python console](Python_console.md).

-    {{FileName|$HOME/.FreeCAD/Gui/Stylesheets}}(on Linux).

-    {{FileName|$HOME/Library/Preferences/FreeCAD/Gui/Stylesheets}}(on MacOS).


{{Top}}

## Addons

Addons offer yet another way to customize the use interface. Below are some addons created by users in the FreeCAD community. They can be downloaded through the <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Addon Manager](Std_AddonMgr.md) (note: they are listed on the Workbenches tab).

### CubeMenu

-   Github repository: <https://github.com/triplus/CubeMenu>

### Glass

-   Github repository: <https://github.com/triplus/Glass>.

### IconThemes

-   Github repository: <https://github.com/triplus/IconThemes>

### Launcher

-   Github repository: <https://github.com/triplus/Launcher>

### PieMenu

-   Github repository: <https://github.com/triplus/PieMenu>

### RemBench

-   Github repository: <https://github.com/triplus/RemBench>

### ShortCut

-   Github repository: <https://github.com/triplus/ShortCuts>


{{Top}}





{{Std Base navi

}} {{Interface navi}}

---
[documentation index](../README.md) > Interface Customization/zh-cn
