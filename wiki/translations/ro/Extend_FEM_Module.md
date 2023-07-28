---
- TutorialInfo:/ro
   Topic: 
   Level: 
   Time: 
   Author:[M42kus](User_M42kus.md)
   FCVersion:
   Files:
---

# Extend FEM Module/ro




<div class="mw-translate-fuzzy">




</div>


<div class="mw-translate-fuzzy">

Atelierul FEM deja suportă o mulțime de constrângeri diferite și un buchet de rezolvitori. Despite that people often need constraints not jet supported by FreeCAD. This page is the starting point to a series of tutorials and other resources describing how to extend the FEM workbench using the existing framework. While this series can prove helpful to software developers too the idea is to allow FEM users with a bit of interrest into python coding to add the stuff they need themselfs.


</div>

Adăugarea de noi constrângeri, ecuatții sau rezolvitori este în cea mai mare parte o activitate de rutină. Dar a face acest lucru pentru prima dată nu va părea ușor. An understanding of the following topics will prove helpful:


<div class="mw-translate-fuzzy">

-   Python scripting in FreeCAD.
    -   [FreeCAD Scripting Tutorial](Python_scripting_tutorial.md)
    -   [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)
-   Extending FreeCAD with Python.
    -   [Scripted Objects](Scripted_objects.md)
-   A solid understanding of the solver for which new objects shall be added (e.g. calculix) is important.
-   A little knowledge about build systems, especially cmake (build system used by FreeCAD)


</div>

## Build System (cmake) 


<div class="mw-translate-fuzzy">

The build system must be modified regardless of which objects shall be added o the FEM workbench. Every python module (file) must be registerd. The FEM workbench even requries every new python module to be registerd twice. Once in Mod/Fem/CMakeLists.txt and a secound time in Mod/Fem/App/CMakeLists.txt. This is true regaredless of the type of the python module (gui or non-gui). Where exactely the module must be inserted depends on the role of the module. Solver, equations and constraints all use different lists. Searching for similar files and inserting the new file in the same list works most of the time.


</div>


<div class="mw-translate-fuzzy">

As an example lets add a new constraint pressure. A new constraint requires at least the following new modules: FemConstraint.py, ViewProviderFemConstraint.py, CommandFemConstraint.py. These three files must be added to CMakeLists.txt as well as App/CMakeLists.txt.


</div>


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


<div class="mw-translate-fuzzy">

For organizing the python code the FEM module uses a similar abbroach to that used for the C++ code thoughout FreeCAD. The module is split into two packages. PyObjects, which contains all non-gui like python proxies for document objects and PyGui containing everything gui related like python proxies for view provider, task panels, ui files and commands.


</div>


<div class="mw-translate-fuzzy">

One package doesn\'t follow this pattern: FemSolver. It has its place on the same level as PyObjects and PyGui (src/Mod/Fem/FemSolver). The package contains solver and equation related packages and modules and it is organized the following way:


</div>

    .femsolver
    .femsolver.elmer
    .femsolver.elmer.equations
    .femsolver.calculix
    .femsolver.calculix.equations
    .femsolver.z88
    .femsolver.z88.equations



## Rezolvitor


<div class="mw-translate-fuzzy">

In FreeCAD a solver can be split into two parts. One is the document object used by the user to interact with the solver. Though it solver parameter can be set and it is also used to control the solving process. The other one are the so called tasks of a solver. The solving process is split into those tasks, namely: check, prepare, solve and results. Those do the actual work of exporting the analysis into a format understood by the solver executable, starting the executable and loading the results back into FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Most files related to a solver reside in a sub-package of the FemSolver package (e.g. FemSolver.Elmer). The following list enumerates all files related to the implementation of a solver. Those are the files that need to be copied and modified to add support for a new solver to FreeCAD.


</div>


<div class="mw-translate-fuzzy">

-   **FemSolver/Elmer/Object.py:** Document object visible in the tree-view. Implemented in python via a document proxy and view proxy.
-   **FemSolver/Elmer/Tasks.py:** Module containing one task class per task required for a solver implementation. Those tasks divide the process of solving a analysis into the following steps: check, prepare, solve, results.
-   **PyGui/\_CommandFemElmer.py:** Adds the solver document object to the active document. Required to access the solver object from the GUI.


</div>



## Ecuații


<div class="mw-translate-fuzzy">

An equation represets a particular physics that shall be considered when solving the analysis (e.g. Flow, Heat). Not all solver in FreeCAD support equations. Equations are represented by child objects of the corresponding solver object. In the tree-view this looks like this:


</div>


<div class="mw-translate-fuzzy">

-   ElmerSolver
    -   Elasticity
    -   Heat
    -   Flow


</div>


<div class="mw-translate-fuzzy">

Most solver specific options (max iterations, method of solving, etc) are set via the equation objects. One consequence of this is that each solver must have it\'s own implementation of \"the same\" equation. Calculix would have a different Heat object that Elmer. To avoid having multiple buttons for the same physics in the GUI each solver object adds it\'s equations itself.


</div>


<div class="mw-translate-fuzzy">

The actual implementation can be split into the generic and the solver specific part. The generic part can be found in the FemSolver.EquationBase module. The solver specific part resides inside individual Equations sub-packages of the solver packages (e.g. FemSolver/Elmer/Equations).


</div>


<div class="mw-translate-fuzzy">

Adding a new equations to elmer should be very easy. For newcomers there exists a tutorial which shows how to add a new equation to elmer by adding the existing elasticity solver to FreeCAD: [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md).


</div>



## Constrângeri

Constrângerile definesc condițiile limită pentru problema care trebuie rezolvată. În FreeCAD constrângerile nu sunt specifice unui anumit rezolvitor. O problemă definită poate fi rezolvată de toțși rezolvitorii care suportă toate condițiile analizei.


<div class="mw-translate-fuzzy">

Adăugarea de noi constrângeri este destul de simplă. Pentru nou-veniți, există un tutorial: [Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md).


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > Extend FEM Module/ro
