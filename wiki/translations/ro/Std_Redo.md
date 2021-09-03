---
- GuiCommand:   Name:Std Redo   MenuLocation:[|Workbenches:All   Shortcut:Maiusc+Ctrl+Z   SeeAlso:[[Std_Undo|Undo](Std_Edit_Menu___Edit]]_→_Redo‏‎.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Această comandă resetează operațiile anulate anterior.


</div>


<div class="mw-translate-fuzzy">

## Utilizare

1.  Deschideți meniul **Modify**, click pe <img alt="" src=images/Std_Redo.png  style="width:32px;"> sau alegeți ** Edit** → **<img src="images/Std_Redo.png" width=32px> Redo** din meniul de sus/top.

o altă posibilitate este utilizare acombinației de taste {{KEY/it|CTRL+Y}}.

Cu fiecare clic al mouse-ului sau combinația de taste, ultima operație anulată este restaurată înapoi.

Numărul de operațiuni care pot fi modificate poate fi definit în **Modifica → Preferenze → Generale → Documento**. În mod implicit, pot fi restaurate ultimele \"\" 20 \"\" de operațiuni modificate.

![Menu\_Annulla\_Ripristina](images/PreferenzeAnnulla.png )


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
