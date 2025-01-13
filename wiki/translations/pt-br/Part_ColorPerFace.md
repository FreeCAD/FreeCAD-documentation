---
 GuiCommand:
   Name: Part ColorPerFace
   MenuLocation: View , Color per face
   Workbenches: Part_Workbench, PartDesign_Workbench
   SeeAlso: Std_SetAppearance
---

# Part ColorPerFace/pt-br

## Description

The **Part ColorPerFace** command sets the display properties of selected faces. To change a whole object use [Std SetAppearance](Std_SetAppearance.md) instead.

This page has been updated for version 1.0.

![](images/Part_ColorPerFace_Taskpanel.png ) 
*The Set appearance per face task panel*

## Usage

1.  Select a single object.
2.  There are several ways to invoke the command:
    -   If the [Part Workbench](Part_Workbench.md) is active: press the **<img src="images/Part_ColorPerFace.svg" width=16px> [Color per face](Part_ColorPerFace.md)** button.
    -   Select the **View → <img src="images/Part_ColorPerFace.svg" width=16px> Color per face** option from the menu.
    -   Select the **<img src="images/Part_ColorPerFace.svg" width=16px> Set appearance per face...** option from the [Tree view](Tree_view.md) context menu.
3.  The **Set appearance per face** task panel opens.
4.  Select one or more faces:
    -   Hold down **Ctrl** to select mutliple faces.
    -   Optionally press the **Box selection** button, click in an empty area and drag a rectangle to select all faces belonging to the object that are (partially) inside the rectangle. Multiple box selections can be specified.
5.  Do one of the following:
    -   Select a material from the list.
        1.  Optionally press the **Launch editor** button to launch the [Materials editor](Materials_Edit.md).
    -   Specify a **Custom appearance**:
        1.  Press the **...** button.
        2.  The **Material properties** dialog box opens:
            ![](images/Material_Properties_Dialog.png )
        3.  These properties can be edited:
            -   **Ambient color**: color of the shadows on the object.
            -   **Diffuse color**: actual/base color of the object.
            -   **Emissive color**: color of the light radiating from the object.
            -   **Specular color**: color of the highlight (reflection) on a shiny surface of the object.
            -   **Shininess**
            -   **Transparency**
        4.  Optionally press the **Reset** button to change the appearance to that defined by the material.
        5.  Optionally press the **Default** button to change the appearance to match the current [preferences](PartDesign_Preferences#Shape_appearance.md).
        6.  Press the **Close** button when done.
    -   Press the **Set to default** button to change the appearance to that defined by the material.
6.  Optionally select one or more new faces whose properties you want to change.
7.  Press the **OK** button to close the task panel and finish the command.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ColorPerFace/pt-br
