---
- GuiCommand   *
   Name   *Path Post
   MenuLocation   *Path → Post Process
   Workbenches   *[Path](Path_Workbench.md)
   Shortcut   ***P** **P**
---

# Path Post/pl

## Description

The **<img src="images/Path_Post.svg" width=16px> [Post](Path_Post.md)** command exports the selected **<img src="images/Path_Job.svg" width=16px> [Path Job](Path_Job.md)** to a G-code file.

**Each CNC Controller speaks a specific G-Code dialect, requiring a Dialect-correct Postprocessor to translate the final output from the agnostic internal FreeCAD G-Code dialect.**

### Typical functions of the Postprocessor include 

-   Using a correct Job output G-Code file extension.
-   Selecting the G-Code commands. CNC controllers typically support a subset of available G-Code commands. The super-set of G-Code commands contains powerful and specialized commands that otherwise must be processed using multiple simpler commands. Postprocessors are written to select the best G-Code for an Operation, available on the target.
-   Formatting the G-Code syntax by reordering the Feed, X, Y, Z, A, and B inputs, and the precision.
-   Inserting a Pre-amble to set units, units format, Work plane, coordinate system, etc\...
-   Inserting a Post-amble to park the machine, stop it, process any arguments.
-   Inserting Tool changes, or suppressing them between subsequent operations using the same tool.
-   Formatting the Feed and Speed rate information to revolutions per minute, or per second.
-   Formatting Function Call Naming and Calling.

### Postprocessor Customization 

If you want to write your own postprocessor, have a look at the [Path Postprocessor Customization](Path_Postprocessor_Customization.md) page.

**Note   *** Several provided Postprocessors generate suitable code for many CNC controllers, or can be used as templates for modification

Postprocessors contain configuration flags and are designed to be tuned by adding G-Codes and M-Codes to provided definitions for   *

-   Machine initialization
-   Job finalization
-   Tool-Changes
-   Cooling on /off
-   Etc\...

Postprocessors use [FreeCAD\'s internal G-Code dialect](Path_scripting#The_FreeCAD_Internal_GCode_Format.md) in conjunction with the Postprocessor configuration definitions, to generate Dialect-Correct G-Code for target machines. This allows the Path workbench to generate correct G-Code to target various CNC machine controllers by invoking different Postprocessors.

CNC Machine Controller types include   *

-   CNC mills
-   CNC lathes
-   3D Printers
-   DragKnife Cutters
-   Laser Cutters
-   Engravers
-   Plasma Torch Cutters
-   Wire Benders
-   EDM Cutters
-   Etc\...

If only one CNC machine is used, or if all CNC machines share a common Postprocesor, the Path workbench would need to include only a single Postprocessor. If a single Postprocessor is inadequate to output G-Code for all target CNC controllers, then multiple Postprocessors must be installed.

## Usage

1.  Select a <img alt="" src=images/Path_Job.svg  style="width   *16px;"> [Path Job](Path_Job.md) in the [Tree view](Tree_view.md).
2.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Path_Post.svg" width=16px> [Path Post](Path_Post.md)** button.
    -   Select the **Path → <img src="images/Path_Post.svg" width=16px> Post Process** option from the menu.
    -   Use the keyboard shortcut   * **P** then **P**.
3.  Confirm the **Output File** name and directory

## Options

Output file and Postprocessor properties can be set in the [Job](Path_Job.md), at any time, prior to invoking the Postprocessor.

The provided Postprocessors are written with comments indicating areas containing Flags, Configuration Variables, and Sections of G-Codes and M-Codes that are to be used by the Postprocessor to configure the output.

Typical Configuration True/False Flags include   *

-   OUTPUT\_COMMENTS (True = Allow, False = Suppress), Used to insert Text Comments in the output G-Code file.
-   OUTPUT\_HEADER (True = Allow, False = Suppress), Used to insert Text Headers in the output G-Code file.
-   OUTPUT\_LINE\_NUMBERS (True = Allow, False = Suppress), Used to insert Line Numbers in the output G-Code file.
-   SHOW\_EDITOR (True = Allow, False = Suppress), Used to show the output G-Code in a Pop-up window when invoking the Postprocessor.
-   MODAL (True = Allow, False = Suppress), Used to reduce the number of output G-Code lines by stripping Mode information when the Mode is not changing.

Typical Configuration Variables include   *

-   LINENR (Line Number), Used to Set the Line Number index.
-   UNITS (G20 or G21), Used to explicitly communicate to the target CNC controller what Units to use to interpret the final output file.
-   MACHINE\_NAME (Name of Target CNC Mill), Used to Insert a machine name label in the final output file.
-   PRECISION, Used to Set the number of digits to include after the decimal place in final output file

Typical Configuration Sections include   *

-   PREAMBLE (Code configuration inserted at beginning of the Job)
-   POSTAMBLE (Code configuration appended to the Job, providing for parking the machine, etc\...)
-   TOOL\_CHANGE (Code inserted with each tool change in the Job)

The **Edit** → **Preferences...** → **Path** → **Job Preferences tab** → **Defaults** → **Path** is used to set the default Postprocessor selected on Job creation. This allows Path workbench to be configured to only display desired Postprocessors, and to set a default.

Included Postprocessors are saved in the **FreeCAD/Mod/Path/Pathscripts/Post** by default   *

-   centroid
-   comparams
-   dxf
-   dynapath
-   grbl, including support for bCNC header blocks using Job output argument \--bcnc
-   jtech (laser)
-   [linuxcnc](http   *//linuxcnc.org/docs/html/gcode/g-code.html#gcode   *g17-g19.1)
-   mach3\_mach4
-   nccad
-   opensbp
-   phillips
-   rml
-   smoothie
-   uccnc

## Limitations

-   Do **not** use the **File** → **Export** menu for export to G-code, it will produce damaged G-code!





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Post/pl
