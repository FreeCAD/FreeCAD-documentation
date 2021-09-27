---
- GuiCommand:/fr
   Name:Material_editor
   Name/fr:Editeur de matériaux
   Icon:Arch_Material_Group.svg
   MenuLocation:Model → Material → Material editor
   Workbenches:[FEM](FEM_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Version:0.18
   SeeAlso:[Matériau](Material/fr.md), [Arch Matériaux](Arch_SetMaterial/fr.md), [Tutoriel FEM](FEM_tutorial/fr.md)
---

# Material editor/fr

## Description

L\'éditeur de matériaux alloue, édite ou sauve les informations contenues dans [matériaux](Material/fr.md). Le module matériaux est utilisé par les ateliers **<img src="images/Workbench_FEM.svg" width=24px> [FEM](FEM_Workbench/fr.md)** et **<img src="images/Workbench_Arch.svg" width=24px> [Arch](Arch_Workbench/fr.md)**.

![](images/Material_editor.jpg )

## Utilisation

L\'éditeur de matériau est accessible soit par:

1.  <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Atelier Arch](Arch_Workbench/fr.md)
    -   Le bouton <img alt="" src=images/Arch_SetMaterial.svg  style="width:16px;"> [Matériaux](Arch_SetMaterial/fr.md) du panneau de création [Nouveau matériaux](Arch_SetMaterial/fr.md) du panneau de l\'[Atelier Arch](Arch_Workbench/fr.md)
    -   L\'entrée du menu **Arch → Outils matériaux...**
2.  <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [Atelier FEM](FEM_Workbench/fr.md)
    -   L\'icône <img alt="" src=images/Arch_Material_Group.svg  style="width:16px;"> [Editeur de matériaux](Material_editor/fr.md)
    -   L\'entrée du menu **Models → Materials → Material editor**
3.  Via Python (voir la section [Script](#Script.md) ci-dessous)

## Options

-   **Browser button**: Ouvre l\'url des propriétés dans un navigateur web

-   **Material card**: Choix d\'un champs prédéterminé

-    **Open**: Ouvre un fichier .FCMat

-    **Save as**: Sauvegarde le contenu de l\'éditeur dans un nouveau fichier .FCMat file

-   **Preview**: Pas encore implémenté

-   **Properties editor**: Alloue ou édite le contenu des propriétés du matériau

-    **Add property**: Alloue ou ajoute une nouvelle propriété

-    **Delete property**: Efface les propriétés du matériau

Remarque:

-   Les boutons **OK** et **Cancel** ont le même effet dans l\'éditeur de matériaux et ne sont pas utilisés directement dans les propriétés du matériau de l\'objet existant.

## Script


```python
import MaterialEditor
MaterialEditor.openEditor()
```





{{FEM Tools navi

}}

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Material](Material_Workbench.md) > Material editor/fr
