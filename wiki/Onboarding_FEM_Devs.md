# Onboarding FEM Devs
{{TOCright}}

## Description

This page will orient new developers on how to setup their development environments in order to hack on the FEM workbench.

## Setting up a Dev Environment 

TBD

### Prerequisites

-   Netgen

### Recommended

-   Paraview

### Compiling via Source 

TBD

### Compiling via Docker 

TBD

## Source Code Management 

Keeping FreeCAD up-to-date is documented in [Source code management](Source_code_management.md) page. Along with useful `git` tips.

## FEM Code Infrastructure 

The FEM code lives in `src/Mod/Fem`

-    `App/`console-mode application, defines basic structures and base classes for document objects, that are used by modules to build their own.

-    `Gui/`GUI-mode application, defines the [3D view](3D_view.md), tools/functions used by workbench to interact with UI and 3D view, defines base classes for [view providers](Viewprovider.md).

-    `femcommands/`
    

-    `fem.dox`
    

-    `femexamples/`
    

-    `femguiobjects/`
    

-    `femguiutils/`
    

-    `feminout/`
    

-    `femmesh/`
    

-    `femobjects/`
    

-    `femresult/`
    

-    `femsolver/`
    

-    `femtaskpanels/`
    

-    `femtest/`
    

-    `femtools/`
    

-    `femviewprovider/`
    

-    `InitGui.py`
    

-    `Init.py`
    

-    `ObjectsFem.py`
    

-    `TestFemApp.py`
    

-    `TestFemGui.py`
    

### Coding Conventions 

Please see [coding\_conventions.md](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Fem/coding_conventions.md) file on the FreeCAD repository.

## Adding New FEM Solvers 

A new FEM solver requires the following:

-   Mesh exporter
-   Results importer
-   Solver object (needs changes in solver settings, unit tests, ObjectsFem modules as well)
-   Task and writer module (here is where the main solver input writing happens)
-   GUI tool to create a solver
-   GUI preference tab to set the solver binary path
-   A solver input writing unit test. Best to take the ccx cantilever. This is available for all mesh element types
-   Having one or two beers

See also:

-   [Add FEM Solver Tutorial](Sandbox_Add_FEM_Solver_Tutorial.md)
-   [Extend FEM Module](Extend_FEM_Module.md)
-   The implementation efforts of the [oofem](https://github.com/berndhahnebach/FreeCAD_bhb/commits/femoofem) solver
-   The implementation efforts of the \[<https://github.com/FreeCAD/FreeCAD/compare/a03eb6b9625ba>\...dfc01ec949525 myStran\] solver

## Writing Unit Tests 

TBD

## Informative

-   [Wrapping a Cplusplus class in Python](Wrapping_a_Cplusplus_class_in_Python.md)
-   [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md)
-   [Add Button to FEM Toolbar Tutorial](Add_Button_to_FEM_Toolbar_Tutorial.md)

## Related

-   FEM bugs in the [FreeCAD bugtracker](https://tracker.freecadweb.org/set_project.php?project_id=4;14)
-   Open FEM [FIXME](https://github.com/FreeCAD/FreeCAD/search?q=FIXME+AND+fem) comments in the FreeCAD source code
-   Open FEM [TODO](https://github.com/FreeCAD/FreeCAD/search?q=TODO+AND+fem) comments in the FreeCAD source code
-   [Original thread discussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=60574) for this wiki page
-   [FEM Workbench](FEM_Workbench.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Onboarding FEM Devs
