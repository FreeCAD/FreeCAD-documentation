---
- GuiCommand   */fr
   Name   *Arch_Rebar
   Name/fr   *Arch Armature personnalisée
   MenuLocation   *Arch → Outils pour armatures → Custom Rebar<br>3D/BIM → Armature personnalisée
   Workbenches   *[Arch](Arch_Workbench/fr.md), [BIM](BIM_Workbench/fr.md)
   Shortcut   ***R** **B**
   SeeAlso   *[Arch Structure](Arch_Structure/fr.md), [Atelier Reinforcement](Reinforcement_Workbench/fr.md)
---

# Arch Rebar/fr

## Description

L\'outil [Armature](Arch_Rebar/fr.md) vous permet de placer des [barres d\'armature](http   *//fr.wikipedia.org/wiki/Armature_%28technique%29) dans les objets [Structure](Arch_Structure/fr.md).

L\'outil [Arch Rebar](Arch_Rebar/fr.md) est également intégré dans l\'[atelier BIM](BIM_Workbench/fr.md).

Les objets Armatures sont basés sur des profils 2D comme les [esquisses](Sketcher_Workbench/fr.md) ou [les objets dessin](Draft_Workbench/fr.md), qui doivent être dessinés sur une face d\'un objet Structure. Vous pouvez ensuite ajuster la configuration de l\'armature comme le nombre et le diamètre des barres ou la distance de décalage entre les deux extrémités de l\'élément structurel.

<img alt="" src=images/Arch_Rebar_example.jpg  style="width   *400px;"> 
*L'image ci dessus montre un objet structurel, sur lequel deux esquisses sont dessinées, qui définissent le chemin des barre de fer. Ces deux esquisses sont ensuite transformées en objet Armature.*

## Extension disponible 

L\'outil Armature a été amélioré dans l\'[Atelier Barres de renfort](Reinforcement_Workbench/fr.md) et peut être installé avec le [Gestionnaire des extensions](Std_AddonMgr/fr.md). Les types de barres supplémentaires disponibles avec l\'extension sont    *

