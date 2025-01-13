# Release notes 1.1
**FreeCAD 1.1 is under development, there is no expected released date yet.**


{{Message|
Are features missing? Mention them in the [https://forum.freecad.org/viewtopic.php?f&#61;10&t&#61;92080 Release notes for v1.1] forum thread.


See [Help FreeCAD](Help_FreeCAD.md) for ways to contribute to FreeCAD.
}}


{{Message|All images on this page must use the **_relnotes_1.1** suffix}}

 

**FreeCAD 1.1** was released on **D Month Year**, get it from the [Download](Download.md) page. This page lists all new features and changes.

Older FreeCAD release notes can be found in the [Feature list](Feature_list#Release_notes.md).

Placeholder for an eye-catching image selected by the admins from the [user showcases forum](https://forum.freecad.org/viewforum.php?f=24).

## General

## User interface 

### Further user interface improvements 

-   A default shortcut for [Std DlgPreferences](Std_DlgPreferences.md) has been added. [Pull request #15536](https://github.com/FreeCAD/FreeCAD/pull/15536)
-   The Notification area preferences page was improved. [Pull request #15207](https://github.com/FreeCAD/FreeCAD/pull/15207)
-   Auto save and additive selection features were added to the [Measure](Std_Measure.md) tool. [Pull request #17717](https://github.com/FreeCAD/FreeCAD/pull/17717)

## Core system and API 

### Core

+++
| <img alt="" src=images/Core_datums_relnotes_1.1.png  style="width:384px;"> | Core Datum tools were implemented to create coordinate systems, datum planes, datum lines and datum points which can be attached and also used in Assembly. [Pull request #18332](https://github.com/FreeCAD/FreeCAD/pull/18332) |
+++

   
  <img alt="" src=images/Core_Transform_relnotes_1.1.gif  style="width:384px;">Click on the image if the animation does not start.   The [Transform](Std_TransformManip.md) tool was overhauled and now allows for precise inputs besides dragging in the 3D view. It is possible to align the interactive dragger to any element in the document and to transform the object in that local (U, V, W) coordinate system of the dragger, or in the global document coordinate system. The dragger can be aligned to the object\'s origin as before, and also to the center of mass of the object. It has a new feature to move the object (at the location of the dragger) to a target location in the document and flip the orientation. [Pull request #17564](https://github.com/FreeCAD/FreeCAD/pull/17564)
   

### API

#### Removed Python API 

#### Changed Python API 

#### New Python API 

## Start

## Addon Manager 

## Assembly Workbench 

-   The [Insert a new part](Assembly_InsertNewPart.md) tool was added making it possible to easily add new parts to assembly. [Pull request #17922](https://github.com/FreeCAD/FreeCAD/pull/17922)
-   The [Create Simulation](Assembly_CreateSimulation.md) tool was added making it possible to add motions to joints and create animations. [Pull request #16414](https://github.com/FreeCAD/FreeCAD/pull/16414)

### Further Assembly improvements 

-   The new core datums can be used for attaching joints to assemble multiple parts. [Pull request #18332](https://github.com/FreeCAD/FreeCAD/pull/18332)

## BIM Workbench 

### Further BIM improvements 

-   The [BIM Views](BIM_Views.md) panel got an overhaul and now has a section for all 2D views. [Pull request #15836](https://github.com/FreeCAD/FreeCAD/pull/15836)
-   NativeIFC support for 2D objects was added to BIM, allowing to embed 2D objects (linework, texts, dimensions) inside IFC files, as well as opening such files from other BIM apps. [Pull request #16629](https://github.com/FreeCAD/FreeCAD/pull/16629)

## CAM Workbench 

### Further CAM improvements 

-   G84/G74 tapping operations were added. [Pull request #8069](https://github.com/FreeCAD/FreeCAD/pull/8069)
-   Multi-pass support was added for profile operations. [Pull request #17326](https://github.com/FreeCAD/FreeCAD/pull/17326)

## Draft Workbench 

### Further Draft improvements 

-   Support for relative font paths has been added to [ShapeStrings](Draft_ShapeString.md). [Pull request #17819](https://github.com/FreeCAD/FreeCAD/pull/17819)
-   The [Draft Fillet](Draft_Fillet.md) command now works on selected edges, instead of the first edge of selected objects. [Pull request #17945](https://github.com/FreeCAD/FreeCAD/pull/17945) and [Pull request #18150](https://github.com/FreeCAD/FreeCAD/pull/18150)
-   The layer menu of the [Draft AutoGroup](Draft_AutoGroup.md) command is sorted alphabetically. [Pull request #18172](https://github.com/FreeCAD/FreeCAD/pull/18172)
-   The handling of Links in [TechDraw DraftViews](TechDraw_DraftView.md) was fixed. [Pull request #18175](https://github.com/FreeCAD/FreeCAD/pull/18175)
-   The position of the *Scale multiplier* field in the UI was improved ([Draft SetStyle](Draft_SetStyle.md), [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md) and [Draft Preferences](Draft_Preferences.md)). [Pull request #18299](https://github.com/FreeCAD/FreeCAD/pull/18299)

## FEM Workbench 

### Further FEM improvements 

-   Log verbosity can now be set for Gmsh in the [Preferences](FEM_Preferences#Gmsh.md). [Pull request #17699](https://github.com/FreeCAD/FreeCAD/pull/17699)
-   The **Second Order Linear** property and support for [local refinement](FEM_MeshRegion.md), previously only available for Gmsh, are now also available for the new [Netgen](FEM_MeshNetgenFromShape.md) implementation. [Pull request #17170](https://github.com/FreeCAD/FreeCAD/pull/17170)
-   Box and elliptical beam section types were added to [FEM ElementGeometry1D](FEM_ElementGeometry1D.md). [Pull request #15843](https://github.com/FreeCAD/FreeCAD/pull/15843)
-   The [Purge results](FEM_ResultsPurge.md) tool now deletes all the results objects, not just the ones native to CalculiX. [Pull request #18328](https://github.com/FreeCAD/FreeCAD/pull/18328)
-   [Tie constraint](FEM_ConstraintTie.md) can now be applied also to shell faces. [Pull request #18325](https://github.com/FreeCAD/FreeCAD/pull/18325)
-   Output format (binary or ASCII) and saving of geometry IDs can now be set for Elmer, also in [Preferences](FEM_Preferences#Elmer.md). [Pull request #17972](https://github.com/FreeCAD/FreeCAD/pull/17972)
-   A smoothing option was added to the [Contours filter](FEM_PostFilterContours.md). [Pull request #18088](https://github.com/FreeCAD/FreeCAD/pull/18088)
-   The *BucklingAccuracy* parameter was added to [CalculiX solver](FEM_SolverCalculixCxxtools.md) - it might be necessary to capture the first eigenvalue in some linear buckling analyses. [Pull request #18790](https://github.com/FreeCAD/FreeCAD/pull/18790)
-   Now all FEM objects for which suppressing makes sense can be suppressed. Previously only constraints were suppressible. [Pull request #18636](https://github.com/FreeCAD/FreeCAD/pull/18636)

## Material Workbench 

### Further Material improvements 

## Mesh Workbench 

### Further Mesh improvements 

## OpenSCAD Workbench 

### Further OpenSCAD improvements 

## Part Workbench 

### Further Part improvements 

-   The [Check geometry](Part_CheckGeometry.md) tool now also has results entries for valid shapes, shows skipped objects and generates reports in the [report view](Report_view.md).

## PartDesign Workbench 

### Further PartDesign improvements 

-   The origin feature in a PartDesign body makes use of the new core datums. The appearance has been changed and the planes enlarge when creating a new sketch. As the orientation was wrong in older FreeCAD versions, files created with these versions need to be converted on opening. It can break files which reference the datums, and converted or new files created with <small>(v1.1)</small>  will be broken in {{VersionMinus|1.0}}. [Pull request #18126](https://github.com/FreeCAD/FreeCAD/pull/18126)
-   The [Toggle freeze](Std_ToggleFreeze.md) command is now available from PartDesign. [Pull request #18373](https://github.com/FreeCAD/FreeCAD/pull/18373)
-   The [Hole feature](PartDesign_Hole.md) can now produce various [Whitworth threads](https://en.wikipedia.org/wiki/British_Standard_Whitworth), following the BSW, BSF, BSP and NPT standards. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)
-   The performance of modelled threads from the [Hole feature](PartDesign_Hole.md) has been improved. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)
-   The initial angle for tapered threads in the [Hole feature](PartDesign_Hole.md) is now automatically set to the value from the ISO 7-1 and ASME B1.20.1 standards. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)

## Points Workbench 

### Further Points improvements 

## Sketcher Workbench 

   
  <img alt="" src=images/Sketcher_defining_external_relnotes_1.1.gif  style="width:384px;">Click on the image if the animation does not start.   [Projection](Sketcher_Projection.md) tool was added making it possible to create defining [external geometry](Sketcher_External.md) and toggle between defining and construction modes for external geometry. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
   

+++
| <img alt="" src=images/Sketcher_intersection_relnotes_1.1.png  style="width:384px;"> | [Intersection](Sketcher_Intersection.md) tool was added making it possible to create [external geometry](Sketcher_External.md) based on the selected reference geometry and the intersection of the sketch plane. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736) |
+++

   
  <img alt="" src=images/Sketcher_external_faces_relnotes_1.1.gif  style="width:384px;">Click on the image if the animation does not start.   [External geometry](Sketcher_External.md) (both projection and intersection) can now be created by selecting a face. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
   

### Further Sketcher improvements 

-   It is now possible to directly use external geometry as input for tools like offset or transform (array), for both external construction and defining geometry. [Pull request #17615](https://github.com/FreeCAD/FreeCAD/pull/17615)
-   External geometry (projected or intersecting) is now by default real (defining) geometry (which does not need to be traced as in 1.0 and prior). It can be toggled to construction geometry as any other geometry [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
-   The Sketcher axes are now displayed with infinite length. [Pull request #17312](https://github.com/FreeCAD/FreeCAD/pull/17312)
-   Sketches are now ordered alphabetically in the [Attach sketch](Sketcher_MapSketch.md) dialog. [Pull request #16518](https://github.com/FreeCAD/FreeCAD/pull/16518)
-   Group dragging was added, making it possible to drag all the selected geometrical entities. [Pull request #18273](https://github.com/FreeCAD/FreeCAD/pull/18273)
-   There is a new preference that, if checked, makes external geometry creation independent of the current construction mode - it is always created as reference geometry in such a case. [Pull request #18697](https://github.com/FreeCAD/FreeCAD/pull/18697)

## Spreadsheet Workbench 

### Further Spreadsheet improvements 

-   Default shortcuts for [Bold text](Spreadsheet_StyleBold.md), [Italic text](Spreadsheet_StyleItalic.md) and [Underline text](Spreadsheet_StyleUnderline.md) have been added. [Pull request #15556](https://github.com/FreeCAD/FreeCAD/pull/15556)
-   Double-clicking on the separator in the header now resizes the column to content. [Pull request #16296](https://github.com/FreeCAD/FreeCAD/pull/16296)
-   Zoom was added to Spreadsheet. [Pull request #16130](https://github.com/FreeCAD/FreeCAD/pull/16130)

## Surface Workbench 

### Further Surface improvements 

## TechDraw Workbench 

### Further TechDraw improvements 

-   The [Insert Area Annotation](TechDraw_AreaDimension.md) tool now properly accounts for holes in faces. [Pull request #17740](https://github.com/FreeCAD/FreeCAD/pull/17740)
-   Shape validation is now available and can be enabled in [Preferences](TechDraw_Preferences#Advanced.md). [Pull request #18282](https://github.com/FreeCAD/FreeCAD/pull/18282)
-   Scaling of SVG symbols has been fixed. [Pull request #18757](https://github.com/FreeCAD/FreeCAD/pull/18757)

## Compilation

## Known limitations 

## Other resources



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.1
