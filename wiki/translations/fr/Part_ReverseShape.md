---
 GuiCommand:
   Name: Part ReverseShape‏‎
   Name/fr: Part Inverser les formes
   MenuLocation: Part , Inverser les formes
   Workbenches: Part_Workbench/fr
---

# Part ReverseShape/fr

## Description

La commande <img alt="" src=images/Part_ReverseShape.svg  style="width:24px;"> **Part Inverser la forme** crée des copies paramétriques avec des normales aux faces inversées à partir d\'objets sélectionnés.



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Sélectionnez l\'option du menu **Part → <img src="images/Part_ReverseShape.svg" width=16px> Inverser les formes**.
3.  Pour chaque objet sélectionné, une forme inversée est créée.



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être utilisés comme objets sources. {{Version/fr|0.20}}
-   Pour voir l\'effet de la commande, changez la propriété **Lighting** de la forme inversée en {{Value|On side}} et, si nécessaire, modifiez **Édition → Préférences... → Affichage → Vue 3D → Rendu → Couleur du rétroéclairage**.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Part Inverser la forme la forme est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Reverse}}

-    **Source|Link**: spécifie la forme source liée.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ReverseShape/fr
