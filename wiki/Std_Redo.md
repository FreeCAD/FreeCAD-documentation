---
- GuiCommand:
   Name:Std Redo
   MenuLocation:Edit → Redo
   Workbenches:All
   Shortcut:**Ctrl**+**Y**
   SeeAlso:[Std Undo](Std_Undo.md)
---

# Std Redo

## Description

The **Std Redo** command reverses the action of the [Std Undo](Std_Undo.md) command.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Redo.svg" width=16px> [Std Redo](Std_Redo.md)** button.
    -   Select the **Edit → <img src="images/Std_Redo.svg" width=16px> Redo** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**Y**.

## Options

-   To redo multiple actions click on the black down arrow to the right of the **<img src="images/Std_Redo.svg" width=16px> [Std Redo](Std_Redo.md)** button and select from the list.

## Preferences

-   The Undo/Redo functionality can be disabled by setting **Tools → Edit parameters... → BaseApp → Preferences → Document → UsingUndo** to `False`, but this is not recommended. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).
-   The maximum number of Undo/Redo steps is controlled by **Tools → Edit parameters... → BaseApp → Preferences → Document → MaxUndoSize**. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To redo an action that has just been undone use the `redo` method of the document object.

 
```python
import FreeCAD

FreeCAD.ActiveDocument.redo()
```




 {{Std Base navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Redo
