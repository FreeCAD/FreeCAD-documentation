---
- GuiCommand:/fr
   Name:Part Box
   Name/fr:Part Cube
   MenuLocation:Pièce → Primitives → Cube
   Workbenches:[Atelier Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

# Part Box/fr

## Description

La commande Cube de l\'[atelier Part](Part_Workbench/fr.md) insère un [parallélépipède rectangle](https://fr.wikipedia.org/wiki/Pav%C3%A9_droit) paramétrique dans le document actif. Par défaut, la commande insère un cube de 10x10x10 mm positionné à l\'origine avec l\'étiquette \"cube\". Ces paramètres peuvent être édités une fois que l\'objet a été ajouté.

<img alt="Part\_Box" src=images/Part_Box.jpg  style="width:400px;">

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Atelier Part](Part_Workbench/fr.md)
2.  Lancez la commande de plusieurs manières:
    -   Appuyez sur le bouton **<img src="images/Part_Box.svg" width=16px> Cube** dans la barre d\'outils.
    -   Sélectionnez **Pièce → Primitives → <img src="images/Part_Box.svg" width=16px> Cube** dans la barre de menus.

**Résultat:** le résultat par défaut est une boîte dont la longueur, la largeur et la hauteur sont égales à 10 mm. Elle est attachée au plan xy global et un bord coïncide avec l\'axe z global.

Les propriétés de la boîte peuvent ensuite être modifiées, soit dans l\'éditeur de propriétés, soit en double-cliquant sur la boîte dans l\'arbre du modèle.

## Propriétés


{{Properties_Title|Box}}

-    **Length**: paramètre longueur est la dimension de la boîte dans la direction x.

-    **Width**: paramètre largeur est la dimension de la boîte dans la direction y.

-    **Height**: paramètre hauteur est la dimension de la boîte dans la direction z.

## Script

Un Part Cube peut être créé en utilisant la fonction suivante:


```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Où {{Incode|"myBox"}} est le nom de l\'objet.
-   La fonction restitue l\'objet nouvellement créé.

Vous pouvez accéder aux attributs de l\'objet {{Incode|box}} et les modifier. Par exemple, vous pouvez modifier les paramètres de longueur, largeur et hauteur.


```python
box.Length = 25
box.Width = 15
box.Height = 30
```

Vous pouvez changer son emplacement avec:


```python
box.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/fr
