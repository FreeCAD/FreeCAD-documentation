# CAM Workbench/zh-tw
<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="CAM workbench icon" src=images/Workbench_CAM.svg  style="width:128px;">


</div>





<div lang="en" dir="ltr" class="mw-content-ltr">

## Introduction


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [CAM Workbench](CAM_Workbench.md) is used to produce machine instructions for [CNC machines](https://en.wikipedia.org/wiki/CNC_router) from a FreeCAD 3D model. These produce real-world 3D objects on CNC machines such as mills, lathes, lasercutters, or similar. Typically, instructions are a [G-code](https://en.wikipedia.org/wiki/G-code) dialect. A [general CNC lathe tool path sequence simulation example](https://www.ange-softs.com/SIMULCNCHTML/index.html) is presented here.


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div lang="en" dir="ltr" class="mw-content-ltr">

The FreeCAD CAM Workbench workflow creates these machine instructions as follows:

-   A 3D model is the base object, typically created using one or more of the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) or <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench.md) Workbenches.
-   A [CAM Job](CAM_Job.md) is created in the CAM Workbench. This contains all the information required to generate the necessary G-code to process the Job on a CNC mill: there is Stock material, the mill has a certain [set of tools](CAM_ToolBitLibraryOpen.md) and it follows certain commands controlling speed and movements (usually G-code).
-   [CAM Tools](CAM_Tools.md) are selected as required by the Job Operations.
-   Milling paths are created using e.g. [Contour](CAM_Profile.md) and [Pocket](CAM_Pocket_3D.md) Operations. These CAM objects use internal FreeCAD G-code dialect, independent of the CNC machine.
-   Export the job with a G-code, matching to your machine. This step is called *post processing*; there are different post processors available.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## General concepts 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The CAM Workbench generates G-code defining the paths required to mill the Project represented by the 3D model on the target mill in [the CAM Job Operations FreeCAD G-code dialect](CAM_scripting#The_FreeCAD_Internal_GCode_Format.md), which is later translated to the appropriate dialect for the target CNC controller by selecting the appropriate postprocessor.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The G-code is generated from directives and Operations contained in a CAM Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding CAM Operations, Path Dressups, Supplemental Commands, and Path Modifications from the CAM Menu, or GUI buttons.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The CAM Workbench provides a Tool Manager (Library, Tool-Table), and G-code Inspection, and Simulation tools. It links the Postprocessor, and allows importing and exporting Job Templates.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The CAM Workbench has external dependencies including:

1.  The FreeCAD 3D model units are defined in the **Edit → Preference → General → Default unit system**. The Postprocessor configuration defines the final G-code units.
2.  The Macro file path, and Geometric tolerances, are defined in the **Edit → Preferences → CAM → Job Preferences** tab.
3.  Colors are defined in the **Edit → Preferences → CAM → GUI** tab.
4.  Holding tag parameters are defined in the **Edit → Preferences → CAM → Dressups** tab.
5.  That the Base 3D model quality supports the CAM workbench requirements, passes Check Geometry.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Limitations


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Some current limitations of which you should be aware are:

-   Most of the CAM Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/CAM_3DPocket.svg" width=24px> [3D Pocket](CAM_Pocket_3D.md)** and **<img src="images/CAM_Surface.svg" width=24px> [3D Surface](CAM_Surface.md)** (which is still an [experimental feature](CAM_experimental.md) as of November 2020).
-   Most of CAM workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19_pre.
-   Most operations in CAM workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/CAM_Engrave.svg" width=24px> [Engrave](CAM_Engrave.md)** and **<img src="images/CAM_Surface.svg" width=24px> [3D Surface](CAM_Surface.md)** operations.
-   The operations within the CAM workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Units


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Unit handling in CAM can be confusing. There are several points to understand:

1.  FreeCAD base units for length and time are \'mm\' and \'s\' respectively. Velocity is thus \'mm/s\'. This is what FreeCAD stores internally regardless of anything else
2.  The default unit schema uses the default units. If you\'re using the default schema and you enter a feed rate without a unit string, it will get entered as \'mm/s\'
3.  Most CNC machines expect feed rate in the form of either \'mm/min\' or \'in/min\'. Most post-processors will automatically convert the unit when generating gcode.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Schemas:

