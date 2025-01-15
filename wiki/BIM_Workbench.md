# BIM Workbench
**In v1.0 the BIM, Native-IFC and [Arch](Arch_Workbench.md) Workbenches have been merged into the integrated BIM Workbench.<br>
This page has been updated for that version.**

<img alt="BIM Workbench icon" src=images/Workbench_BIM.svg  style="width:128px;">

 

## Introduction

The <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Workbench](BIM_Workbench.md) provides a modern [Building Information Modelling](https://en.wikipedia.org/wiki/Building_information_modeling) workflow in FreeCAD, with fully parametric objects such as walls, beams, roofs, windows, stairs, pipes, and furniture. It supports [Industry Foundation Classes](Arch_IFC.md) (IFC) files, and the production of 2D plans in combination with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [TechDraw Workbench](TechDraw_Workbench.md).

The BIM Workbench imports tools from the <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft Workbench](Draft_Workbench.md), as it uses its 2D objects to build 3D parametric objects. But it can also use solid shapes created with other workbenches like <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench.md) and <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench.md).

See [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) for a quick overview if you are already a user of another BIM application.

The developers of Draft and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

 <img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;"> 

## Getting started 

 <img alt="" src=images/BIM_welcome_screen.png  style="width:800px;"> 

When starting the BIM workbench for the first time, a welcome dialog is shown, giving a quick overview of how the workbench works, and allowing the user to start an [in-game tutorial](BIM_ingame_tutorial.md). The welcome dialog is also available from the **help** menu. When the welcome screen is closed by clicking OK, the [BIM setup dialog](BIM_Setup.md) will be shown, that allows the user to quickly set some of the most common BIM-related preferences of FreeCAD without the need to browse through the full [FreeCAD preferences pages](Preferences_Editor.md).

The [BIM project setup](BIM_Setup.md) tool allows you to quickly setup a BIM project by entering some basic information about your project. You can then, for example, use the different 2D drafting tools to sketch guidelines and baselines, then use the different 3D modeling tools to automatically build 3D BIM objects from them. A line, for example, can become a wall simply by selecting it and pressing the [Wall](Arch_Wall.md) button.

Common building elements such as [walls](Arch_Wall.md) or [columns](BIM_Column.md) are easily created by pressing the appropriate toolbar button and clicking points in the 3D view. They can be moved, rotated and edited once created. Most BIM elements are created on the current [working plane](Draft_SelectPlane.md), so a typical workflow involves placing the working plane first, then creating a BIM element. More complex elements can be created by drawing 2D elements first, then using one of the BIM tools to convert them into the desired element.

Elements of building projects can be organized using [sites](Arch_Site.md), [buildings](Arch_Building.md) and [levels](Arch_BuildingPart.md), to reproduce what is commonly done in other BIM applications. In FreeCAD, however, such structures are not mandatory, and you are free to organize your model elements as you see fit, for example using [groups](Std_Group.md).

2D drawings can be generated from a model to represent plan, section or elevation views. To generate such a drawing,[section planes](Arch_SectionPlane.md) are placed in the model, to indicate where it should be cut or viewed from. Once the section planes are in place, two methods are possible:

1.  Create projected views in the document using [shape views](Draft_Shape2DView.md), then add all the necessary annotations such as texts and dimensions, then put all this on a page. This is the recommended way, as it offers more flexibility.
2.  Create a view on a page directly from the section plane. Then all the needed 2D annotations must either be added to the section plane, or done directly on the page. This is less flexible.

Finally, quantities schedules can be created using the [schedule](Arch_Schedule.md) tool.

If you are used to another BIM application, check our [BIM application compatibility table](BIM_application_compatibility_table.md) to get your bearings when starting with FreeCAD.

 <img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;"> 

The [in-game tutorial](BIM_ingame_tutorial.md) is an easy way to quickly get on track with the BIM workbench.

## Tools

The BIM workbench gathers tools from several other FreeCAD workbenches, mainly [Draft](Draft_Workbench.md) and [Part](Part_Workbench.md), roughly reorganized in logical categories.

