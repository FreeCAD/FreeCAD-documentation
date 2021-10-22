---
- GuiCommand:/fr
   Name:EM FHPlaneAddRemoveNodeHole
   Name/fr:EM FHPlaneAddRemoveNodeHole
   MenuLocation:EM → FHPlaneAddRemoveNodeHole
   Workbenches:[EM](EM_Workbench/fr.md) (Addon)
   Shortcut:E A
   SeeAlso:[EM FHPlane](EM_FHPlane/fr.md), [EM FHNode](EM_FHNode/fr.md), [EM FHPlaneHole](EM_FHPlaneHole/fr.md)
   Version:0.17
---

# EM FHPlaneAddRemoveNodeHole/fr

## Description

L\'outil FHPlaneAddRemoveNodeHole insère ou supprime des FHNodes ou FHPlaneHoles d\'un objet FHPlane.

![](images/EM_FHPlaneAddRemoveNodeHole_Example.png ) 
*Noeuds ajoutés (bleu) et supprimés (rouge) d'un FHPlane, et un FHPlaneHole retiré du FHPlane (sans couper un trou dans le plan)*

## Utilisation

Pour supprimer un ou plusieurs objets FHNode ou objets FHPlaneHole d\'un FHPlane:

1.  Sélectionnez tous les objets [EM FHNode](EM_FHNode/fr.md) ou [EM FHPlaneHole](EM_FHPlaneHole/fr.md) que vous souhaitez supprimer du FHPlane (notez que vous devez étendre la liste des enfants du FHPlane si vous souhaitez sélectionner ces objets de l\'arborescence au lieu de la vue 3D actuelle).
2.  Appuyez sur le bouton **<img src="images/EM_FHPlaneAddRemoveNodeHole.svg" width=16px> [EM FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/fr.md)** ou appuyez sur les touches **E** puis **A**.

Pour insérer un ou plusieurs objets FHNode ou objets FHPlaneHole dans un FHPlane:

1.  Sélectionnez les [EM FHPlane](EM_FHPlane/fr.md) et tous les objets [EM FHNode](EM_FHNode/fr.md) ou [EM FHPlaneHole](EM_FHPlaneHole/fr.md) que vous souhaitez insérer dans le FHPlane.
2.  Appuyez sur le bouton **<img src="images/EM_FHPlaneAddRemoveNodeHole.svg" width=16px> [EM FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/fr.md)** ou appuyez sur les touches **E** puis **A**.

### Remarques

Vous pouvez également supprimer des objets FHNode ou FHPlaneHole d\'un FHPlane et insérer simultanément un ou plusieurs objets FHNode ou FHPlaneHole dans un FHPlane. Tous les objets FHNode ou FHPlaneHole qui appartiennent déjà à un FHPlane seront supprimés de ce FHPlane, tandis que les autres seront ajoutés au FHPlane sélectionné.

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour ajouter ou supprimer des objets FHNode ou FHPlaneHole d\'un FHPlane via des scripts Python, il suffit d\'ajouter ou de supprimer les objets des propriétés pertinentes de l\'objet FHPlane. La PropertyList fait l\'objet d\'un suivi des changements, de sorte que le FHNode ou le FHPlaneHole sera traité comme prévu (changement de couleur, etc.)


{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHPlaneAddRemoveNodeHole/fr
