---
- GuiCommand:/fr
   Name:Part Torus
   Name/fr:Part Tore
   MenuLocation:Pièce → Primitives → Tore
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

# Part Torus/fr

## Description

Crée un tore paramétrique simple avec les paramètres position angle1, angle2, angle3, rayon1 et rayon2.

<img alt="" src=images/SimpleTorus.jpg  style="width:400px;">

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Atelier PArt](Part_Workbench/fr.md)
2.  Lancez la commande de plusieurs manières:
    -   Appuyez sur le bouton **<img src="images/Part_Torus.svg" width=16px> Tore** dans la barre d\'outils.
    -   Sélectionnez **Pièce → Primitives → <img src="images/Part_Torus.svg" width=16px> Tore** dans la barre de menus.

**Résultat:** Le tore sera positionné à l\'origine (point 0,0,0) lors de la création.
Les paramètres d\'angle (angle1, angle2, angle3) ainsi que les paramètres de paramètre de rayon (radius1, radius2) permettent de paramétrer le tore, voir section suivante.

## Option

![](images/TorusExampleOverviewParameters.jpg )

**Paramètres**

Un tore peut être assimilé à un petit disque qui forme une orbite circulaire autour d\'un axe imaginaire. Ainsi, le tore paramétrique est défini par les paramètres suivants:

-    {{Parameter|Radius1:}}Rayon du cercle autour duquel le disque circule

-    {{Parameter|Radius2:}}Rayon du disque définissant la forme du tore

-    {{Parameter|Angle1:}}1er angle pour couper/définir le disque du tore

-    {{Parameter|Angle2:}}2ème angle pour couper/définir le disque du tore

-    {{Parameter|Angle3:}}3ème angle pour définir la circonférence du tore.

ainsi que l\'ensemble standard de paramètres de placement. Les images ci-dessous donnent un aperçu visuel des paramètres mentionnés précédemment:

![](images/TorusExampleRadius1.jpg ) Le paramètre Rayon1 a une valeur de 20 mm.

![](images/TorusExampleRadius2.jpg ) Le paramètre Rayon2 a une valeur de 2 mm.

![](images/TorusExampleAngle1.jpg ) Le paramètre Angle1 a une valeur de -90°. Notez que l\'outil \"Mesure d\'angle\" ne peut pas afficher un angle négatif. Considérez la valeur affichée dans l\'image comme \"-90°\".

![](images/TorusExampleAngle2.jpg ) Le paramètre Angle2 a une valeur de 90°.

![](images/TorusExampleAngle3.jpg ) Le paramètre Angle3 a une valeur de 90°. 

## Script

Un Part Tore peut être créé en utilisant la fonction suivante:


```python
torus = FreeCAD.ActiveDocument.addObject("Part::Torus", "myTorus")
```

-   Où {{Incode|"myTorus"}} est le nom de l\'objet.
-   La fonction restitue l\'objet nouvellement créé.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Torus/fr
