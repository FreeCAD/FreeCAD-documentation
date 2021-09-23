# Feature list/zh-tw
This is an extensive, but not complete, list of features which FreeCAD implements. If you want to look into the future see the [Development roadmap](Development_roadmap.md) for a quick overview of what\'s coming next. Also, the [Screenshots](Screenshots.md) are a nice place to go.


{{TOCright}}

## Release notes 

-   [Release 0.11](Release_notes_0.11.md) - March 2011
-   [Release 0.12](Release_notes_0.12.md) - December 2011
-   [Release 0.13](Release_notes_0.13.md) - January 2013
-   [Release 0.14](Release_notes_0.14.md) - March 2014
-   [Release 0.15](Release_notes_0.15.md) - March 2015
-   [Release 0.16](Release_notes_0.16.md) - April 2016
-   [Release 0.17](Release_notes_0.17.md) - April 2018
-   [Release 0.18](Release_notes_0.18.md) - March 2019
-   [Release 0.19](Release_notes_0.19.md) - March 2021
-   [Release 0.20](Release_notes_0.20.md) - TBD

## Key features 

-   ![](images/Feature1.jpg ) A complete [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE)-based **geometry kernel** allowing complex 3D operations on complex shape types, with native support for concepts like [Boundary Representation](https://en.wikipedia.org/wiki/Boundary_representation) (BREP), [Non-uniform rational basis spline](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) (NURBS) curves and surfaces, a wide range of geometric entities, boolean operations and [fillets](https://en.wikipedia.org/wiki/Fillet_(mechanics)), and built-in support of [STEP](https://en.wikipedia.org/wiki/ISO_10303) and [IGES](https://en.wikipedia.org/wiki/IGES) formats 
-   ![](images/Feature3.jpg ) A full **parametric model**. All FreeCAD objects are natively parametric, meaning their shape can be based on [properties](Property.md) or even depend on other objects. All changes are recalculated on demand, and recorded by an undo/redo stack. New object types can be added easily, and can even be [fully programmed in Python](Scripted_objects.md).
-   ![](images/Feature4.jpg ) A **modular architecture** that allows plugin extensions (modules) to add functionality to the core application. An extension can be as complex as a whole new application programmed in C++ or as simple as a [Python script](Power_users_hub.md) or self-recorded [macro](macros.md). You have complete access to almost any part of FreeCAD from the built-in **Python** interpreter, macros or external scripts, be it [geometry creation and transformation](Topological_data_scripting.md), the 2D or 3D representation of that geometry ([scenegraph](scenegraph.md)) or even the [FreeCAD interface](PySide.md) 
-   ![](images/Feature5.jpg ) Import/export to **standard formats** such as [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) or [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) in addition to FreeCAD\'s native {{FileName|[FCStd](File_Format_FCStd.md)}} file format. The level of compatibility between FreeCAD and a given file format can vary, since it depends on the module that implements it.
-   ![](images/Feature7.jpg ) A [Sketcher](Sketcher_Workbench.md) with integrated constraint-solver, allowing you to sketch geometry-constrained 2D shapes. The constrained 2D shapes built with Sketcher may then be used as a base to build other objects throughout FreeCAD.
-   ![](images/Feature9.jpg ) A [Robot simulation](Robot_Workbench.md) module that allows you to study robot movements in a graphical environment.
-   ![](images/Feature8.jpg ) A [technical drawing module](TechDraw_Workbench.md) with options for detail views, cross sectional views, dimensioning and others, allowing you to generate 2D views of existing 3D models. The module then produces ready-to-export SVG or PDF files. An older [Drawing workbench](Drawing_Workbench.md) with sparse Gui-commands but a powerful Python functionality also exists.
-   ![](images/Feature-raytracing.jpg ) A [Rendering](Raytracing_Workbench.md) module that can export 3D objects for rendering with external renderers. It currently only supports [povray](http://en.wikipedia.org/wiki/POV-Ray) and [LuxRender](http://en.wikipedia.org/wiki/LuxRender), but is expected to be extended to other renderers in the future.
-   ![](images/Feature-arch.jpg ) An [Architecture](Arch_Workbench.md) module that allows [Building Information Modeling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM)-like workflow, with [Industry Foundation Classes](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC) compatibility.
-   ![](images/Feature-CAM.jpg ) A [Path module](Path_Workbench.md) dedicated to mechanical machining for [Computer Aided Manufacturing](https://en.wikipedia.org/wiki/Computer-aided_manufacturing) (CAM). Using the Path module you may output, display and adjust the [G code](http://en.wikipedia.org/wiki/G-code) used to control the target machine.
-   ![](images/Feature_spreadsheet.png ) An [Integrated Spreadsheet](Spreadsheet_Workbench.md) and an [expression parser](Expressions.md) which may be used to drive formula-based models and organize model data in a central location.

## General features 

-   **multi-platform**. FreeCAD runs and behaves exactly the same way on Windows, Linux, macOS and other platforms.

-   **full GUI application**. FreeCAD has a complete Graphical User Interface based on the [Qt](https://www.qt.io/) framework, with a 3D viewer based on [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor); allowing fast rendering of 3D scenes and a very accessible scene graph representation.

-   **runs as a command line application**. In command line mode, FreeCAD runs without its interface but with all its geometry tools. In this mode it has a relatively low memory footprint and can be used, for example, as a server to produce content for other applications.

-   **can be imported as a [Python module](Embedding_FreeCAD.md)**. FreeCAD can be imported into any application that can run Python scripts. As in command line mode, the interface part of FreeCAD is unavailable, but all geometry tools are accessible.

-   **workbench concept**. In the FreeCAD interface, tools are grouped by [workbenches](workbenches.md). This allows you to display only the tools used to accomplish a certain task, keeping the workspace uncluttered and responsive, and allowing the application to load rapidly.

-   **plugin/module framework for late loading of features/data-types**. FreeCAD is divided into a core application with modules that are loaded only when needed. Almost all tools and geometry types are stored in modules. Modules behave like plugins; in addition to delayed loading, individual modules can be added to or removed from an existing installation of FreeCAD.

-   **parametric associative document objects**. All objects in a FreeCAD document can be defined by parameters. Those parameters can be modified and recomputed at any time. Since object relationships are maintained, the modification of one object will automatically propagate to any dependent objects.

-   **parametric primitive creation**. Primitive objects such as box, sphere, cylinder, etc. can be created by specifying their geometry constraints.

-   **graphical modification operations**. FreeCAD can perform translation, rotation, scaling, mirroring, offset (either trivial or as described in [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting)) or shape conversion, in any plane of the 3D space.

-   **[Constructive solid geometry](Constructive_solid_geometry.md) (boolean operations)**. FreeCAD can do constructive solid geometry operations (union, difference, intersect).

-   **graphical creation of planar geometry**. Lines, wires, rectangles, B-splines, and circular or elliptic arcs can be created graphically in any plane of the 3D space.

-   **modeling with straight or revolved** **extrusions**, **sections** and **fillets**.

-   **topological components** like **vertices**, **edges**, **wires** and **planes**.

-   **testing and repairing**. FreeCAD has tools for testing meshes (solid test, non-two-manifolds test, self-intersection test) and for repairing meshes (hole filling, uniform orientation).

-   **annotations**. FreeCAD can insert annotations for text or dimensions.

-   **Undo/Redo framework**. Everything in FreeCAD is undo/redoable, with user access to the undo stack. Multiple steps can be undone at one time.

-   **transaction oriented**. The undo/redo stack stores document transactions, not single actions, allowing each tool to define exactly what must be undone or redone.

-   **built-in [scripting](Scripting.md) framework**. FreeCAD features a built-in [Python](http://www.python.org/) interpreter, with an API that covers almost any part of the application, the interface, the geometry and the representation of this geometry in the 3D viewer. The interpreter can run complex scripts as well as single commands; entire modules can be programmed completely in Python.

-   **built-in Python console**. The Python interpreter includes a console with syntax highlighting, autocomplete and a class browser. Python commands can be issued directly in FreeCAD and immediately return results, permitting script writers to test functionality on the fly, explore the contents of FreeCAD\'s modules and easily learn about FreeCAD internals.

-   **mirrors user interaction**. Everything the user does in the FreeCAD interface executes Python code, which can be printed on the console and recorded in macros.

-   **full [macro](Macros.md) recording and editing** capabilities. The Python commands issued when the user manipulates the interface can be recorded, edited if needed, and saved to be reproduced later.

-   **compound (ZIP based) document save format**. FreeCAD documents are saved with a {{FileName|.[FCStd](File_Format_FCStd.md)}} extension. The document can contain many different types of information such as geometry, scripts or thumbnail icons. The {{FileName|.FCStd}} file is itself a zip container; a saved FreeCAD file has already been compressed.

-   **fully customizable/scriptable Graphical User Interface**. The [Qt](https://www.qt.io)-based interface of FreeCAD is entirely accessible via the Python interpreter. Aside from simple functions FreeCAD itself provides to workbenches, the entire Qt framework is accessible. The user may perform any operation on the GUI such as creating, adding, docking, modifying or removing widgets and toolbars.

-   **thumbnailer**. (currently only Linux systems) FreeCAD document icons show the contents of the file in most file manager applications such as Gnome\'s Nautilus.

-   **modular MSI installer**. FreeCAD\'s installer allows flexible installations on Windows systems. Packages for Ubuntu systems are also maintained.

## In development 

-   ![](images/Feature-assembly.jpg ) An [Assembly](Assembly_project.md) module that allows one to work with multiple projects, multiple shapes, multiple documents, multiple files, multiple relationships\... This module is currently in the planning state.

## Extra Workbenches 

Power users have created various custom [external workbenches](external_workbenches.md).







[Category:User Documentation](Category:User_Documentation.md)

---
[documentation index](../README.md) > [User Documentation](Category:User Documentation.md) > Feature list/zh-tw
