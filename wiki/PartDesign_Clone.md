---
- GuiCommand:
   Name:PartDesign Clone
   MenuLocation:Part Design → Create a clone
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[Draft Clone](Draft_Clone.md)
---

# PartDesign Clone

## Description

**PartDesign Clone** creates a linked copy of a selected object which will follow any future edits to the original object (except placement). For example, one use case is when you want to do [PartDesign Boolean](PartDesign_Boolean.md) on an object created in another workbench. Most types of objects are accepted, as long as they are single solids. If you need to clone multiple objects (i.e., bodies) or a [Part Container](Std_Part.md), you may use [Draft Workbench\'s clone](Draft_Clone.md). One caveat is that the Part Design Workbench\'s clone sets the current placement of the clone as zero (both Cartesian translation and spatial orientations). While the Draft\'s workbenches clone calculates and sets the numerical values of the current placement and orientation of the cloned objects with respect to the cloned object container.

 ![*Clone of the inner gear while being translated in 3D space as an independent object*](images/clone.png )  *Clone of the inner gear while being translated in 3D space as an independent object*

## Usage

1.  In the Model tree, select the object to be cloned.
2.  Press the **<img src=images/PartDesign_Clone.svg style="width:24px"> '''Create a clone'''** button.

## Properties

-    **Base Feature**: sets the original object the clone is based on. To replace, press the **...** button to get a list of available objects.

-    **Placement**: defines the orientation and position of the Clone in the 3D space. See [Placement](Placement.md).

-    **Label**: label given to the Clone object. Change to suit your needs.

## Limitations

-   Only a single object can be used for a PartDesign Clone.
-   Only objects that consist of a single solid are supported. Hence, [compounds](Glossary#Compound.md) like [Part container](Std_Part.md), [Part Compound](Part_Compound.md) or [Draft OrthoArray](Draft_OrthoArray.md) are not supported.




 {{PartDesign Tools navi}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Clone