Additionally, if such [addons](External_workbenches.md) are installed, tools from [Reinforcement](Reinforcement_Workbench.md) (extra reinforcing bar tools), [Fasteners](Fasteners_Workbench.md) (bolts and screws), [Flamingo/Dodo](Flamingo_Workbench.md) (metal structure and piping tools) and [Parts Library](Parts_Library_Workbench.md) are automatically included in the BIM workbench.

The BIM workbench also adds a series of items in the **status bar** of FreeCAD, and a couple of **context menu items**, accessible by right-clicking in the 3D view or in the tree view.

### 2D drafting 

2D objects are commonly used as drafting aids, or to draw base lines and profiles to build BIM objects on. They can also be used to draw symbols and annotations in your model. Apart from sketches, that use their own coordinate system, 2D objects will be drawn on the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/BIM_Sketch.svg  style="width:32px;"> [Sketch](BIM_Sketch.md): Creates‎ a new sketch and enters sketch edit mode. Sketches are advanced 2D objects with constraints support.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Line](Draft_Line.md): Creates a straight line.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polyline](Draft_Wire.md): Creates a polyline (also called wire), a sequence of several connected line segments.

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Circle](Draft_Circle.md): Creates a circle from a center and a radius.

-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc.md): Creates a circular arc from a center, a radius, a start angle and an aperture angle.

-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc by 3 points](Draft_Arc_3Points.md): Creates a circular arc from three points that define its circumference.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Fillet](Draft_Fillet.md): Creates a fillet, a rounded corner, or a chamfer, a straight edge, between two [Draft Lines](Draft_Line.md).

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse.md): Creates an ellipse from two points defining a rectangle in which the ellipse will fit.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon.md): Creates a regular polygon from a center and a radius.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle.md): Creates a rectangle from two points.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline.md): Creates a B-spline curve from several points.

-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bézier curve](Draft_BezCurve.md): Creates a Bézier curve from several points.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Cubic Bézier curve](Draft_CubicBezCurve.md): Creates a Bézier curve of the third degree.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point.md): Creates a simple point.

### 3D/BIM

3D and BIM objects are the real-world elements that will compose your BIM project.

-   <img alt="" src=images/BIM_Project.svg  style="width:32px;"> [Project](BIM_Project.md): Creates an IFC project including selected objects.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site.md): Creates a site including selected objects.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Building](Arch_Building.md): Creates a building including selected objects.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Level](Arch_Floor.md): Creates a floor including selected objects.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Space](Arch_Space.md): Creates a space object.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Wall](Arch_Wall.md): Creates a wall from scratch or using a selected object as a base.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Curtain Wall](Arch_CurtainWall.md): Creates a curtain wall from scratch or using a selected object as a base.

-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Column](BIM_Column.md): Creates a vertical [structural](Arch_Structure.md) element at a given point, optionally using a selected object as a profile.

-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Beam](BIM_Beam.md): Creates a horizontal [structural](Arch_Structure.md) element between two points, optionally using a selected object as a profile.

-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Slab](BIM_Slab.md): Creates a flat [structural](Arch_Structure.md) element by extruding a selected flat object.

-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Door](BIM_Door.md): Creates a [Window](Arch_Window.md) object using door presets.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Window](Arch_Window.md): Creates a window from scratch or using a selected object as a base.

-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Pipe](Arch_Pipe.md): Creates a pipe.

-   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Connector](Arch_PipeConnector.md): Creates a corner or T-connection between 2 or 3 selected pipes.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Stairs](Arch_Stairs.md): Creates a stairs object.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Roof](Arch_Roof.md): Creates a sloped roof from a selected wire.

-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel.md): Creates a panel object from a selected 2D object.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Frame](Arch_Frame.md): Creates a frame object from a selected layout.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Fence](Arch_Fence.md): Creates a fence object from a selected post and path.

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Truss](Arch_Truss.md): Creates a truss from a selected line or from scratch.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Equipment](Arch_Equipment.md): Creates an equipment or furniture object.

-   Reinforcement tools:

