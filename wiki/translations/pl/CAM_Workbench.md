# <img alt="Ikonka FreeCAD dla środowiska pracy CAM" src=images/Workbench_CAM.svg  style="width:64px;"> CAM Workbench/pl






## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [CAM](CAM_Workbench/pl.md) jest używane do tworzenia instrukcji maszynowych dla [maszyn CNC](https://en.wikipedia.org/wiki/CNC_router) z modelu 3D FreeCAD. Instrukcje te wytwarzają rzeczywiste obiekty 3D na maszynach CNC, takich jak frezarki, tokarki, wycinarki laserowe i podobne. Zazwyczaj instrukcje są dialektem [G-code](https://en.wikipedia.org/wiki/G-code). Przedstawiono tu [ogólny przykład symulacji sekwencji ścieżki narzędzia tokarki CNC](https://www.ange-softs.com/SIMULCNCHTML/index.html).

<img alt="" src=images/pathwb.png  style="width:600px;">

Przepływ pracy środowiska FreeCAD CAM tworzy te instrukcje maszynowe w następujący sposób:

-   Model 3D jest obiektem bazowym, zwykle tworzonym przy użyciu jednego lub więcej środowisk pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) lub <img alt="" src=images/Workbench_Draft.svg  style="width:24px;">. [Rysunek Roboczy](Draft_Workbench/pl.md).
-   W środowisku CAM tworzone jest [Zadanie](CAM_Job/pl.md). Zawiera ono wszystkie informacje potrzebne do wygenerowania niezbędnego G-kodu do obróbki zadania na frezarce CNC: jest materiał magazynowy, frezarka ma określony [zestaw narzędzi](CAM_ToolBitLibraryOpen/pl.md) i wykonuje określone polecenia kontrolujące prędkość i ruchy *(zwykle G-kod)*.
-   [Narzędzia](CAM_Tools/pl.md) są wybierane zgodnie z wymaganiami zadania.
-   Ścieżki frezowania są tworzone przy użyciu np. operacji [konturu](CAM_Profile/pl.md) i [kieszeni](CAM_Pocket_3D/pl.md). Te obiekty CAM używają wewnętrznego dialektu G-code FreeCAD, niezależnego od maszyny CNC.
-   Wyeksportuj zadanie z G-kodem, dopasowanym do Twojej maszyny. Ten krok nazywany jest *postprocesowaniem*. Dostępne są różne postprocesory.



## Koncepcje ogólne 

