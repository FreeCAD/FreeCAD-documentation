---
- GuiCommand:/fr
   Name:Draft BezCurve
   Name/fr:Draft Courbe de Bézier
   MenuLocation:Drafting → Outils Bézier → Courbe de Bézier
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**B** **Z**
   Version:0.14
   SeeAlso:[Draft Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md), [Draft B-spline](Draft_BSpline/fr.md)
---

# Draft BezCurve/fr

## Description

La commande <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> **Draft Courbe de Bézier** crée une [courbe de Bézier](http://fr.wikipedia.org/wiki/Courbe_de_B%C3%A9zier) à partir de plusieurs points.

La commande crée une seule courbe de Bézier dont la {{PropertyData/fr|Degree}} est `number_of_points - 1`. Elle peut être transformée en une courbe de Bézier par morceaux en réduisant cette propriété.

Les commandes Draft Courbe de Bézier et [Draft Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md) utilisent **des points de contrôle** pour définir la position et la courbure de la spline. La commande [Draft B-spline](Draft_BSpline.md), quant à elle, spécifie les **points exacts** par lesquels la courbe passera.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Courbe de Bézier définie par plusieurs points de control*

## Utilisation

Voir aussi : [Draft La barre](Draft_Tray/fr.md), [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_BezCurve.svg" width=16px> [Draft Courbe de Bézier](Draft_BezCurve/fr.md)**.
    -   Sélectionnez l\'option **Drafting → Outils Bézier → <img src="images/Draft_BezCurve.svg" width=16px> Courbe de Bézier** dans le menu.
    -   Utilisez le raccourci clavier : **B** puis **Z**. {{Version/fr|0.20}}
2.  Le panneau de tâches **Courbe de Bézier** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Choisissez le premier point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
4.  Choisissez des points supplémentaires dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
5.  Appuyez sur **Echap** ou sur le bouton **Fermer** pour terminer la commande.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune. Ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **R** ou cliquez sur la case **Relative** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées sont relatives au dernier point, si disponible, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **L** ou cliquez sur la case **Rempli** pour activer le mode de remplissage. Si le mode rempli est activé, la courbe créée aura la valeur {{PropertyData/fr|Make Face}} mis à `True` et aura une face remplie, à condition qu\'elle soit fermée et ne s\'auto-intersectionne pas. Notez qu\'une courbe qui s\'auto-intersecte avec une face ne s\'affichera pas correctement. Pour une telle courbe, {{PropertyData/fr|Make Face}} doit être défini sur `False`.
-   Appuyez sur **T** ou cliquez sur la case **Continuer** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir utilisé **<img src="images/Draft_FinishLine.svg" width=16px> Terminer** ou **<img src="images/Draft_CloseLine.svg" width=16px> Fermer**, ou après avoir créé une courbe fermée en la fixant au premier point de la courbe, ce qui vous permet de continuer à créer des courbes.
-   Appuyez sur le bouton **<img src="images/Draft_UndoLine.svg" width=16px> Annuler** pour annuler le dernier point. Le raccourci clavier **Ctrl**+**Z** ne fonctionne pas actuellement.
-   Appuyez sur **A** ou sur le bouton **<img src="images/Draft_FinishLine.svg" width=16px> Terminer** pour terminer la commande et laisser la courbe ouverte.
-   Appuyez sur **O** ou sur le bouton **<img src="images/Draft_CloseLine.svg" width=16px> Fermer** pour terminer la commande et fermer la courbe. Une courbe fermée peut également être créée en se plaçant au premier point de la courbe.
-   Appuyez sur **W** ou sur le bouton **<img src="images/Draft_Wipe.svg" width=16px> Effacer** pour supprimer les segments déjà placés, mais continuez à travailler à partir du dernier point.
-   Appuyez sur **U** ou sur le bouton **<img src="images/Draft_SelectPlane.svg" width=16px> [Définir le plan de travail](Draft_SelectPlane/fr.md)** pour ajuster le plan de travail actuel dans l\'orientation définie par le dernier et le précédent point.
-   Appuyez sur **S** pour activer ou désactiver [Draft Accrochage](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour terminer la commande.

## Remarques

-   Une Draft Courbe de Bézier peut être éditée avec la commande [Draft Éditer](Draft_Edit/fr.md).
-   OpenCascade, et donc FreeCAD, ne supporte pas les courbes de Bézier de degrés supérieurs à 25. Cela ne devrait pas être un problème en pratique, car la plupart des utilisateurs utilisent généralement des courbes de Bézier de degrés 3 à 5.

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées : **Édition → Préférences... → Général → Unités → Système d'unités → Nombre de décimales**.
-   Pour modifier la valeur initiale du mode rempli : **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Remplir les objets avec des faces si possible**. La modification du mode rempli dans un panneau de tâches annule cette préférence pour la session FreeCAD en cours.

## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Courbe de Bézier est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty|Draft}}

-    {{PropertyData/fr|Area|Area}}: (en lecture seule) spécifie la surface de la face de la courbe. La valeur sera {{value|0.0}} si {{PropertyData/fr|Make Face}} est `False` ou si la face ne peut être créée.

-    {{PropertyData/fr|Closed|Bool}}: spécifie si la courbe est fermée ou non. Si la courbe est initialement ouverte, cette valeur est `False`, si vous lui attribuez la valeur `True`, un segment sera dessiné pour fermer la courbe. Si la courbe est initialement fermée, cette valeur est `True`, la mettre à `False` supprimera le dernier segment et rendra la courbe ouverte.

-    {{PropertyData/fr|Continuity|IntegerList}}: (en lecture seule) spécifie la continuité de la courbe.

-    {{PropertyData/fr|Degree|Integer}}: spécifie le degré de la courbe.

-    {{PropertyData/fr|Length|Length}}: (en lecture seule) spécifie la longueur totale de la courbe.

-    {{PropertyData/fr|Make Face|Bool}}: spécifie si la courbe fait une face ou non. Si c\'est `True`, une face est créée, sinon seul le périmètre est considéré comme faisant partie de l\'objet. Cette propriété ne fonctionne que si {{PropertyData/fr|Closed}} est `True` et si la courbe ne s\'auto-intersecte pas.

-    {{PropertyData/fr|Points|VectorList}}: spécifie les points de contrôle de la courbe dans son système de coordonnées local.

### Vue


{{TitleProperty|Draft}}

-    {{PropertyView/fr|Arrow Size|Length}}: spécifie la taille du symbole affiché à l\'extrémité de la courbe.

-    {{PropertyView/fr|Arrow Type|Enumeration}}: spécifie le type de symbole affiché à la fin de la courbe, qui peut être {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} ou {{value|Tick-2}}.

-    {{PropertyView/fr|End Arrow|Bool}}: spécifie s\'il faut afficher un symbole à la fin de la courbe, afin qu\'elle puisse être utilisée comme ligne d\'annotation.

-    {{PropertyView/fr|Pattern|Enumeration}}: spécifie le [Draft Motif](Draft_Pattern/fr.md) avec lequel remplir la face de la courbe fermée. Cette propriété ne fonctionne que si {{PropertyData/fr|Make Face}} est `True` et si {{PropertyView/fr|Display Mode}} est {{value|Flat Lines}}.

-    {{PropertyView/fr|Pattern Size|Float}}: spécifie la taille du [Draft Motif](Draft_Pattern/fr.md).

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer une Draft Ligne, utilisez la méthode `make_bezcurve` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeBezCurve`.


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```

-   Crée un objet `bezcurve` avec la liste de points donnée, `pointslist`.
    -   Chaque point de la liste est défini par son `FreeCAD.Vector`, en millimètres.
    -   Sinon, l\'entrée peut être un `Part.Wire` à partir duquel les points sont extraits.
-   Si `closed` est `True` ou si les premier et dernier points sont identiques, la courbe est fermée.
-   Si un `placement` est `None`, la courbe est créée à l\'origine.
-   Si `face` est `True` et la courbe est fermée, la courbe fera une face, c\'est-à-dire qu\'elle apparaîtra remplie.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)
p4 = App.Vector(1500, -2000, 0)

bezcurve1 = Draft.make_bezcurve([p1, p2, p3, p4], closed=True)
bezcurve2 = Draft.make_bezcurve([p4, 1.3*p2, p1, 4.1*p3], closed=True)
bezcurve3 = Draft.make_bezcurve([1.7*p3, 1.5*p4, 2.1*p2, p1], closed=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/fr
