---
- GuiCommand:/fr
   Name:Arch Building
   Name/fr:Arch Bâtiment
   MenuLocation:Arch → Bâtiment
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Shortcut:**B** **U**
   SeeAlso:[Arch Partie de bâtiment](Arch_BuildingPart/fr.md), [Arch Site](Arch_Site/fr.md)
---

# Arch Building/fr

## Description

Arch Building (Bâtiment) est un type spécial d\'objet de groupe FreeCAD particulièrement adapté pour représenter une unité de construction entière. Ils sont principalement utilisés pour organiser votre modèle, en contenant des objets [Arch Niveaux](Arch_Floor/fr.md).

## Utilisation

1.  Optionnellement, sélectionnez un ou plusieurs objets que vous voulez inclure dans votre nouveau bâtiment
2.  Pressez le bouton **<img src="images/Arch_Building.svg" width=16px> [Crée un objet bâtiment...](Arch_Building/fr.md)** ou appuyez sur les touches **B** puis **U**.

## Options

-   À partir de FreeCAD version 0.18, l\'objet Building est en réalité une [Arch Partie de bâtiment](Arch_BuildingPart/fr.md) (BuildingPart) avec sa propriété {{PropertyData/fr|IFC Type}} définie sur \"Building\". Vous pouvez convertir n\'importe quelle BuildingPart en un bâtiment simplement en modifiant son Type IFC.
-   Après la création du bâtiment, vous pouvez ajouter un ou plusieurs objets que vous pouvez copier/coller dans la vue arborescente ou utilisez l\'outil **<img src="images/Arch_Add.svg" width=16px> [Arch Ajouter](Arch_Add/fr.md)**.
-   Vous pouvez effacer le bâtiment que vous avez copier/coller dans la vue arborescente ou utiliser l\'outil **<img src="images/Arch_Remove.svg" width=16px> [Arch Soustraire](Arch_Remove/fr.md)**.

## Propriétés

-    {{PropertyData/fr|Building Type}}: Le type de ce bâtiment, à choisir dans une liste.

## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Bâtiment peut être utilisé à l\'intérieur d\'une [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```

-   Crée un objet `Building` à partir de `objectlist` qui est une liste d\'objets ou de `baseobj` qui est un `Shape`.

Exemple:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Building/fr