Środowisko pracy CAM generuje G-kod definiujący ścieżki wymagane do frezowania projektu reprezentowanego przez model 3D na docelowej frezarce w [wewnętrznym formacie G-Code programu FreeCAD](CAM_scripting/pl#Wewn.C4.99trzny_format_GCode_programu_FreeCAD.md), który jest następnie tłumaczony na odpowiedni dialekt dla docelowego sterownika CNC poprzez wybór odpowiedniego postprocesora.

G-kod jest generowany na podstawie dyrektyw i operacji zawartych w zadaniu CAM. Obieg zadań zawiera ich listę w kolejności, w jakiej będą wykonywane. Listę tę tworzy się, dodając Operacje CAM, wykończenia CAM, Polecenia uzupełniające CAM i Modyfikacje CAM z menu CAM lub przycisków graficznego interfejsu użytkownika.

Środowisko pracy CAM udostępnia menedżera narzędzi *(bibliotekę, tabelę narzędzi)*, narzędzia do inspekcji G-kodu oraz symulacji. Łączy się z postprocesorem i umożliwia importowanie i eksportowanie szablonów zadań.

Środowisko CAM ma zewnętrzne zależności, w tym:

1.  Jednostki modelu FreeCAD 3D są zdefiniowane w **Edycja → Preferencje ... → Ogólne → Domyślny układ jednostek**. Konfiguracja Postprocesora definiuje jednostki wynikowe G-kodu.
2.  Ścieżka do pliku Makrodefinicji oraz tolerancje geometryczne są zdefiniowane w zakładce **Edycja → Preferencje ... → CAM → Ustawienia dla zadania**.
3.  Kolory są definiowane w zakładce **Edycja → Preferencje ... → CAM → GUI**.
4.  Parametry znaczników trzymania definiuje się w zakładce **Edycja → Preferencje ... → CAM → Wykończenia**.
5.  To, że jakość modelu Base 3D jest zgodna z wymaganiami środowiska CAM, potwierdza sprawdzenie geometrii.



## Ograniczenia

Niektóre z obecnych ograniczeń, o których należy pamiętać, to:

-   Większość narzędzi CAM nie jest prawdziwymi narzędziami 3D, a jedynie 2,5D. Oznacza to, że przyjmują one ustalony kształt 2D i mogą go przyciąć do określonej głębokości. Istnieją jednak dwa narzędzia, które tworzą prawdziwe ścieżki 3D: **<img src="images/CAM_3DPocket.svg" width=24px> [Kieszeń 3D](CAM_Pocket_3D/pl.md)** i **<img src="images/CAM_Surface.svg" width=24px> [Powierzchnia 3D](CAM_Surface/pl.md)** *(która jest wciąż [funkcją eksperymentalną](CAM_experimental/pl.md) od listopada 2020 roku)*.
-   Większość środowiska pracy CAM jest zaprojektowana dla standardowej, prostej, 3-osiowej *(xyz)* frezarki / routera CNC, ale narzędzia tokarskie są w trakcie opracowywania w wersji 0.19_pre.
-   Większość operacji w środowisku pracy CAM zwróci ścieżki oparte tylko na standardowym narzędziu / bicie, niezależnie od typu narzędzia / bita przypisanego w danym kontrolerze narzędzia, z wyjątkiem operacji <img alt="" src=images/CAM_Engrave.svg  style="width:24px;"> [Grawer](CAM_Engrave/pl.md) i <img alt="" src=images/CAM_Surface.svg  style="width:24px;"> [powierzchnia 3D](CAM_Surface/pl.md).
-   Operacje wykonywane w środowisku pracy CAM nie uwzględniają mechanizmów mocujących, które są używane do mocowania modelu na maszynie. W związku z tym przed wysłaniem kodu do maszyny należy przejrzeć i zasymulować generowane ścieżki. Jeśli to konieczne, wymodeluj mechanizmy mocujące w programie FreeCAD, aby lepiej sprawdzić wygenerowane ścieżki. Zwróć uwagę na ewentualne kolizje z zaciskami lub innymi przeszkodami na ścieżkach.



## Jednostki

Obsługa jednostek w środowisku CAM może być myląca. Należy zrozumieć kilka kwestii:

1.  Jednostkami podstawowymi FreeCAD dla długości i czasu są odpowiednio \"mm\" i \"s\". Prędkość jest więc \"mm / s\". To jest to, co FreeCAD przechowuje wewnętrznie, niezależnie od wszystkiego innego.
2.  Domyślny schemat jednostek używa jednostek domyślnych. Jeśli używasz domyślnego schematu i wprowadzasz prędkość posuwu bez łańcucha jednostek, zostanie ona wprowadzona jako \"mm/s\".
3.  Większość maszyn CNC oczekuje prędkości posuwu w postaci \"mm / min\" lub \"in / min\". Większość postprocesorów automatycznie konwertuje jednostkę podczas generowania G-kodu.

Schematy:

1.  Zmiana schematu w preferencjach zmienia domyślny ciąg jednostek dla pól wejściowych. Jeśli jesteś użytkownikiem CAM i wolisz projektować w jednostkach metrycznych, zalecane jest użycie schematu \"Metryczny drobne części i CNC\". Jeśli projektujesz w jednostkach amerykańskich, możesz użyć schematu Calowy dziesiętny lub Budowlany US.
2.  Zmiana preferowanego schematu jednostek nie będzie miała wpływu na wynik, ale pomoże uniknąć błędów przy wprowadzaniu danych.

Wyjście:

1.  Generowanie poprawnej jednostki na wyjściu jest zadaniem postprocesora i jest wykonywane tylko w tym czasie.
2.  Jednostka wyjściowa maszyny jest całkowicie niezwiązana z wybranym przez użytkownika schematem jednostek.
3.  Postprocesory generują dane wyjściowe w systemie metrycznym *(G21)*, imperialnym *(G20)* lub są konfigurowalne.
4.  Konfigurowalne postprocesory domyślnie produkują dane metryczne *(G21)*.
5.  Jeśli chcesz, aby twój konfigurowalny postprocesor generował G-code imperialny *(G20)*, ustaw odpowiedni argument w konfiguracji wyjścia zadania *(np. \--inches dla linuxcnc)*. Można to zapisać w szablonie zadania i ustawić jako szablon domyślny, aby działało to automatycznie dla wszystkich przyszłych zadań.

Inspekcja CAM:

1.  Jeśli użyjesz narzędzia Inspekcja CAM do obejrzenia G-kodu, zobaczysz go w \"mm / s\", ponieważ nie jest on poddawany obróbce postprocesora.



## Wysokość i głębokość 

Wiele poleceń ma zróżnicowaną wysokość i głębokość:

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Wizualne odniesienie do właściwości głębokości ''( ustawienia)''*



## Polecenia

Niektóre polecenia są eksperymentalne i nie są domyślnie dostępne. Aby je włączyć, zobacz stronę [Funkcje eksperymentalne](CAM_experimental/pl.md).



### Polecenia projektu 

-   <img alt="" src=images/CAM_Job.svg  style="width:32px;"> [Zadanie](CAM_Job/pl.md): Tworzy nowe zadanie obróbki CNC.

-   <img alt="" src=images/CAM_Post.svg  style="width:32px;"> [Post Process](CAM_Post/pl.md): Eksportuje projekt do G-kodu.

-   <img alt="" src=images/CAM_Sanity.svg  style="width:32px;"> [Sprawdź, czy zadanie CAM nie zawiera typowych błędów](CAM_Sanity/pl.md): Sprawdza, czy w wybranym zadaniu nie występują brakujące wartości.

-   <img alt="" src=images/CAM_ExportTemplate.svg  style="width:32px;"> [Eksport szablonu](CAM_ExportTemplate/pl.md): Eksportuj aktualne zadanie jako szablon.



### Polecenia narzędzi 

-   <img alt="" src=images/CAM_Inspect.svg  style="width:32px;"> [Przeglądaj polecenia CAM](CAM_Inspect/pl.md): Wyświetla G-kod do weryfikacji.

-   <img alt="" src=images/CAM_Simulator.svg  style="width:32px;"> [ Symulator CAM](CAM_Simulator/pl.md): Przedstawia operację frezowania w sposób, w jaki jest ona wykonywana na maszynie.

-   <img alt="" src=images/CAM_SimulatorGL.svg  style="width:32px;"> [CAM SymulatorGL](CAM_SimulatorGL/pl.md): Uruchamia nowy, ulepszony symulator CAM. {{Version/pl|1.0}}

-   <img alt="" src=images/CAM_SelectLoop.svg  style="width:32px;"> [Zakończ zaznaczanie pętli](CAM_SelectLoop/pl.md): Uzupełnia pętlę na podstawie dwóch wybranych krawędzi.

-   <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:32px;"> [Przełącz aktywność operacji](CAM_OpActiveToggle/pl.md): Aktywuje lub dezaktywuje operację na ścieżce.

-   <img alt="" src=images/CAM_ToolBitLibraryOpen.svg  style="width:32px;"> [Edytor biblioteki narzędzi](CAM_ToolBitLibraryOpen/pl.md): Otwiera edytor do zarządzania bibliotekami końcówek narzędzi.

-   <img alt="" src=images/CAM_ToolBitDock.svg  style="width:32px;"> [Stacja dokująca narzędzi](CAM_ToolBitDock/pl.md): Przełącza stacja dokującą narzędzi.



### Operacje podstawowe 

-   <img alt="" src=images/CAM_Profile.svg  style="width:32px;"> [Profil](CAM_Profile/pl.md): Tworzy operację profilowania całego modelu albo jednej lub kilku wybranych powierzchni lub krawędzi.

-   <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:32px;"> [Kształt kieszeni](CAM_Pocket_Shape/pl.md): Tworzy operację kieszeni z jednej lub kilku wybranych kieszeni.

-   <img alt="" src=images/CAM_Drilling.svg  style="width:32px;"> [Owierty](CAM_Drilling/pl.md): Przeprowadza cykl wiercenia.

-   <img alt="" src=images/CAM_MillFace.svg  style="width:32px;"> [Ściana](CAM_MillFace/pl.md): Tworzy ścieżkę obróbki powierzchni.

-   <img alt="" src=images/CAM_Helix.svg  style="width:32px;"> [Helisa](CAM_Helix/pl.md): Tworzy ścieżkę o kształcie helisy.

-   <img alt="" src=images/CAM_Adaptive.svg  style="width:32px;"> [Algorytm adaptacyjny](CAM_Adaptive/pl.md): Tworzy operację dostosowania oczyszczania i profilowania.

-   <img alt="" src=images/CAM_Slot.svg  style="width:32px;"> [Rowek](CAM_Slot/pl.md): Tworzy operację szczelinowania na podstawie wybranych elementów lub punktów niestandardowych. [**funkcja eksperymentalna**](CAM_experimental/pl.md).

-   <img alt="" src=images/CAM_Engrave.svg  style="width:32px;"> [Grawer](CAM_Engrave/pl.md): Tworzy trasę grawerowania.

-   <img alt="" src=images/CAM_Deburr.svg  style="width:32px;"> [Usuwanie zadziorów](CAM_Deburr/pl.md): Tworzy ścieżkę usuwania zadziorów.

-   <img alt="" src=images/CAM_Vcarve.svg  style="width:32px;"> [Wycięcie V](CAM_Vcarve/pl.md): Tworzy ścieżkę grawerowania przy użyciu kształtu narzędzia V.



### Operacje przestrzenne 

-   <img alt="" src=images/CAM_Pocket_3D.svg  style="width:32px;"> [Kieszeń 3D](CAM_Pocket_3D/pl.md): Tworzy ścieżkę dla kieszeni 3D.

-   <img alt="" src=images/CAM_Surface.svg  style="width:32px;"> [Powierzchnia 3D](CAM_Surface/pl.md): Tworzy ścieżkę dla powierzchni 3D. [**funkcja eksperymentalna**](CAM_experimental/pl.md).

-   <img alt="" src=images/CAM_Waterline.svg  style="width:32px;"> [Linia poziomu](CAM_Waterline/pl.md): Tworzy ścieżkę linii poziomu dla powierzchni 3D. [**Experimental**](CAM_experimental/pl.md).



### Wykończenia ścieżki 

-   <img alt="" src=images/CAM_DressupAxisMap.svg  style="width:32px;"> [Odwzorowanie osi](CAM_DressupAxisMap/pl.md): Odwzorowuje jedną oś na drugą.

-   <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:32px;"> [Kontur](CAM_DressupPathBoundary/pl.md): Dodaje ulepszenie obrysu krawędzi do wybranej ścieżki.

-   <img alt="" src=images/CAM_DressupDogbone.svg  style="width:32px;"> [Nadcięcie w narożnikach](CAM_DressupDogbone/pl.md): Dodaje modyfikację nadcięcia narożników do wybranej ścieżki.

-   <img alt="" src=images/CAM_DressupDragKnife.svg  style="width:32px;"> [Rylec](CAM_DressupDragKnife/pl.md): Dodaje modyfikację dla noża do przeciągania do wybranej ścieżki.

-   <img alt="" src=images/CAM_DressupLeadInOut.svg  style="width:32px;"> [Wprowadzenie / wyprowadzenie](CAM_DressupLeadInOut/pl.md): Dodaje punkt wejścia i / lub wyjścia do wybranej ścieżki.

-   <img alt="" src=images/CAM_DressupRampEntry.svg  style="width:32px;"> [Parkowanie narzędzia](CAM_DressupRampEntry/pl.md): Dodaje modyfikację wejścia na rampę do wybranej ścieżki.

-   <img alt="" src=images/CAM_DressupTag.svg  style="width:32px;"> [Pola mocujące](CAM_DressupTag/pl.md): Dodaje modyfikację mostka przytrzymującego do wybranej ścieżki.

-   <img alt="" src=images/CAM_DressupZCorrect.svg  style="width:32px;"> [Korekta głębokości Z](CAM_DressupZCorrect/pl.md): Koryguje głębokość Z przy użyciu mapowania sondy.



### Polecenia uzupełniające 

-   <img alt="" src=images/CAM_Fixture.svg  style="width:32px;"> [Mocowanie](CAM_Fixture/pl.md): Zmienia położenie uchwytu.

-   <img alt="" src=images/CAM_Comment.svg  style="width:32px;"> [Komentarz](CAM_Comment/pl.md): Wstawia komentarz do G-kodu ścieżki.

-   <img alt="" src=images/CAM_Stop.svg  style="width:32px;"> [Stop](CAM_Stop/pl.md): Wstawia instrukcję pełnego zatrzymania maszyny.

-   <img alt="" src=images/CAM_Custom.svg  style="width:32px;"> [Wstawka Gcode](CAM_Custom/pl.md): Wstawia G-kod użytkownika.

-   <img alt="" src=images/CAM_Probe.svg  style="width:32px;"> [Sonda](CAM_Probe/pl.md): Tworzy siatkę pomiarową z zasobu zadania.

-   <img alt="" src=images/CAM_Shape.svg  style="width:32px;"> [G-kod z kształtu](CAM_Shape/pl.md): Tworzy obiekt ścieżki z wybranego obiektu części. [**funkcja eksperymentalna**](CAM_experimental/pl.md).



### Modyfikacja ścieżki 

-   <img alt="" src=images/CAM_Copy.svg  style="width:32px;"> [Kopia](CAM_Copy/pl.md): Tworzy parametryczną Kopię wybranego obiektu ścieżki.

-   <img alt="" src=images/CAM_Array.svg  style="width:32px;"> [Szyk](CAM_Array/pl.md): Tworzy szyk przez powielanie wybranej ścieżki.

-   <img alt="" src=images/CAM_SimpleCopy.svg  style="width:32px;"> [Szybka kopia](CAM_SimpleCopy/pl.md): Tworzy nieparametryczną kopię wybranego obiektu ścieżki.



### Operacje specjalistyczne 

-   <img alt="" src=images/CAM_ThreadMilling.svg  style="width:32px;"> [Frezowanie gwintów](CAM_ThreadMilling/pl.md): Tworzy operację CAM frezowania gwintów na podstawie cech obiektu bazowego. [**funkcja eksperymentalna**](CAM_experimental/pl.md).



### Różności

-   <img alt="" src=images/CAM_Area.svg  style="width:32px;"> [Obszar](CAM_Area/pl.md): Tworzy obszar charakterystyczny z wybranych obiektów. [**funkcja eksperymentalna**](CAM_experimental/pl.md).

-   <img alt="" src=images/CAM_Area_Workplane.svg  style="width:32px;"> [Obszar płaszczyzny roboczej](CAM_Area_Workplane/pl.md): Tworzy płaszczyznę roboczą obszaru cechy. [**funkcja eksperymentalna**](CAM_experimental/pl.md).



## Noże tokarskie, architektura 

Umożliwia zarządzanie narzędziami, nożami tokarskimi i biblioteką narzędzi. Oparte na architekturze noży tokarskich.

-   [Narzędzia](CAM_Tools/pl.md)
-   [Profil narzędzia](CAM_ToolShape/pl.md)
-   [Noże tokarskie](CAM_ToolBit/pl.md)
-   [Biblioteka narzędzi](CAM_ToolBit_Library/pl.md)
-   [Kontroler narzędzi](CAM_ToolController/pl.md)



## Pozostałe

-   [Często zadawane pytania](CAM_FAQ/pl.md): Środowisko CAM ma wiele wspólnych koncepcji z innymi pakietami oprogramowania CAM, ale ma też swoje własne cechy szczególne. Jeśli coś wydaje się nie tak, to jest to dobre miejsce, aby zacząć.
-   [Karta konfiguracji](CAM_SetupSheet/pl.md): Można użyć arkusza ustawień, aby dostosować sposób obliczania różnych wartości właściwości dla operacji.
-   [Dostosowywanie przetwarzania końcowego](CAM_Postprocessor_Customization/pl.md): Jeśli masz specjalną maszynę, która nie może używać jednego z dostępnych postprocesorów, może być konieczne napisanie własnego postprocesora.
-   [Oś czwarta](CAM_fourth_axis/pl.md): Eksperymentalne frezowanie w czterech osiach.



## Ustawienia

-   <img alt="" src=images/Preferences-cam.svg  style="width:32px;"> [Ustawienia](CAM_Preferences/pl.md): Preferencje dostępne dla środowiska pracy CAM.



## Tworzenie skryptów 

Zobacz również: [skrypty dla środowiska Path](CAM_scripting/pl.md)



## Poradniki

-   [opis dla niecierpliwych](CAM_Walkthrough_for_the_Impatient/pl.md): krótki samouczek pozwalający zapoznać się ze środowiskiem pracy CAM.



## Filmy

-   [FreeCAD Path: Niestandardowe ścieżki z Pythonem - część 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): lista odtwarzania z serią 5 filmów w języku angielskim autorstwa Sliptonic. Seria ta pokazuje, jak pracować ze środowiskiem [CAM](CAM_Workbench/pl.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): lista odtwarzania z serią 7 filmów w języku angielskim przygotowana przez CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ): lista odtwarzania z serią 8 filmów w języku angielskim przygotowana przez CAD CAM Lessons.
-   Zobacz również sekcję [Wytwarzanie wspomagane komputerowo (CAM)](Video_tutorials/pl#Wytwarzanie_wspomagane_komputerowo_(CAM).md) na stronie [Wideo poradniki](Video_tutorials/pl.md).



## Plan rozwoju 

-   [CAM Development Roadmap](CAM_Development_Roadmap.md): Przeczytaj ten artykuł, jeśli jesteś programistą i chcesz przyczynić się do rozwoju środowiska CAM.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [CAM](Category_CAM.md) > CAM Workbench/pl
