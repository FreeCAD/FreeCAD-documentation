---
 GuiCommand:
   Name: Assembly3 AddXYWorkplane
   Name/fr: Assembly3 Ajouter un plan de travail
   Icon: Assembly_Add_Workplane.svg‎‎
   MenuLocation: Assembly3 , Workplane and origin , Add workplane
   Workbenches: Assembly3_Workbench/fr
---

# Assembly3 AddWorkplane/fr

## Description

La commande <img alt="" src=images/Assembly_Add_Workplane.svg  style="width:24px;"> [Ajouter un plan de travail](Assembly3_AddWorkplane/fr.md) ajoute un plan de travail à un assemblage actif.

Un objet Workplane sera créé dans le conteneur Parts de l\'arbre d\'assemblage et un élément plan de travail associé sera placé dans la vue 3D. Il est placé à l\'origine de l\'assemblage et orienté selon le plan XY de l\'assemblage, si l\'objet Assemblage a été sélectionné directement.

<img alt="" src=images/Assembly_Add_Workplane-01.png  style="width:250px;"> <img alt="" src=images/Assembly_Add_Workplane-02.png  style="width:350px;">

L\'assemblage peut également être sélectionné indirectement par un élément appartenant à l\'assemblage. Le plan de travail est alors placé à l\'origine de l\'élément et orienté selon le plan XY local de cet élément.

Les éléments valides sont par exemple les éléments, les corps, les sommets, les arêtes, les faces, les origines et les autres plans de travail de la [Vue en arborescence](Tree_view/fr.md) ou de la [Vue 3D](3D_view/fr.md).

## Utilisation

1.  Activez la commande <img alt="" src=images/Assembly_Add_Workplane.svg  style="width:16px;"> **Ajouter un plan de travail** en utilisant l\'une des commandes suivantes :
    -   Le bouton **<img src="images/Assembly_Add_Workplane.svg_" width=16px> [Add workplane](Assembly3_AddWorkplane/fr.md)**.
    -   L\'option de menu **Assembly3 → Workplane and origin → <img src="images/Assembly_Add_Workplane.svg_" width=16px> Add workplane**.



---
⏵ [documentation index](../README.md) > Assembly3 AddWorkplane/fr
