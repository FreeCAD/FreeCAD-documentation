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

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Analiza MES](FEM_Analysis/pl.md): Tworzy nowy kontener dla analizy mechanicznej. Jeśli przed kliknięciem w oknie Widoku drzewa zostanie wybrana bryła, to następnie zostanie otwarte okno dialogowe generatora siatek.



### Materiał

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Materiał dla bryły](FEM_MaterialSolid/pl.md): Pozwala wybrać materiał dla bryły z bazy danych.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Materiał dla płynu](FEM_MaterialFluid/pl.md): Umożliwia wybór materiału dla płynu z bazy danych.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Nieliniowy materiał mechaniczny](FEM_MaterialMechanicalNonlinear/pl.md): Umożliwia dodanie nieliniowego modelu materiału mechanicznego.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Materiał zbrojony (beton)](FEM_MaterialReinforced/pl.md): Pozwala wybrać z bazy danych materiały zbrojone składające się z osnowy i zbrojenia.

-   <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Edytor materiału](FEM_MaterialEditor/pl.md): Pozwala otworzyć edytor materiałów, aby edytować materiały.



### Geometria elementu 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Przekrój poprzeczny belki](FEM_ElementGeometry1D/pl.md): Służy do definiowania przekrojów poprzecznych dla elementów belkowych.

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Obrót belki](FEM_ElementRotation1D/pl.md): Służy do obracania przekrojów poprzecznych elementów belkowych.

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Grubość powłoki](FEM_ElementGeometry2D/pl.md): Służy do określenia grubości powłoki elementu.

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Przekrój dla przepływu 1D](FEM_ElementFluid1D/pl.md): Służy do tworzenia elementu przekroju cieczy dla instalacji pneumatycznych i hydraulicznych.



### Wiązania elektromagnetyczne 

-   <img alt="" src=images/FEM_CompEmConstraints.png  style="width:48px;"> [Wiązania elektromagnetyczne](FEM_CompEmConstraints/pl.md): Jest to menu przyborów na pasku narzędzi wiązań MES, które zawiera następujące wiązania:

  - <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Zdefiniuj potencjał elektrostatyczny](FEM_ConstraintElectrostaticPotential/pl.md): Służy do definiowania potencjału elektrostatycznego.

  - <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:32px;"> [Zdefiniuj gęstość prądu](FEM_ConstraintCurrentDensity/pl.md): Służy do określenia gęstości prądu. {{Version/pl|0.21}}

  - <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:32px;"> [Zdefiniuj magnetyzację](FEM_ConstraintMagnetization/pl.md): Służy do określenia namagnesowania. {{Version/pl|0.21}}



### Wiązania płynu 

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Zdefiniuj początkową prędkość przepływu](FEM_ConstraintInitialFlowVelocity/pl.md): Służy do określenia początkowej prędkości przepływu dla ciała *(objętości)*.

-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Zdefiniuj początkowe obciążenie ciśnieniem](FEM_ConstraintInitialPressure/pl.md): Służy do określenia ciśnienia początkowego dla danego ciała *(objętości)*. {{Version/pl|0.21}}

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Zdefiniuj prędkość przepływu](FEM_ConstraintFlowVelocity/pl.md): Służy do określenia prędkości przepływu jako warunku brzegowego na krawędzi *(2D)* lub ścianie *(3D)*.



### Wiązania geometrii 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Zdefiniuj obrót w płaszczyźnie](FEM_ConstraintPlaneRotation/pl.md): Służy do definiowania wiązania obrotu w płaszczyźnie na ściance planarnej.

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Zapis wyników z przekroju](FEM_ConstraintSectionPrint/pl.md): Służy do drukowania predefiniowanych zmiennych wyjściowych ścian *(sił i momentów)* do pliku dat.

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Zdefiniuj odkształcenie](FEM_ConstraintTransform/pl.md): Służy do zdefiniowania wiązania przekształcenia na ścianie.



### Wiązania mechaniczne 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Zdefiniuj przytwierdzenie](FEM_ConstraintFixed/pl.md): Służy do definiowania stałego wiązania punktu / krawędzi / powierzchni.

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Constraint displacement](FEM_ConstraintDisplacement.md): Used to define a displacement constraint on point/edge/face(s).

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Constraint contact](FEM_ConstraintContact.md): Used to define a contact constraint between two faces.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Constraint tie](FEM_ConstraintTie.md): Used to define a tie constraint (\"bonded contact\") between two faces.

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Constraint spring](FEM_ConstraintSpring.md): Used to define a spring. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Constraint force](FEM_ConstraintForce.md): Used to define a force in \[N\] applied uniformly to a selectable face in a definable direction.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Constraint pressure](FEM_ConstraintPressure.md): Used to define a pressure constraint.

