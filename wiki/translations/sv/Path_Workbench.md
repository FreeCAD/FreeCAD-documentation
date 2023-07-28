# <img alt="Path workbench icon" src=images/Workbench_Path.svg  style="width:64px;"> Path Workbench/sv


{{TOCright}}

## Introduction

The <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Path Workbench](Path_Workbench.md) is used to produce machine instructions for [CNC machines](https://en.wikipedia.org/wiki/CNC_router) from a FreeCAD 3D model. These produce real-world 3D objects on CNC machines such as mills, lathes, lasercutters, or similar. Typically, instructions are a [G-code](https://en.wikipedia.org/wiki/G-code) dialect. A [general CNC lathe tool path sequence simulation example](https://www.ange-softs.com/SIMULCNCHTML/index.html) is presented here.

<img alt="" src=images/pathwb.png  style="width:600px;">

The FreeCAD Path Workbench workflow creates these machine instructions as follows:

-   A 3D model is the base object, typically created using one or more of the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) or <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench.md) Workbenches.
-   A [Path Job](Path_Job.md) is created in the Path Workbench. This contains all the information required to generate the necessary G-code to process the Job on a CNC mill: there is Stock material, the mill has a certain [set of tools](Path_ToolLibraryEdit.md) and it follows certain commands controlling speed and movements (usually G-code).
-   [Path Tools](Path_Tools.md) are selected as required by the Job Operations.
-   Milling paths are created using e.g. [Contour](Path_Profile.md) and [Pocket](Path_Pocket_3D.md) Operations. These Path objects use internal FreeCAD G-code dialect, independent of the CNC machine.
-   Export the job with a G-code, matching to your machine. This step is called *post processing*; there are different post processors available.

## General concepts 

The Path Workbench generates G-code defining the paths required to mill the Project represented by the 3D model on the target mill in [the Path Job Operations FreeCAD G-code dialect](Path_scripting#The_FreeCAD_Internal_GCode_Format.md), which is later translated to the appropriate dialect for the target CNC controller by selecting the appropriate postprocessor.

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.

The Path Workbench provides a Tool Manager (Library, Tool-Table), and G-code Inspection, and Simulation tools. It links the Postprocessor, and allows importing and exporting Job Templates.

The Path Workbench has external dependencies including:

1.  The FreeCAD 3D model units are defined in the **Edit → Preference → General → Units tab's Units settings**. The Postprocessor configuration defines the final G-code units.
2.  The Macro file path, and Geometric tolerances, are defined in the **Edit → Preferences → Path → Job Preferences** tab.
3.  Colors are defined in the **Edit → Preferences → Path → Path colors** tab.
4.  Holding tag parameters are defined in the **Edit → Preferences → Path → Dressups** tab.
5.  That the Base 3D model quality supports the Path workbench requirements, passes Check Geometry.

## Limitations

Some current limitations of which you should be aware are:

-   Most of the Path Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/Path_3DPocket.svg" width=24px> [3D Pocket](Path_Pocket_3D.md)** and **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** (which is still an [experimental feature](Path_experimental.md) as of November 2020).
-   Most of Path workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19_pre.
-   Most operations in Path workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/Path_Engrave.svg" width=24px> [Engrave](Path_Engrave.md)** and **<img src="images/Path_Surface.svg" width=24px> [3D Surface](Path_Surface.md)** operations.
-   The operations within the Path workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.

## Units

Unit handling in Path can be confusing. There are several points to understand:

1.  FreeCAD base units for length and time are \'mm\' and \'s\' respectively. Velocity is thus \'mm/s\'. This is what FreeCAD stores internally regardless of anything else
2.  The default unit schema uses the default units. If you\'re using the default schema and you enter a feed rate without a unit string, it will get entered as \'mm/s\'
3.  Most CNC machines expect feed rate in the form of either \'mm/min\' or \'in/min\'. Most post-processors will automatically convert the unit when generating gcode.

Schemas:

1.  Changing schema in preferences changes default unit string for the input fields. If you\'re a Path user and prefer to design in metric, it\'s highly recommended that you use the \"Metric Small Parts & CNC\" schema. If you design in US units, either the Imperial Decimal and Building US will work
2.  Changing your preferred unit schema will have no effect on output but will help avoid input errors

Output:

1.  Generating the correct unit in output is the responsibility of the post-processor and is done only at that time
2.  Machine output unit is completely unrelated to your selected unit schema
3.  Post-processors produce either metric (G21) output, Imperial (G20) output or are configurable.
4.  Configurable post-processors default to metric (G21)
5.  If you want your configurable post-processor to output imperial gcode (G20), Set the correct argument in your job output configation (ie \--inches for linuxcnc). This can be stored in a job template and set as your default template to make it automatic for all future jobs

Path Inspection:

1.  If you use the Path Inspect tool to look at g-code, you will see it in \'mm/s\' because it is not being post-processed

## Heights and depths 

Many of the commands have various heights and depths:

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Job](Path_Job.md): Creates a new CNC job.

-   <img alt="" src=images/Path_Post.svg  style="width:32px;"> [Post Process](Path_Post.md): Exports a project to G-code.

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Check the path job for common errors](Path_Sanity.md): Checks the selected job for missing values.

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Export Template](Path_ExportTemplate.md): Export the current job as a template.

