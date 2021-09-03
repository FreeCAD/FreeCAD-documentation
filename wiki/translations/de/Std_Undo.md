---
- GuiCommand:/de   Name:Std Undo   Name/de:Std Rückgängig   MenuLocation:[Workbenches:Alle   Shortcut:**Strg**+**Z**   SeeAlso:[[Std Redo/de|Wiederherstellen](Std_Edit_Menu/de___Bearbeiten]]_→_Rückgängig.md)---


</div>


<div class="mw-translate-fuzzy">

## Beschreibung

Macht genau eine Aktion rückgängig.


</div>

The **Std Undo** command undoes the last action.


<div class="mw-translate-fuzzy">

## Anwendung

Klicke auf <img alt="" src=images/Std_Undo.png  style="width:32px;"> oder wähle **Bearbeiten** → **<img src="images/Std_Undo.png" width=32px> Rückgängig** aus der Menüleiste.
Klicke auf den schwarzen Pfeil-nach-unten rechts neben <img alt="" src=images/Std_Undo.png  style="width:32px;">, um aus einer Liste der maximal zwölf letzten Aktionen auswählen zu können.


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Undo.svg" width=16px> [Std Undo](Std_Undo.md)** button.
    -   Select the **Edit → <img src="images/Std_Undo.svg" width=16px> Undo** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**Z**.

## Options

-   To undo multiple actions click on the small black down arrow to the right of the **<img src="images/Std_Undo.svg" width=16px> [Std Undo](Std_Undo.md)** button and select from the list.

## Preferences

-   The Undo/Redo functionality can be disabled by setting **Tools → Edit parameters... → BaseApp → Preferences → Document → UsingUndo** to `False`, but this is not recommended. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).
-   The maximum number of Undo/Redo steps is controlled by **Tools → Edit parameters... → BaseApp → Preferences → Document → MaxUndoSize**. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To undo the last action use the `undo` method of the document object.


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```





{{Std Base navi

}}  