:   These tools, except the first, are only available if the [Reinforcement Workbench](Reinforcement_Workbench.md) has been installed.

  - <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Custom Rebar](Arch_Rebar.md): Creates a custom reinforcement bar in a selected structural element using a sketch.

  - <img alt="" src=images/Reinforcement_StraightRebar.svg  style="width:32px;"> [Straight Rebar](Reinforcement_StraightRebar.md): Creates a straight reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_UShapeRebar.svg  style="width:32px;"> [U-Shape Rebar](Reinforcement_UShapeRebar.md): Creates a U-shape reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_LShapeRebar.svg  style="width:32px;"> [L-Shape Rebar](Reinforcement_LShapeRebar.md): Creates an L-shape reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_StirrupRebar.svg  style="width:32px;"> [Stirrup](Reinforcement_StirrupRebar.md): Creates a stirrup reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_BentShapeRebar.svg  style="width:32px;"> [Bent-Shape Rebar](Reinforcement_BentShapeRebar.md): Creates a bent-shape reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_HelicalRebar.svg  style="width:32px;"> [Helical Rebar](Reinforcement_HelicalRebar.md): Creates a helical reinforcement bar in a selected structural element.

  - <img alt="" src=images/Reinforcement_ColumnRebars.svg  style="width:32px;"> [Column Reinforcement](Reinforcement_ColumnRebars.md): Creates reinforcement bars in a selected column.

  - <img alt="" src=images/Reinforcement_BeamRebars.svg  style="width:32px;"> [Beam Reinforcement](Reinforcement_BeamRebars.md): Creates reinforcement bars in a selected beam.

  - <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:32px;"> [Slab Reinforcement](Reinforcement_SlabRebars.md): Creates reinforcement bars in a selected slab.

  - <img alt="" src=images/Reinforcement_FootingRebars.svg  style="width:32px;"> [Footing Reinforcement](Reinforcement_FootingRebars.md): Creates reinforcement bars in a selected footing.

-   Generic 3D tools:

:   These tools build generic 3D objects that can be turned or used into BIM components.

  - <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profile](Arch_Profile.md): Creates a parametric 2D profile.

  - <img alt="" src=images/BIM_Box.svg  style="width:32px;"> [Box](BIM_Box.md): Creates a box by specifying its dimensions graphically.

  - <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Shape builder\...](Part_Builder.md): Creates more complex shapes from various geometric primitives.

  - <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Facebinder](Draft_Facebinder.md): creates a surface object from selected faces.

  - <img alt="" src=images/BIM_Library.svg  style="width:32px;"> [Objects library](BIM_Library.md): Inserts an equipment or furniture object. Requires the [Parts Library](Parts_Library.md) addon.

  - <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Component](Arch_Component.md): Creates a non-parametric Arch component.

  - <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [External reference](Arch_Reference.md): Links objects from another FreeCAD file into the current document.

### Annotation

Annotations are visual help objects that can be placed inside your model. They can be used to export your model directly to a 2D format like [DXF](Draft_DXF.md), or reused when creating 2D views of your model with the [TechDraw Workbench](TechDraw_Workbench.md).

-   <img alt="" src=images/BIM_Text.svg  style="width:32px;"> [Text](BIM_Text.md): Creates a 2D text in a document or on a TechDraw page.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Shape from text](Draft_ShapeString.md): Creates a compound shape that represents a text string.

-   <img alt="" src=images/BIM_DimensionAligned.svg  style="width:32px;"> [Aligned dimension](BIM_DimensionAligned.md): Creates a dimension aligned with two points or a selected edge.

-   <img alt="" src=images/BIM_DimensionHorizontal.svg  style="width:32px;"> [Horizontal dimension](BIM_DimensionHorizontal.md): Creates an horizontal dimension between two points or from a selected edge.

-   <img alt="" src=images/BIM_DimensionVertical.svg  style="width:32px;"> [Vertical dimension](BIM_DimensionVertical.md): Creates a vertical dimension between two points or from a selected edge.

-   <img alt="" src=images/BIM_Leader.svg  style="width:32px;"> [Leader](BIM_Leader.md): Creates a 2-segment polyline with an arrow at its end, to be used as a leader line in conjunction with a [Text](BIM_Text.md).

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): Creates a multi-line text with a 2-segment leader line and an arrow.

-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axis](Arch_Axis.md): Adds a 1-direction array of axes.

-   <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Axis System](Arch_AxisSystem.md): Adds an axis system composed of several axes.

-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grid](Arch_Grid.md): Adds a grid-like object.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Section Plane](Arch_SectionPlane.md): Adds a section plane object.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Hatch](Draft_Hatch.md): Creates hatches on the planar faces of a selected object.

