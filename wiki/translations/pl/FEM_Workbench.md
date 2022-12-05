# <img alt="Ikonka FreeCAD dla środowiska pracy MES" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy **MES** zapewnia nowoczesną [analizę metodą elementów skończonych](https://en.wikipedia.org/wiki/Finite_element_analysis) *(FEA)* dla FreeCAD. Głównie oznacza to, że wszystkie narzędzia do wykonania analizy są połączone w jeden graficzny interfejs użytkownika *(GUI)*.

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Przepływ pracy 

Kroki przeprowadzania analizy metodą elementów skończonych:

1.  Preprocessing: ustawienie zagadnienia analizy.
    1.  Modelowanie geometrii: tworzenie geometrii za pomocą programu FreeCAD lub importowanie jej z innej aplikacji.
    2.  Tworzenie analizy.
        1.  Dodawanie do modelu geometrycznego uwarunkowań symulacyjnych, takich jak obciążenia i podpory stałe.
        2.  Dodawanie materiałów do części poza modelem geometrycznym.
        3.  Tworzenie siatki elementów skończonych dla modelu geometrycznego lub importowanie jej z innej aplikacji.
2.  Rozwiązywanie: uruchamianie zewnętrznego solwera z poziomu FreeCAD.
3.  Postprocessing: wizualizacja wyników analizy z poziomu FreeCAD lub eksportowanie wyników, aby można je było przetworzyć w innej aplikacji.

Środowisko pracy MES może być używane w systemach Linux, Windows i Mac OSX. Ponieważ korzysta z zewnętrznych solverów, zakres ręcznej konfiguracji zależy od systemu operacyjnego, z którego korzystasz. Instrukcje dotyczące konfiguracji zewnętrznych narzędzi znajdują się na stronie [Instalacja środowiska MES](FEM_Install/pl.md).

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



*Przepływ pracy w środowisku MES. Środowisko to wywołuje dwa zewnętrzne środowiska w celu wykonania siatkowania obiektu bryłowego oraz rozwiązania problemu metodą elementów skończonych.*

## Menu: Model 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Analysis container](FEM_Analysis.md): Creates a new container for a mechanical analysis. If a solid is selected in the tree view before clicking on it, the meshing dialog will be opened next.

### Materiał

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Material for solid](FEM_MaterialSolid.md): Lets you select a solid material from the database.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Material for fluid](FEM_MaterialFluid.md): Lets you select a fluid material from the database.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear.md): Lets you add a nonlinear mechanical material model.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Reinforced material (concrete)](FEM_MaterialReinforced.md): Lets you select reinforced materials consisting of a matrix and a reinforcement from the database.

-   <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Material editor](FEM_MaterialEditor.md): Lets you open the material editor to edit materials.

### Geometria elementu 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Beam cross section](FEM_ElementGeometry1D.md): Used to define cross sections for beam elements.

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Beam rotation](FEM_ElementRotation1D.md): Used to rotate cross sections of beam elements.

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Shell plate thickness](FEM_ElementGeometry2D.md): Used to define shell element thickness.

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Fluid section for 1D flow](FEM_ElementFluid1D.md): Used to create fluid section element for pneumatic and hydraulic networks.

### Electrostatic Constraints 

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Constraint electrostatic potential](FEM_ConstraintElectrostaticPotential.md): Used to define electrostatic potential.

### Fluid Constraints 

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Constraint initial flow velocity](FEM_ConstraintInitialFlowVelocity.md): Used to define an initial flow velocity for the body.

-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Constraint initial pressure](FEM_ConstraintInitialPressure.md): Used to define an initial pressure for the body. <small>(v1.0)</small> 

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Constraint flow velocity](FEM_ConstraintFlowVelocity.md): Used to define a flow velocity as a boundary condition at an edge (2D) or face (3D).

