# Macro Toggle Panels Visibility/en
{{Macro
|Name=Macro Toggle Panels Visibility
|Icon=Macro_Toggle_Views_Visibility.png
|Description=This macro toggles the visibility of various supporting views in FreeCAD, allowing the main window to be viewed with all available screen space.
|Author=Piffpoof
|Version=1.0
|Date=2015-01-17
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/d/d0/Macro_Toggle_Views_Visibility.png Toolbar icon]
|SeeAlso=[https://forum.freecadweb.org/viewtopic.php?f=22&t=30450&hilit=Toggle_Panels Toggle_Panels]
}}

## Description

When working with FreeCAD there are times when you need many supporting windows open, such as Combo View, Report View, etc. There are other times when you want all the clutter of the supporting windows to disappear so that all the screen space available can be used to view the model being worked with. This macro lets you hide all the supporting windows (or make them visible again) with one click on the toolbar.

## Installation

Save the provided code to the appropriate Macro directory and execute it from the Macro menu. It is preferable to add it to a toolbar for ease of access.

-   see [How to install macros](How_to_install_macros.md) for information on how to install this macro code
-   see [Customize Toolbars](Customize_Toolbars.md) for information how to install as a button on a toolbar

## Usage

Click on the associated toolbar button, or invoke from the Macro menu. The supporting windows Python console, Report view, Combo view will either all become visible or all become hidden.

## User Interface 

There is immediate confirmation of the user action as the supporting windows either appear or disappear.

## Scripts

Toolbar icon ![](images/Macro_Toggle_Views_Visibility.png )

**Macro\_Toggle\_Panels\_Visibility.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
# macro to toggle visibility of Report view, Python console, Combo view
from PySide import QtCore, QtGui
mainWindow = FreeCADGui.getMainWindow()
dockWidgets = mainWindow.findChildren(QtGui.QDockWidget)
for dw in dockWidgets:
    if dw.objectName() == "Python console":
        pcWidget = dw
    if dw.objectName() == "Combo View":
        cvWidget = dw
    if dw.objectName() == "Report view":
        rvWidget = dw
     
if pcWidget.isVisible():
    pcWidget.hide()
    cvWidget.hide()
    rvWidget.hide()
else:
    pcWidget.show()
    cvWidget.show()
    rvWidget.show()

}}

---
[documentation index](../README.md) > Macro Toggle Panels Visibility/en
