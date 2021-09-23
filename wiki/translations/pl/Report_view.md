# Report view/pl
## Introduction

The [Report view](Report_view.md) is a panel that shows text messages from FreeCAD processes and tools. It is available in the menu **{{StdMenu|[View](Std_View_Menu.md)** → Panels → Report view}}.

Certain properties of this panel, like color of the text and whether to display it automatically on warnings or errors, can be configured in the **General → Output window** tab of the [preferences editor](Preferences_Editor.md).

<img alt="" src=images/FreeCAD_Report_view.png  style="width:800px;">


*The report view showing messages when FreeCAD has just started.*

## Messages


**See also:**

[Console API](Console_API.md), and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The report view displays messages from the internal FreeCAD `Console` class.

-    `FreeCAD.Console.PrintMessage("text")`, print any sort of informative message, that doesn\'t imply any misbehavior; for example, print the coordinates of points, the result of a distance calculation, the number of vertices in a shape, etc. By default, in black color.

-    `FreeCAD.Console.PrintWarning("text")`, print messages that are intended to warn the user about strange behavior in the application. Warnings should be shown when some functionality is missing but the software still works acceptably. By default, in yellow color.

-    `FreeCAD.Console.PrintError("text")`, print messages that are intended to be error messages, that is, when a critical component is missing that makes a certain operation fail. By default, in red color.

-    `FreeCAD.Console.PrintLog("text")`, print messages that are going into the logs. These messages could be anything that is valuable to troubleshoot a problem in the future by reading the logs, for example, starting or closing a workbench. By default, in blue color.

These functions can be used from the [Python console](Python_console.md) directly, or from [macros](Macros.md) and custom workbenches.

<img alt="" src=images/FreeCAD_Report_view_example.png  style="width:800px;">


*Example messages in the report view: a general message, a warning, an error, and a logged message.*

## Actions

Right click on the report view shows some commands:

-    **Options**: logging, warning, error, redirect Python output, redirect Python errors, go to end.

-    **Copy**: stores the selected text in the clipboard for later pasting; it is disabled if nothing is selected.

-    **Select all**: selects all text in the report view.

-    **Clear**: erases all messages in the report view. This is useful if you want to troubleshoot a tool that prints messages to the report view, and want to be sure there are no old messages from previous tools.

-    **Save as**: save the messages in the report view to a text file.


{{Interface navi

}} {{Std Base navi}}

---
[documentation index](../README.md) > Report view/pl
