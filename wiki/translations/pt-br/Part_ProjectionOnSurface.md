---
- GuiCommand:
   Name:Part ProjectionOnSurface
   MenuLocation:Part → Create projection on surface...
   Workbenches:[Part](Part_Workbench.md)
   Version:0.19
---

# Part ProjectionOnSurface/pt-br

## Description


**[<img src=images/Part_ProjectionOnSurface.svg style="width:16px"> [Part ProjectionOnSurface](Part_ProjectionOnSurface.md)**

is used to project a [Shape](Shape.md) on top of a face from another object; this can be used to project a logo or textual object (see **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Draft ShapeString](Draft_ShapeString.md)**) onto different surfaces to create interesting effects.

Given a source [Shape](Shape.md), this tool can project edges, wires (closed edges), or entire faces from it; the result can be new edges, new wires, new faces, or even new extruded solids which can be used in <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [boolean operations](Part_Boolean.md) for effects such as engraving or stamping.

<img alt="" src=images/Part_ProjectionOnSurface1.png  style="width:300px;"> <img alt="" src=images/Part_ProjectionOnSurface2.png  style="width:300px;">



*Projection of a logo on a curved surface.*

## Usage

1.  Make sure you have at least two objects in your document; the \"source\" object that you wish to project, and the \"target\" object where the projection will be made.
2.  Click on **[<img src=images/Part_ProjectionOnSurface.svg style="width:16px"> [Projection on surface](Part_ProjectionOnSurface.md)** to launch a [task panel](task_panel.md) with various options.
3.  Click on **Select projection surface**, and then click on the \"target\" surface where the projection will be created.
4.  Then click on the specific button to choose the type of subelement that you want to add to your projection object.
    -   
        **Add face**
        
        : select a source face.

    -   
        **Add wire**
        
        : select a source edge. The tool will extract the entire wire to which the edge belongs. For example, by choosing a single edge of a polygon, it will project the entire polygon.

    -   
        **Add edge**
        
        : select a source edge. The tool will only project the selected edge.

    -   Once a button is depressed, pick a subelement in the [3D view](3D_view.md). If you wish to deselect it, pick the same element again.

    -   When you are satisfied with your selection, press the same **Add...** button to leave the selection mode.
5.  Then click on the specific radiobutton to choose the type of projection shape to create.
    -   
        {{RadioButton|TRUE|Show all}}
        
        : it will show all types of closed wires and edges on the target surface. If a \"face\" subelement was selected in the previous step, a preview of a solid object extruded from the projection will be shown, depending on the value of **Extrude height**.

    -   
        {{RadioButton|TRUE|Show faces}}
        
        : it will show a preview of a filled face on the target surface. This will only work if you selected a \"face\" subelement in the previous step; if you selected a closed \"wire\", only the edges (no face) will be created as projection; if you selected \"edges\", only those edges will be created as projection.

    -   
        {{RadioButton|TRUE|Show edges}}
        
        : it will show a preview of the edges on the target surface. This will work whether you added a \"face\", \"wire\", or \"edge\" subelement in the previous step; even if you added a filled \"face\", only the edges will be created as projection.
6.  Press the **OK** to complete the operation and produce the new projection object.

Notes:

-   The projection direction is automatically taken from the camera direction in the [3D view](3D_view.md) at the moment the tool is launched.
-   To change the direction, move the camera, and press **Get current camera direction**.
-   Alternatively press the **X:**, **Y:**, or **Z:** buttons to set the projection direction to the main global axes, +X, -X, +Y, -Y, +Z, or -Z.
-   However, do notice that changing the projection direction won\'t automatically update the projection preview; in order to do this, you must re-select the geometry by pressing the **Add...** buttons and picking the subelements again.

## Options

-    **Extrude height**: it is the height of the solid shape that is created by extruding the projected face, from the target surface and along the negative of the projection direction. For example, if the projection direction is along +Y {{Value|(0, 1, 0)}}, the extrusion will be created in the direction -Y {{Value|(0, -1, 0)}}. This solid extrusion will only be created if the subelement selected was a closed face, by pressing the **Add face** button, and by choosing the {{RadioButton|TRUE|Show all}} option.

-    **Solid depth**: it is the distance that the projection object is moved along the projection direction. Negative values will displace the object in the opposite direction; this allows creating a projection that is offset from the target surface.

## Limitations

The projection algorithm sometimes is not able to create a valid projection face. If this happens a solid extrusion won\'t be able to be created either.

If this happens:

-   Check if your source face is valid; try running the **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [CheckGeometry](Part_CheckGeometry.md)** tool for clues.
-   Check if the projection direction is valid. Can the source face be realistically projected onto the target surface? Would a straight projection hit the surface? Adjust the camera so that the source face is in front of the target surface, and try again.
-   Try to use the {{RadioButton|TRUE|Show edges}} option. Are the edges projected correctly? Try to create a face with the edges by hand.

The projection done in the Part workbench is not parametric. If you need a parametric workflow, please consult with the [Projection class](https://gist.github.com/CsatiZoltan/f4fd10bf20923143ba0e0678ea1d3d61), which is a Python scripted object, intended for programmatic use.

## Links

-   Forum thread: [Project faces onto bent surface](https://forum.freecadweb.org/viewtopic.php?f=9&t=33700)

## Examples



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ProjectionOnSurface/pt-br
