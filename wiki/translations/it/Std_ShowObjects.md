---
- GuiCommand:
   Name:Std ShowObjects
   Name/it:Mostra tutti gli oggetti
   MenuLocation:Visualizza → Visibilità → Mostra tutti gli oggetti
   Workbenches:Tutti
   SeeAlso:[Mostra/Nascondi](Std_ToggleVisibility/it.md), [Mostra la selezione](Std_ShowSelection/it.md), [Nascondi la selezione](Std_HideSelection/it.md), [Commuta tutti gli oggetti](Std_ToggleObjects/it.md), [Nascondi tutti gli oggetti](Std_HideObjects/it.md)
---

# Std ShowObjects/it



## Descrizione

Il comando **Mostra tutti gli oggetti** mostra tutti gli oggetti appartenenti al documento attivo nella [Vista 3D](3D_view/it.md). Prestare attenzione quando si utilizza questo comando poiché mostrerà anche i sottoelementi dei [Corpi di PartDesign](PartDesign_Body/it.md) e gli oggetti utilizzati per [operazioni booleane](Part_Boolean/it.md). Nella maggior parte dei casi questi dovrebbero rimanere invisibili.



## Utilizzo

1.  Selezionare l\'opzione **Visualizza → Visibilità → <img src="images/Std_ShowObjects.svg" width=16px> Mostra tutti gli oggetti** dal menu.



## Note

-   L\'azione di questo comando non può essere annullata con [Annulla](Std_Undo/it.md).
-   La visibilità di un oggetto può anche essere modificata tramite la relativa proprietà **Visibility** in [Editor delle proprietà](Property_editor/it.md) o nella [Vista combinata](Combo_view/it.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per un esempio di script vedere [Commutare la visibilità](Std_ToggleVisibility/it.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ShowObjects/it
