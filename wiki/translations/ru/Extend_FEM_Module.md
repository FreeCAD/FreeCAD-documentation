---
- TutorialInfo   */ru
   Topic   * 
   Level   * 
   Time   * 
   Author   *[M42kus](User_M42kus.md)
   FCVersion   *
   Files   *
---

# Extend FEM Module/ru




<div class="mw-translate-fuzzy">




</div>


<div class="mw-translate-fuzzy">

Bерстак FEM(МКЭ) уже поддерживает множество различных ограничений и несколько решателей. Несмотря на это, людям часто нужны ограничения, а не поддержка JetCAD. Эта страница является отправной точкой для серии учебных пособий и других ресурсов, описывающих, как расширить рабочую среду FEM с использованием существующей инфраструктуры. Хотя эта серия может оказаться полезной и для разработчиков программного обеспечения, идея состоит в том, чтобы позволить пользователям FEM, немного интересующимся программированием на Python, самостоятельно добавлять то, что им нужно.


</div>

Добавление новых ограничений, уравнений или решателя - это в основном рутинная работа. Но сделать это в первый раз будет не так просто, как может показаться. Понимание следующих тем окажется полезным   *

-   Python scripting in FreeCAD.
    -   [FreeCAD Scripting Tutorial](Python_scripting_tutorial.md)
    -   [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)
-   Extending FreeCAD with Python.
    -   [Scripted Objects](Scripted_objects.md)
-   A solid understanding of the solver for which new objects shall be added (e.g. CalculiX or Elmer) is important.
-   A little knowledge about build systems, especially cmake (build system used by FreeCAD).

## Build System (cmake) 

The build system must be modified regardless of which objects shall be added o the FEM workbench. Every python module (file) must be registered. The FEM workbench requires every new python module to be registered in `Mod/Fem/CMakeLists.txt`. This is true regardless of the type of the python module (GUI or non-GUI). Where exactly the module must be inserted depends on the role of the module. Solver, equations and constraints all use different lists. Searching for similar files and inserting the new file in the same list works most of the time.

As an **example** lets add a new constraint called  for this constraint. A new constraint requires at least the following new modules   *

-    `constraint_<name>.py`
    

-    `view_constraint_<name>.py`
    

-    `CommandFemConstraint<name>.py`(may be unnecessary)

These three files must be added to `Mod/Fem/CMakeLists.txt` as well as `Mod/Fem/App/CMakeLists.txt`. All inserted lines of code are indicated by a starting **+**.


**Mod/Fem/CMakeLists.txt**


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

For organizing the python code the FEM module uses the following approach. The module is split into the following packages   *

-    `femobjects`, which contains all non-GUI like python proxies for document objects and

-    `femviewproviders`containing everything GUI related like python proxies for view provider

-   C++ based task panels are stored in \'`Gui`\',

-   icons can be found in \'`Gui/Resources/icons/`\',

-   .ui files are stored in \'`Gui/Resources/ui/`\' commands.

One package doesn\'t follow this pattern   * `femsolver`. It has its place on the same level as `femobjects` and `femguiobjects` (`src/Mod/Fem/femsolver`). The package contains solver and equation related packages and modules and it is organized the following way   *

    .femsolver
    .femsolver.elmer
    .femsolver.elmer.equations
    .femsolver.calculix
    .femsolver.calculix.equations
    .femsolver.z88
    .femsolver.z88.equations

## Solver

In FreeCAD a solver can be split into two parts   *

-   One is the document object used by the user to interact with the solver. Though it solver parameter can be set and it is also used to control the solving process.
-   The other one are the so called tasks of a solver. The solving process is split into those tasks, namely   * *check, prepare, solve and results*. Those do the actual work of exporting the analysis into a format understood by the solver executable, starting the executable and loading the results back into FreeCAD.

Most files related to a solver reside in a sub-package of the `femsolver` package (e.g. for Elmer its in `femsolver/elmer`). The following list enumerates all files related to the implementation of a solver. Those are the files that need to be copied and modified to add support for a new solver to FreeCAD. The given example is taken from the solver implementation of Elmer.

-   **femsolver/elmer/solver.py   *** Document object visible in the tree-view. Implemented in python via a document proxy and view proxy.
-   **femsolver/elmer/tasks.py   *** Module containing one task class per task required for a solver implementation. Those tasks divide the process of solving a analysis into the following steps   * check, prepare, solve, results.
-   **femcommands/commands.py   *** Adds the solver document object to the active document. Required to access the solver object from the GUI.

There is a tutorial of adding a new solver   * [Add FEM Solver Tutorial](Sandbox_Add_FEM_Solver_Tutorial.md)

## Equations

An equation represents a particular physics that shall be considered when solving the analysis (e.g. Flow, Heat). Not all solver in FreeCAD support (all) equations. Equations are represented by child objects of the corresponding solver object. In the tree-view this looks like this   *

-   elmer-solver
    -   elasticity
    -   heat
    -   flow
    -   electrostatics

Most solver specific options (e.g. max. iterations, method of solving, etc) are set via the equation objects. One consequence of this is that each solver must have it\'s own implementation of \"the same\" equation. CalculiX would have a different Heat-object that Elmer. To avoid having multiple buttons for the same physics in the GUI each solver object adds it\'s equations itself.

The actual implementation can be split into the generic and the solver specific part. The generic part can be found in the `femsolver.equationbase` module. The solver specific part resides inside individual Equations sub-packages of the solver packages (e.g. `femsolver/elmer/equations`).

Adding a new equations to Elmer should be very easy. For newcomers there exists a tutorial which shows how to add a new equation to Elmer by adding the existing elasticity solver to FreeCAD   * [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md).

## Constraints

Constraints define boundary conditions for the problem that shall be solved. In FreeCAD constraints aren\'t specific to a particular solver. A problem setup can be solved by all solver that support all conditions in the analysis.

Adding new constraints is quite straight forward. For newcomers there is a tutorial   * [Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md).

[Category   *FEM](Category_FEM.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > Extend FEM Module/ru