### Geometrical Constraints 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Constraint plane rotation](FEM_ConstraintPlaneRotation.md): Used to define a plane rotation constraint on a planar face.

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Constraint section print](FEM_ConstraintSectionPrint.md): Used to print the predefined facial output variables (forces and moments) to the dat file. <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Constraint transform](FEM_ConstraintTransform.md): Used to define a transform constraint on a face.

### Mechanical Constraints 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Constraint fixed](FEM_ConstraintFixed.md): Used to define a fixed constraint on point/edge/face(s).

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Constraint displacement](FEM_ConstraintDisplacement.md): Used to define a displacement constraint on point/edge/face(s).

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Constraint contact](FEM_ConstraintContact.md): Used to define a contact constraint between two faces.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Constraint tie](FEM_ConstraintTie.md): Used to define a tie constraint (\"bonded contact\") between two faces. <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Constraint spring](FEM_ConstraintSpring.md): Used to define a spring. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Constraint force](FEM_ConstraintForce.md): Used to define a force in \[N\] applied uniformly to a selectable face in a definable direction.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Constraint pressure](FEM_ConstraintPressure.md): Used to define a pressure constraint.

-   <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Constraint centrif](FEM_ConstraintCentrif.md): Used to define a centrifugal body load constraint. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Constraint self weight](FEM_ConstraintSelfWeight.md): Used to define a gravity acceleration acting on a model.

### Thermal Constraints 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Constraint initial temperature](FEM_ConstraintInitialTemperature.md): Used to define the initial temperature of a body.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Constraint heatflux](FEM_ConstraintHeatflux.md): Used to define a heat flux constraint on a face(s).

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Constraint temperature](FEM_ConstraintTemperature.md): Used to define a temperature constraint on a point/edge/face(s).

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Constraint body heat source](FEM_ConstraintBodyHeatSource.md): Used to define an internally generated body heat.

### Constraints without solver 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Fluid boundary condition](FEM_ConstraintFluidBoundary.md): Used to define a fluid boundary condition.

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Constraint bearing](FEM_ConstraintBearing.md): Used to define a bearing constraint.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Constraint gear](FEM_ConstraintGear.md): Used to define a gear constraint.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Constraint pulley](FEM_ConstraintPulley.md): Used to define a pulley constraint.

### Overwrite Constants 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity.md): Used to overwrite the [permittivity of vacuum](https://en.wikipedia.org/wiki/Vacuum_permittivity) with a custom value. <small>(v0.19)</small> 

## Menu: Siatka 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [FEM mesh from shape by Netgen](FEM_MeshNetgenFromShape.md): Generates a finite element mesh for a model using Netgen.

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md): Generates a finite element mesh for a model using Gmsh.

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [FEM mesh boundary layer](FEM_MeshBoundaryLayer.md): Creates anisotropic meshes for accurate calculations near boundaries.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [FEM mesh region](FEM_MeshRegion.md): Creates a localized area(s) to mesh which highly optimizes analysis time.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [FEM mesh group](FEM_MeshGroup.md): Groups and labels elements of a mesh (vertex, edge, surface) together, useful for exporting the mesh to external solvers.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Nodes set](FEM_CreateNodesSet.md): Creates/defines a node set from FEM mesh.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh.md): Convert the surface of a FEM mesh to a mesh.

## Menu: Rozwiąż 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md): Creates a new solver for this analysis. In most cases the solver is created together with the analysis.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solver CalculiX (new framework)](FEM_SolverCalculiX.md):

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md): Creates the solver controller for Elmer. It is independent from other solver objects.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran.md): <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solver Z88](FEM_SolverZ88.md): Creates the solver controller for Z88. It is independent from other solver objects.

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elasticity equation](FEM_EquationElasticity.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform mechanical analyses.

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Electricforce equation](FEM_EquationElectricforce.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate the electric force on surfaces. <small>(v0.19)</small> 

-   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Electrostatic equation](FEM_EquationElectrostatic.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform electrostatic analyses.

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Flow equation](FEM_EquationFlow.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform flow analyses.

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Flux equation](FEM_EquationFlux.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform flux analyses.

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Heat equation](FEM_EquationHeat.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform heat transfer analyses.

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Solver job control](FEM_SolverControl.md): Opens the menu to adjust and start the selected solver.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Run solver calculations](FEM_SolverRun.md): Runs the selected solver of the active analysis.

