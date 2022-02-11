# Topological naming problem/pl
## Wprowadzenie


{{TOCright}}

Problem z **nazewnictwem topologicznym** w programie FreeCAD odnosi się do kwestii zmiany wewnętrznej nazwy kształtu po wykonaniu operacji modelowania *(wyciągnięcie, wycięcie, połączenie, fazka, zaokrąglenie, itp.)*. Spowoduje to, że inne właściwości parametryczne, które zależą od tego kształtu, zostaną uszkodzone lub niepoprawnie obliczone. Ten problem dotyczy wszystkich obiektów w programie FreeCAD, ale jest szczególnie zauważalny podczas budowania brył za pomocą środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), oraz podczas wymiarowania tych brył za pomocą środowiska<img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md).

-   W środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), jeśli element jest obsługiwany na powierzchni *(lub krawędzi lub wierzchołku)*, element może zostać uszkodzony, jeśli bazowa bryła zmieni rozmiar lub orientację, ponieważ oryginalna powierzchnia *(lub krawędź lub wierzchołek)* może zostać wewnętrznie przemianowana.
-   W przypadku środowiska <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md), jeżeli wymiar mierzy długość rzutowanej krawędzi, wymiar może zostać uszkodzony, jeżeli model 3D zostanie zmodyfikowany, ponieważ wierzchołki mogą zostać przemianowane, zmieniając w ten sposób mierzoną krawędź.

Kwestia nazewnictwa topologicznego jest złożonym problemem w modelowaniu CAD, który wynika ze sposobu, w jaki wewnętrzne procedury programu FreeCAD obsługują aktualizacje kształtów geometrycznych utworzonych za pomocą [jądra OCCT](OpenCASCADE/pl.md). Od wersji FreeCAD 0.19 trwają prace nad poprawą obsługi kształtów w celu zmniejszenia lub wyeliminowania tego typu problemów.

-   Wątek na forum: [Nazewnictwo topologiczne, Moje spojrzenie](https://forum.freecadweb.org/viewtopic.php?t=27278)

Problem nazewnictwa topologicznego najczęściej dotyka i dezorientuje nowych użytkowników programu FreeCAD. W środowisku Projekt Części użytkownik powinien stosować się do najlepszych praktyk omówionych na stronie [Edycja cech](Feature_editing/pl.md). Użycie obiektów [płaszczyzny](PartDesign_Plane/pl.md) oraz [lokalne układy współrzędnych](PartDesign_CoordinateSystem/pl.md) jest zalecane do tworzenia modeli, które nie są podatne na tego typu błędy topologiczne. W środowisku Rysunek Techniczny, użytkownik powinien dodawać wymiary tylko wtedy, gdy model 3D jest kompletny i nie będzie dalej modyfikowany.

## Przykład

1\. W środowisku <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), stwórz <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Zawartość](PartDesign_Body/pl.md), następnie użyj przycisku <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Nowy szkic](PartDesign_NewSketch/pl.md) i wybierz płaszczyznę XY, aby narysować szkic bazowy. Kolejnie zrób <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [wyciągnięcie](PartDesign_Pad/pl.md), aby utworzyć pierwszą bryłę.

<img alt="" src=images/FreeCAD_topological_problem_01_solid.png  style="width:" height="400px;">

2\. Zaznacz górną ścianę poprzedniej bryły, a następnie użyj narzędzia <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Nowy szkic](PartDesign_NewSketch/pl.md), aby narysować kolejny szkic. Kolejnie wykonaj drugie wyciągnięcie.

   
  <img alt="" src=images/FreeCAD_topological_problem_02_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_03_solid_2.png  style="width:" height="400px;">
   

3\. Wybierz górną płaszczyznę poprzedniego wyciągnięcia i ponownie utwórz szkic oraz wyciągnięcie.

<img alt="" src=images/FreeCAD_topological_problem_04_solid_3.png  style="width:" height="400px;">

