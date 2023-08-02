---
- GuiCommand:
   Name: PartDesign Hole
   MenuLocation: Part Design -> Create a substractive feature -> Hole
   Workbenches: PartDesign_Workbench
   Version: 0.17
   SeeAlso: PartDesign_Pocket
---

# PartDesign Hole/tr



## Tanım

The **Hole** feature creates one or more holes from a selected sketch\'s circles and arcs. If arcs are present they must be part of closed contours. All non arc/circle entities are ignored but they still must form closed contours. Many parameters can be set such as threading and size, fit, hole type (countersink, counterbore, straight) and more.

The centers of the circles and arcs are used to position the holes, but please note that their radii are not taken into account. The generated holes will be identical even if the radii vary.

<img alt="" src=images/Countersunk_and_counterbored_holes_cross-section1.png  style="width:600px;">



*Countersunk (to the left) and counterbored (to the right) holes longitudinal section.*

## Usage

1.  Press the **<img src="images/PartDesign_Hole.svg" width=16px> '''Hole'''** button.
2.  If an existing unused sketch is found, it will be used automatically. If more than one sketch is found, a **Select feature** panel appears to make a selection. Alternatively, a sketch can be selected before launching the Hole command.
3.  Define the Hole parameters, that are described in section [Options](#Options.md).
4.  Press **OK**.

## Options

Depending on which selection is made, some fields will activate or stay disabled.

![](images/PartDesign_Hole_parameters.png )

### Threading and size 

-   **Profile**: if set to *None*, no threading info is defined. [ISO](https://en.wikipedia.org/wiki/ISO_metric_screw_thread) and [UTS](https://en.wikipedia.org/wiki/Unified_Thread_Standard) thread profiles enable the *Size* fields.
-   **Threaded**: if checked threading data will be added to the Hole feature and the hole minor diameter is used. If left unchecked, the hole is considered non-threaded, and the nominal major diameter with defined *Clearance* is chosen.
-   **Model Thread**: if checked a real thread is modeled. This consumes much computing power and is usually not used for models, except for display purposes or sometimes for 3D prints. If it is used, it is advised to check it as one of the last actions done to the model, because it will increase recomputation time significantly. (<small>(v0.20)</small> )
-   **Direction**: sets the thread direction (Right Hand or Left hand) if *Threaded* is checked.
-   **Size**: sets the thread size. Requires *Profile* to be set to one of the [ISO](https://en.wikipedia.org/wiki/ISO_metric_screw_thread) or [UTS](https://en.wikipedia.org/wiki/Unified_Thread_Standard) profiles.
-   **Clearance**: sets either standard, close or wide clearance hole diameter. For ISO threads the diameters are according to the ISO 273 standard, for UTS they are calculated using a rule of thumb because there is no norm defining them. Only available for non-threaded holes.
-   **Class**: defines the tolerance class.
-   **Diameter**: defines the hole diameter if the *Profile* is set to *None*.
-   **Depth**: depth of the hole from the sketch plane. *Dimension* enables a field to enter a value. *Through All* will cut the hole through the whole Body. **Note:** For technical reasons, *Through All* is actually a 10 meter deep hole. If you need deeper holes, use *Dimension*.

### Hole cut 

-   **Type**: sets type of hole cut: *None* means no cut, other types are the various norms for screws and the generic types *Counterbore*, *Countersink* and (<small>(v0.21)</small> ) *Counterdrill*.
-   **Diameter**: sets the upper diameter (at the sketch plane) for the hole cut.
-   **Depth**: The depth is defined differently depending on the *Type*:
    -   For a *Counterbore* it is the depth of the hole cut, measured from the sketch plane.
    -   For a *Countersink* it is the depth of the screw head top below the sketch plane.
    -   For a *Counterdrill* it is the depth of the cylindrical part of the hole cut.
-   **Countersink angle**: angle of the conical hole cut. Only applicable for countersinks.

### Drill point 

-   **Type**: defines the ending of the hole if *Depth* is set to *Dimension*.
    -   **Flat** produces a flat bottom
    -   **Angled** sets a conical point. Its option **Take into account for depth** will subtract the conical height from the *Dimension*. So if for example *Dimension* is 7.00 and the option is not used, the cylindrical part of the hole will be 7.00 and the depth necessary for the conical part is added to the hole depth. If the option is used, the overall hole depth including the conical point will be 7.00.

### Misc

-   **Tapered**: sets a taper angle to the hole. Value is calculated from the sketch plane normal. 90 degrees sets a straight hole. A value under 90 generates a smaller hole radius at the bottom; a value over 90 enlarges the hole radius at the bottom.
-   **Reversed**: reverses the hole extrusion direction. The default direction is the mapping direction of the hole sketch to its attachment.

## Properties

Much of the Data properties are the same as those shown in [Options](#Options.md).

-    **Label**: name given to the object, this name can be changed at convenience.

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See **<img src="images/Part_RefineShape.svg" width=16px> [Part RefineShape](Part_RefineShape.md)** for more details.

## Limitations

-   By default, the hole feature extrudes below the sketch plane. If the solid lies on the XY_Plane, and the hole sketch is attached to the XY_Plane, it will try to extrude away from the solid and seemingly produce no result. In such a case, the option *Reversed* needs to be set; alternatively the sketch can be mapped to the bottom face of the solid.
-   Model Thread works only if Reversed is not set.

## Cut Type Definitions 

Cut types (screw-types) are defined in [json](https://de.wikipedia.org/wiki/JavaScript_Object_Notation) files. There is a set of files distributed with FreeCAD, but users can create their own definitions. Files are searched in <UserAppDataDir>/PartDesign/Hole. The `UserAppDataDir` can be found by typing `App.getUserAppDataDir()` in the [Python console](Python_console.md).

The file should contain:

-   **name**: The name of the definition. This must be unique as it will be used as identifier in the FreeCAD UI and as internal index.
-   **cut_type**: Either `countersink` or `counterbore`.
-   **thread_type**: Either `metric` or `metricfine`.
-   **angle**: The angle of a countersink (not necessary for counterbore).
-   **data**: A list of sizes, consisting of:
    -   **thread**: Name of thread known to FreeCAD.
    -   **diameter**: The diameter of the cut.
    -   **depth**: Depth of the counterbore (not necessary for countersink).

Example: {{Code|lang=json|code=
{
    "name": "DIN 7984",
    "cut_type": "counterbore",
    "thread_type": "metric",
    "data": [
        { "thread": "M2",   "diameter":  4.3, "depth":  1.6 },
        { "thread": "M2.5", "diameter":  5.0, "depth":  2.0 },
        …
    ]
}
}}





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Hole/tr
