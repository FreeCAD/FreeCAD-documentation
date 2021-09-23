# Body/pt-br
## Introdução

In FreeCAD the word \"[Body](Body.md)\" is normally used to refer to a [PartDesign Body](PartDesign_Body.md) object (`PartDesign::Body` class) that is defined by the [PartDesign Workbench](PartDesign_Workbench.md). This is a container object that can hold [2D sketches](Sketch.md) and [3D geometrical features](PartDesign_Feature.md) to build a solid shape.

See [PartDesign Body](PartDesign_Body.md) for more information about this type of object.

## Utilização

1.  Switch to the [PartDesign Workbench](PartDesign_Workbench.md).
2.  Press **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**.
3.  Press **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)** to create a new [sketch](Sketch.md).
4.  Create a closed wire, and then use **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)** to extrude the sketch, and create an initial solid.
5.  Add more sketches and pads, and use other tools of the [PartDesign Workbench](PartDesign_Workbench.md) to modify and transform the initial solid.

Alternatively, instead of using <img src=images/PartDesign_AdditiveBox.svg style="width:sketches](Sketch.md), you can add primitive [PartDesign Features](PartDesign_Feature.md), for example, a **[16px"> [PartDesign Additive box](PartDesign_AdditiveBox.md)**. Any number of additive and subtractive features can be used to create a final volume.

## Notas

A Body is required when using the [PartDesign Workbench](PartDesign_Workbench.md) in a [feature editing](feature_editing.md) methodology.

A Body is not required when using the [Part Workbench](Part_Workbench.md), as this workbench uses a [constructive solid geometry](constructive_solid_geometry.md) workflow, which is based on [primitive shapes](Part_Primitives.md) and boolean operations.


{{PartDesign Tools navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)

---
[documentation index](../README.md) > [Glossary](Category:Glossary.md) > Body/pt-br
