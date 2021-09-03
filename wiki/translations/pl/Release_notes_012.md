To jest podsumowanie najbardziej interesujących zmian, które nastąpiły we FreeCAD-zie w odniesieniu do poprzedniej wersji.Pełną listę zmian znajdziesz [tutaj](http://www.freecadweb.org/tracker/changelog_page.php).

Starsze wersje: [0.11](Release_notes_011.md)

### Witaj!

-   Gdy otwierasz FreeCAD po raz pierwszy, jesteś witany całkowicie nowym centrum startowym, które zawiera najbardziej popularne czynności jak: otwarcie określonego warsztatu (workbench), załadowanie ostatnio edytowanych plików, przegląd niusów z prac nad FreeCAD-em czy oglądanie jenego z wielu nowych wideotutoriali stworzonych niedawno przez heroiczną społeczność FreeCAD-a.

![](images/FreeCAD_start_center.jpg )

### Sketcher i PartDesign 

<img alt="" src=images/Rim_bling.png  style="width:800px;">

-   Warsztatowi [Szkicownika (Sketcher)](Sketcher_Workbench.md) poświęcono wiele pracy od czasu ostatniego wydania. Obecnie posiada on nowy solver zaprojektowany specjalnie do tego zadani. Szkicownik potrafi obecnie wykonać większość operacji rysunku 2D [modułu Draft](Draft_Workbench.md), wraz z szeroką gamą więzów dla elementów szkicu.

-   Dodatkowo, [ Warsztat PartDesign](PartDesign_Workbench.md) również znacznie ewoluował i obecnie posiada wiele popularnych (i w pełni parametrycznych) narzędzi do pracy na bazie szkiców jak wyciąganie (extrusion), przeciąganie (lofting) czy obracanie (revolution).

### Architektura

-   Nowy [moduł Architektury](Arch_Workbench.md) jest obecnie częścią FreeCAD-a. Jest on wciąż we wczesnej fazie budowy, ale już teraz posiada garść podręcznych obiektów pomocniczych jak ściany czy elementy struktury (słupy i belki). Mogą być one zbudowane na bazie istniejącej geometrii 2D, jak linie, przewody (wires) czy szkice, przez podanie szerokości i wysokości lub, dla elementów struktury, na bazie profili 2D. Mogą one także bazować na bryłąch lub nawet zawierać inne bryły jako dodanie lub odjęcie, pozwalając wirtualnie na dowolną geometrię.

![](images/Arch_screenshot.jpg )

-   Moduł Arch posiada także importer [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes), importer i exporter [DAE (collada)](http://en.wikipedia.org/wiki/Collada) i specjalny eksporter [OBJ](http://en.wikipedia.org/wiki/Wavefront_.obj_file) bardziej dopasowany do modeli architektonicznych niż standardowy eksporter.

-   W module Arch zawarto także rosnącą kolekcję narzędzi do łatwiejszej pracy z obiektami Siatki (Mesh) pobranymi z innego oprogramowania jak [Blender](http://www.blender.org). Siatki, jeśli są dobrze zamodelowane, mogą być łatwo i automatycznie zamienione w \"czyste\" kształty i potem w parametryczne obiekty Arch.

### 2D Drafting 

![](images/Draft_taskview.jpg )

-   Odzyskaj swoją przestrzeń roboczą! Moduł Draft posiada obecnie nowy tryb interfejsu użytkownika, który używa systemu FreeCAD Task, zbierającego całą interakcję w jedno miejcie, uwalniając cenne miejsce pożerane wcześniej przez pasek narzędzi Draft.

-   Narzędzie Draft Przytnij/Rozszerz (Trim/Extend) pozwala obecnie wyciągać pojedyncze ściany z istniejących obiektów.

-   Zostało dodanych kilka nowych trybów przyciągania, pozwalając obecnie na na przyciąganie prostopadłe lub równoległe do istniejących linii i znajdowanie pozycji w których są wyrównanie do innych linii.

-   Moduł Draft posiada nowe narzędzie, które tworzy, wewnątrz tego samego dokumentu, rzutowany widok 2D istniejącego kształtu 3D.

-   Obiekty Draft mogą być teraz rysowane na powierzchni istniejących ścian. Jeśli nie wskażesz płaszczyzny roboczej tymczasowo zostanie wykorzystania ściana leżąca poniżej.

-   Moduł draft potrafi teraz importować krzywe Béziera z plików SVG.


{{languages/pl | {{en|Release_notes_012}} {{es|Release_notes_012/es}} {{fr|Release_notes_012/fr}} {{it|Release_notes_012/it}} {{ru|Release_notes_012/ru}} }}

[Category:News{{\#translation:}}](Category:News.md) [Category:Documentation{{\#translation:}}](Category:Documentation.md) [Category:Releases{{\#translation:}}](Category:Releases.md)
