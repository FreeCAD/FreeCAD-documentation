# Release notes 0.14/cs
FreeCAD 0.14 was released on July 1, 2014. This is a summary of the most interesting changes. The complete list of changes can be found in the [Mantis changelog](http://www.freecadweb.org/tracker/changelog_page.php). Older versions at: [0.13](Release_notes_0.13.md) - [0.12](Release_notes_0.12.md) - [0.11](Release_notes_0.11.md)

<img alt="" src=images/Freecad_jeep.png  style="width:1024px;">


<center>

Jeep model by Psicofil


</center>

## General

### Site migration 

We finally moved all the web applications of FreeCAD from [SourceForge](http://www.sourceforge.net) to our [own domain](http://www.freecadweb.org). The new FreeCAD homepage can be found at <http://www.freecadweb.org>, the wiki is now at <http://www.freecadweb.org/wiki>, the bug and features tracker at <http://www.freecadweb.org/tracker>, and the forum at <http://forum.freecadweb.org>. If you had an account on one of these applications when we were on SourceForge, you can regain your existing user following these [instructions](http://forum.freecadweb.org/viewtopic.php?f=8&t=4942).

The only part of FreeCAD that remains at SourceForge is the main git repository, at the same address: <http://sourceforge.net/p/free-cad/code/ci/master/tree/> but there is also have an automatic mirror of that code set up on github, at <http://github.com/FreeCAD/FreeCAD_sf_master>

If you haven\'t met the incredible FreeCAD community yet, pay us a visit on the forum, and be amazed by its talent, energy and helpfulness.

### Move to pyside, FreeCAD is now fully LGPL 

With the many complications caused by the double-license model of FreeCAD (LGPL & GPL), some of the components of FreeCAD (namely the OpenCasCade kernel) being incompatible with GPL code, we decided to switch all the remaining bits of GPL code of FreeCAD to LGPL. As a result of this operation, [PyQt](http://en.wikipedia.org/wiki/PyQt) is not used anymore, and has been replaced by [PySide](http://en.wikipedia.org/wiki/PySide). There is not much consequence for python scriptwriters, PyQt can still be used inside FreeCAD.

After we finished the move to LGPL, OpenCasCade has [switched to LGPL](http://www.opencascade.org/getocc/license/) too, which would have solved all our license conflicts too. But we have now a much clearer and unified license model, which should satisfy all the strictest linux distributions.

### Plugins and side projects: Parts library, BOLTS, Eagle importer 

The last year has seen a couple of interesting side projects emerge along FreeCAD. A [Parts library](http://github.com/yorikvanhavre/FreeCAD-library) has been started by the community and is slowly growing, consisting of a collection of reusable parts to add to your FreeCAD models. It can be launched and used from inside FreeCAD with the use of a macro.

Another similar but more ambitious project is [BOLTS](http://bolts-library.org/), which is also a parts library, but built from parametric scripts, able to produce a wide variety of parametric parts. BOLTS, although application-independent, can also be run from FreeCAD by launching a macro. The image below shows BOLTS running inside FreeCAD.

<img alt="" src=images/Freecad-bearing.png  style="width:1024px;">

Another interesting external project is the [EAGLE importer](http://sourceforge.net/projects/eaglepcb2freecad/), which allows you to import PCB board designs made from several applications into FreeCAD.

### WebGL export 

From FreeCAD, you can now export your scene as a [WebGL](http://en.wikipedia.org/wiki/WebGL)-enabled html file. This file includes an embedded [three.js](http://threejs.org/)-based viewer that allows to inspect the scene from the web without any plugin, as long as you view it with a WebGL-capable browser.

### Units system 

Finally, a [units](units.md) system has been implemented at FreeCAD level, so it is available to all modules. You are now able to choose a units schema from the preferences. Currently available schemas include millimeters, meters and imperial measurements, but more should become available soon. Once this schema is set, most properties and tools of FreeCAD will use this unit preferentially. But the system is very flexible, and in most places, you can mix units as much as you like, for example giving measures in inches in a document set in millimeters.

### Style Sheets 

FreeCAD 0.14 becomes even more customizable with the addition of [Style Sheets](http://forum.freecadweb.org/viewtopic.php?f=8&t=4700&start=30) being used to control the background image in the main window. No longer is the user stuck with the grey stone background. Almost any image, picture or custom tile may be used to fill the background space in FreeCAD\'s main Window.

<img alt="" src=images/Style_Sheets.png  style="width:1024px;">

### Display style override 

The default View toolbar has been extended with a couple of new buttons to easily switch the display of the whole 3D view to wireframe, shaded or flat lines mode.

### 3D window anti-aliasing 

New options have been added to the 3D view anti-aliasing system of FreeCAD, that you can find in the preferences. If you have a good 3D graphic chip, you can now enjoy FreeCAD with very high-quality anti-aliasing.

## Part

### Loft and Sweep 

The [Part Loft](Part_Loft.md) and [Part Sweep](Part_Sweep.md) tools have been improved and can now use Draft Workbench objects as profiles

### Offset

The new [Part Offset](Part_Offset.md) tool creates copies of a selected shape at a certain distance from the base shape.

### Thickness

A new [Part Thickness](Part_Thickness.md) tool is now available. This tool works on a solid shape, and turns it into a hollow object, by giving each of its faces a given thickness.

### Make Compound 

The [Part Workbench](Part_Workbench.md) now features a [Make Compound](Part_Compound.md) tool, which allows you to quickly create a compound object from a set of selected shapes.

### Part Primitives 

New Part primitives have been added to the [Part CreatePrimitives](Part_CreatePrimitives.md) tool: Prisms, regular polygons and spirals are now easy to create by filling out a couple of parameters. Furthermore, some tools from the [Draft Workbench](Draft_Workbench.md) can now take advantage of this feature and create these primitives too, instead of their regular Draft object, when the appropriate option is set in the Draft preferences settings.

![](images/Part_Create_Primitives1.jpeg )

### Measure tools 

A new measurement toolset has been added to the [Part workbench](Part_Workbench.md). With it, you can select two shape elements (vertices, edges or faces), and display the distance between the two in absolute distance, and along X and Y axes.

## PartDesign & Sketcher 

### Validate sketch 

The [Sketcher](Sketcher_Workbench.md) now features a new [Validate sketch](Sketcher_ValidateSketch.md) tool to help you to validate a sketch, by finding missing or redundant constraints. It can also automatically add some missing constraints, in order to make your sketch fully constrained.

### Gear generator 

An [involute gear generator](PartDesign_InvoluteGear.md) tool has been added to the [PartDesign workbench](PartDesign_Workbench.md), to quickly create such gears from parameters.

## Drawing

### Automatic projections 

The Drawing Workbench continues to be improved with some exciting new features. Orthographic Projections now allows all views to be displayed as well as much greater control over individual views. Another key feature, Drawing Templates may now contain data defining Border and Title Block locations that will automatically confine Projections within the border while at the same time automatically avoiding the space occupied by the Title Block.

<img alt="" src=images/DrawingWB.png  style="width:1024px;">

### Symbols

A new [Drawing Symbol](Drawing_Symbol.md) tool is available on the [Drawing Workbench](Drawing_Workbench.md) allowing to quickly place SVG objects on the Drawing sheet. These objects are stored within the FreeCAD file, so you don\'t need to ship the original SVG file when distributing your files.

## Raytracing

### New rendering tools 

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">

The [Raytracing workbench](Raytracing_Workbench.md) has also received some love, and its toolbar has been reworked. The \"old\" buttons that manually produced partial povray files have been removed (they are still there in the Raytracing menu), and you can now produce a rendering pretty much the same way as you use the [Drawing workbench](Drawing_Workbench.md): You create a new project, give it a template, then fill it with views of your objects. When you are done, just hit the render button, or export it to a file that is ready to render outside of FreeCAD.

The [Raytracing templates](Raytracing_Workbench#Templates.md) system has also been extended, and templates are now easier to manipulate and create.

FreeCAD produced .pov scripts now contain auto-aspect ratio. Users no longer need to maintain a 4:3 aspect ratio in their Raytracing settings or need to manually edit the output to change ratios in order to get a proper render. Any width and height may now be entered without fear that the rendered objects will come out squashed or stretched.

### Luxrender support 

Together with the existing support for [POV-Ray](http://en.wikipedia.org/wiki/POV-Ray), the [Raytracing workbench](Raytracing_Workbench.md) now also supports [LuxRender](http://en.wikipedia.org/wiki/LuxRender). Where POV-Ray is a [classical-style raytracer](http://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29), that shoots rays from the camera in order to find the color of each pixel of the image, Luxrender is an [unbiased renderer](http://en.wikipedia.org/wiki/Unbiased_rendering), which takes much longer to render scenes, but can produce much more realistic lighting.

## Spreadsheet

A new [Spreadsheet Workbench](Spreadsheet_Workbench.md) has been added to FreeCAD. It allows you to create [spreadsheet](Spreadsheet_Create.md) objects, that contain 2-dimensional spreadsheet data. It also features an editor so you can edit the spreadsheet contents (texts, numbers and some basic formulas are supported), and a special [cell controller](Spreadsheet_Controller.md) object, that can scan the document for certain types of objects, extract a certain property from them, and fill a certain range of cells with these values.

<img alt="" src=images/Arch_tutorial_53.jpg  style="width:1024px;">

## Draft

### DWG import/export 

FreeCAD is now able to import and export to the [DWG format](https://en.wikipedia.org/wiki/.dwg), thanks to the free, multiplatform [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter). Once it is installed, and its path set in the FreeCAD Draft preferences settings, FreeCAD will be able to use it to import and export dwg files, by converting them to dxf, then using the Draft dxf importer and exporter. The import and export of dwg files has therefore the same limitations as the [dxf format](Draft_DXF.md).

### Draft to Drawing works with groups 

The [Draft to Drawing](Draft_Drawing.md) tool, used to place Draft objects on a [Drawing](Drawing_Workbench.md) sheet, can now be applied on groups, allowing to create fewer View objects on the Drawing sheet. By intelligently combine your Draft objects into a couple of groups, you have a quick way to control the appearance of many objects on your page.

### Dimensions recoded 

The [Draft Dimension](Draft_Dimension.md) tool has been fully recoded, and dimension objects now behave much better, and have gained a few new properties, allowing to fine-tune them better, such as nicer and scalable arrows, more control over the position of the text and the direction of the dimension, and, above all, better support for the [Drawing Workbench](Drawing_Workbench.md). You can now place dimensions in any plane of the 3D space, and expect correct results when placing them on a Drawing sheet with the [Draft Drawing](Draft_Drawing.md) tool.

<img alt="" src=images/Draft_dimensions_recode.jpg  style="width:1024px;">

### Hatches

The [Draft workbench](Draft_Workbench.md) also features a new toy: hatching. On specific Draft objects (those that form a closed shape such as closed polylines, rectangles, regular polygons or circles), it is now possible to apply hatching. Currently, only a couple of default hatch patterns are available, but since those patterns are very easy to create (they are simple svg files), and custom patterns can already be added by the user, the default collection might grow quickly. Draft objects with patterns are also faithfully supported by the [Drawing workbench](Drawing_Workbench.md).

<img alt="" src=images/Draft_hatches.jpg  style="width:1024px;">

### Ellipses

Support for [ellipses](Draft_Ellipse.md) has been added, the Draft workbench now allows you to draw full or portions of ellipses.

### Chamfer

In the same fashion as fillets, that had appeared in [release 0.13](Release_notes_0.13.md), Draft rectangles, wires and polygons now gained a chamfer property, which chamfers their angle. The chamfer is applied before the fillet,and both properties can be used together, allowing you to quickly turn a very simple wire into a complex object made of many sections.

### Upgrade and downgrade recoded 

The [Draft Upgrade](Draft_Upgrade.md) and [Draft Downgrade](Draft_Downgrade.md) tools, previously hermetic pieces of magic, from which you were never too sure what the result would be, have been recoded, and now output much friendlier messages, informing you what has been done and why. They are now also available to python scripting, not only as a whole, but also their internal operations, so you can precisely order a certain upgrade type to be performed.

### Facebinder

A new [Draft Facebinder](Draft_Facebinder.md) tool has been added, that does a very simple but potentially very useful operation: It gathers any number of selected faces from different objects, and creates a new object from these faces. The new object keeps links to the original objects, so any change in them is reflected in the facebinder object. This should prove useful above all for [architectural](Arch_Workbench.md) objects, where you can now construct new objects from the faces of several others.

### Shape strings 

The [Draft ShapeString](Draft_ShapeString.md) tool creates planar objects from a text and a truetype font. These objects, unlike common annotations such as the [Draft Text](Draft_Text.md), are real 3D objects, can be extruded, and can therefore be used to create engravings and other kinds of 3D objects with text in relief.

### Bezier Curves 

Alongside the existing [arcs of circle](Draft_Arc.md) and [B-spline](Draft_BSpline.md) curves, a new type of curve has just been merged in the Draft workbench: [Bezier curves](Draft_BezCurve.md). They can be created by clicking points, the same way as other Draft objects, but you can then [edit](Draft_Edit.md) them and modify their handle points, gaining a very precise control over the curve shape.

## Arch

### Structure presets + profiles 

The [Arch Structure](Arch_Structure.md) tool has gained several improvements: it now features presets, which allow you to quickly build a beam or column based on a standard profile such as INP or HEB, and an easier placement system, with a special [snapping](Draft_Snap.md) mode. You can now also give structural elements an extrusion path, so very advanced configurations become possible. Some of the pieces offered by [BOLTS](#Plugins_and_side_projects:_Parts_library.2C_BOLTS.2C_Eagle_importer.md) can also be created directly as Arch structural elements.

### Window presets 

The [Arch Window](Arch_Window.md) tool also gained a new presets system. Although still based on sketches, which ensures maximum flexibility (virtually any window type can be easily created), new windows can now be made from a series of presets. You only need to choose a preset, fill a couple of parameters, and place your window, in an exiting wall or structural element if you wish so. Underneath, an appropriate sketch will be created, which is still editable at any later time.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:1024px;">

### Spaces

A new [Space](Arch_Space.md) object is now available, allowing you to build, mark and compute spaces and floor areas. These space objects always encompass a solid volume, so you can always know their volume and floor area. They can be built from a solid shape, or from a set of boundary faces.

### Multilayer walls 

[Walls](Arch_Wall.md) can now be multilayer, with a very simple trick: Several walls can be based on a same baseline, specifying an offset distance from the baseline. This, combined for example with [Arch Frames](Arch_Frame.md), allows for example to create complex framed walls, or walls with an insulation layer. Furthermore, these walls are aware of their \"brothers\" (other walls based on the same baseline), and any window placed on one of these walls will also create a hole on its brothers.

<img alt="" src=images/Screenshot_arch_multiwall.jpg  style="width:1024px;">

### Stairs

A new [Stairs](Arch_Stairs.md) tool has also been added, which allows you to build complex stairs from a couple of parameters. Currently only straight stairs are available, but the list will grow over time. These stairs have many configuration parameters, such as the size of the step floor, or the type of their structure.

### Reinforcing bars 

Reinforcing bars (also called rebars) have been introduced with the [Arch Rebar](Arch_Rebar.md) tool. They are also based on sketches, which ensures great flexibility. They are created basically by drawing the diagrams of the bars on the appropriate faces of [structural elements](Arch_Structure.md), then turning those diagrams into actual rebars.

<img alt="" src=images/Screenshot_arch_rebar.jpg  style="width:1024px;">

### Frames

Frame systems are used everywhere in architecture: Railings, structural systems, frame walls, etc. The new [Arch Frame](Arch_Frame.md) tool allows to easily create all kinds of frames, by combining a profile object, which can be any flat, extrudable shape, such as a rectangle or a circle, and a layout object, which defines extrusion lines on which the members of the frame object are placed. Layouts are typically drawn with the [Sketcher Workbench](Sketcher_Workbench.md). These Frame objects can then be turned into walls or structures if needed.

### Survey

Another simple but useful tool is now available in the Arch workbench: the [Arch Survey](Arch_Survey.md) mode. In this mode, you click on vertices, edges, faces or whole objects, and get their height, length, area or volume. This information is shown on the model, but also copied to the clipboard, and gathered as text, so it is easy to paste in other applications, giving you a pretty fast workflow when building quantities bills.

### Tutorial

A new 35-page [tutorial](Arch_tutorial.md) describes the Arch workbench in all its details, following a complete exercise.

### IFC import & export 

Much work has been done on both FreeCAD and [IfcOpenShell](http://www.ifcopenshell.org), which is the piece of software responsible for handling IFC files in the Arch workbench. When using a [development version](http://github.com/aothms/IfcOpenShell) of IfcOpenShell, apart from a spectacular gain in speed when importing medium-sized IFC files (around 50Mb), FreeCAD is also able to export models to the IFC format. The support to export is still in first stages of development, but already manages to export files readable without errors by most of the major IFC-supporting applications.

## Full list 

The full list of bugfixes and new features can be read on <http://freecadweb.org/tracker/changelog_page.php>

[<img src="images/Property.png" style="width:16px"> News](Category_News.md) [<img src="images/Property.png" style="width:16px"> Documentation](Category_Documentation.md) [<img src="images/Property.png" style="width:16px"> Releases](Category_Releases.md)

---
[documentation index](../README.md) > [News](Category_News.md) > Release notes 0.14/cs
