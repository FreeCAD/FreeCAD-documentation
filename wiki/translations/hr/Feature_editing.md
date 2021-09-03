 {{TOCright}}

## Predstavljanje

This page explains the way the <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Workbench](PartDesign_Workbench.md) is intended to be used starting with FreeCAD 0.17.

While the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and other workbenches construct models by combining shapes together (see [Constructive solid geometry](Constructive_solid_geometry.md)), the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md) workbench uses **[features](PartDesign_Feature.md)**. A [feature](https://en.wikipedia.org/wiki/Feature_recognition) is an operation that modifies the shape of a model.

## Feature editing methodology {#feature_editing_methodology}

The first feature is commonly called the **base feature**. As more features are added to the model, each feature takes the shape of the previous one and adds or removes matter, creating linear dependencies from one feature to the next. In effect, this methodology mimics a common manufacturing process: a block is cut on one side, then on another side, holes are added, then rounds, etc.

All features are listed sequentially in the Model tree and can be edited at any time, with the last feature at the bottom representing the final part.

Features can be sorted into different categories:

-   **Profile-based**: these features start from a profile to define the shape of the matter to be added or removed. The profile can be a sketch, a planar face on existing geometry (a profile will be extracted from its edges), a ShapeBinder or a Draft object that has been included in the active Body.

-   **Additive**: adds matter to the existing model. Additive features show yellow icons.

-   **Subtractive**: removes matter from the existing model. Subtractive features show red and blue icons.

-   **Primitive-based**: based on geometric primitives (cube, cylinder, cone, torus...). They can be additive or subtractive.

-   **Transformation features**: they apply a transformation to existing features (mirrored, linear pattern, polar pattern, multitransform).

-   **Dress-up**: features that apply a treatment to edges or faces, such as fillets/rounds, chamfers and drafts.

-   **Procedural**: can be said of features that are not based on sketches, like the transformation and dress-up features.

## Body

Working in PartDesign requires first creating a <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[Body](PartDesign_Body.md)**. The PartDesign Body is a container that groups a sequence of features forming a single contiguous solid.

![](images/PartDesign_Body_tree.png )

**What is a single contiguous solid?** It is an object like a casting or something machined from a single block of metal. If the object involves nails, screws, glue or welding, it is not a single contiguous solid. As a practical example, a wooden chair would be made of multiple bodies, with one for each of its sub-components (legs, slats, seat, etc).

Multiple bodies can be created in a FreeCAD document; they can also be combined to form a single contiguous solid.

Only one body can be active in a document. The active body gets the new created features. A body can be activated or deactivated by double clicking on it. An activated body is highlighted in light blue. The highlighting color can be set in the preferences under Display/Colors/Active container since version 0.18.

When a model requires multiple bodies, like the previous wooden chair example, the general purpose <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Part container](Std_Part.md) can be used to group them and move the whole as a unit.

### Body visibility management {#body_visibility_management}

A body will present by default its most recent feature to the outside. This feature is defined by default as the tip. A good analogy is the expression *the tip of the iceberg*: only the tip is visible above the water, most of the iceberg\'s mass (the other features) is hidden. As a new feature is added to the body, visibility of the previous feature is turned off, and the new feature becomes the tip.

There can only be one feature visible at a time. It is possible to [toggle the visibility](Std_ToggleVisibility.md) of any feature in the body, by selecting it in the Model tree and pressing the **Spacebar**, in effect going back in the history of the body.

### Početna točka tijela {#početna_točka_tijela}

The body has an Origin which consists of reference planes (XY, XZ, YZ) and axes (X, Y, Z) that can be used by sketches and features. Sketches can be attached to Origin planes, and they no longer need to be mapped to planar faces for features based on them to be added or subtracted from the model.

### Pomjeri i posloži objekte {#pomjeri_i_posloži_objekte}

It is possible to temporarily redefine the tip to a feature in the middle of the Body tree to insert new objects (features, sketches or datum geometry). It is also possible to reorder features under a Body, or to move them to a different Body. Select the object and right-click to get a contextual menu that will offer both options. The operation may be prevented if the object has dependencies in the source Body, such as being attached to a face. To move a sketch to another Body, it should not contain links to external geometry.

