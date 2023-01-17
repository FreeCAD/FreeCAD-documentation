# Release notes 1.0
**FreeCAD 1.0 is under development, there is no expected released date yet.**


{{Message|
Are features missing? Mention them in the [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Release notes for v1.0] forum thread.


See [Help FreeCAD](Help_FreeCAD.md) for ways to contribute to FreeCAD.
}}


{{Message|All images on this page must use the **_relnotes_1.0** suffix}}

 

**FreeCAD 1.0** was released on **DD MM 2023**, get it from the [Download](Download.md) page. This page lists all new features and changes.

Older FreeCAD release notes can be found in the [Feature list](Feature_list#Release_notes.md).

Placeholder for an eye-catching image selected by the admins from the [user showcases forum](https://forum.freecadweb.org/viewforum.php?f=24).

## General

## User interface 

   
  ![](images/Navi_Cube_relnotes_1.0.gif )   The navigation cube corner faces are now hexagonal and bigger, making them easier to click. [Pull request #7876](https://github.com/FreeCAD/FreeCAD/pull/7876).
   

   
  <img alt="" src=images/Measurement-Part_relnotes_1.0.png  style="width:384px;">   The display style of [measurement](Part_Workbench#Measure.md) results created using the [Part](Part_Workbench.md) or [PartDesign](PartDesign_Workbench.md) workbench can now be changed in the [preferences](PartDesign_Preferences#Measure.md). [Pull request #7148](https://github.com/FreeCAD/FreeCAD/pull/7148)
   

   
  <img alt="" src=images/WbSelector_relnotes_1.0.png  style="width:300px;">   The workbench selector can now optionally be put in the menubar instead of the toolbar area. [Pull request #7679](https://github.com/FreeCAD/FreeCAD/pull/7679)
   

### Further user interface improvements 

-   The button for <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> [Edit Mode](Std_UserEditMode.md) has been removed from the standard toolbar. It can be re-added by [customizing](Std_DlgCustomize.md) your toolbar. [Pull request #7570](https://github.com/FreeCAD/FreeCAD/pull/7570)
-   The buttons for <img alt="" src=images/Std_Print.svg  style="width:24px;"> [Print](Std_Print.md), <img alt="" src=images/Std_Copy.svg  style="width:24px;"> [Copy](Std_Copy.md), <img alt="" src=images/Std_Paste.svg  style="width:24px;"> [Paste](Std_Paste.md) and <img alt="" src=images/Std_Cut.svg  style="width:24px;"> [Cut](Std_Cut.md) have been removed from the standard toolbar. They can be re-added by [customizing](Std_DlgCustomize.md) your toolbar. [Pull request #7571](https://github.com/FreeCAD/FreeCAD/pull/7571) and [commit ea9a04e](https://github.com/FreeCAD/FreeCAD/commit/ea9a04e)
-   Commands to [store](Std_StoreWorkingView.md) and [recall](Std_RecallWorkingView.md) a temporary working view have been added. [Pull request #7525](https://github.com/FreeCAD/FreeCAD/pull/7525)
-   Value changes with the mouse wheel in \'input fields\' (a widget type used to enter values in task panels, for example by [Draft Line](Draft_Line.md)) are disabled if the widget doesn\'t have the focus and the [ComboBoxWheelEventFilter](Fine-tuning#Mouse_related.md) parameter is enabled. This prevents unwanted value changes while scrolling, as was already the case for spin and combo boxes. [Pull request #7561](https://github.com/FreeCAD/FreeCAD/pull/7561)
-   It is now possible to set a default transparency for new [Part](Part_Module.md) or [PartDesign](PartDesign_Workbench.md) objects in the [Preferences](PartDesign_Preferences.md). [Pull request #7103](https://github.com/FreeCAD/FreeCAD/pull/7103)
-   There is the new orbit style **Free Turntable**. It can either be enabled in the [Preferences](Preferences_Editor#Navigation.md) or by pressing the **[<img src=images/NavigationCAD_dark.svg style="width:16px">** button in the [Status bar](Status_bar.md) and then using the menu **Settings → Orbit**). [Pull Request #8048](https://github.com/FreeCAD/FreeCAD/pull/8048)
-   The [Std SetAppearance](Std_SetAppearance.md) task panel now also has a button to set the Point Color property. [Pull request #7708](https://github.com/FreeCAD/FreeCAD/pull/7708)
-   A button has been added to switch the colors of the [3D view](3D_view.md) background gradient in the [Preferences](Preferences_Editor#Colors.md). [Pull request #7155](https://github.com/FreeCAD/FreeCAD/pull/7155)
-   All transparency settings use now the uniform spin button step of 5%: One click on the button in a dialog or the [property editor](Property_editor.md) changes the transparency by 5%. Keep the button pressed to change several 5% steps at once. [Pull request #7723](https://github.com/FreeCAD/FreeCAD/pull/7723)
-   The Output window has been renamed to Report view for uniformity with the UI. [Pull Request #7739](https://github.com/FreeCAD/FreeCAD/pull/7739)

## Core system and API 

### Core

### API




<div class="mw-collapsible mw-collapsed toccolours">



#### New Python API 




<div class="mw-collapsible-content">
-   *BSplineSurfacePy::scaleKnotsToBounds*: Scales the U and V knots lists to fit the specified bounds. [Pull request #7258](https://github.com/FreeCAD/FreeCAD/pull/7258) and [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)
-   *BSplineCurvePy::scaleKnotsToBounds*: Scales the knots list to fit the specified bounds. [Pull request #7385](https://github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy*: Root class for fixing operations. [commit 4d4adb93](https://github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy*: Fixing invalid edge. [commit 4089cbfb](https://github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy*: Rebuilds connectivity between faces in shell. [commit a0eb2e9d](https://github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy*: Class for fixing operations on faces. [commit b6cd635c](https://github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy*: Class for fixing operations on faces. [commit 4c2946c8](https://github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy*: Fixing solids with small size. [commit b70d8d37](https://github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix_FreeBoundsPy*: Intended to output free bounds of the shape. [commit 1ee1aee1](https://github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix_RootPy*: Root class for fixing operations. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_ShapePy*: Class for fixing operations on shapes. [commit 87db9dcc](https://github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix_ShapeTolerancePy*: Modifies tolerances of sub-shapes (vertices, edges, faces). [commit 125d5b63](https://github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix_ShellPy*: Root class for fixing operations. [commit f3e941a3](https://github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_SolidPy*: Root class for fixing operations. [commit 8d568793](https://github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix_SplitCommonVertexPy*: Class for fixing operations on shapes. [commit 4b44c54c](https://github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix_SplitToolPy*: Tool for splitting and cutting edges. [commit bbecc3f2](https://github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix_WireframePy*: Provides methods for fixing wireframe of shape. [commit 6843a461](https://github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix_WirePy*: Class for fixing operations on wires. [commit 94f6279a](https://github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix_WireVertexPy*: Fixing disconnected edges in the wire. [commit 8c6ffc99](https://github.com/FreeCAD/FreeCAD/commit/8c6ffc99)




</div>



#### Removed Python API 

-   *FreeCAD.EndingAdd*: replaced by *FreeCAD.addImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)
-   *FreeCAD.EndingGet*: replaced by *FreeCAD.getImportType*. [Pull request #7167](https://github.com/FreeCAD/FreeCAD/pull/7167)




</div>



## Addon Manager 

## Arch Workbench 

-   Several edit mode issues have been fixed and the [Tree view](Tree_view.md) context menus for Arch objects have been improved. Objects that can be edited now have an **Edit** option in that menu. The **Set colors** option was removed for objects without a face or that can only have a single face. [Pull request #8122](https://github.com/FreeCAD/FreeCAD/pull/8122)

### Further Arch improvements 

-   [Profile](Arch_Profile.md) objects now support modification of the profile type after creation. [Pull request #7217](https://github.com/FreeCAD/FreeCAD/pull/7217)

## Draft Workbench 

-   The inaccuracy of [Draft Snap Near](Draft_Snap_Near.md) when snapping to curves was fixed. In addition, [Draft Snap Perpendicular](Draft_Snap_Perpendicular.md) can now also snap to faces and find multiple points. To snap to a vertex (e.g. a [Draft Point](Draft_Point.md)) [Draft Snap Endpoint](Draft_Snap_Endpoint.md) must now be used instead of [Draft Snap Near](Draft_Snap_Near.md). [Pull request #7132](https://github.com/FreeCAD/FreeCAD/pull/7132)
-   To make working with [layers](Draft_Layer.md) easier their drag and drop behavior was modified. If you drop an object from a [Std Group](Std_Group.md), or a group-like object such as an [Arch BuildingPart](Arch_BuildingPart.md), on a layer, it is no longer removed from the group, and vice versa. This works without holding down the **Ctrl** key. [Pull request #7462](https://github.com/FreeCAD/FreeCAD/pull/7462)
-   The [Draft PointArray](Draft_PointArray.md) command now supports more point object types. Any object with a shape and vertices, as well as a [mesh](Mesh_Workbench.md) and a [point cloud](Points_Workbench.md) can be used. [Pull request #7597](https://github.com/FreeCAD/FreeCAD/pull/7597)
-   The [Tree view](Tree_view.md) context menus for Draft objects have been improved. Objects that can be edited with the [Draft Edit](Draft_Edit.md) command, or that have a dedicated edit solution, now have an **Edit** option in that menu. The **Set colors** option was removed for objects without a face or that can only have a single face. [Pull request #7970](https://github.com/FreeCAD/FreeCAD/pull/7970)
-   The properties of Draft annotation objects have been unified. [Draft Text](Draft_Text.md), [Draft Dimension](Draft_Dimension.md) and [Draft Label](Draft_Label.md) objects now all have a Font Name, a Font Size and a Text Color property. The Display Mode options have been made consistent as well and are now: Screen and World. [Issue #7861](https://github.com/FreeCAD/FreeCAD/issues/7861) and [Pull request #8081](https://github.com/FreeCAD/FreeCAD/pull/8081)

### Further Draft improvements 

-   Several [Draft PathArray](Draft_PathArray.md) related issues have been fixed. [Pull request #7506](https://github.com/FreeCAD/FreeCAD/pull/7506) and [Pull request #7662](https://github.com/FreeCAD/FreeCAD/pull/7662)
-   The [Draft Edit](Draft_Edit.md) command has received several improvements. For [wires](Draft_Wire.md), [B-splines](Draft_BSpline.md) and [Bézier curves](Draft_BezCurve.md) a Close/Open option has been added to the edge context menu. For B-splines and Bézier curves a Reverse option has been added to the same menu as well. The task panels have been cleaned up. [Pull request #7527](https://github.com/FreeCAD/FreeCAD/pull/7527) and [Pull request #7541](https://github.com/FreeCAD/FreeCAD/pull/7541)
-   The [Draft Snap](Draft_Snap.md) toolbar was changed to a standard toolbar. Keyboard shortcuts can now be assigned to snaps. But using them during a command only works if none of the input boxes in the task panel has the focus as they \'catch\' the so-called in-command shortcuts. [Pull request #7656](https://github.com/FreeCAD/FreeCAD/pull/7656)
-   In the task panel of the [Draft SetStyle](Draft_SetStyle.md) command the \"Texts/dims\" button has been replaced by the \"Annotations\" button. Pressing this button will process all annotations, including [Draft Labels](Draft_Label.md). Several minor additional issues were also fixed. [Pull request #8190](https://github.com/FreeCAD/FreeCAD/pull/8190), [Pull request #8195](https://github.com/FreeCAD/FreeCAD/pull/8195) and [Pull request #8196](https://github.com/FreeCAD/FreeCAD/pull/8196)

## FEM Workbench 

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_1.0.png  style="width:384px;">Simulation result where 8 mesh regions are visible (one for every CPU core used).   It is now possible to run the solver [Elmer](FEM_SolverElmer.md) using multiple CPU cores. For more info about the caveats, see [this forum post](https://forum.freecadweb.org/viewtopic.php?p=610617#p610617) [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
   

### Further FEM improvements 

-   There is now an <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [initial pressure constraint](FEM_ConstraintInitialPressure.md) to set the initial internal pressure of fluids. [Pull request #7364](https://github.com/FreeCAD/FreeCAD/pull/7364)
-   The <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:24px;"> [body heat source constraint](FEM_ConstraintBodyHeatSource.md) now has a task panel and it is possible to set the heat for several bodies or to use several constraints for different bodies in one analysis. [Pull request #7367](https://github.com/FreeCAD/FreeCAD/pull/7367)
-   It is now possible to open (and this way visualize) \*.pvtu files (partitioned VTK unstructured grid data). A \*.pvtu file is also the result of an [Elmer](FEM_SolverElmer.md) simulation, when more than one CPU core was used. [Pull request #7159](https://github.com/FreeCAD/FreeCAD/pull/7159)
-   Critical Strain Ratio has been added to the VTK result pipeline. It gives an indication of ductile rupture for materials with a \"MaterialMechanicalNonlinear\" object. [Pull request #7467](https://github.com/FreeCAD/FreeCAD/pull/7467)
-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:24px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh.md) enables to define the scale of deformed mesh using Python. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=71936) and [Pull request #7715](https://github.com/FreeCAD/FreeCAD/pull/7715)

## Export

## Mesh

### Further Mesh improvements 

-   Support to add transparencies to a mesh. [Forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=72531) and [Commit f88305e](https://github.com/FreeCAD/FreeCAD/commit/f88305e)

## OpenSCAD Workbench 

## Part Workbench 

### Further Part improvements 

## PartDesign Workbench 

   
  <img alt="" src=images/PD_Counterdrill_relnotes_1.0.png  style="width:384px;">A counterdrill hole.   The [Hole](PartDesign_Hole.md) dialog supports the screw head type *Counterdrill*. [Pull request #7562](https://github.com/FreeCAD/FreeCAD/pull/7562)
                                                                                                                            
   

### Further PartDesign improvements 

-   In the [Hole](PartDesign_Hole.md) dialog, the deprecated screw head types (cheese head, cap screw etc.) have been removed. They were deprecated since FreeCAD 0.19. Holes using these types are transformed to custom countersinks/counterbore holes with the diameter and depth used by the types. [Pull request #7654](https://github.com/FreeCAD/FreeCAD/pull/7654)
-   The [Validate sketch](Sketcher_ValidateSketch.md) command was added to Helper toolbar. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)
-   The unusable [Leave sketch](Sketcher_LeaveSketch.md) and [View sketch](Sketcher_ViewSketch.md) commands were removed from the menu. The [Edit sketch](Sketcher_EditSketch.md), [Merge sketches](Sketcher_MergeSketches.md) and [Mirror sketch](Sketcher_MirrorSketch.md) commands were added to the menu. [Pull request #7700](https://github.com/FreeCAD/FreeCAD/pull/7700)

## Path Workbench 

-   Camotics integration. If camotics (version 1.2.2 or later) is installed, a new icon will be added to the Path toolbar. Select a Path Job and press the button to open the Camotics dialog. Then drag the slider to generate a simulated solid at any point in the job. You can also launch the full camotics application to run the animated simulaton. This results in a silent post-processing of the job and creation of a camotics project file. [Pull request #6637](https://github.com/FreeCAD/FreeCAD/pull/6637)

-   Additional substitution strings for automatic output naming. If output is being split into multiple files, the filenames can automatically substitute the toolcontroller label, WCS, or operation label. This is in addition to the other existing substitution strings like date, job name, etc.

-   Implemented Chipbreaking option for peck style drill cycles. Chipbreaking emits a G73 cycle which causes the control to make a very small retraction move to break the chip without fully retracting the bit from the hole. G73 is supported natively by LinuxCNC. Some other postprocessors will have to interpret the G73 and emit control appropriate codes or decompose the retraction into G1/G0 moves. Postprocessor support for G73 decomposition has been added to the \"refactored\" postprocessors.[Pull request #7469](https://github.com/FreeCAD/FreeCAD/pull/7469)

## Plot module 

## Sketcher Workbench 

   
  <img alt="" src=images/Constrain_B-spline_knots_relnotes_1.0.gif  style="width:384px;">Dragging of B-spline knots.Click on the image to see the animation.   B-spline knots can now be dragged around and constrained like any other sketch point. [Pull request #7484](https://github.com/FreeCAD/FreeCAD/pull/7484)
                                                                                                                                                                                                           
   

   
  <img alt="" src=images/sketcher-move-piece_relnotes_1.0.gif  style="width:384px;">Dragging of a B-spline.Click on the image if the animation does not start.   Dragging a B-spline now only moves the part between knots. [Pull request #7110](https://github.com/FreeCAD/FreeCAD/pull/7110)
                                                                                                                                                                                                        
   

   
  <img alt="" src=images/Sketcher_BackEdit_relnotes_1.0.gif  style="width:384px;">Click on the image to see the animation.   Possibility to seamlessly edit sketches from the front or back. When working from the back, vertices (and all geometries and constraints) are equally selectable and the section view is switched automatically. [Pull request #7417](https://github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                                                                                    
   

   
  <img alt="" src=images/Sketcher_Element_Widget_relnotes_1.0.gif  style="width:384px;">Click on the image to see the animation.   The Element widget has been reworked to simplify the UI and enable simpler selection of the different parts of each geometry: Edge, start point, end point and mid point. [Pull request #7567](https://github.com/FreeCAD/FreeCAD/pull/7567)
                                                                                                                                                                
   

   
  <img alt="" src=images/Sketcher_Join_Curves_relnotes_1.0.gif  style="width:384px;">Click on the image to see the animation.   The [Join curves](Sketcher_JoinCurves.md) tool has been added. It can combine multiple curves into a single B-spline. [Pull request #6507](https://github.com/FreeCAD/FreeCAD/pull/6507)
                                                                                                                                                          
   

### Further Sketcher improvements 

-   The toolbar button for [Constrain refraction (Snell\'s law)](Sketcher_ConstrainSnellsLaw.md) has been removed. [Commit ef62fc3](https://github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   The [Dimensional Constraints](Sketcher_Workbench#Dimensional_constraints.md) and Quantity Spin Boxes now support the same math as [Expressions](Expressions.md) (Evaluated in place). [Pull Request #7124](https://github.com/FreeCAD/FreeCAD/pull/7124)
-   The toolbar buttons for [Select redundant constraints](Sketcher_SelectRedundantConstraints.md) and [Select conflicting constraints](Sketcher_SelectConflictingConstraints.md) have been removed. [Pull request #7568](https://github.com/FreeCAD/FreeCAD/pull/7568)
-   The toolbar button for [Stop operation](Sketcher_StopOperation.md) has been removed. [Pull request #7569](https://github.com/FreeCAD/FreeCAD/pull/7569)
-   The \'Edit controls\' section in the Sketcher dialog has been made optional. [Pull request #7572](https://github.com/FreeCAD/FreeCAD/pull/7572)
-   The toolbar button for [Select unconstrained DoF](Sketcher_SelectElementsWithDoFs.md) has been removed. [Pull request #7603](https://github.com/FreeCAD/FreeCAD/pull/7603)
-   The Sketcher toolbar has been split in two: \'Sketcher-edit-mode\' and \'Sketcher\' (i.e. \'not edit mode\'). The Sketcher toolbars that are only for edit-mode are hidden in non-edit-mode, and those only for non-edit-mode are hidden in edit-mode. The Structure toolbar is also hidden in Sketcher. [Pull request #7655](https://github.com/FreeCAD/FreeCAD/pull/7655)
-   [Coincident constraint](Sketcher_ConstrainCoincident.md) can now act as a concentric constraint when selecting 2 or more circles, arcs, ellipses or arcs of ellipses. [Pull request #7703](https://github.com/FreeCAD/FreeCAD/pull/7703)
-   [Carbon copy](Sketcher_CarbonCopy.md) if possible now uses constraint names in the expressions it creates instead of an index based reference, making it more reliable. [Pull request #7688](https://github.com/FreeCAD/FreeCAD/pull/7688)

## Spreadsheet Workbench 

### Further Spreadsheet improvements 

## TechDraw Workbench 

   
  <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_1.0.png  style="width:250px;">   The [SurfaceFinishSymbol](TechDraw_SurfaceFinishSymbol.md) tool was added to allow for the creation of surface finish symbols describing roughness, lay and waviness, but also denoting the type of surface treatment. It supports both ISO and ASME styles. As shown in the image, the existing [LeaderLine](TechDraw_LeaderLine.md) tool can be used to properly refer oriented symbols to the edges of an object. [Pull request #7227](https://github.com/FreeCAD/FreeCAD/pull/7227)
  <img alt="" src=images/TechDraw_ComplexSection_relnotes_1.0.png  style="width:250px;">               The [ComplexSection](TechDraw_ComplexSection.md) tool was added. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
                                                                                                                      
   

### Further TechDraw improvements 

-   Navigation modes have been updated to match those used in the 3D view. [Pull request #7081](https://github.com/FreeCAD/FreeCAD/pull/7081) and [Pull request #7107](https://github.com/FreeCAD/FreeCAD/pull/7107)
-   Bitmap hatching was fixed. [Issue #6582](https://github.com/FreeCAD/FreeCAD/issues/6582) and [Pull request #7121](https://github.com/FreeCAD/FreeCAD/pull/7121)
-   Support for adjustable gaps for extension lines of [dimensions](TechDraw_Preferences#Dimensions.md) was added. [Pull request #7133](https://github.com/FreeCAD/FreeCAD/pull/7133)
-   Multithreading was introduced for hidden line removal and face finding. [Pull request #7377](https://github.com/FreeCAD/FreeCAD/pull/7377)
-   The face detection algorithm was improved. [Pull request #7448](https://github.com/FreeCAD/FreeCAD/pull/7448)
-   The [PrintAll](TechDraw_PrintAll.md) tool was added. [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   [Four tools](TechDraw_StackGroup.md) to control the stacking order of views were added. [Issue #6012](https://github.com/FreeCAD/FreeCAD/issues/6012) and [Pull request #7460](https://github.com/FreeCAD/FreeCAD/pull/7460)
-   [ActiveView](TechDraw_ActiveView.md) now creates a screen capture instead of an SVG image. [Pull request #7471](https://github.com/FreeCAD/FreeCAD/pull/7471)
-   All Latin script templates have been converted to \"plain svg\". [Pull request #7472](https://github.com/FreeCAD/FreeCAD/pull/7472)
-   A preview was added to the task panel of the [SectionView](TechDraw_SectionView.md) tool. [Pull request #7658](https://github.com/FreeCAD/FreeCAD/pull/7658)
-   Removed deprecated functions: DrawViewPart::replaceCenterLine, DrawViewPart::replaceCosmeticEdge, DrawViewPart::replaceCosmeticVertex and DrawViewPart::replaceGeomFormat.

## Web

## External workbenches 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Compilation

Since this release FreeCAD can only be compiled using Qt 5.x and Python 3.x. The lowest supported Python version is 3.8 according to the [FreeCAD 1.0 development goals](FreeCAD_1.0_Development_Cycle.md).

To compile FreeCAD see the instructions for [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) and [MacOS](Compile_on_MacOS.md).

The supported operating systems are:

-   Windows 7, 8, 10 and 11
-   Linux Ubuntu Focal Fossa (20.04) and newer
-   MacOS: 10.12 Sierra or newer

## Known Limitations 

### 32bit Windows 

Since FreeCAD 0.19 we no longer officially support 32bit Windows. FreeCAD might work on these systems, but no support is given.

### Remote Desktop under Windows 

Depending on the OpenGL graphics capabilities of a computer, it might be that one encounters a crash when running FreeCAD via remote desktop. To fix this upgrade your OpenGL driver. Only if this doesn\'t help:

-   Download [this](https://downloads.fdossena.com/geth.php?r=mesa64-latest) OpenGL library for 64bit Windows and extract it.
-   Rename the DLL file to *opengl32sw.dll* and copy it to the *bin* subfolder of FreeCAD\'s installation folder (overwrite the existing DLL there).

### MacOS: Start Workbench shows blank page 

If the [Start Workbench](Start_Workbench.md) shows only a blank page, you must enable the option **Use software OpenGL** in the menu **Edit → Preferences → Display**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0