-   <img alt="" src=images/BIM_TDPage.svg  style="width:32px;"> [Page](BIM_TDPage.md): Creates a [TechDraw page](TechDraw_PageTemplate.md) from a template SVG file.

-   <img alt="" src=images/BIM_TDView.svg  style="width:32px;"> [View](BIM_TDView.md): Creates a view of the selected object(s) such as a [Section plane](Arch_SectionPlane.md) or a Group containing the different elements of a 2D view.

-   <img alt="" src=images/BIM_Shape2DView.svg  style="width:32px;"> [Shape-based view](BIM_Shape2DView.md): Creates a 2D projected view from a selected object such as a [Section plane](Arch_SectionPlane.md) or a [Level](Arch_BuildingPart.md).

### Snapping

This menu contains the [Draft Snap](Draft_Snap.md) tools as well as the following tools:

-   <img alt="" src=images/BIM_SetWPTop.svg  style="width:32px;"> [Working Plane Top](BIM_SetWPTop.md): Places the working plane on the global XY plane (ground).

-   <img alt="" src=images/BIM_SetWPFront.svg  style="width:32px;"> [Working Plane Front](BIM_SetWPFront.md): Places the working plane on the global XZ plane (front).

-   <img alt="" src=images/BIM_SetWPSide.svg  style="width:32px;"> [Working Plane Side](BIM_SetWPSide.md): Places the working plane on the global YZ plane (side).

### Modify

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Move](Draft_Move.md): Moves or copies selected objects from one point to another.

-   <img alt="" src=images/BIM_Copy.svg  style="width:32px;"> [Copy](BIM_Copy.md): Copies selected objects from one point to another.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate.md): Rotates or copies selected objects around a center point by a given angle.

-   <img alt="" src=images/BIM_Clone.svg  style="width:32px;"> [Clone](BIM_Clone.md): Clones selected objects.

-   <img alt="" src=images/BIM_SimpleCopy.svg  style="width:32px;"> [Create simple copy](BIM_SimpleCopy.md): Creates a non-parametric copy of a selected object. This is the same tool as [Part SimpleCopy](Part_SimpleCopy.md).

-   <img alt="" src=images/BIM_Compound.svg  style="width:32px;"> [Make compound](BIM_Compound.md): Creates a compound from selected objects. This is the same tool as [Part Compound](Part_Compound.md).

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset.md): Offsets each segment of a selected object over a given distance, or creates an offset copy of the selected object.

-   <img alt="" src=images/BIM_Offset2D.svg  style="width:32px;"> [2D Offset\...](BIM_Offset2D.md): Constructs a parallel wire at a given distance from the original, or enlarges/shrinks a planar face (parametric version). This is the same tool as [Part Offset2D](Part_Offset2D.md).

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trimex](Draft_Trimex.md): Trims or extends a selected object.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join.md): Joins [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md) into a single wire.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split.md): Splits a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md) at a specified point or edge.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale.md): Scales or copies selected objects around a base point.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch.md): Stretches objects by moving selected points.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to sketch](Draft_Draft2Sketch.md): Converts Draft objects to [Sketcher Sketches](Sketcher_NewSketch.md) and vice versa.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): Upgrades selected objects.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): Downgrades selected objects.

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Add component](Arch_Add.md): Adds objects to a component.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remove component](Arch_Remove.md): Subtracts or removes objects from a component.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Array](Draft_OrthoArray.md): Creates an orthogonal array from a selected object. It can optionally create a [Link](App_Link.md) array.

-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path array](Draft_PathArray.md): Creates an array from a selected object by placing copies along a path.

-   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar array](Draft_PolarArray.md): Creates an array from a selected object by placing copies along a circumference. It can optionally create a [Link](App_Link.md) array.

-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point array](Draft_PointArray.md): Creates an array from a selected object by placing copies at the points from a point compound.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Cut with plane](Arch_CutPlane.md): Cuts an object according to a plane.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror.md): Creates mirrored copies from selected objects.

-   <img alt="" src=images/BIM_Extrude.svg  style="width:32px;"> [Extrude\...](BIM_Extrude.md): Extrudes planar faces of an object. This is the same tool as [Part Extrude](Part_Extrude.md).

