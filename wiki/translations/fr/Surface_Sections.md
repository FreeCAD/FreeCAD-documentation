---
- GuiCommand:/fr
   Name:Surface Sections
   Name/fr:Surface Sections
   MenuLocation:Surface → Sections...
   Workbenches:[Surface](Surface_Workbench/fr.md)
   Version:0.19
---

# Surface Sections/fr

## Description


**<img src=images/Surface_Sections.svg style="width:16px"> [Surface Sections](Surface_Sections/fr.md)**

est utilisé pour créer une surface à partir d\'arêtes qui représentent des sections transversales d\'une surface.

<img alt="" src=images/Surface_Sections_edges_example.png  style="width:" height="250px;"> <img alt="" src=images/Surface_Sections_example.png  style="width:" height="250px;">


*À gauche: bords de contrôle (coupes transversales). À droite: surface produite à partir de ces arêtes.*

## Utilisation

1.  Assurez-vous d\'avoir au moins deux arêtes ou courbes dans l\'espace. Par exemple, ceux-ci peuvent être créés avec des outils de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> _.
2.  Appuyez sur le bouton **<img src=images/_Surface_Sections.svg style="width:16px"> [Surface sections](Surface_Sections/fr.md)**.
3.  Appuyez sur **Add edge**.
4.  Utilisez le pointeur pour sélectionner les arêtes souhaitées dans la [Vue 3D](3D_view/fr.md). Un aperçu de la forme finale sera affiché après avoir sélectionné deux arêtes valides.
5.  Appuyez sur **OK** pour terminer l\'opération.

## Options

-    **Add edge**: appuyez une fois pour commencer à choisir les arêtes dans la <img src=images/Draft_BSpline.svg style="width:Vue 3D](3D_view/fr.md). Les lignes individuelles telles que les **_** peuvent être choisies ainsi que n\'importe quelle arête des objets solides, comme celles de **[16px"> <img src=images/Part_Primitives.svg style="width:PartDesign Corps](PartDesign_Body/fr.md)** et de **[16px"> [Part Primitives](Part_Primitives/fr.md)**.

-    **Remove edge**: appuyez une fois pour commencer à choisir les arêtes dans la [Vue 3D](3D_view/fr.md). Celles-ci doivent être des arêtes précédemment sélectionnées avec **Add edge**.

-    **Bouton droit de la souris**: ouvrez le menu contextuel et sélectionnez **Remove** ou appuyez sur **Suppr** au clavier pour supprimer le bord actuellement sélectionné dans la liste.

-    **Drag**: faites glisser l\'élément actuellement sélectionné dans la liste afin de changer l\'ordre dans lequel il sera traité. La liste est traitée de haut en bas.

-   Appuyez sur **Cancel** ou **Echap** pour abandonner l\'opération en cours.

## Propriétés

_ (classe `Part::Feature` via la sous-classe `Part::Spline`). Elles partagent donc toutes les propriétés de cette dernière.

Outre les propriétés décrites dans [Part Feature](Part_Feature/fr.md), Surface Section a les propriétés suivantes dans l\'[éditeur de propriétés](property_editor/fr.md).

### Données


{{TitleProperty|Sections}}

-    {{PropertyData/fr|NSections|LinkSubList}}: une liste d\'arêtes qui seront utilisées pour construire la surface.

### Vue


{{TitleProperty|Base}}

-    {{PropertyView/fr|Control Points|Bool}}: la valeur par défaut est `False`. Mis à `True`, elle affichera une superposition avec les points de contrôle de la surface.

## Torsion de la surface 

La forme de la surface dépend de la direction des arêtes choisies. Si des arêtes sont sélectionnées et que le résultat est une surface qui \"se tord\" sur elle-même, l\'une des arêtes peut avoir besoin de sa liste de sommets dans l\'ordre inverse. Voir les informations dans **<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [Surface Remplir entre les courbes limites](Surface_GeomFillSurface/fr.md)** pour une explication plus complète.

<img alt="" src=images/Surface_twisting_example_smooth.png  style="width:330px;"> <img alt="" src=images/Surface_twisting_example_twisted.png  style="width:330px;">

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Surface Sections peut être utilisé dans des [macros](macros/fr.md) et depuis la console [Python](Python/fr.md) en ajoutant l\'objet `Surface::Sections`.

-   Les arêtes à utiliser pour définir la surface doivent être affectées en tant que [LinkSubList](LinkSubList/fr.md) à la propriété `NSections` de l\'objet.
-   Tous les objets avec des arêtes doivent être calculés avant de pouvoir être utilisés comme entrée pour les propriétés de l\'objet Sections.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pl1 = App.Placement()
obj1 = Draft.make_circle(50, placement=pl1, face=False, startangle=0, endangle=180)

pl2 = App.Placement(App.Vector(0, 0, 25), App.Rotation())
obj2 = Draft.make_circle(30, placement=pl2, face=False, startangle=0, endangle=180)

points3 = [App.Vector(18, -10, 50),
           App.Vector(12, 10, 50),
           App.Vector(-12, 10, 50),
           App.Vector(-18, -10, 50)]
obj3 = Draft.make_bspline(points3)

points4 = [App.Vector(15, -20, 100),
           App.Vector(0, 6, 100),
           App.Vector(-15, -20, 100)]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::Sections", "Surface")
surf.NSections = [(obj1, "Edge1"),
                  (obj2, "Edge1"),
                  (obj3, "Edge1"),
                  (obj4, "Edge1")]
doc.recompute()
```





{{Surface Tools navi

}}

---
[documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface Sections/fr
