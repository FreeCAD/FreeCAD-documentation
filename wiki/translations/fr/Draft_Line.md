---
- GuiCommand:/fr
   Name:Draft Line
   Name/fr:Draft Ligne
   MenuLocation:Drafting → Ligne
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**L** **I**
   Version:0.7
   SeeAlso:[Draft Polyligne](Draft_Wire/fr.md)
---

# Draft Line/fr

## Description

La commande <img alt="" src=images/Draft_Line.svg  style="width:24px;"> **Draft Ligne** crée une ligne droite.

Une Draft Ligne est en fait une [Draft Polyligne](Draft_Wire/fr.md) avec seulement deux points.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;"> 
*Ligne définie par deux points*

## Utilisation

Voir aussi : [Draft La barre](Draft_Tray/fr.md), [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Draft_Line.svg" width=16px> [Créer une ligne par deux points](Draft_Line/fr.md)**.
    -   Sélectionnez l\'option **Création → <img src="images/Draft_Line.svg" width=16px> Ligne** dans le menu.
    -   Utilisez le raccourci clavier : **L** puis **I**.
2.  Le panneau de tâches **Line** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Choisissez le premier point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
4.  Choisissez le deuxième point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Pour utiliser des coordonnées polaires, entrez une valeur pour la **Longueur** et une valeur pour l\'**Angle** et appuyez sur **Entrée** après chacune d\'elles.
-   Cochez la case **Angle** pour contraindre le pointeur à l\'angle spécifié.
-   Appuyez sur **H** pour faire passer le curseur de **X** à **Longueur** et inversement. Selon la saisie, la case **Angle** est cochée ou décochée.
-   Appuyez sur **R** ou cliquez sur la case **Relative** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées du deuxième point sont relatives au premier point, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **T** ou cliquez sur la case **Continuer** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir terminé, ce qui vous permet de continuer à créer des lignes.
-   Le bouton **<img src="images/Draft_UndoLine.svg" width=16px> Annuler**, affichée dans FreeCAD version 0.19 et antérieure, n\'a pas d\'utilité pour cette commande.
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour abandonner la commande.

## Remarques

-   Une Draft Ligne peut être éditée avec la commande [Draft Editer](Draft_Edit/fr.md).
-   Les Draft Lignes et les [Draft Polylignes](Draft_Wire/fr.md) peuvent être jointes avec la commande [Draft Polylignes](Draft_Wire/fr.md), la commande [Draft Joinde](Draft_Join/fr.md) ou la commande [Draft Mettre à niveau](Draft_Upgrade/fr.md).

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées, longueurs et angles : **Édition → Préférences... → Général → Unités → Système d'unités → Nombre de décimales**.
-   Pour modifier le champ initial du panneau des tâches sur le champ de saisie de **Longueur** : **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Mettre l'accent sur la longueur plutôt que la coordonnée X**. Notez que vous devez déplacer le pointeur dans la [vue 3D](3D_view/fr.md) pour que le changement prenne effet.
-   Si le **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Utiliser les primitives de Part si possible** est cochée, la commande créera une [Part Ligne](Part_Line/fr.md) au lieu d\'une Draft ligne.

## Propriétés

Voir [Draft Polylignes](Draft_Wire/fr#Propri.C3.A9t.C3.A9s.md).

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer une Draft Ligne, utilisez la méthode `make_line` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeLine`.


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```

-   Crée une `Ligne` entre les points `p1` et `p2` chacun défini par son `FreeCAD.Vector`, avec les unités en millimètres.
-   Crée un objet `Ligne` à partir d\'un `Part.LineSegment`.
-   Crée un objet `Ligne` du premier sommet au dernier sommet de la `Shape` donnée.

Exemple:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/fr
