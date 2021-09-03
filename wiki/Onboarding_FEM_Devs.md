
{{TOCright}}

## Description

This page will orient new developers on how to setup their development environments in order to hack on the FEM workbench.

## Setting up a Dev Environment {#setting_up_a_dev_environment}

TBD

### Prerequisites

-   Netgen
-
### Recommended

-   Paraview

### Compiling via Source {#compiling_via_source}

TBD

### Compiling via Docker {#compiling_via_docker}

TBD

## Source Code Management {#source_code_management}

Keeping FreeCAD up-to-date is documented in [Source code management](Source_code_management.md) page. Along with useful `git` tips.

## FEM Code Infrastructure {#fem_code_infrastructure}

The FEM code lives in `src/Mod/Fem`

-    `App/`console-mode application, defines basic structures and base classes for document objects, that are used by modules to build their own.

-    `Gui/`GUI-mode application, defines the [3D view](3D_view.md), tools/functions used by workbench to interact with UI and 3D view, defines base classes for [view providers](view_provider.md).

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
    

### Coding Conventions {#coding_conventions}

Please see [coding\_conventions.md](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Fem/coding_conventions.md) file on the FreeCAD repository.

## Adding New FEM Solvers {#adding_new_fem_solvers}

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

-   [Add FEM solver tutorial](Add_FEM_solver_tutorial.md)
-   [Extend\_FEM\_Module](Extend_FEM_Module.md)
-   The implementation efforts of the [oofem](https://github.com/berndhahnebach/FreeCAD_bhb/commits/femoofem) solver
-   The implementation efforts of the \[<https://github.com/FreeCAD/FreeCAD/compare/a03eb6b9625ba>\...dfc01ec949525 myStran\] solver

## Writing Unit Tests {#writing_unit_tests}

TBD

## Informative

-   [Wrapping a Cplusplus class in Python](Wrapping_a_Cplusplus_class_in_Python.md)
-   [Add FEM equation tutorial](Add_FEM_equation_tutorial.md)
-   [Add button to FEM toolbar tutorial](Add_button_to_FEM_toolbar_tutorial.md)

## Related

-   FEM bugs in the [FreeCAD bugtracker](https://tracker.freecadweb.org/set_project.php?project_id=4;14)
-   Open FEM [FIXME](https://github.com/FreeCAD/FreeCAD/search?q=FIXME+AND+fem) comments in the FreeCAD source code
-   Open FEM [TODO](https://github.com/FreeCAD/FreeCAD/search?q=TODO+AND+fem) comments in the FreeCAD source code
-   [Original thread discussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=60574) for this wiki page
-   [FEM Workbench](FEM_Workbench.md)
-
[Category:FEM](Category:FEM.md) [Category:FEM{{\#translation:}}](Category:FEM.md) [Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md)
