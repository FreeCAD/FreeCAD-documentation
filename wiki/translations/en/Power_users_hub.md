# <img alt="" src=images/Power_user_hub.png  style="width:64px;"> Power users hub/en





This is the place to come if you are an experienced user and want to learn more about customizing and extending FreeCAD.

FreeCAD is extensible by [Python](Python.md) code that is run directly in the [Python console](Python_console.md), or that is loaded from modules at startup. This means that you can modify FreeCAD without needing to recompile the program. For example, you can:

-   **Create and modify geometry**: you can create a new object type, either from scratch or by adapting an existing type.
-   **Create custom tools and commands**: add your own set of tools that run your code.
-   **Modify the interface**: create toolbars to put your tools, create special windows, panels, or interfaces for interacting with your tools.
-   **Modify the scenegraph representation**: FreeCAD has separate processes for building up the geometry and displaying that geometry on screen. You have full access to the way the scene contents are displayed on screen, therefore you can modify that representation, interact with it, or add custom behaviour to it. You can also add custom screen widgets, like information, draggers, anchors or temporary entities.

If you\'d like to contribute content to these pages, request a wiki account with editor permissions [in the forum](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830), and read the [WikiPages](WikiPages.md) for the general guidelines that you should follow. For other ways to contribute with the project, see the [Help FreeCAD](Help_FreeCAD.md) page.

## Customizing FreeCAD 

-   [Interface Customization](Interface_Customization.md): Starting with the beginning: Toolbars and shortcuts
-   [Working with Macros](Macros.md): Easily record often repeated tasks or Python code
-   [Macros recipes](Macros_recipes.md)
-   [Customize Toolbars](Customize_Toolbars.md)
-   [Installing more workbenches](Installing_more_workbenches.md)

## Scripting in FreeCAD 

### General

