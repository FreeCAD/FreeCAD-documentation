---
 GuiCommand:
   Name: Draft Rotate
   Name/fr: Draft Pivoter
   MenuLocation: Draft/BIM : Modification , Pivoter
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   Shortcut: **R** **O**
   Version: 0.7
   SeeAlso: Draft_SubelementHighlight/fr
---

# Draft Rotate/fr

## Description

La commande <img alt="" src=images/Draft_Rotate.svg  style="width:24px;"> **Draft Pivoter** permet de faire pivoter ou de copier les objets sélectionnés autour d\'un point central selon un angle donné. L\'axe de rotation est perpendiculaire au [plan de travail](Draft_SelectPlane/fr.md) en cours et l\'angle de rotation est relatif à ce plan. En mode sous-élément, la commande fait pivoter les points et les bords sélectionnés, ou copie les bords sélectionnés, des [Draft Lignes](Draft_Line/fr.md) et [Draft Polylignes](Draft_Wire/fr.md).

Cette commande peut être utilisée sur des objets 2D créés avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi sur de nombreux objets 3D tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md), l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ou l\'[atelier BIM](BIM_Workbench/fr.md).

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;"> 
*Pivoter un objet autour d'un point central*



## Utilisation

Voir aussi : [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Sélectionnez un ou plusieurs objets ou un ou plusieurs sous-éléments de [Draft Lignes](Draft_Line/fr.md) ou [Draft Polylignes](Draft_Wire/fr.md).
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Rotate.svg" width=16px> [Pivoter](Draft_Rotate/fr.md)**.
    -   [Draft](Draft_Workbench/fr.md) : sélectionnez l\'option **Modification → <img src="images/Draft_Rotate.svg" width=16px> Pivoter** du menu.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Modification → <img src="images/Draft_Rotate.svg" width=16px> Pivoter** du menu.
    -   Utilisez le raccourci clavier : **R** puis **O**.
3.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet dans la [vue 3D](3D_view/fr.md).
4.  Le panneau de tâches **Pivoter** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
5.  Si des sous-éléments ont été sélectionnés : cochez la case **Modifier les sous-éléments** pour activer le mode sous-élément.
6.  Choisissez le premier point, le centre de rotation, dans la [vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrer un point**.
7.  Choisissez le deuxième point dans la [vue 3D](3D_view/fr.md) ou entrez un **Angle de base**.
8.  Choisissez le troisième point dans la [vue 3D](3D_view/fr.md) ou entrez une **Rotation**.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut (pour la version 1.0).

-   Pour saisir manuellement les coordonnées du centre de rotation, entrez les valeurs X, Y et Z,et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrer un point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour basculer en mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md).
-   Appuyez sur **N** ou cliquez sur la case **Continuer** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir été terminée. Ce mode n\'a vraiment de sens que si le mode copie est activé. En fonction de la préférence **Sélectionner les objets de base après la copie**, soit les objets originaux sont sélectionnés pour le prochain appel de la commande, soit les copies créées en dernier. Voir [Préférences](#Préférences.md).
-   Appuyez sur **C** ou cliquez sur la case **Copier** pour activer le mode copie. Si le mode de copie est activé, la commande créera des copies pivotées au lieu de faire pivoter les objets originaux.
-   Appuyez sur **B** ou cliquez sur la case **Modifier les sous-éléments** pour basculer en mode sous-éléments. Si le mode sous-élément est activé, la commande utilisera les sous-éléments sélectionnés au lieu des objets entiers. Les sous-éléments doivent appartenir à des [Draft Lignes](Draft_Line/fr.md) ou des [Draft Polylignes](Draft_Wire/fr.md).
-   Si le mode copier et le mode sous-éléments sont tous deux activés, et que les bords des [Draft Polylignes](Draft_Wire/fr.md) sont sélectionnés, de nouvelles polylignes seront créées à partir de ces bords.
-   Si vous maintenez la touche **Alt** enfoncée après avoir saisi la **Angle de base**, le mode copier sera également activé. Lorsque vous maintenez la touche {KEY\|Alt} enfoncée, vous pouvez sélectionner plusieurs points pour la **Rotation**. Relâchez **Alt** pour terminer la commande et voir les copies créées.
-   Appuyez sur **S** pour activer ou désactiver l\'[Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur **Échap** ou sur le bouton **Fermer** pour interrompre la commande.



## Remarques

-   Un objet [accroché](Part_EditAttachment/fr.md) ne peut pas être pivoté avec la commande Draft Rotation. Pour le faire pivoter, il faut soit faire pivoter sa **Support**, soit modifier sa **Attachment Offset**.
-   Le concept d\'angle de base peut être quelque peu déroutant. D\'autant plus qu\'il ne fonctionne que lors de la sélection des points, et non lors de la spécification de l\'angle à l\'aide du champ de saisie. Vous trouverez une explication de son fonctionnement, ainsi qu\'un exemple, dans [ce fil de discussion](https://forum.freecad.org/viewtopic.php?p=736674#p736674).



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour resélectionner les objets de base après avoir copié des objets : **Édition → Préférences... → Draft → Général → Sélectionner les objets de base après la copie**.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour faire pivoter des objets, utilisez la méthode `rotate` du module Draft.


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```

-    `objectslist`contient les objets à faire pivoter. Il s\'agit soit d\'un objet unique, soit d\'une liste d\'objets.

-    `angle`est l\'angle de rotation en degrés.

-    `center`est le point central de la rotation.

-    `axis`est la direction de l\'axe de rotation.

-   Si `copy` est `True`, des copies sont créées au lieu de faire tourner les objets originaux.

-    `rotated_list`est retourné avec les objets originaux ayant subi une rotation, ou avec les nouvelles copies. Il s\'agit soit d\'un objet unique, soit d\'une liste d\'objets, en fonction de `objectlist`.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=300)
Draft.move(polygon1, App.Vector(1000, 0, 0))

# Rotation around the origin
angle1 = 45
rot2 = Draft.rotate(polygon1, angle1, copy=True)
rot3 = Draft.rotate(polygon1, 2*angle1, copy=True)
rot4 = Draft.rotate(polygon1, 4*angle1, copy=True)

polygon2 = Draft.make_polygon(3, radius=1000)
polygon3 = Draft.make_polygon(5, radius=500)
Draft.move(polygon2, App.Vector(2000, 0, 0))
Draft.move(polygon3, App.Vector(2000, 0, 0))

# Rotation around another point
angle2 = 60
cen = App.Vector(3100, 0, 0)
list2 = [polygon2, polygon3]
rot_list2 = Draft.rotate(list2, angle2, center=cen, copy=True)
rot_list3 = Draft.rotate(list2, 2*angle2, center=cen, copy=True)
rot_list4 = Draft.rotate(list2, 4*angle2, center=cen, copy=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/fr
