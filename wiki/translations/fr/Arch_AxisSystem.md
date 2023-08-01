---
- GuiCommand:
   Name:Arch AxisSystem
   Name/fr:Arch Système d'axes
   MenuLocation:Arch - Outils pour les axes - Système d'axes
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Axes](Arch_Axis/fr.md), [Arch Grille](Arch_Grid/fr.md)
---

# Arch AxisSystem/fr

## Description

L\'outil [Système d\'axes](Arch_AxisSystem/fr.md) vous permet de combiner 2 ou 3 objets [Arch Axes](Arch_Axis/fr.md).

Ceci est utile pour définir les points d\'intersection entre les différents axes. Les objets Arch peuvent ensuite utiliser ce système pour dupliquer leur forme sur les différents points d\'intersection.

<img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;"> 
*Trois objets [Arch Axes](Arch_Axis/fr.md) combinés en un [Système d'axes](Arch_AxisSystem/fr.md). Un objet [Arch Structure](Arch_Structure/fr.md) utilise ce système comme propriété **Axis* pour que sa forme soit dupliquée à chaque point d'intersection.**



## Utilisation

1.  En option, sélectionnez les objets [Arch Axes](Arch_Axis/fr.md) que vous souhaitez inclure dans ce système.
2.  Appuyez sur le bouton **<img src="images/Arch_AxisSystem.svg" width=16px> [Système d'axes](Arch_AxisSystem/fr.md)**.
3.  Cliquez avec le bouton droit sur l\'objet système d\'axes nouvellement créé dans l\'arborescence pour ajouter/modifier les objets [Axes](Arch_Axis/fr.md) inclus dans ce système.
4.  Sélectionnez un [Arch Axes](Arch_Axis/fr.md) existant et appuyez sur les boutons **<img src="images/Arch_Add.svg" width=16px> [Arch Ajouter](Arch_Add/fr.md)** ou **<img src="images/Arch_Remove.svg" width=16px> [Arch Soustraire](Arch_Remove/fr.md)** pour ajouter ou enlever de ce système.
5.  Définir la propriété **Axis** de n\'importe quel objet Arch pour pointer vers ce système, pour que sa forme soit dupliquée aux points d\'intersection de ce système

## Options

-   Un même objet [Arch Axes](Arch_Axis/fr.md) peut faire partie de plus d\'un système
-   Tout objet basé sur une forme peut également être utilisé comme propriété **Axis** des objets Arch. Dans ce cas, la forme de l\'objet sera dupliquée le long des sommets de l\'objet Axe



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Système d\'Axes peut être utilisé dans une [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante: 
```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```

-   Crée un objet `AxisSystem` à partir de l\'objet `axes` qui est un seul [Arch Axe](Arch_Axis/fr.md) ou une liste d\'entre eux.

Exemple: 
```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()

AxisSystem = Arch.makeAxisSystem([Axes, Axes2])

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = AxisSystem
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch AxisSystem/fr
