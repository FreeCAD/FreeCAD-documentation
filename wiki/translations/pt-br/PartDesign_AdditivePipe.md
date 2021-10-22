---
- GuiCommand:
   Name:PartDesign AdditivePipe
   MenuLocation:PartDesign → Create an additive feature → Additive pipe
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign Additive Loft](PartDesign_AdditiveLoft.md), [PartDesign Subtractive Pipe](PartDesign_SubtractivePipe.md)
---

# PartDesign AdditivePipe/pt-br

## Description

**Additive Pipe** creates a solid in the active Body by sweeping one or more sketches (also referred to as cross-sections) along an open or closed path. If the Body already contains features, the additive pipe will be merged to them.

![](images/PartDesign_AdditivePipe_example.svg ) 
*On the left: cross-sections (A) and (B) to be swept along path (C); resulting Additive pipe on the right.*

## Usage

The example image above shows two different cross-section shapes. The text below will describe the procedure with a single shape only. This will achieve a part with the same cross-section along the whole path.

1.  Create two separate sketches;
    -   one for the path, e.g two lines connected by a curve as in the image above,
    -   one for the cross-section shape, e.g. a circle as the first shape in the image above.
2.  **Arrange** the two shapes in 3D correctly. It is recommended to place the origin of the cross-section onto the line of the path. The two sketches should in most cases be **orthogonal**. This can be done with the \'Map Mode\' function (make both sketches visible with **Space**. Select the cross-section sketch. Select Properties/DataTab/MapMode. Click the appearing **...** button at the right side. In the Attachment Dialog select a vertex of the path sketch and select the correct mode to get the two sketches aligned correctly).
3.  Press the **<img src="images/PartDesign_AdditivePipe.svg" width=24px> [Additive pipe](PartDesign_AdditivePipe.md)** button.
4.  In the **Select feature** dialog, select a sketch to be used cross-section and click **OK**.
    -   Alternatively, the cross-section sketch can be selected prior to pressing the Additive pipe button. In that case you will not get a \"Select feature\' dialog.
5.  In the **Pipe parameters** under **Path to sweep along**, press the **Object** button.
6.  Select the sketch to be used as path in the 3D view. In this case the whole sketch will be used as path.
    -   Alternatively, single edges of the sketch can be selected by pressing **Add Edge** and selecting edges in the 3D view. Note that you must press the **Add Edge** for each edge again. You must select a continous line with no branches.
7.  The other settings should work with the default settings in most cases.
8.  Click **OK**.

To use more than one cross-section, start with the first cross-section sketch as described above. Then under **Section transformation** set the Transform mode to *Multisection*; press **Add Section** then select a sketch in the [3D view](3D_view.md). Repeat for each additional cross-section.

## Options

**Section Transformation**:

-   Select **Constant** to use a single profile
-   Select **Multisection** to use multiple profiles

**Section Orientation**:

-   Standard

    :   This keeps the cross section shape perpendicular to the path. This is the default setting.
-   Fixed
    -   Orientation set by first profile and constant throughout. This deactivates the alignment to the path normal vector. That means that the cross-section shape will not rotate with the path. Sweep along a circle to see the effect.
-   Frenet
    -   Create minimum possible twisting of profile. For more info, see [Frenet-Serret Formulas](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)
-   Auxiliary
    -   Specify secondary path to guide pipe.
    -   For each point **P** along the sweep path, there will be a corresponding point **Q** on the auxiliary path.
    -   As the profile is swept, it will be transformed such that the **PQ** line is the normal of the sweep path.
    -   If **Curvilinear** is set, then the **Q** points are scaled proportionally along the sweep path, regardless of it\'s length.
-   Binormal
    -   Specify binormal vector in X, Y and Z

**Corner Transition**

-   Transformed
-   Right
-   Rounded

## Properties

-    **Label**: name given to the operation, this name can be changed at convenience.

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

-    **Sections**: lists the sections used.

-    **Spine Tangent**: true or false (default). True extends the path to include tangent edges.

-    **Auxiliary Spine Tangent**: true or false (default). True extends the auxiliary path to include tangent edges.

-    **Auxiliary Curvelinear**: true or false (default). True calculates normal between equidistant points on both spines.

-    **Mode**: profile mode. See [Options](#Options.md).

-    **Binormal**: binormal vector for corresponding orientation mode.

-    **Transition**: transition mode. Options are *Transformed*, *Right Corner* or *Round Corner*.

-    **Transformation**: *Constant* uses a single cross-section. *Multisection* uses two or more cross-sections. *Linear*, *S-shape* and *Interpolation* are currently not functional.

## Limitations

-   Sketches used for cross-sections must form closed profiles.
-   The path can only be from a single sketch, feature or ShapeBinder. In case you want to sweep along several edges from different sketches, use a **<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [SubShapeBinder](PartDesign_SubShapeBinder.md)**.
-   The path must not contain branches or T-junctions etc. Loops are allowed.
-   It is not possible to use a vertex as cross-section.
-   It can lead to issues if the cross-section is not perpendicular to the path in 3D (some other CAD systems consider the origin of the cross-section as the path and do not require to place that sketch explicitly).
-   A cross-section cannot lie on the same plane as the one immediately preceding it.
-   To better control the shape of the pipe, it is recommended that all the cross-sections have the same number of segments. For example, for a pipe between a rectangle and a circle, the circle may be broken down into 4 connected arcs.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/pt-br
