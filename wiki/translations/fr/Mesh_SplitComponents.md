---
- GuiCommand:/fr
   Name:Mesh SplitComponents
   Name/fr:Mesh Séparer
   MenuLocation:Maillages → Eclater par composants
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Fusionner](Mesh_Merge/fr.md)
---

## Description

La commande **Mesh Séparer** divise un objet maillé en ses composants. Un composant de maillage est un groupe complet de faces connectées. Pour chaque composant, un nouvel objet maillage non paramétrique, un [Mesh Feature](Mesh_Feature/fr.md), est créé. Si l\'objet maillage d\'origine ne contient qu\'un seul composant, et c\'est généralement le cas, un seul nouvel objet maillage, en fait une copie, est créé. Cette commande est le pendant de la commande [Mesh Fusionner](Mesh_Merge/fr.md).

## Utilisation

1.  Sélectionnez un seul objet maillé.
2.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_SplitComponents.svg" width=16px> [Eclater le maillage sélectionné en composants](Mesh_SplitComponents/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_SplitComponents.svg" width=16px> Eclater par composants** dans le menu.

## Propriétés

Voir: [Mesh Feature](Mesh_Feature/fr.md).





{{Mesh Tools navi

}}  
