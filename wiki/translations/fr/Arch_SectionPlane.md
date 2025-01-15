---
 GuiCommand:
   Name: Arch SectionPlane
   Name/fr: Arch Plan de coupe
   MenuLocation: Annotation , Plan de coupe
   Workbenches: BIM_Workbench/fr
   Shortcut: **S** **P**
   SeeAlso: Draft_Shape2DView/fr
---

# Arch SectionPlane/fr

## Description

L\'outil **Arch Plan de coupe** place dans le document courant une \"chose\" qui définit un plan de coupe ou de vue. La \"chose\" est placée en fonction du [Draft Plan de travail](Draft_SelectPlane/fr.md) en cours et peut être déplacée et réorientée en la déplaçant et en la faisant tourner, jusqu\'à ce qu\'elle décrive la vue 2D que vous souhaitez obtenir. L\'objet Plan de coupe ne tiendra compte que d\'un certain ensemble d\'objets. Les objets sélectionnés lorsque vous créez un plan de coupe seront automatiquement ajoutés à cet ensemble. D\'autres objets peuvent être ajoutés ou retirés ultérieurement d\'un objet Plan de coupe à l\'aide des outils [Arch Ajouter](Arch_Add/fr.md) et [Arch Supprimer](Arch_Remove/fr.md) ou en double-cliquant sur le Plan de coupe dans l\'arborescence.

Le Plan de coupe seul ne permet pas de créer une vue de son ensemble d\'objets. Pour cela, vous devez créer une [TechDraw Vue d\'un objet Arch](TechDraw_ArchView/fr.md) pour créer une vue dans une [TechDraw page](TechDraw_Workbench/fr.md).

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">



## Utilisation

1.  Activez le [Draft Plan de travail](Draft_SelectPlane/fr.md) pour représenter le plan que vous voulez placer dans le plan de coupe.
2.  Sélectionnez l\'objet ou les objets à inclure dans le plan.
3.  Appuyez sur le bouton **<img src="images/Arch_SectionPlane.svg" width=16px> [Plan de coupe](Arch_SectionPlane/fr.md)** ou pressez les touches **S** puis **P**.
4.  Utilisez les touches [Draft Déplacer](Draft_Move/fr.md)/[Draft Pivoter](Draft_Rotate/fr.md) pour placer le plan dans sa position correcte.
5.  Sélectionnez le plan s\'il n\'est pas sélectionné.
6.  Utilisez les fonctions [Draft Vue 2D d\'une forme](Draft_Shape2DView/fr.md) ou [TechDraw Vue d\'un objet Arch](TechDraw_ArchView/fr.md) pour créer une vue.

## Options

-   L\'objet Plan de coupe ne prendra qu\'un certain nombre d\'objets, pas tous les objets du document. Des objets peuvent être ajoutés ou supprimés à partir d\'un objet Plan de coupe en utilisant les outils [Arch Ajouter](Arch_Add/fr.md) et [Arch Supprimer](Arch_Remove/fr.md) ou en double-cliquant sur le Plan de coupe dans la vue en arborescence, en sélectionnant des objets dans la liste ou dans la vue 3D puis en appuyant sur les boutons **Ajouter** ou **Supprimer**.

-   Après avoir sélectionné un plan de coupe, utilisez l\'outil de [Draft Vue 2D d\'une forme](Draft_Shape2DView/fr.md) pour créer un objet shape qui représente l\'affichage du plan de coupe dans le document.

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">

-   Créer une [TechDraw Vue d\'un objet Arch](TechDraw_ArchView/fr.md).

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   Le Plan de coupe peut également être utilisé pour afficher toute la vue 3D coupée par un plan infini. Ceci est seulement visuel, et n\'affectera pas la géométrie des objets coupés.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">



## Propriétés

-    **Only Solids**: si activé, les objets non solides compris dans l\'ensemble ne seront pas pris en charge

-    **Display Length**: donne la longueur du plan de coupe dans la vue 3D. N\'affecte pas le résultat de la vue résultante.

-    **Display Height**: donne la hauteur du plan de coupe dans la vue 3D. N\'affecte pas le résultat de la vue résultante.

-    **Arrow Size**: donne la dimension des flèches du plan de coupe dans la vue 3D. N\'affecte pas le résultat de la vue résultante.

-    **Cut View**: si `True`, toute la vue 3D sera coupée à l\'emplacement du plan de coupe.

-    **Clip view**: si `True`, il coupera la vue à la hauteur et à la longueur de l\'affichage du plan de coupe. Cela transforme effectivement le plan de coupe en une caméra orthographique, limitant le champ de vision.

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*Plan de coupe avec l'option clip view se comportera comme une caméra, en limitant le champ de vision.*



## Ajustements

-   En ajoutant manuellement une propriété nommée **RotateSolidRender** de type **App::PropertyAngle** aux propriétés **View** du plan de coupe (cliquez avec le bouton droit sur la vue des propriétés -\> tout afficher, clic droit de nouveau -\> ajouter une propriété), cela permet de faire pivoter le rendu lors de l\'utilisation du mode Solide. Ceci est utile lorsqu\'une vue comporte, par exemple, des éléments Arch et Draft, et que le rendu des éléments Arch pivote par rapport aux éléments Draft.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Plan de coupe peut servir dans une [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante :


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



---
⏵ [documentation index](../README.md) > Arch SectionPlane/fr
