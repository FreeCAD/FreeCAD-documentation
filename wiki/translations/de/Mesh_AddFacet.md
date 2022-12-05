---
- GuiCommand:
   Name:Mesh AddFacet
   MenuLocation:Meshes → Add triangle
   Workbenches:[Mesh](Mesh_Workbench.md)
   SeeAlso:[Mesh FillupHoles](Mesh_FillupHoles.md), [Mesh FillInteractiveHole](Mesh_FillInteractiveHole.md)
---

# Mesh AddFacet/de

## Beschreibung

The **Mesh AddFacet** command adds faces along a boundary of an open mesh object. It can be used to fill holes.

## Anwendung

1.  During the command edit mode will be active. In this mode it is impossible to rotate or pan the [3D view](3D_view.md), although zooming still works. But you can temporarily switch out of edit mode with the [Std ToggleNavigation](Std_ToggleNavigation.md) command should you need to change the view.
2.  Select a single open mesh object.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_AddFacet.svg" width=16px> [Mesh AddFacet](Mesh_AddFacet.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_AddFacet.svg" width=16px> Add triangle** option from the menu.
4.  If you hover over a vertex along a boundary of the mesh a yellow marker will appear and a left-click will select it.
5.  Select two additional points to define a triangular face. The order of the three points, clockwise or counterclockwise, determines the direction of the normal of the face.
6.  A menu pops up with the following options:
    -   
        **Add triangle**
        
        : adds the face to the mesh.

    -   
        **Flip normal**
        
        : flips the normal of the face. After selecting this option a left-click will again show the menu.

    -   
        **Clear**
        
        : removes the selected points.
7.  Optionally add more faces.
8.  Choose **Finish** from the 3D view contex menu to finish the command.

## Hinweise

-   For a clear indication of the orientation of the faces of mesh objects make sure the **Lighting** property of the mesh objects is set to {{Value|One side}}. The color of the back side of their faces will then depend on the backlight settings: **Edit → Preferences... → Display → 3D View → Backlight color - Intensity**. See: [Preferences Editor](Preferences_Editor#3D_View.md).





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh AddFacet/de