### Difference with other CAD systems {#difference_with_other_cad_systems}

A fundamental difference between FreeCAD and other programs, like Catia, is that FreeCAD doesn\'t allow you to have many disconnected solids in the same <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[PartDesign Body](PartDesign_Body.md)**. That is, a new feature should always be built on top of the previous one. Or said in a different way, the newer feature should \"touch\" the previous feature, so that both features are fused together and become a single solid. You cannot have \"floating\" solids.

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width:550px;">


*Difference between Catia and FreeCAD. Left: Catia allows disconnected bodies from the previous features of the body. In FreeCAD this causes an error; Right: the newer feature should always contact or intersect the previous feature so that it is fused to it, and becomes a single contiguous solid.*

## Datum geometry {#datum_geometry}

Datum geometry consists of custom planes, lines, points or externally linked shapes. They can be created for use as reference by sketches and features. There is a multitude of attachment possibilities for datum objects.

In some CAD systems you can define a datum plane that is offset from the previous body and you can create a disconnected solid. So, placing a lot of datum planes, and building objects on them is okay and won\'t cause an error. Typically, you would eventually adjust the planes to their final positions, so that the individual objects are fused together.

In FreeCAD, as mentioned in the previous section, disconnected solids are **NOT** allowed, so a sketch on a datum plane that would create a non-contiguous solid will fail.

In FreeCAD, datum planes make sense if you are placing sketches (and padding, pocketing, etc.) in non-standard orientations, that is, in planes offset or rotated around the three main axes. Since sketches can also be placed in non-standard orientations in the same way as datum planes, often there is no need to use datum planes.

Datum planes also make sense if there will be more than one sketch in the same non-standard orientation. In this case a datum plane can be used and the orientation only needs to be adjusted for the datum plane to adjust all associated sketches and the features created from the sketches.

Both sketches and datum planes should be attached to base planes. Referencing generated geometry (geometry that is the result of a feature creating operation, for example a pad or pocket) should be avoided since faces and edges get renamed and renumbered and the references no longer refer to the same thing. This is called topological instability and is due the way FreeCAD uses some external geometric libraries. Hopefully this will be improved in the future. (See Advice for creating stable models below).

Even if not used for supporting sketches, datum objects are still helpful as visual indicators, to draw attention to important features or distances in the modelling process. (Though, simply adding geometry to a sketch also provides similar visual feedback.)

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width:550px;">


*Difference between Catia and FreeCAD. Left: Catia allows disconnected bodies from the previous features of the body. In FreeCAD this causes an error; Right: the newer feature should always contact or intersect the previous feature, so that it is fused to it, and becomes a single contiguous solid. In this example, the new solid is based on a datum plane that is rotated around the Y axis.*

## Cross-referencing {#cross_referencing}

It is possible to cross-reference elements from a body in another body via datums. For example the datum shape binder allows to copy over faces from a body as reference in another one. This should make it easy to build a box with fitting cover in two different bodies. FreeCAD helps you to avoid accidentally linking to other bodies by asking for confirmation of your intent.

## Dodatak

Object attachment is not a specific PartDesign tool, but rather a Part utility introduced in v0.17 that can be found in the Part menu. It is heavily used in the PartDesign workbench to attach sketches and reference geometry to the standard planes and axes of the Body. Very extensive ways of creating datum points, lines and planes are available. Optional attachment offset parameters make this tool very versatile.

More info can be found in the [Attachment](Part_Attachment.md) page and the [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md).

## Advice for creating stable models {#advice_for_creating_stable_models}

The idea of parametric modeling implies that you can change the values of certain parameters and subsequent steps are changed according to the new values. However, when severe changes are made, the model can break due to the [topological naming problem](topological_naming_problem.md) that is still unresolved in FreeCAD. Breakage can be minimized when you respect the following design principles:

-   Avoid attaching sketches and datum objects to generated geometry of the model. (Generated geometry is any face or edge created as a result of a pad, pocket, etc..)
-   Place your sketches on standard coordinate planes, or on custom datum planes attached to standard planes.
    -   Sketches attached to basic coordinate planes/axes or to datum planes attached to coordinate planes/axes, will not get unexpectedly reattached to a different reference.
