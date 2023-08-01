# BIM Workbench/hr
}

<img alt="BIM External Workbench icon" src=images/IFC.svg  style="width:128px;">


{{TOCright}}



## Predstavljanje

The <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Workbench](BIM_Workbench.md) is an [external workbench](External_workbenches.md) aimed at implementing complete [Building Information Modeling](https://en.wikipedia.org/wiki/Building_information_modeling) (BIM) tools and workflow in FreeCAD. It can be installed from the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

The BIM Workbench is based on the built-in <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md), and both will probably be merged in the future. The BIM Workbench is a \"meta workbench\", intended to gather many useful tools from other workbenches in a single place, and create a workflow that is more convenient and user-friendly to both experienced BIM users and beginners. The BIM workbench also features some specific tools of its own, mostly wizards and management tools, located under the **Management** menu.

See [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) for a quick overview if you are already a user of another BIM application.

The developers of Draft, Arch and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">



## Instalacija

The BIM workbench is not bundled with the default FreeCAD package, but can easily be installed via the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). Invoke it from **Tools → Addon Manager**. The BIM workbench code is [hosted and developed on github](https://github.com/yorikvanhavre/BIM_Workbench) and can also be installed manually by copying it into FreeCAD\'s **MOD** directory.

**Note**

The BIM workbench is a work in progress, and will change often. Be sure to update it regularly! If you have the [Python-Git](https://github.com/chidimo/python-git) module installed, the BIM workbench will automatically look for available updates at start, and display an icon in the status bar if an update is available.

The tools listed below might also not all be present if your FreeCAD version is not fully up-to-date. The BIM workbench should however work seamlessly on all FreeCAD versions, it will only drop the tools not available.

## Getting started 

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">

Upon starting the BIM workbench for the first time, a welcome dialog is shown, giving a quick overview of how the workbench works, and allowing the user to start an [in-game tutorial](BIM_ingame_tutorial.md). The welcome dialog is also available from the **help** menu. When the welcome screen is closed by clicking OK, the [BIM setup dialog](BIM_Setup.md) will be shown, that allows the user to quickly set some of the most common BIM-related preferences of FreeCAD without the need to browse through the full FreeCAD preferences pages.

The [BIM project setup](BIM_Project.md) tool allows you to quickly setup a BIM project by filling some basic information about your project. You can then, for example, use the different 2D drafting tools to sketch guidelines and baselines, then use the different 3D modeling tools to automatically build 3D BIM objects from them. A line, for example, can become a wall simply by selecting it and pressing the [Wall](Arch_Wall.md) button.

If you are used to another BIM application, check our [BIM application compatibility table](BIM_application_compatibility_table.md) to get your marks when starting with FreeCAD.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

The [in-game tutorial](BIM_ingame_tutorial.md) is an easy way to quickly get on track with the BIM workbench.

## Tools

The BIM workbench gather tools from several other FreeCAD workbenches, mainly [Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md) and [Part](Part_Workbench.md), roughly reorganized in logical categories: **2D drafting**, **3D modeling**, **annotation** and **modification** tools. The **manage** category contains tools that are specific to the BIM workbench.

Additionally, if such [addons](External_workbenches.md) are installed, tools from [Reinforcement](Arch_Rebar.md) (extra reinforcing bar tools), [Fasteners](Fasteners_Workbench.md) (bolts and screws), [Flamingo/Dodo](Flamingo_Workbench.md) (metal structure and piping tools) and [Parts Library](Parts_Library_Workbench.md) are automatically included in the BIM workbench.

The BIM workbench also adds a series of items in the **status bar** of FreeCAD, and a couple of **context menu items**, accessible by right-clicking in the 3D view or in the tree view.

### 2D drafting 

2D objects are commonly used as drafting aids, or to draw base lines and profiles to build BIM objects on. They can also be used to draw symbols and annotations in your model. Apart from sketches, that use their own coordinate system, 2D objects will be drawn on the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Sketch](Sketcher_NewSketch.md): Creates‎ a new sketch and enters sketch drawing mode. Sketches are advanced 2D objects with constraints support
-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Line](Draft_Line.md): Draws a line segment between 2 points
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Wire](Draft_Wire.md): Draws a line made of multiple line segments (polyline)
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Circle](Draft_Circle.md): Draws a circle from center and radius
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc.md): Draws an arc segment from center, radius, start angle and end angle
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc 3Points](Draft_Arc_3Points.md): draws a circular arc segment from three points that are located in the circumference
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse.md): Draws an ellipse from two corner points
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon.md): Draws a regular polygon from a center and a radius
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle.md): Draws a rectangle from 2 opposite points
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [BSpline](Draft_BSpline.md): Draws a B-Spline from a series of points
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Cubic Bezier Curve](Draft_CubicBezCurve.md): draws a Bezier curve of third degree by dragging two points.
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bezier Curve](Draft_BezCurve.md): Draws a Bezier curve from a series of points
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point.md): Inserts a point object

