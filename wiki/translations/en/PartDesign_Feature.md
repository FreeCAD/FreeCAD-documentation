# PartDesign Feature/en
## Introduction

A [PartDesign Feature](PartDesign_Feature.md) refers to a \"step\" in the modelling process that happens inside of a [PartDesign Body](PartDesign_Body.md). For example, each time you add a solid box with [PartDesign AdditiveBox](PartDesign_AdditiveBox.md), you add a feature; when you add a chamfer to an edge with [PartDesign Chamfer](PartDesign_Chamfer.md), you add another feature; when you cut a hole using a [sketch](Sketch.md) and [PartDesign Pocket](PartDesign_Pocket.md), you add another feature.

<img alt="" src=images/PartDesign_Feature_example.png  style="width:600px;"> 
*Feature editing in a [PartDesign Body](PartDesign_Body.md) with three sequential features.*

There are many types of features which can add or remove volume from an initial solid. The word \"feature\" refers to the operation itself, and also to the resulting solid after that operation.

To learn more about creating solid objects with the [PartDesign Workbench](PartDesign_Workbench.md) see [feature editing](feature_editing.md).

## Usage

Almost all tools in the [PartDesign Workbench](PartDesign_Workbench.md) are meant to add features to a [PartDesign Body](PartDesign_Body.md). These tools can be accessed from the menu and toolbar buttons while an object or sub-element (vertex, edge, face) is selected.

The features can be placed in different categories:

-   Feature base: refers to the Base Feature object that can be created in a [PartDesign Body](PartDesign_Body.md).
-   Additive and subtractive
    -   Primitive shapes: [Box](PartDesign_AdditiveBox.md), [Cone](PartDesign_AdditiveCone.md), [Cylinder](PartDesign_AdditiveCylinder.md), [Ellipsoid](PartDesign_AdditiveEllipsoid.md), [Prism](PartDesign_AdditivePrism.md), [Sphere](PartDesign_AdditiveSphere.md), [Torus](PartDesign_AdditiveTorus.md), and [Wedge](PartDesign_AdditiveWedge.md).
    -   Primitive shapes subtractive: [Subtractive Box](PartDesign_SubtractiveBox.md), [Subtractive Cone](PartDesign_SubtractiveCone.md), [Subtractive Cylinder](PartDesign_SubtractiveCylinder.md), [Subtractive Ellipsoid](PartDesign_SubtractiveEllipsoid.md), [Subtractive Prism](PartDesign_SubtractivePrism.md), [Subtractive Sphere](PartDesign_SubtractiveSphere.md), [Subtractive Torus](PartDesign_SubtractiveTorus.md), and [Subtractive Wedge](PartDesign_SubtractiveWedge.md).
    -   Profile based: [Pad](PartDesign_Pad.md), [Revolution](PartDesign_Revolution.md), [Loft](PartDesign_AdditiveLoft.md), [Pipe](PartDesign_AdditivePipe.md).
    -   Profile based subtractive: [Pocket](PartDesign_Pocket.md), [Hole](PartDesign_Hole.md), [Groove](PartDesign_Groove.md), [Subtractive Loft](PartDesign_SubtractiveLoft.md), [Subtractive Pipe](PartDesign_SubtractivePipe.md).
-   [Boolean](PartDesign_Boolean.md), including fuse, cut, and common.
-   Dress up
    -   [Chamfer](PartDesign_Chamfer.md)
    -   [Draft](PartDesign_Draft.md)
    -   [Fillet](PartDesign_Fillet.md)
    -   [Thickness](PartDesign_Thickness.md)
-   Transform
    -   [Linear pattern](PartDesign_LinearPattern.md)
    -   [Mirrored](PartDesign_Mirrored.md)
    -   [Multi-transformed](PartDesign_MultiTransform.md)
    -   [Polar pattern](PartDesign_PolarPattern.md)
    -   [Scaled](PartDesign_Scaled.md)

## Inheritance

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `PartDesign::Feature* objects are used to build parametric 3D solids, and thus are derived from the basic {{incode|Part::Feature` object.}}

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects from the [Python console](Python_console.md).

See [PartDesign Body](PartDesign_Body.md) for the general information on adding a Body. Once a Body exists, features can be attached to it using the Body\'s `addObject()` method.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject('PartDesign::Body', 'Body')
obj.Label = "Custom label"

feature = App.ActiveDocument.addObject('PartDesign::AdditiveBox', 'Box')
feature.Width = 200
feature.Length = 300
feature.Height = 500
obj.addObject(feature)
App.ActiveDocument.recompute()

feature2 = App.ActiveDocument.addObject('PartDesign::SubtractiveBox', 'Box')
feature2.Width = 50
feature2.Length = 200
feature2.Height = 400
obj.addObject(feature2)
App.ActiveDocument.recompute()
```


{{PartDesign Tools navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Feature/en
