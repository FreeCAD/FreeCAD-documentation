---
- GuiCommand:
   Name:PartDesign SubtractiveCylinder
   MenuLocation:Part Design → Create a subtractive primitive → Subtractive Cylinder
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[Create a subtractive primitive](PartDesign_CompPrimitiveSubtractive.md), [Additive Cylinder](PartDesign_AdditiveCylinder.md)
---

## Description

Inserts a subtractive cylinder in the active Body. Its shape is subtracted from the existing solid.

![](images/PartDesign_SubtractiveCylinder_example.svg )

*On the left: active body (A) shown in grey and subtractive cylinder (B) shown in transparent red; result on the right.*

## Usage

1.  Press the **<img src="images/PartDesign_SubtractiveCylinder.svg" width=24px> '''Subtractive Cylinder'''** button. **Note**: the Subtractive Cylinder is part of an icon menu labelled *Create an subtractive primitive*. After launching FreeCAD, the Subtractive Box is the one displayed in the toolbar. To get to the Cylinder button, click on the down arrow besides the visible icon and select Subtractive cylinder in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Cylinder feature appears under the active Body.

## Options

It is possible to create skewed prisms by specifying angles in respect to the normal vector of the chosen attachment. <small>(v0.20)</small> 

The Cylinder can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: label given to the Cylinder object. Change to suit your needs.

-    **Radius**: the radius value of the cylinder.

-    **Angle**: angle of rotation of the cross section (360 degrees forms a full cylinder).

-    **Height**: the length of the cylinder along its axis.

-    **First Angle**: angle in first direction. <small>(v0.20)</small> 

-    **Second Angle**: angle in second direction. <small>(v0.20)</small> 





{{PartDesign Tools navi

}}  
