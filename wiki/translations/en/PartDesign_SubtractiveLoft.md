---
- GuiCommand:
   Name:PartDesign SubtractiveLoft
   MenuLocation:Part Design → Create a substractive feature → Subtractive loft
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
   SeeAlso:[PartDesign Additive loft](PartDesign_AdditiveLoft.md), [PartDesign Subtractive pipe](PartDesign_SubtractivePipe.md)
---

# PartDesign SubtractiveLoft/en

## Description

**Subtractive Loft** creates a subtractive solid in the active Body by making a transition between two or more sketches (also referred to as cross-sections). Its shape is then subtracted from the existing solid.

## Usage

### Dialog-based workflow 

1.  Press the **<img src=images/PartDesign_SubtractiveLoft.svg style="width:24px"> [Subtractive loft](PartDesign_SubtractiveLoft.md)** button.
2.  In the **Select feature** dialog, select a sketch to be used as base profile object and click **OK**.
    -   Alternatively, either a single sketch or the face of a 3D object (<small>(v0.20)</small> ) can be selected prior to pressing the subtractive loft button.
3.  In the **Loft parameters**, press the **Add Section** button.
4.  Select the next sketch in the [3D view](3D_view.md). Repeat to select more sketches in the order you want them to be lofted through. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
5.  Set options if needed and click **OK**.

### Selection-based workflow 


<small>(v0.19)</small> 

1.  Select several sketches. It is hereby important in what order you select them:
    -   The sketch selected at first will become the base profile object in the next step
    -   The sketches selected after the first one will become the loft sections. Also here the selection order is important: The sketch selected as second will become the first loft section, the one selected as third becomes the second section and so on. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
    -   The first or last selection can also be a face of a 3D object (<small>(v0.20)</small> )
2.  Press the **<img src=images/PartDesign_SubtractiveLoft.svg style="width:24px"> [Subtractive loft](PartDesign_SubtractiveLoft.md)** button.
3.  Set options if needed and click **OK**.

## Options

-   **Ruled surface**: makes straight transitions between cross-sections. Does not apply to a loft with two cross-sections. If not checked, transitions will be smooth.
-   **Closed**: makes a transition from the last cross-section to the first, creating a loop.

## Properties

-    **Label**: name given to the operation, this name can be changed at convenience.

-    **Sections**: lists the sections used.

-    **Ruled**: see [Options](#Options.md).

-    **Closed**: see [Options](#Options.md).

-    **Midplane**: N/A

-    **Reversed**: N/A

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

## Notes

-   To better control the shape of the loft, it is recommended that all cross-sections have the same number of segments. For example, for a loft between a rectangle and a circle, the circle should be broken down into 4 connected arcs.
-   You can loft from or toward a single [vertex](Glossary#V.md) from a sketch or the body. <small>(v0.20)</small> 
-   [Vertices](Glossary#V.md) can in most cases only be the start or end of a loft.
-   A cross-section cannot lie on the same plane as the one immediately preceding it.
-   If the sketch has inner geometry, i.e. the loft is supposed to have holes, then the order in which the sketch geometry is created, should be the same for all sections: Either start all sections with the inner geometry or start them all with the outer. Otherwise an invalid loft can be created where inner and outer walls cross.
-   It is not possible to loft disjoint or crossing loops.

## Links

-   [Part Loft Technical Details](Part_Loft_Technical_Details.md) explains how a [Part Loft](Part_Loft.md) is created, much of its content is relevant to the PartDesign Subtractive loft.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveLoft/en
