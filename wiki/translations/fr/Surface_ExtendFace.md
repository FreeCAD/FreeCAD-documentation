---
- GuiCommand:/fr
   Name:Surface ExtendFace
   Name/fr:Surface Extension de surface
   MenuLocation:Surface → Extend face
   Workbenches:[Surface](Surface_Workbench/fr.md)
   Version:0.17
---

# Surface ExtendFace/fr

## Description


**<img src=images/Surface_ExtendFace.svg style="width:16px"> [Surface ExtendFace](Surface_ExtendFace/fr.md)**

extrapole une face ou une surface existante à ses limites avec ses paramètres U et V locaux.

<img alt="" src=images/Surface_ExtendFace_base_example.png  style="width:300px;"> <img alt="" src=images/Surface_ExtendFace_example.png  style="width:300px;">



*À gauche: surface d'origine. À droite: surface étendu.*

## Utilisation

1.  Assurez-vous que vous avez un objet qui a des faces. L\'objet peut être créé avec l\'<img alt="" src=images/Workbench_Surface.svg  style="width:24px;"> _ ou <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md).
2.  Sélectionnez la face à étendre en cliquant dessus dans la [Vue 3D](3D_view/fr.md).
3.  Appuyez sur **<img src=images/Surface_ExtendFace.svg style="width:16px"> [Extend face](Surface_ExtendFace/fr.md)**.

## Options

Cette commande n\'a pas d\'options. Soit cela fonctionne avec la sélection, soit non.

## Propriétés

_ (classe `Part::Feature` via la sous-classe `Part::Spline`). Elles partagent donc toutes les propriétés de cette dernière.

Outre les propriétés décrites dans [Part Feature](Part_Feature/fr.md), Surface Remplissage a les propriétés suivantes dans l\'[éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Face|LinkSub}}: le sous-élément d\'un objet qui sera étendu; ce doit être une face.

-    {{PropertyData/fr|Tolerance|FloatConstraint}}: la valeur par défaut est {{Value|0.1}}.

-    {{PropertyData/fr|Extend UNeg|FloatConstraint}}: la valeur par défaut est {{Value|0.05}}. Le rapport du paramètre U local qui sera étendu dans le sens négatif.

-    {{PropertyData/fr|Extend UPos|FloatConstraint}}: la valeur par défaut est {{Value|0.05}}. Le rapport du paramètre U local qui sera étendu dans le sens positif.

-    {{PropertyData/fr|Extend USymetric|Bool}}: il vaut par défaut `True`, auquel cas {{PropertyData/fr|Extend UNeg}} et {{PropertyData/fr|Extend UPos}} auront la même valeur.

-    {{PropertyData/fr|Extend VNeg|FloatConstraint}}: la valeur par défaut est {{Value|0.05}}. Le rapport du V local qui sera étendu dans la direction négative.

-    {{PropertyData/fr|Extend VPos|FloatConstraint}}: il vaut par défaut {{Value|0.05}}. Le rapport de la direction V locale qui sera étendue dans la direction positive.

-    {{PropertyData/fr|Extend VSymetric|Bool}}: il est par défaut `True`, auquel cas {{PropertyData/fr|Extend VNeg}} et {{PropertyData/fr|Extend VPos}} auront la même valeur.

-    {{PropertyData/fr|SampleU|IntegerConstraint}}: par défaut {{Value|32}}.

-    {{PropertyData/fr|SampleV|IntegerConstraint}}: par défaut {{Value|32}}.

### Vue


{{TitleProperty|Base}}

-    {{PropertyView/fr|Control Points|Bool}}: la valeur par défaut est `False`. Mis à `True`, elle affichera une superposition avec les points de contrôle de la surface.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Surface Extend peut être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en ajoutant l\'objet `Surface::Extend`.

-   La face à étendre doit être affectée en tant que [LinkSub](LinkSub/fr.md) à la propriété `Face` de l\'objet. Il ne doit contenir qu\'une seule surface.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

a = App.Vector(-20, -20, 0)
b = App.Vector(-18, 25, 0)
c = App.Vector(60, 26, 0)
d = App.Vector(33, -20, 0)

points = [a, App.Vector(-20, -8, 0), b, c,
          App.Vector(37, 4, 0), d,
          App.Vector(-2, -18, 0), a]
obj = Draft.make_bspline(points)
doc.recompute()

if App.GuiUp:
    obj.ViewObject.Visibility = False

surf = doc.addObject("Surface::Filling", "Surface")
surf.BoundaryEdges = [(obj, "Edge1")]
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
surf_extended = doc.addObject("Surface::Extend", "Surface")
surf_extended.Face = [surf, "Face1"]
doc.recompute()
```





{{Surface Tools navi

}}

---
[documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface ExtendFace/fr
