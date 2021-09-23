---
- GuiCommand:
   Name:PartDesign SubtractivePipe
   MenuLocation:Part Design → Create a substractive feature → Subtractive pipe
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign Additive pipe](PartDesign_AdditivePipe.md), [PartDesign Subtractive loft](PartDesign_SubtractiveLoft.md)
---

# PartDesign SubtractivePipe/pt-br

## Description

**Subtractive Pipe** creates a subtractive solid in the active Body by sweeping one or more sketches (also referred to as cross-sections) along an open or closed path. Its shape is then subtracted from the existing solid. SubtractivePipe is often used in connection with [Part Helix](Part_Helix.md) and [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) to create a thread; see the [Thread for Screw Tutorial](Thread_for_Screw_Tutorial.md) for details.

## Usage

1.  Press the **<img src="images/PartDesign_SubtractivePipe.svg" width=24px> '''Subtractive pipe'''** button.
2.  In the **Select feature** dialog, select a sketch to be used as first cross-section and click **OK**.
    -   Alternatively, a single sketch can be selected prior to pressing the Subtractive pipe button.
3.  In the **Pipe parameters** under **Profile**, press the **Object** button.
4.  Select the sketch to be used as path in the 3D view:
    -   Alternatively, edges of the body can be selected by pressing **Add Edge** and selecting edges in the 3D view.
5.  To use more than one cross-section, under **Section transformation** set the Transform mode to *Multisection*; press **Add Section** then select a sketch in the 3D view. Repeat for each additional cross-section.
6.  Set options if needed and click **OK**.

## Options

**Section Transformation**:

-   Select **Constant** to use a single profile
-   Select **Multisection** to use multiple profiles

**Section Orientation**:

-   Standard
    -   This keeps the cross section shape perpendicular to the path. This is the default setting.
-   Fixed
    -   Orientation set by first profile and constant throughout. This deactivates the alignment to the path normal vector. That means that the cross-section shape will not rotate with the path. Sweep along a circle to see the effect.
-   Frenet
    -   Create minimum possible twisting of profile. For more info, see [Frenet-Serret Formulas](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)
-   Auxiliary
    -   Specify secondary path to guide pipe.
    -   For each point **P** along the sweep path, there will be a corresponding point **Q** on the auxiliary path.
    -   As the profile is swept, it will be transformed such that the **PQ** line is the normal of the sweep path.
    -   If **Curvelinear equivalence** is set, then the **Q** points are scaled proportionally along the sweep path, regardless of is length.
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
-   It is not possible to use a vertex as cross-section.
-   A cross-section cannot lie on the same plane as the one immediately preceding it.
-   To better control the shape of the pipe, it is recommended that all the cross-sections have the same number of segments. For example, for a pipe between a rectangle and a circle, the circle may be broken down into 4 connected arcs.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePipe/pt-br
