# <img alt="Ikonka FreeCAD dla środowiska pracy MES" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/pl






## Wprowadzenie

Środowisko pracy **MES** zapewnia nowoczesną [analizę metodą elementów skończonych](https://pl.wikipedia.org/wiki/Metoda_element%C3%B3w_sko%C5%84czonych) *(MES)* dla FreeCAD. Głównie oznacza to, że wszystkie narzędzia do wykonania analizy są połączone w jeden graficzny interfejs użytkownika *(GUI)*.

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

  - <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Materiał dla bryły](FEM_MaterialSolid/pl.md): Pozwala wybrać materiał dla bryły z bazy danych.

  - <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Materiał dla płynu](FEM_MaterialFluid/pl.md): Umożliwia wybór materiału dla płynu z bazy danych.

  - <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Nieliniowy materiał mechaniczny](FEM_MaterialMechanicalNonlinear/pl.md): Umożliwia dodanie nieliniowego modelu materiału mechanicznego.

  - <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Materiał zbrojony *(beton)*](FEM_MaterialReinforced/pl.md): Pozwala wybrać z bazy danych materiały zbrojone składające się z osnowy i zbrojenia.

  - <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Edytor materiału](FEM_MaterialEditor/pl.md): Pozwala otworzyć edytor materiałów, aby edytować materiały.



### Geometria elementu 

  - <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Przekrój poprzeczny belki](FEM_ElementGeometry1D/pl.md): Służy do definiowania przekrojów poprzecznych dla elementów belkowych.

  - <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Obrót belki](FEM_ElementRotation1D/pl.md): Służy do obracania przekrojów poprzecznych elementów belkowych.

  - <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Grubość powłoki](FEM_ElementGeometry2D/pl.md): Służy do określenia grubości powłoki elementu.

  - <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Przekrój dla przepływu 1D](FEM_ElementFluid1D/pl.md): Służy do tworzenia elementu przekroju cieczy dla instalacji pneumatycznych i hydraulicznych.



### Elektromagnetyczne warunki brzegowe 

  - <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Warunek brzegowy potencjału elektrostatycznego](FEM_ConstraintElectrostaticPotential/pl.md): Służy do definiowania potencjału elektrostatycznego.

  - <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:32px;"> [Warunek brzegowy gęstości prądu](FEM_ConstraintCurrentDensity/pl.md): Służy do określenia gęstości prądu. {{Version/pl|0.21}}

  - <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:32px;"> [Warunek brzegowy magnetyzacji](FEM_ConstraintMagnetization/pl.md): Służy do określenia magnetyzacji. {{Version/pl|0.21}}



### Warunki brzegowe płynu 

  - <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Warunek początkowy prędkości przepływu](FEM_ConstraintInitialFlowVelocity/pl.md): Służy do określenia początkowej prędkości przepływu dla ciała *(objętości)*.

  - <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Warunek początkowy ciśnienia](FEM_ConstraintInitialPressure/pl.md): Służy do określenia ciśnienia początkowego dla danego ciała *(objętości)*. {{Version/pl|0.21}}

  - <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Warunek brzegowy prędkości przepływu](FEM_ConstraintFlowVelocity/pl.md): Służy do określenia prędkości przepływu jako warunku brzegowego na krawędzi *(2D)* lub ścianie *(3D)*.



### Funkcje analizy geometrycznej 

  - <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Wiązanie MPC typu płaszczyzna](FEM_ConstraintPlaneRotation/pl.md): Służy do definiowania wiązania utrzymującego węzły na płaskiej powierzchni w tej samej płaszczyźnie.

  - <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Funkcja zapisu wyników z przekroju](FEM_ConstraintSectionPrint/pl.md): Służy do drukowania predefiniowanych zmiennych wyjściowych ścian *(sił i momentów)* do pliku danych.

  - <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Lokalny układ współrzędnych](FEM_ConstraintTransform/pl.md): Służy do zdefiniowania wiązania przekształcenia na ścianie.



