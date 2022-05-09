---
- GuiCommand   */fr
   Name   *Arch CloseHoles
   Name/fr   *Arch Fermer les trous
   MenuLocation   *Arch → Utilitaires → Fermer les trous
   Workbenches   *[Arch](Arch_Workbench/fr.md)
   SeeAlso   *[Arch Vérification](Arch_Check/fr.md)
---

# Arch CloseHoles/fr

## Description

Cet outil identifie les trous (séquence circulaire d\'arêtes ouvertes (edges)) dans un objet [shape](Part_Workbench/fr.md) et tente de les fermer avec l\'ajout d\'une nouvelle face construite sur la séquence de bords. Vous devez cependant, vous assurer que le résultat est un solide.

## Utilisation

1.  Sélectionnez un objet [Shape](Part_Workbench/fr.md).
2.  Appuyez sur l\'entrée **<img src="images/Arch_CloseHoles.svg" width=16px> [Fermer les trous](Arch_CloseHoles/fr.md)** dans **Arch → Utilitaires → Fermer les trous**.

## Script


**Voir aussi   ***

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](macros/fr.md), et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction    * 
```python
solid = closeHole(shape)
```

-   Ferme un trou dans une `shape` qui est un `Part.Shape` et renvoie le nouvel objet `solid`.

Exemple   * 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part   *   *Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute() 

solid = Arch.closeHole(Wall.Shape)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CloseHoles/fr
