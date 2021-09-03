---
- GuiCommand:/fr
   Name:Part Box
   Name/fr:Part Cube
   MenuLocation:Pièce → Primitives → Cube
   Workbenches:[Atelier Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

## Description

La commande Cube de l\'[atelier Part](Part_Workbench/fr.md) insère un [parallélépipède droit](https://fr.wikipedia.org/wiki/Pav%C3%A9_droit) paramétrique dans le document actif. Par défaut, la commande insère un cube de 10x10x10 mm positionné à l\'origine avec l\'étiquette \"cube\". Ces paramètres peuvent être édités une fois que l\'objet a été ajouté.

<img alt="Cube" src=images/Part_Box.jpg  style="width:400px;">

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Atelier Part](Part_Workbench/fr.md)
2.  Lancez la commande de plusieurs manières:
    -   Appuyez sur le bouton **<img src="images/Part_Box.svg" width=16px> Créer un cube plein** dans la barre d\'outils.
    -   Sélectionnez {{MenuCommand|Pièce → Primitives → <img src="images/Part_Box.svg" width=16px> Cube}} dans la barre de menus.

**Résultat:** le résultat par défaut est une boîte dont la longueur, la largeur et la hauteur sont égales à 10 mm. Elle est attachée au plan xy global et un bord coïncide avec l\'axe z global.

Les propriétés de la boîte peuvent ensuite être modifiées, soit dans l\'éditeur de propriétés, soit en double-cliquant sur la boîte dans l\'arbre du modèle.

## Propriétés


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: Spécifie l\'orientation et la position du cube dans l\'espace 3D. Voir [Placement](Placement/fr.md). Le point de référence est le coin inférieur avant gauche du cube.

-    {{PropertyData/fr|Label}}: Étiquette donnée à l\'objet Cube. Modifiez le label en fonction de vos besoins.


{{Properties_Title|Box}}

-    {{PropertyData/fr|Length}}: Le paramètre length est la dimension de la boîte dans la direction x.

-    {{PropertyData/fr|Width}}: Le paramètre width est la dimension de la boîte dans la direction y.

-    {{PropertyData/fr|Height}}: Le paramètre height est la dimension de la boîte dans la direction z.

![Part\_Box-Properties](images/Part_Box-Properties.jpg )

## Script

La commande Box peut être utilisée dans [macro](Macros/fr.md) et à partir de la console python en utilisant la fonction suivante: 
```python
FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Où \"myBox\" est l\'étiquette de l\'objet Box.
-   Retourne l\'objet nouvellement créé de type Box.

Vous pouvez accéder aux attributs de l\'objet Box et les modifier. Par exemple, vous pouvez modifier les paramètres de longueur, largeur et hauteur. 
```python
FreeCAD.ActiveDocument.myBox.Length = 25
FreeCAD.ActiveDocument.myBox.Width = 15
FreeCAD.ActiveDocument.myBox.Height = 30
```

Vous pouvez changer son emplacement avec: 
```python
FreeCAD.ActiveDocument.myBox.Placement = FreeCAD.Placement(FreeCAD.Vector(4, 6, 3), FreeCAD.Rotation(30, 45, 10))
```





 