-   <img alt="" src=images/BIM_Cut.svg  style="width:32px;"> [Difference](BIM_Cut.md): Subtracts one object from another. This is the same tool as [Part Cut](Part_Cut.md).

-   <img alt="" src=images/BIM_Fuse.svg  style="width:32px;"> [Union](BIM_Fuse.md): Fuses two objects. This is the same tool as [Part Fuse](Part_Fuse.md).

-   <img alt="" src=images/BIM_Common.svg  style="width:32px;"> [Intersection](BIM_Common.md): Extracts the common part of two objects. This is the same tool as [Part Common](Part_Common.md).

### Manage

-   <img alt="" src=images/BIM_Setup.svg  style="width:32px;"> [BIM Setup\...](BIM_Setup.md): Configures some of the FreeCAD preferences most commonly used for BIM.

-   <img alt="" src=images/BIM_Views.svg  style="width:32px;"> [Views manager](BIM_Views.md): Manage the different views and levels of your project.

-   <img alt="" src=images/BIM_ProjectManager.svg  style="width:32px;"> [Manage project\...](BIM_ProjectManager.md): Allows to create some basic objects such as a [site](Arch_Site.md), a [building](Arch_Building.md) and [axes](Arch_Axis.md) by filling basic project information.

-   <img alt="" src=images/BIM_Windows.svg  style="width:32px;"> [Manage doors and windows\...](BIM_Windows.md): Manage the doors and windows of your project.

-   <img alt="" src=images/BIM_IfcElements.svg  style="width:32px;"> [Manage IFC elements\...](BIM_IfcElements.md): Manage how the different elements of your project will be exported to IFC.

-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [Manage IFC quantities\...](BIM_IfcQuantities.md): Manage how the quantities of your objects are explicitely exported to IFC

-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [Manage IFC properties\...](BIM_IfcProperties.md): Manage the IFC properties attached to each of your objects.

-   <img alt="" src=images/BIM_Classification.svg  style="width:32px;"> [Manage classification\...](BIM_Classification.md): Manage how objects and materials of your project relate to classifications systems such as [Uniclass](https://en.wikipedia.org/wiki/Uniclass).

-   <img alt="" src=images/BIM_Layers.svg  style="width:32px;"> [Manage layers\...](BIM_Layers.md): Manage the layers of your document.

-   <img alt="" src=images/BIM_Material.svg  style="width:32px;"> [Material](BIM_Material.md): Manages [materials](Arch_SetMaterial.md) or [multimaterials](Arch_MultiMaterial.md) of selected objects

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Schedule](Arch_Schedule.md): Creates different types of schedules.

-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Preflight checks\...](BIM_Preflight.md): Perform different checks on your model before exporting to IFC.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation styles\...](Draft_AnnotationStyleEditor.md): Allows you to define styles that affect the visual properties of annotation-like objects.

### Utils

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Toggle bottom panels](BIM_TogglePanels.md): Shows or hides output windows (the Report view and the Python console).

-   <img alt="" src=images/BIM_Trash.svg  style="width:32px;"> [Move to Trash](BIM_Trash.md): Moves selected objects to a Trash group, which gets created if necessary

-   <img alt="" src=images/BIM_WPView.svg  style="width:32px;"> [Working Plane View](BIM_WPView.md): Sets the camera to face the current working plane

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group](Draft_SelectGroup.md): Selects the contents of [Std Groups](Std_Group.md) or group-like [Arch](Arch_Workbench.md) objects.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Set slope](Draft_Slope.md): Slopes selected [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md) by increasing, or decreasing, the Z coordinate of all points after the first one.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Create working plane proxy](Draft_WorkingPlaneProxy.md): Creates a working plane proxy to save the current [Draft working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to construction group](Draft_AddConstruction.md): Moves objects to the [Draft construction group](Draft_ToggleConstructionMode.md).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Split Mesh](Arch_SplitMesh.md): Splits a selected mesh into separate components.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Mesh to Shape](Arch_MeshToShape.md): Converts a mesh into a shape, unifying coplanar faces.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Select non-manifold meshes](Arch_SelectNonSolidMeshes.md): Selects all non-manifold meshes from the current selection or from the document.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remove Shape from Arch](Arch_RemoveShape.md): Turns cubic shape-based Arch object fully parametric.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Close holes](Arch_CloseHoles.md): Closes holes in a selected shape-based object.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Merge Walls](Arch_MergeWalls.md): Merges walls.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Check](Arch_Check.md): Check if the selected objects are solids and don\'t contain defects.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Toggle IFC B-rep flag](Arch_ToggleIfcBrepFlag.md): Forces a selected object to be exported as an [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Toggle subcomponents](Arch_ToggleSubs.md): Shows or hides the subcomponents of an Arch object.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Survey](Arch_Survey.md): Enters or leaves surveying mode.

