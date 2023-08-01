# <img alt="PartDesign workbench icon" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/id




## Introduction


<div class="mw-translate-fuzzy">

![](images/Revolve3_cropped.png )


</div>

The PartDesign Workbench is intrinsically related to the [Sketcher Workbench](Sketcher_Workbench.md). The user normally creates a Sketch, then uses the [PartDesign Pad](PartDesign_Pad.md) tool to extrude it and create a basic solid, and then this solid is further modified.

While the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) is based on a [constructive solid geometry](constructive_solid_geometry.md) (CSG) methodology for building shapes, the PartDesign Workbench uses a parametric, feature editing methodology, which means a basic solid is sequentially transformed by adding features on top until the final shape is obtained. See the [feature editing](feature_editing.md) page for a more complete explanation of this process, and then see [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md) to get started with creating solids.

A more detailed discussion of Part workbench versus Part Design workbench can be found here: [Part and Part Design](Part_and_PartDesign.md).

The bodies created with PartDesign are often subject to the [topological naming problem](Topological_naming_problem.md) which causes internal features to be renamed when the parametric operations are modified. This problem can be minimized by following the best practices described in the [feature editing](feature_editing.md) page, and by taking advantage of datum objects as support for sketches and features.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">




<div class="mw-translate-fuzzy">

## Tools


</div>

The Part Design tools are all located in the **Part Design** menu and the PartDesign toolbar that appear when you load the Part Design workbench.




<div class="mw-translate-fuzzy">

### Structure tools 

These are tools to organize the Model tree.

-   <img alt="" src=images/Std_Part.png  style="width:32px;"> [Part](Std_Part.md): adds a new Part container in the active document and makes it active.
-   <img alt="" src=images/Group.svg  style="width:32px;"> [Group](Std_Group.md): adds a Group in the active document\'s Model tree.


</div>

These tools are in fact not part of the PartDesign Workbench. They belong to the [Std Base](Std_Base.md) system. They were developed in v0.17 with the intention that they would be useful to organize a model, and create [assemblies](Assembly.md); as such, they are very useful when working with bodies created with this workbench.

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Part](Std_Part.md): adds a new Part container in the active document and makes it active.

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Group](Std_Group.md): adds a Group container in the active document, which allows organizing the objects in the [tree view](Tree_view.md).

### Part Design Helper tools 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Create body](PartDesign_Body.md): creates a [Body](Body.md) object in the active document and makes it active.

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Create sketch](PartDesign_NewSketch.md): creates‎ a new sketch on a selected face or plane. If no face is selected while this tool is executed, the user is prompted to select a plane from the Tasks panel. The interface then switches to the [Sketcher Workbench](Sketcher_Workbench.md) in sketch editing mode.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Edit sketch](Sketcher_EditSketch.md): edit the selected Sketch.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Map sketch to face](Sketcher_MapSketch.md): maps a sketch to a previously selected plane or a face of the active body.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Validate sketch](Sketcher_ValidateSketch.md): verifies the tolerance of different points and adjusts them.

### Part Design Modeling tools 

#### Datum tools 

-   <img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Create a datum point](PartDesign_Point.md): creates a datum point in the active body.

-   <img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Create a datum line](PartDesign_Line.md): creates a datum line in the active body.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Create a datum plane](PartDesign_Plane.md): creates a datum plane in the active body.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Create a local coordinate system](PartDesign_CoordinateSystem.md): creates a local coordinate system attached to datum geometry in the active body.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Create a shape binder](PartDesign_ShapeBinder.md): creates a shape binder referencing geometry from a single parent object.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Create a sub-object(s) shape binder](PartDesign_SubShapeBinder.md): creates a shape binder referencing geometry from one or more parent objects.

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Create a clone](PartDesign_Clone.md): creates a clone of the selected body.

#### Additive tools 

These are tools for creating base features or adding material to an existing solid body.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Pad](PartDesign_Pad.md): extrudes a solid from a selected sketch.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolution](PartDesign_Revolution.md): creates a solid by revolving a sketch around an axis. The sketch must form a closed profile.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Additive loft](PartDesign_AdditiveLoft.md): creates a solid by making a transition between two or more sketches.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Additive pipe](PartDesign_AdditivePipe.md): creates a solid by sweeping one or more sketches along an open or closed path.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Additive helix](PartDesign_AdditiveHelix.md): creates a solid by sweeping a sketch along a helix.

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width:48px;"> [Create an additive primitive](PartDesign_CompPrimitiveAdditive.md): adds an additive primitive to the active body.

  -<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Additive box](PartDesign_AdditiveBox.md): creates an additive box.

  -<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Additive cylinder](PartDesign_AdditiveCylinder.md): creates an additive cylinder.

  -<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Additive sphere](PartDesign_AdditiveSphere.md): creates an additive sphere.

  -<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Additive cone](PartDesign_AdditiveCone.md): creates an additive cone.

  -<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Additive ellipsoid](PartDesign_AdditiveEllipsoid.md): creates an additive ellipsoid.

  -<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Additive torus](PartDesign_AdditiveTorus.md): creates an additive torus.

  -<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Additive prism](PartDesign_AdditivePrism.md): creates an additive prism.

  -<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Additive wedge](PartDesign_AdditiveWedge.md): creates an additive wedge.

