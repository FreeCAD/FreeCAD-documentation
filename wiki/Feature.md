# Feature
## Introduction

In FreeCAD the word \"_. This is an operation or modelling step performed to create or modify a solid [Shape](Shape.md) following the [feature editing](feature_editing.md) paradigm.

See [PartDesign Feature](PartDesign_Feature.md) for more information about this type of object.

## Usage

1.  Switch to the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md).
2.  Press **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**.
3.  Press **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)** to create a new [Sketch](Sketch.md).
4.  Create a closed wire, and then use **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)** to extrude the sketch, and create an initial solid. This initial solid is the initial Feature.
5.  Add more sketches and pads, and use other tools of the [PartDesign Workbench](PartDesign_Workbench.md) to modify and transform the initial solid. Each of these steps correspond to Features of the [Body](Body.md).
6.  Alternatively, add primitive objects, like **<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> <img src=images/PartDesign_SubtractiveCylinder.svg style="width:PartDesign Additive box](PartDesign_AdditiveBox.md)** and **[16px"> [PartDesign Subtractive cylinder](PartDesign_SubtractiveCylinder.md)**. Any number of additive and subtractive steps are Features that are used to create a final volume.

## Notes

In the general sense, a \"Feature\" can be any modelling step used to create a final [Shape](Shape.md), with any tool of any [workbench](Workbenches.md).

-   For example, in the <img src=images/Part_Fuse.svg style="width:Part Workbench](Part_Workbench.md), in the _**, **[16px"> <img src=images/Part_Common.svg style="width:Part Cut](Part_Cut.md)**, or **[16px"> [Part Common](Part_Common.md)**.

In a more specific sense, a \"Feature\" is a modelling step used inside a [PartDesign Body](PartDesign_Body.md).

-   For example, **<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> <img src=images/PartDesign_AdditiveLoft.svg style="width:PartDesign Additive cylinder](PartDesign_AdditiveCylinder.md)**, **_**, **[16px"> [PartDesign Subtractive cone](PartDesign_SubtractiveCone.md)**, etc., are all \"Features\".

 {{PartDesign Tools navi}}  {{Document objects navi}} 

_

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Feature
