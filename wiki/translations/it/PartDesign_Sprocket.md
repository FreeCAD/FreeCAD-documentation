---
- GuiCommand:
   Name:PartDesign Sprocket
   MenuLocation:Part Design → Sprocket...
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.19
---

## Description

This tool allows you to create a 2D profile of a sprocket. It can be padded with the [PartDesign Pad](PartDesign_Pad.md) feature.

## Usage

1.  Go to the menu **Part Design → <img src=images/PartDesign_Sprocket.svg style="width:24px"> Sprocket...**.
2.  Set the **Number Of Teeth** and the **Sprocket Reference**.
3.  Click **OK**
4.  If the sprocket gear is created outside of the active body, drag and drop it into a body for the application of further features like padding.

## Properties

-    **Number Of Teeth**: Number of teeth

-    **Sprocket Reference**: The sprocket type. A list of sprocket definitions. <small>(v0.20)</small>  The list includes ANSI and ISO-norms as well as some bicycle and motorcycle sprocket definitions.

-    **Pitch**: Distance between two teeth

-    **Roller Diameter**: Diameter of the chain rollers the sprocket is designed for

-    **Thickness**:The principal thickness of the sprocket. **Note:** The sprocket cannot just be padded with this thickness because the teeth have side chamfers. Therefore look at the sprocket definition to model a valid 3D sprocket. <small>(v0.20)</small> 





{{PartDesign Tools navi

}} 