4\. Teraz kliknij dwukrotnie drugi szkic i zmodyfikuj go tak, aby jego długość przebiegała wzdłuż kierunku X. W ten sposób zostanie odtworzone drugie wyciągnięcie. Trzeci szkic i wyciągnięcie pozostaną w tym samym miejscu.

   
  <img alt="" src=images/FreeCAD_topological_problem_05_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_06_solid_2.png  style="width:" height="400px;">
   

<img alt="" src=images/FreeCAD_topological_problem_07_solid_3.png  style="width:" height="400px;">

5\. Teraz ponownie kliknij dwukrotnie drugi szkic i dopasuj jego punkty tak, aby część z nich znalazła się poza granicami zdefiniowanymi przez pierwsze wyciągnięcie. W ten sposób drugie wyciągnięcie obliczy się poprawnie, ale w [widoku drzewa](Tree_view/pl.md) pojawi się błąd w trzecim wyciągnięciu.

   
  <img alt="" src=images/FreeCAD_topological_problem_08_solid_sketch_2.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_09_solid_2.png  style="width:" height="400px;">
   

![](images/FreeCAD_topological_problem_12_broken_tree.png )

6\. Po uwidocznieniu trzeciego szkicu i wyciągnięcia widać wyraźnie, że obliczanie nowej bryły nie przebiegło poprawnie. Trzeci szkic, zamiast opierać się na górnej powierzchni drugiego wyciągnięcia, pojawia się w dziwnym miejscu, ze swoją normalną skierowaną w kierunku X. Skutkuje to tym, że wyciągnięcie tego szkicu nie jest poprawne, ponieważ wyciągnięcie to byłoby odłączone od reszty <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [zawartości](PartDesign_Body/pl.md) bryły, co jest niedozwolone.

Wydaje się, że problem polega na tym, że gdy zmodyfikowano drugi szkic, nazwa górnej powierzchni drugiego wyciągnięcia została zmieniona z `Face13` na `Face14`. Trzeci szkic jest dołączony do `Face13` tak jak pierwotnie, ale ponieważ ta powierzchnia znajduje się teraz z boku (a nie na górze), szkic podąża za jej orientacją i jest teraz nieprawidłowo umieszczony.

   
  <img alt="" src=images/FreeCAD_topological_problem_10_solid_2_sketch_3.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_11_solid_2_faces.png  style="width:" height="400px;">
   

7\. Aby rozwiązać ten problem, należy ponownie zmapować trzeci szkic do górnej powierzchni. Zaznacz szkic, kliknij wielokropek *(trzy kropki)* obok właściwości **Tryb dołączenia** i ponownie wybierz górną powierzchnię drugiego wyciągnięcia. Wtedy szkic zostanie przeniesiony na wierzch istniejącej bryły, a trzecie wyciągnięcie zostanie wygenerowane bez problemów.

![](images/FreeCAD_topological_problem_13_remap_sketch_2.png )

   
  <img alt="" src=images/FreeCAD_topological_problem_14_solid_2_sketch_3.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_15_solid_3.png  style="width:" height="400px;">
   

Przemapowanie szkicu w ten sposób może być wykonywane za każdym razem, gdy wystąpi błąd nazewnictwa topologicznego, jednak może to być uciążliwe, jeśli model jest skomplikowany i jest wiele takich szkiców, które wymagają korekty.

## Rozwiązanie

![](images/FreeCAD_topological_problem_16_dependency_graph.png )

[Graf zależności](Std_DependencyGraph/pl.md) jest narzędziem, które jest pomocne w obserwowaniu zależności pomiędzy różnymi zawartościami w dokumencie. Użycie oryginalnego przepływu pracy modelowania ujawnia bezpośrednią zależność, jaka istnieje między szkicami a wyciągnięciami. Podobnie jak w przypadku łańcucha, łatwo zauważyć, że ta bezpośrednia zależność będzie podlegała problemom z nazewnictwem topologicznym, jeśli któreś z ogniw sekwencji ulegnie zmianie.

