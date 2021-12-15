---
- GuiCommand:/fr
   Name:EM FHPlaneAddRemoveNodeHole
   Name/fr:EM Bascule noeud trou FH
   MenuLocation:EM → FHPlaneAddRemoveNodeHole
   Workbenches:[EM](EM_Workbench/fr.md)
   Shortcut:**E** **A**
   Version:0.17
   SeeAlso:[EM Plan FH](EM_FHPlane/fr.md), [EM Noeud FH](EM_FHNode/fr.md), [EM Trou FH](EM_FHPlaneHole/fr.md)
---

# EM FHPlaneAddRemoveNodeHole/fr

## Description

L\'outil Bascule noeud trou FH insère ou supprime des Noeuds FH ou desF Trous FH d\'un objet Plan FH.

![](images/EM_FHPlaneAddRemoveNodeHole_Example.png )



*Noeuds FH ajoutés (bleu) et supprimés (rouge) d'un Plan FH et un Trou FH retiré du Plan FH (sans découper de trou dans le plan)*

## Utilisation

Pour supprimer un ou plusieurs objets Noeuds FH ou objets Trou FH d\'un Plan FH:

1.  Sélectionnez tous les objets [EM Noeud FH](EM_FHNode/fr.md) ou [EM Trou FH](EM_FHPlaneHole/fr.md) que vous souhaitez supprimer du Plan FH (notez que vous devez étendre la liste des enfants du Plan FH si vous souhaitez sélectionner ces objets de la [Vue en arborescence](Tree_view/fr.md) au lieu de la [vue 3D](3D_view/fr.md) en cours).
2.  Appuyez sur le bouton **<img src="images/EM_FHPlaneAddRemoveNodeHole.svg" width=16px> [EM FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/fr.md)** ou appuyez sur les touches **E** puis **A**.

Pour insérer un ou plusieurs objets Noeud FH ou objets Trou FH dans un Plan FH:

1.  Sélectionnez le [EM Plan FH](EM_FHPlane/fr.md) et tous les objets [EM Noeud FH](EM_FHNode/fr.md) ou [EM Trou FH](EM_FHPlaneHole/fr.md) que vous souhaitez insérer dans le Plan FH.
2.  Appuyez sur le bouton **<img src="images/EM_FHPlaneAddRemoveNodeHole.svg" width=16px> [EM FHPlaneAddRemoveNodeHole](EM_FHPlaneAddRemoveNodeHole/fr.md)** ou appuyez sur les touches **E** puis **A**.

### Remarques

Vous pouvez également supprimer des objets Noeud FH ou Trou FH d\'un Plan FH et insérer simultanément un ou plusieurs objets Noeud FH ou Trou FH dans un Plan FH. Tous les objets Noeud FH ou Trou FH qui appartiennent déjà à un Plan FH seront supprimés de ce Plan FH, tandis que les autres seront ajoutés au Plan FH sélectionné.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour ajouter ou supprimer des objets Noeud FH ou Trou FH d\'un Plan FH via des scripts Python, il suffit d\'ajouter ou de supprimer les objets des propriétés pertinentes de l\'objet Plan FH. La PropertyList fait l\'objet d\'un suivi des changements, de sorte que le Noeud FH ou le Trou FH sera traité comme prévu (changement de couleur, etc.)





{{EM Tools navi

}}

---
[documentation index](../README.md) > EM FHPlaneAddRemoveNodeHole/fr
