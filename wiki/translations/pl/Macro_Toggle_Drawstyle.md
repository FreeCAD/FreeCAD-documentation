# Macro Toggle Drawstyle/pl
{{Macro
|Name=Macro Toggle Drawstyle
|Description=When working with FreeCAD there are times when you want to quickly change the Drawstyle of the object you are working with. This is available through the Drawstyle pull-down menu where any Drawstyle may be selected. This macro makes 2 of the Drawstyles available as a clickable button on a toolbar which the user may click to toggle back and forth between the two Drawstyles. The user can modify the macro code to select which 2 Drawstyles they wish to toggle between. This does not add functionality missing in the Drawstyles pull-down menu, but rather an increased convenience level.
|Author=Piffpoof
|Version=2.0
|Date=2020-02-02
|FCVersion= >=0.17
|Download=[https://www.freecadweb.org/wiki/images/0/0b/Macro_Toggle_Drawstyle.png ToolBar Icon]
|SeeAlso=[Macro Toggle Drawstyle Optimized](Macro_Toggle_Drawstyle_Optimized.md) <img src="images/Macro_Toggle_Drawstyle_Optimized.png" width=24px> for all language
}}

## Description

When working with FreeCAD there are times when you want to quickly change the Drawstyle of the object you are working with. This is available through the Drawstyle pull-down menu where any Drawstyle may be selected. This macro makes 2 of the Drawstyles available as a clickable button on a toolbar which the user may click to toggle back and forth between the two Drawstyles. The user can modify the macro code to select which 2 Drawstyles they wish to toggle between. This does not add functionality missing in the Drawstyles pull-down menu, but rather an increased convenience level.

## Installation

Installation is comprised of copying the two code to the appropriate Macro directory and invoking it from the Macro menu. It is much preferable to add it both to a toolbar so as to be more easily available.

-   see [How to install macros](How_to_install_macros.md) for information on how to install this macro code
-   see [Customize Toolbars](Customize_Toolbars.md) for information how to install as a button on a toolbar

## Usage

Select an object, then click on the associated toolbar button, or invoke from the Macro menu. The Drawstyle of the slected object will toggle between the two drawstyles specified in the macro code (see code listing below). **Note**: The specification for each Drawstyle is listed in the code, by modifying the code (which is documented in the macro code) the user may select which 2 Drawstyles are toggled between.

## User Interface 

The selected object will be redrawn in the other drawstyle specified in the macro.

Script optimized for all languages and to object selected or all objects [Keyboard shortcut, View toolbar - Wireframe](https://forum.freecadweb.org/viewtopic.php?f=3&t=14336&start=40#p146239) (Sun Nov 27, 2016 6:49 pm)

## Script

ToolBar icon ![](images/Macro_Toggle_Drawstyle.png )

**Macro Toggle Drawstyle.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
#
#
#           Macro: Toggle Draw Style
#
# This macros allows the user to switch between different Drawstyles by clicking on
# the button of a Macro in a toolbar.
#
# initial code:     triplus
# macro-isation:    piffpoof
#
# This macro switches (or toggles) between 2 selected styles from the Drawstyle menu.
# As written the macro toggles between "WireFrame" and "As is".
# Immediately below this text is a list of the legal values for the Drawstyle menu.
# The first 2 lines of executable code are of the form "DrawstyleA = " followed by
# the 2nd line which is of the form "DrawstyleB = ".
# These 2 lines specify which of the Drawstyle values the macro will toggle between.
# Drawstyle "As is" is the system default and so is specified as the first drawstyle.
# The second line specifies which drawstyle will be toggled to and from.
# Any of the legal values may be used, so if, for example, it is desired to toggle between
# the Shaded and Points drawstyles, then the 2 lines of code would be modified to be:
#
# drawstyleA = "Shaded"
# drawstyleB = "Points"
#
# but remember that the hash signs ('#') are not to be present on the executable lines.
#
###Legal Values for Drawstyle###
#
# 0 = "As is"
# 1 = "Flat lines"
# 2 = "Shaded
# 3 = "Wireframe"
# 4 = "Points"
# 5 = "Hidden line"
# 6 = "No shading"
#
################################

# triplus @ 2016, 2020
# Toggle global display mode
# ==============================

# 0 = "As is"
# 1 = "Flat lines"
# 2 = "Shaded
# 3 = "Wireframe"
# 4 = "Points"
# 5 = "Hidden line"
# 6 = "No shading"

styleA = 0
styleB = 3

# ==============================

from PySide import QtGui
import FreeCADGui as Gui

mw = Gui.getMainWindow()


act = {
    0: mw.findChild(QtGui.QAction, "Std_DrawStyleAsIs"),
    1: mw.findChild(QtGui.QAction, "Std_DrawStyleFlatLines"),
    2: mw.findChild(QtGui.QAction, "Std_DrawStyleShaded"),
    3: mw.findChild(QtGui.QAction, "Std_DrawStyleWireframe"),
    4: mw.findChild(QtGui.QAction, "Std_DrawStylePoints"),
    5: mw.findChild(QtGui.QAction, "Std_DrawStyleHiddenLine"),
    6: mw.findChild(QtGui.QAction, "Std_DrawStyleNoShading"),
}


actionA = act[styleA]
actionB = act[styleB]


if actionA.isChecked():
    actionB.trigger()
else:
    actionA.trigger()

}}

## Link

The forum discussion [Keyboard shortcut, View toolbar - Wireframe](https://forum.freecadweb.org/viewtopic.php?f=3&t=14336)

---
[documentation index](../README.md) > Macro Toggle Drawstyle/pl