### Annotation

Annotations are visual help objects that can be placed inside your model. They can be used to export your model directly to a 2D format like [DXF](Draft_DXF.md), or reused when creating 2D views of your model with the [TechDraw Workbench](TechDraw_Workbench.md).

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): Draws a multi-line text annotation
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [ShapeString](Draft_ShapeString.md): Draws a text line as geometry
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): Draws a linear, angular, radial or diameter dimension
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): Places a label with an arrow pointing to a selected element
-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axis](Arch_Axis.md): Creates a single axis or a 1-direction array of axes to the document
-   <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Axis System](Arch_AxisSystem.md): Creates an axes system composed of up to 3 series of axes
-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grid](Arch_Grid.md): Creates a grid-like object to the document
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Section Plane](Arch_SectionPlane.md): Adds a section plane object to the document. Section planes define 2D views such as plans, sections and elevations
-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Page](TechDraw_PageDefault.md): Creates a new [TechDraw](TechDraw_Workbench.md) page from a [SVG template](TechDraw_Templates.md)
-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [View](TechDraw_ArchView.md): Inserts a view of a section plane on a page

### 3D / BIM modeling 

3D and BIM objects are the real-world elements that will compose your BIM project.

**Building structure**: These tools help you to organize your model

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Project](Arch_Project.md): Creates a project including selected objects
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site.md): Creates a site including selected objects
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Building](Arch_Building.md): Creates a building including selected objects
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Level](Arch_BuildingPart.md) (Building Part): Creates a building part including selected objects. Building parts are commonly used to represent levels
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Space](Arch_Space.md): Creates a space object in the document
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Reference](Arch_Reference.md): Links objects from another FreeCAD file into this document

**BIM tools**: These tools build BIM components

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Wall](Arch_Wall.md): Creates a wall from scratch or using a selected object as a base
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Curtain Wall](Arch_CurtainWall.md): creates a curtain wall from scratch or using a selected object as a base
-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Column](Arch_Structure.md): Creates a vertical [structural](Arch_Structure.md) element at a given point, optionally using a selected object as a profile
-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Beam](Arch_Structure.md): Creates a horizontal [structural](Arch_Structure.md) element between two points, optionally using a selected object as a profile
-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Slab](Arch_Structure.md): Creates a flat [structural](Arch_Structure.md) element by extruding a selected flat object
-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Rebar](Arch_Rebar.md): Creates a reinforcement bar in a selected structural element using a sketch. Requires the [Reinforcement](Reinforcement_Addon.md) addon
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Window](Arch_Window.md): Creates a window using a selected object as a base
-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Door](Arch_Window.md): Creates a [Window](Arch_Window.md) object using door presets
-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Pipe tools](Arch_Pipe.md): Creates pipes and corner or tee connection between 2 or 3 selected pipes
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Stairs](Arch_Stairs.md): Creates a stairs object in the document
-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Roof](Arch_Roof.md): Creates a sloped roof from a selected face
-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Panel tools](Arch_Panel.md): Creates panel objects, and 2D cutouts from these panels
-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Frame](Arch_Frame.md): Creates a frame object from a selected layout
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Fence](Arch_Fence.md): Creates a fence object from a selected post object and path
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Truss](Arch_Truss.md): Creates a truss from a selected line of from scratch
-   <img alt="" src=images/BIM_Library.png  style="width:32px;"> [Library](BIM_Library.md): Inserts an equipment or furniture object. Requires the [Parts Library](Parts_Library.md) addon
-   <img alt="" src=images/Arch_Component.png  style="width:32px;"> [BIM Component](Arch_Component.md): Turns any selected object into a BIM object, with complete IFC support

**Generic 3D tools**: These tools build generic 3D objects that can be turned or used into BIM components

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profile](Arch_Profile.md): Creates a parametric 2D profile to be used for example in extrusions
-   <img alt="" src=images/BIM_Box.png  style="width:32px;"> [Box](BIM_Box.md): Draws a box by specifying its dimensions graphically
-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Shapebuilder](Part_Builder.md): A tool to create more complex shapes from various parametric geometric primitives
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Facebinder](Draft_Facebinder.md): Creates a new object from selected faces on existing objects