-   <img alt="" src=images/BIM_Diff.svg  style="width:32px;"> [IFC Diff](BIM_Diff.md): Shows a visual diff between two IFC files

-   <img alt="" src=images/BIM_IfcExplorer.svg  style="width:32px;"> [IFC explorer](BIM_IfcExplorer.md): Opens a tool to explore the structure of an IFC file prior to importing

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Create IFC spreadsheet\...](Arch_IfcSpreadsheet.md): This tool creates a spreadsheet to store IFC properties of an object.

-   <img alt="" src=images/BIM_ImagePlane.svg  style="width:32px;"> [Image plane](BIM_ImagePlane.md): Inserts an image plane in the document.

-   <img alt="" src=images/BIM_Unclone.svg  style="width:32px;"> [Unclone](BIM_Unclone.md): Makes a cloned object independent from its original object

-   <img alt="" src=images/BIM_Rewire.svg  style="width:32px;"> [Rewire](BIM_Rewire.md):

-   <img alt="" src=images/BIM_Glue.svg  style="width:32px;"> [Glue](BIM_Glue.md):

-   <img alt="" src=images/BIM_Reextrude.svg  style="width:32px;"> [Reextrude](BIM_Reextrude.md): Recreates an extrusion from a shape that has lost its parametric extrusion by selecting a base face

-   Panel tools:

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel.md): Creates a panel object from a selected 2D object.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Panel Cut](Arch_Panel_Cut.md): Creates a 2D cut view from a panel.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Panel Sheet](Arch_Panel_Sheet.md): Creates a 2D cut sheet including panel cuts or other 2D objects.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Nest](Arch_Nest.md): Allows to nest several flat objects inside a container shape.

-   Structure tools:

  - <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Structure](Arch_Structure.md): Creates a structural element from scratch or using a selected object as a base.

  - <img alt="" src=images/Arch_StructuralSystem.svg  style="width:32px;"> [Structural System](Arch_StructuralSystem.md):

  - <img alt="" src=images/Arch_StructuresFromSelection.svg  style="width:32px;"> [Multiple Structures](Arch_StructuresFromSelection.md):

-   <img alt="" src=images/IFC_Diff.svg  style="width:32px;"> [IFC Diff\...](IFC_Diff.md):

-   <img alt="" src=images/IFC_Expand.svg  style="width:32px;"> [IFC Expand](IFC_Expand.md):

-   <img alt="" src=images/IFC_MakeProject.svg  style="width:32px;"> [Make IFC project](IFC_MakeProject.md):

-   <img alt="" src=images/IFC_UpdateIOS.svg  style="width:32px;"> [IfcOpenShell update](IFC_UpdateIOS.md):

-   Nudge:

  - [Nudge Switch](BIM_Nudge_Switch.md):

  - [Nudge Up](BIM_Nudge_Up.md):

  - [Nudge Down](BIM_Nudge_Down.md):

  - [Nudge Left](BIM_Nudge_Left.md):

  - [Nudge Right](BIM_Nudge_Right.md):

  - [Nudge Rotate Left](BIM_Nudge_RotateLeft.md):

  - [Nudge Rotate Right](BIM_Nudge_RotateRight.md):

  - [Nudge Extend](BIM_Nudge_Extend.md):

  - [Nudge Shrink](BIM_Nudge_Shrink.md):

### Status bar 

The status bar contains a few buttons that allow to easily change different states:

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Toggle panels](BIM_TogglePanels.md): Shows or hides the [Report view](Report_view.md) and the [Python console](Python_console.md).

