# Release notes 0.18/es
FreeCAD 0.18 was released on 12 March, 2019, get it from the [Download](Download.md) page. This is a summary of the most interesting changes. The complete list of changes can be found in the [MantisBT bugtracker FC 0.18 changelog](https://www.freecadweb.org/tracker/changelog_page.php?version_id=78).

Older FreeCAD release notes can be found in [Feature list](Feature_list#Release_notes.md).

## Destacados

Herramientas [TechDraw](#TechDraw_Workbench/es.md) extendidas

<img alt="Model by Laurent14" src=images/TechDraw_sheet_screenshot.png  style="width:700px;">




New [sketcher](#Sketcher_Workbench.md) tools, more stable and robust [PartDesign](#PartDesign_Workbench.md)

<img alt="Model by un1corn" src=images/Part_engine_screenshot.jpg  style="width:700px;">




Enhanced and extended [Arch and BIM](#Arch_Workbench.md) tools

<img alt="Model by regis" src=images/Arch_work_screenshot.png  style="width:700px;">




## General

-   Redesigned Start center
-   The Document tree (Model tab) now offers 3 options for how all documents are displayed, with the option set from the menu **View → Document Tree** :
    -   Single Document (Only display the currently active document)
    -   Multi Document (Display all documents as it used to be up to FreeCAD 0.17)
    -   Collapse/Expand (Expand the active document and collapse all others)
-   When a task is active and requires user input, an icon showing a pencil now appears on the Tasks tab and disappears when the task is completed.
-   The 3D view now benefits from a new **[Navigation Cube](Navigation_Cube.md)** to quickly orientate the view. It also has a small menu to set the projection to orthographic or perspective, as well as to fit the content to the view. The placement of the navigation cube can be set in **Preferences → Display → 3D View** and it can also be hidden.
-   Generic support for US Civil / Transportation Engineering units has been added. These units include ft, ft\^2, ft\^3, mph, and angles as degrees/minutes/seconds. These units allow for expression of feet in decimal form, as opposed to US Building, which forces fractions of inches.
-   It is now possible to specify a custom background image for FreeCAD\'s main window using the option [**Preferences → General → Enable tiled background**](Preferences_Editor#General.md).

<File:Start> center 0.18 screenshot.jpg\|thumb\|left\|The redesigned Start center <File:FC018> Navigation Cube.png\|thumb\|left\|The navigation cube <File:FreeCAD> with background image.jpg\|thumb\|left\|FreeCAD with a custom background image




## Ambiente de Trabajo Arch 

<img alt="The Arch workbench at work" src=images/Arch_release018_example.jpg  style="width:700px;">

-   [Walls](Arch_Wall.md) can now be displayed as a stack of blocks. There are many options to configure their size and how blocks must be stacked.
-   [Building Parts](Arch_BuildingPart.md) are the new use-for-all Arch container. They can group any number of objects, they can be used to make floors (storeys), buildings (the [Arch Floor](Arch_Floor.md) and [Arch Building](Arch_Building.md) tools now produce Building Parts), or any other group of Arch objects. They can be moved like [Parts](Std_Part.md), and they are [clonable](Draft_Clone.md) and [referencable](Arch_Reference.md)!
-   The [BIM Workbench](BIM_Workbench.md) (added via the [Addon Manager](Std_AddonMgr.md)), is a new external, experimental counterpart of [Arch](Arch_Workbench.md). In it, we test new features and workflows in a more free environment. Be sure to give it a test ride!
-   [Windows](Arch_Window.md) have new presets such as a 4-pane sliding window, plus, if the [Parts Library](https://github.com/FreeCAD/FreeCAD-library/tree/c5eea12cdda7a3e6349323808815f63b0f97ef2e) is installed, all the doors and windows from the library.
-   [Panels](Arch_Panel.md) can now do different kinds of corrugated panels, such as undulated sheets, or even sandwich panels.
-   [Structure](Arch_Structure.md) objects have a new beam drawing mode, which allow you to click two points to place a structural element between them.
-   All IFC types are now available for all Arch objects. Any object can be exported to any other type to IFC.
-   [Window placement](Arch_Window.md) has been fully redesigned. Correctly placing windows in host objects, which was before a real pain to do is now much easier.
-   Dynamic window parameters: The size of the window frames is now a window property, so it is now possible to adjust the thickness of preset windows without the need to edit their components or base sketches.
-   IFC Property Sets are now supported by all Arch objects.
-   The IFC importer and exporter have been greatly enhanced with a wealth of new features: Property sets support, grid support, file compression, shared profiles, groups support, quantity sets, etc\...
-   [Materials](Arch_SetMaterial.md) now support hierarchy, if you give a material another material as father, they appear correctly stacked in the tree.
-   All Arch objects and materials now support classification systems (not yet supported by IFC import/export).
-   [External references](Arch_Reference.md) now allow you to link parts from another FreeCAD file into a FreeCAD file.

-   But there is much more! Check the [Arch/BIM development reports](https://github.com/yorikvanhavre/BIM_Workbench/wiki) to see everything that has been done there this year.

## Ambiente de Trabajo Draft 

<img alt="More precise Draft annotation tools" src=images/Draft_release018_example.jpg  style="width:700px;">

-   The [Draft Scale](Draft_Scale.md) tool has been fully redesigned, and has now more options and is much more comfortable to use
-   The [Draft Text](Draft_Text.md) tool has also been fully redesigned, it now has its own parametric object with many more options. Warning, these new texts are not supported by 0.17
-   [Draft Wires](Draft_Wire.md) now have a right-click option that allows to force-flatten them on their median plane
-   New [Draft Join](Draft_Join.md) tool, which allows you to join individual wires and lines into a single wire
-   New [Draft Split](Draft_Split.md) tool, which splits a line or a wire at a point to create another wire or line
-   Pressing the **** key while drawing in draft mode cycles the snapping object target, allowing you to snap on objects that are obscured by others
-   The Draft AddPoint tool has been improved to more reliably add nodes on lines and wires exactly where you click




## FEM Workbench 

<img alt="The polished FEM material dialog" src=images/FEM-Material-dialog-018.png  style="width:300px;"> In 0.17 there where added tons of new features in FEM. Thus the main focus for FEM in 0.18 release of FreeCAD was not adding even more new features and tools, but make the existing ones more stable and fix as much as possible bugs. FEM got 470 commits during FreeCAD 0.18 development cycle [1](https://forum.freecadweb.org/viewtopic.php?f=10&t=13154&p=297292#p297110).

### General Improvements on the code base 

-   Tons of bug fixes.
-   Code refactor and cleaning. Get rid of duplicate code.
-   Fix a lot of typos in code and visible messages.
-   Python 3 compatibility fixes.
-   More unit tests where added.
-   Possibility to compile FreeCAD with external uptodate SMESH.

### Tools

-   A clipping plane tool was added to be able to select solids which are inside other solids.
-   The VTK warp filter got some love.
-   An analysis type for CalculiX model checking was added.

### Material

The material handling was improved. It is now possible to use the global FreeCAD material editor. See also [material cards](Release_notes_0.18#Material_Handling.md). For this the the FEM material task panel was polished.

## Ambiente de Trabajo Part 

-   The [Check Geometry](Part_CheckGeometry.md) tool now opens a small window with a progress bar and a **Cancel** button to end the task if it takes too long.
-   The new [Defeaturing](Defeaturing_Workbench.md) tool is based on the tool of the same name included in OCCT 7.3.0. It can remove selected attributes on a solid such as holes, protrusions, gaps, chamfers, fillets, etc. For more info, see [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211) article on the OCCT website. Please note that if FreeCAD is built on an older version that OCCT 7.3.0, this tool won\'t be available and will be greyed out.

-   The new [SliceApart](Part_SliceApart.md) tool is based on the [Slice to Compound](Part_Slice.md) and includes an automatic compound explode for easily splitting objects.

## Ambiente de Trabajo PartDesign 

-   The new [Local Coordinate System](PartDesign_CoordinateSystem.md) tool now allows the addition of a local coordinate system visualization to several datum objects.

## Ambiente de Trabajo Path 

### General Improvements 

-   Path can now correctly display gcode with ABC axis words
-   Improvements to Tool editor -- Simplified edit for selective tool types

### Job Improvements 

-   Jobs can now have multiple base objects
-   Job container organisation has been improved
-   Default Values for Operation Settings can be controlled through SetupSheets

### Operaciones

-   New Adaptive Clearing Operation
-   New Deburr Operaton
-   new AxisMap dressup does limited 4th axis by mapping a linear direction to a rotary axis
-   Support for 2D objects and individual edge milling through Engrave and Deburr
-   RampEntry dressup now has a configurable start point
-   PocketShape Operation can now \'use outline\'

### Post Processors 

-   grbl\_post -- argument to suppress tool change commands
-   grbl\_g81 post processor

## Ambiente de Trabajo Sketcher 

<img alt="Sketcher View Section demo" src=images/Sketch-clip-plane-demo.png  style="width:700px;">

-   The new **[View section](Sketcher_ViewSection.md)** tool creates a section plane that removes matter on the model that is in front of the sketch plane. This can be useful when the sketch plane is located inside a solid model. Pressing the View section tool again toggles the view back to a full view.
-   The **Sketcher solver** benefited from improvements and is now better at detecting redundant and conflicting constraints, especially those induced by symmetric constraints.
-   New **[Constrain Diameter](Sketcher_ConstrainDiameter.md)** tool added
-   **DoF Finder** is a new utility to help find degrees of freedom. In the Solver messages widget in the Tasks panel, the traditional message *Under-constrained sketch with x degrees of freedom* now underlines the *x degrees* text in blue. Clicking on it will highlight in green, in the 3D view, the elements that are not fully constrained.
-   **Sketcher Auto Remove Redundants** is a new checkbox in the Solver messages box. When enabled, it will prevent creation of redundant constraint when the user is sketching and applying constraints, and it will automatically delete the redundant constraints.
-   There is a new command to delete all constraints at once. It can be found in the menu **Sketch → Sketcher tools → Delete All Constraints**.
-   New option in **Preferences → Sketcher → General → Hide base length units for supported unit systems**. This hides the unit for dimensional constraints while in sketch editing mode.
-   Size of vertices (points) can now be set in **Preferences → Display → 3D View → Marker size**.
-   New **[Move](Sketcher_Move.md)** command to move all selected geometry from the last selected point. It can be access under the Clone tool drop down.
-   Added *Extended Information* checkbox to the Constraints list widget.

Relevant forum links:

-   [Recent Several Sketcher improvements](https://forum.freecadweb.org/viewtopic.php?f=9&t=29192)
-   [Feature \#1632: Allow entering of diameter instead of radius for circle radius constraint](https://forum.freecadweb.org/viewtopic.php?f=8&t=29152)
-   [Sketcher Auto Remove Redundants mode](https://forum.freecadweb.org/viewtopic.php?f=9&t=30594)
-   [Constraints extended naming](https://forum.freecadweb.org/viewtopic.php?f=10&t=28890)

## Ambiente de Trabajo Spreadsheet 

## Ambiente de Trabajo Surface 

## TechDraw Workbench 

The TechDraw Workbench received a number of additions and improvements for v0.18.

-   New export Page to Dxf
-   new tutorial for TechDraw
-   improved dimension formatting for isometric views, angles, text location
-   improved error messages
-   improved section view formatting
-   allow custom line groups
-   additional preferences
-   easier edge & center mark selection
-   view direction based on current 3d view or selected face
-   added +/\* tolerances to dimensions
-   new 3 point angle dimension
-   RMB context menu
-   keyboard zooming (Ctl+/-)
-   support for DMS dimensions

## Material Handling 

<img alt="A material card" src=images/Material-Card-018.png  style="width:300px;"> The material handling has been improved. It is now possible to create **material cards** for every material. The cards can contain all information, physical properties, architectural specification, web links, comments. etc. The cards are text files with the file suffix {{FileName|.FCMat}} and can be used for all workbenches of FreeCAD.

FreeCAD provides material cards for standard metals, plastics and different types of steel.

## Módulos Adicionales 

Some of the new community modules that were actively developed during the 0.18 development cycle.

-   [A2plus](A2plus_Workbench.md) is a new workbench to assemble different parts in FreeCAD. It is an extension of the Assembly2 workbench providing an extended color and transparency handling for parts and a new constraint using the center of mass of parts.

-   [Curves](https://github.com/tomate44/CurvesWB), a collection of tools to create and edit NURBS curves and surfaces.

-   [Nurbs](https://github.com/microelly2/freecad-nurbs), a collection of scripts for managing freeform surfaces and curves.

-   [Silk](https://github.com/edwardvmills/Silk), a collection of NURBS surface modeling tools focused on low degree and seam continuity.

-   [Flamingo Workbench](Flamingo_Workbench.md), a set of customized FreeCAD commands and objects that help to speed-up the drawing of frames and pipelines.

-   [Civil Engineering/Transportation Workbench](Civil_Engineering_Workbench.md)

-   [GDT](https://github.com/juanvanyo/FreeCAD-GDT), geometric dimensioning and tolerancing (GD&T).

-   [InventorLoader](https://github.com/jmplonka/InventorLoader) to import Autodesk Inventor files (in progress).

-   [Kicad StepUp Workbench](https://www.freecadweb.org/wiki/KicadStepUp_Workbench) is aimed to help KiCad and FreeCAD users in ECAD and MCAD collaboration.

-   [CadQuery FreeCAD Module](https://github.com/jmwright/cadquery-freecad-module/wiki) is a workbench that allows users to write Python scripts, and is tailored to those based on the CadQuery CAD scripting API. A new code editor is made available, and script variables can be edited dynamically through the use of a parameter dialog. The workbench also adds a menu that includes normal file operations for CadQuery scripts (open, new, close, etc), and example scripts to help users learn new concepts.

-   [Defeaturing Workbench](Defeaturing_Workbench.md) is intended for editing imported STEP models, removal of the selected features from the model.

[<img src="images/Property.png" style="width:16px"> News](Category_News.md) [<img src="images/Property.png" style="width:16px"> Documentation](Category_Documentation.md) [<img src="images/Property.png" style="width:16px"> Releases](Category_Releases.md)

---
[documentation index](../README.md) > [News](Category_News.md) > Release notes 0.18/es
