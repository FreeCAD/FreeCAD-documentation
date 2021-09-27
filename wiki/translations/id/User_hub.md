# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/id

------------------------------------------------------------------------



This is the main help area for newcomers to FreeCAD.

These pages are in continuous development, so there may be missing or outdated information. If you cannot find the information that you need, don\'t hesitate to ask in the [FreeCAD forum](http://forum.freecadweb.org).

If you\'d like to contribute to FreeCAD, please _ for the general guidelines that you should follow.

If you would like to know how FreeCAD started years ago visit the [History](History.md) page.

## Using FreeCAD 

### Introduction

-   [Application Overview](About_FreeCAD.md): A general overview of FreeCAD
-   Installing: How to install FreeCAD on [Windows](Installing_on_Windows.md), [Linux](Installing_on_Linux.md) and [Mac](Installing_on_Mac.md)
-   [Installing help files](Installing_Helpfile.md): how to install the offline documentation which is based on this wiki.
-   [Installing additional components](Installing_additional_components.md): how to install additional third-party components that can work together with FreeCAD.
-   [Getting started](Getting_started.md): A quick overview of the available tools
-   [FAQ](Frequently_asked_questions.md): Frequently asked questions
-   [Tutorials](Tutorials.md) covering different parts of FreeCAD

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)

### Basic application 

-   _, the [tree view](Tree_view.md), the [property editor](Property_editor.md), the [task panel](Task_panel.md), and the [Python console](Python_console.md).
-   [Mouse navigation](Mouse_navigation.md): the different types of using the mouse or trackpad to navigate in the 3D view.
-   [Selection methods](Selection_methods.md): the different methods of selecting objects in the software.
-   [Object name](Object_name.md): all objects have a read-only `Name` that uniquely identifies them, and a `Label` which is user editable.
-   [Preferences Editor](Preferences_Editor.md): the system that allows you to control many properties of the base system and of the individual workbenches.
-   [File formats](Import_Export.md): the different file formats that FreeCAD can read and write.

### Workbenches

[Workbenches](Workbenches.md) are collections of tools used for specific tasks. These are the base workbenches bundled with every FreeCAD installation:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](Constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Macros

[Macros](Macros.md) are relatively small snippets of [Python](Python.md) code that perform a simple or a complex task that is not available in the base FreeCAD system.

Power users have written various [macros](macros.md) to enhance FreeCAD with more capabilities.

Since FreeCAD 0.17, many macros can be installed using the [Addon Manager](Std_AddonMgr.md). For a list of the macros refer to the [Macros recipes](Macros_recipes.md) page. For manual installation see [How to install macros](How_to_install_macros.md).

### External workbenches 

When many macros or functions are developed together, and are organized in toolbars and menus, they can become a new workbench.

[External workbenches](External_workbenches.md) are collections of functions that are not part of the base FreeCAD system, usually developed by experienced users, and targeting a particular need.

Since FreeCAD 0.17, many workbenches can be installed using the [Addon Manager](Std_AddonMgr.md). For manual installation see [How to install additional workbenches](How_to_install_additional_workbenches.md).

## Reference

-   [Commands Reference](List_of_Commands.md): A complete list of the available FreeCAD commands.

## Online Help 

This is the official FreeCAD online help. Please note that the whole online help system is currently being reworked. It will be used to generate a .CHM file, that will be distributed with the binary packages of FreeCAD. At the moment the online help summarizes some of the most complete sections of this wiki.

-   [Online help system - Table of Contents](Online_Help_Toc.md)

## More

-   The [Power users hub](Power_users_hub.md) is the place to go if you would like to see more advanced use of FreeCAD
-   The [FreeCAD Community Portal](FreeCAD_Community_Portal.md) lists projects made by community members around FreeCAD.
-   Don\'t understand a term or phrase as used in FreeCAD? Try the [Glossary](Glossary.md) page.




_

---
[documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/id
