# Surface CurveOnMesh/it
---
- GuiCommand:   Name: Surface CurveOnMesh   Name/it: CurveOnMesh   MenuLocation: Surface - Curve on mesh...   Workbenches: [Surface](Surface_Workbench/it.md)|---



## Descrizione


**[<img src=images/Surface_CurveOnMesh.svg style="width:16px"> [Surface CurveOnMesh](Surface_CurveOnMesh.md)**

creates approximated spline segments on top of a selected [mesh](Mesh_Workbench.md).

If the object is not a [Mesh](Mesh.md), but a parametric [Shape](Shape.md) or surface, it must be converted first to a mesh using **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Mesh FromPartShape](Mesh_FromPartShape.md)**.

These edges created on top of the mesh may be further used to re-create the surface in a parametric way by using tools such as **[<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [GeomFillSurface](Surface_GeomFillSurface.md)** and **[<img src=images/Surface_Sections.svg style="width:16px"> [Sections](Surface_Sections.md)**.

![](images/Surface_CurveOnMesh_mesh_example.png ) ![](images/Surface_CurveOnMesh_example.png )

![](images/Surface_CurveOnMesh_surface_example.png )



*Above left: mesh object with selected points on the surface. Above right: splines created by picking several points on the mesh. Lower left: a parametric surface reconstructed from the approximated splines, using [Surface Sections](Surface_Sections.md).*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare **Surface → Curve on mesh\...** nel menu.
2.  Passaggi secondo le esigenze.
3.  Impostare le opzioni e premere **OK**.


</div>

After pressing **Start**, the context menu (right-click) in the [3D view](3D_view.md) shows various options beside **Create**.

-    **Close wire**: if at least three points have been picked, this option will be available to join the last point to the first point with a line.

-    **Clear**: it will erase the tentative points that have been picked on the mesh, and will allow you to pick new ones.

-    **Cancel**: it will erase the tentative points that have been picked, and will stop the picking operation. Press **Start** again to pick points once more.



## Opzioni


**(Editor: this information must be verified)**


**Wire**

section:

-    **Snap tolerances to vertices**: it defaults to {{Value|10 px}}; it indicates the minimum distance between one point and another when picking with the pointer.

-    **Split threshold**: it defaults to {{Value|45 deg}}; it indicates the angular deviation from one point in the mesh to another point necessary to create a new spline instead of extending the previous spline.


**Spline approximation**

, if it is {{CheckBox|TRUE|checked}}, it will create spline objects, otherwise, it will create simple straight line objects (polyline).

-    **Tolerance to mesh**: it defaults to {{Value|0.2}}. It is a parameter that takes into account the imperfections of the mesh; the smaller this number the more precise it will consider the mesh, particularly if it is a very fine mesh.

-    **Continuity**: it defaults to {{Value|C2}}. It determines the continuity of the spline; it can be {{Value|C0}} (touching), {{Value|C1}} (tangent), {{Value|C2}} (curvature), and {{Value|C3}} (acceleration curvature).

-    **Maximum curve degree**: it defaults to {{Value|5}}. It determines the maximum degree of the spline to approximate the surface; it can be a value from {{Value|1}} to {{Value|8}}.



## Proprietà


<div class="mw-translate-fuzzy">

-    **Property**:

-    **Property**:


</div>

If {{CheckBox|TRUE|Spline approximation}} is checked, the [Curve on mesh](Surface_CurveOnMesh.md) tool creates a **[<img src=images/Part_Spline.svg style="width:16px"> [Part Spline](Part_Spline.md)** (`Part::Spline` class) which is derived from the basic [Part Feature](Part_Feature.md) (`Part::Feature` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the Part Spline has the following properties in the [property editor](Property_editor.md).

### View


{{TitleProperty|Base}}

-    **Control Points|Bool**: it defaults to `False`; if set to `True`, it will show an overlay with the control points of the surface.





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface CurveOnMesh/it
