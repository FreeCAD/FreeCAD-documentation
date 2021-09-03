---
- GuiCommand:
   Name:Surface ExtendFace
   MenuLocation:Surface → Extend face
   Workbenches:[Surface](Surface_Workbench.md)
   Version:0.17
---

## Description


**<img src=images/Surface_ExtendFace.svg style="width:16px"> [Surface ExtendFace](Surface_ExtendFace.md)**

extrapolates an existing face or surface at its boundaries with its local U and V parameters.

 <img alt="" src=images/Surface_ExtendFace_base_example.png  style="width:300px;"> <img alt="" src=images/Surface_ExtendFace_example.png  style="width:300px;"> 


*Left: original face. Right: extended face.*

## Usage

1.  Make sure you have an object that has faces. The object could be created with the <img alt="" src=images/Workbench_Surface.svg  style="width:24px;"> [Surface Workbench](Surface_Workbench.md) but it could also be any other object, for example, created with <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) or <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md).
2.  Select the face to extend by clicking on it on the [3D view](3D_view.md).
3.  Press **<img src=images/Surface_ExtendFace.svg style="width:16px"> [Extend face](Surface_ExtendFace.md)**.

## Options

This command doesn\'t have any options. Either it works with the selection or not.

## Properties

A [Surface Extend](Surface_ExtendFace.md) object (`Surface::Extend` class) is derived from the basic [Part Feature](Part_Feature.md) (`Part::Feature` class, through the `Part::Spline` subclass), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the Surface Filling has the following properties in the [property editor](Property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Face|LinkSub**: the subelement from an object that will be extended; it must be a face.

-    **Tolerance|FloatConstraint**: it defaults to {{Value|0.1}}.

-    **Extend UNeg|FloatConstraint**: it defaults to {{Value|0.05}}. The ratio of the local U parameter that will be extended in the negative direction.

-    **Extend UPos|FloatConstraint**: it defaults to {{Value|0.05}}. The ratio of the local U parameter that will be extended in the positive direction.

-    **Extend USymetric|Bool**: it defaults to `True`, in which case **Extend UNeg** and **Extend UPos** will have the same value.

-    **Extend VNeg|FloatConstraint**: it defaults to {{Value|0.05}}. The ratio of the local V that will be extended in the negative direction.

-    **Extend VPos|FloatConstraint**: it defaults to {{Value|0.05}}. The ratio of the local V direction that will be extended in the positive direction.

-    **Extend VSymetric|Bool**: it defaults to `True`, in which case **Extend VNeg** and **Extend VPos** will have the same value.

-    **SampleU|IntegerConstraint**: it defaults to {{Value|32}}.

-    **SampleV|IntegerConstraint**: it defaults to {{Value|32}}.

### View


{{TitleProperty|Base}}

-    **Control Points|Bool**: it defaults to `False`; if set to `True`, it will show an overlay with the control points of the surface.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Surface Extend tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by adding the `Surface::Extend` object.

-   The face to extend must be assigned as a [LinkSub](LinkSub.md) to the `Face` property of the object. It must contain only a single face.

 
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




 {{Surface Tools navi}} 
