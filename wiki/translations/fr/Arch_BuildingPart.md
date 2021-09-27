---
- GuiCommand:/fr
   Name:Arch BuildingPart
   Name/fr:Arch Partie de bâtiment
   MenuLocation:Arch → Partie de bâtiment
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Version:0.18
   SeeAlso:[Arch Bâtiment](Arch_Building/fr.md), [Arch Site](Arch_Site/fr.md)
---

# Arch BuildingPart/fr

## Description

BuildingPart (Partie de bâtiment) remplace les anciens [Arch Planchers](Arch_Floor/fr.md) et [Arch Bâtiment](Arch_Building/fr.md) par une version plus performante qui peut être utilisée non seulement pour créer un étage/un niveau/des niveaux mais également pour toutes sortes de situations dans lesquelles différents objets Arch/BIM doivent être groupés. Ce groupe pourra être traité comme un seul objet ou répliqué.

## Utilisation

1.  En option, vous pouvez également sélectionner un ou plusieurs objets à inclure dans votre nouvelle pièce de construction.
2.  Appuyez sur le bouton **<img src="images/Arch_BuildingPart.svg" width=16px> [Créer un objet Partie de bâtiment...](Arch_BuildingPart/fr.md)**.

### Remarques

Les Partie de bâtiment ont un [Arch Plan de section](Arch_SectionPlane/fr.md) implicite intégré. {{Version/fr|0.19}}

Ce plan est toujours parallèle au plan de base du BuildingPart, mais vous pouvez spécifier le décalage entre eux. Ainsi, tous les outils qui fonctionnent avec un plan de coupe, tels que [Draft Vue 2D d\'une forme](Draft_Shape2DView/fr.md) et [TechDraw Vue Aarchitecturale](TechDraw_ArchView/fr.md) fonctionnent également avec Parties de bâtiment.

## Options

-   Après avoir créé un BuildingPart, vous pouvez ajouter d\'autres objets à celui-ci en les faisant glisser dans la vue en arborescence ou en utilisant l\'outil **<img src="images/Arch_Add.svg" width=16px> [Arch Ajouter](Arch_Add/fr.md)**.
-   Vous pouvez supprimer des objets d\'une BuildingPart en les faisant glisser dans l\'arborescence ou en utilisant l\'outil **<img src="images/Arch_Remove.svg" width=16px> [Arch Soustraire](Arch_Remove/fr.md)**.
-   En double-cliquant sur l\'objet BuildingPart dans la vue arborescente, le [Draft Plan de travail](Draft_SelectPlane/fr.md) sera défini sur son emplacement et le BuildingPart deviendra actif, ce qui signifie que de nouveaux objets lui seront automatiquement ajoutés. Double-cliquez à nouveau sur le BuildingPart pour le désactiver et ramener le plan de travail à sa position précédente. (dans la version 0.19, pour être disponible, cette option doit être définie sur true, dans le panneau Afficher les propriétés - Interaction - Double-clic l\'active).
-   The BuildingPart can display a mark in the 3D view with a label and level indication.
-   Lorsqu\'un élément BuildingPart est déplacé/pivoté, tous ses enfants qui ne possèdent pas de propriété {{PropertyData/fr|Move With Host}} ou qui l\'ont activé sont déplacés/pivotés ensemble.
-   Les pièces de construction peuvent être [Draft Clonées](Draft_Clone/fr.md).
-   Les pièces de construction peuvent prendre n'importe quel type d'IFC. Leur propriété **IFC Type** détermine son utilisation. Si vous la définissez sur **Building Storey**, il se comportera comme un niveau. Si vous la définissez sur **Building**, il se comporte comme un bâtiment et si vous la définissez sur **Element Assembly**, il se comporte comme un assemblage. Son icône changera pour refléter ce paramètre mais à part cela, cela n'a aucun autre impact dans FreeCAD. Toutefois, le fait d\'être exporté vers IFC sous un type ou un autre peut avoir un impact sur d\'autres applications BIM.

## Propriétés

### Data

-    {{PropertyData/fr|Height}}: La hauteur de cet objet et de ses objets enfants. Les objets enfants pourraient être par exemple des [Arch murs](Arch_Wall/fr.md). La hauteur de chaque mur doit être définie sur `0` (zéro), de sorte que la propriété hauteur (height) de BuildingPart se propage aux objets qu\'elle contient.

-    {{PropertyData/fr|LevelOffset}}: niveau du point (0,0,0) de ce niveau. Cette valeur est ajoutée à l\'attribut `Placement.Base.z` du BuildingPart, pour indiquer un décalage vertical sans déplacer réellement l\'objet. Le décalage résultant est affiché si {{PropertyView/fr|Show Level}} est fixé sur `True`.

-    {{PropertyData/fr|Area}}: la surface de plancher calculée de cet étage.

-    {{PropertyData/fr|IfcType}}: le type IFC de cet objet.

-    {{PropertyData/fr|Description}}: Une description facultative pour ce composant

-    {{PropertyData/fr|Tag}}: Une balise facultative pour ce composant

-    {{PropertyData/fr|IfcAttributes}}: Propriétés et attributs IFC personnalisés

### View

-    {{PropertyView/fr|LineWidth}}: la largeur de trait de cet objet.

-    {{PropertyView/fr|OverrideUnit}}: une unité facultative pour exprimer les niveaux.

-    {{PropertyView/fr|DisplayOffset}}: une transformation à appliquer au repère de niveau.

-    {{PropertyView/fr|ShowLevel}}: Si la valeur est true, affiche le niveau.

-    {{PropertyView/fr|ShowUnit}}: Si la valeur est true, affiche l\'unité sur la balise de niveau.

-    {{PropertyView/fr|SetWorkingPlane}}: Si la valeur est true, le plan de travail, lorsqu\'il est activé, s\'adaptera automatiquement à cette partie (Building Part).

-    {{PropertyView/fr|OriginOffset}}: Si la valeur est true, le décalage d\'affichage affectera également la marque d\'origine.

-    {{PropertyView/fr|ShowLabel}}: Si la valeur est true, le libellé de l\'objet est activé lorsqu\'il est activé.

-    {{PropertyView/fr|FontName}}: police à utiliser pour les textes.

-    {{PropertyView/fr|FontSize}}: La taille de la police des textes.

-    {{PropertyView/fr|RestoreView}}: Si défini, la vue stockée dans cet objet sera restaurée par un double-clic.

-    {{PropertyView/fr|DiffuseColor}}: les couleurs de visage individuelles.


{{Version/fr|0.19}}

-    {{PropertyView/fr|ChildrenOverride}}: Si cette option est définie, les paramètres ci-dessous affecteront les enfants de cette partie du bâtiment.

-    {{PropertyView/fr|ChildrenLineWidth}}: La largeur de ligne à appliquer aux enfants de cette partie du bâtiment.

-    {{PropertyView/fr|ChildrenLineColor}}: La couleur de trait à appliquer aux enfants de cette partie du bâtiment.

-    {{PropertyView/fr|ChildrenShapeColor}}: La couleur de la forme à appliquer aux enfants de cette partie du bâtiment.

-    {{PropertyView/fr|ChildrenTransparency}}: La transparence à appliquer aux enfants de cette partie du bâtiment.

## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil BuildingPart peut être utilisé à l\'intérieur d\'une [macro](macros/fr.md), et à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Crée un objet `BuildingPart` à partir de `objectslist` qui est une liste d\'objets.

Exemple : 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/fr