## Menu: Wyniki 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Purge results](FEM_ResultsPurge.md): Deletes the results of the active analysis.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow.md): Used to display the result of an analysis.

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Apply changes to pipeline](FEM_PostApplyChanges.md): Toggles if changes to pipelines and filters are applied immediately.

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Post pipeline from result](FEM_PostPipelineFromResult.md): Used to add a new graphical representation of FEM analysis results (color scale and more display options).

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Warp filter](FEM_PostFilterWarp.md): Used to visualize the scaled deformed shape of the model.

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalar clip filter](FEM_PostFilterClipScalar.md): Used to clip a field with a specified scalar value.

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Function cut filter](FEM_PostFilterCutFunction.md): Used to display the results on a sphere or a plane cutting through the model.

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Region clip filter](FEM_PostFilterClipRegion.md): Used to clip a field with a sphere or a plane cutting through the model.

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Line clip filter](FEM_PostFilterDataAlongLine.md): Used to plot the values of a field along a specified line.

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Stress linearization plot](FEM_PostFilterLinearizedStresses.md): Creates a stress linearization plot.

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Data at point clip filter](FEM_PostFilterDataAtPoint.md): Used to display value of a selected field at a given point.

-   <img alt="" src=images/FEM_CompPostCreateFunctions.png  style="width:48px;"> [Filter functions](FEM_PostCreateFunctions.md): This is an icon menu in the FEM Results toolbar that holds the following commands:

  - <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;"> [Filter function plane](FEM_PostCreateFunctionPlane.md): Defines that the result mesh is cut with a plane.

  - <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;"> [Filter function sphere](FEM_PostCreateFunctionSphere.md): Defines that the result mesh is cut with a sphere.

## Menu: Narzędzia 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Clipping plane on face](FEM_ClippingPlaneAdd.md): Adds a clipping plane for the whole model view.

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Remove all clipping planes](FEM_ClippingPlaneRemoveAll.md): Removes all existing [clipping planes](FEM_ClippingPlaneAdd.md).

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Open FEM examples](FEM_Examples.md): Open the GUI to access FEM examples.

## Menu podręczne 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Clear FEM mesh](FEM_MeshClear.md): Deletes the mesh file from the FreeCAD file. Useful to make a FreeCAD file lighter.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Display FEM mesh info](FEM_MeshDisplayInfo.md): Displays basic statistics of existing mesh - number of nodes and elements of each type.

## Ustawienia

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferences\...](FEM_Preferences.md): Preferences available in FEM Tools.

## Informacje dodatkowe 

The following pages explain different topics of the FEM Workbench.

[FEM Install](FEM_Install.md): a detailed description on how to set up the external programs used in the workbench.

[FEM Mesh](FEM_Mesh.md): further information on obtaining a mesh for finite element analysis.

[FEM Solver](FEM_Solver.md): further information on the different solvers available in the workbench, and those that could be used in the future.

[FEM CalculiX](FEM_CalculiX.md): further information on CalculiX, the default solver used in the workbench for structural analysis.

[FEM Concrete](FEM_Concrete.md): interesting information on the topic of simulating concrete structures.

## Poradniki

Poradnik 1: [MES CalculiX wspornik 3D](FEM_CalculiX_Cantilever_3D/pl.md), podstawowa analiza belki swobodnie podpartej.

Poradnik 2: [Poradnik dla środowiska pracy MES](FEM_tutorial/pl.md), prosta analiza naprężenia konstrukcji.

Poradnik 3: [Skrypty w środowisku MES](FEM_Tutorial_Python/pl.md), skonfiguruj przykład wspornika całkowicie poprzez skrypty w środowisku Python, w tym siatkę.