1.  Changing schema in preferences changes default unit string for the input fields. If you\'re a CAM user and prefer to design in metric, it\'s highly recommended that you use the \"Metric Small Parts & CNC\" schema. If you design in US units, either the Imperial Decimal and Building US will work.
2.  Changing your preferred unit schema will have no effect on output but will help avoid input errors.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Output:

1.  Generating the correct unit in output is the responsibility of the post-processor and is done only at that time.
2.  Machine output unit is completely unrelated to your selected unit schema.
3.  Post-processors produce either metric (G21) output, Imperial (G20) output or are configurable.
4.  Configurable post-processors default to metric (G21).
5.  If you want your configurable post-processor to output imperial G-code (G20), set the correct argument in your job output configuration (ie \--inches for linuxcnc). This can be stored in a job template and set as your default template to make it automatic for all future jobs.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

CAM Inspection:

1.  If you use the CAM Inspect tool to look at G-code, you will see it in \'mm/s\' because it is not being post-processed.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Heights and depths 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Many of the commands have various heights and depths:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Commands


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Some commands are experimental and not available by default. To enable them see [CAM experimental](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Project Commands 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Job.svg  style="width:32px;"> [Job](CAM_Job.md): Creates a new CNC job.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Post.svg  style="width:32px;"> [Post Process](CAM_Post.md): Exports a project to G-code.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Sanity.svg  style="width:32px;"> [Check the CAM job for common errors](CAM_Sanity.md): Checks the selected job for missing values.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ExportTemplate.svg  style="width:32px;"> [Export Template](CAM_ExportTemplate.md): Export the current job as a template.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Tool Commands 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Inspect.svg  style="width:32px;"> [Inspect CAM Commands](CAM_Inspect.md): Shows the G-code for checking.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Simulator.svg  style="width:32px;"> [CAM Simulator](CAM_Simulator.md): Shows the milling operation like it\'s done on the machine.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_SimulatorGL.svg  style="width:32px;"> [CAM SimulatorGL](CAM_SimulatorGL.md): Enables the new, improved CAM simulator. <small>(v1.0)</small> 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_SelectLoop.svg  style="width:32px;"> [Finish Selecting Loop](CAM_SelectLoop.md): Completes a loop from two selected edges.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](CAM_OpActiveToggle.md): Activates or de-activates a path operation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](CAM_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](CAM_ToolBitDock.md): Toggles the ToolBit Dock.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Basic Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Profile.svg  style="width:32px;"> [Profile](CAM_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:32px;"> [Pocket Shape](CAM_Pocket_Shape.md): Creates a pocketing operation from one or more selected pocket(s).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Drilling.svg  style="width:32px;"> [Drilling](CAM_Drilling.md): Performs a drilling cycle.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_MillFace.svg  style="width:32px;"> [Face](CAM_MillFace.md): Creates a surfacing path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Helix.svg  style="width:32px;"> [Helix](CAM_Helix.md): Creates a helical path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Adaptive.svg  style="width:32px;"> [Adaptive](CAM_Adaptive.md): Creates an adaptive clearing and profiling operation.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Slot.svg  style="width:32px;"> [Slot](CAM_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Engrave.svg  style="width:32px;"> [Engrave](CAM_Engrave.md): Creates an engraving path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Deburr.svg  style="width:32px;"> [Deburr](CAM_Deburr.md): Creates a deburr path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Vcarve.svg  style="width:32px;"> [Vcarve](CAM_Vcarve.md): Creates an engraving path using a V tool shape.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### 3D Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Pocket_3D.svg  style="width:32px;"> [3D Pocket](CAM_Pocket_3D.md): Creates a path for a 3D pocket.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Surface.svg  style="width:32px;"> [3D Surface](CAM_Surface.md): Creates a path for a 3D surface. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Waterline.svg  style="width:32px;"> [Waterline](CAM_Waterline.md): Creates a waterline path for a 3D surface. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Path Dressup 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupAxisMap.svg  style="width:32px;"> [Axis Map](CAM_DressupAxisMap.md): Remaps one axis to another.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:32px;"> [Boundary](CAM_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupDogbone.svg  style="width:32px;"> [Dogbone](CAM_DressupDogbone.md): Adds a dogbone dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupDragKnife.svg  style="width:32px;"> [DragKnife](CAM_DressupDragKnife.md): Adds a dragknife dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupLeadInOut.svg  style="width:32px;"> [LeadInOut](CAM_DressupLeadInOut.md): Adds a lead-in and/or lead-out point to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupRampEntry.svg  style="width:32px;"> [RampEntry](CAM_DressupRampEntry.md): Adds ramp entry dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupTag.svg  style="width:32px;"> [Tag](CAM_DressupTag.md): Adds a holding tag dressup modification to a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_DressupZCorrect.svg  style="width:32px;"> [Z Depth Correction](CAM_DressupZCorrect.md): Corrects the Z depth using Probe Map.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Supplemental Commands 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Fixture.svg  style="width:32px;"> [Fixture](CAM_Fixture.md): Changes the fixture position.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Comment.svg  style="width:32px;"> [Comment](CAM_Comment.md): Inserts a comment in the G-code of a path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Stop.svg  style="width:32px;"> [Stop](CAM_Stop.md): Inserts a full stop of the machine.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Custom.svg  style="width:32px;"> [Custom](CAM_Custom.md): Inserts custom G-code.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Probe.svg  style="width:32px;"> [Probe](CAM_Probe.md): Creates a Probing Grid from a job stock.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Shape.svg  style="width:32px;"> [From Shape](CAM_Shape.md): Creates a path object from a selected Part object. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Path Modification 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Copy.svg  style="width:32px;"> [Copy the operation in the job](CAM_Copy.md): Creates a parametric Copy of a selected path object.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Array.svg  style="width:32px;"> [Array](CAM_Array.md): Creates an array by duplicating a selected path.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_SimpleCopy.svg  style="width:32px;"> [Simple Copy](CAM_SimpleCopy.md): Creates a non-parametric copy of a selected path object.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Specialty Operations 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_ThreadMilling.svg  style="width:32px;"> [Thread Milling](CAM_ThreadMilling.md): Creates a CAM Thread Milling operation from features of a base object. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Miscellaneous


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Area.svg  style="width:32px;"> [Area](CAM_Area.md): Creates a feature area from selected objects. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/CAM_Area_Workplane.svg  style="width:32px;"> [Area workplane](CAM_Area_Workplane.md): Creates a feature area workplane. [**Experimental**](CAM_experimental.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## ToolBit architecture 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Tools](CAM_Tools.md)
-   [CAM ToolShape](CAM_ToolShape.md)
-   [CAM ToolBit](CAM_ToolBit.md)
-   [CAM ToolBit Library](CAM_ToolBit_Library.md)
-   [CAM ToolController](CAM_ToolController.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Other


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM FAQ](CAM_FAQ.md): The CAM Workbench shares many concepts with other CAM software packages but has its own peculiarities. If something seems wrong this is a good place to start.
-   [CAM SetupSheet](CAM_SetupSheet.md): You can use a SetupSheet to customize how various property values for operations are calculated.
-   [CAM Postprocessor Customization](CAM_Postprocessor_Customization.md): If you have a special machine which cannot use one of the available post-processors you may need to write your own post-processor.
-   [CAM fourth axis](CAM_fourth_axis.md): Experimental four axis milling.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Preferences


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Preferences-cam.svg  style="width:32px;"> [Preferences\...](CAM_Preferences.md): Preferences available for the CAM Workbench.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Scripting


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

See [CAM scripting](CAM_scripting.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Tutorials


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Walkthrough for the Impatient](CAM_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with CAM.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Videos


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): A playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [CAM Workbench](CAM_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): A playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ): A playlist with a series of 8 videos in English by CAD CAM Lessons.
-   Also see the [Computer-Aided Manufacturing (CAM) section](Video_tutorials#Computer-Aided_Manufacturing_(CAM).md) of the [Video tutorials](Video_tutorials.md) wiki page.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Roadmap


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [CAM Development Roadmap](CAM_Development_Roadmap.md): Read this if you are a developer and want to contribute to CAM.


</div>


<div class="mw-translate-fuzzy">


</div>


{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > CAM Workbench/zh-tw
