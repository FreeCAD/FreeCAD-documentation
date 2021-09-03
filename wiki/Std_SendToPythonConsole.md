---
- GuiCommand:
   Name:Std SendToPythonConsole
   MenuLocation:Edit → Send to Python Console
   Workbenches:All
   Shortcut:**Ctrl**+**Shift**+**P**
   Version:0.19
---

## Description

The **Std SendToPythonConsole** command creates a variable in the [Python console](Python_console.md) referencing a selected object. If a subshape of the object is selected two additional variables are created, one referencing the shape of the object and the other referencing the subshape itself. The variables and the code involved can be used to development Python code.



>>> ### Begin command Std_SendToPythonConsole
>>> obj = App.getDocument("Unnamed").getObject("Box")
>>> shp = App.getDocument("Unnamed").getObject("Box").Shape
>>> elt = App.getDocument("Unnamed").getObject("Box").Shape.Edge8
>>> ### End command Std_SendToPythonConsole

 *Example output: an edge of a [Part Box](Part_Box.md) was selected*

## Usage

1.  Select a single object.
2.  There are several ways to invoke the command:
    -   Select the {{MenuCommand|Edit → <img src="images/Std_SendToPythonConsole.svg" width=16px> Send to Python Console}} option from the menu.
    -   Select the {{MenuCommand|<img src="images/Std_SendToPythonConsole.svg" width=16px> Send to Python Console}} option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Ctrl**+**Shift**+**P**.




 {{Std Base navi}}  
