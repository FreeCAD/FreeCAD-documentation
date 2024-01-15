---
 GuiCommand:
   Name: Arch Space
   Name/fr: Arch Espace
   MenuLocation: Arch , Espace
   Workbenches: Arch_Workbench/fr
   Shortcut: **S** **P**
   Version: 0.14
   SeeAlso: Arch_Wall/fr, Arch_Structure/fr
---

# Arch Space/fr

## Description

L\'outil Espace vous permet de définir un volume vide, soit en le basant sur une forme solide, soit en définissant ses limites, soit en combinant les deux. S\'il est basé uniquement sur des limites, le volume est calculé en partant du cadre de sélection de toutes les limites données et en soustrayant les espaces situés derrière chaque limite. L\'objet Espace définit toujours un volume solide. La surface de plancher d\'un objet d\'espace, calculée en coupant un plan horizontal au centre de gravité du volume d\'espace, peut également être affichée.

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;">



*L'objet Espace créé à partir d'un objet solide existant, deux faces de mur sont ajoutées en tant que limites.*



## Utilisation

1.  Sélectionnez un objet solide existant ou des faces sur des objets de contour.
2.  Lancez la commande Arch Espace en utilisant plusieurs méthodes:
    -   En appuyant sur le bouton **<img src="images/Arch_Space.svg" width=16px> [Espace](Arch_Space/fr.md)** dans la barre d\'outils.
    -   En utilisant les touches **S** puis **P**
    -   En utilisant l\'entrée **Arch → Espace** du menu supérieur



### Limitations

-   Les propriétés des bords ne sont actuellement pas modifiables via l\'interface graphique.
-   Voir sur le forum [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275).



## Propriétés

-    **Base**: objet de base, le cas échéant (doit être un solide)

-    **Boundaries**: liste d\'éléments de limite facultatifs.

-    **Area**: surface de plancher calculée de cet espace.

-    **FinishFloor**: finition du sol de cet espace.

-    **FinishWalls**: finition des murs de cet espace.

-    **FinishCeiling**: finition du plafond de cet espace.

-    **Group**: objets inclus dans cet espace, tels que des meubles.

-    **SpaceType**: type de cet espace.

-    **FloorThickness**: épaisseur de la finition du sol.

-    **NumberOfPeople**: nombre de personnes qui occupent généralement cet espace.

-    **LightingPower**: puissance électrique nécessaire pour éclairer cet espace en watts.

-    **EquipmentPower**: puissance électrique nécessaire à l\'équipement de cet espace en watts.

-    **AutoPower**: si True, la puissance de l\'équipement sera automatiquement renseignée par l\'équipement inclus dans cet espace.

-    **Conditioning**: type de climatisation de cet espace.

-    **Internal**: spécifie si cet espace est interne ou externe.

-    **Text**: texte à afficher. Utilisez \$area, \$label, \$tag, \$floor, \$walls, \$ceiling pour insérer les données respectives.

-    **FontName**: nom de la police.

-    **TextColor**: couleur du texte.

-    **FontSize**: taille du texte.

-    **FirstLine**: taille de la première ligne de texte (multiplie la taille de la police. 1 = même taille, 2 = double taille, etc\...)

-    **LineSpacing**: espace entre les lignes de texte.

-    **TextPosition**: position du texte. Laisser à (0,0,0) pour la position automatique.

-    **TextAlign**: justification du texte.

-    **Decimals**: nombre de décimales à utiliser pour les textes calculés.

-    **ShowUnit**: affiche le suffixe de l\'unité ou non.

## Options

-   Pour créer des zones regroupant plusieurs espaces, utilisez [Arch Partie de bâtiment](Arch_BuildingPart/fr.md) et définir son type IFC sur \"Spatial Zone\".
-   L\'objet Espace a les mêmes modes d\'affichage que les autres objets d\'Arch et Part, avec un mode en plus appelé **Footprint** qui n\'affiche que la face inférieure de l\'espace.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Espace peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante :


```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```

-   Crée un objet `Space` à partir de `objects` donné ou `baseobj` qui peut être :
    -   un objet de document, auquel cas il devient la forme de base de l\'objet Espace, ou
    -   une liste d\'objets de sélection renvoyés par `FreeCADGui.Selection.getSelectionEx()`, ou
    -   une liste de tuples `(objet,subobjectname)`

Exemple :


```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```

Après avoir créé un objet Espace, les faces sélectionnées peuvent être ajoutées avec le code suivant :


```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```

Les limites peuvent également être supprimées, à nouveau en sélectionnant les faces indiquées :


```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Space/fr
