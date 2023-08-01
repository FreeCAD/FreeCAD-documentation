# Release notes 0.12/pl
To jest podsumowanie najbardziej interesujących zmian, które miały miejsce w programie FreeCAD w odniesieniu do poprzedniej wersji. Pełną listę zmian znajdziesz na stronie [Mantis changelog](http://www.freecadweb.org/tracker/changelog_page.php).

Starsze wersje: [0.11](Release_notes_0.11/pl.md)

### Witaj!

-   Gdy otwierasz FreeCAD po raz pierwszy, jesteś witany całkowicie nowym centrum startowym, które zawiera najbardziej popularne czynności jak: otwarcie określonego warsztatu (workbench), załadowanie ostatnio edytowanych plików, przegląd niusów z prac nad FreeCAD-em czy oglądanie jenego z wielu nowych wideotutoriali stworzonych niedawno przez heroiczną społeczność FreeCAD-a.

![](images/FreeCAD_start_center.jpg )

### Skzkicownik i Projekt Części 

<img alt="" src=images/Rim_bling.png  style="width:800px;">

-   Środowisku pracy [Szkicownika (Sketcher)](Sketcher_Workbench/pl.md) poświęcono wiele uwagi od czasu ostatniego wydania. Obecnie posiada on nowy solver zaprojektowany specjalnie do tego zadani. Szkicownik potrafi obecnie wykonać większość operacji rysunku 2D [modułu Draft](Draft_Workbench.md), wraz z szeroką gamą więzów dla elementów szkicu.

-   Dodatkowo, środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md) również znacznie ewoluowało i obecnie posiada wiele popularnych *(i w pełni parametrycznych)* narzędzi do pracy na bazie szkiców jak wyciąganie *(extrusion)*, przeciąganie *(lofting)* czy obracanie *(revolution)*.

### Architektura

-   Nowy [moduł Architektury](Arch_Workbench/pl.md) jest obecnie częścią programu FreeCAD. Jest on wciąż we wczesnej fazie budowy, ale już teraz posiada garść podręcznych obiektów pomocniczych jak ściany czy elementy struktury (słupy i belki). Mogą być one zbudowane na bazie istniejącej geometrii 2D, jak linie, przewody (wires) czy szkice, przez podanie szerokości i wysokości lub, dla elementów struktury, na bazie profili 2D. Mogą one także bazować na bryłach lub nawet zawierać inne bryły jako dodanie lub odjęcie, pozwalając wirtualnie na dowolną geometrię.

![](images/Arch_screenshot.jpg )

-   Moduł Architektura posiada także importer [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes), importer i exporter [DAE *(collada)*](http://en.wikipedia.org/wiki/Collada) i specjalny eksporter [OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file) bardziej dopasowany do modeli architektonicznych niż standardowy eksporter.

-   W module Arch zawarto także rosnącą kolekcję narzędzi do łatwiejszej pracy z obiektami Siatki *(Mesh)* pobranymi z innego oprogramowania jak [Blender](http://www.blender.org). Siatki, jeśli są dobrze wymodelowane, mogą być łatwo i automatycznie zamienione w \"czyste\" kształty i potem w parametryczne obiekty Arch.

### 2D Drafting 

![](images/Draft_taskview.jpg )

-   Odzyskaj swoją przestrzeń roboczą! Moduł Draft posiada obecnie nowy tryb interfejsu użytkownika, który używa systemu FreeCAD Task, zbierającego całą interakcję w jedno miejcie, uwalniając cenne miejsce pożerane wcześniej przez pasek narzędzi Draft.

-   Narzędzie Draft Przytnij / Rozszerz *(Trim / Extend)* pozwala obecnie wyciągać pojedyncze ściany z istniejących obiektów.

-   Zostało dodanych kilka nowych trybów przyciągania, pozwalając obecnie na na przyciąganie prostopadłe lub równoległe do istniejących linii i znajdowanie pozycji w których są wyrównanie do innych linii.

-   Moduł Draft posiada nowe narzędzie, które tworzy, wewnątrz tego samego dokumentu, rzutowany widok 2D istniejącego kształtu 3D.

-   Obiekty Draft mogą być teraz rysowane na powierzchni istniejących ścian. Jeśli nie wskażesz płaszczyzny roboczej tymczasowo zostanie wykorzystania ściana leżąca poniżej.

-   Moduł draft potrafi teraz importować krzywe Béziera z plików SVG.


{{languages/pl | {{en|Release_notes_0.12}} {{es|Release_notes_0.12/es}} {{fr|Release_notes_0.12/fr}} {{it|Release_notes_0.12/it}} {{ru|Release_notes_0.12/ru}} }}



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.12/pl
