# Migrating to FreeCAD from Fusion360/pl
## Kontekst

Ta strona jest przeznaczona dla użytkowników, którzy są zainteresowani migracją do FreeCAD ze świata Fusion 360.



## Co powinienem zrobić? 

1.  Pierwszą rzeczą, którą należy zrobić, jest usunięcie plików z zastrzeżonych formatów i pamięci masowej. Zacznij od wyeksportowania modeli z chmury na komputer lokalny.
    -   Popularną metodą jest użycie skryptu [Fusion360 total exporter](https://github.com/Jnesselr/fusion-360-total-exporter).
2.  Zalecamy eksport do formatu STEP.

## Słowniczek


**Prosimy również o odniesienie się do trwających prac w ramach projektu [CAD Rosetta Stone](CAD_Rosetta_Stone.md), aby poznać analogiczne nazwy, których używają popularne, komercyjne programy CAD.**

Odnieś się ogólnie do strony [słowniczka](Glossary/pl.md), ale tutaj znajduje się krótka lista konkretnych terminów, które użytkownicy F360 mogą uznać za szczególnie pomocne:

-   Tangent constraint - forma FreeCAD **Wiązania współliniowego**. Zobacz informacje na stronie <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Wiązanie styczności](Sketcher_ConstrainTangent/pl#Pomiędzy_dwoma_liniami_(współliniowe).md).
-   Pad - funkcja **wyciągnięcia** w programie FreeCAD. Przeczytaj dokumentację na stronie <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [Wyciągnij](PartDesign_Pad/pl.md), aby dowiedzieć się więcej.
-   Toponaming - skrót od [Problem Nazewnictwa Topologicznego](Topological_naming_problem/pl.md). Bardzo dobrze omówiony w [klipie youtube Brodiego Fairhalla](https://www.youtube.com/watch?v=6p2vqEEmWq4)\].
--   



## Najczęściej zadawane pytania 

1.  Jakie formaty obsługuje FreeCAD?
    -   Natywnym formatem pliku w FreeCAD jest BREP, [boundary representation](https://en.wikipedia.org/wiki/Boundary_representation), dostarczany przez wewnętrzne jądro geometrii [OpenCASCADE *(OCCT)*](OpenCASCADE/pl.md).
    -   FreeCAD obsługuje wszystkie formaty obsługiwane przez OCCT, więc przynajmniej STEP i IGES.
2.  Jakich formatów powinienem użyć do migracji do FreeCAD?
    -   STEP jest najlepszym formatem, ponieważ jest to format bryłowy [kształtu](Shape/pl.md), w przeciwieństwie do [siatki](Mesh/pl.md) *(STL, OBJ, DAE)*. Przykład [Importowanie formatu Step z kolorami](https://forum.freecadweb.org/viewtopic.php?f=3&t=50308).
    -   Importowanie STL jest możliwe, ale ten format siatki będzie trudny do dalszej modyfikacji. Zalecamy konwertowanie zaimportowanych siatek na bryły przy użyciu **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Utwórz kształt z siatki](Part_ShapeFromMesh/pl.md)**. Najlepszą radą jest przemodelowanie obiektu w programie FreeCAD, używając siatki jako odniesienia.



## Wskazówki

-   \@MPetrika ([twitter](https://twitter.com/MPetrikas/status/1362051484704264198)) zaleca zainstalowanie [Środowisko pracy Nowoczesny UI](ModernUI_Workbench/pl.md) autorstwa HakanSeven12.



## Zasoby dydaktyczne 

-   [Fusion360 do FreeCAD - wprowadzenie](https://www.youtube.com/watch?v=_GxJkB23ZHM), wideo autorstwa Brodie Fairhall.
-   [Fusion360 do FreeCAD - część 2](https://www.youtube.com/watch?v=IESZD4QS3P8), wideo autorstwa Brodiego Fairhalla.
-   [V0.19 Benchmarking\--2019 Monthly Challenges](https://forum.freecadweb.org/viewtopic.php?f=36&t=50492), seria obiektów stworzonych w Fusion360 jest przebudowywana za pomocą FreeCAD, przez doświadczonego użytkownika ppemawm.
-   [Pisemny poradnik dla początkujących: od pierwszej części do rysunku technicznego](https://github.com/macdroid53/LearningFreeCAD) autorstwa macdroid53.
-   [Zasoby online dla użytkowników FreeCAD](https://www.freecad.info/).



## Filmy porównawcze 

-   [Modelowanie turbiny sprężarki w programach FreeCAD i Fusion360](https://www.youtube.com/watch?v=kirDbZd0dvI&feature=youtu.be)



## Pomoc

Czy na tej stronie wiki czegoś brakuje. Złóż prośbę o [dostęp do Wiki](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) na forum, aby edytować tę stronę.



## Powiązane

-   [Migracja z OnShape do FreeCAD](Migrating_to_FreeCAD_from_OnShape/pl.md)



---
⏵ [documentation index](../README.md) > Migrating to FreeCAD from Fusion360/pl