Poradnik 4: [Ścinanie bloku kompozytowego](FEM_Shear_of_a_Composite_Block/pl.md), obserwuj deformację bloku, który składa się z dwóch materiałów.

Poradnik 5: [Analiza MES w stanie przejściowym](Transient_FEM_analysis/pl.md).

Poradnik 6: [Post-Processing wyników MES za pomocą Paraview](Post-Processing_of_FEM_Results_with_Paraview/pl.md).

Poradnik 7: [Przykład pojemność dwóch kul](FEM_Example_Capacitance_Two_Balls/pl.md), Elmer\'s GUI poradnik 6 \"Elektrostatyka Pojemność Dwóch Kul\" z wykorzystaniem przykładów FEM.

Sprzężona analiza termiczno-mechaniczna poradnik [openSIM](https://opensimsa.github.io/training.html).

Wideo poradnik 1: [FEM wideo dla początkujących](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) *(w tym link do YouTube)*.

Wideo poradnik 2: [FEM wideo dla początkujących](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) *(w tym link do YouTube)*.

Wiele poradników w formie wideo: [anisim Open Source Engineering Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw), *(w języku niemieckim)*.

## Rozszerzenie środowiska pracy MES 

Środowisko pracy MES jest w ciągłym rozwoju. Celem projektu jest znalezienie sposobu na łatwą interakcję z różnymi solverami MES, tak aby użytkownik końcowy mógł usprawnić proces tworzenia, siatkowania, symulacji i optymalizacji problemu projektowego, wszystko w ramach programu FreeCAD.

Poniższe informacje są skierowane do użytkowników i programistów, którzy chcą rozszerzyć środowisko MES na różne sposoby. Oczekiwana jest znajomość C++ i Pythona, a także pewna znajomość systemu \"document object\" używanego w FreeCAD. Informacje te są dostępne na stronach [Centrum Power użytkowników](Power_users_hub/pl.md) i [Centrum programisty](Developer_hub/pl.md). Proszę zauważyć, że ponieważ FreeCAD jest w trakcie aktywnego rozwoju, niektóre artykuły mogą być zbyt stare, a więc przestarzałe. Najbardziej aktualne informacje są omawiane na [forum FreeCAD](https://forum.freecadweb.org/index.php), w sekcji Development. W przypadku dyskusji na temat MES, porad lub pomocy w rozszerzeniu środowiska pracy, czytelnik powinien odnieść się do [forum FEM](https://forum.freecadweb.org/viewforum.php?f=18).

Poniższe artykuły wyjaśniają, jak można rozszerzyć środowisko pracy, np. poprzez dodanie nowych typów warunków brzegowych *(wiązań)*, czy równań.

-   [Rozszerzenie modułu FEM](Extend_FEM_Module/pl.md)
-   [Wprowadzenie do MES dla programistów](Onboarding_FEM_Devs/pl.md) próbuje zorientować nowych twórców, w jaki sposób mogą przyczynić się do rozwoju środowiska pracy MES.
-   [Dodawanie wiązań w środowisku MES](Add_FEM_Constraint_Tutorial/pl.md)
-   [Dodawanie równań w środowisku MES](Add_FEM_Equation_Tutorial/pl.md)

Przewodnik programisty został napisany, aby pomóc użytkownikom w zrozumieniu złożonej bazy kodowej FreeCAD i interakcji między podstawowymi elementami i poszczególnymi środowiskami pracy. Książka jest umieszczona w serwisie Github, więc wielu użytkowników może ją współtworzyć i aktualizować.

-   [Wczesny podgląd ebooka: Przewodnik programisty modułów po źródłach FreeCAD](https://forum.freecadweb.org/viewtopic.php?t=17581) wątek na forum.
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) repozytorium Github.

## Rozszerzenie dokumentacji środowiska pracy MES 

-   Więcej informacji dotyczących rozszerzenia lub braku dokumentacji dla MES można znaleźć na forum, w temacie: [Brak dokumentacji MES na Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/pl
