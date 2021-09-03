---
- GuiCommand:/fr
   Name:Draft Ellipse
   Name/fr:Draft Ellipse
   MenuLocation:Drafting → Ellipse
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**E** **L**
   Version:0.7
---

## Description

La commande <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> **Draft Ellipse** crée une ellipse dans le [plan de travail](Draft_SelectPlane/fr.md) en cours à partir de deux points définissant un rectangle dans lequel l\'ellipse s\'inscrira.

Une Draft Ellipse peut être transformée en arc d\'ellipse en donnant à ses propriétés {{PropertyData/fr|First Angle}} et {{PropertyData/fr|Last Angle}} des valeurs différentes.

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;"> 
*Ellipse définie par les coins d'un rectangle*

## Utilisation

Voir aussi: [Draft La barre](Draft_Tray/fr.md), [Draft Accrochage](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Ellipse.svg" width=16px> [Créer une ellipse](Draft_Ellipse/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Drafting → <img src="images/Draft_Ellipse.svg" width=16px> Ellipse}} dans le menu.
    -   Utilisez le raccourci clavier : **E** puis **L**.
2.  Le panneau de tâches {{MenuCommand|Ellipse}} s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Choisissez le premier point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
4.  Choisissez le deuxième point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**. Ce point ne doit pas être contraint sur l\'axe X, Y ou Z.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valeurs de X, Y et Z, et appuyez sur **Entrée** après chacune, ou, vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **R** ou cliquez sur la case {{MenuCommand|Relative}} pour activer le mode relatif. Si le mode relatif est activé, les coordonnées du deuxième point sont relatives au premier point, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case {{MenuCommand|Global}} pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **L** ou cliquez sur la case {{MenuCommand|Rempli}} pour activer le mode de remplissage. Si le mode rempli est activé, l\'ellipse créée aura la valeur {{PropertyData/fr|Make Face}} `True` et aura un face remplie.
-   Appuyez sur **T** ou cliquez sur la case {{MenuCommand|Continuer}} pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir terminé, ce qui vous permet de continuer à créer des ellipses.
-   Appuyez sur **S** pour activer ou désactiver [Draft Accrochage](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour interrompre la commande.

## Remarques

-   Une Draft Ellipse peut être éditée avec la commande [Draft Editer](Draft_Edit/fr.md).

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées : {{MenuCommand|Édition → Préférences... → Général → Unités → Système d'unités → Nombre de décimales}}.
-   Pour modifier la valeur initiale du mode rempli : {{MenuCommand|Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Remplir les objets avec des faces si possible}}. La modification du mode de remplissage dans un panneau de tâches annule cette préférence pour la session FreeCAD en cours.
-   Si l\'option {{MenuCommand|Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Utiliser les primitives de Part si possible}} est cochée, la commande créera une [Part Ellipse](Part_Ellipse/fr.md) au lieu d\'une Draft Ellipse.

## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Ellipse est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Draft}}

-    {{PropertyData/fr|Area|Area}}: (en lecture seule) spécifie la surface de la face de l\'ellipse. La valeur sera {{value|0.0}} si {{PropertyData/fr|Make Face}} est `False` ou si la face ne peut être créée.

-    {{PropertyData/fr|First Angle|Angle}}: spécifie l\'angle du premier point de l\'ellipse, normalement {{value|0&#176;}}.

-    {{PropertyData/fr|Last Angle|Angle}}: spécifie l\'angle du dernier point de l\'ellipse, normalement {{value|0&#176;}}.

-    {{PropertyData/fr|Major Radius|Length}}: indique le rayon principal de l\'ellipse.

-    {{PropertyData/fr|Make Face|Bool}}: spécifie si l\'ellipse forme une face ou non. Si c\'est `True`, une face est créée, sinon seul le périmètre est considéré comme faisant partie de l\'objet. Cette propriété ne fonctionne que si la forme est une ellipse complète.

-    {{PropertyData/fr|Minor Radius|Length}}: spécifie le rayon mineur de l\'ellipse.

### Vue


{{TitleProperty|Draft}}

-    {{PropertyView/fr|Pattern|Enumeration}}: spécifie un [Draft Motif](Draft_Pattern/fr.md). avec lequel remplir la face de l\'ellipse. Cette propriété ne fonctionne que si {{PropertyData/fr|Make Face}} est `True` et si {{PropertyView/fr|Display Mode}} est {{value|Flat Lines}}.

-    {{PropertyView/fr|Pattern Size|Float}}: spécifie la taille du [Draft Motif](Draft_Pattern/fr.md).

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer une Draft Ellipse, utilisez la méthode `make_ellipse` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeEllipse`.


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```

-   Crée un objet `ellipse` avec un grand rayon donné (`majradius`) et un petit (`minradius`) en millimètres.
    -   La valeur la plus grande sera utilisée pour le grand rayon (X axis) si aucun autre placement n\'est indiqué.
-   Si `placement` est `None`, l\'ellipse sera créée à l\'origine.
-   Si `face` est `True`, l\'ellipse fera une surface c\'est-à-dire rempli.

Exemple:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```





 
