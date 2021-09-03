---
- GuiCommand:/de   Name:Std Redo   Name/de:Std Wiederherstellen   MenuLocation:[|Workbenches:Alle   Shortcut:**Strg**+**Y**   SeeAlso:[[Std_Undo/de|Rückgängig](Std_Edit_Menu/de___Bearbeiten]]_→_Wiederherstellen‎.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

Wendet den durch *Rückgängig* zurückgenommenen Befehl erneut wieder an.


</div>


<div class="mw-translate-fuzzy">

## Anwendung

1.  Klicke auf <img alt="" src=images/Std_Redo.png  style="width:32px;"> oder wähle **Bearbeiten** → **<img src="images/Std_Redo.png" width=32px> Wiederherstellen** aus der Menüleiste.


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Redo.svg" width=16px> [Std Redo](Std_Redo.md)** button.
    -   Select the {{MenuCommand|Edit → <img src="images/Std_Redo.svg" width=16px> Redo}} option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**Y**.

## Options

-   To redo multiple actions click on the black down arrow to the right of the **<img src="images/Std_Redo.svg" width=16px> [Std Redo](Std_Redo.md)** button and select from the list.

## Preferences

-   The Undo/Redo functionality can be disabled by setting {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → UsingUndo}} to `False`, but this is not recommended. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).
-   The maximum number of Undo/Redo steps is controlled by {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → MaxUndoSize}}. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To redo an action that has just been undone use the `redo` method of the document object.


```python
import FreeCAD

FreeCAD.ActiveDocument.redo()
```





{{Std Base navi

}}  
