---
- GuiCommand:/fr
   Name:Part Sphere
   Name/fr:Part Sphère
   MenuLocation:Pièce → Primitives → Sphère
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

# Part Sphere/fr

## Description

Crée une sphère paramétrique simple avec des paramètres de position angle1, angle2, angle3 et rayon.

<img alt="" src=images/SimpleSphere.jpg  style="width:400px;">

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Atelier PArt](Part_Workbench/fr.md)
2.  Lancez la commande de plusieurs manières:
    -   Appuyez sur le bouton **<img src="images/Part_Sphere.svg" width=16px> Sphère** dans la barre d\'outils.
    -   Sélectionnez **Pièce → Primitives → <img src="images/Part_Sphere.svg" width=16px> Sphère** dans la barre de menus.

**Résultat:** la sphère sera positionnée à l\'origine (point 0,0,0) à la création. Les paramètres d\'angle permettent de faire une partie de sphère au lieu d\'une sphère entière (ils sont réglés à 360° par défaut).

Les propriétés de l\'objet peuvent être modifiées, soit dans l\'[Éditeur de propriétés](Property_editor/fr.md), soit en double-cliquant sur l\'objet dans la [Vue en arborescence](Tree_view/fr.md).

## Propriétés

### Données


{{TitleProperty|Sphere}}

-    **Radius:**rayon de la sphère

-    **Angle 1:**1er angle pour couper/définir la sphère

-    **Angle 2:**2ème angle pour couper/définir la sphère

-    **Angle 3:**3ème angle pour couper/définir la sphère

Comme il est assez difficile d'expliquer la signification des paramètres angle 1, angle 2, angle 3, l'illustration ci-dessous explique ces paramètres avec les valeurs suivantes: angle 1 = -45 °, angle 2 = 45 ° et angle 3 = 90 °.

<img alt="" src=images/SphereCutThreeAngles.jpg  style="width:400px;">

## Script

Une Part Sphère peut être créée en utilisant la fonction suivante:


```python
sphere = FreeCAD.ActiveDocument.addObject("Part::Sphere", "mySphere")
```

-   Où {{Incode|"mySphere"}} est le nom de l\'objet.
-   La fonction restitue l\'objet nouvellement créé.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sphere/fr
