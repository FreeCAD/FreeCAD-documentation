# <img alt="FEM workbench icon" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/ro


{{TOCright}}



## Introducere


<div class="mw-translate-fuzzy">

[FEM Workbench](FEM_Workbench.md)  oferă un flux modern de analiză prin metoda elementelor finite (MEF) pentru FreeCAD. În principal, acest lucru înseamnă că toate instrumentele pentru a face o analiză prin Metoda Elementului Finit sunt combinate într-o singură interfață grafică(GUI).


</div>

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">



## Plan de lucru 


<div class="mw-translate-fuzzy">

Pașii pentru a face AEF în Atelierul AEF din FreeCAD GUI sunt:

-   Preprocesare, setting up the analysis problem.
    -   Modelarea geometriei, în care FreeCAD este deja un software aproape dezvoltat: creating the geometry with FreeCAD, or importing it from a different application.
    -   Creați o analiză:
        -   Creați o Plasă AEF din modelul geometric.
        -   Adăugați la modelul de analiză constrângeri, cum ar fi sarcini și corecții de asistență.
        -   Adăugați un material la modelul de analiză
-   Rezolvarea: Rezolvați sistemul de ecuații din cadrul GUI-ului FreeCAD.
-   Postprocesare: Vezi rezultatele din FreeCAD GUI.


</div>

Începând cu versiunea 0.15 a FreeCAD, Atelierul AEF poate fi folosit pe platforme Windows, Mac OSX și Linux. Deoarece Atelierul AEF folosește software extern, cantitatea de intervenție manuală până când Atelierul AEF este gata de utilizare va depinde de sistemul de operare pe care îl utilizați. Verificați [ FEM Install](FEM_Install.md) page for instructions on setting up the external tools.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



*Workflow of the FEM Workbench; the workbench calls two external programs to perform meshing of a solid object, and perform the actual solution of the finite element problem*



## Meniu: Model 

-   <img alt="" src=images/Fem-analysis.svg  style="width:32px;"> [Analysis container](FEM_Analysis/ro.md): Creează un nou container pentru analiza mecanică. Dacă un solid este selectat în vederea arborescentă înainte de a face click pe el dialogul plasei de discretizare va fi deschis alături



### Materiale

-   <img alt="" src=images/Fem-material.svg  style="width:32px;"> [FEM material for solid](FEM_MaterialSolid/ro.md): Vă permite să selectați un material din baza de date.

-   <img alt="" src=images/Fem-material-fluid.svg  style="width:32px;"> [Material for fluid](FEM_MaterialFluid.md): Lets you select a material from the database.

-   <img alt="" src=images/Fem-material-nonlinear.svg  style="width:32px;"> [Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear/ro.md): Vă permite să selectați un material din baza de date..

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Reinforced material (concrete)](FEM_MaterialReinforced.md): Lets you select reinforced materials consisting of a matrix and a reinforcement from the database.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Material editor](FEM_MaterialEditor.md):: Lets you open the material editor to edit materials


</div>

### Element Geometry 

-   <img alt="" src=images/Fem-beam-section.svg  style="width:32px;"> [Beam cross section](FEM_ElementGeometry1D.md):

-   <img alt="" src=images/Fem-beam-rotation.svg  style="width:32px;"> [Beam rotation](FEM_ElementRotation1D.md):

-   <img alt="" src=images/Fem-shell-thickness.svg  style="width:32px;"> [Shell plate thickness](FEM_ElementGeometry2D.md):


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-fluid-section.svg  style="width:32px;"> [Fluid section for 1D flow](FEM_ElementFluid1D.md):


</div>



### Constrângeri Electrostatice 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/fem-constraint-electrostatic-potential.svg  style="width:32px;"> [Constraint electrostatic potential](FEM_ConstraintElectrostaticPotential.md):


</div>



### Fluid constraints 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-constraint-initial-flow-velocity.svg  style="width:32px;"> [Constraint initial flow velocity](FEM_ConstraintInitialFlowVelocity.md):


</div>

-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Constraint initial pressure](FEM_ConstraintInitialPressure.md): Used to define an initial pressure for a body (volume). <small>(v1.0)</small> 

-   <img alt="" src=images/Fem-constraint-flow-velocity.svg  style="width:32px;"> [Constraint flow velocity](FEM_ConstraintFlowVelocity.md):

### Geometrical Constraints 

