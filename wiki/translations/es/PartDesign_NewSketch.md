---
- GuiCommand:/es
   Name:PartDesign NewSketch
   Name/es:Croquis PartDesign
   Workbenches:[PartDesign](PartDesign_Workbench/es.md)
   MenuLocation:Part Design → Crear croquis
   Version:0.17
---

# PartDesign NewSketch/es


</div>



## Descripción

This tool creates a new sketch, creates a new [PartDesign Body](PartDesign_Body.md) to contain the sketch if one does not exist and automatically opens the [Sketcher workbench](Sketcher_Workbench.md) after creation.

When creating models using the [PartDesign workbench](PartDesign_Workbench.md), this tool should be preferred to the **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher NewSketch](Sketcher_NewSketch.md)** tool found in the [Sketcher workbench](Sketcher_Workbench.md).

## Usage

1.  Press the **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)** button from the PartDesign toolbar.
2.  In the Tasks panel, the **Select feature** dialog is brought up. Select one of the planes in the list or in the 3D view which can be reoriented for better visibility.
3.  Press **OK**.
4.  The interface automatically switches to the Sketcher workbench and the sketch can be edited. Once the sketch is exited, the interface is brought back to the PartDesign workbench and the 3D view is restored to the view orientation prior to creating the sketch.
5.  Alternatively, a plane or a face on the existing active body can be selected before creating the sketch, in which case the sketch is instantly created.

## Options

-   To change the attachment of an existing sketch, change its **Map Mode** property (see [Properties](#Properties.md).)

-   The *Select feature* Dialog defines the features of the new sketch

:   

    :   <img alt="" src=images/PartDesign.CreateSketch.SelectFeatureDialog.jpeg  style="width:300px;">
    :   *Select feature* dialog. These settings create a sketch on the XY plane and allow cross-references from other items of the same body

Dialog settings

-   Coordinate system box: defines the orientation of the sketch plane
-   Allow Used Features: *TBD*

:   Allow external features options

-   From other bodies of the same part: any elements used in the same body can be referenced
-   From different parts or free features: *TBD*
-   Make independent copy: all other elements will be separate copies, i.e. they will not change when the original changes.
-   Make dependent copy: the elements will be copies, but a dependency to the original elements is kept. This is basically using a [Shapebinder](PartDesign_ShapeBinder.md)
-   Create cross-reference: the linked elements will not be copies, but point to the original elements, e.g. a master sketch. Any changes are reflected to this sketch

To reference any items in the [Workbench Sketcher](Sketcher_Workbench.md) use the **<img src="images/Sketcher_External.svg" width=16px> [External Geometry](Sketcher_External.md)** and **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [CarbonCopy](Sketcher_CarbonCopy.md)** tools. Generally it is recommended to use other sketches as source for references rather than faces or edges, because they are less affected by the Topological Naming Issue.

## Properties

-    **Map Mode**: mode of attachment of the sketch to another object, usually a plane or a face but can be other types of objects. Click once in the field to reveal a **...** button and press it to open the [Attachment](Part_EditAttachment.md) dialog. If set to Deactivated, the Placement property is enabled.

-    **Placement**: controls the orientation of the sketch in the 3D space; see [placement](Std_Placement.md). Disabled if the sketch is attached through the Map Mode property.








{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign NewSketch/es
