---
 GuiCommand:
   Name: Arch Check
   Name/fr: Arch Vérifier
   MenuLocation: Utilitaires , Vérifier
   Workbenches: BIM_Workbench/fr
   SeeAlso: Arch_CloseHoles/fr
---

# Arch Check/fr

## Description

Cet outil vérifie que le document en cours ou les objets sélectionnés ne contiennent pas d\'objets non solides des [Atelier Part](Part_Workbench/fr.md) ou [Atelier BIM](BIM_Workbench/fr.md), lesquels pourrait poser des problèmes, étant donné que la plupart des opérations de l\'atelier BIM nécessitent des objets solides.



## Utilisation

1.  Sélectionnez l\'option **Utilitaires  → <img src="images/Arch_Check.svg" width=16px> Vérifier** du menu.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](Macros/fr.md) et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction : 
```python
list_bad = check(objectslist, includehidden=False)
```

-   Vérifie si les objets donnés dans `objectslist` ne contiennent que des solides.
-   Si `includehidden` est `True`, il inclura tous les objets cachés, sinon il les omettra de la recherche.
-   Retourne `list_bad`, une liste avec les objets qui ne sont pas dérivés d\'une `Part::Feature`, ou des composants qui ne sont pas fermés, non valides, ne contiennent pas de solides ou qui contiennent des faces qui ne font partie d\'aucun solide. Ceci est utilisé pour détecter des polylignes de [BIM](BIM_Workbench/fr.md) ou de [Draft](Draft_Workbench/fr.md) et des profils qui ne sont pas des solides.
    -   Chaque élément de `list_bad` est une autre liste `[object, message]`, où `object` est l\'élément non solide détecté, et `message` indique la raison pour laquelle il a été inclus dans cette liste.

Exemple :


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute()

Circle = Draft.makeCircle(450)
Wire = Draft.makeWire([FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(1500, 1000, 0), FreeCAD.Vector(2500, -1000, 0)])

list_bad = Arch.check([Wall1, Wall2, Circle, Wire], includehidden=True)
print(list_bad)
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Check/fr
