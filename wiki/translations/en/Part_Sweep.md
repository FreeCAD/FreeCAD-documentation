---
- GuiCommand   *
   Name   *Part Sweep
   MenuLocation   *Part → Sweep...
   Workbenches   *[Part](Part_Workbench.md)
   SeeAlso   *[Part Loft](Part_Loft.md)
---

# Part Sweep/en

## Description

The <img alt="" src=images/Part_Sweep.svg  style="width   *24px;"> [Part Sweep](Part_Sweep.md) tool is used to create a face, a shell, or a solid shape from one or more profiles (cross-sections) projected along a path.

The Part Sweep tool is similar to <img alt="" src=images/Part_Loft.svg  style="width   *24px;"> [Part Loft](Part_Loft.md) with the addition of a path to define the projection between profiles.

![](images/Part_Sweep_simple.png ) *A solid sweep generated from a single profile (A) projected along a path (B).*

## Usage

1.  Press the **<img src="images/Part_Sweep.svg" width=16px> '''Sweep'''** button. This opens the Sweep parameters in the [Task panel](Task_panel.md).
2.  In the *Available Profiles* left column (previously *Vertex/Edge/Wire/Face* in v0.16), click on the element to be used as sweep profile, then click on the right arrow to place it in the *Selected profiles* right column (previously *Sweep* in v0.16). Repeat if more than one profile is desired. Use the up and down arrows to reorder the selected profiles.
3.  Click on the **Sweep Path** button, then choose either mode of selection   *
    -   *Single segment selection*   * select one or more contiguous edges in the [3D view](3D_view.md) (press **CTRL** for multiple selection) and click **Done**. The sweep will only be generated along the selected edges.
    -   *Complete path selection*   * switch to the Model tab, select the 2D object to be used as path in the tree, switch back to the [Task panel](Task_panel.md) and click **Done**. The sweep will be generated along all the contiguous edges found in the 2D object.
4.  Define options [Solid](#Solid.md) and [Frenet](#Frenet.md).
5.  Click **OK**

### Accepted geometry 

-   **Profiles**   * can be a point (vertex), line (Edge), wire or face. Edges and wires may be either open or closed. There are various [profile limitations and complications](Part_Sweep#Profile_limitations_and_complications.md), see below, however the profiles may come from the Part Workbench primitives, Draft Workbench features and Sketches.

-   **Path**   * can be a line (Edge) or series of connecting lines, wire or various Part Workbench primitives, Draft Workbench features or a Sketch. The path is often selected directly from the main model window, however it can also be selected from the [Tree view](Tree_view.md) (Model Tab of [Combo View](Combo_View.md)). The path can either be an entire appropriate shape or an appropriate sub-component of a more advance shape (for example, an edge of a <img alt="" src=images/Part_Box.svg  style="width   *24px;"> [Part Box](Part_Box.md) could be selected as the path). The path may be either open or closed and will thus create either an open or closed Sweep. A closed path such as a Part Circle will result in a closed Sweep. For example a Sweep of a smaller circle around a path of a larger circle will create a torus.

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as profiles and paths. <small>(v0.20)</small> 

## Properties

### Solid

If \"Solid\" is set to \"true\", FreeCAD creates a solid, provided the profiles are of closed geometry; if set to \"false\", FreeCAD creates a face or (if more than one face) a shell for either open or closed profiles.

### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width   *500px;">

The \"Frenet\" property controls how the profile orientation changes as it follows along the sweep path. If \"Frenet\" is \"false\", the orientation of the profile is kept consistent from point to point. The resulting shape has the minimum possible twisting. Unintuitively, when a profile is swept along a helix, this results in the orientation of the profile slowly creep (rotate) as it follows the helix. Setting \"Frenet\" to true prevents such a creep.

If \"Frenet\" is \"true\" the orientation of the profile is computed basing on local curvature and tangency vectors of the path. This keeps the orientation of the profile consistent when sweeping along a helix (because curvature vector of a straight helix is always pointing to its axis). However, when path is not a helix, the resulting shape can have strange looking twists sometimes. For more information, see [Frenet Serret formulas](http   *//en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas).

### Transition

\"Transition\" sets the transition style of the Sweep at a joint in the path, if the path does not define the corner transition (for example where the path is a wire). The property is not exposed in the [Task panel](Task_panel.md) and can be found in properties after the Sweep has been created.

## Profile limitations and complications 

-   A vertex or point
    -   vertex or point may only be used as the first and/or last profile in the list of profiles.
        -   For example
            -   you can not Sweep from a circle to a point, to a ellipse.
            -   However you could Sweep from a point to a circle to an ellipse to another point.
-   Open or closed geometry profiles can not be mixed in one single Sweep
    -   In one Sweep, all profiles (lines wires etc.) must be either open or closed.
        -   For example
            -   FreeCAD can not Sweep between one Part Circle and one default Part Line.
-   Draft Workbench features
    -   Draft Workbench features can be directly used as a profile in FreeCAD 0.14 or later.
        -   For example the following Draft features can be used as profiles in a Part Sweep
            -   Draft Polygon.
            -   Draft Point, Line, wire,
            -   Draft B-spline, Bezier Curve
            -   Draft Circle, Ellipse, Rectangle
-   PartDesign Sketches
    -   The profile may be created with a sketch. However only a valid sketch will be shown in the list to be available for selection.
    -   The sketch must contain only one open or closed wire or line (can be multiple lines, if those lines are all connected as they are then a single wire)
-   Part Workbench
    -   the profile can be a valid Part geometric primitive which can be created with the [Part Primitives tool](Part_Primitives.md)
        -   For example the following Part geometric primitives can be a valid profile
            -   Point (Vertex), Line (Edge)
            -   Helix, Spiral
            -   Circle, Ellipse
            -   Regular Polygon
            -   Plane (Face)

## Links

-   Since Sweep is often used to create threads for screws, you should see [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/en
