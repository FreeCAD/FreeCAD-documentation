---
- GuiCommand:/it
   Name:Std ShowObjects
   Name/it:Std ShowObjects
   Empty:1
   MenuLocation:Visualizza → Visibilità → Mostra tutti gli oggetti
   Workbenches:Tutti
   SeeAlso:[Mostra/Nascondi](Std_ToggleVisibility/it.md), [Mostra la selezione](Std_ShowSelection/it.md), [Nascondi la selezione](Std_HideSelection/it.md), [Commuta tutti gli oggetti](Std_ToggleObjects/it.md), [Nascondi tutti gli oggetti](Std_HideObjects/it.md)
---

# Std ShowObjects/it


</div>

## Descrizione

The **Std ShowObjects** command shows all objects belonging to the active document in [3D views](3D_view.md). Be careful when you use this command as it will also show sub-elements of [PartDesign bodies](PartDesign_Body.md) and objects used for [Part Booleans](Part_Boolean.md). In most cases these should stay invisible.

## Utilizzo

1.  Select the **View → Visibility → <img src="images/Std_ShowObjects.svg" width=16px> Show all objects** option from the menu.

## Note

-   The action of this command cannot be undone with [Std Undo](Std_Undo.md).
-   The visibility of an object can also be changed through its related **Visibility** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

For a scripting example see [Std ToggleVisibility](Std_ToggleVisibility.md).


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ShowObjects/it
