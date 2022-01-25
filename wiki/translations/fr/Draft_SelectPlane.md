---
- GuiCommand:/fr
   Name:Draft SelectPlane
   Name/fr:Draft Plan de travail
   MenuLocation:Utilitaires → Plan de travail
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**W** **P**
   SeeAlso:[Draft Objet Proxy pour plan de travail](Draft_WorkingPlaneProxy/fr.md)
---

# Draft SelectPlane/fr

## Description

La commande <img alt="" src=images/Draft_SelectPlane.svg  style="width:24px;"> **Draft Sélectionner un plan** sélectionne le plan de travail Draft en cours. Il s\'agit du plan dans la [vue 3D](3D_view/fr.md) où les nouveaux objets [Draft](Draft_Workbench/fr.md) sont créés. Un nouveau plan de travail peut être basé sur l\'une des nombreuses [présélections](#Utilisation_avec_les_pr.C3.A9s.C3.A9lections.md) ou sur une sélection. La sélection peut être créée avant ([présélection](#Utilisation_avec_pr.C3.A9s.C3.A9lection.md)) ou après ([post-sélection](#Utilisation_avec_post-s.C3.A9lection.md)) le lancement de la commande.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Formes créées sur différents plans de travail*

## Utilisation avec présélection 

1.  Faites l\'une des choses suivantes :
    -   Sélectionnez un seul objet. Les objets suivants sont pris en charge :
        -   [Draft Proxy pour plan de travail](Draft_WorkingPlaneProxy/fr.md) : la {{PropertyView/fr|View Data}} (position de la caméra) et la {{PropertyView/fr|Visibility Map}} (la visibilité enregistrée des objets) du proxy plan de travail sont également restaurées.
        -   [Arch Partie de bâtiment](Arch_BuildingPart/fr.md).
        -   [Arch Plan de section](Arch_SectionPlane/fr.md).
        -   Les objets [Std Parts](Std_Part/fr.md) : pour éviter de sélectionner des sous-éléments, il est conseillé de les sélectionner dans la [Vue en arborescence](Tree_view/fr.md).
        -   Les objets [Part Feature](Part_Feature/fr.md) qui ont une seule face. Les [Part Plans](Part_Plane/fr.md) par exemple.
        -   Les objets qui ne sont pas des objets [Part Feature](Part_Feature/fr.md) et qui ont une propriété {{PropertyData/fr|Placement}}.
    -   Sélectionnez un ou plusieurs sous-éléments. Vous pouvez sélectionner :
        -   Une face plane.
        -   Trois sommets.
        -   Une arête circulaire.
        -   Deux arêtes droites qui sont coplanaires mais pas colinéaires.
        -   Une arête droite et un sommet qui ne se trouve pas sur l\'arête (étendue).
2.  Il existe plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft Plan de travail](Draft_SelectPlane/fr.md)** de [Draft La barre](Draft_Tray/fr.md). En fonction du plan de travail actuel, ce bouton peut avoir un aspect différent.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SelectPlane.svg" width=16px> Sélectionnez un plan** dans le menu.
    -   Utilisez le raccourci clavier : **W** puis **P**.
3.  Le plan de travail et le bouton de [Draft La barre](Draft_Tray/fr.md) sont mis à jour.

## Utilisation avec post-sélection 

1.  Il y a plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft Plan de travail](Draft_SelectPlane/fr.md)** de [Draft La barre](Draft_Tray/fr.md). En fonction du plan de travail actuel, ce bouton peut avoir un aspect différent.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SelectPlane.svg" width=16px> Sélectionnez le plan** dans le menu.
    -   Utilisez le raccourci clavier : **W** puis **P**.
2.  Le panneau de tâches **Préparation du plan** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Effectuez l\'une des opérations suivantes :
    -   Sélectionnez un seul objet. Voir le [paragraphe précédent](#Utilisation_avec_présélection.md) pour les objets pris en charge.
    -   Sélectionner un ou plusieurs sous-éléments. Vous pouvez sélectionner :
        -   Une face plane.
        -   Trois sommets.
4.  Cliquez n\'importe où dans la [Vue 3D](3D_view/fr.md) pour confirmer la sélection et terminer la commande.
5.  Le plan de travail et le bouton de [Draft La barre](Draft_Tray/fr.md) sont mis à jour.

## Utilisation avec les présélections 

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft Plan de travail](Draft_SelectPlane/fr.md)** de [Draft La barre](Draft_Tray/fr.md). En fonction du plan de travail actuel, ce bouton peut avoir un aspect différent.
    -   Sélectionnez l\'option **Utilitaires → <img src="images/Draft_SelectPlane.svg" width=16px> Sélectionnez le plan** dans le menu.
    -   Utilisez le raccourci clavier : **W** puis **P**.
2.  Le panneau de tâches **Préparation du plan** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Appuyez sur l\'un des boutons pour terminer la commande.
4.  Le plan de travail et le bouton de [Draft La barre](Draft_Tray/fr.md) sont mis à jour.

## Options

-   Appuyez sur le bouton **<img src="images/View-top.svg" width=16px> Haut (XY)** pour aligner le plan de travail avec le plan XY du système de coordonnées global.

-   Appuyez sur le bouton **<img src="images/View-front.svg" width=16px> Face (XZ)** pour aligner le plan de travail sur le plan XZ du système de coordonnées global.