-   [Introduction to Python](Introduction_to_Python.md) - See also other Python tutorials at the bottom of this page
-   [FreeCAD scripting tutorial](Python_scripting_tutorial.md) - A general look at python scripting in FreeCAD
-   [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md): Well, the basics.
-   [Gui Command](Gui_Command.md): Adding custom commands to the GUI
-   Using mixed [Units](Units.md) in FreeCAD
-   [Profiling](Profiling.md) the Python code
-   [Debugging](Debugging#Python_Debugging.md) the Python code

### Modules

The functionality of FreeCAD is separated in Modules which deal with special data types and applications. FreeCAD has built-in modules and Extension Modules (plug-ins). Once plugin modules are installed, they become availible to you as easily as the built-in modules. The modules described below are the default modules, includeed in every FreeCAD installation.

-   The [Builtin modules](Builtin_modules.md) are the principal FreeCAD modules. They contain tools for manipulating general FreeCAD configurations, documents and their contents.
-   [Workbench creation](Workbench_creation.md) shows you how to create your own workbench

#### Working with Meshes 

-   [Mesh Scripting](Mesh_Scripting.md): How to interact with the [Mesh Workbench](Mesh_Workbench.md)

#### Working with Parts 

-   [The Part Workbench](Part_Workbench.md): How [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE) tools and structure is used in FreeCAD
-   [Topological data scripting](Topological_data_scripting.md): How to interact with the Part Module
-   [PythonOCC](PythonOCC.md): How to unleash the whole Open CASCADE power
-   [Mesh to Part](Mesh_to_Part.md): Converting between object types

#### Accessing the Coin scenegraph 

-   [The Coin/Inventor scenegraph](Scenegraph.md): How the FreeCAD scene representation works
-   [Pivy](Pivy.md): How to access and modify the scenegraph

### Controlling the Qt interface 

-   [PySide](PySide.md): How to access the interface, and modify its contents
-   [Using the FreeCAD GUI](Embedding_FreeCADGui.md) in another Qt application with PyQt

### Working with parametric objects 

-   [Scripted objects](Scripted_objects.md): how to make 100% Python-scripted objects.
    -   [Scripted objects with attachment](Scripted_objects_with_attachment.md): how to make scripted objects attachable to other objects.
    -   [Scripted objects saving attributes](Scripted_objects_saving_attributes.md): how to save and restore attributes of the proxy class with `__getstate__` and `__setstate__`.
    -   [Scripted objects migration](Scripted_objects_migration.md): how to migrate old scripted objects to a new class.

### Examples

-   [Code snippets](Code_snippets.md) : A collection of pieces of FreeCAD Python code, to serve as ingredients in your scripts\...
-   [Line drawing function](Line_drawing_function.md): How to build a simple tool to draw lines
-   [Dialog creation](Dialog_creation.md): How to construct dialogs with Qt designer, and use them in FreeCAD
-   [Embedding FreeCAD](Embedding_FreeCAD.md): How to import FreeCAD as a Python module in other applications
-   The [Draft Workbench](Draft_Workbench.md) adds basic 2d drawing functions to freecad. It is written entirely in Python, so it can be a good example if you want to write your own modules.
-   [FreeCAD vector math library](FreeCAD_vector_math_library.md) : A couple of handy functions to manipulate FreeCAD vectors. This library is also included in the Draft module.

## API Functions 

The complete API documentation of FreeCAD is located at <http://www.freecadweb.org/api/> . It contains both C++ and Python APIs, and is not totally well formatted yet, which can be confusing when looking for python-only code. An easier to browse version can be found [here](:Category_API.md). Note that it can be incomplete, since it is updated manually. For more accurate information, browse the modules directly from FreeCAD\'s Python console.

Related: [Exposing C++ to Python](Exposing_C%2B%2B_to_Python.md)

## Advanced modification 

-   [Start up and Configuration](Start_up_and_Configuration.md): Startup and command line options
-   [Installing on Windows](Installing_on_Windows.md): Using the windows installer
-   [Compiling FreeCAD on Windows](Compile_on_Windows.md) and [Compiling FreeCAD on Linux](Compile_on_Linux.md)
-   [Branding](Branding.md): Simple modifications you can do to the source code to change some aspects of FreeCAD
-   [Extra python modules](Extra_python_modules.md) : Extend the FreeCAD python interpreter with these powerful modules!

## Python tutorials 

These are good generic tutorials, not specific to FreeCAD, that might interest you if you are totally new to python.

**Python**

-   [Official python tutorial](https://docs.python.org/3/tutorial/index.html) - A very complete tutorial for discovering python
-   [Non-programmer tutorial for python](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3) - an excellent wikibook
-   [Python for newbies](http://npt.cc.rsu.ru/user/wanderer/ODP/Python_for_Newbies.htm) - one big tutorial covering all the basics

**PySide** - How to create and manage FreeCAD\'s Qt UI interface from python

-   [PySide tutorial](http://zetcode.com/gui/pysidetutorial/) : A platform-agnostic tutorial showing the usage of PySide with examples
-   [PySide/PyQt tutorial](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) : A easy to read tutorial that covers PySide and PyQt with examples
-   [PySide documentation](http://qt-project.org/wiki/PySideDocumentation) : from the Qt Project (the people who wrote it all)
-   [Using QtCreator in PySide](http://qt-project.org/wiki/QtCreator_and_PySide) : also from the Qt Project
-   [PySide reference](http://srinikom.github.io/pyside-docs/index.html) : endless detail on the minutiae of PySide and Qt, a reliable reference source
-   [PySide code snippets](http://nullege.com/codes/search?cq=PySide) : a searchable database of PySide code snippets

The following two references are PyQt specific (not PySide) but may offer some information of use:

-   [Basic PyQt tutorial](http://www.cs.usfca.edu/~afedosov/qttut/) : A simple and short linux-based tutorial that will explain how to work with PyQt and Qt Designer
-   [Programming Qt applications in python](http://vizzzion.org/?id=pyqt) : A more in-depth tutorial covering all the process of working with qt and python

**Pivy** - How to interact with FreeCAD\'s 3D scenes

-   [Pivy - Embedding a Dynamic Scripting Language into a Scene Graph Library](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.947&rep=rep1&type=pdf) : Thesis that explains Pivy in detail
-   [High Level 3D Graphics Programming in Python](http://ftp.ntua.gr/mirror/python/pycon/dc2004/papers/47/) : Pivy example from Pycon 2004
-   [Introducing Pivy into studierstube](https://www.semanticscholar.org/paper/Integrating-Pivy-into-Studierstube-4.2-Gruber/08c9a89c8326c87f81c2d83428029fbfb6c2ae64) [(Mirror)](https://www.researchgate.net/publication/228737136_Integrating_Pivy_into_Studierstube_42) : A paper that is not really a tutorial, but that illustrates well how Pivy works (requires an academic account)

## Community projects 

On the [Community portal](FreeCAD_Community_Portal.md), you can find other FreeCAD-based projects run by the FreeCAD users community. If you are starting a new FreeCAD project, be sure to list it there! We also have a page with things you can do if you would like to [Help FreeCAD](Help_FreeCAD.md).

-   [Scientific literature](Scientific_literature.md): articles that reference or use the FreeCAD system in different ways.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > Power users hub/en
