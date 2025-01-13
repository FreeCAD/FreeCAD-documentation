---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM MaterialEditor
   Name/de: FEM MaterialEditor
   MenuLocation: Modell , Materialien , Material editor
   Workbenches: FEM_Workbench/de, Arch_Workbench/de
   Version: 0.18
   SeeAlso: Arch_SetMaterial/de, FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: Alle
}}
---

# FEM MaterialEditor/de



## Beschreibung

Mit dem **Material-Editor** kann man die in einem [FreeCAD-Material](Material.md) gespeicherten Informationen bearbeiten und speichern. Derzeit werden diese Materialien von den Arbeitsbereichen <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench/de.md) und <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/de.md) verwendet.

![](images/Material_editor.png )



## Anwendung

Derzeit hat man zwei Möglichkeiten den Material-Editor aufzurufen:

1.  Arbeitsbereich <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/de.md):
    -   Die Schaltfläche **<img src="images/BIM_Material.svg" width=16px> [Material](BIM_Material/de.md)** drücken.
    -   Den Menüeintrag **Verwalten → <img src="images/BIM_Material.svg" width=16px> Material** auswählen.
2.  Arbeitsbereich <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench/de.md):
    -   Die Schaltfläche **<img src="images/FEM_MaterialEditor.svg" width=16px> [Material-Editor](FEM_MaterialEditor/de.md)** drücken.
    -   Den Menüeintrag **Modell → Materialien → <img src="images/FEM_MaterialEditor.svg" width=16px> Material-Editor** auswählen.



## Optionen

-   **Browser button**: Opens the contents of the URL property in a browser

-   **Material card**: Allows to choose a preset to fill in the fields

-    **Open**: Opens a .FCMat file

-    **Save as**: Saves the contents of the editor as a new .FCMat file

-   **Preview**: Not implemented yet

-   **Properties editor**: Allows to edit the contents of the material properties

-    **Add property**: Allows to add a new custom property

-    **Delete property**: Deletes a selected property. Only custom properties can be deleted



## Hinweise

-   The **OK** and **Cancel** buttons have the same effect when the Material editor is not used to edit directly the material property of an existing object.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialEditor/de
