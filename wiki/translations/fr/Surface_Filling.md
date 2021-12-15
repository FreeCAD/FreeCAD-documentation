---
- GuiCommand:/fr
   Icon:Filling.svg
   Name:Surface Filling
   Name/fr:Surface Remplissage
   MenuLocation:Surface → Filling...
   Workbenches:[Surface](Surface_Workbench/fr.md)
   Version:0.17
---

# Surface Filling/fr

## Description


**<img src=images/Surface_Filling.svg style="width:16px"> [Surface Remplissage](Surface_Filling/fr.md)**

crée une surface à partir d\'une série d\'arêtes limites connectées.

La surface peut être modifiée en ajoutant des arêtes et des sommets de contrainte que la surface doit traverser.

<img alt="" src=images/Surface_Filling_example.png  style="width:600px;">



*Exemple de surface remplie, délimitée par quatre arêtes situées dans le plan XY; (à gauche) uniquement les quatre arêtes et (à droite) une courbe supplémentaire dans l'espace définissant la courbure de la surface*

## Utilisation


<div class="mw-translate-fuzzy">

1.  Assurez-vous d\'avoir au moins trois arêtes ou courbes dans l\'espace formant un contour fermé. Par exemple, ceux-ci peuvent être créés avec des outils de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> _ . L\'utilisation de trois arêtes créerait une surface triangulaire; quatre arêtes une surface quadrilatérale.
    -   En option, les courbes peuvent être dessinées à l\'intérieur du contour fermé, sans nécessairement toucher les bords. Ces courbes peuvent être utilisées pour contrôler la courbure de la surface résultante.
    -   De même, un certain nombre de sommets peuvent être utilisés dans le même but pour indiquer où la surface doit passer.
2.  Appuyez sur le bouton **<img src=images/Surface_Filling.svg style="width:16px"> [Surface fill](Surface_Filling/fr.md)**.
3.  Dans la section **Boundary**, appuyez sur **Add edge**.
4.  Utilisez le pointeur pour sélectionner les arêtes souhaitées dans la [Vue 3D](3D_view/fr.md). Un aperçu de la forme finale sera affiché après avoir sélectionné des arêtes valides qui forment un contour fermé.
    -   En option, allez dans la section **Curvature: non-boundary edges**, appuyez sur **Add edge**, et choisissez les arêtes souhaitées dans la [Vue 3D](3D_view/fr.md) .
    -   En option, allez dans la section **Curvature: non-boundary vertices**, appuyez sur **Add vertex**, et choisissez les sommets désirés dans la [Vue 3D](3D_view/fr.md) .
5.  Appuyez sur **OK** pour terminer l\'opération.


</div>

Les arêtes de base qui forment le contour fermé, ainsi que les sommets et arêtes auxiliaires, peuvent appartenir à des courbes 2D de <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> _ mais peut également appartenir à des objets solides 3D tels que ceux créés avec <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> _.

## Options

-   Dans la section **Boundary**.
    -   
        **Add edge**
        
        : appuyez une fois pour commencer à sélectionner **Boundary edges** (les bords) dans la <img src=images/Draft_Wire.svg style="width:Vue 3D](3D_view/fr.md). Les arêtes droites telles que **_** ou les arêtes courbes telles que **_ _** et des **[16px"> [Part Primitives](Part_Primitives/fr.md)**.

    -   
        **Remove edge**
        
        : appuyez une fois pour commencer à choisir les arêtes dans la [Vue 3D](3D_view/fr.md). Ces arêtes doivent avoir été préalablement sélectionnées avec **Add edge**.

-    **Right mouse button**: ouvrez le menu contextuel et sélectionnez **Remove** ou appuyez sur **Suppr** au clavier pour supprimer le bord actuellement sélectionné dans la liste.

-   Section **Curvature: non-boundary edges**. Le bouton **Add edge** permet de sélectionner des arêtes auxiliaires (lignes droites ou B-Splines) pour contrôler la courbure de la surface. La surface sera forcée de passer à travers ces bords auxiliaires. Cela fonctionne mieux lorsque les arêtes auxiliaires se trouvent à l\'intérieur de la région délimitée par **Boundary bords**.
-   Section **Curvature: non-boundary vertices**. Similaire aux arêtes non-frontières (non-boundary edges), l\'utilisateur peut choisir des sommets auxiliaires pour contrôler la courbure. Ces sommets peuvent être autonomes **<img src=images/Draft_Point.svg style="width:16px"> <img src=images/Part_Point.svg style="width:Draft Points](Draft_Point/fr.md)** ou **[16px"> [Part Points](Part_Point/fr.md)** ou peut appartenir à n\'importe quelle arête (lignes droites ou B-Splines) ou être un sommet d\'angle dans un objet solide. Dans ce cas, la surface sera contrainte de passer par ces points auxiliaires.
-   Appuyez sur **Cancel** ou **Echap** pour abandonner l\'opération en cours.

## Propriétés

_ (classe `Part::Feature` via la sous-classe `Part::Spline`), elle partage donc toutes les propriétés de cette dernière.

Outre les propriétés décrites dans [Part Feature](Part_Feature/fr.md), Surface Remplissage a les propriétés suivantes dans l\'[éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty|Filling}}

-    {{PropertyData/fr|Boundary Edges|LinkSubList}}: bords de frontière; C0 est requis pour les arêtes sans face correspondante.

-    {{PropertyData/fr|Boundary Faces|StringList}}:

-    {{PropertyData/fr|Boundary Order|IntegerList}}: ordre de contrainte sur les faces limites; {{Value|0}}, {{Value|1}} et {{Value|2}} sont possibles.

