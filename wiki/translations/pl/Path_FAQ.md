# Path FAQ/pl
## How many axes can Path Workbench handle? 

At the moment, Version 0.18, Path Workbench can handle up to 3 axis milling. Currently, 4th-axis capabilities are under development for the next official release, with some Path Workbench operations already upgraded to basic 4th-axis status.


{{top}}

## Why does it seem that in some instances, Path workbench provides more than one way to specify an Operation? 

Path workbench provides existing tools to meet many milling operations, more are in progress, and because FreeCAD is open source, there is nothing impeding any user from creating their own functionality.

As with 3D modeling, there are often multiple methods available that might be advantageous to use for different Job operations. In some cases, combinations of Operations are used to provide complete milling of the Stock.

One common example is that a Contour cut could be generated from Edges or Faces. In some cases there will be an advantage to one geometric input over another.

[na początek strony](#top.md)

## Why does Dressing up an Operation change the position in the Job Workflow shown in the Operations list? 

All additions to the Job\--including modifications, and Operation copies\--are appended at the end of the Job Workflow. If that disrupts the correct Job sequence, it must be reordered in the Job editor-\>Workflow tab.

[na początek strony](#top.md)

## What is the difference between Clearance Height and Safe Height? 

More detailed information is available in [Depths and Heights](Template:Depths/Heights.md).

[na początek strony](#top.md)

## What is the typical use of the SetupSheet? 

The SetupSheet is a dedicated spreadsheet contained within a Job, modified in the Property view, accessible only from Path workbench. It provides a mechanism for more expert users to configure aspects of their Job by using Values and Expressions contained within the SetupSheet.

Current inputs for Depths, Heights, and Tool Controllers include:

1.  Final Depth Expression \-- OpFinalDepth
2.  Start Depth Expression \-- OpStartDepth
3.  Step Down Expression \-- Defaults to OpToolDiameter. This expression is used for each Operation to calculate its default Step down value based on the diameter of the Tool defined in the associated Tool controller.
4.  Clearance Height Expression \-- StartDepth+SetupSheet.ClearanceHeightOffset
5.  Clearance Height Offset Value \-- Contains value used in Expressions
6.  Safe Height Expression \-- StartDepth+SetupSheet.SafeHeightOffset
7.  Safe Height Offset Value \-- Contains value used in Expressions
8.  Horizontal Rapid Value \-- Provides the default value used to initially populate the Horizontal Rapid Feed rate for all Tool controllers.
9.  Vertical Rapid Value \-- Provides the default value used to initially populate the Vertical Rapid Feed rate for all Tool controllers.

This provides flexibility. For example, default expressions are provided, but can be overwritten by the user. The modification can even reduce the default equation to a Value if that suits the user.

[na początek strony](#top.md)

## What is the typical use of the Job Templates? 

Job templates allow commonly used Job definitions to be saved from a Job for use on subsequent similarly configured Jobs.

[na początek strony](#top.md)

## How many Base objects does Path workbench support? 

Support exists only for a single Base object. To create paths for multiple solids in a single Job you can make a Compound out of them and use that as the base object for the Job.

[na początek strony](#top.md)

## Why does an Operation not produce usable output? 

A variety of reasons exist that may cause an individual Operation to generate no output.

One common reason is that the Tool geometry defined in the Tool controller selected for the Operation is too large to fit within the geometry selected on the 3D model for the Operation.

Be aware that this will typically exhibit as a Rapids movement to where the Operation beginning, completed by a Rapid Z movement to the geometry selected to define the Operation, and then a return to Rapid transit height.

Another common misunderstanding is that a Contour Operation is not outputting paths, when the Contour editor Operation-\>Cut Side is \"Inside\", the default, and toggling the 3D Model viability allows them to be seen.

[na początek strony](#top.md)

## Can Path Workbench perform 3D surface milling? 

Yes, Path provides for 3D surface milling Operations. It requires installation in the Macro file path of OpenCamLibrary\--a 3rd party Open Source module.

OpenCamLibrary is not integrated into FreeCAD to ensure no licensing violations occur.

[na początek strony](#top.md)

## What do I do if the default Operation strategies don\'t meet my needs? 

For Pocket Operations, the Start Point defaults to XYZ = 000, and is always on, but it too can be configured in the Property view window. Pocket and Facing Operations provide explicit Climb versus Conventional Cut Mode specification in the Operation tab.

For Contour style Operations, the Operation tab has a \"Direction\" input that may be configured as CW (clockwise), or CCW (counterclockwise), which defines the cut direction. For reference:

1.  Cut Side = Outside, Cut Direction = CCW, Climb Cut
2.  Cut Side = Outside, Cut Direction = CW, Conventional Cut
3.  Cut Side = Inside, Cut Direction = CW, Conventional Cut

Cut Side = Inside, Cut Direction = CCW, Climb Cut

Start Points can be enabled and configured in the Property view window.

In FaceMill Operations Material Allowance can be specified, allowing overcutting for positive values, and undercutting for negative values.

In Contour and Pocket Operations, the Extra Offset serves the same purpose.

These inputs are valuable, allowing functionality including:

1.  Defining Roughing Passes, in conjunction with the Depths input fields.
2.  Specifying overcut for Facing operations
3.  Features smaller than the Tool diameter, that must be faced, can benefit from specifying an Outside Contour cut with a negative Extra Offset value.

Judicious care should be exercised when specifying Material Allowances and Offsets, at the risk of undesired cuts into the Stock.

[na początek strony](#top.md)

## What do I do if an Operation generates more Vertical movements than my Job can tolerate? 

Operations such as [Pocket 3D](Path_Pocket_3D.md), [Pocket Shape](Path_Pocket_Shape.md), and [MillFace](Path_MillFace.md), but not Contour Operations have a configuration option to keep the tool down, in the Data tab of the Property View.

[na początek strony](#top.md)

## How can I leave tabs to clamp my milled work? 

Path workbench provides a [Tag dressup](Path_DressupTag.md) for just this purpose.

[na początek strony](#top.md)

## Czym jest Postprocessor? 

The [Postprocessor](Path_Post.md) is used to tailor output code to target CNC controllers for various machines, in their G-Code dialect.

[na początek strony](#top.md)

## Can I modify an existing, or make my own Postprocessor? 

Postprocessors are Python scripts, and are saved in the Macro file path. They are intended to be modified, or used as a template for further Postprocessor development.

[na początek strony](#top.md)

## I only want to use one Postprocessor\--can I make it the default, or hide other options? 

Yes, the [Path preferences](Path_Preferences.md) has a section for post processors where you can select which post processors to display and select a default post.

[na początek strony](#top.md)

## How I can set metric/imperial units for my path object? 

The 3D model units are defined in the Edit-\>Preferences\...\>General-\>Units tab\'s User System drop menu.

The Units setting configuring how the the target mill interprets the Job G-Code is set in the output Postprocessor, which inserts a G20, or a G21 G-Code command to indicate inches or millimeters, respectively.

The Postprocessor also is configured for Units/Second, or Units/Minute. If set for Units/Minute, the Path workbench internal G-Code dialect Feed rate is multiplied by 60.

Mismatches between the 3D model and Postprocessor settings are likely culprits for factor of 60 errors in Feed rate, and factors of 25.4 in distance.

[na początek strony](#top.md)

## How I can simulate my milling strategies? 

A volumetric simulator is provided to view the result of cutting the tool geometries included in the Job Operations against the Stock.

If the path lines obscure the simulation result, their visibility should be toggled off before simulation.

[na początek strony](#top.md)

## What is the significance of the path line colors? 

Path line colors are defined in the Edit-\>Preference\...-\>Path-\>GUI-\>Default Path colors. Default colors include:

1.  Green for normal paths.
2.  Red for rapid paths.
3.  Yellow for Probed paths.

[na początek strony](#top.md)

## How do I Enable/Disable visibility of path lines? 

Path workbench allows control of the display of path lines by toggling the visibility of the Job by selecting it in the [Combo View](Combo_view.md). The visibility of individual or groups of Operations are then toggled from the Combo View.

[na początek strony](#top.md)

## How do I check that my G-Code sequence is correct? 

By default, the Postprocessor output is displayed in a window before saving. This\--along with the Path CAM simulator provide a means to examine the Job before processing it on a CNC machine. The G-Code inspection tool allows you to inspect the internal Path G-Code for each Operation, providing a means to trace whether the output of the Postprocessor reflects what is defined in the Operation.

The Operations list in the Combo View panel displays the sequence that the operations will be processed in the Job. If the Operations are correct, but not in the desired sequence, that can be adjusted by double clicking the Operations list and dragging the Operations to their proper location, or by double clicking the Job editor and selecting the Workflow tab, then using the Up/Down arrows on selected Operations to sort them.

[na początek strony](#top.md)

## Why am I not getting correct G-Code output from my Postprocessor for Operations inserted using the Partial Command-\>Custom command? 

Commonly, the Custom G-Code command because the format is always in Units/second, it can cause factor of 60 errors for CNC machine targets that operate in Units/minute.

[na początek strony](#top.md)

## Why do changes to Placement values in the Property View not seem to work correctly in Path workbench? 

\"The Path feature also holds a Placement property. Changing the value of that placement will change the position of the Feature in the 3D view, although the Path information itself won\'t be modified. The transformation is purely visual. This allows you, for example, to create a Path around a face that has a particular orientation on your model, that is not the same orientation as your cutting material will have on the CNC machine.

However, Path Compounds can make use of the Placement of their children (see below).\"

[Path scripting ](Path_scripting.md)

[na początek strony](#top.md)

## Why does Path workbench on my computer seem to miss functionality that I see in other users forum posts? 

By default, Experimental functionality is hidden in Path workbench.

[na początek strony](#top.md)

## Why do Youtube videos posted by Path workbench developers appear out of synch with the Path workbench? 

Path workbench shifted dramatically from FreeCAD v0.16 to v0.17, and any videos posted prior to January 1st, 2018, are very likely to contain information that is no longer in synch with v0.17 of FreeCAD Path workbench.

[na początek strony](#top.md)

## Why are arcs not round, but are made of a set of straight lines? 

This is only a matter of displaying the path. You can change this in the preferences: Load Path workbench.

1.  open Preferences-\>Path-\>Job Preferences
2.  set the values for *Default Geometry Tolerance* and *Default Curve Accuracy* to small values but not to 0, e.g. to 0.01mm.
3.  confirm the change
4.  Restart FreeCAD.

[na początek strony](#top.md)





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path FAQ/pl
