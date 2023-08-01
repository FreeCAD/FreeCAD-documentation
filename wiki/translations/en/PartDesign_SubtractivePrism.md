---
- GuiCommand:
   Name:PartDesign SubtractivePrism
   MenuLocation:Part Design - Create a subtractive primitive - Subtractive Prism
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign CompPrimitiveSubtractive](PartDesign_CompPrimitiveSubtractive.md), [PartDesign AdditivePrism](PartDesign_AdditivePrism.md)
---

# PartDesign SubtractivePrism/en

## Description

Inserts a subtractive prism in the active Body. Its shape is subtracted from the existing solid.

![](images/PartDesign_SubtractivePrism_example.svg )

*On the left: active body (A) shown in grey and subtractive prism (B) shown in transparent red; result on the right.*

## Usage

1.  Press the **<img src="images/PartDesign_SubtractivePrism.svg" width=24px> '''Subtractive Prism'''** button. **Note**: the Subtractive Prism is part of an icon menu labelled *Create an subtractive primitive*. After launching FreeCAD, the Subtractive Box is the one displayed in the toolbar. To get the Prism, click on the down arrow besides the visible icon and select Subtractive Prism in the menu.
2.  Set the Primitive parameters and [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  A Prism feature appears under the active Body.

## Options

It is possible to create skewed prisms by specifying angles in respect to the normal vector of the chosen attachment.

The Prism can be edited after its creation in two ways:

-   Double-clicking it in the Model tree, or by right-clicking and selecting **Edit primitive** in the contextual menu; this brings up the Primitive parameters.
-   Via the [Property editor](Property_editor.md).

## Properties

-    **Attachment**: defines the attachment mode as well as the Attachment Offset. See [Part EditAttachment](Part_EditAttachment.md).

-    **Label**: label given to the Prism object. Change to suit your needs.

-    **Polygon**: number of sides in the polygon cross-section of the prism.

-    **Circumradius**: [circumscribed radius](https://en.wikipedia.org/wiki/Circumscribed_circle) of the polygon cross-section of the prism.

-    **Height**: height of the prism.

-    **First Angle**: angle in first direction.

-    **Second Angle**: angle in second direction.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePrism/en
