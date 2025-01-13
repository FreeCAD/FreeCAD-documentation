---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM MaterialEditor
   Name/fr: FEM Éditeur de matériaux
   MenuLocation: Modèle , Matériaux , Éditeur de matériaux
   Workbenches: FEM_Workbench/fr, Arch_Workbench/fr
   Version: 0.18
   SeeAlso: Arch_SetMaterial/fr, FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: Tous
}}
---

# FEM MaterialEditor/fr

## Description

L**\'Éditeur de matériaux** vous permet de modifier et de sauvegarder les informations contenues dans un [matériau de FreeCAD](Material/fr.md). Actuellement, ces matériaux sont utilisés par les ateliers <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench/fr.md) et <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM](BIM_Workbench/fr.md).

![](images/Material_editor.png )



## Utilisation

L\'éditeur de matériau est accessible soit par :

1.  L\'<img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [atelier BIM](BIM_Workbench/fr.md)
    -   Le bouton **<img src="images/BIM_Material.svg" width=16px> [Matériau](BIM_Material/fr.md)**.
    -   L\'entrée du menu **Gestion → <img src="images/BIM_Material.svg" width=16px> Matériau**.
2.  L\'<img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [atelier FEM](FEM_Workbench/fr.md)
    -   Le bouton **<img src="images/FEM_MaterialEditor.svg" width=16px> [Éditeur de matériaux](FEM_MaterialEditor/fr.md)**.
    -   Le menu **Modèle → Matériaux → <img src="images/FEM_MaterialEditor.svg" width=16px> Éditeur de matériaux**.

## Options

-   **Bouton du navigateur** : ouvre le contenu de la propriété URL dans un navigateur.

-   **Jeu de paramètres du matériau** : permet de choisir un préréglage pour remplir les champs.

-    **Ouvrir**: ouvre un fichier .FCMat.

-    **Enregistrer sous**: enregistre le contenu de l\'éditeur comme un nouveau fichier .FCMat.

-   **Aperçu** : pas encore implémenté.

-   **Éditeur de propriétés** : permet d\'éditer le contenu des propriétés des matériaux.

-    **Ajouter une propriété**: permet d\'ajouter une nouvelle propriété personnalisée.

-    **Supprimer la propriété**: supprime une propriété sélectionnée. Seules les propriétés personnalisées peuvent être supprimées.



## Remarques

-   Les boutons **OK** et **Annuler** ont le même effet dans l\'éditeur de matériaux et ne sont pas utilisés directement dans les propriétés du matériau de l\'objet existant.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialEditor/fr
