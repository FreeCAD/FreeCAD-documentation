---
- GuiCommand:/fr
   Name:Arch SectionPlane
   Name/fr:Arch Plan de section
   MenuLocation:Arch → Plan de section
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**S** **P**
   SeeAlso:[Draft Vue 2D d'une forme](Draft_Shape2DView/fr.md), [TechDraw Vue Arch](TechDraw_ArchView/fr.md)
---

## Description

Cet outil place dans le document courant une \"chose\" qui définit un plan de section ou de vue. La \"chose\" est placée en fonction du [Draft plan de travail](Draft_SelectPlane/fr.md) en cours et peut être déplacée et réorientée en la déplaçant et en la faisant tourner, jusqu\'à ce qu\'elle décrive la vue 2D que vous souhaitez obtenir. L\'objet Plan de section ne tiendra compte que d\'un certain ensemble d\'objets. Les objets sélectionnés lorsque vous créez un plan de coupe seront automatiquement ajoutés à cet ensemble. D\'autres objets peuvent être ajoutés ou retirés ultérieurement d\'un objet Plan de coupe à l\'aide des outils [Arch Ajouter](Arch_Add.md) et [Arch Soustraire](Arch_Remove.md) ou en double-cliquant sur le Plan de coupe dans l\'arborescence.

Le Plan de section seul ne permet pas de créer une vue de son ensemble d\'objets. Pour cela, vous devez créer une [TechDraw Vue Arch](TechDraw_ArchView/fr.md) pour créer une vue dans une [page TechDraw](TechDraw_Workbench/fr.md).

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">

## Utilisation

1.  Optionnellement activez [Draft Plan de travail](Draft_SelectPlane/fr.md) pour représenter le plan que vous voulez placer dans Section Plane.
2.  Sélectionnez l\'objet ou les objets à inclure dans le plan.
3.  Appuyez sur le bouton **<img src="images/Arch_SectionPlane.svg" width=16px> [Arch Crée un plan de coupe...](Arch_SectionPlane/fr.md)** ou pressez les touches **S** puis **P**.
4.  Utilisez les touches [Draft Déplacez](Draft_Move/fr.md)/[Draft Pivotez](Draft_Rotate/fr.md) pour placer le plan dans sa position correcte.
5.  Sélectionnez le plan s\'il n\'est pas sélectionné.
6.  Utilisez les fonctions [Drawing DraftView](Draft_Drawing/fr.md), [Draft Vue 2D d\'une forme](Draft_Shape2DView/fr.md) ou [TechDraw Vue Arch](TechDraw_ArchView/fr.md) pour créer une vue.

## Options

-   L\'objet Section Plane ne prendra qu\'un certain nombre d\'objets, pas tous les objets du document. Les objets peuvent être ajoutés ou supprimés à partir d\'un objet SectionPlane en utilisant les outils [Arch Ajouter](Arch_Add/fr.md) et [Arch Soustraire](Arch_Remove/fr.md), en double-cliquant sur le Section Plane dans la vue 3D, ou en sélectionnant des objets dans l\'arborescence de la vue combinée, puis appuyez sur les boutons **Ajouter** ou **Supprimer**.

-   Après avoir sélectionné un plan de coupe, utilisez l\'outil de [Draft Vue 2D d\'une forme](Draft_Shape2DView/fr.md) pour créer un objet shape qui représente l\'affichage du plan de coupe dans le document

<img alt="Arch Section" src=images/Arch_Section_example2.jpg  style="width:600px;">

-   Créer un nouvel objet [Draft Dessin](Draft_Drawing/fr.md) si vous travaillez avec l\'[atelier Drawing](Drawing_Workbench/fr.md), ou [TechDraw Vue Arch](TechDraw_ArchView/fr.md) si vous utilisez l\'[atelier TechDraw](TechDraw_Workbench/fr.md).

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   Le plan de coupe peut également être utilisé pour afficher toute la vue 3D coupée par un plan infini. Ceci est seulement visuel, et n\'affectera pas la géométrie des objets coupés.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">

## Propriétés

-    {{PropertyData/fr|Only Solids}}: S\'il est activé, les objets non solides comppris dans l\'ensemble ne seront pas pris en charge

-    {{PropertyView/fr|Display Length}}: Donne la longueur du Section Plane dans la vue 3D. N\'affecte pas le résultat de la vue résultante.

-    {{PropertyView/fr|Display Height}}: Donne hauteur du Section Plane dans la vue 3D. N\'affecte pas le résultat de la vue résultante.

-    {{PropertyView/fr|Arrow Size}}: Donne la dimension des flèches du Section Plane dans la vue 3D. N\'affecte pas le résultat de la vue résultante.

-    {{PropertyView/fr|Cut View}}: S\'il est activé `True`, toute la vue 3D sera coupée à l\'emplacement du Section Plane.

-    {{PropertyView/fr|Clip view}}: S\'il est activé `True`, il coupera la vue à la hauteur et à la longueur de l\'affichage du plan de coupe. Cela transforme effectivement le plan de coupe en une caméra orthographique, limitant le champ de vision.{{version/fr|0.19}}

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">


*Le plan de coupe Arch avec l'option de vue Clip se comportera comme une caméra, limitant le champ de vision de la vue.*

## Ajustements

-   Ajout manuel d\'une propriété nommée **RotateSolidRender** de type **App::PropertyAngle** aux propriétés \'\' \'View\' \'\' du plan de coupe (cliquez avec le bouton droit sur la vue des propriétés -\> tout afficher, clic droit de nouveau -\> ajouter une propriété) permet de faire pivoter le rendu lors de l\'utilisation du mode Solide. Ceci est utile lorsqu\'une vue rendue comporte, par exemple, des éléments Arch et Draft, et que le rendu des éléments Arch pivote par rapport aux éléments Draft. {{version/fr|0.19}}

## Script


**Voir aussi:**

[API](Arch_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil plan de coupe peut servir dans une [macro](macros/fr.md) et à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```

-   Crée un objet `Section` à partir de `objectlist` qui est une liste d\'objets.

Exemple :


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```









