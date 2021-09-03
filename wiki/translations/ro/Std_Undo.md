---
- GuiCommand:   Name:Std Undo   MenuLocation:[Workbenches:All   Shortcut:Ctrl+Z   SeeAlso:[[Std Redo|Redo](Std_Edit_Menu___Edit]]_→_Undo.md)---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Anulează exact o acțiune.


</div>

The **Std Undo** command undoes the last action.


<div class="mw-translate-fuzzy">

## Utilizare

Click pe <img alt="" src=images/Std_Undo.png  style="width:32px;"> sau alegeți ** Edit** → **<img src="images/Std_Undo.png" width=32px> Undo** din meniul principal.
Faceți clic pe săgeata în jos negru din partea dreaptă a iconiței pentru a obține o listă cu maxim 12 acțiuni de selectat.


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Undo.svg" width=16px> [Std Undo](Std_Undo.md)** button.
    -   Select the {{MenuCommand|Edit → <img src="images/Std_Undo.svg" width=16px> Undo}} option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**Z**.

## Options

-   To undo multiple actions click on the small black down arrow to the right of the **<img src="images/Std_Undo.svg" width=16px> [Std Undo](Std_Undo.md)** button and select from the list.

## Preferences

-   The Undo/Redo functionality can be disabled by setting {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → UsingUndo}} to `False`, but this is not recommended. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).
-   The maximum number of Undo/Redo steps is controlled by {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → MaxUndoSize}}. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).

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
