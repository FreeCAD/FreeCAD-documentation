---
 GuiCommand:
   Name: Arch Add
   Name/fr: Arch Ajouter
   MenuLocation: Modifier , Ajouter un composant
   Workbenches: BIM_Workbench/fr
   SeeAlso: Arch_Remove/fr
---

# Arch Add/fr

## Description

L\'outil Ajouter vous permet de faire 4 types d\'opérations :

-   Ajoutez des objets basés sur [Part](Part_Workbench/fr.md) à un composant Arch, tels qu\'un **<img src="images/Arch_Wall.svg" width=16px> [Arch Mur](Arch_Wall/fr.md)** ou une **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**. Ces objets font alors partie du composant Arch et vous permettent de modifier sa forme tout en conservant ses propriétés de base telles que la largeur et la hauteur
-   Ajouter des composants Arch, tels qu\'un **<img src="images/Arch_Wall.svg" width=16px> [Arch Mur](Arch_Wall/fr.md)** ou une **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**, à un objet Arch basé sur un groupe tel que des **<img src="images/Arch_Floor.svg" width=16px> [Arch Niveaux](Arch_Floor/fr.md)**.
-   Ajoutez un **<img src="images/Arch_Axis.svg" width=16px> [Arch Système d'axes](Arch_Axis/fr.md)
** à une **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure/fr.md)**
-   Ajouter des objets à des **<img src="images/Arch_SectionPlane.svg" width=16px> [Arch Plans de coupe](Arch_SectionPlane/fr.md)
**

La contrepartie de cet outil est l\'outil **<img src="images/Arch_Remove.svg" width=16px> [Arch Supprimer](Arch_Remove/fr.md)**.

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;"> 
*Dans l'image ci-dessus, une boîte est ajoutée à un mur.*



## Utilisation

1.  Sélectionnez les objets à ajouter ensemble. Le dernier objet sélectionné sera l\'objet Arch de l\'hôte.
2.  Appuyez sur le bouton **<img src="images/Arch_Add.svg" width=16px> [Ajouter un composant](Arch_Add/fr.md)** ou utilisez **Modifier → <img src="images/Arch_Add.svg" width=16px> Ajouter un composant** du menu supérieur.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Ajouter peut être utilisé dans une [macro](Macros/fr.md) ou dans la console [Python](Python/fr.md) en utilisant la fonction :

:   
    
```python
    addComponents(objectsList, host)
    
```
    





:   L\'extrait de code ci-dessus ajoute les objets donnés dans `objectsList` à l\'objet `host` donné.
:   **Note:** `objectsList` peut être un objet unique ou une liste d\'objets.

Exemple:


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Add/fr
