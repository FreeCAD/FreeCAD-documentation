---
 GuiCommand:
   Name: PartDesign AdditivePipe
   MenuLocation: Part Design , Create an additive feature , Additive pipe
   Workbenches: PartDesign_Workbench
   Version: 0.17
   SeeAlso: PartDesign_AdditiveLoft, PartDesign_SubtractivePipe
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
    -   one for the cross-section shape, e.g. a circle as the first shape in the image above. Instead of a sketch also the face of a 3D object can be used. (<small>(v0.20)</small> )
2.  **Arrange** the two shapes in 3D correctly. It is recommended to place the origin of the cross-section onto the line of the path. The two sketches should in most cases be **orthogonal**. This can be done with the \'Map Mode\' function (make both sketches visible with **Space**. Select the cross-section sketch. Select Properties/DataTab/MapMode. Click the appearing **...** button at the right side. In the Attachment Dialog select a vertex of the path sketch and select the correct mode to get the two sketches aligned correctly.
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_AdditivePipe.svg" width=16px> [Additive pipe](PartDesign_AdditivePipe.md)** button.
    -   Select the **PartDesign → Create an additive feature → <img src="images/PartDesign_AdditivePipe.svg" width=16px> Additive pipe** option from the menu.
4.  In the **Select feature** dialog select a sketch to be used as a cross-section and click **OK**.
    -   Alternatively, a sketch or a face of a 3D object (<small>(v0.20)</small> ) can be selected before starting the tool. You will not get this dialog then.
5.  In the **Pipe parameters** under **Path to sweep along**, press the **Object** button.
6.  Select the sketch to be used as a path in the 3D view. In this case, the whole sketch will be used as a path.
    -   Alternatively, single edges of the sketch can be selected by pressing **Add Edge** and selecting edges in the 3D view. Note that you must press the **Add Edge** for each edge again. You must select a continuous line with no branches.
7.  The other settings should work with the default settings in most cases.
8.  Click **OK**.

To use more than one cross-section, start with the first cross-section sketch as described above. Then under **Section transformation** set the Transform mode to *Multisection*; press **Add Section** then select a sketch in the [3D view](3D_view.md). Repeat for each additional cross-section.

## Options

**Section Transformation**:

-   Select **Constant** to use a single profile
-   Select **Multisection** to use multiple profiles

**Section Orientation**:

-   Standard

    :   This keeps the cross-section shape perpendicular to the path. This is the default setting.
-   Fixed
    -   Orientation set by the first profile and constant throughout. This deactivates the alignment to the path normal vector. That means that the cross-section shape will not rotate with the path. Sweep along a circle to see the effect.
-   Frenet
    -   Create minimum possible twisting of profile. For more info, see [Frenet-Serret Formulas](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)
-   Auxiliary
    -   Specify secondary path to guide pipe.
    -   For each point **P** along the sweep path, there will be a corresponding point **Q** on the auxiliary path.
    -   As the profile is swept, it will be transformed such that the **PQ** line is the normal of the sweep path.
    -   If **Curvelinear equivalence** is set, then the **Q** points are scaled proportionally along the sweep path, regardless of its length.
-   Binormal
    -   Specify binormal vector in X, Y and Z

**Corner Transition**

-   Transformed
-   Right
-   Rounded

## Properties

See also: [Property editor](Property_editor.md).

A PartDesign AdditivePipe object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}

-    **Add Sub Shape|PartShape|Hidden**:

-    **Base Feature|Link|Hidden**:

-    **_Body|LinkHidden|Hidden**:


{{TitleProperty|Part Design}}

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**: reference to sketch.

-    **Midplane|Bool**: extrude symmetrically to sketch face.

-    **Reversed|Bool**: reverses extrusion direction.

-    **Up To Face|LinkSub**: face where feature will end.

-    **Allow Multi Face|Bool**: allow multiple faces in profile.


{{TitleProperty|Sweep}}

-    **Sections|LinkSubList**: lists the sections used.

-    **Spine|LinkSub**: spine (path) to sweep along.

-    **Spine Tangent|Bool**: true or false (default). True extends the spine to include tangent edges.

-    **Auxiliary Spine|LinkSub|Hidden**: secondary spine (path) to orient the Sweep.

-    **Auxiliary Spine Tangent|Bool**: true or false (default). True extends the auxiliary spine to include tangent edges.

-    **Auxiliary Curvelinear|Bool**: true or false (default). True calculates the normal between equidistant points on both spines.

-    **Mode|Enumeration**: profile mode. Options are *Fixed*, *Frenet*, *Auxiliary* or *Binormal*. See [Options](#Options.md).

-    **Binormal|Vector**: binormal vector for corresponding orientation mode.

-    **Transition|Enumeration**: transition mode. Options are *Transformed*, *Right Corner* or *Round Corner*.

-    **Transformation|Enumeration**: *Constant* uses a single cross-section. *Multisection* uses two or more cross-sections. *Linear*, *S-shape* and *Interpolation* are currently not functional.

## Notes

-   To better control the shape of the pipe, it is recommended that all cross-sections have the same number of segments. For example, for a pipe between a rectangle and a circle, the circle should be broken down into 4 connected arcs.
-   You can pipe from or toward a single [vertex](Glossary#V.md) from a sketch or the body. <small>(v0.20)</small> 
-   When you select a [vertex](Glossary#V.md) as section, it must be the last section of the pipe. Otherwise the pipe body would consist of two solids connected at a single point. This would violates the CAD kernel\'s definition of a 3D object. You can change the order of the sections by dragging them in the list.
-   The path can only be from a single sketch, feature or ShapeBinder. In case you want to sweep along several edges from different sketches, use a [SubShapeBinder](PartDesign_SubShapeBinder.md).
-   The path must not contain branches or T-junctions etc. Loops are allowed.
-   It can lead to issues if the cross-section is not perpendicular to the path in 3D.
-   A cross-section cannot lie on the same plane as the one immediately preceding it.
-   The cross-sections must not contain disjoint or crossing loops.
-   If the sketch has inner geometry, then the order in which the sketch geometry is created should be the same for all sections. Either start all sections with the inner geometry, or start them all with the outer. Otherwise an invalid pipe will be created where inner and outer walls cross.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/pt-br
