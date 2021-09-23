---
- GuiCommand:/fr
   Name:Draft BSpline
   Name/fr:Draft B-spline
   MenuLocation:Drafting → B-spline
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**B** **S**
   Version:0.7
   SeeAlso:[Draft Polyligne](Draft_Wire/fr.md), [Draft Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md), [Draft Courbe de Bézier](Draft_BezCurve/fr.md)
---

# Draft BSpline/fr

## Description

La commande <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> **Draft B-spline** crée une [courbe B-spline](http://fr.wikipedia.org/wiki/B-spline) à partir de plusieurs points.

La commande Draft B-spline spécifie les **points exacts** par lesquels la courbe passera. Les commandes [Draft Courbe de Bézier](Draft_BezCurve.md) et [Draft Courbe de Bézier cubique](Draft_CubicBezCurve.md), en revanche, utilisent **des points de contrôle** pour définir la position et la courbure de la spline.

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*Spline definie par plusieurs points*

## Utilisation

Voir aussi: [Draft La barre](Draft_Tray/fr.md), [Draft Accrochage](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons d\'invoquer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_BSpline.svg" width=16px> [Créer une courbe B-spline...](Draft_BSpline/fr.md)**.
    -   Sélectionnez l\'option **Drafting → <img src="images/Draft_BSpline.svg" width=16px> B-spline** dans le menu.
    -   Utilisez le raccourci clavier : **B** puis **S**.
2.  Le panneau de tâches **B-spline** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Choisissez le premier point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
4.  Choisissez des points supplémentaires dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
5.  Appuyez sur **Echap** ou sur le bouton **Fermer** pour terminer la commande.

## Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valeurs X, Y et Z et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous avez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **R** ou cliquez sur la case **Relative** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées sont relatives au dernier point, si disponible, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cliquez sur la case **Global** pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **L** ou cliquez sur la case **Rempli** pour activer le mode de remplissage. Si le mode rempli est activé, la spline créée aura la valeur {{PropertyData/fr|Make Face}} `True` et aura une face remplie, à condition qu\'elle soit fermée et ne s\'auto-intersectionne pas. Notez qu\'une spline qui s\'auto-intersecte avec une face ne s\'affichera pas correctement, pour une telle spline, {{PropertyData/fr|Make Face}} doit être définie sur `False`.
-   Appuyez sur **T** ou cliquez sur la case **Continuer** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir utilisé **<img src="images/Draft_FinishLine.svg" width=16px> Terminer** ou **<img src="images/Draft_CloseLine.svg" width=16px> Fermer**, ou après avoir créé une spline fermée en l\'accrochant au premier point de la spline, ce qui vous permet de continuer à créer des splines.
-   Appuyez sur le bouton **<img src="images/Draft_UndoLine.svg" width=16px> Annuler** pour annuler le dernier point. Le raccourci clavier **Ctrl**+**Z** ne fonctionne pas actuellement.
-   Appuyez sur **A** ou sur le bouton **<img src="images/Draft_FinishLine.svg" width=16px> Terminer** pour terminer la commande et laisser la cannelure ouverte.
-   Appuyez sur **O** ou sur le bouton **<img src="images/Draft_CloseLine.svg" width=16px> Fermer** pour terminer la commande et fermer la courbe. Une spline fermée peut également être créée en s\'accrochant au premier point de la spline.
-   Appuyez sur **W** ou sur le bouton **<img src="images/Draft_Wipe.svg" width=16px> Effacer** pour supprimer les segments de courbe déjà placés, mais continuez à travailler à partir du dernier point.
-   Appuyez sur **U** ou sur le bouton **<img src="images/Draft_SelectPlane.svg" width=16px> [Définir le plan de travail](Draft_SelectPlane/fr.md)** pour ajuster le plan de travail actuel dans l\'orientation définie par le dernier et le précédent point.
-   Appuyez sur **S** pour activer ou désactiver [Draft Accrochage](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour terminer la commande.

## Remarques

-   Une Draft B-spline peut être éditée avec la commande [Draft Editer](Draft_Edit/fr.md).
-   Une Draft B-spline peut être convertie en un [Draft Polyligne](Draft_Wire/fr.md) avec la commande [Draft Filaire vers B-spline](Draft_WireToBSpline/fr.md).

## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées : **Édition → Préférences... → Général → Unités → Système d'unités → Nombre de décimales**.
-   Pour modifier la valeur initiale du mode rempli : **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Remplir les objets avec des faces si possible**. La modification du mode rempli dans un panneau de tâches annule cette préférence pour la session FreeCAD en cours.

## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft B-spline est dérivée d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{TitleProperty/fr|Draft}}

-    {{PropertyData/fr|Area|Area}}: (en lecture seule) spécifie la surface de la face de la spline. La valeur sera {{value|0.0}} si {{PropertyData/fr|Make Face}} est `False` ou si la face ne peut être créée.

-    {{PropertyData/fr|Closed|Bool}}: spécifie si la spline est fermée ou non. Si la spline est initialement ouverte, cette valeur est `False`, si vous lui attribuez la valeur `True`, un segment de courbe sera dessiné pour fermer la spline. Si la courbe est initialement fermée, cette valeur est `True`, la définir sur `False` supprimera le dernier segment de courbe et rendra la courbe ouverte.

-    {{PropertyData/fr|Make Face|Bool}}: spécifie si la spline fait une face ou non. Si c\'est `True`, une face est créée, sinon seul le périmètre est considéré comme faisant partie de l\'objet. Cette propriété ne fonctionne que si {{PropertyData/fr|Closed}} est `True` et si le spline ne s\'auto-intersecte pas.

-    {{PropertyData/fr|Parameterization|Float}}: affecte la forme de la spline.

-    {{PropertyData/fr|Points|VectorList}}: spécifie les points de la spline dans son système de coordonnées local.

### Vue


{{TitleProperty/fr|Draft}}

-    {{PropertyView/fr|Arrow Size|Length}}: spécifie la taille du symbole affiché à l\'extrémité de la courbe.

-    {{PropertyView/fr|Arrow Type|Enumeration}}: spécifie le type de symbole affiché à l\'extrémité de la courbe, qui peut être {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} ou {{value|Tick-2}}.

-    {{PropertyView/fr|End Arrow|Bool}}: spécifie s\'il faut afficher un symbole à l\'extrémité de la courbe spline, afin qu\'elle puisse être utilisée comme ligne d\'annotation.

-    {{PropertyView/fr|Pattern|Enumeration}}: spécifie le [Draft Motif](Draft_Pattern/fr.md) avec lequel remplir la face de la courbe fermée. Cette propriété ne fonctionne que si {{PropertyData/fr|Make Face}} est `True` et si {{PropertyView/fr|Display Mode}} est {{value|Flat Lines}}.

-    {{PropertyView/fr|Pattern Size|Float}}: spécifie la taille du [Draft Motif](Draft_Pattern/fr.md).

## Script

Voir aussi: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour créer une Draft B-spline, utilisez la méthode `make_bspline` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeBSpline`.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Crée un objet `bspline` avec la liste de points donnée, `pointslist`.
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

spline1 = Draft.make_bspline([p1, p2, p3], closed=False)
spline2 = Draft.make_bspline([p1, 2*p3, 1.3*p2], closed=False)
spline3 = Draft.make_bspline([1.3*p3, p1, -1.7*p2], closed=False)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/fr
