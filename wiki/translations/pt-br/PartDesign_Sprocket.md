---
- GuiCommand:
   Name: PartDesign Sprocket
   MenuLocation: Part Design - Sprocket...
   Workbenches: [PartDesign](PartDesign_Workbench.md)
   Version: 0.19
---

# PartDesign Sprocket/pt-br

## Description

This tool allows you to create a 2D profile of a sprocket (or chainwheel). It can be padded with the [PartDesign Pad](PartDesign_Pad.md) feature.

## Usage

1.  Optionally activate the correct body.
2.  Go to the menu **Part Design → [<img src=images/PartDesign_Sprocket.svg style="width:16px"> Sprocket...**.
3.  Set the **Number Of Teeth** and the **Sprocket Reference**.
4.  Click **OK**.
5.  If there was no active body: drag and drop the sprocket into a body for the application of further features like padding.

## Properties

-    **Number Of Teeth**: Number of teeth

-    **Sprocket Reference**: The sprocket type. A list of sprocket definitions. <small>(v0.20)</small>  The list includes ANSI and ISO-norms as well as some bicycle and motorcycle sprocket definitions.

-    **Pitch**: Distance between two teeth

-    **Roller Diameter**: Diameter of the chain rollers the sprocket is designed for

-    **Thickness**:The principal thickness of the sprocket. **Note:** The sprocket cannot just be padded with this thickness because the teeth have side chamfers. Therefore look at the sprocket definition to model a valid 3D sprocket. <small>(v0.20)</small> 





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Sprocket/pt-br
