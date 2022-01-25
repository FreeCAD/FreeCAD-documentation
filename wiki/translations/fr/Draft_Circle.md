---
- GuiCommand:/fr
   Name:Draft Circle
   Name/fr:Draft Cercle
   MenuLocation:Drafting → Cercle
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**C** **I**
   Version:0.7
   SeeAlso:[Draft Arc](Draft_Arc/fr.md), [Draft Arc par 3 points](Draft_Arc_3Points/fr.md)
---

# Draft Circle/fr

## Description

La commande <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> **Draft Cercle** crée un cercle dans le [Draft Plan de travail](Draft_SelectPlane/fr.md) en cours à partir d\'un centre et d\'un rayon. Le rayon peut être défini en choisissant un point.

Un Draft Cercle peut être transformé en arc de cercle en donnant à ses propriétés {{PropertyData/fr|First Angle}} et {{PropertyData/fr|Last Angle}} des valeurs différentes.

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;"> 
*Cercle défini par deux points, le centre et le rayon*

## Utilisation

Voir aussi : [Draft La barre](Draft_Tray/fr.md), [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Draft_Circle.svg" width=16px> [Créer un cercle](Draft_Circle/fr.md)**.
    -   Sélectionnez l\'option **Drafting → <img src="images/Draft_Circle.svg" width=16px> Cercle** dans le menu.
    -   Utilisez le raccourci clavier : **C** puis **I**.
2.  Le panneau de tâches **Cercle** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Choisissez le premier point, le centre du cercle dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
4.  Choisissez le deuxième point dans la [Vue 3D](3D_view/fr.md) ou entrez un **Rayon**.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement les coordonnées du centre, entrez les valeurs de X, Y et Z et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   La case à cocher **Relative**, affichée dans FreeCAD version 0.19 et antérieure, n\'a aucune utilité pour cette commande.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour basculer en mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **L** ou cliquez sur la case à cocher **Rempli** pour basculer en mode rempli. Si le mode rempli est activé, le cercle créé aura {{PropertyData/fr|Make Face}} défini sur `True` et aura une face remplie.
-   Appuyez sur **T** ou cliquez sur la case **Continuer** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir terminé, ce qui vous permet de continuer à créer des cercles.
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour interrompre la commande.

## Remarques

-   Un Draft Cercle peut être édité avec la commande [Draft Editer](Draft_Edit/fr.md).

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées et des rayons : **Édition → Préférences... → Général → Unités → Système d'unités → Nombre de décimales**.
-   Pour modifier la valeur initiale du mode rempli : **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Remplir les objets avec des faces si possible**. La modification du mode de remplissage dans un panneau de tâches annule cette préférence pour la session FreeCAD en cours.
-   Si l\'option **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Utiliser les primitives de Part si possible** est cochée, la commande créera un [Part Cercle](Part_Circle/fr.md) au lieu d\'un Draft Cercle.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Cercle est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Draft}}

-    {{PropertyData/fr|Area|Area}}: (en lecture seule) spécifie la surface de la face du cercle. La valeur sera {{value|0.0}} si {{PropertyData/fr|Make Face}} est `False` ou si la face ne peut être créée.

-    {{PropertyData/fr|First Angle|Angle}}: spécifie l\'angle de départ du cercle, normalement {{value|0&#176;}}.

-    {{PropertyData/fr|Last Angle|Angle}}: spécifie l\'angle final du cercle, normalement {{value|0&#176;}}.

-    {{PropertyData/fr|Make Face|Bool}}: spécifie si le cercle forme une face ou non. Si c\'est `True`, une face est créée, sinon seul le périmètre est considéré comme faisant partie de l\'objet. Cette propriété ne fonctionne que si les {{PropertyData/fr|First Angle}} et {{PropertyData/fr|Last Angle}} ont la même valeur. Notez que {{value|0&#176;}} et {{value|360&#176;}} ne sont pas considérés comme identiques.

-    {{PropertyData/fr|Radius|Length}}: spécifie le rayon du cercle.

### Vue


{{TitleProperty|Draft}}

-    {{PropertyView/fr|Pattern|Enumeration}}: spécifie un [Draft Motif](Draft_Pattern/fr.md). avec lequel remplir la face du cercle. Cette propriété ne fonctionne que si {{PropertyData/fr|Make Face}} est `True` et si {{PropertyView/fr|Display Mode}} est {{value|Flat Lines}}.

-    {{PropertyView/fr|Pattern Size|Float}}: spécifie la taille du [Draft Motif](Draft_Pattern/fr.md).

## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer un Draft Cercle, utilisez la méthode `make_circle` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeCircle`.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```

-   Crée un objet `circle` avec un `radius` donné en millimètres.
    -   
        `radius`
        
        peut aussi être un `Part.Edge`, dont l\'attribut `Curve` doit être un `Part.Circle`.
-   Si un `placement` est `None`, le cercle est créé à l\'origine.
-   Si `face` a la valeur `True`, le cercle fera une face, c\'est-à-dire qu\'il apparaîtra rempli.
-   Si `startangle` et `endangle` sont donnés en degrés et ont des valeurs différentes, ils sont utilisés et l\'objet apparaît comme une [Draft Arc](Draft_Arc/fr.md).

Exemple : 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/fr