-   When creating datum geometry, do not attach it to generated geometry
    -   Attach it to standard planes/axes and/or sketches or datum objects which use attachment offsets to standard planes/axes.
-   Use a \"master sketch\". Since a master sketch is done before rest of the model, it only references the coordinate planes/axes.
    -   A master sketch should be as simple as possible, containing basic geometric elements of your model.
    -   Master sketch elements can be referenced when modelling subsequent features.
    -   A master sketch can be the first sketch in the Body, or outside the body completely
    -   A master sketch can be referenced as external geometry or via a ShapeBinder.
-   Don\'t create ShapeBinders from generated geometry
-   Keep in mind that ShapeBinders can be an issue when geometry is deleted from the sketch it is based on.
-   If you inevitably have to reference an intermediate feature, e.g. the result of a thickness operation
    -   Use the first reference possible in the list of subsequent features where the referenced geometric element occurs.
    -   If you take an early feature as reference, all changes to intermediate steps won\'t break your model.
    -   Try to reference a sketch or sketch geometry rather than generated geometry.
-   Use *dress ups*, like fillets and chamfers, as late in the feature tree as possible
-   Note, using spreadsheets, dynamic data, master sketches, etc. generally produce more parametric models and help avoid the topological naming issue.

## Body building workflow {#body_building_workflow}

There are several workflows that are possible with the [PartDesign Workbench](PartDesign_Workbench.md). What should always be noticed is that all the features created inside a [PartDesign Body](PartDesign_Body.md) will be fused together to obtain the final object.

### Different sketches {#different_sketches}

Sketches need to be supported by a plane. This plane can be one of the main planes (XY, XZ, or YZ) defined by the Origin of the Body. A sketch is either extruded into a positive solid (additive), with a tool like <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md), or into a negative solid (subtractive), with a tool like <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Pocket](PartDesign_Pocket.md). The first adds volume to the final shape of the body, while the latter cuts volume from the final shape. Any number of sketches and partial solids can be created in this way; the final shape (tip) is the result of fusing these operations together. Naturally, the Body can\'t consist of only subtractive operations, as the final shape should be a solid with a positive, non-zero volume.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width:600px;">

### Sequential features {#sequential_features}

Sketches can be supported by the faces of previous solid operations. This may be necessary if you need to access a face that is only available after a certain feature has been created. However, this workflow isn\'t recommended since, if the original feature is modified, the following features in the sequence may break. This is the [topological naming problem](topological_naming_problem.md).

<img alt="" src=images/PartDesign_workflow_2.svg  style="width:600px;">

### Use of datum planes for support {#use_of_datum_planes_for_support}

Datum planes are useful to support the sketches. These auxiliary planes should be attached to the base planes of the body.

\'\'Note: In many cases, a sketch attached to a base plane with attachment offsets can accomplish the same function. Datums are particularly useful when multiple sketches or other constructs will use the datum. This means all changes to the datum will be apply to attached sketches, etc. Adding a single sketch to a datum, rather than using attachment offsets in the sketch properties, is an extra step and is essentially redundant. \'\'

As with sketches, it is possible to attach Datum planes to generated geometry (edges, faces of previously created solids), ***but this is not recommended*** since it can cause the topological naming problem.

In addition, a <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) can be used to import external geometry into the body to serve as reference; then sketches can be attached to this auxiliary body, either using datum planes or not.

*Again, the ShapeBinder should be based on Sketches from the previous body, not generated geometry.*

Using datum objects is often the best way to produce stable models, when used with base planes and attachment offsets, although it requires a bit more work from the user. For details about basic attachment see: [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) *Note: while this tutorial talks about sketches, datum attachment is done in similar fashion.*

## Tutorials

The [tutorials](Tutorials.md) page provides some examples of using the [feature editing](feature_editing.md) method of the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md).

-   [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)
-   [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)
-   [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md)

## Related

-   [Constructive solid geometry](Constructive_solid_geometry.md)

<img alt="" src=images/PartDesign_workflow_3.svg  style="width:600px;">


{{PartDesign Tools navi

}} 

[Category:Common Questions{{\#translation:}}](Category:Common_Questions.md)
