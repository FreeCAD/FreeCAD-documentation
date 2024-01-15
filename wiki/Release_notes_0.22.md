# Release notes 0.22
**FreeCAD 0.22 is under development, there is no expected released date yet.**


{{Message|
Are features missing? Mention them in the [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;80197 Release notes for v0.22] forum thread.


See [Help FreeCAD](Help_FreeCAD.md) for ways to contribute to FreeCAD.
}}


{{Message|All images on this page must use the **_relnotes_0.22** suffix}}

 

**FreeCAD 0.22** was released on **D Month 2024**, get it from the [Download](Download.md) page. This page lists all new features and changes.

Older FreeCAD release notes can be found in the [Feature list](Feature_list#Release_notes.md).

Placeholder for an eye-catching image selected by the admins from the [user showcases forum](https://forum.freecadweb.org/viewforum.php?f=24).

## General

## User interface 

+++
| <img alt="" src=images/Rotation_Center_Indicator_relnotes_0.22.gif  style="width:320px;"> | A rotation center indicator has been added. This indicator is shown when the view is rotated by dragging the mouse. It can optionally be disabled in the preferences. There are also settings for its color, transparency and size. [Pull request #9909](https://github.com/FreeCAD/FreeCAD/pull/9909) and [Pull request #10790](https://github.com/FreeCAD/FreeCAD/pull/10790) |
+++

   
  <img alt="" src=images/Selection_filters_relnotes_0.22.gif  style="width:320px;">Click on the image if the animation does not start.   Selection filters were added, facilitating the selection of vertices, edges and faces. [Pull request #10271](https://github.com/FreeCAD/FreeCAD/pull/10271)
   

+++
| <img alt="" src=images/Tasks_Dockable_relnotes_0.22.png  style="width:320px;"> | For more flexibility, the task panel is now a a stand-alone dockable widget but the old layout has been kept as the default. [Pull request #10681](https://github.com/FreeCAD/FreeCAD/pull/10681) and [Pull request #10848](https://github.com/FreeCAD/FreeCAD/pull/10848) |
+++

+++
| <img alt="" src=images/Transform_tool_relnotes_0.22.png  style="width:320px;"> | The appearance of the [Transform](Std_TransformManip.md) tool dragger has been improved. It now also has a set of planar draggers for moving objects along the 3 default planes. [Pull request #10706](https://github.com/FreeCAD/FreeCAD/pull/10706) |
+++

+++
| <img alt="" src=images/Overlay_relnotes_0.22.png  style="width:320px;"> | Realthunder\'s feature allowing for the overlay of dock widgets (tree and task transparency) has been added. [Pull request #7888](https://github.com/FreeCAD/FreeCAD/pull/7888) |
+++

+++
| <img alt="" src=images/Light_source_relnotes_0.22.PNG  style="width:320px;"> | The light source position can now be set in in the preferences (Preferences → Display). [Pull request #11146](https://github.com/FreeCAD/FreeCAD/pull/11146) |
+++

+++
| <img alt="" src=images/Preference_tree_relnotes_0.22.png  style="width:320px;"> | The Preferences window was redesigned to replace the tabs with a tree view. [Pull request #11018](https://github.com/FreeCAD/FreeCAD/pull/11018) |
+++

### Further user interface improvements 

-   A project unit system was introduced. [Pull request #9521](https://github.com/FreeCAD/FreeCAD/pull/9521)
-   The [Section Cut](Part_SectionCut.md) tool now also works in a perspective view. [Pull request #10143](https://github.com/FreeCAD/FreeCAD/pull/10143)
-   An option to sort workbenches alphabetically (available after right-clicking in Preferences → Workbenches) was added. [Pull request #10363](https://github.com/FreeCAD/FreeCAD/pull/10363)
-   A **Find file** filter and a **Find in files** filter were added to the [Std DlgMacroExecute](Std_DlgMacroExecute.md) dialog. [Pull request #10714](https://github.com/FreeCAD/FreeCAD/pull/10714)
-   The [View menu](Std_View_Menu.md) and the View toolbar have been revised. [Pull request #10761](https://github.com/FreeCAD/FreeCAD/pull/10761)
-   The stop button was removed from the [Macro toolbar](Macros.md). The [record button](Std_DlgMacroRecord.md) now switched to a stop button when recording is in progress. [Pull request #10836](https://github.com/FreeCAD/FreeCAD/pull/10836)
-   The reset button in the Preferences now shows a menu with options to reset the settings at different levels: all, in the current group or in the current tab. [Pull request #10688](https://github.com/FreeCAD/FreeCAD/pull/10688) and [Pull request #11038](https://github.com/FreeCAD/FreeCAD/pull/11038)
-   The Help Module was merged so that it\'s no longer necessary to download an add-on to make use of it. [Pull request #11008](https://github.com/FreeCAD/FreeCAD/pull/11008)
-   Preferences to customize the current theme were added. [Pull request #10238](https://github.com/FreeCAD/FreeCAD/pull/10238)
-   Default selection settings were changed to make the selection of objects in the 3D window easier. [Pull request #11187](https://github.com/FreeCAD/FreeCAD/pull/11187)
-   A meters-only unit scheme named **Meter decimal** was added since the MKS (m/kg/s/degree) system doesn\'t always result in dimensions being displayed in meters - millimeters are still used for values below 0.1 m while for some applications (e.g. civil engineering) a unit system that actually changes the display of all dimensions to meters is useful. [Pull request #11365](https://github.com/FreeCAD/FreeCAD/pull/11365)
-   Additional marker sizes (20, 25 and 30px) were added to *Preferences → Display → 3D View → Marker size* in order to assist users of 4K screens. [Pull request #11524](https://github.com/FreeCAD/FreeCAD/pull/11524)
-   A *Toggle transparency* option was added to the View and context menus to quickly switch transparency on or off for selected objects. [Pull request #10805](https://github.com/FreeCAD/FreeCAD/pull/10805)
-   A Lock toolbars command was added. With it toolbar positions can be locked or unlocked. It is available in the View menu and the toolbar area context menu. [Pull request #11596](https://github.com/FreeCAD/FreeCAD/pull/11596)

## Core system and API 

### Core

-   Vector functions from the [Vector API](Vector_API.md) can now be used in [Expressions](Expressions.md). [Pull request #8603](https://github.com/FreeCAD/FreeCAD/pull/10237).
-   The file list in the [Macro Execute dialog](Std_DlgMacroExecute.md) can now be filtered both by file name and by file content. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/10714).
-   The python editor now matches indentation of the previous line when pressing the enter key. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/11356).

### API

#### New Python API 

-    {{Incode|getUpDirection}}: Gets the up-direction from a View3DInventor view. [Pull request #10060](https://github.com/FreeCAD/FreeCAD/pull/10060)

#### Removed Python API 

## Addon Manager 

## Arch Workbench 

-   The [Arch CutPlane](Arch_CutPlane.md) command has been improved. It is now nesting and link aware and the selection is more flexible. Edges can also be selected making the Arch CutLine command obsolete. [Pull request #11254](https://github.com/FreeCAD/FreeCAD/pull/11254) and [Pull request #11792](https://github.com/FreeCAD/FreeCAD/pull/11792)

### Further Arch improvements 

## Draft Workbench 

-   A justification option and several related properties have been added to [Draft ShapeStrings](Draft_ShapeString.md). [Pull request #10233](https://github.com/FreeCAD/FreeCAD/pull/10233)
-   [Radial dimensions](Draft_Dimension#Usage_radial_dimension.md) now only show a single arrow. [Pull request #10655](https://github.com/FreeCAD/FreeCAD/pull/10655)
-   An Oblique Angle property has been added to [Draft ShapeStrings](Draft_ShapeString.md). [Pull request #10783](https://github.com/FreeCAD/FreeCAD/pull/10783)
-   Support for hyperlinks has been added. Hyperlinks, to local and remote files and URLs, in [Draft Texts](Draft_Text.md) and [Draft Labels](Draft_Label.md) can be opened from the their [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu. [Pull request #10878](https://github.com/FreeCAD/FreeCAD/pull/10878)
-   The [Draft working plane](Draft_SelectPlane.md) code has been reworked. There is now a working plane per 3D view. [Pull request #11010](https://github.com/FreeCAD/FreeCAD/pull/11010)
-   The history feature and the alignment options of the [Draft SelectPlane](Draft_SelectPlane.md) command have been improved. [Pull request #11062](https://github.com/FreeCAD/FreeCAD/pull/11062)
-   The behavior of the [grid](Draft_ToggleGrid.md) has been improved. Its visibility is now stored per 3D view. When switching to a different workbench all grids are hidden (a [fine-tuning](Fine-tuning.md) parameter is available to disable this). [Pull request #11336](https://github.com/FreeCAD/FreeCAD/pull/11336)
-   The Draft preferences have been checked and improved. Some preferences have been added, obsolete preferences have been removed. The pages in the [Preferences Editor](Preferences_Editor.md) have a new layout and show units where applicable. Restarting FreeCAD after changing a Draft preference is no longer required. [Pull request #11379](https://github.com/FreeCAD/FreeCAD/pull/11379), [Pull request #11503](https://github.com/FreeCAD/FreeCAD/pull/11503), [Pull request #11512](https://github.com/FreeCAD/FreeCAD/pull/11512), [Pull request #11550](https://github.com/FreeCAD/FreeCAD/pull/11550), [Pull request #11579](https://github.com/FreeCAD/FreeCAD/pull/11579), [Pull request #11585](https://github.com/FreeCAD/FreeCAD/pull/11585), [Pull request #11677](https://github.com/FreeCAD/FreeCAD/pull/11677) and [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694)

### Further Draft improvements 

-   [Draft Facebinders](Draft_Facebinder.md) can now handle faces belonging to links and faces nested in [Std Parts](Std_Part.md). [Pull request #11081](https://github.com/FreeCAD/FreeCAD/pull/11081)
-   Some settings have been added to the [Draft SetStyle](Draft_SetStyle.md) command. [Pull request #11593](https://github.com/FreeCAD/FreeCAD/pull/11593) and [Pull request #11694](https://github.com/FreeCAD/FreeCAD/pull/11694)
-   Settings have also been added to the [Draft ApplyStyle](Draft_ApplyStyle.md) command. [Pull request #11610](https://github.com/FreeCAD/FreeCAD/pull/11610)
-   Snap, edit and tracker markers now use the [Marker size](Preferences_Editor#3D_View.md) preference. [Pull request #11688](https://github.com/FreeCAD/FreeCAD/pull/11688)

## FEM Workbench 

+++
| <img alt="" src=images/FEM_legend_labels_relnotes_0.22.PNG  style="width:384px;"> | The position of the color legend labels was adjusted to make the top ones less likely to be covered by the navigation cube. The default font and color of the labels was changed to increase the visibility and preferences were added to allow label color and size modification. [Pull request #10552](https://github.com/FreeCAD/FreeCAD/pull/10552) |
+++

+++
| <img alt="" src=images/FEM_stress_component_linearization_relnotes_0.22.png  style="width:384px;"> | The [FEM PostFilterLinearizedStresses](FEM_PostFilterLinearizedStresses.md) command can now use the stress tensor components for linearized stress computations. Previously, only Von Mises, Tresca and principal (major/intermediate/minor) stresses could be used for this. [Pull request #11724](https://github.com/FreeCAD/FreeCAD/pull/11724) |
+++

### Further FEM improvements 

-   The **Model → Constraints without solver** menu was removed from the GUI. The listed constraints could not be used. [Pull request #10457](https://github.com/FreeCAD/FreeCAD/pull/10457) and [Pull request #10459](https://github.com/FreeCAD/FreeCAD/pull/10459)
-   The word \"constraint\" was removed from the names and descriptions of most features in the FEM workbench to ensure the correct nomenclature. The names were changed in such a way to fit the standards in the FEA industry and to make them intuitive for new users. [Pull request #10519](https://github.com/FreeCAD/FreeCAD/pull/10519) and [Pull request #10799](https://github.com/FreeCAD/FreeCAD/pull/10799)
-   New icons were added for [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md), [Solver job control](FEM_SolverControl.md) and [Run solver calculations](FEM_SolverRun.md) for greater intuitiveness.
-   Solver CalculiX (new framework) was removed from the GUI since it\'s unfinished and unnecessary at the moment. [Pull request #10823](https://github.com/FreeCAD/FreeCAD/pull/10823)
-   The layout of some postprocessing tool task panels was improved to reduce the size of the horizontal space occupied by them. [Pull request #11066](https://github.com/FreeCAD/FreeCAD/pull/11066)
-   The [FEM ConstraintTemperature](FEM_ConstraintTemperature.md) task panel was reworked to fix issues when editing this feature. [Pull request #11126](https://github.com/FreeCAD/FreeCAD/pull/11126)
-   An old issue with the [FEM PostFilterDataAlongLine](FEM_PostFilterDataAlongLine.md) being able to plot only magnitude, not vector components of a selected output variable was finally fixed. [Pull request #10992](https://github.com/FreeCAD/FreeCAD/pull/10992)
-   The [FEM ConstraintForce](FEM_ConstraintForce.md) and [FEM ConstraintPressure](FEM_ConstraintPressure.md) were overhauled to make them work better on the source code side. [Pull request #10935](https://github.com/FreeCAD/FreeCAD/pull/10935) and [Pull request #10923](https://github.com/FreeCAD/FreeCAD/pull/10923)
-   The [FEM PostFilterDataAtPoint](FEM_PostFilterDataAtPoint.md) now has a PointSize property to set the size of the point symbol for more visibility. [Pull request #11054](https://github.com/FreeCAD/FreeCAD/pull/11054)
-   For clarity, the [FEM mesh region](FEM_MeshRegion.md) command was relabeled to *FEM mesh refinement* in the GUI (the command name remains unchanged). [Pull request #11489](https://github.com/FreeCAD/FreeCAD/pull/11489)

## Export

## Material

+++
| <img alt="" src=images/Materials_relnotes_0.22.PNG  style="width:384px;"> | The material handling system, including the editor, has been completely reworked. Further improvements in this regard will follow. [Pull request #10690](https://github.com/FreeCAD/FreeCAD/pull/10690) |
+++

+++
| <img alt="" src=images/Appearance_preview_relnotes_0.22.png  style="width:384px;"> | Appearance preview was added to show the materials in the same way they will be shown in documents. [Pull request #11628](https://github.com/FreeCAD/FreeCAD/pull/11628) |
+++

## Mesh

### Further Mesh improvements 

## OpenSCAD Workbench 

### Further OpenSCAD improvements 

## Part Workbench 

+++
| <img alt="" src=images/Part_scale_relnotes_0.22.PNG  style="width:384px;"> | [Part Scale](Part_Scale.md) tool was added to allow for easy scaling of shapes without having to use tools from the Draft Workbench. [Pull request #10583](https://github.com/FreeCAD/FreeCAD/pull/10583) |
+++

+++
| <img alt="" src=images/Part_Mirror_relnotes_0.22.png  style="width:384px;"> | [Part Mirror](Part_Mirror.md) Now supports reference objects, such as a [Part Plane](Part_Plane.md) to define an arbitrary mirror plane in addition to the standard XY, XZ, and YZ planes. [Pull request #11535](https://github.com/FreeCAD/FreeCAD/pull/11535) |
+++

### Further Part improvements 

-   The *Frenet* property is now enabled by default for the [Part Sweep](Part_Sweep.md) tool to avoid a common rendering issue. [Pull request #11590](https://github.com/FreeCAD/FreeCAD/pull/11590)

## PartDesign Workbench 

+++
| <img alt="" src=images/Pad_task_dialog_relnotes_0.22.png  style="width:384px;"> | [Pad](PartDesign_Pad.md) and [pocket](PartDesign_Pocket.md) task panels were improved (reordered UI elements, **Select face** option hidden when unnecessary and so on). [Pull request #10392](https://github.com/FreeCAD/FreeCAD/pull/10392) |
+++

+++
| <img alt="" src=images/Pattern_offset_mode_relnotes_0.22.png  style="width:384px;"> | Offset mode was added for [linear](PartDesign_LinearPattern.md) and [polar pattern](PartDesign_PolarPattern.md). The previous mode was renamed **Overall Length**. [Pull request #10377](https://github.com/FreeCAD/FreeCAD/pull/10377) |
+++

### Further PartDesign improvements 

-   The *Make thickness inwards* option is now enabled by default for the [Thickness](PartDesign_Thickness.md) tool. [Pull request #7488](https://github.com/FreeCAD/FreeCAD/pull/7488)

## Path Workbench 

### Further Path improvements 

## Plot module 

## Points Workbench 

### Further Points improvements 

## Sketcher Workbench 

+++
| <img alt="" src=images/Arc_helper_relnotes_0.22.png  style="width:384px;"> | Implementation of a circle overlay for arcs (to solve the issue of constraints appearing away from them) was completed with a command to switch them. [Pull request #9703](https://github.com/FreeCAD/FreeCAD/pull/9703) |
+++

   
  <img alt="" src=images/Contextual_dimension_relnotes_0.22.gif  style="width:320px;">Click on the image if the animation does not start.   Contextual dimension constraint was added to enable quick and intuitive dimensioning with a single versatile tool. [Pull request #9810](https://github.com/FreeCAD/FreeCAD/pull/9810)
   

   
  <img alt="" src=images/Tool_parameters_relnotes_0.22.gif  style="width:320px;">Click on the image if the animation does not start.   Tool parameters were added to allow dimensioning on the go (when drawing shapes). Depending on the preference setting On-View-Parameters, they can be disabled, reduced to dimensions only (no initial coordinates) or fully enabled. Moreover, modes were added for the shape tools. They can be selected using the M key or a drop-down list in the task panel. Some tools have additional settings in the form of checkboxes in the task panel and additional keyboard shortcuts. Currently, the new features are available for points, lines, arcs, ellipses, rectangles, polygons and slots. This is a work in progress. [Pull request #11048](https://github.com/FreeCAD/FreeCAD/pull/11048), [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) and following
   

+++
| <img alt="" src=images/Offset_relnotes_0.22.png  style="width:384px;"> | An [Offset](Sketcher_Offset.md) tool was added to allow offsetting curves. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Three_point_rectangle_relnotes_0.22.png  style="width:384px;"> | Three-point [rectangle](Sketcher_CompCreateRectangles.md) mode was added in two versions - 3 corners or center and 2 corners. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

+++
| <img alt="" src=images/Arc_slot_relnotes_0.22.png  style="width:384px;"> | An Arc slot tool was added with two modes (arc ends and flat ends) to allow for the creation of curved slots [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174) |
+++

   
  <img alt="" src=images/Auto_horizontal-vertical_relnotes_0.22.gif  style="width:320px;">Click on the image if the animation does not start.   A Horizontal/Vertical constraint was added. It automatically applies horizontal constraint if a line is closer to horizontal orientation or vertical constraint if it\'s closer to vertical orientation. [Pull request #11538](https://github.com/FreeCAD/FreeCAD/pull/11538)
   

+++
| <img alt="" src=images/Angle_radius_rendering_relnotes_0.22.png  style="width:384px;"> | Rendering of angle and radius constraints was improved. Angle constraints have full extension lines now. [Pull request #11507](https://github.com/FreeCAD/FreeCAD/pull/11507) |
+++

+++
| <img alt="" src=images/Polar_transform_relnotes_0.22.png  style="width:384px;"> | A polar transform tool was added to allow rotation and circular patterns of sketcher geometries. [Pull request #11264](https://github.com/FreeCAD/FreeCAD/pull/11264) |
+++

### Further Sketcher improvements 

-   Frame mode was added for the Rectangle tool. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   Two new modes were added for the Line tool: *Point, length, angle* and *Point, width, height*. [Pull request #11174](https://github.com/FreeCAD/FreeCAD/pull/11174)
-   [ToggleConstruction](Sketcher_ToggleConstruction.md) and [ToggleDrivingConstraint](Sketcher_ToggleDrivingConstraint.md) icons were changed. Now the former is not so similar to [CarbonCopy](Sketcher_CarbonCopy.md) and both toggle icons change when clicked. [Pull request #11500](https://github.com/FreeCAD/FreeCAD/pull/11500)
-   Sketcher icons were overhauled to unify their appearance (stroke widths, colors and point sizes). [Pull request #11785](https://github.com/FreeCAD/FreeCAD/pull/11785)
-   An optional (deactivated by default) unification of [Coincident](Sketcher_ConstrainCoincident.md) and [PointOnObject](Sketcher_ConstrainPointOnObject.md) was introduced. [Pull request #11494](https://github.com/FreeCAD/FreeCAD/pull/11494)

## Spreadsheet Workbench 

### Further Spreadsheet improvements 

## Start Workbench 

+++
| <img alt="" src=images/Start_page_template_buttons_new_relnotes_0.22.PNG  style="width:384px;"> | A **New file** section that includes a number of quick-start buttons has been added to the Start Page. [Pull request #10171](https://github.com/FreeCAD/FreeCAD/pull/10171) |
+++

+++
| <img alt="" src=images/Start_page_layout_relnotes_0.22.png  style="width:384px;"> | The visual design of the Start Page has been overhauled. It now looks more modern and consistent. [Pull request #10391](https://github.com/FreeCAD/FreeCAD/pull/10391) |
+++

### Further Start improvements 

-   The preferences page of the Start Workbench has been re-organized. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   There now is a **Custom CSS** option for the Start Page which allows you to customize the Start Page CSS style from the Start Workbench preferences. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   The **Hide scrollbars** preference has been removed. The scrollbars on the Start Page are now styled according to the theme and are much thinner. [Pull request #10520](https://github.com/FreeCAD/FreeCAD/pull/10520)
-   There are now preferences for hiding and changing the size of the file thumbnail icons on the Start Page. [Pull request #10410](https://github.com/FreeCAD/FreeCAD/pull/10410)

## Surface Workbench 

### Further Surface improvements 

## TechDraw Workbench 

+++
| <img alt="" src=images/TechDraw_cosmetic_circle_relnotes_0.22.png  style="width:250px;"> | The [CosmeticCircle](TechDraw_CosmeticCircle.md) tool was added to allow for the creation of cosmetic circles by selecting the center and inputting the radius. [Pull request #10763](https://github.com/FreeCAD/FreeCAD/pull/10763) |
+++

+++
| <img alt="" src=images/Arc_length_relnotes_0.22.PNG  style="width:250px;"> | The [ArcLengthAnnotation](TechDraw_ExtensionArcLengthAnnotation.md) tool was added to create dimension-like annotations of arc length of selected edges. [Pull request #11532](https://github.com/FreeCAD/FreeCAD/pull/11532) |
+++

+++
| <img alt="" src=images/Offset_vertex_relnotes_0.22.png  style="width:250px;"> | The [AddOffsetVertex](TechDraw_CommandAddOffsetVertex.md) tool was added to create cosmetic vertices as offsets from selected vertices. [Pull request #11655](https://github.com/FreeCAD/FreeCAD/pull/11655) |
+++

### Further TechDraw improvements 

-   Sections based on other sections now use the original (uncut) shape by default. This can be changed in section settings to use the previous section instead. [Pull request #10281](https://github.com/FreeCAD/FreeCAD/pull/10281)
-   Cosmetic objects and centerlines can now be deleted by selecting them and pressing the Delete key. Previously, this resulted in the whole view being deleted. [Pull request #10695](https://github.com/FreeCAD/FreeCAD/pull/10695) and [Pull request #10813](https://github.com/FreeCAD/FreeCAD/pull/10813)
-   A new, more intuitive icon was added for the [WeldSymbol](TechDraw_WeldSymbol.md) tool. [Pull request #10936](https://github.com/FreeCAD/FreeCAD/pull/10936)
-   The behavior of the point + edge mode of the [LengthDimension](TechDraw_LengthDimension.md) was corrected. [Pull request #10860](https://github.com/FreeCAD/FreeCAD/pull/10860)
-   A checked state was added for the [ToggleFrame](TechDraw_ToggleFrame.md) button so that a user can see whether the button is activated or not. [Pull request #11240](https://github.com/FreeCAD/FreeCAD/pull/11240)
-   The behavior of the [DecorateLine](TechDraw_DecorateLine.md) tool was improved. Now double-clicking a line invokes this tool. And line styles are correctly restored if the user presses *Cancel*. Previously, there was no difference between pressing *OK* and *Cancel*. [Pull request #11188](https://github.com/FreeCAD/FreeCAD/pull/11188)
-   Color and transparency of faces can now be set per view. [Pull request #11315](https://github.com/FreeCAD/FreeCAD/pull/11315)
-   Multiselection mode was added and can be enabled in Preferences. In this mode, multiple vertices, edges and faces can be selected by left-clicking on them, without having to keep the Ctrl key pressed. [Pull request #11417](https://github.com/FreeCAD/FreeCAD/pull/11417)
-   [ExtensionAreaAnnotation](TechDraw_ExtensionAreaAnnotation.md) can now calculate areas of arbitrary faces. [Pull request #11473](https://github.com/FreeCAD/FreeCAD/pull/11473)
-   Non-continuous lines will now follow the ISO/ANSI standards instead of a Qt line style. A new preference was added to select the standard. [Pull request #11594](https://github.com/FreeCAD/FreeCAD/pull/11594)
-   The behavior of the [AxoLengthDimension](TechDraw_AxoLengthDimension.md) tool was improved. Now, when dimensioning edges parallel to the global coordinate system axes, the actual (3D) value is calculated automatically and inserted into the Format Spec property (as text). [Pull request #11678](https://github.com/FreeCAD/FreeCAD/pull/11678)
-   The [ExtensionPositionSectionView](TechDraw_ExtensionPositionSectionView.md) tool can now be used by selecting an edge in a section view and a vertex in the source view. [Pull request #11797](https://github.com/FreeCAD/FreeCAD/pull/11797)

## Web Workbench 

### Further Web improvements 

## Compilation

## Known Limitations



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.22
