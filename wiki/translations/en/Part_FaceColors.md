---
- GuiCommand   *
   Name   *Part FaceColors
   MenuLocation   *Context menu → Set colors
   Workbenches   *[Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md)
   SeeAlso   *[Std Appearance](Std_SetAppearance.md)
---

# Part FaceColors/en

## Description

The **FaceColors** feature allows you to define a color for each face or surface of an object. This way you can assign multiple colors to one part. To color whole parts, use instead is the feature *[SetAppearance](Std_SetAppearance.md)*.

## Usage

To color faces   *

1.  Right-click on an item in the tree view. If the items supports the *FaceColors* feature, there is a context menu entry **Set colors\...** and you can click on it.
2.  To select face(s)   *
    1.  For a single face simply click on it, then select in the dialog its color
    2.  To select multiple faces, either keep **Ctrl** pressed and click on several faces.
        Or click in the dialog on the button **Box selection**. Then you can drag with the mouse a selection rectangle in the model. Every face that is partly in the selection rectangle will be selected.
3.  Choose in the dialog a color for the selected faces. <small>(v0.20)</small>    * The color can also get a transparency by setting the *Alpha channel*.
4.  Click **OK** to close the dialog an accept the changes you made.

To reset all face colors   *

1.  Click **Set to default**. This sets the colors of all faces of the part to the default color. The button works instantly, i.e. you can not revert this with the **Cancel** button.

![](images/Part_FaceColors-dialog.png ) 
*The FaceColors dialog*





 

[Category   *User Documentation](Category_User_Documentation.md) [Category   *Command_Reference](Category_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Command_Reference](Category_Command_Reference.md) > [Part](Part_Workbench.md) > Part FaceColors/en
