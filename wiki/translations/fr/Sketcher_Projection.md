---
 GuiCommand:
   Name: Sketcher Projection
   Name/fr: Sketcher Projection
   MenuLocation: Esquisse , Outils d'esquisse , Créer la géométrie externe de la projection 
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **X**
   Version: 1.1
   SeeAlso: Sketcher_ToggleConstruction/fr
---

# Sketcher Projection/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projection](Sketcher_Projection/fr.md) projette sur le plan de l\'esquisse les arêtes et/ou les sommets appartenant à des objets situés en dehors de l\'esquisse. La géométrie projetée est appelée \"géométrie externe\". Elle reste paramétriquement liée à ses objets sources. La géométrie externe est marquée par une [couleur](Sketcher_Preferences/fr#Apparence.md) (magenta par défaut) et un type de ligne dédiés. Il peut s\'agir d\'une géométrie de définition visible en dehors de l\'esquisse ou d\'une géométrie de construction non visible en dehors de l\'esquisse.



## Utilisation

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_Projection.svg" width=16px> [Créer la géométrie externe de la projection](Sketcher_Projection/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_Projection.svg" width=16px> Créer la géométrie externe de la projection** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_Projection.svg" width=16px> Créer la géométrie externe de la projection** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **X**.
2.  Le curseur se transforme en croix avec l\'icône de l\'outil.
3.  Sélectionnez une ou plusieurs faces externes, arêtes et/ou sommets. Voir [Remarques](#Remarques.md).
4.  La géométrie externe est créée.
5.  Cet outil fonctionne toujours en mode continu : vous pouvez continuer à sélectionner des faces, des arêtes et/ou des sommets externes.
6.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap** ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Toutes les arêtes d\'une face sont projetées sur le plan d\'esquisse.
-   La géométrie externe est créée en tant que géométrie de définition ou géométrie de construction en fonction de l\'état de l\'outil [Sketcher Géométrie de construction](Sketcher_ToggleConstruction/fr.md). Cet outil peut également être utilisé pour basculer le mode de chaque arête. Cochez l\'option **Édition → Préférences... → Sketcher → Général → Toujours ajouter les géométries externes comme des géométries de référence** pour ignorer le statut de cet outil et toujours ajouter la géométrie externe comme géométrie de construction.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Projection/fr
