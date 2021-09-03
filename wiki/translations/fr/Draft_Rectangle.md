---
- GuiCommand:/fr
   Name:Draft Rectangle
   Name/fr:Draft Rectangle
   MenuLocation:Drafting → Rectangle
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**R** **E**
   Version:0.7
---

## Description

La commande <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> **Draft Rectangle** crée un rectangle dans le [plan de travail](Draft_SelectPlane/fr.md) en cours à partir de deux points.

Vous pouvez éventuellement ajouter un chanfrein ou un congé circulaire à 45 degrés à chaque coin du rectangle et le diviser en une série de lignes et de colonnes de même taille.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;"> 
*Rectangle défini par deux points*

## Utilisation

Voir aussi: [Draft La barre](Draft_Tray/fr.md), [Draft Accrochage](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Rectangle.svg" width=16px> [Créer un rectangle...](Draft_Rectangle/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Drafting → <img src="images/Draft_Rectangle.svg" width=16px> Rectangle}} dans le menu.
    -   Utilisez le raccourci clavier : **R** puis **E**.
2.  Le panneau de tâches {{MenuCommand|Rectangle}} s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Choisissez le premier point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
4.  Choisissez le deuxième point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**. Ce point ne doit pas être contraint sur l\'axe X, Y ou Z.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **R** ou cliquez sur la case {{MenuCommand|Relative}} pour activer le mode relatif. Si le mode relatif est activé, les coordonnées du deuxième point sont relatives au premier point, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case {{MenuCommand|Global}} pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **L** ou cliquez sur la case {{MenuCommand|Rempli}} pour activer le mode de remplissage. Si le mode rempli est activé, le rectangle créé aura la valeur {{PropertyData/fr|Make Face}} `True` et aura une face remplie.
-   Appuyez sur **T** ou cliquez sur la case {{MenuCommand|Continue}} pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir terminé, ce qui vous permet de continuer à créer des rectangles.
-   Appuyez sur **S** pour activer ou désactiver [Draft Accrochage](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour interrompre la commande.

## Remarques

-   Un Draft Rectangle peut être édité avec la commande [Draft Editer](Draft_Edit/fr.md).

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées : {{MenuCommand|Édition → Préférences... → Général → Unités → Système d'unités → Nombre de décimales}}.
-   Pour modifier la valeur initiale du mode rempli : {{MenuCommand|Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Remplir les objets avec des faces si possible}}. La modification du mode de remplissage dans un panneau de tâches annule cette préférence pour la session FreeCAD en cours.
-   Si l\'option {{MenuCommand|Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Utiliser les primitives de Part si possible}} est cochée, la commande créera un [Part Plan](Part_Plane/fr.md) au lieu d\'un Draft Rectangle.

## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Rectangle est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Draft}}

-    {{PropertyData/fr|Area|Area}}: (en lecture seule) spécifie la surface de la face du rectangle. La valeur sera {{value|0.0}} si {{PropertyData/fr|Make Face}} est `False`.

-    {{PropertyData/fr|Chamfer Size|Length}}: spécifie la longueur des chanfreins aux coins du rectangle.

-    {{PropertyData/fr|Columns|Integer}}: indique le nombre de colonnes de taille égale dans lesquelles le rectangle est divisé.

-    {{PropertyData/fr|Fillet Radius|Length}}: spécifie le rayon des congés aux coins du rectangle.

-    {{PropertyData/fr|Height|Distance}}: spécifie la hauteur du rectangle.

-    {{PropertyData/fr|Length|Distance}}: spécifie la longueur du rectangle.

-    {{PropertyData/fr|Make Face|Bool}}: spécifie si le rectangle forme un visage ou non. Si c\'est `True`, une face est créée, sinon seul le périmètre est considéré comme faisant partie de l\'objet.

-    {{PropertyData/fr|Rows|Integer}}: spécifie le nombre de lignes de taille égale dans lesquelles le rectangle est divisé.

### Vue


{{TitleProperty|Draft}}

-    {{PropertyView/fr|Pattern|Enumeration}}: spécifie le [Draft Motif](Draft_Pattern/fr.md) avec lequel remplir la face du rectangle. Cette propriété ne fonctionne que si {{PropertyData/fr|Make Face}} est `True` et si {{PropertyView/fr|Display Mode}} est {{value|Flat Lines}}.

-    {{PropertyView/fr|Pattern Size|Float}}: spécifie la taille du [Draft Motif](Draft_Pattern/fr.md).

-    {{PropertyView/fr|Texture Image|File}}: spécifie le chemin d\'accès au fichier image qui doit être mappé sur la face du rectangle. Si vous videz cette propriété, l\'image sera supprimée. Le rectangle doit avoir les mêmes proportions que l\'image pour éviter les distorsions.

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer un Draft Rectangle, utilisez la méthode `make_rectangle` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeRectangle`.


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```

-   Crée un objet `rectangle` avec `length` dans la direction X et `height` dans la direction Y, avec des unités en millimètres.
-   Si `placement` est `None`, le rectangle est créé à l\'origine et la longueur sera parallèle à l\'axe X.
-   Si `face` est `True`, le rectangle fera une face, c\'est-à-dire qu\'il apparaîtra rempli.

Exemple: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle1 = Draft.make_rectangle(4000, 1000)
rectangle2 = Draft.make_rectangle(1000, 4000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 45))

rectangle3 = Draft.make_rectangle(3500, 250, placement=place3)

doc.recompute()
```





 