### Tool Commands 

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Inspect Path Commands](Path_Inspect.md): Shows the G-code for checking.

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [CAM Simulator](Path_Simulator.md): Shows the milling operation like it\'s done on the machine.

-   <img alt="" src=images/Path_SelectLoop.svg  style="width:32px;"> [Finish Selecting Loop](Path_SelectLoop.md): Completes a loop from two selected edges.

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](Path_OpActiveToggle.md): Activates or de-activates a path operation.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries.

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock.

### Basic Operations 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges.

-   <img alt="" src=images/Path_Pocket_Shape.svg  style="width:32px;"> [Pocket Shape](Path_Pocket_Shape.md): Creates a pocketing operation from one or more selected pocket(s).

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Drilling](Path_Drilling.md): Performs a drilling cycle.

-   <img alt="" src=images/Path_MillFace.svg  style="width:32px;"> [Face](Path_MillFace.md): Creates a surfacing path.

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix.md): Creates a helical path.

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptive](Path_Adaptive.md): Creates an adaptive clearing and profiling operation.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Slot](Path_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](Path_experimental.md).

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Engrave](Path_Engrave.md): Creates an engraving path.

-   <img alt="" src=images/Path_Deburr.svg  style="width:32px;"> [Deburr](Path_Deburr.md): Creates a deburr path.

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [Vcarve](Path_Vcarve.md): Creates an engraving path using a V tool shape.

### 3D Operations 

-   <img alt="" src=images/Path_Pocket_3D.svg  style="width:32px;"> [3D Pocket](Path_Pocket_3D.md): Creates a path for a 3D pocket.

-   <img alt="" src=images/Path_Surface.svg  style="width:32px;"> [3D Surface](Path_Surface.md): Creates a path for a 3D surface. [**Experimental**](Path_experimental.md).

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Waterline](Path_Waterline.md): Creates a waterline path for a 3D surface. [**Experimental**](Path_experimental.md).

### Path Dressup 

-   <img alt="" src=images/Path_DressupAxisMap.svg  style="width:32px;"> [Axis Map](Path_DressupAxisMap.md): Remaps one axis to another.

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Boundary](Path_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupDogbone.svg  style="width:32px;"> [Dogbone](Path_DressupDogbone.md): Adds a dogbone dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [DragKnife](Path_DressupDragKnife.md): Adds a dragknife dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [LeadInOut](Path_DressupLeadInOut.md): Adds a lead-in and/or lead-out point to a selected path.

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [RampEntry](Path_DressupRampEntry.md): Adds ramp entry dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Tag](Path_DressupTag.md): Adds a holding tag dressup modification to a selected path.

-   <img alt="" src=images/Path_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](Path_DressupZCorrect.md): Corrects the Z depth using Probe Map.

### Supplemental Commands 

-   <img alt="" src=images/Path_Fixture.svg  style="width:32px;"> [Fixture](Path_Fixture.md): Changes the fixture position.

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Comment](Path_Comment.md): Inserts a comment in the G-code of a path.

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Stop](Path_Stop.md): Inserts a full stop of the machine.

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Custom](Path_Custom.md): Inserts custom G-code.

-   <img alt="" src=images/Path_Probe.svg  style="width:32px;"> [Probe](Path_Probe.md): Creates a Probing Grid from a job stock.

-   <img alt="" src=images/Path_Shape.svg  style="width:32px;"> [From Shape](Path_Shape.md): Creates a path object from a selected Part object. [**Experimental**](Path_experimental.md).

### Path Modification 

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Copy the operation in the job](Path_Copy.md): Creates a parametric Copy of a selected path object.

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Array](Path_Array.md): Creates an array by duplicating a selected path.

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Simple Copy](Path_SimpleCopy.md): Creates a non-parametric copy of a selected path object.

### Specialty Operations 

-   <img alt="" src=images/Path_ThreadMilling.svg  style="width:32px;"> [Thread Milling](Path_ThreadMilling.md): Creates a Path Thread Milling operation from features of a base object. [**Experimental**](Path_experimental.md).

### Miscellaneous

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Area](Path_Area.md): Creates a feature area from selected objects. [**Experimental**](Path_experimental.md).

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Area workplane](Path_Area_Workplane.md): Creates a feature area workplane. [**Experimental**](Path_experimental.md).

### Obsolete

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Tool Manager](Path_ToolLibraryEdit.md): Edit the Tool Manager. \'Legacy\' tool system. {{VersionMinus|0.18}}

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture.

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other

-   [Path FAQ](Path_FAQ.md): The Path Workbench shares many concepts with other CAM software packages but has its own peculiarities. If something seems wrong this is a good place to start.
-   [Path SetupSheet](Path_SetupSheet.md): You can use a SetupSheet to customize how various property values for operations are calculated.
-   [Path Postprocessor Customization](Path_Postprocessor_Customization.md): If you have a special machine which cannot use one of the available post-processors you may need to write your own post-processor.
-   [Path fourth axis](Path_fourth_axis.md): Experimental four axis milling.

## Preferences

-   <img alt="" src=images/Preferences-path.svg  style="width:32px;"> [Preferences\...](Path_Preferences.md): Preferences available for the Path Workbench.

## Scripting

See [Path scripting](Path_scripting.md).

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.

## Roadmap

-   [Path Development Roadmap](Path_Development_Roadmap.md): Read this if you are a developer and want to contribute to Path.


<div class="mw-translate-fuzzy">


</div>


{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Path Workbench/sv