-   <img alt="" src=images/Arch_Rebar_Straight.svg  style="width   *32px;"> [Armature droite](Arch_Rebar_Straight/fr.md)
-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width   *32px;"> [Armature en U](Arch_Rebar_UShape/fr.md)
-   <img alt="" src=images/Arch_Rebar_LShape.svg  style="width   *32px;"> [Armature en L](Arch_Rebar_LShape/fr.md)
-   <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width   *32px;"> [Armature cintrée](Arch_Rebar_BentShape/fr.md)
-   <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width   *32px;"> [Armature en étrier](Arch_Rebar_Stirrup/fr.md)
-   <img alt="" src=images/Arch_Rebar_Helical.svg  style="width   *32px;"> [Armature hélicoïdale](Arch_Rebar_Helical/fr.md)

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_Arch.svg  style="width   *16px;"> [atelier Arch](Arch_Workbench/fr.md)
2.  Créez un objet **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)
**
3.  Basculez vers l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;"> [atelier Sketcher](Sketcher_Workbench/fr.md)
4.  Sélectionnez une face de l\'objet Structure
5.  Appuyez sur le bouton **<img src="images/Sketcher_NewSketch.svg" width=16px> [Sketcher Créer une nouvelle esquisse](Sketcher_NewSketch/fr.md)** pour démarrer l\'édition d\'une nouvelle esquisse sur la face choisie
6.  Dessinez la forme de l\'Armature
7.  Cliquez sur le bouton **<img src="images/Sketcher_LeaveSketch.svg" width=16px> [Sketcher Sortir de l'edition de l'esquisse](Sketcher_LeaveSketch/fr.md)** pour finir
8.  Basculez de nouveau vers l\'<img alt="" src=images/Workbench_Arch.svg  style="width   *16px;"> [atelier Arch](Arch_Workbench/fr.md)
9.  Sélectionnez l\'esquisse que vous venez de dessiner
10. Appuyez sur le bouton **<img src="images/Arch_Rebar.svg" width=16px> [Arch Armature](Arch_Rebar/fr.md)
**, ou pressez les touches **R** puis **B**
11. Ajustez les propriétés désirées (votre armature peut ne pas apparaître immédiatement, si certaines propriétés créent des situations impossibles comme un diamètre égal à 0 mm ou un décalage plus grand que la longueur de l\'objet Structure).

Bien que normalement une barre d'accès soit utilisée dans une structure en arc, depuis FreeCAD 0.19, elle peut être créée en dehors de tout objet hôte. Pour héberger une barre dans un objet, il vous suffit de définir son {{PropertyData/fr|hôte}}.

## Options

-   Armature partage les propriétés communes et les comportements de tous les [Arch Composants](Arch_Component/fr.md).
-   La valeur d\'arrondi est exprimée en multiples du diamètre. Si la barre a un diamètre de 5 mm, la valeur d\'arrondi de 3 va créer des angles arrondis d\'un rayon de 15 mm.
-   La valeur par défaut des nouvelles Armatures peut être définie dans les préférences de l\'atelier Arch.
-   Si un vecteur de direction n\'est pas spécifié, la direction et la distance le long de laquelle les barres seront répandues sont définies automatiquement sur l\'objet hôte structurel, en prenant la direction normale de l\'esquisse de base et en son intersection avec l\'objet structurel. Si vous spécifiez un vecteur de direction, la longueur de ce vecteur va également être prise en compte.
-   La valeur d\'espacement est calculée d\'après le nombre actuel des barres et représente la distance entre les axes de chaque barre. Vous devez donc soustraire le diamètre de la barre pour obtenir la taille de l\'espace libre entre les barres.

## Propriétés

-    {{PropertyData/fr|Amount}}   * La quantité de barres.

-    {{PropertyData/fr|Diameter}}   * Le diamètre des barres.

-    {{PropertyData/fr|Direction}}   * La direction (et longueur) selon laquelle la barre est répartie. Si la valeur est (0,0,0), la direction est calculée automatiquement en fonction de l\'objet Structure hôte.

-    {{PropertyData/fr|Offset Start}}   * La distance du décalage entre le bord de l\'objet Structure et la première barre.

-    {{PropertyData/fr|Offset End}}   * La distance du décalage entre le bord de l\'objet Structure et la dernière barre.

-    {{PropertyData/fr|Rounding}}   * Une valeur d\'arrondi qui s\'applique aux angles des barres, multiple du diamètre.

-    {{PropertyData/fr|Spacing}}   * L\'espacement des axes de chaque barre.

## Script


**Voir aussi    ***

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Armature peut être utilisé dans les [macros](macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant les fonctions suivantes    * 
```python
Rebar = makeRebar(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name="Rebar")
```

-   Crée un objet `Rebar` à partir d\'`objet de base` donné, qui est une [Arch Structure](Arch_Structure/fr.md), et une `sketch` comme profil.
    -   
        `diameter`
        
        , `amount` et `offset` sont utilisés pour définir les caractéristiques des barres.

    -   Si aucune valeur `diameter`, `amount` ou `offset` n\'est donnée, les valeurs par défaut des [Arch Préférences](Arch_Preferences/fr.md) sont utilisées.

Exemple    *


```python
import FreeCAD, Arch, Part

Structure = Arch.makeStructure(None, length=1000, width=1000, height=3000)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

p1 = FreeCAD.Vector(-400, 400, 0)
p2 = FreeCAD.Vector(400, 400, 0)
Sketch = FreeCAD.ActiveDocument.addObject('Sketcher   *   *SketchObject', 'Sketch')
Sketch.MapMode = "FlatFace"
Sketch.Support = [(Structure, "Face6")]
Sketch.addGeometry(Part.LineSegment(p1, p2))
FreeCAD.ActiveDocument.recompute()

Rebar = Arch.makeRebar(Structure, Sketch, diameter=80, amount=7, offset=50)
Rebar.OffsetStart = 100
Rebar.OffsetEnd = 100
FreeCAD.ActiveDocument.recompute()
```





 

[Category   *External Command Reference](Category_External_Command_Reference.md) [Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar/fr