-   <img alt="" src=images/Fem-constraint-planerotation.svg  style="width:32px;"> [Constraint plane rotation](FEM_ConstraintPlaneRotation/ro.md): Vă permite să definiți o constrângere de rotație a planului pe o fațetă plană

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Constraint section print](FEM_ConstraintSectionPrint.md): Used to print the predefined facial output variables (forces and moments) to the dat file. <small>(v0.19)</small> 

-   <img alt="" src=images/Fem-constraint-transform.svg  style="width:32px;"> [Constraint transform](FEM_ConstraintTransform.md):



### Constrângeri Mecanice 

-   <img alt="" src=images/Fem-constraint-fixed.svg  style="width:32px;"> [Constraint fixed](FEM_ConstraintFixed/ro.md):Se utilizează pentru a defini o constrângere fixă pe punct/margine/fațetă (e)..

-   <img alt="" src=images/Fem-constraint-displacement.svg  style="width:32px;"> [Constraint displacement](FEM_ConstraintDisplacement.md): Used to define a displacement constraint on point/edge/face(s).

-   <img alt="" src=images/Fem-constraint-contact.svg  style="width:32px;"> [Constraint contact](FEM_ConstraintContact/ro.md): Utilizat pentru a defini contactul de constrângere între două fațete.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Constraint tie](FEM_ConstraintTie.md): Used to define a tie constraint (\"bonded contact\") between two faces. <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Constraint spring](FEM_ConstraintSpring.md): Used to define a spring. <small>(v0.20)</small> 

-   <img alt="" src=images/Fem-constraint-force.svg  style="width:32px;"> [Constraint force](FEM_ConstraintForce/ro.md): Utilizat pentru a defini o forță exprimată în \[N\] aplicată unifrom pe fațetă selectată într-o direcție definibilă.

-   <img alt="" src=images/Fem-constraint-pressure.svg  style="width:32px;"> [Constraint pressure](FEM_ConstraintPressure/ro.md): Utilizat pentru a defini constrângere de presiune.

-   <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Constraint centrif](FEM_ConstraintCentrif.md): Used to define a centrifugal body load constraint. <small>(v0.20)</small> 

-   <img alt="" src=images/Fem-constraint-selfweight.svg  style="width:32px;"> [Constraint self weight](FEM_ConstraintSelfWeight/ro.md): Utilizat pentru a defini accelerația gravitațională care acționează asupra modelului.



### Constrângeri termice 

-   <img alt="" src=images/Fem-constraint-InitialTemperature.svg  style="width:32px;"> [Constraint initial temperature](FEM_ConstraintInitialTemperature/ro.md): Utilizat pentru a defini temperatura inițială a corpului.

-   <img alt="" src=images/Fem-constraint-heatflux.svg  style="width:32px;"> [Constraint heatflux](FEM_ConstraintHeatflux/ro.md): Utilizat pentru a defini fluxul de căldură constrâns pe o fațetă(e).

-   <img alt="" src=images/Fem-constraint-temperature.svg  style="width:32px;"> [Constraint temperature](FEM_ConstraintTemperature/ro.md): Utilizat pentru a defini constrângerea de temperatură pe un punct/muchie/fațetă(e).

-   <img alt="" src=images/Fem-constraint-heatflux.svg  style="width:32px;"> [Constraint body heat source](FEM_ConstraintBodyHeatSource/ro.md):

### Constraints without solver 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-constraint-fluid-boundary.svg  style="width:32px;"> [Constraint fluid boundary](FEM_ConstraintFluidBoundary.md):


</div>

-   <img alt="" src=images/Fem-constraint-bearing.svg  style="width:32px;"> [Constraint bearing](FEM_ConstraintBearing/ro.md): Utilizat pentru a defini o constrângere de rulment.

-   <img alt="" src=images/Fem-constraint-gear.svg  style="width:32px;"> [Constraint gear](FEM_ConstraintGear/ro.md): Utilizat pentru a defini o constrângere de angrenaj de roți dințate.

-   <img alt="" src=images/Fem-constraint-pulley.svg  style="width:32px;"> [Constraint pulley](FEM_ConstraintPulley/ro.md): Utilizat pentru a defini o constrângere de tip fulie.

### Overwrite Constants 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity.md): Used to overwrite the [permittivity of vacuum](https://en.wikipedia.org/wiki/Vacuum_permittivity) with a custom value. <small>(v0.19)</small> 