### Mechaniczne warunki brzegowe i obciążenia 

  - <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Warunek brzegowy utwierdzenia](FEM_ConstraintFixed/pl.md): Służy do definiowania stałego wiązania punktu / krawędzi / powierzchni.

  - <img alt="" src=images/FEM_ConstraintRigidBody.svg  style="width:32px;"> [Wiązanie ciała sztywnego](FEM_ConstraintRigidBody/pl.md): Służy do definiowania wiązania ciała sztywnego solvera CalculiX, które wiąże ruch węzłów wybranego obiektu geometrycznego z ruchem punktu referencyjnego o pozycji określonej przez użytkownika. {{Version/pl|1.0}}

  - <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Warunek brzegowy przemieszczenia](FEM_ConstraintDisplacement/pl.md): Służy do definiowania przemieszczeń punktów / krawędzi / powierzchni.

  - <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Kontakt](FEM_ConstraintContact/pl.md): Służy do definiowania kontaktu między 2 powierzchniami.

  - <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Wiązanie tie](FEM_ConstraintTie/pl.md): Służy do definiowania wiązania tie *(\"kontakt wiązany\")* między 2 powierzchniami lub, {{Version/pl|1.0}}, symetrią cykliczną.

  - <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Sprężyna](FEM_ConstraintSpring/pl.md): Służy do definiowania sprężyny. {{Version/pl|0.20}}

  - <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Obciążenie siłą](FEM_ConstraintForce/pl.md): Służy do definiowania siły w \[N\] rozłożonej równomiernie na wybranych ścianach w określonym kierunku.

  - <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Obciążenie ciśnieniem](FEM_ConstraintPressure/pl.md): Służy do definiowania obciążenia powierzchni ciśnieniem.

  - <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Obciążenie siłą odśrodkową](FEM_ConstraintCentrif/pl.md): Służy do definiowania obciążenia ciała siłą odśrodkową. {{Version/pl|0.20}}

  - <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Obciążenie grawitacją](FEM_ConstraintSelfWeight/pl.md): Służy do definiowania przyspieszenia grawitacyjnego działającego na model.



### Termiczne warunki brzegowe i obciążenia 

  - <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Temperatura początkowa](FEM_ConstraintInitialTemperature/pl.md): Służy do definiowania początkowej temperatury ciała.

  - <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Obciążenie strumieniem ciepła](FEM_ConstraintHeatflux/pl.md): Służy do definiowania obciążenia powierzchni strumieniem ciepła.

  - <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Warunek brzegowy temperatury](FEM_ConstraintTemperature/pl.md): Służy do definiowania warunku brzegowego temperatury dla punktu / krawędzi / ściany.

  - <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Objętościowe źródło ciepła](FEM_ConstraintBodyHeatSource/pl.md): Służy do definiowania ciepła generowanego w ciele.



### Nadpisywanie wiązań 

  - <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Zdefiniuj przenikalność elektryczną próżni](FEM_ConstantVacuumPermittivity/pl.md): Służy do nadpisywania [przenikalności elektrycznej próżni](https://en.wikipedia.org/wiki/Vacuum_permittivity) dowolną wartością.



## Menu: Siatka 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [Siatka MES z kształtu przy pomocy generatora Netgen](FEM_MeshNetgenFromShape/pl.md): Generuje siatkę MES dla modelu przy pomocy generatora Netgen.

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Siatka MES z kształtu przy pomocy generatora Gmsh](FEM_MeshGmshFromShape/pl.md): Tworzy siatkę MES dla modelu przy pomocy generatora Gmsh.

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [Warstwa graniczna siatki](FEM_MeshBoundaryLayer/pl.md): Tworzy anizotropowe siatki dla dokładnych obliczeń przy brzegach.

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [Obszar siatki](FEM_MeshRegion/pl.md): Tworzy zlokalizowane obszary do generowania siatki, aby zoptymalizować czas obliczeń.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [Grupa siatki](FEM_MeshGroup/pl.md): Grupuje i oznacza elementy siatki *(wierzchołek, krawędź, powierzchnia)* razem - przydatne do eksportowania siatki do zewnętrznych solverów.

-   <img alt="" src=images/FEM_CreateElementsSet.svg  style="width:32px;"> [Usuń elementy](FEM_CreateElementsSet/pl.md): Ukrywa elementy wskazane wielokątem z siatki. {{Version/pl|1.0}}

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [Siatka MES na obiekt środowiska Siatka](FEM_FemMesh2Mesh/pl.md): Konwertuje powierzchnie elementów 3D lub całe elementy 2D wybranej siatki MES na siatkę powierzchniową.



## Menu: Rozwiąż 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Narzędzia CalculiX](FEM_SolverCalculixCxxtools/pl.md): Tworzy kontroler solvera dla CalculiX.

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer/pl.md): Tworzy kontroler solvera dla Elmer.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran/pl.md): Tworzy kontroler solvera dla Mystran. {{Version/pl|0.20}}

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Solver Z88](FEM_SolverZ88/pl.md): Tworzy kontroler solvera dla Z88.



