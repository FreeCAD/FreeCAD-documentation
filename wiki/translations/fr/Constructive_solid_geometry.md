# Constructive solid geometry/fr
{{TOCright}}

## Introduction

La [géométrie solide constructive](https://fr.wikipedia.org/wiki/Géométrie_de_construction_de_solides) (**CSG**) est un paradigme de modélisation utilisé dans de nombreux systèmes de CAO traditionnels. Cela consiste essentiellement à utiliser des objets solides primitifs et à effectuer des opérations booléennes, telles que la fusion, la soustraction et l\'intersection, afin de créer une forme finale.

Dans FreeCAD, cette méthode est principalement utilisée avec l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md), qui permet de créer des objets primitifs tels que des <img alt="" src=images/Part_Box.svg  style="width:24px;"> [boîtes](Part_Box/fr.md), des <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [cylindres](Part_Cylinder/fr.md), des <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [sphères](Part_Sphere.md), et de les fusionner, ou de les utiliser pour couper d\'autres objets avec des outils tels que **<img src="images/Part_Cut.svg" width=24px> [Part Soustraction](Part_Cut/fr.md)**.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">



*Flux de travail d'une géométrie solide constructive (CSG); un nombre quelconque d'opérations peuvent être effectuées sur des primitives solides pour créer d'autres objets solides, puis fusionnées ou coupées jusqu'à ce que la forme finale soit produite.*

Autre possibilité l'<img alt="Workbench_PartDesign.svg" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md) utilise une approche plus moderne que le simple CSG. cette méthode est appelée [édition de fonctions](feature_editing/fr.md), ce qui signifie la création d'un solide de base, puis l'ajout de transformations paramétriques séquentielles pour obtenir un corps final.


**Remarque:**

Un [PartDesign Corps](PartDesign_Body/fr.md) créé avec l\'[atelier PartDesign](PartDesign_Workbench.md) peut également être utilisé dans une opération booléenne avec d\'autres objets.

## Exemple

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">



*Exemple de flux de travail d'une géométrie solide constructive (CSG) : les pièces primitives sont fusionnées (union) ; l'intersection de deux autres parties primitives est calculée (commune) ; la différence (coupe) des deux formes précédentes est obtenue.*

## Tutoriels

La page [Tutoriels](tutorials/fr.md) fournit des exemples de création de solides avec l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) utilisant la méthode **CSG**.

-   [Modélisation traditionnelle, mode CSG](Manual:Traditional_modeling,_the_CSG_way/fr.md)
-   [Tutoriel balle Whiffle](Whiffle_Ball_tutorial/fr.md)
-   [Tutoriel d\'introduction à la modélisation](Basic_modeling_tutorial/fr.md)

 

[<img src="images/Property.png" style="width:16px"> Common Questions](Category_Common_Questions.md)

---
[documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > Constructive solid geometry/fr