-   <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Constraint centrif](FEM_ConstraintCentrif.md): Used to define a centrifugal body load constraint. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Constraint self weight](FEM_ConstraintSelfWeight.md): Used to define a gravity acceleration acting on a model.



### Wiązania termiczne 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Constraint initial temperature](FEM_ConstraintInitialTemperature.md): Used to define the initial temperature of a body.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Constraint heatflux](FEM_ConstraintHeatflux.md): Used to define a heat flux constraint on a face(s).

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Constraint temperature](FEM_ConstraintTemperature.md): Used to define a temperature constraint on a point/edge/face(s).

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Constraint body heat source](FEM_ConstraintBodyHeatSource.md): Used to define an internally generated body heat.



### Wiązania nie wymagające solwera 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Fluid boundary condition](FEM_ConstraintFluidBoundary.md): Used to define a fluid boundary condition.

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Constraint bearing](FEM_ConstraintBearing.md): Used to define a bearing constraint.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Constraint gear](FEM_ConstraintGear.md): Used to define a gear constraint.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Constraint pulley](FEM_ConstraintPulley.md): Used to define a pulley constraint.



### Nadpisywanie wiązań 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity.md): Used to overwrite the [permittivity of vacuum](https://en.wikipedia.org/wiki/Vacuum_permittivity) with a custom value.



## Menu: Siatka 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [FEM mesh from shape by Netgen](FEM_MeshNetgenFromShape.md): Generates a finite element mesh for a model using Netgen.

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md): Generates a finite element mesh for a model using Gmsh.

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [FEM mesh boundary layer](FEM_MeshBoundaryLayer.md): Creates anisotropic meshes for accurate calculations near boundaries.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [FEM mesh region](FEM_MeshRegion.md): Creates a localized area(s) to mesh which highly optimizes analysis time.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [FEM mesh group](FEM_MeshGroup.md): Groups and labels elements of a mesh (vertex, edge, surface) together, useful for exporting the mesh to external solvers.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Nodes set](FEM_CreateNodesSet.md): Creates/defines a node set from FEM mesh.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh.md): Convert the surface of a FEM mesh to a mesh.



## Menu: Rozwiąż 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md): Creates a new solver for this analysis.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solver CalculiX (new framework)](FEM_SolverCalculiX.md): Same as the original framework <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools.md) with extra checks.

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md): Creates the solver controller for Elmer.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran.md): Creates the solver controller for the MYSTRAN solver. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solver Z88](FEM_SolverZ88.md): Creates the solver controller for Z88.

-   <img alt="" src=images/FEM_CompMechEquations.png  style="width:" height="32px;"> [Mechanical equations](FEM_CompMechEquations.md): This is an icon menu in the FEM Equations toolbar that holds the following equations: <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elasticity equation](FEM_EquationElasticity.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform linear mechanical analyses.

  - <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Deformation equation](FEM_EquationDeformation.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform nonlinear mechanical analyses (deformations). <small>(v0.21)</small> 

-   <img alt="" src=images/FEM_CompEmEquations.png  style="width:" height="32px;"> [Electromagnetic equations](FEM_CompEmEquations.md): This is an icon menu in the FEM Equations toolbar that holds the following equations: <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Electrostatic equation](FEM_EquationElectrostatic.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform electrostatic analyses.

  - <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Electricforce equation](FEM_EquationElectricforce.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate the electric force on surfaces.

  - <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:32px;"> [Magnetodynamic equation](FEM_EquationMagnetodynamic.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate magnetodynamics. <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:32px;"> [Magnetodynamic 2D equation](FEM_EquationMagnetodynamic2D.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate magnetodynamics in 2D. <small>(v0.21)</small> 

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Flow equation](FEM_EquationFlow.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform flow analyses.

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Flux equation](FEM_EquationFlux.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform flux analyses.

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Heat equation](FEM_EquationHeat.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform heat transfer analyses.

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Solver job control](FEM_SolverControl.md): Opens the menu to adjust and start the selected solver.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Run solver calculations](FEM_SolverRun.md): Runs the selected solver of the active analysis.



