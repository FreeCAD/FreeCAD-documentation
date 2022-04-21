---
- GuiCommand:/fr
   Name:Ship Weight
   Name/fr:Ship Poids
   MenuLocation:Weights → Create a new ship weight
   Workbenches:[Ship](Ship_Workbench/fr.md)
   Shortcut:
   SeeAlso:
---

# Ship Weight/fr

## Description

Ajoute un poids à l\'instance du bateau.

Jusqu\'à ce stade, tous les outils de Ship workbench sont basés sur une **instance de bateau** (voir [Créer une coque](Ship_New/fr.md)), qui ne contient que des informations sur la forme du bateau. Suivant le système d\'introduction progressive des données, l\'utilisateur peut à ce stade définir des conditions de charge, ce qui implique de créer des poids avec cet outil, de créer des réservoirs (voir [Création de réservoirs](Ship_TankNew/fr.md)) et de les assembler dans des conditions de charge (voir [Conditions de charge](Ship_Loading/fr.md)). Avec ces informations, le centre de gravité du bateau peut être défini, permettant ainsi d\'autres calculs.

## Utilisation

Pour créer un poids, sélectionnez la géométrie du poids (voir ci-dessous) et invoquez **Weights → Create a new ship weight**.

Le panneau des tâches s\'affiche, où vous devez sélectionner l\'instance du bateau (voir [Créer une coque](Ship_New/fr.md)) dans laquelle le poids doit être ajouté, ainsi que la densité/masse.

Lorsque vous appuyez sur le bouton **Accept**, une nouvelle instance de réservoir est créée dans l**\'instance de bateau** choisie.

## Niveaux d\'abstraction 

Comme nous l\'avons déjà vu, les poids peuvent être définis sur différents types de géométries, ce qui permet différents niveaux d\'abstraction. Si plusieurs de ces entités sont sélectionnées simultanément, le niveau d\'abstraction le plus bas possible est sélectionné.

### Poids solides/volumétriques 

Il s\'agit du niveau inférieur d\'abstraction, où la forme solide du poids est fournie, ce qui nécessite une connaissance détaillée de l\'élément. Si des solides sont trouvés dans la géométrie sélectionnée, c\'est ce type d\'abstraction qui sera appliqué, en écartant tout autre type de géométrie.

Les poids solides/volumétriques sont caractérisés par la densité du matériau (en kg/m^3^, ou toute autre unité compatible).

### Poids surfaces/aires 

Le niveau d\'abstraction suivant est celui des poids basés sur la surface. Ce niveau d\'abstraction peut être considéré pour les assiettes, ou en général pour tout élément de surface ayant une petite largeur.

<img alt="" src=images/Thin_Plate.png  style="width:200px;"> 
*Vue schématique d'une plaque mince*

Si la géométrie sélectionnée ne contient pas de solides mais des surfaces, c\'est ce type d\'abstraction qui sera appliqué, en éliminant les lignes et les sommets.

Les poids des surfaces sont caractérisés par leur densité surfacique (en kg/m^2^, ou toute autre unité compatible), c\'est-à-dire la densité du matériau multipliée par la largeur de l\'élément.

### Poids linéaires 

Le niveau d\'abstraction suivant est celui des poids basés sur les lignes. Ce niveau d\'abstraction peut être envisagé pour les poutres, ou en général pour tout élément dont la section transversale est petite par rapport à la dimension longitudinale.

<img alt="" src=images/Thin_Beam.png  style="width:200px;"> 
*Vue schématique d'une poutre mince*

Si aucun solide ou surface ne peut être trouvé dans la géométrie sélectionnée, mais que des arêtes/lignes sont bien présentes, c\'est ce type d\'abstraction qui sera appliqué. Les sommets sont en effet éliminés.

Les poids linéaires sont caractérisés par leur densité linéaire (en kg/m, ou toute autre unité compatible), c\'est-à-dire la densité du matériau multipliée par la surface de la section transversale.

### Poids ponctuels 

Il s\'agit du plus haut niveau d\'abstraction, dans lequel l\'ensemble du poids est représenté par un seul point (si plusieurs points sont fournis, la moyenne du point d\'application final sera calculée). Dans le cas où seuls des sommets peuvent être trouvés dans la géométrie sélectionnée, c\'est le type d\'abstraction qui sera appliqué.

Les poids ponctuels sont caractérisés par leur masse (en kg, ou toute autre unité compatible).

## Tutoriels

-   [Tutoriel Construction navale S60](FreeCAD-Ship_s60_tutorial/fr.md)
-   [Tutoriel Construction navale S60 (II)](FreeCAD-Ship_s60_tutorial_(II)/fr.md)





{{Ship_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Ship Weight/fr
