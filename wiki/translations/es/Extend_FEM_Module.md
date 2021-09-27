# Extend FEM Module/es
<div class="mw-translate-fuzzy">


{{TutorialInfo/es
|Topic= 
|Level= 
|Time= 
|Author=_
|FCVersion=
|Files=
}}


</div>


<div class="mw-translate-fuzzy">

El banco de trabajo FEM ya es compatible con muchas restricciones diferentes y un puñado de solucionadores. A pesar de que las personas a menudo necesitan restricciones no son compatibles con los chorros de FreeCAD. Esta página es el punto de partida para una serie de tutoriales y otros recursos que describen cómo extender el entorno de trabajo FEM utilizando el marco existente. Si bien esta serie también puede ser útil para los desarrolladores de software, la idea es permitir que los usuarios de FEM con un poco de interferencia en la codificación Python agreguen las cosas que necesitan ellos mismos.


</div>

Agregar nuevas restricciones, ecuaciones o solucionadores es principalmente un trabajo de rutina. Pero hacerlo por primera vez no será tan fácil como podría parecer. Una comprensión de los siguientes temas será útil:

-   Python scripting in FreeCAD.
    -   [FreeCAD Scripting Tutorial](Python_scripting_tutorial.md)
    -   [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)
-   Extending FreeCAD with Python.
    -   [Scripted Objects](Scripted_objects.md)
-   A solid understanding of the solver for which new objects shall be added (e.g. CalculiX or Elmer) is important.
-   A little knowledge about build systems, especially cmake (build system used by FreeCAD).

## Build System (cmake) 

The build system must be modified regardless of which objects shall be added o the FEM workbench. Every python module (file) must be registered. The FEM workbench requires every new python module to be registered in `Mod/Fem/CMakeLists.txt`. This is true regardless of the type of the python module (GUI or non-GUI). Where exactly the module must be inserted depends on the role of the module. Solver, equations and constraints all use different lists. Searching for similar files and inserting the new file in the same list works most of the time.

As an **example** lets add a new constraint called  for this constraint. A new constraint requires at least the following new modules:

-    `constraint_<name>.py`
    

-    `view_constraint_<name>.py`
    

-    `CommandFemConstraint<name>.py`(may be unnecessary)

These three files must be added to `Mod/Fem/CMakeLists.txt` as well as `Mod/Fem/App/CMakeLists.txt`. All inserted lines of code are indicated by a starting **+**.


{{FileName|Mod/Fem/CMakeLists.txt}}


{{code|code=
SET(FemObjects_SRCS
    femobjects/__init__.py
    femobjects/base_fempythonobject.py
    femobjects/constraint_bodyheatsource.py
    femobjects/constraint_electrostaticpotential.py
    femobjects/constraint_flowvelocity.py
    femobjects/constraint_initialflowvelocity.py
+   femobjects/constraint_initialflowpressure.py
    femobjects/constraint_selfweight.py
...
    femobjects/solver_ccxtools.py
)
...
SET(FemGuiViewProvider_SRCS
    femviewprovider/__init__.py
    femviewprovider/view_base_femconstraint.py
    femviewprovider/view_base_femobject.py
    femviewprovider/view_constraint_bodyheatsource.py
    femviewprovider/view_constraint_electrostaticpotential.py
    femviewprovider/view_constraint_flowvelocity.py
+   femviewprovider/view_constraint_flowpressure.py
    femviewprovider/view_constraint_initialflowvelocity.py
    femviewprovider/view_constraint_selfweight.py
...
    femviewprovider/view_solver_ccxtools.py
)
}}

## Source Organization 

For organizing the python code the FEM module uses the following approach. The module is split into the following packages:

-    `femobjects`, which contains all non-GUI like python proxies for document objects and

-    `femviewproviders`containing everything GUI related like python proxies for view provider

-   C++ based task panels are stored in \'`Gui`\',

-   icons can be found in \'`Gui/Resources/icons/`\',

-   .ui files are stored in \'`Gui/Resources/ui/`\' commands.

One package doesn\'t follow this pattern: `femsolver`. It has its place on the same level as `femobjects` and `femguiobjects` (`src/Mod/Fem/femsolver`). The package contains solver and equation related packages and modules and it is organized the following way:

    .femsolver
    .femsolver.elmer
    .femsolver.elmer.equations
    .femsolver.calculix
    .femsolver.calculix.equations
    .femsolver.z88
    .femsolver.z88.equations

## Solver

In FreeCAD a solver can be split into two parts:

-   One is the document object used by the user to interact with the solver. Though it solver parameter can be set and it is also used to control the solving process.
-   The other one are the so called tasks of a solver. The solving process is split into those tasks, namely: *check, prepare, solve and results*. Those do the actual work of exporting the analysis into a format understood by the solver executable, starting the executable and loading the results back into FreeCAD.

Most files related to a solver reside in a sub-package of the `femsolver` package (e.g. for Elmer its in `femsolver/elmer`). The following list enumerates all files related to the implementation of a solver. Those are the files that need to be copied and modified to add support for a new solver to FreeCAD. The given example is taken from the solver implementation of Elmer.

-   **femsolver/elmer/solver.py:** Document object visible in the tree-view. Implemented in python via a document proxy and view proxy.
-   **femsolver/elmer/tasks.py:** Module containing one task class per task required for a solver implementation. Those tasks divide the process of solving a analysis into the following steps: check, prepare, solve, results.
-   **femcommands/commands.py:** Adds the solver document object to the active document. Required to access the solver object from the GUI.

There is a tutorial of adding a new solver: [Add FEM solver tutorial](Add_FEM_solver_tutorial.md)

## Equations

An equation represents a particular physics that shall be considered when solving the analysis (e.g. Flow, Heat). Not all solver in FreeCAD support (all) equations. Equations are represented by child objects of the corresponding solver object. In the tree-view this looks like this:

-   elmer-solver
    -   elasticity
    -   heat
    -   flow
    -   electrostatics

Most solver specific options (e.g. max. iterations, method of solving, etc) are set via the equation objects. One consequence of this is that each solver must have it\'s own implementation of \"the same\" equation. CalculiX would have a different Heat-object that Elmer. To avoid having multiple buttons for the same physics in the GUI each solver object adds it\'s equations itself.

The actual implementation can be split into the generic and the solver specific part. The generic part can be found in the `femsolver.equationbase` module. The solver specific part resides inside individual Equations sub-packages of the solver packages (e.g. `femsolver/elmer/equations`).

Adding a new equations to Elmer should be very easy. For newcomers there exists a tutorial which shows how to add a new equation to Elmer by adding the existing elasticity solver to FreeCAD: [Add FEM equation tutorial](Add_FEM_equation_tutorial.md).

## Restricciones

Las restricciones definen condiciones de contorno para el problema que se resolverá. En FreeCAD, las restricciones no son específicas de un solucionador en particular. Un solucionador de problemas puede ser resuelto por todos los solucionadores que soportan todas las condiciones en el análisis.


<div class="mw-translate-fuzzy">

Agregar nuevas restricciones es bastante sencillo. Para los recién llegados hay un tutorial:[Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md).


</div>

_

---
[documentation index](../README.md) > [FEM](Category_FEM.md) > Extend FEM Module/es