### Równania mechaniczne 

  - <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Równanie elastyczności](FEM_EquationElasticity/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do liniowych analiz mechanicznych.

  - <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Równanie deformacji](FEM_EquationDeformation/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do nieliniowych analiz mechanicznych. {{Version/pl|0.21}}



### Równania elektromagnetyczne 

  - <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Równanie elektrostatyczne](FEM_EquationElectrostatic/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do analiz elektrostatycznych.

  - <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Równanie siły elektrostatycznej](FEM_EquationElectricforce/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do obliczania sił elektrycznych na powierzchni.

  - <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:32px;"> [Równanie magnetodynamiczne](FEM_EquationMagnetodynamic/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do analiz magnetodynamicznych. {{Version/pl|0.21}}

  - <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:32px;"> [Równanie magnetodynamiczne 2D](FEM_EquationMagnetodynamic2D/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do analiz magnetodynamicznych 2D. {{Version/pl|0.21}}

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Równanie przepływu](FEM_EquationFlow/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do analiz przepływów.

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Równanie strumienia](FEM_EquationFlux/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do analiz strumieni.

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Równanie ciepła](FEM_EquationHeat/pl.md): Równanie dla <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solvera Elmer](FEM_SolverElmer/pl.md) do analiz przepływu ciepła.

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Kontrola pracy solvera](FEM_SolverControl/pl.md): Otwiera menu do ustawiania i uruchamiania wybranego solvera.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Uruchom solver](FEM_SolverRun/pl.md): Uruchamia wybrany solver w aktywnej analizie.



## Menu: Wyniki 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Usuń wyniki](FEM_ResultsPurge/pl.md): Kasuje wyniki aktywnej analizy.

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Pokaż wynik](FEM_ResultShow/pl.md): Służy do wyświetlania wyniku analizy. To okno dialogowe nie jest dostępne dla [Solvera Elmer](FEM_SolverElmer/pl.md), ponieważ ten solver wizualizuje tylko przy użyciu obiektu [Prezentacja graficzna wyników](FEM_PostPipelineFromResult/pl.md).

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Zastosuj zmiany](FEM_PostApplyChanges/pl.md): Przełącza, czy zmiany w potokach i filtrach są stosowane natychmiast.

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Prezentacja graficzna wyników](FEM_PostPipelineFromResult/pl.md): Służy do dodania nowej graficznej reprezentacji wyników analizy MES *(skala kolorów i więcej opcji wyświetlania)*.

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Filtr wizualizacji deformacji](FEM_PostFilterWarp/pl.md): Służy do wizualizacji skalowanego zdeformowanego kształtu modelu.

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Filtr przycinania skalarnego](FEM_PostFilterClipScalar/pl.md): Służy do przycinania pola wybraną wartością skalarną.

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Filtr cięcia funkcją](FEM_PostFilterCutFunction/pl.md): Służy do wyświetlania wyników na kuli lub płaszczyźnie przecinającej model.

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Filtr przycięcia obszaru](FEM_PostFilterClipRegion/pl.md): Służy do przycinania pola kulą lub płaszczyzną przechodzącą przez model.

-   <img alt="" src=images/FEM_PostFilterContours.svg  style="width:32px;"> [Filtr konturów](FEM_PostFilterContours/pl.md): Służy do wyświetlania izolinii *(w 2D)* i izokonturów. {{Version/pl|0.21}}

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Filtr przycięcia linią](FEM_PostFilterDataAlongLine/pl.md): Służy do wyświetlania wartości pola wzdłuż wskazanej linii.

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Wykres linearyzacji naprężeń](FEM_PostFilterLinearizedStresses/pl.md): Tworzy wykres linearyzacji naprężeń.

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Filtr danych w punkcie](FEM_PostFilterDataAtPoint/pl.md): Służy do wyświetlania wartości wybranego pola we wskazanym punkcie.



### Funkcje filtrowania 

  - <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:32px;"> [Utwórz funkcję płaszczyzny](FEM_PostCreateFunctionPlane/pl.md): Przecina siatkę wynikową płaszczyzną.

  - <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:32px;"> [Utwórz funkcję sfery](FEM_PostCreateFunctionSphere/pl.md): Przecina siatkę wynikową kulą.

  - <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:32px;"> [Utwórz funkcję walca](FEM_PostCreateFunctionCylinder/pl.md): Przecina siatkę wynikową walcem. {{Version/pl|0.21}}

  - <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:32px;"> [Utwórz funkcję prostopadłościanu](FEM_PostCreateFunctionBox/pl.md): Przecina siatkę wynikową prostopadłościanem. {{Version/pl|0.21}}