### Modification tools 

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Move](Draft_Move.md): Moves object(s) from one location to another
-   <img alt="" src=images/BIM_Copy.png  style="width:32px;"> [Copy](BIM_Copy.md): Copies object(s) from one location to another
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate.md): Rotates object(s) from a start angle to an end angle
-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](BIM_Clone.md): Clones the selected objects
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset.md): Moves segments of an object about a certain distance
-   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Offset](Part_Offset2D.md): Constructs a parallel wire at certain distance from original, or enlarges/shrinks a planar face ((parametric version)
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trim/Extend (Trimex)](Draft_Trimex.md): Trims or extends an object
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale.md): Scales selected object(s) around a base point
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch.md): Stretches the selected objects
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array.md): Creates a polar or rectangular array from selected objects
-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md): Creates an array of objects by placing the copies along a path
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror.md): Mirrors the selected objects
-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrude](Part_Extrude.md): Extrudes planar faces of an object
-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut.md): Cuts (subtracts) one object from another
-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse.md): Fuses (unions) two objects
-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Common](Part_Common.md): Extracts the common (intersection) part of two objects
-   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Compound](Part_Compound.md): Creates a compound from the selected objects
-   <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Simple copy](Part_SimpleCopy.md): Creates a non-parametric copy of a selected object
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): Joins objects into a higher-level object
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): Explodes objects into lower-level objects
-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D View](Draft_Shape2DView.md): Creates a 2D object which is a flattened 2D view of another 3D object
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): Converts a Draft object to Sketch and vice-versa
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Cut with plane](Arch_CutPlane.md): Cut an object according to a plan.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Add component](Arch_Add.md): Adds objects to a component
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remove component](Arch_Remove.md): Subtracts or removes objects from a component

### Management tools 

-   <img alt="" src=images/BIM_Setup.png  style="width:32px;"> [BIM setup](BIM_Setup.md): Configures some of the FreeCAD preferences most commonly used for BIM
-   <img alt="" src=images/BIM_Project.png  style="width:32px;"> [Project setup](BIM_Project.md): Allows to create some basic objects such as a [site](Arch_Site.md), a [building](Arch_Building.md) and [axes](Arch_Axis.md) by filling basic project information.
-   <img alt="" src=images/BIM_Views.png  style="width:32px;"> [Views and levels manager](BIM_Views.md): Manage the different views and levels of your project
-   <img alt="" src=images/BIM_Windows.png  style="width:32px;"> [Windows manager](BIM_Windows.md): Manage the doors and windows of your project
-   <img alt="" src=images/BIM_IfcElements.png  style="width:32px;"> [IFC elements manager](BIM_IfcElements.md): Manage how the different elements of your project will be exported to IFC
-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [IFC properties manager](BIM_IfcProperties.md): Manage the IFC properties attached to each of your objects
-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [IFC quantities manager](BIM_IfcQuantities.md): Manage how the quantities of your objects are explicitely exported to IFC
-   <img alt="" src=images/BIM_Classification.png  style="width:32px;"> [Classification manager](BIM_Classification.md): Manage how objects and materials of your project relate to classifications systems such as [Uniclass](https://en.wikipedia.org/wiki/Uniclass)
-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [Layers manager](BIM_Layers.md): Manage the layers of your document
-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Material](Arch_SetMaterial.md): Manages materials or [multimaterials](Arch_MultiMaterial.md) of selected objects
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Schedule](Arch_Schedule.md): Creates different types of schedules
-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Preflight checks](BIM_Preflight.md): Perform different checks on your model before exporting to IFC
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md): Manages annotation styles used by texts and dimensions

## Tutorials and Learning 

-   [Migrating to FreeCAD from Revit](Migrating_to_FreeCAD_from_Revit.md)
-   [Arch & BIM tutorials on this wiki](Tutorials#Architecture_and_BIM.md)
-   [\"BIM with FreeCAD\" video series by Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutorials\" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)

## External workbenches 

FreeCAD workbenches are easy to program in [Python](Python.md), there are therefore many people developing additional workbenches outside of the FreeCAD main developers.

The [external workbenches](External_workbenches.md) page has some information and tutorials on some of them, and the [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) project aims at gathering them and making them easily installable from within FreeCAD.

New workbenches are in development, stay tuned!



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [BIM](Category_BIM.md) > BIM Workbench/hr
