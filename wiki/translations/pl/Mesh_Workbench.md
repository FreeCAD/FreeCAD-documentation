# <img alt="Ikona FreeCAD dla środowiska pracy Siatka" src=images/Workbench_Mesh.svg  style="width:64px;"> Mesh Workbench/pl






## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Siatka](Mesh_Workbench/pl.md) obsługuje [sieci trójkątnych oczek](http://en.wikipedia.org/wiki/Triangle_mesh). Siatki są specjalnym rodzajem obiektu 3D, złożonym z trójkątnych ścian połączonych ich wierzchołkami i krawędziami.

Wiele aplikacji 3D, takich jak [Sketchup](http://en.wikipedia.org/wiki/Sketchup), [Blender](http://en.wikipedia.org/wiki/Blender_(software)), [Maya](http://en.wikipedia.org/wiki/Maya_(software)) i [3D Studio Max](http://en.wikipedia.org/wiki/3d_max), używa siatki jako podstawowego typu obiektu 3D. Ponieważ siatki są bardzo prostymi obiektami, zawierającymi tylko wierzchołki *(punkty)*, krawędzie i trójkątne powierzchnie, są one bardzo łatwe do tworzenia, modyfikowania, dzielenia, rozciągania i mogą być łatwo przekazywane z jednej aplikacji do drugiej bez utraty szczegółów. Ponadto, ponieważ siatki zawierają bardzo nieskomplikowane dane, aplikacje 3D mogą zazwyczaj zarządzać bardzo dużymi ich ilościami bez konieczności używania wielkich zasobów. Z tych powodów, siatki są często wybierane jako obiekt 3D dla aplikacji obsługujących filmy, animacje i tworzenie obrazów.

**Jednak w dziedzinie siatek inżynieryjnych istnieje jedno duże ograniczenie:** nie mogą one dokładnie określać zakrzywionych powierzchni. Dlatego FreeCAD polega na [Brep](wikipedia_Boundary_representation.md). Środowisko pracy Mesh oferuje kilka poleceń do bezpośredniego manipulowania siatkami, ale najczęściej jest używane do importu danych o siatkach 3D i konwertowania ich na bryłę, do użycia w Środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/pl.md) lub <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md).

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">



## Przybory

Wszystkie narzędzia Środowiska pracy Siatka są dostępne w menu **Siatki**. Prawie wszystkie są również dostępne w jednym z pasków narzędzi **Siatka**.

-   <img alt="" src=images/Mesh_Import.svg  style="width:32px;"> [Import siatki\...](Mesh_Import.md): : Importuje obiekty siatek z pliku.

-   <img alt="" src=images/Mesh_Export.svg  style="width:32px;"> [Eksport siatki\...](Mesh_Export.md): Eksport obiektów siatek do pliku.

-   <img alt="" src=images/Mesh_FromPartShape.svg  style="width:32px;"> \[\[Mesh_FromPartShape\|

Utwórz siatkę z kształtu \...\]\]: Tworzy obiekty siatkowe z obiektów kształtu.

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width:32px;"> [Ulepsz przez Gmsh](Mesh_RemeshGmsh/pl.md): Ulepsza obiekty siatkowe.

-   Analiza
    -   <img alt="" src=images/Mesh_Evaluation.svg  style="width:32px;"> [Oceń i napraw siatkę\...](Mesh_Evaluation.md) Ocenia i naprawia obiekt siatkowy.
    -   <img alt="" src=images/Mesh_CurvatureInfo.svg  style="width:32px;"> [Dane o powierzchnii](Mesh_EvaluateFacet.md): Pokazuje informacje o powierzchniach obiektów siatkowych.
    -   [Informacje o krzywiźnie](Mesh_EvaluateCurvature.md): Pokazuje krzywiznę absolutną [obiektów krzywizny](Mesh_VertexCurvature.md) w wybranych punktach.
    -   <img alt="" src=images/Mesh_EvaluateSolid.svg  style="width:32px;"> [Sprawdź siatkę bryły](Mesh_EvaluateSolid.md): Sprawdza, czy obiekt siatkowy jest bryłą.
    -   <img alt="" src=images/Mesh_BoundingBox.svg  style="width:32px;"> [Informacja o granicach](Mesh_BoundingBox.md): Pokazuje współrzędne pola ograniczającego obiekt siatki.

