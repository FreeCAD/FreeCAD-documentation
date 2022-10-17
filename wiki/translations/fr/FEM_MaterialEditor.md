---
- GuiCommand   */fr
   Name   *FEM MaterialEditor
   Name/fr   *FEM Éditeur de matériaux
   MenuLocation   *Modèle → Matériaux → Éditeur de matériaux
   Workbenches   *[FEM](FEM_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Version   *0.18
   SeeAlso   *[Matériaux](Material/fr.md), [Arch Matériaux](Arch_SetMaterial/fr.md), [Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM MaterialEditor/fr

## Description

L**\'Éditeur de matériaux** vous permet de modifier et de sauvegarder les informations contenues dans un [matériau de FreeCAD](Material/fr.md). Actuellement, ces matériaux sont utilisés par les ateliers <img alt="" src=images/Workbench_FEM.svg  style="width   *24px;"> [FEM](FEM_Workbench/fr.md) et <img alt="" src=images/Workbench_Arch.svg  style="width   *24px;"> [Arch](Arch_Workbench/fr.md).

![](images/Material_editor.png )

## Utilisation

L\'éditeur de matériau est accessible soit par    *

1.  L\'<img alt="" src=images/Workbench_Arch.svg  style="width   *24px;"> [Atelier Arch](Arch_Workbench/fr.md)
    -   Le bouton **<img src="images/Arch_SetMaterial.svg" width=16px> [Matériau](Arch_SetMaterial/fr.md)**.
    -   L\'entrée du menu **Arch → Outils pour les matériaux → <img src="images/Arch_SetMaterial.svg" width=16px> Matériau**.
2.  L\'<img alt="" src=images/Workbench_FEM.svg  style="width   *24px;"> [Atelier FEM](FEM_Workbench/fr.md)
    -   Le bouton **<img src="images/FEM_MaterialEditor.svg" width=16px> [Editeur de matériaux](FEM_MaterialEditor/fr.md)**.
    -   L\'entrée du menu **Modèle → Matériaux → <img src="images/FEM_MaterialEditor.svg" width=16px> Éditeur de matériaux**.

## Options

-   **Bouton du navigateur**    * ouvre le contenu de la propriété URL dans un navigateur.

-   **Carte de matériau**    * permet de choisir un préréglage pour remplir les champs.

-    **Ouvrir**   * ouvre un fichier .FCMat.

-    **Enregistrer sous**   * enregistre le contenu de l\'éditeur comme un nouveau fichier .FCMat.

-   **Aperçu**    * pas encore implémenté.

-   **Éditeur de propriétés**    * permet d\'éditer le contenu des propriétés des matériaux.

-    **Ajouter une propriété**   * permet d\'ajouter une nouvelle propriété personnalisée.

-    **Supprimer la propriété**   * supprime une propriété sélectionnée. Seules les propriétés personnalisées peuvent être supprimées.

## Remarques

-   Les boutons **OK** et **Annuler** ont le même effet dans l\'éditeur de matériaux et ne sont pas utilisés directement dans les propriétés du matériau de l\'objet existant.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialEditor/fr