## Meniu plase/Mesh 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-femmesh-netgen-from-shape.svg  style="width:32px;"> [FEM mesh from shape by Netgen](FEM_MeshNetgenFromShape.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-femmesh-gmsh-from-shape.svg  style="width:32px;"> [FEM mesh from shape by GMSH](FEM_MeshGmshFromShape.md):


</div>

-   <img alt="" src=images/Fem-femmesh-boundary-layer.svg  style="width:32px;"> [FEM mesh boundary layer](FEM_MeshBoundaryLayer.md):

-   <img alt="" src=images/Fem-femmesh-region.svg  style="width:32px;"> [FEM mesh region](FEM_MeshRegion.md):

-   <img alt="" src=images/Fem-femmesh-from-shape.svg  style="width:32px;"> [FEM mesh group](FEM_MeshGroup.md):

-   <img alt="" src=images/Fem-femmesh-create-node-by-poly.svg  style="width:32px;"> [Nodes set](FEM_CreateNodesSet.md): Creates/defines a node set from FEM mesh.

-   <img alt="" src=images/Fem-femmesh-to-mesh.svg  style="width:32px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh.md): Convert the surface of a FEM mesh to a mesh.



## Meniu Rezolvitori 

-   <img alt="" src=images/Fem-solver.svg  style="width:32px;"> [Solver Calculix CCX tools](FEM_SolverCalculixCxxtools/ro.md): Creează un nou rezolvitor pentru această analiză. În cele mai multe cazuri rezolvitorul este creat împreună cu analiza.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-solver.svg  style="width:32px;"> [Solver CalculiX](FEM_SolverCalculiX.md):


</div>