-   <img alt="" src=images/Mesh_VertexCurvature.svg  style="width:32px;"> [Wykres krzywizny](Mesh_VertexCurvature.md): Tworzy obiekty krzywizny siatki dla obiektów siatkowych.

-   <img alt="" src=images/Mesh_HarmonizeNormals.svg  style="width:32px;"> [Porządkuj wektory normalne](Mesh_HarmonizeNormals.md): Ujednolicenie wektorów normalnych obiektu siatki.

-   <img alt="" src=images/Mesh_FlipNormals.svg  style="width:32px;"> [Odwróć wektory normalne](Mesh_FlipNormals.md): Odwraca wektory normalne obiektu siatki.

-   <img alt="" src=images/Mesh_FillupHoles.svg  style="width:32px;"> [Wypełnij otwory\...](Mesh_FillupHoles.md): Wypełnia otwory w obiekcie siatki.

-   <img alt="" src=images/Mesh_FillInteractiveHole.svg  style="width:32px;"> [Zamknij otwór](Mesh_FillInteractiveHole.md): Wypełnia wybrane otwory w obiektach siatkowych.

-   <img alt="" src=images/Mesh_AddFacet.svg  style="width:32px;"> [Dodaj trójkąt](Mesh_AddFacet.md) : Dodaje powierzchnie wzdłuż obwiedni otwartego obiektu siatkowego.

-   <img alt="" src=images/Mesh_RemoveComponents.svg  style="width:32px;"> [Usuń fragment\...](Mesh_RemoveComponents.md): Usuwa powierzchnie z obiektów siatkowych.

-   <img alt="" src=images/Mesh_RemoveCompByHand.svg  style="width:32px;"> [Usuń fragment ręcznie\...](Mesh_RemoveCompByHand.md): Usuwa elementy z obiektów siatkowych.

-   <img alt="" src=images/Mesh_Segmentation.svg  style="width:32px;"> [Utwórz segmenty siatki\...](Mesh_Segmentation.md): Tworzy oddzielne segmenty siatki dla określonych typów powierzchni obiektu siatkowego.

-   <img alt="" src=images/Mesh_SegmentationBestFit.svg  style="width:32px;"> [Utwórz segmenty siatki z najlepiej dopasowanych powierzchni\...](Mesh_SegmentationBestFit.md): Tworzy oddzielne segmenty siatki dla określonych typów powierzchni obiektu siatkowego i może określić ich parametry.

-   <img alt="" src=images/Mesh_Smoothing.svg  style="width:32px;"> [Wygładź\...](Mesh_Smoothing.md): Wygładza obiekt siatki.

-   <img alt="" src=images/Mesh_Decimating.svg  style="width:32px;"> [Uprość \...](Mesh_Decimating/pl.md): Zmniejsza liczbę ścianek w obiektach siatkowych.

-   <img alt="" src=images/Mesh_Scale.svg  style="width:32px;"> [Skala\...](Mesh_Scale.md): Skaluje obiekt siatki.

-   <img alt="" src=images/Mesh_BuildRegularSolid.svg  style="width:32px;"> [Bryła podstawowa\...](Mesh_BuildRegularSolid.md): Tworzy regularny, parametryczny obiekt siatki bryły pierwotnej.

-   Operacje logiczne
    -   <img alt="" src=images/Mesh_Union.svg  style="width:32px;"> [Suma](Mesh_Union.md): Tworzy obiekt siatki, który jest połączeniem dwóch obiektów siatki.
    -   <img alt="" src=images/Mesh_Intersection.svg  style="width:32px;"> [Przecięcie](Mesh_Intersection.md): Tworzy obiekt siatki, który jest przecięciem dwóch obiektów siatki.
    -   <img alt="" src=images/Mesh_Difference.svg  style="width:32px;"> [Różnica](Mesh_Difference.md): Tworzy obiekt siatki, który jest różnicą dwóch obiektów siatki.

