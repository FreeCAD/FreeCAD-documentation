---
- GuiCommand:
   Name:Draft Wire
   Name/fr:Draft Polyligne
   MenuLocation:Draft → Polyligne
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   Shortcut:**P** **L**
   Version:0.7
   SeeAlso:[Draft Ligne](Draft_Line/fr.md), [Draft B-spline](Draft_BSpline/fr.md)
---

# Draft Wire/fr

## Description

La commande <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> **Draft Polyligne** [crée](#Cr.C3.A9er.md) une polyligne, une séquence de plusieurs segments de ligne connectés. La commande peut aussi être utilisée pour [joindre](#Joindre.md) des [Draft Lignes](Draft_Line/fr.md) et des Draft Polylignes.

Les angles d\'une Draft Polyligne peuvent être arrondis ou chanfreinés en modifiant respectivement sa propriété **Fillet Radius** ou **Chamfer Size**. Il est également possible de subdiviser les bords d\'une Draft Polyligne en modifiant sa propriété **Subdivisions**.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;"> 
*Une polyligne définie par plusieurs points*



## Créer



### Utilisation

Voir aussi : [Draft La barre](Draft_Tray/fr.md), [Draft Aimantation](Draft_Snap/fr.md) et [Draft Contrainte](Draft_Constrain/fr.md).

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Wire.svg" width=16px> [Polyligne](Draft_Wire/fr.md)**.
    -   Sélectionnez l\'option **Draft → <img src="images/Draft_Wire.svg" width=16px> Polyligne** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **L**.
2.  Le panneau de tâches **Polyligne** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
3.  Choisissez le premier point dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
4.  Choisissez des points supplémentaires dans la [Vue 3D](3D_view/fr.md) ou rentrez des coordonnées et appuyez sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point**.
5.  Appuyez sur **Echap** ou sur le bouton **Fermer** pour terminer la commande.

### Options

Les raccourcis clavier à caractère unique disponibles dans le panneau des tâches peuvent être modifiés. Voir [Draft Préférences](Draft_Preferences/fr.md). Les raccourcis mentionnés ici sont les raccourcis par défaut.

-   Pour saisir manuellement des coordonnées, entrez les valuers X, Y et Z, et appuyez sur **Entrée** après chacune, ou vous pouvez appuyer sur le bouton **<img src="images/Draft_AddPoint.svg" width=16px> Entrez le point** lorsque vous savez les valeurs souhaitées. Il est conseillé de déplacer le pointeur hors de la [Vue 3D](3D_view/fr.md) avant de saisir les coordonnées.
-   Appuyez sur **R** ou cochez la case **Relative** pour activer le mode relatif. Si le mode relatif est activé, les coordonnées sont relatives au dernier point, si disponible, sinon elles sont relatives à l\'origine du système de coordonnées.
-   Appuyez sur **G** ou cochez la case **Global** pour activer le mode global. Si le mode global est activé, les coordonnées sont relatives au système de coordonnées global, sinon elles sont relatives au système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.20}}
-   Appuyez sur **L** ou cochez la case **Rempli** pour activer le mode de remplissage. Si le mode rempli est activé, la ligne créée aura la valeur {{PropertyData/fr|Make Face}} `True` et aura une face remplie, à condition qu\'elle soit fermée et qu\'elle ne s\'auto-intersecte pas. Notez qu\'une ligne qui s\'auto-intersecte avec une face ne s\'affichera pas correctement. Pour une telle ligne, {{PropertyData/fr|Make Face}} doit être défini sur `False`.
-   Appuyez sur **T** ou cochez la case **Continuer** pour activer le mode continu. Si le mode continu est activé, la commande redémarre après avoir utilisé **<img src="images/Draft_FinishLine.svg" width=16px> Terminer** ou **<img src="images/Draft_CloseLine.svg" width=16px> Fermer**, ou après avoir créé une ligne fermée en s\'aimantant au premier point de la ligne, ce qui vous permet de continuer à créer des lignes.
-   Appuyez sur **/** ou sur le bouton **<img src="images/Draft_UndoLine.svg" width=16px> Annuler** pour annuler le dernier point.
-   Appuyez sur **A** ou sur le bouton **<img src="images/Draft_FinishLine.svg" width=16px> Terminer** pour terminer la commande et laisser la ligne ouverte.
-   Appuyez sur **O** ou sur le bouton **<img src="images/Draft_CloseLine.svg" width=16px> Fermer** pour terminer la commande et fermer la ligne. Une ligne fermée peut également être créée en s\'aimantant au premier point de la ligne.
-   Appuyez sur **W** ou sur le bouton **<img src="images/Draft_Wipe.svg" width=16px> Effacer** pour supprimer les segments déjà placés, mais continuez à travailler à partir du dernier point.
-   Appuyez sur **U** ou sur le bouton **<img src="images/Draft_SelectPlane.svg" width=16px> [Définir le plan de travail](Draft_SelectPlane/fr.md)** pour ajuster le plan de travail actuel dans l\'orientation du dernier segment.
-   Appuyez sur **S** pour activer ou désactiver [Draft Aimantation](Draft_Snap/fr.md).
-   Appuyez sur **Echap** ou sur le bouton **Fermer** pour terminer la commande.



## Joindre



### Utilisation 

1.  Les extrémité des [Draft Lignes](Draft_Line/fr.md) et/ou des Draft Polylignes à joindre doivent coïncider exactement. Si nécessaire, ajustez d\'abord les points pour vous assurer que c\'est le cas.
2.  Sélectionnez deux ou plusieurs [Draft Lignes](Draft_Line/fr.md) et/ou des Draft Polylignes.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Draft_Wire.svg" width=16px> [Polyligne](Draft_Wire/fr.md)**.
    -   Sélectionnez l\'option **Draft → <img src="images/Draft_Wire.svg" width=16px> Polyligne** dans le menu.
    -   Utilisez le raccourci clavier : **P** puis **L**.



## Remarques

-   Une Draft Polyligne peut être éditée avec la commande [Draft Éditer](Draft_Edit/fr.md).
-   Une Draft Ligne peut être convertie en une [Draft B-spline](Draft_BSpline/fr.md) avec la commande [Draft Polyligne vers B-spline](Draft_WireToBSpline/fr.md).
-   Les [Draft Lignes](Draft_Line/fr.md) et les Draft Polylignes peuvent également être jointes avec la commande [Draft Joindre](Draft_Join/fr.md) ou la commande [Draft Agréger](Draft_Upgrade/fr.md).



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   Pour modifier le nombre de décimales utilisées pour la saisie des coordonnées : **Édition → Préférences... → Général → Unités → Système d'unités → Nombre de décimales**.
-   Pour modifier la valeur initiale du mode rempli : **Édition → Préférences... → Draft → Paramètres généraux → Options des outils de Draft → Remplir les objets avec des faces si possible**. La modification du mode rempli dans un panneau de tâches annule cette préférence pour la session FreeCAD en cours.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Draft Polyligne est dérivé d\'un [Part Part2DObject](Part_Part2DObject/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Draft}}

-    **Area|Area**: (en lecture seule) spécifie la surface de la face générée par la ligne. La valeur sera {{value|0.0}} si **Make Face** est `False` ou si la face ne peut être créée.

-    **Base|Link**
    

-    **Chamfer Size|Length**: spécifie la longueur des chanfreins aux coins de la ligne.

-    **Closed|Bool**: spécifie si la ligne est fermée ou non. Si la ligne est initialement ouverte, cette valeur est `False`. Si vous lui attribuez la valeur `True`, un segment de la ligne sera dessiné pour fermer la ligne. Si la ligne est initialement fermée, cette valeur est `True`, la mettre à `False` supprimera le dernier segment de la ligne et rendra la ligne ouverte.

-    **End|VectorDistance**: spécifie le dernier point de la ligne.

-    **lignelet Radius|Length**: spécifie le rayon des filets aux brisures de la ligne.

-    **Length|Length**: (en lecture seule) spécifie la longueur totale de la ligne.

-    **Make Face|Bool**: spécifie si la ligne fait une face ou non. Si c\'est `True`, une face est créée, sinon seuls les bords sont considérés comme faisant partie de l\'objet. Cette propriété ne fonctionne que si **Closed** est `True` et si la ligne ne s\'auto-intersecte pas.

-    **Points|VectorList**: spécifie les points de la ligne dans son système de coordonnées local.

-    **Start|VectorDistance**: spécifie le premier point de la ligne.

-    **Subdivisions|Integer**: spécifie le nombre de subdivisions pour chaque arête de la ligne. Si la valeur est {{value|1}}, chaque bord sera divisé en {{value|2}} segments égaux. Les subdivisions sont appliquées avant les chanfreins et les ligneets.

-    **Tool|Link**
    



### Vue


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: spécifie la taille du symbole affiché à l\'extrémité de la ligne.

-    **Arrow Type|Enumeration**: spécifie le type de symbole affiché à l\'extrémité de la ligne, qui peut être {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} ou {{value|Tick-2}}.

-    **End Arrow|Bool**: spécifie s\'il faut afficher un symbole à la fin de la ligne, afin qu\'elle puisse être utilisée comme ligne d\'annotation.

-    **Pattern|Enumeration**: spécifie le [Draft Motif](Draft_Pattern/fr.md) avec lequel remplir la face de la ligne fermée. Cette propriété ne fonctionne que si **Make Face** est `True` et si **Display Mode** est à {{value|Flat Lines}}.

-    **Pattern Size|Float**: spécifie la taille du [Draft Motif](Draft_Pattern/fr.md).



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Pour créer une Draft Polyligne, utilisez la méthode `make_wire` ({{Version/fr|0.19}}) du module Draft. Cette méthode remplace la méthode dépréciée `makeWire`.


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Crée un objet `Wire` avec la liste de points donnée, `liste de points`.
    -   Chaque point de la liste est défini par son `FreeCAD.Vector`, avec comme unité le millimètre.
    -   Sinon, l\'entrée peut être un `Part.Wire`, à partir duquel les points sont extraits.
-   Si `closed` est réglé sur `True`, ou si les premier et dernier points sont identiques, le fil est fermé.
-   Si un `placement` est `None`, la courbe est créée à l\'origine.
-   Si `face` est réglé sur `True`, et que le fil est fermé, le fil fera une face, c\'est-à-dire qu\'elle apparaîtra remplie.

Exemple :


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/fr
