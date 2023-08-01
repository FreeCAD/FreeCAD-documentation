---
- GuiCommand:
   Name: Arch Remove
   Name/fr: Arch Soustraire
   MenuLocation: Arch - Enlever un composant
   Workbenches: [Arch](Arch_Workbench/fr.md)
   SeeAlso: [Arch Couper selon une ligne](Arch_CutLine.md), [Arch Couper selon un plan](Arch_CutPlane.md), [Arch Ajouter](Arch_Add/fr.md)
---

# Arch Remove/fr

## Description

Les outils de suppression vous permettent d\'effectuer 2 types d\'opérations :

-   Supprimer un sous-composant d\'un objet Arch, par exemple supprimer une boîte qui a été ajoutée à un mur avec **<img src="images/Arch_Add.svg" width=16px> [Arch Ajouter](Arch_Add/fr.md)**.
-   Soustraire un objet issu de l\'[Atelier Part](Part_Workbench/fr.md) d\'un composant Arch tel qu\'un **<img src="images/Arch_Wall.svg" width=16px> [Arch Mur](Arch_Wall/fr.md)** ou **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**.

La contrepartie de cet outil est l\'outil **<img src="images/Arch_Add.svg" width=16px> [Arch Ajouter](Arch_Add/fr.md)
**

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;"> 
*Une boîte soustraite d'un mur, laissant un trou dedans.*



## Utilisation

1.  Sélectionnez un sous-composant dans un objet Arch.
2.  Appuyez sur le bouton **<img src="images/Arch_Remove.svg" width=16px>** ou **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Enlever un composant](Arch_Remove/fr.md)** dans le menu supérieur.

Ou

1.  Sélectionnez les objets à soustraire, le dernier objet sélectionné doit être l'objet Arch auquel les autres objets seront soustraits.
2.  Appuyez sur le bouton **<img src="images/Arch_Remove.svg" width=16px>** ou **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Enlever un composant](Arch_Remove/fr.md)** dans le menu supérieur.

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [FreeCAD Scripts de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Soustraire peut être utilisé dans [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante: 
```python
removeComponents(objectsList, host=None)
```

-   Supprime les objets donnés dans `objectsList` de leurs parents.
-   Si un objet `host` est spécifié, cette fonction essaiera d\'ajouter les objets dans `objectsList` en tant que trous de l\'élément `host`.

Exemple : 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Remove/fr