-   <img alt="" src=images/Fem-elmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md):

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran.md): <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-solver.svg  style="width:32px;"> [Solver Z88](FEM_SolverZ88.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-equation-elasticity.svg  style="width:32px;"> [Equation elasticity](FEM_EquationElasticity.md):


</div>

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Electricforce equation](FEM_EquationElectricforce.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate the electric force on surfaces. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-equation-electrostatic.svg  style="width:32px;"> [Equation electrostatic](FEM_EquationElectrostatic.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-equation-flow.svg  style="width:32px;"> [Equation flow](FEM_EquationFlow.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Equation fluxsolver](FEM_EquationFlux.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-equation-heat.svg  style="width:32px;"> [Equation heat](FEM_EquationHeat.md):


</div>

-   <img alt="" src=images/Fem-control-solver.svg  style="width:32px;"> [Solver job control](FEM_SolverControl/ro.md): Deschide meniul pentru a ajusta și porni rezolvitorul selectat.

-   <img alt="" src=images/Fem-run-solver.svg  style="width:32px;"> [Solver run calculation](FEM_SolverRun/ro.md): Rulează rezolvitorul selectat al analizei active.



## Meniu Rezultate 

-   <img alt="" src=images/Fem-purge-results.svg  style="width:32px;"> [Results purge](FEM_ResultsPurge/ro.md): Șterge rezultatul analizei active.

-   <img alt="" src=images/Fem-result.svg  style="width:24px;"> [Result show](FEM_ResultShow/ro.md): Utilizează afișarea rezultatelor analizei


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostApplyChanges.png  style="width:32px;"> [Post Apply changes](FEM_PostApplyChanges.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-data.svg  style="width:32px;"> [Post Pipeline from result](FEM_PostPipelineFromResult.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Warp filter](FEM_PostFilterWarp/ro.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalar clip filter](FEM_PostFilterClipScalar/ro.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Function cut filter](FEM_PostFilterCutFunction/ro.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Region clip filter](FEM_PostFilterClipRegion/ro.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Line clip filter](FEM_PostFilterDataAlongLine/ro.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Stress linearization plot](FEM_PostFilterLinearizedStresses/ro.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Data at point clip filter](FEM_PostFilterDataAtPoint/ro.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;"> [Post Create functions](FEM_PostCreateFunctions.md):


</div>

  - <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;"> [Filter function plane](FEM_PostCreateFunctionPlane.md): Defines that the result mesh is cut with a plane.

  - <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;"> [Filter function sphere](FEM_PostCreateFunctionSphere.md): Defines that the result mesh is cut with a sphere.



## Meniu: Utilități 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/fem-clipping-plane-add.svg  style="width:32px;"> [Clipping plane on face](FEM_ClippingPlaneAdd.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/fem-clipping-plane-remove-all.svg  style="width:32px;"> [Remove all clipping planes](FEM_ClippingPlaneRemoveAll.md):


</div>

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Open FEM examples](FEM_Examples.md): Open the GUI to access FEM examples.



## Meniu de Context 

-   <img alt="" src=images/Fem-femmesh-clear-mesh.svg  style="width:32px;"> [FEM mesh clear](FEM_MeshClear.md):

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Display FEM mesh info](FEM_MeshDisplayInfo/ro.md): Displays basic statistics of existing mesh - number of nodes and elements of each type.



## Preferințe

!!FUZZY!!\* <img alt="" src=images/Std_DlgParameter.svg  style="width:32px;"> [Preferences\...](FEM_Preferences.md): Preferințe disponibile în Instrumentele MEF.



## Links

[FEM Install](FEM_Install.md) pentru o detaliată descriere a modului cum lucrează Modului MEF.

The following pages explain different topics of the FEM Workbench.

[FEM Install](FEM_Install.md): a detailed description on how to set up the external programs used in the workbench.

[FEM Mesh](FEM_Mesh.md) pentru informații suplimentere privind AEF asupra Plaselor în Modulul MEF din FreeCAD

[ FEM Solver](FEM_Solver.md) for further Informations about FEM Solvers in FEM Module,

[FEM CalculiX](FEM_CalculiX.md) Pentru informații suplimentare despre Calculix, cel mai folosit ți bine dezvoltat rezolvitor în Modulul MEF

[FEM Concrete](FEM_Concrete.md) for informations about analysis\'s of concrete structures.

## Tutorials


<div class="mw-translate-fuzzy">

## Tutoriale

Tutorial 1 [ FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D.md)


</div>

Tutorial 2 [ FEM Tutorial](FEM_tutorial.md)

Tutorial 3 [ FEM Tutorial Python](FEM_Tutorial_Python.md)

Tutorial 4 [FEM Shear of a Composite Block](FEM_Shear_of_a_Composite_Block.md)

Tutorial 5: [Transient FEM analysis](Transient_FEM_analysis.md)

Tutorial 6: [Post-Processing of FEM Results with Paraview](Post-Processing_of_FEM_Results_with_Paraview.md)

Tutorial 7: [FEM Example Capacitance Two Balls](FEM_Example_Capacitance_Two_Balls.md); Elmer\'s GUI tutorial 6 \"Electrostatics Capacitance Two Balls\" using FEM Examples.

Cuprins tutoriale de analiză termică la piese mecanice [PDF\'s](https://opensimsa.github.io/training.html)

Video Tutorial 1 [Forum post with you tube link](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353)

Video Tutorial 2 [Forum post with you tube link](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321)

Further video Tutorials [Forum post with you tube link](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162640)

## Extending the FEM Workbench 

The FEM Workbench is under constant development. An objective of the project is to find ways to easily interact with various FEM solvers, so that the end user can streamline the process of creating, meshing, simulating, and optimizing an engineering design problem, all within FreeCAD.

The following information is aimed at power users and developers who want to extend the FEM Workbench in different ways. Familiarity with C++ and Python is expected, and also some knowledge of the \"document object\" system used in FreeCAD is necessary; this information is available in the [Power users hub](Power_users_hub.md) and the [Developer hub](Developer_hub.md). Please notice that since FreeCAD is under active development, some articles may be too old, and thus obsolete. The most up to date information is discussed in the [FreeCAD forums](https://forum.freecadweb.org/index.php), in the Development section. For FEM discussions, advice or assistance in extending the workbench, the reader should refer to the [FEM subforum](https://forum.freecadweb.org/viewforum.php?f=18).


<div class="mw-translate-fuzzy">

-   [Extend FEM Module](Extend_FEM_Module.md)
    -   [Add FEM Equation Tutorial](Add_FEM_Equation_Tutorial.md)
    -   [Add FEM Constraint Tutorial](Add_FEM_Constraint_Tutorial.md)


</div>

A developer\'s guide has been written to help power users in understanding the complex FreeCAD codebase and the interactions between the core elements and the individual workbenches. The book is hosted at github so multiple users can contribute to it and keep it updated.

-   [Early preview of ebook: Module developer\' guide to FreeCAD source](https://forum.freecadweb.org/viewtopic.php?t=17581) forum thread.
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) github repository.

## Extending the FEM Workbench documentation 

-   More information regarding extending or missing FEM documentation can be found in the forum: [FEM documentation missing on the Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/ro
