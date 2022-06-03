---
- GuiCommand   */ro
   Name   *Std MergeProjects
   Name/ro   *Fuzionați Proiectul
   Workbenches   *All
   MenuLocation   *File → Fuzionați Proiectul
   Shortcut   *
   SeeAlso   *
---

# Std MergeProjects/ro


</div>

## Descriere

Incorporează un alt proiect FreeCAD în cel actual.

The **Std MergeProjects** command adds the contents of a FreeCAD file into the active document.


<div class="mw-translate-fuzzy">

## Utilizare

1.  Alegeți ** File** → ** Merge project...** din meniul principalu.
2.  Va apărea un dialog contextual care vă va solicita numele fișierului și locația proiectului FreeCAD care urmează să fie îmbinate în cel curent.


</div>

1.  Select the **File → <img src="images/Std_MergeProjects.svg" width=16px> Merge project...** option from the menu.
2.  Select a FreeCAD file in the dialog box.
3.  Press the **Open** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   A project cannot be merged with itself, selecting the current file is not allowed.
-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.

## Preferences

-   The last used file location is stored   * **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Duplicate labels are allowed if **Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels** is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std MergeProjects/ro
