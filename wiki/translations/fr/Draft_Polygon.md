---
- GuiCommand   */fr
   Name   *Draft Polygon
   Name/fr   *Draft Polygone
   MenuLocation   *Draft → Polygone
   Workbenches   *[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut   ***P** **G**
   Version   *0.7
---

# Draft Polygon/fr

## Description

La commande <img alt="" src=images/Draft_Polygon.svg  style="width   *24px;"> **Draft Polygone** crée un polygone régulier dans le [plan de travail](Draft_SelectPlane/fr.md) en cours à partir d\'un centre et d\'un rayon. Le rayon peut être défini en choisissant un point.

Un Draft Polygone peut passer du mode inscrit au mode circonscrit en modifiant sa propriété **Draw Mode**. Les coins d\'un Draft Polygone peuvent recevoir un congé (arrondis) ou chanfreinés en modifiant respectivement **Fillet Radius** ou **Chamfer Size**.

<img alt="" src=images/Draft_polygon_example.jpg  style="width   *400px;"> 
*Polygone régulier défini par deux points, le centre et le rayon*

## Utilisation

Voir aussi    * [Draft La barre](Draft_Tray/fr.md), [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons de lancer la commande    *
    -   Appuyez sur le **<img src="images/Draft_Polygon.svg" width=16px> [Polygone](Draft_Polygon/fr.md)**.
    -   Sélectionnez l\'option **Draft → <img src="images/Draft_Polygon.svg" width=16px> Polygone** dans le menu.
    -   Utilisez le raccourci clavier    * **P** puis **G**.
2.  Le panneau de tâches **Polygone** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Réglez le nombre souhaité de **Côtés**.
4.  Choisissez le premier point, le centre du polygone, dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
5.  Choisissez le deuxième point dans la [Vue 3D](3D_view/fr.md) ou entrez un **Rayon**.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement les coordonnées du centre, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   La case à cocher **Relative**, affiché dans FreeCAD version 0.19 et antérieure, n\'a aucune utilité pour cette commande.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour basculer en mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **L** ou cliquez sur la case **Rempli** pour activer le mode de remplissage. Si le mode rempli est activé, le polygone créé aura la valeur **Make Face** `True` et aura une face remplie.
-   Appuyez sur **T** ou cliquez sur la case **Continuer** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir terminé, ce qui vous permet de continuer à créer des polygones.
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur **Échap** ou sur le bouton **Fermer** pour interrompre la commande.

## Remarques

-   Un Draft Polygone peut être édité avec la commande [Draft Editer](Draft_Edit/fr.md).

## Préférences

Voir aussi    * [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées et des rayons    * **Édition → Préférences... → Général → Unités → Système d'unités → Nombre de décimales**.
-   Pour modifier la valeur initiale du mode rempli    * **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Remplir les objets avec des faces si possible**. La modification du mode de remplissage dans un panneau de tâches annule cette préférence pour la session FreeCAD en cours.
-   Si l\'option **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Utiliser les primitives de Part si possible** est cochée, la commande créera un [Part Polygone régulier](Part_RegularPolygon/fr.md) au lieu d\'un Draft Polygone.

## Propriétés

Voir aussi    * [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Polygone est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes    *

### Données


{{TitleProperty|Draft}}

-    **Area|Area**   * (en lecture seule) spécifie la surface de la face du polygone. La valeur sera {{value|0.0}} si **Make Face** est `False`.

-    **Chamfer Size|Length**   * spécifie la longueur des chanfreins aux coins du polygone.

-    **Draw Mode|Enumeration**   * spécifie si le polygone est {{value|inscrit}} dans un cercle ou {{value|circonscrit}} autour d\'un cercle.

-    **Faces Number|Integer**   * spécifie le nombre de côtés du polygone.

-    **Fillet Radius|Length**   * spécifie le rayon des congés aux coins du polygone.

-    **Make Face|Bool**   * spécifie si le polygone forme une face ou non. Si c\'est `True`, une face est créée, sinon seul le périmètre est considéré comme faisant partie de l\'objet.

-    **Radius|Length**   * spécifie le rayon du cercle qui définit le polygone.

### Vue


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**   * spécifie un [Draft Motif](Draft_Pattern/fr.md) avec lequel remplir la face du polygone. Cette propriété ne fonctionne que si **Make Face** est `True` et si **Make Face** est à {{value|Flat Lines}}.

-    **Pattern Size|Float**   * spécifie la taille du [Draft Motif](Draft_Pattern/fr.md).

## Script

Voir aussi    * [Autogenerated API documentation](https   *//freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour créer un Draft Polygone, utilisez la méthode `make_polygon` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makePolygon`.


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```

-   Crée un objet `polygon` avec le nombre de faces spécifié (`nfaces`) basé sur un cercle de `radius` en millimètres.
-   Si `inscribed` est à `True`, le polygone est inscrit dans le cercle, sinon il sera circonscrit.
    -   L\'un des sommets du polygone sera situé sur l\'axe des X si aucun autre placement n\'est indiqué.
-   Si `placement` est `None`, le polygone est créé à l\'origine et l\'un de ses sommets se trouve sur l\'axe des X.
-   Si `face` est à `True`, le polygone aura une surface, c\'est-à-dire qu\'il apparaîtra remplie.

Exemple   * 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/fr
