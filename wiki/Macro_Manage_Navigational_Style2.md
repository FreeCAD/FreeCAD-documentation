# Macro Manage Navigational Style2
{{Macro
|Name=Macro Manage Navigational Styles2
|Icon=Macro_Manage_Navigational_Styles2.png
|Description=This macro allow you to alter the Navigation Style Inventor while using the Sketcher.<br/>When using the Sketcher the right-button menu is redefined to hold options relevant to the Sketcher. Consequently the option to change the Navigational Style, which is available when outside the Sketcher,  is not available when in the Sketcher.
|Author=PiffPoof
|Version=1.0
|Date=2015-01-17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/1/1c/Macro_Manage_Navigational_Styles2.png ToolBar icon]
|SeeAlso=[Macro_Manage_Navigational_Style1](Macro_Manage_Navigational_Style.md)
}}

## Description

When using the Sketcher the right-button menu is redefined to hold options relevant to the Sketcher. Consequently the option to change the Navigational Style, which is available when outside the Sketcher, is not available when in the Sketcher.

## Installation

There are two brief code snippets, each of which is a separate Macro. Installation is comprised of copying the two pieces code to the appropriate Macro directory and invoking them from the Macro menu. It is much preferable to add them both to a toolbar so as to be easily available while using the Sketcher.

-   see [How to install macros](How_to_install_macros.md) for information on how to install this macro code
-   see [Customize Toolbars](Customize_Toolbars.md) for information how to install as a button on a toolbar

## Usage

Click on the associated toolbar button, or invoke from the Macro menu. There is no visible confirmation of their executing, aside from the Navigational Style will change.

## User Interface 

There really isn\'t any user interface, not even any confirmation that the Navigational Style has been changed. The confirmation will be when you next manipulate the view, your mouse movements will interpreted in the Navigational Style you selected.

## Scripts

-   icon and macro code to change the Navigational Style to \'Inventor\'



![](images/Macro_Manage_Navigational_Styles2.png )

**Macro\_Manage\_Navigational\_Styles2\_Inventor.FCMacro**


{{MacroCode|code=
# change to Inventor Navigational Style
p=App.ParamGet("User parameter:BaseApp/Preferences/View")
p.SetString("NavigationStyle","Gui::InventorNavigationStyle")
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Manage Navigational Style2
