---
- GuiCommand   */fr
   Name   *Draft Array
   Name/fr   *Draft Réseau
   MenuLocation   *Draft → Réseau
   Workbenches   *[Draft](Draft_Workbench/fr.md)
   SeeAlso   *[Draft Réseau polaire](Draft_PolarArray/fr.md), [Draft Réseau circulaire](Draft_CircularArray/fr.md), [Draft Chemin pour série de copies](Draft_PathArray/fr.md), [Draft Matrice de points](Draft_PointArray/fr.md), [Draft Clone](Draft_Clone/fr.md)
---

# Draft Array/fr


</div>

## Description


<div class="mw-translate-fuzzy">

L\'outil **<img src="images/Draft_Array.svg" width=16px> [Draft Réseau (tableau ou copies multiples)](Draft_Array/fr.md)** crée une copie orthogonale (3 axes) ou un tableau polaire ou ciruclaire de l\'objet sélectionné.


</div>


<div class="mw-translate-fuzzy">

Cet outil peut être utilisé sur des formes 2D créées avec l\'[atelier Draft](Draft_Workbench/fr.md), mais également sur de nombreux types d\'objets 3D, tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md).


</div>

This command is now obsolete. Use the [Draft OrthoArray](Draft_OrthoArray.md), [Draft PolarArray](Draft_PolarArray.md) or [Draft CircularArray](Draft_CircularArray.md) command instead.

## Usage


<div class="mw-translate-fuzzy">

## Utilisation

1.  Sélectionnez l\'objet pour créer un réseau.
2.  Pressez le bouton **<img src="images/Draft_Array.png" width=16px> [Réseau Draft](Draft_Array/fr.md)**. Si aucun objet n\'est sélectionné vous serez invité à en sélectionner un.
3.  L\'objet Array est créé immédiatement. Vous devez modifier les propriétés du tableau pour modifier le nombre et la direction des copies créées.


</div>

## Properties


<div class="mw-translate-fuzzy">

## Propriétés

-    {{PropertyData/fr|Base}}   * spécifie l\'objet à dupliquer dans le tableau.

-    {{PropertyData/fr|Array Type|Enumeration}}   * spécifie le type de tableau à créer, {{value|"ortho"}}, {{value|"polar"}}, ou {{value|"circular"}}.

-    {{PropertyData/fr|Fuse}}   * si elle est réglée sur `True` et que les copies se croisent, elles seront fusionnées en une seule forme.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Voir aussi    ***

[Draft API](Draft_API/fr.md) et [FreeCAD Scripts de base](FreeCAD_Scripting_Basics/fr.md).


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/fr
