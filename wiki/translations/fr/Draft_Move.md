---
- GuiCommand:/fr
   Name:Draft Move
   Name/fr:Draft Déplacer
   MenuLocation:Modification → Déplacer
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**M** **V**
   Version:0.7
   SeeAlso:[Draft Surligner les sous éléments](Draft_SubelementHighlight/fr.md)
---

# Draft Move/fr

## Description

La commande <img alt="" src=images/Draft_Move.svg  style="width:24px;"> **Draft Déplacer** déplace ou copie les objets sélectionnés d\'un point à un autre. En mode sous-élément, la commande déplace les points et les bords sélectionnés ou copie les bords sélectionnés, des [Draft Lignes](Draft_Line/fr.md) et [Draft Polylignes](Draft_Wire/fr.md).

Cette commande peut être utilisée sur des objets 2D créés avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi sur de nombreux objets 3D tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md), l\'[atelier PartDesign](PartDesign_Workbench/fr.md) ou l\'[atelier Arch](Arch_Workbench/fr.md).

<img alt="" src=images/Draft_Move_example.jpg  style="width:400px;"> 
*Déplacer un objet d'un point à un autre*

## Utilisation

Voir aussi : [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Sélectionnez un ou plusieurs objets, ou un ou plusieurs sous-éléments de [Draft Lignes](Draft_Line/fr.md) ou [Draft Polylignes](Draft_Wire/fr.md).
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Draft_Move.svg" width=16px> [Déplacer](Draft_Move/fr.md)**.
    -   Sélectionnez l\'option **Modification → <img src="images/Draft_Move.svg" width=16px> Déplacer** dans le menu.
    -   Utilisez le raccourci clavier : **M** puis **V**.
3.  Si vous n\'avez pas encore sélectionné d\'objet : sélectionnez un objet dans la [Vue 3D](3D_view/fr.md).
4.  Le panneau de tâches **Move** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
5.  Si des sous-éléments ont été sélectionnés : cochez la case **Modifier les sous-éléments** pour activer le mode sous-élément.
6.  Choisissez le premier point, le point de base, dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
7.  Choisissez le deuxième point, le point cible, dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.

## Options

Les raccourcis clavier à caractère unique mentionnés ici peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md).

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Pour utiliser des coordonnées polaires, entrez une valeur pour la **Longueur** et une valeur pour l\'**Angle** et appuyez sur **Entrée** après chacune d\'elles.
-   Cochez la case **Angle** pour contraindre le pointeur à l\'angle spécifié.
-   Appuyez sur **H** pour faire passer le curseur de **X** à **Longueur** et inversement. Selon la saisie, la case **Angle** est cochée ou décochée.
-   Appuyez sur **R** ou cliquez sur la case **Relative** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées du deuxième point sont relatives au premier point, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **T** ou cliquez sur la case **Continue** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir été terminée. Ce mode n\'a vraiment de sens que si le mode copie est activé. En fonction de la préférence **Sélectionner les objets de base après la copie**, soit les objets originaux sont sélectionnés pour le prochain appel de la commande, soit les copies créées en dernier. Voir [Préférences](#Préférences.md).
-   Appuyez sur **P** ou cliquez sur la case **Copie** pour activer le mode copie. Si le mode copie est activé, la commande créera des copies déplacées au lieu de déplacer les objets originaux.
-   Appuyez sur **D** ou cliquez sur la case **Modifier les sous-éléments** pour faire basculer le mode sous-élément. Si le mode sous-élément est activé, la commande utilisera les sous-éléments sélectionnés au lieu des objets entiers. Les sous-éléments doivent appartenir à [Draft Lignes](Draft_Line/fr.md) ou [Draft Polylignes](Draft_Wire/fr.md).
-   Si le mode copie et le mode sous-élément sont tous deux activés et que les bords de [Draft Polylignes](Draft_Wire/fr.md) sont sélectionnés, de nouveaux fils seront créés à partir de ces bords.
-   En maintenant la touche **Alt** enfoncée après avoir choisi le point de base, vous basculerez également en mode copie. Pendant que vous maintenez la touche **Alt** enfoncée, vous pouvez choisir plusieurs points cibles. Relâchez **Alt** pour terminer la commande et voir les copies créées. Cette option ne fonctionne pas dans la version 0.19 de FreeCAD.
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour abandonner la commande.

## Remarques

-   Un objet [accroché](Part_EditAttachment/fr.md) ne peut pas être déplacé avec la commande Draft Déplacer. Pour le déplacer, il faut soit déplacer son objet **Support**, soit modifier son **Attachment Offset**.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées, longueurs et angles : **Édition → Préférences... → Général → Unités → Réglages des unités → Nombre de décimales**.
-   Pour modifier le champ initial du panneau des tâches sur le champ de saisie de **Longueur** : **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Mettre l'accent sur la longueur plutôt que la coordonnée X**. Notez que vous devez déplacer le pointeur dans la [vue 3D](3D_view/fr.md) pour que le changement prenne effet.
-   Pour stocker et réutiliser le même paramètre de mode de copie d\'une commande à l\'autre : **Édition → Préférences... → Draft → Paramètres généraux → Options de l'outil de dessin → Mode de copie global**.
-   Pour resélectionner les objets de base après avoir copié des objets : ** Édition → Préférences... → Draft → Paramètres généraux → Options de l'outil de dessin → Sélectionner les objets de base après la copie**.

## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour déplacer des objets, utilisez la méthode `move` du module Draft.


```python
moved_list = move(objectslist, vector, copy=False)
```

-    `objectslist`contient les objets à déplacer. Il s\'agit soit d\'un objet unique, soit d\'une liste d\'objets.

-    `vector`est le déplacement.

-   Si `copy` est `True`, des copies sont créées au lieu de déplacer les objets originaux.

-    `moved_list`est retourné avec les objets originaux déplacés, ou avec les nouvelles copies. Il s\'agit soit d\'un objet unique, soit d\'une liste d\'objets, en fonction de `objectslist`.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/fr