## Menu: Wyniki 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Usuń wyniki](FEM_ResultsPurge/pl.md): Kasuje wyniki aktywnej analizy.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Pokaż wynik](FEM_ResultShow/pl.md): Służy do wyświetlania wyniku analizy. To okno dialogowe nie jest dostępne dla [Solvera Elmer](FEM_SolverElmer/pl.md), ponieważ ten solver wizualizuje tylko przy użyciu obiektu [Prezentacja graficzna wyników](FEM_PostPipelineFromResult/pl.md).

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Zastosuj zmiany](FEM_PostApplyChanges/pl.md): Przełącza, czy zmiany w potokach i filtrach są stosowane natychmiast.

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Prezentacja graficzna wyników](FEM_PostPipelineFromResult/pl.md): Służy do dodania nowej graficznej reprezentacji wyników analizy MES *(skala kolorów i więcej opcji wyświetlania)*.

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Filtr wizualizacji deformacji](FEM_PostFilterWarp/pl.md): Służy do wizualizacji skalowanego zdeformowanego kształtu modelu.

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalar clip filter](FEM_PostFilterClipScalar.md): Used to clip a field with a specified scalar value.

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Function cut filter](FEM_PostFilterCutFunction.md): Used to display the results on a sphere or a plane cutting through the model.

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Region clip filter](FEM_PostFilterClipRegion.md): Used to clip a field with a sphere or a plane cutting through the model.

-   <img alt="" src=images/FEM_PostFilterContours.svg  style="width:32px;"> [Contours filter](FEM_PostFilterContours.md): Used to display iso-lines (for analyses in 2D) or iso-contours. <small>(v0.21)</small> 

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Line clip filter](FEM_PostFilterDataAlongLine.md): Used to plot the values of a field along a specified line.

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Stress linearization plot](FEM_PostFilterLinearizedStresses.md): Creates a stress linearization plot.

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Data at point clip filter](FEM_PostFilterDataAtPoint.md): Used to display value of a selected field at a given point.

-   <img alt="" src=images/FEM_CompPostCreateFunctions.png  style="width:" height="32px;"> [Filter functions](FEM_PostCreateFunctions.md): This is an icon menu in the FEM Results toolbar that holds the following commands:

  - <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:32px;"> [Filter function plane](FEM_PostCreateFunctionPlane.md): Cuts the result mesh with a plane.

  - <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:32px;"> [Filter function sphere](FEM_PostCreateFunctionSphere.md): Cuts the result mesh with a sphere.

  - <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:32px;"> [Filter function cylinder](FEM_PostCreateFunctionCylinder.md): Cuts the result mesh with a cylinder. <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:32px;"> [Filter function box](FEM_PostCreateFunctionBox.md): Cuts the result mesh with a box. <small>(v0.21)</small> 



## Menu: Narzędzia 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Płaszczyzna cięcia na ścianie](FEM_ClippingPlaneAdd/pl.md): Dodaje płaszczyznę przycinania dla całego widoku modelu.

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Usuń wszystkie płaszczyzny cięcia](FEM_ClippingPlaneRemoveAll/pl.md): Usuwa wszystkie istniejące [płaszczyzny cięcia](FEM_ClippingPlaneAdd/pl.md).

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Otwórz przykłady](FEM_Examples/pl.md): Otwórz GUI, aby uzyskać dostęp do przykładów MES.



## Menu podręczne 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Wyczyść dane siatki MES](FEM_MeshClear/pl.md): Usuwa plik siatki z pliku FreeCAD. Przydatne, aby uczynić plik FreeCAD lżejszym.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Wyświetl informacje o siatce MES](FEM_MeshDisplayInfo/pl.md): Wyświetla podstawowe statystyki istniejącej siatki - ilość węzłów i elementów każdego typu.



## Ustawienia

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferencje \...](FEM_Preferences/pl.md): Ustawienia dostępne dla narzędzi środowiska MES w menu Edycja.



## Informacje dodatkowe 

Na kolejnych stronach znajdują się objaśnienia poszczególnych tematów związanych z środowiskiem pracy MES.

[Instalacja środowiska MES](FEM_Install/pl.md): szczegółowy opis jak skonfigurować zewnętrzne programy używane w środowisku pracy.

[MES: Siatka](FEM_Mesh/pl.md): dalsze informacje na temat uzyskiwania siatki do analizy metodą elementów skończonych.

[MES: Solver](FEM_Solver/pl.md): dalsze informacje na temat różnych solverów dostępnych w środowisku pracy oraz tych, które mogą być używane w przyszłości.

[MES: CalculiX](FEM_CalculiX/pl.md): dalsze informacje na temat CalculiX, domyślnego solvera używanego w środowisku pracy do analizy strukturalnej.

[MES: Beton](FEM_Concrete/pl.md): ciekawe informacje na temat symulacji konstrukcji betonowych.



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
![](images/Button_right.svg) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/pl
