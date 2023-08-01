---
- GuiCommand:/de
   Name:FEM PostApplyChanges
   Name/de:FEM PostApplyChanges
   MenuLocation:Ergebnisse → Änderungen auf Pipeline anwenden
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[Std Aktualisieren](Std_Refresh/de.md), [NachbereitungFunktionenErstellen](FEM_PostCreateFunctions/de.md)
---

# FEM PostApplyChanges/de



## Beschreibung

Toggles if changes to pipelines and filters are applied immediately or not.

If the feature is active, changes to [filter functions](FEM_PostCreateFunctions.md) and filters have an immediate effect. However, for large result meshes this can slow down the PC significantly.

If the feature is not active, a change of the size and position of functions first have an effect after recomputing the function object (see [Std Refresh](Std_Refresh.md)). For changes to filters, the change will first have an effect when pressing in the filter dialog the button **Apply** or by recomputing the filter object.



## Anwendung

Click the toolbar button **<img src="images/FEM_PostApplyChanges.svg" width=16px> '''Apply changes to pipeline'''** or use the menu **Results → <img src="images/FEM_PostApplyChanges.svg" width=16px> Apply changes to pipeline**.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostApplyChanges/de
