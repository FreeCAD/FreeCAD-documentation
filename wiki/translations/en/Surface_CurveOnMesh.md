---
- GuiCommand   *
   Name   *Surface CurveOnMesh
   MenuLocation   *Surface → Curve on mesh
   Workbenches   *[Surface](Surface_Workbench.md)|
   Version   *0.17
---

# Surface CurveOnMesh/en

## Description


**[<img src=images/Surface_CurveOnMesh.svg style="width   *16px"> [Surface CurveOnMesh](Surface_CurveOnMesh.md)**

creates approximated spline segments on top of a selected [mesh](Mesh_Workbench.md).

If the object is not a [Mesh](Mesh.md), but a parametric [Shape](Shape.md) or surface, it must be converted first to a mesh using **[<img src=images/Mesh_FromPartShape.svg style="width   *16px"> [Mesh FromPartShape](Mesh_FromPartShape.md)**.

These edges created on top of the mesh may be further used to re-create the surface in a parametric way by using tools such as **[<img src=images/Surface_GeomFillSurface.svg style="width   *16px"> [GeomFillSurface](Surface_GeomFillSurface.md)** and **[<img src=images/Surface_Sections.svg style="width   *16px"> [Sections](Surface_Sections.md)**.

![](images/Surface_CurveOnMesh_mesh_example.png ) ![](images/Surface_CurveOnMesh_example.png )

![](images/Surface_CurveOnMesh_surface_example.png )



*Above left   * mesh object with selected points on the surface. Above right   * splines created by picking several points on the mesh. Lower left   * a parametric surface reconstructed from the approximated splines, using [Surface Sections](Surface_Sections.md).*

## Usage

1.  Make sure you have a [mesh object](Mesh.md). This can be created by the <img alt="" src=images/Workbench_Mesh.svg  style="width   *24px;"> [Mesh Workbench](Mesh_Workbench.md), or by importing a mesh file type, like STL, [OBJ](Arch_OBJ.md), or [DAE](Arch_DAE.md). If a solid object or solid file type (STEP) is used, it can be converted to a mesh using **[<img src=images/Mesh_FromPartShape.svg style="width   *16px"> [Mesh FromPartShape](Mesh_FromPartShape.md)**.
2.  Press **[<img src=images/Surface_CurveOnMesh.svg style="width   *16px"> [Curve on mesh](Surface_CurveOnMesh.md)**.
3.  Press **Start**.
4.  Using the mouse pointer, pick points on the surface of the mesh in the [3D view](3D_view.md); pick as many points as necessary to draw a smooth preview line.
5.  When enough points have been added, right click on the [3D view](3D_view.md) to open the context menu, and select **Create**. Depending on how smooth the original mesh is, one spline or multiple splines will be created in the [tree view](tree_view.md).
6.  Repeat the sequence **Start** → Pick → **Create**, to add more approximated splines.
7.  The new spline will be created, and will appear in the [tree view](Tree_view.md), immediately after choosing **Create**; the [task panel](Task_panel.md) will remain active.
8.  Press **Close** to close the [task panel](Task_panel.md), and terminate the command completely.

After pressing **Start**, the context menu (right-click) in the [3D view](3D_view.md) shows various options beside **Create**.

-    **Close wire**   * if at least three points have been picked, this option will be available to join the last point to the first point with a line.

-    **Clear**   * it will erase the tentative points that have been picked on the mesh, and will allow you to pick new ones.

-    **Cancel**   * it will erase the tentative points that have been picked, and will stop the picking operation. Press **Start** again to pick points once more.

## Options


**(Editor   * this information must be verified)**


**Wire**

section   *

-    **Snap tolerances to vertices**   * it defaults to {{Value|10 px}}; it indicates the minimum distance between one point and another when picking with the pointer.

-    **Split threshold**   * it defaults to {{Value|45 deg}}; it indicates the angular deviation from one point in the mesh to another point necessary to create a new spline instead of extending the previous spline.


**Spline approximation**

, if it is {{CheckBox|TRUE|checked}}, it will create spline objects, otherwise, it will create simple straight line objects (polyline).

-    **Tolerance to mesh**   * it defaults to {{Value|0.2}}. It is a parameter that takes into account the imperfections of the mesh; the smaller this number the more precise it will consider the mesh, particularly if it is a very fine mesh.

-    **Continuity**   * it defaults to {{Value|C2}}. It determines the continuity of the spline; it can be {{Value|C0}} (touching), {{Value|C1}} (tangent), {{Value|C2}} (curvature), and {{Value|C3}} (acceleration curvature).

-    **Maximum curve degree**   * it defaults to {{Value|5}}. It determines the maximum degree of the spline to approximate the surface; it can be a value from {{Value|1}} to {{Value|8}}.

## Properties

If {{CheckBox|FALSE|Spline approximation}} is unchecked, the [Curve on mesh](Surface_CurveOnMesh.md) tool creates a basic [Part Feature](Part_Feature.md).

If {{CheckBox|TRUE|Spline approximation}} is checked, the [Curve on mesh](Surface_CurveOnMesh.md) tool creates a **[<img src=images/Part_Spline.svg style="width   *16px"> [Part Spline](Part_Spline.md)** (`Part   *   *Spline` class) which is derived from the basic [Part Feature](Part_Feature.md) (`Part   *   *Feature` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the Part Spline has the following properties in the [property editor](Property_editor.md).

### View


{{TitleProperty|Base}}

-    **Control Points|Bool**   * it defaults to `False`; if set to `True`, it will show an overlay with the control points of the surface.





{{Surface Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface CurveOnMesh/en
