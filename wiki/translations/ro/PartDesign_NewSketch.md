---
- GuiCommand:   Name:PartDesign NewSketch   Workbenches:[[PartDesign Workbench   PartDesign]], Complete|MenuLocation:Part Design → Create sketch   Shortcut:   SeeAlso:---


</div>

## Descriere

This tool creates a new sketch, creates a new [PartDesign Body](PartDesign_Body.md) to contain the sketch if one does not exist and automatically opens the [Sketcher workbench](Sketcher_Workbench.md) after creation.

When creating models using the <img src=images/Sketcher_NewSketch.svg style="width:PartDesign workbench](PartDesign_Workbench.md), this tool should be preferred to the **[16px"> [Sketcher NewSketch](Sketcher_NewSketch.md)** tool found in the [Sketcher workbench](Sketcher_Workbench.md).

## Utilizare


<div class="mw-translate-fuzzy">

1.  Click pe <img alt="" src=images/PartDesign_NewSketch.png  style="width:24px;"> din toolbar, sau selectați **PartDesign** → **<img src="images/PartDesign_NewSketch.png" width=24px> Create sketch** sin meniul principal.


</div>

## Opţiuni

-   To change the attachment of an existing sketch, change its **Map Mode** property (see [Properties](#Properties.md).)

-   The *Select feature* Dialog defines the features of the new sketch

:   

    :   <img alt="" src=images/PartDesign.CreateSketch.SelectFeatureDialog.jpeg  style="width:300px;">
    :   *Select feature* dialog. These settings create a sketch on the XY plane and allow cross-references from other items of the same body\'\'

Dialog settings

-   Coordinate system box: defines the orientation of the sketch plane
-   Allow Used Features checkbox: *TBD*

:   Allow external features options

-   From other bodies of the same part: any elements used in the same body can be referenced
-   From different parts or free features: *TBD*
-   Make independent copy: all other elements will be separate copies, i.e. they will not change when the original changes.
-   Make dependent copy: the elements will be copies, but a dependency to the original elements is kept. This is basically using a [Shapebinder](PartDesign_ShapeBinder.md)
-   Create cross-reference: the linked elements will not be copies, but point to the original elements, e.g. a master sketch. Any changes are reflected to this sketch

To reference any items in the <img src=images/Sketcher_CarbonCopy.svg style="width:Workbench Sketcher](Sketcher_Workbench.md) use the **<img src="images/Sketcher_External.svg" width=16px> [External Geometry](Sketcher_External.md)** and **[16px"> [CarbonCopy](Sketcher_CarbonCopy.md)** tools. Generally it is recommended to use other sketches as source for references rather than faces or edges, because they are less affected by the Topological Naming Issue.

## Properties

-    **Map Mode**: mode of attachment of the sketch to another object, usually a plane or a face but can be other types of objects. Click once in the field to reveal a **...** button and press it to open the [Attachment](Part_EditAttachment.md) dialog. If set to Deactivated, the Placement property is enabled.

-    **Placement**: controls the orientation of the sketch in the 3D space; see [placement](Std_Placement.md). Disabled if the sketch is attached through the Map Mode property.








{{PartDesign Tools navi

}} 
