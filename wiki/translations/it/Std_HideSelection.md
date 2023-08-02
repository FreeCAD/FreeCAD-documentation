---
- GuiCommand:
   Name: Std HideSelection
   Name/it: Nascondi la selezione
   MenuLocation: Visualizza -> Visibilità -> Nascondi la selezione
   Workbenches: Tutti
   SeeAlso: Std_ToggleVisibility/it, Std_ShowSelection/it, Std_ToggleObjects/it, Std_ShowObjects/it, Std_HideObjects/it
---

# Std HideSelection/it



## Descrizione

Il comando **Nascondi la selezione** nasconde gli oggetti selezionati nella [Vista 3D](3D_view/it.md).



## Utilizzo

1.  Selezionare uno o più oggetti.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → Visibilità → <img src="images/Std_HideSelection.svg" width=16px> Nascondi selezione** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_HideSelection.svg" width=16px> Nascondi selezione** dal menu contestuale [Vista albero](Tree_view/it.md). Questa opzione non è disponibile in [PartDesign](PartDesign_Workbench/it.md).



## Note

-   Gli oggetti invisibili vengono visualizzati con un\'etichetta in grigio e un\'icona in grigio nella [Vista ad albero](Tree_view/it.md).
-   Oggetti nidificati in una [Parte](Std_Part/it.md), o [Link](Std_LinkMake/it.md) verso un [Gruppo](Std_Group/it.md), o in un LinkGroup, e [funzioni](PartDesign_Feature/it.md) di un [Corpo di PartDesign](PartDesign_Body/it.md) saranno visibili solo nella [Vista 3D](3D_view/it.md) se anche il loro genitore è visibile. Ciò significa che una funzione in un corpo di PartDesign annidata in una parte standard sarà visibile solo nelle viste 3D se la funzione stessa, il corpo di PartDesign e la parte standard sono tutti visibili. E se l\'oggetto Part è a sua volta nidificato in un altro oggetto Part, anche quest\'ultimo oggetto deve essere visibile.
-   Se la visibilità di un [Gruppo](Std_Group/it.md) (o di un oggetto derivato da esso come un [Parte di edificio Arch](Arch_BuildingPart/it.md)) viene modificata, la visibilità dei suoi oggetti nidificati cambierà di conseguenza. Ma anche la loro visibilità può essere modificata in modo indipendente.
-   L\'azione di questo comando non può essere annullata con [Annulla](Std_Undo/it.md).
-   La visibilità di un oggetto può anche essere modificata tramite la relativa proprietà **Visibility** in [Editor delle proprietà](Property_editor/it.md) o nella [Vista combinata](Combo_view/it.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per un esempio di script vedere [Commutare la visibilità](Std_ToggleVisibility/it.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std HideSelection/it
