---
- GuiCommand:
   Name:Surface Filling
   Name/fr:Surface Remplissage
   MenuLocation:Surface → Filling...
   Workbenches:[Surface](Surface_Workbench/fr.md)
   Version:0.17
---

# Surface Filling/fr

## Description


**[<img src=images/Surface_Filling.svg style="width:16px"> [Surface Remplissage](Surface_Filling/fr.md)**

crée une surface à partir d\'une série d\'arêtes de délimitation connectées. La courbure de la surface peut être contrôlée en outre par des bords et des sommets non délimités, ainsi que par une surface de support.

La géométrie de base peut appartenir à des courbes créées avec l\'[atelier Draft](Draft_Workbench/fr.md) ou l\'[atelier Sketcher](Sketcher_Workbench/fr.md), mais aussi à des objets solides tels que ceux créés avec l\'[atelier Part](Part_Workbench/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md).

<img alt="" src=images/Surface_Filling_example.png  style="width:600px;"> 
*Deux surfaces remplies délimitées par quatre arêtes situées sur le plan XY. La surface de droite est en plus contrôlée par une arête non délimitée.*



## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Surface_Filling.svg style="width:16px"> [Remplissage](Surface_Filling/fr.md)**.
2.  Le panneau de tâches **Boundaries** s\'ouvre. Voir [Options](#Options.md).
3.  Sélectionnez deux ou plusieurs bords dans la [Vue 3D](3D_view/fr.md) :
    -   Il n\'est pas nécessaire d\'appuyer sur le bouton **Ajouter une arête** dans la section **Limites** à ce moment-là.
    -   Les arêtes doivent être sélectionnées dans un ordre consécutif.
    -   Les arêtes doivent être connectées, mais la frontière complète ne doit pas nécessairement être fermée.
    -   Le contour complet ne doit pas s\'auto-intersecter.
    -   Pour un contour circulaire de 360°, deux bords semi-circulaires peuvent être sélectionnés.
4.  Un aperçu de la forme finale s\'affiche dès qu\'un nombre suffisant de géométries valides a été sélectionné.
5.  Optionnellement, sélectionnez une **Support surface**. Voir [Exemple](#Exemple.md).
6.  Sélectionnez éventuellement une ou plusieurs **Contraintes d'arête**.
7.  Sélectionnez éventuellement une ou plusieurs **Contraintes de vertices**.
8.  Appuyez sur le bouton **OK**.

## Options

-   Dans la section **Limites**, vous pouvez spécifier une surface de support et les bords des limites :
    -   Appuyez sur le bouton **Surface de support** et sélectionnez une face dans la [Vue 3D](3D_view/fr.md) pour ajouter une surface de support.
        -   Cliquez sur l\'icône <img alt="" src=images/Edit-cleartext.svg  style="width:16px;"> pour supprimer la surface de support.
    -   Appuyez une fois sur le bouton **Ajouter une arête** pour commencer à sélectionner les arêtes de délimitation dans la [Vue 3D](3D_view/fr.md).
    -   Il existe plusieurs façons de désélectionner les arêtes de délimitation :
        -   Appuyez une fois sur le bouton **Supprimer l'arête** pour commencer à désélectionner les arêtes dans la [Vue 3D](3D_view/fr.md).
        -   Sélectionnez un bord dans la liste et appuyez sur **Supprimer**.
        -   Cliquez avec le bouton droit de la souris sur un bord de la liste et sélectionnez **Remove** dans le menu contextuel.

-   Dans la section **Contraintes d'arêtes**, il est possible de spécifier des arêtes non limites :
    -   Les options de sélection sont similaires à celles des arêtes limites.

-   Dans la section **Contraintes de sommets**, il est possible de spécifier des sommets non-bornés :
    -   Les options de sélection sont similaires à celles des arêtes limites.

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler l\'opération.



## Exemple


**Support surface**

agit comme une contrainte supplémentaire pour la surface. L\'exemple simple suivant vous donnera une idée de la façon dont cela fonctionne :

1.  Dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [atelier Part](Part_Workbench/fr.md), créez un <img alt="" src=images/Part_Cylinder.svg  style="width:16px;">[cylindre](Part_Cylinder/fr.md) et définissez **Angle** à {{Value|180°}}.
2.  Passez à l\'<img alt="" src=images/Workbench_Surface.svg  style="width:16px;"> [atelier Surface](Surface_Workbench/fr.md) et appuyez sur **[<img src=images/Surface_Filling.svg style="width:16px"> [Remplissage](Surface_Filling/fr.md)**.
3.  Sélectionnez les deux bords semi-circulaires et les deux bords droits qui les relient.
4.  Le résultat correspond aux quatre arêtes limites, mais la forme intérieure est très différente de la face cylindrique.
5.  Editez l\'objet Surface et pour la **Support surface** sélectionnez la face cylindrique.
6.  La forme modifiée correspond beaucoup mieux à la face cylindrique.



## Propriétés

[Surface Remplissage](Surface_Filling/fr.md) (classe `Surface::Filling`) est dérivée de la classe de base [Part Feature](Part_Feature/fr.md) (classe `Part::Feature` via la sous-classe `Part::Spline`), elle partage donc toutes les propriétés de cette dernière.

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

-    **Control Points|Bool**: par défaut `False`. Mis à `True`, elle affichera une superposition avec les points de contrôle de la surface.



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

# 
points_spl = [App.Vector(-10, 0, 2),
              App.Vector(4, 0, 7),
              App.Vector(18, 0, -5),
              App.Vector(25, 0, 0),
              App.Vector(30, 0, 0)]
aux_edge = Draft.make_bspline(points_spl)
doc.recompute()

surf.UnboundEdges = [(aux_edge, "Edge1")]
doc.recompute()

# 
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
![](images/Button_right.svg) [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface Filling/fr