-   Appuyez sur le bouton **<img src="images/View-right.svg" width=16px> Côté (YZ)** pour aligner le plan de travail sur le plan YZ du système de coordonnées global.

-   Appuyez sur le bouton **<img src="images/View-isometric.svg" width=16px> Aligner selon la vue** pour aligner le plan de travail sur la [Vue 3D](3D_view/fr.md) actuelle. Si la case **Centrer le plan dans la vue** n\'est pas cochée, l\'origine du plan de travail correspondra à l\'origine du système de coordonnées global, sinon elle correspondra au centre de la vue [3D](3D_view.md) actuelle.

-   Appuyez sur le bouton **<img src="images/View-axonometric.svg" width=16px> Automatique** pour aligner automatiquement le plan de travail sur la [Vue 3D](3D_view/fr.md) en cours chaque fois qu\'une commande Draft ou [Arch](Arch_Workbench/fr.md) nécessitant la saisie de points est lancée. Cela équivaut à appuyer sur le bouton **<img src="images/View-isometric.svg" width=16px> Aligner selon la vue** avant d\'utiliser la commande.

-    {{MenuCommand/fr|Décalage}}définit la distance perpendiculaire entre le plan calculé et le plan de travail réel en cours.

-   Cochez la case **Centrer le plan dans la vue** pour placer l\'origine du plan de travail au centre de la [Vue 3D](3D_view/fr.md) actuelle. Cette option n\'a vraiment de sens que si le bouton **<img src="images/View-isometric.svg" width=16px> Aligner selon la vue** est utilisé.

-   Sélectionnez un sommet dans la [Vue 3D](3D_view/fr.md) et appuyez sur le bouton **<img src="images/Draft_Move.svg" width=16px> Déplacer le plan de travail** pour déplacer le plan de travail afin que son origine corresponde à la position du sommet sélectionné.

-    **Grid spacing**définit la distance entre les lignes de la grille.

-   La valeur de **Ligne principale tous les** détermine l\'endroit où les lignes de grille principales sont dessinées. Les lignes de grille principales sont légèrement plus épaisses que les lignes de grille normales. Par exemple, si l\'espacement de la grille est de {{Value|0.5 m}} et qu\'une ligne principale est tracée toutes les {{Value|10 lignes}}, une telle ligne sera tracée tous les {{Value|5 m}}.

-   La valeur de **Extension de la grille** détermine le nombre de lignes de grille dans les directions X et Y de la grille.

-    **Rayon d'aimantation**est la distance maximale à laquelle [Draft Accrochage Grille](Draft_Snap_Grid/fr.md) détecte les intersections des lignes de la grille.

-   Appuyez sur le bouton **<img src="images/view-fullscreen.svg" width=16px> Vue centrale** pour utiliser l\'origine du plan de travail en cours comme centre de la [Vue 3D](3D_view/fr.md).

-   Appuyez sur le bouton **<img src="images/edit-undo.svg" width=16px> Précédent** pour réinitialiser le plan de travail à sa position précédente.

-   Appuyez sur **Echap** ou sur le bouton {{button|Fermez}} pour abandonner la commande.

## Remarques

-   Il peut être utile d\'aligner la [Vue 3D](3D_view/fr.md) avec le plan de travail Draft sélectionné. Par exemple, après avoir changé le plan de travail en vue de face, vous pouvez vouloir passer à la [Vue de face](Std_ViewFront/fr.md) également.
-   La grille peut être basculée avec la commande [Draft Visibilité de la grille](Draft_ToggleGrid/fr.md).
-   En double-cliquant sur [Draft Proxy pour plan de travail](Draft_WorkingPlaneProxy/fr.md) dans la [Vue en arborescence](Tree_view/fr.md), vous pouvez rapidement passer d\'un plan de travail à un autre.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Les paramètres de la grille dans le panneau des tâches ainsi que plusieurs autres paramètres de la grille sont disponibles en tant que préférences : **Edition → Préférences... → Draft → Grille et aimantation → Grille**.
-   Pour utiliser la grille, **Edition → Préférences... → Draft → Grille et aimantation → Grille → Activer la grille** doit être sélectionnée. Après avoir modifié cette préférence, vous devez redémarrer FreeCAD.
-   Le rayon d\'aimantation peut également être modifié à la volée (voir [Draft Accrochage](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)) ou en modifiant : **Outils → Editer paramètres... → BaseApp → Preferences → Mod → Draft → snapRange**.

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Si l\'[atelier Draft](Draft_Workbench/fr.md) est actif, l\'objet de l\'application FreeCAD possède une propriété `DraftWorkingPlane` qui stocke le plan de travail Draft en cours. Vous pouvez accéder à cette propriété et lui appliquer des transformations :


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui

workplane = App.DraftWorkingPlane

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()

workplane.alignToPointAndAxis(v1, v2, 17)
Gui.Snapper.toggleGrid()
Gui.Snapper.toggleGrid()
```

Il est également possible de créer des plans indépendamment du plan de travail Draft. Cela peut être utile pour les calculs et les projections :


```python
import WorkingPlane

my_plane = WorkingPlane.plane()

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()
my_plane.alignToPointAndAxis(v1, v2, 17)

projection = my_plane.projectPoint(App.Vector(10, 15, 2))
print(projection)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/fr