## Menu: Narzędzia 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Płaszczyzna cięcia na ścianie](FEM_ClippingPlaneAdd/pl.md): Dodaje płaszczyznę przycinania dla całego widoku modelu.

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Usuń wszystkie płaszczyzny cięcia](FEM_ClippingPlaneRemoveAll/pl.md): Usuwa wszystkie istniejące [płaszczyzny cięcia](FEM_ClippingPlaneAdd/pl.md).

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Otwórz przykłady](FEM_Examples/pl.md): Otwórz GUI, aby uzyskać dostęp do przykładów MES.



## Menu podręczne 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Wyczyść dane siatki MES](FEM_MeshClear/pl.md): Usuwa plik siatki z pliku FreeCAD. Przydatne, aby uczynić plik FreeCAD lżejszym.

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Wyświetl informacje o siatce MES](FEM_MeshDisplayInfo/pl.md): Wyświetla podstawowe statystyki istniejącej siatki - ilość węzłów i elementów każdego typu.



## Narzędzia przestarzałe 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Zdefiniuj przepływ graniczny](FEM_ConstraintFluidBoundary/pl.md): Służy do definiowania warunku brzegowego płynu. Niewspierane przez żaden solver, niedostępne w {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Wiązanie łożyska](FEM_ConstraintBearing/pl.md): Służy do definiowania wiązania łożyska. Niewspierane przez żaden solver, niedostępne w {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Wiązanie koła zębatego](FEM_ConstraintGear/pl.md): Służy do definiowania wiązania koła zębatego. Niewspierane przez żaden solver, niedostępne w {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Constraint pulley](FEM_ConstraintPulley/pl.md): Służy do definiowania wiązania koła pasowego. Niewspierane przez żaden solver, niedostępne w {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Solver CalculiX](FEM_SolverCalculiX/pl.md): To samo co <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Narzędzia CalculiX](FEM_SolverCalculixCxxtools/pl.md) z dodatkowymi sprawdzeniami. Narzędzie niedokończone, niedostępne w {{VersionPlus/pl|1.0}}.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Utwórz zestaw węzłów](FEM_CreateNodesSet/pl.md): Tworzy zestaw węzłów z siatki MES.

Narzędzie było niedokończone i nie można było go użyć. Niedostępne w {{VersionPlus/pl|1.0}}.



## Ustawienia

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferencje \...](FEM_Preferences/pl.md): Ustawienia dostępne dla narzędzi środowiska MES w menu Edycja.



## Informacje dodatkowe 

Na kolejnych stronach znajdują się objaśnienia poszczególnych tematów związanych z środowiskiem pracy MES.

[Instalacja środowiska MES](FEM_Install/pl.md): szczegółowy opis jak skonfigurować zewnętrzne programy używane w środowisku pracy.

[Przygotowanie geometrii i siatki MES](FEM_Geometry_Preparation_and_Meshing/pl.md): wskazówki dotyczące przygotowania geometrii dla MES i siatki.

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

Wideo poradnik 1: [MES wideo dla początkujących](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) *(w tym link do YouTube)*.

Wideo poradnik 2: [MES wideo dla początkujących](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) *(w tym link do YouTube)*.

Wiele poradników w formie wideo: [anisim Open Source Engineering Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw), *(w języku niemieckim)*.



## Rozszerzenie środowiska pracy MES 

Środowisko pracy MES jest w ciągłym rozwoju. Celem projektu jest znalezienie sposobu na łatwą interakcję z różnymi solverami MES, tak aby użytkownik końcowy mógł usprawnić proces tworzenia, generowania siatki, symulacji i optymalizacji problemu projektowego, wszystko w ramach programu FreeCAD.

Poniższe informacje są skierowane do użytkowników i programistów, którzy chcą rozszerzyć środowisko MES na różne sposoby. Oczekiwana jest znajomość C++ i środowiska Python, a także pewna znajomość systemu \"document object\" używanego w FreeCAD. Informacje te są dostępne na stronach [Centrum Power użytkowników](Power_users_hub/pl.md) i [Centrum programisty](Developer_hub/pl.md). Proszę zauważyć, że ponieważ FreeCAD jest w trakcie aktywnego rozwoju, niektóre artykuły mogą być zbyt stare, a więc przestarzałe. Najbardziej aktualne informacje są omawiane na [forum FreeCAD](https://forum.freecadweb.org/index.php), w sekcji Development. W przypadku dyskusji na temat MES, porad lub pomocy w rozszerzeniu środowiska pracy, czytelnik powinien odnieść się do [forum MES](https://forum.freecadweb.org/viewforum.php?f=18).

Poniższe artykuły wyjaśniają, jak można rozszerzyć środowisko pracy, np. poprzez dodanie nowych typów warunków brzegowych *(wiązań)*, czy równań.

-   [Rozszerzenie modułu MES](Extend_FEM_Module/pl.md)
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
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/pl