-   Przycinanie
    -   <img alt="" src=images/Mesh_PolyCut.svg  style="width:32px;"> [Przytnij siatkę linia łamaną](Mesh_PolyCut/pl.md): Wycina całe powierzchnie z obiektów siatkowych.
    -   <img alt="" src=images/Mesh_PolyTrim.svg  style="width:32px;"> [Przytnij siatkę](Mesh_PolyTrim/pl.md): Przycina powierzchnie i części ścian z obiektów siatki.
    -   <img alt="" src=images/Mesh_TrimByPlane.svg  style="width:32px;"> [Przytnij siatkę płaszczyzną](Mesh_TrimByPlane/pl.md): Przycina powierzchnie i części powierzchni po jednej stronie płaszczyzny z obiektu siatkowego.
    -   <img alt="" src=images/Mesh_SectionByPlane.svg  style="width:32px;"> [Tworzenie przekroju z siatki i płaszczyzny](Mesh_SectionByPlane/pl.md): Tworzy przekrój poprzeczny przez obiekt siatkowy.
    -   <img alt="" src=images/Mesh_CrossSections.svg  style="width:32px;"> [Przekrój\...](Mesh_CrossSections/pl.md): Tworzy wiele przekrojów poprzecznych na obiektach siatkowych.

-   <img alt="" src=images/Mesh_Merge.svg  style="width:32px;"> [Połącz](Mesh_Merge.md): Tworzy obiekt siatki poprzez połączenie dwóch lub więcej obiektów siatkowych.

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width:32px;"> [Podziel według komponentów](Mesh_SplitComponents/pl.md): Dzieli obiekt siatkowy na jego komponenty.

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Rozwiń siatkę](MeshPart_CreateFlatMesh/pl.md): Tworzy płaską reprezentację obiektu siatkowego.

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Rozwiń powierzchnię](MeshPart_CreateFlatFace/pl.md): Tworzy płaską reprezentację powierzchni obiektu kształtu.



## Ustawienia

Istnieje kilka [preferencji eksportu związanych z formatami siatki](Import_Export_Preferences/pl#Formaty_Mesh.md), ale nie są one używane przez polecenia należące do tego stanowiska pracy. Są one używane przez polecenie [Std: Eksport](Std_Export/pl.md).

Preferencje środowiska pracy Siatka można znaleźć w następujących kategoriach [Edytora Preferencji](Preferences_Editor/pl.md):

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Wyświetlanie](Preferences_Editor/pl#Ustawienia_wyświetlania.md): Na stronie [widoku siatki](Preferences_Editor/pl#Widok_siatki.md) można ustawić kilka parametrów.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences/pl.md): Polecenia [Siatka: Połączenie](Mesh_Union/pl.md), [Siatka: Przecięcie](Mesh_Intersection/pl.md) oraz [Siatka: Różnica](Mesh_Difference/pl.md) wymagają [OpenSCAD](http://www.openscad.org/) i użyj preferencji **OpenSCAD executable**, aby znaleźć jego plik wykonywalny.



## Uwagi

-   Więcej narzędzi mesh jest dostępnych w Środowisku pracy <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD](OpenSCAD_Workbench/pl.md)
-   Siatkami można również manipulować i tworzyć je za pomocą [skryptów](Mesh_Scripting/pl.md) środowiska [Python](Python/pl.md).
-   Zobacz również: [FreeCAD oraz import siatki](FreeCAD_and_Mesh_Import.md).
-   Zobacz [Asymptote](Asymptote.md), aby wyeksportować siatki do formatu Asymptote.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Mesh](Category_Mesh.md) > Mesh Workbench/pl