-    {{PropertyData/fr|Bords non liés|LinkSubList}}: bords de contrainte non liés; C0 est requis pour les arêtes sans face correspondante.

-    {{PropertyData/fr|Unbound Faces|StringList}}:

-    {{PropertyData/fr|Unbound Order|IntegerList}}: ordre de contrainte sur les faces non liées; {{Value|0}}, {{Value|1}} et {{Value|2}} sont possibles.

-    {{PropertyData/fr|Free Faces|LinkSubList}}: contrainte libre sur une face.

-    {{PropertyData/fr|Free Order|IntegerList}}: ordre de contrainte sur les faces libres.

-    {{PropertyData/fr|Points|LinkSubList}}: points de contrainte sur la surface.

-    {{PropertyData/fr|Initial Face|LinkSub}}: surface initiale à utiliser.

-    {{PropertyData/fr|Degree|Integer}}: degré de départ, la valeur par défaut est {{Value|3}}.

-    {{PropertyData/fr|Points On Curve|Integer}}: nombre de points sur une arête pour la contrainte.

-    {{PropertyData/fr|Iterations|Integer}}: nombre d\'itérations, la valeur par défaut est {{Value|2}}.

-    {{PropertyData/fr|Anisotropy|Bool}}: il vaut par défaut `False`.

-    {{PropertyData/fr|Tolerance2d|Float}}: tolérance 2D, la valeur par défaut est {{Value|0.0}}.

-    {{PropertyData/fr|Tolerance3d|Float}}: tolérance 3D, la valeur par défaut est {{Value|0.0}}.

-    {{PropertyData/fr|Tol Angular|Float}}: tolérance G1, la valeur par défaut est {{Value|0.01}}.

-    {{PropertyData/fr|Tol Curvature|Float}}: tolérance G2, la valeur par défaut est {{Value|0.10}}.

-    {{PropertyData/fr|Maximum Degree|Integer}}: degré maximum de la courbe, la valeur par défaut est {{Value|8}}.

-    {{PropertyData/fr|Maximum Segments|Integer}}: nombre maximum de segments, la valeur par défaut est {{Value|9}}.

### Vue


{{TitleProperty|Base}}

-    {{PropertyView/fr|Control Points|Bool}}: la valeur par défaut est `False`. Mis à `True`, elle affichera une superposition avec les points de contrôle de la surface.

## Limitations

Le code de surface du noyau de modélisation interne [OpenCASCADE](OpenCASCADE/fr.md) est fragile et ne peut pas gérer correctement les entrées erronées. Les situations suivantes peuvent causer des problèmes et faire planter le programme, elles doivent donc être évitées:

-   Ajouter des {{PropertyData/fr|Boundary Edges}} à cela résulterait en plusieurs faces fermées. Dans ce cas, ces arêtes doivent être ajoutées en tant que {{PropertyData/fr|Unbound Edges}} pour contrôler uniquement la courbure.
-   Utilisation des {{PropertyData/fr|Boundary Edges}} paramétriques (par exemple **<img src=images/Draft_BSpline.svg style="width:16px"> [Draft BSplines](Draft_BSpline/fr.md)**) qui, une fois recalculés, ne parviennent pas à produire une frontière fermée. Autrement dit, les arêtes à utiliser comme {{PropertyData/fr|Boundary Edges}} doivent toujours former une forme fermée, même si leurs propriétés internes changent.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Remplissage de Surface peut être utilisé dans [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en ajoutant l\'objet `Surface :: Filling`.

-   Les arêtes à utiliser pour définir la surface doivent être affectées en tant que [LinkSubList](LinkSubList/fr.md) à la propriété `BoundaryEdges` de l\'objet.
-   Les arêtes et les sommets auxiliaires doivent être affectés en tant que [LinkSubLists](LinkSubList/fr.md) aux propriétés `UnboundEdges` et `Points` de l\'objet.
-   Tous les objets avec des arêtes doivent être calculés avant de pouvoir être utilisés comme entrée pour les propriétés de l\'objet Filling.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

a = App.Vector(-20, -20, 0)
b = App.Vector(-18, 25, 0)
c = App.Vector(60, 26, 0)
d = App.Vector(33, -20, 0)

points1 = [a, App.Vector(-20, -8, 0), App.Vector(-17, 7, 0), b]
obj1 = Draft.make_bspline(points1)

points2 = [b, App.Vector(0, 25, 0), c]
obj2 = Draft.make_bspline(points2)

points3 = [c, App.Vector(37, 4, 0), d]
obj3 = Draft.make_bspline(points3)

points4 = [d, App.Vector(-2, -18, 0), a]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::Filling", "Surface")
surf.BoundaryEdges = [(obj1, "Edge1"),
                      (obj2, "Edge1"),
                      (obj3, "Edge1"),
                      (obj4, "Edge1")]
doc.recompute()

# ---------------------------------------------------------
points_spl = [App.Vector(-10, 0, 2),
              App.Vector(4, 0, 7),
              App.Vector(18, 0, -5),
              App.Vector(25, 0, 0),
              App.Vector(30, 0, 0)]
aux_edge = Draft.make_bspline(points_spl)
doc.recompute()

surf.UnboundEdges = [(aux_edge, "Edge1")]
doc.recompute()

# ---------------------------------------------------------
aux_v1 = Draft.make_line(App.Vector(-13, -12, 5),
                         App.Vector(-13, -12, -5))
aux_v2 = Draft.make_line(App.Vector(-3, 18, 5),
                         App.Vector(-3, 18, -5))
doc.recompute()

surf.Points = [(aux_v1, "Vertex2"),
               (aux_v2, "Vertex1")]
doc.recompute()
```





{{Surface Tools navi

}}

---
[documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface Filling/fr