As explained in the [feature editing](feature_editing.md) page, a solution to this problem is to support sketches not on faces but on datum planes which are offset from the main planes of the [PartDesign Body\'s](PartDesign_Body.md) Origin.

1\. Select the origin of the [PartDesign Body](PartDesign_Body.md) and make sure that it is visible. Then select the XY plane, and click on [PartDesign Plane](PartDesign_Plane.md). In the attachment offset dialog, give it an offset in the Z direction so that the datum plane is coplanar with the top face of the first pad.

2\. Repeat the process but this time add a larger offset so that the second datum plane is coplanar with the top face of the second pad.




   
  <img alt="" src=images/FreeCAD_topological_problem_17_datum_plane_1.png  style="width:" height="400px;">   <img alt="" src=images/FreeCAD_topological_problem_18_datum_plane_2.png  style="width:" height="400px;">
   

3\. Select the second sketch, click on the ellipsis next to the **Map Mode** property, and then select the first datum plane. The datum plane is already offset from the body\'s XY plane, so no further Z offset is required for the sketch.

4\. Repeat the process with the third sketch, and select the second datum plane as support. Again, no further Z offset is necessary.

5\. The dependency graph now shows that the sketches and pads are supported by the datum planes. This model is more stable as each sketch can be modified essentially independently from each other.

![](images/FreeCAD_topological_problem_19_dependency_graph_datum_planes.png )

6\. Double click the second sketch and modify the shape. The second pad should update immediately without causing topological problems with the third sketch and the third pad.

<img alt="" src=images/FreeCAD_topological_problem_20_independent_solid_2.png  style="width:" height="400px;">

7\. In fact, every sketch can be modified without interfering with each other\'s pads. As long as the pads have sufficient extrusion length, so that they touch and form a contiguous solid, the entire body will be valid.

<img alt="" src=images/FreeCAD_topological_problem_21_independent_solids_all.png  style="width:" height="400px;">

## Uwagi końcowe 

Adding datum objects is more work for the user but ultimately produces more stable models that are less subject to the topological naming problem.

Naturally, datum objects can be created before any sketches are drawn, and pads are produced. This may be helpful to visualize the approximate shape and dimensions of the final body.

Datum planes can also be based on other datum planes. This creates a chain of dependencies that could also result in topological problems; however, since datum planes are very simple objects, the risks of having these issues is less than if the face of a solid object is used as support.

Datum objects, [points](PartDesign_Point.md), [lines](PartDesign_Line.md), [planes](PartDesign_Plane.md), and [coordinate systems](PartDesign_CoordinateSystem.md), may also be useful as reference geometry, that is, as visual aids to show the important features in the model, even if no sketch is directly attached to them.

## Odnośniki internetowe 

-   [PartDesign Fillet - Topological naming](PartDesign_Fillet#Topological_naming.md)
-   [Topological Naming, My Take](https://forum.freecadweb.org/viewtopic.php?t=27278): a possible solution, by realthunder.
-   [Naming project](Naming_project.md): effort to implement a robust topological naming in FreeCAD.
-   [Topological Naming Project](Topological_Naming_Project.md): idea to solve the problem, by ickby.
-   [Topological data scripting](Topological_data_scripting.md)
-   [Feature editing](Feature_editing.md): contains alternate advice for stable modelling techniques.

## Filmy

-   [Why do my FreeCAD models break? - \"Topological Naming Problem\"](https://youtu.be/6p2vqEEmWq4): A Video explanation of the underlying issues of [Topological naming problem](Topological_naming_problem.md)
-   [FreeCAD Is Fundamentally Broken! - Now what\... Help Me Decide\...](https://www.youtube.com/watch?v=QSsVFu929jo): A Maker Tales Video


 {{TechDraw Tools navi}} {{PartDesign Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [TechDraw](Category_TechDraw.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Topological naming problem/pl