-   <img alt="" src=images/BIM_ToggleViews.svg  style="width:32px;"> Toggle Views: Shows or hides the [BIM Views](BIM_Views.md) panel.

-   <img alt="" src=images/BIM_ToggleBackground.svg  style="width:32px;"> Cycle background: Cycles between vertical gradient, radial gradient and simple color background modes. This can be used to toggle between a dark background for modelling and a white background for 2D drawing.

-   <img alt="" src=images/IFC.svg  style="width:32px;"> Lock IFC: Switches between [locked and unlocked IFC mode](NativeIFC#Locked_and_unlocked_modes.md).

### Tree view context menu 

TBD

### 3D view context menu 

TBD

### Obsolete tools 

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [Arch 3Views](Arch_3Views.md): Creates top, front and side views from a [mesh](Mesh_Workbench.md). Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Arch BuildingPart](Arch_BuildingPart.md): Creates a building part including selected objects. Not available in <small>(v1.0)</small> . Use [Arch Floor](Arch_Floor.md) instead.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Arch CloneComponent](Arch_CloneComponent.md): Produces Arch Components that are clones of selected Arch objects. Not available in <small>(v1.0)</small> . Use [Draft Clone](Draft_Clone.md) instead.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Arch CutLine](Arch_CutLine.md): Cuts an object according to a line. Not available in <small>(v1.0)</small> . Use [Arch CutPlane](Arch_CutPlane.md) instead.

-   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Arch MultiMaterial](Arch_MultiMaterial.md): Creates a multi-material and attributes it to selected objects, if any. Not available in <small>(v1.0)</small> . Use [BIM Material](BIM_Material.md) instead.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Arch Project](Arch_Project.md): Creates a project including selected objects. Not available in <small>(v1.0)</small> . Use [BIM Project](BIM_Project.md) instead.

-   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Arch SetMaterial](Arch_SetMaterial.md): Creates a material and attributes it to selected objects, if any. Not available in <small>(v1.0)</small> . Use [BIM Material](BIM_Material.md) instead.

## Preferences

-   <img alt="" src=images/Preferences-bim.svg  style="width:32px;"> [Preferences](BIM_Preferences.md): General preferences for the BIM Workbench.
-   [Fine tuning](Fine-tuning#BIM_Workbench.md): Extra parameters to fine-tune BIM behavior.

## Working with IFC 

The BIM workbench works natively with [Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC) files. Native means there is no more translation between the IFC contents and FreeCAD: The IFC contents are directly rendered in FreeCAD, and any change affects the IFC contents directly. Read more on [NativeIFC](NativeIFC.md).

If you don\'t plan to work with others, and have no need for IFC, you can still use the BIM workbench tools and simply ignore anything related to IFC. You can still export your model to IFC anytime.

The old [Arch IFC](Arch_IFC.md) importer is disabled by default in FreeCAD, but still available from Python.

## File formats 

-   [IFC](Arch_IFC.md): industry foundation classes
-   [DAE](Arch_DAE.md): Collada mesh format
-   [OBJ](Arch_OBJ.md): OBJ mesh format (export only)
-   [JSON](Arch_JSON.md): JavaScript Object Notation format (export only)
-   [3DS](Arch_3DS.md): 3DS format (import only)
-   [SHP](Arch_SHP.md): GIS Shapefiles (import only)

## API

The Arch module can be used in [Python](Python.md) scripts and [macros](Macros.md) using the [Arch Python API](Arch_API.md) functions.

## Tutorials and learning 

-   [Migrating to FreeCAD from Revit](Migrating_to_FreeCAD_from_Revit.md)
-   [Arch & BIM tutorials on this wiki](Tutorials#Architecture_and_BIM.md)
-   [\"BIM with FreeCAD\" video series by Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutorials\" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" video series by Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)
-   [\"HRCompacta\" youtube channel (most content is in portuguese)](https://www.youtube.com/@HRCompacta)
-   [\"FreeCADBIM\" youtube channel (most content is in portuguese)](https://www.youtube.com/@FreeCadBIM)

## Example files 

-   FreeCAD features a BIM example file on the Start page.
-   More example BIM files are available at <https://github.com/yorikvanhavre/FreeCAD-BIM-examples> . From within FreeCAD, use menu Help -\> BIM examples.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [BIM](Category_BIM.md) > BIM Workbench