#### Subtractive tools 

These are tools for subtracting material from an existing body.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Pocket](PartDesign_Pocket.md): creates a pocket from a selected sketch.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Hole](PartDesign_Hole.md): creates a hole feature from a selected sketch. The sketch must contain one or multiple circles.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Groove](PartDesign_Groove.md): creates a groove by revolving a sketch around an axis.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Subtractive loft](PartDesign_SubtractiveLoft.md): creates a solid shape by making a transition between two or more sketches and subtracts it from the active body.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Subtractive pipe](PartDesign_SubtractivePipe.md): creates a solid shape by sweeping one or more sketches along an open or closed path and subtracts it from the active body.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtractive helix](PartDesign_SubtractiveHelix.md): creates a solid shape by sweeping a sketch along a helix and subtracts it from the active body.

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Create a subtractive primitive](PartDesign_CompPrimitiveSubtractive.md): adds a subtractive primitive to the active body.

  -<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Subtractive box](PartDesign_SubtractiveBox.md): adds a subtractive box to the active body.

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Subtractive cylinder](PartDesign_SubtractiveCylinder.md): adds a subtractive cylinder to the active body.

  -<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Subtractive sphere](PartDesign_SubtractiveSphere.md): adds a subtractive sphere to the active body.

  -<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Subtractive cone](PartDesign_SubtractiveCone.md): adds a subtractive cone to the active body.

  -<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Subtractive ellipsoid](PartDesign_SubtractiveEllipsoid.md): adds a subtractive ellipsoid to the active body.

  -<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Subtractive torus](PartDesign_SubtractiveTorus.md): adds a subtractive torus to the active body.

  -<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Subtractive prism](PartDesign_SubtractivePrism.md): adds a subtractive prism to the active body.

  -<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Subtractive wedge](PartDesign_SubtractiveWedge.md): adds a subtractive wedge to the active body.

#### Transformation tools 

These are tools for transforming existing features.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Mirrored](PartDesign_Mirrored.md): mirrors one or more features.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Linear Pattern](PartDesign_LinearPattern.md): creates a linear pattern of one or more features.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Polar Pattern](PartDesign_PolarPattern.md): creates a polar pattern of one or more features.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Create MultiTransform](PartDesign_MultiTransform.md): creates a pattern by combining any of the transformations mentioned above, as well as the [Scaled](PartDesign_Scaled.md) transformation.
    -   <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> [Scaled](PartDesign_Scaled.md): scales one or more features. This is not available as a separate transformation tool.

#### Dress-up tools 

These tools apply a treatment to edges or faces.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Fillet](PartDesign_Fillet.md): fillets (rounds) edges of the active body.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Chamfer](PartDesign_Chamfer.md): chamfers edges of the active body.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Draft](PartDesign_Draft.md): applies an angular draft to selected faces of the active body.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Thickness](PartDesign_Thickness.md): creates a thick shell from the active body and opens selected face.

#### Boolean

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Boolean operation](PartDesign_Boolean.md): imports one or more Bodies or PartDesign Clones into the active body and applies a Boolean operation.

#### Extras

Some additional functionality found in the Part Design menu:

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrate](PartDesign_Migrate.md): migrates files created with older FreeCAD versions. If the file is pure PartDesign feature-based, migration should succeed. If the file contains mixed Part/Part Design/Draft objects, the conversion will most likely fail.

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Sprocket](PartDesign_Sprocket.md): creates a sprocket profile that can be padded.

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [Involute gear](PartDesign_InvoluteGear.md): creates an involute gear profile that can be padded.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Shaft design wizard](PartDesign_WizardShaft.md): Generates a shaft from a table of values and allows to analyze forces and moments. The shaft is made with a revolved sketch that can be edited.

### Context Menu items 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Set tip](PartDesign_MoveTip.md): redefines the tip, which is the feature exposed outside of the Body.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Move object to other body](PartDesign_MoveFeature.md): moves the selected sketch, datum geometry or feature to another Body.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Move object after other object](PartDesign_MoveFeatureInTree.md): allows reordering of the Body tree by moving the selected sketch, datum geometry or feature to another position in the list of features.

#### Items shared with the Part workbench 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Appearance](Std_SetAppearance.md): determines appearance of the whole part (color transparency etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Set colors](Part_FaceColors.md): assigns colors to part faces.

## Preferences

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferences](PartDesign_Preferences.md): preferences available for PartDesign Tools.
-   [Fine tuning](Fine-tuning.md): some extra parameters to fine-tune PartDesign behavior.

## Tutorials

-   [How to use FreeCAD](http://help-freecad-jpg87.fr/), a website describing the workflow for mechanical design.
-   [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)
-   [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)
-   [PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I.md) (needs updating)
-   [PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II.md) (needs updating)

## Examples

For some ideas of what can be achieved with Part Design tools, have a look at: [PartDesign examples](PartDesign_Examples.md).

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">





 {{PartDesign_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/id
