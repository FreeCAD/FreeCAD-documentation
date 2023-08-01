---
- GuiCommand:
   Name:Part FaceColors
   MenuLocation:Context menu - Set colors
   Workbenches:[Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md)
   SeeAlso:[Std Appearance](Std_SetAppearance.md)
---

# Part FaceColors/en

## Description

The **FaceColors** feature allows you to define a color for each face or surface of an object. This way you can assign multiple colors to one part. To color whole parts, use the [SetAppearance](Std_SetAppearance.md) feature instead.

## Usage

To color faces:

1.  Right-click on an object in the [tree view](Tree_view.md). If the object supports the *FaceColors* feature, there is a context menu entry **Set colors\...** and you can click on it.
2.  To select face(s):
    -   For a single face simply click on it.
    -   To select multiple faces:
        -   Keep **Ctrl** pressed and click on several faces.
        -   Or click the **Box selection** button in the task panel. You can then drag a selection rectangle in the [3D view](3D_view.md) with the mouse. Every face that is partly inside the rectangle will be selected.
3.  Choose a color for the selected faces in the task panel. <small>(v0.20)</small> : The color can also get a transparency by setting the *Alpha channel*.
4.  Click the **OK** button to close the task panel and accept the changes.

To reset all face colors:

1.  Click **Set to default**. This sets the colors of all faces of the part to the default color. The button works instantly, i.e. you can not revert this with the **Cancel** button.

![](images/Part_FaceColors-dialog.png ) 
*The FaceColors task panel*



---
![](images/Button_right.svg) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Command_Reference](Category_Command_Reference.md) > [Part](Part_Workbench.md) > Part FaceColors/en
