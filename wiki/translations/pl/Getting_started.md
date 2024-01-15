# Getting started/pl
## Przedmowa

FreeCAD jest aplikacją typu 3D [parametric modeling application](About_FreeCAD/pl.md). Został stworzony przede wszystkim do projektowania mechanicznego. Może służyć również do wszystkich pokrewnych zastosowań, w których trzeba precyzyjnie modelować obiekty przestrzenne. Dodatkowo zapewnia kontrolę nad historią modelowania.

Freecad jest już rozwijany od 2002 roku i oferuje sporą listę [funkcjonalności](Feature_list/pl.md). Niektórych z nich wciąż brakuje, w porównaniu z komercyjnymi rozwiązaniami. Jednak w zupełności spełnia wymagania hobbystów i osób pracujących z mniejszymi projektami. Na [forum](http://forum.freecadweb.org/index.php) możesz znaleźć naszą szybko rozwijającą się społeczność zaangażowaną w rozwój programu FreeCAD. [Tutaj](https://forum.freecadweb.org/viewforum.php?f=24) możesz znaleźć wiele wartościowych przykładowych projektów dla FreeCAD. Zobacz również, [FreeCAD używany w produkcji](FreeCAD_used_in_production.md).

Jak wszystkie wolne projekty, projekt FreeCAD jest uzależniony od swojej społeczności, aby się rozwijać, zdobywać funkcje i stabilizować *(usuwać błędy)*. Więc nie zapominaj o tym podczas używania programu FreeCAD. Jeśli ci się to podoba, możesz dokonać [darowizny](Donate/pl.md) i [wspomóc FreeCAD](Help_FreeCAD/pl.md) również na inne sposoby, takie jak tworzenie dokumentacji i tłumaczeń.

Zobacz również:

-   [Migracja z Fusion360 do FreeCAD](Migrating_to_FreeCAD_from_Fusion360/pl.md)
-   [Które środowisko pracy wybrać?](Which_workbench_should_I_choose.md)
-   [Poradniki](Tutorials/pl.md)
-   [Wideo poradniki](Video_tutorials/pl.md)



## Instalacja

Przede wszystkim pobierz i zainstaluj FreeCAD. Informacje na temat aktualnych wersji i aktualizacji oraz instrukcje instalacji dla danego systemu operacyjnego *([Linux](Installing_on_Linux/pl.md), [Mac OS](Installing_on_Mac/pl.md) lub [Windows](Installing_on_Windows/pl.md))*.FreeCAD jest dostępny w menedżerach pakietów wielu dystrybucji Linuksa. Ponieważ FreeCAD jest oprogramowaniem typu open-source, można również pobrać kod źródłowy i [skompilować](Compiling/pl.md) go samodzielnie.



## Poznawaj interfejs użytkownika 

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">



*Standardowy interfejs FreeCAD.*


**zobacz szczegółową prezentację [Interface](Interface/pl.md).**


:   1\. Obszar widoku [głównego](main_view_area.md), który może zawierać różne okna z zakładkami, głównie [widok 3D](3D_view.md).
:   2\. [Widok 3D](3D_view/pl.md), pokazujący obiekty geometryczne w dokumencie.
:   3\. [Widok drzewa](Tree_view/pl.md) jest *(częścią [widoku złożonego](combo_view/pl.md))*, pokazuje hierarchię i historię budowy obiektów w dokumencie. Może również wyświetlać [panel zadań](Task_panel/pl.md) dla aktywnych poleceń.
:   4\. [Edytor właściwości](Property_editor/pl.md) jest \'\'(częścią [widoku złożonego](combo_view/pl.md)), który pozwala na przeglądanie i modyfikowanie właściwości wybranych obiektów.
:   5\. Widok [wyboru](Selection_view/pl.md), który wskazuje wybrane obiekty lub elementy składowe obiektów *(wierzchołki, krawędzie, powierzchnie)*.
:   6\. Okno [widok raportu](Report_view/pl.md) *(lub okno wyjściowe)*, w którym wyświetlane są komunikaty, ostrzeżenia i błędy.
:   7\. [Konsola Python](Python_console/pl.md), gdzie są wyświetlane wszystkie wykonywane polecenia i gdzie można wprowadzić kod [Python](Python/pl.md).
:   8\. [Pasek statusu](status_bar.md), to szczególne miejsce gdzie pojawiają się niektóre komunikaty i podpowiedzi.
:   9\. Obszar paska narzędzi, gdzie dokowane są paski narzędzi.
:   10\. Okienko umożliwiające wybór [Środowisk pracy](Std_Workbench/pl.md), dla wykonania zamierzonych prac stosownych dla kązdego ze [Środowisk pracy](workbenches/pl.md).
:   11\. [Standardowe menu](Standard_Menu/pl.md), które zawiera zbiór podstawowych funkcji programu.

Główna koncepcja interfejsu FreeCAD opiera się na tym, że jest on podzielony na [środowiska pracy](Workbenches/pl.md). Każde z nich jest zbiorem narzędzi dostosowanych do realizacji konkretnych zadań, takich jak praca z [siatkami](Mesh_Workbench/pl.md), lub rysowanie [obiektów 2D](Draft_Workbench/pl.md), lub [związanymi szkicami](Sketcher_Workbench/pl.md). Możesz przełączyć bieżące środowisko pracy za pomocą [okna wyboru](Std_Workbench/pl.md). Możesz [dostosowywać ustawienia](Interface_Customization/pl.md) narzędzi zawartych w każdym środowisku pracy, dodawać narzędzia z innych środowisk. Możliwe jest również dodanie narzędzi utworzonych samodzielnie, które nazywamy [makrodefinicjami](macros/pl.md) *(w skrócie makro)*. Najczęściej stosowanymi narzędziami bazowymi są środowiska [Projekt Części](PartDesign_Workbench/pl.md) i [Część](Part_Workbench/pl.md).

Kiedy uruchamiasz FreeCAD po raz pierwszy, zobaczysz stronę startową. Oto jak to wygląda dla wersji **0.19**:

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">

Strona startowa pozwala na szybkie przejście do jednego z najchętniej używanych Środowisk pracy, otwarcie jednego z ostatnich plików lub zobaczenie najnowszych wiadomości ze świata FreeCAD. Możesz zmienić domyślne środowisko pracy w [Edytorze preferencji](Preferences_Editor/pl.md).



### Nawigacja w przestrzeni 3D 

FreeCAD udostępnia kilka różnych [trybów nawigacji](Mouse_navigation/pl.md), które zmieniają sposób używania myszy do interakcji z obiektami w widoku 3D i samego widoku. Jedna z nich została stworzona specjalnie dla [touchpad](Mouse_navigation/pl#Touchpad.md), gdzie środkowy przycisk myszy nie jest używany. Domyślnym trybem nawigacji jest [CAD](Mouse_navigation#CAD.md). Możesz szybko zmienić aktualny tryb nawigacji za pomocą przycisku **[<img src=images/NavigationCAD_dark.svg style="width:24px">** na [Pasku statusu](Status_bar/pl.md) lub klikając prawym przyciskiem myszy pusty obszar okna [widoku 3D](3D_view/pl.md).

W menu Widok, na pasku narzędzi Widok oraz za pomocą skrótów klawiaturowych (**1**, **2** itp\...) dostępnych jest również kilka ustawień widoku *(widok z góry, widok z przodu itp.)*. Klikając obiekt prawym przyciskiem myszki lub pusty obszar widoku 3D, masz szybki dostęp do niektórych typowych operacji, takich jak ustawianie konkretnego widoku lub wyszukiwanie obiektu w widoku drzewa.



## FreeCAD pierwsze kroki 

FreeCAD został zaprojektowany do tworzenia precyzyjnych modeli 3D, ścisłą kontrolę nad tymi modelami *(możliwość cofnięcia się w historii modelowania i zmiany parametrów)*, a w końcu na budowanie tych modeli *(poprzez wydruk w technologii 3D i obróbkę numeryczną CNC lub nawet budowę obiektu budowlanego)*.
W związku z tym bardzo różni się on od innych aplikacji 3D stworzonych do innych celów, takich jak film animowany czy gry. Jego nauka może być bardzo trudna, zwłaszcza jeśli jest to Twój pierwszy kontakt z modelowaniem 3D. Jeśli w którymś momencie staniesz się zaskoczony, nie zapominaj, że przyjazna społeczność użytkowników na forum [FreeCAD forum](http://forum.freecadweb.org/index.php) może być w stanie wyciągnąć cię z tarapatów w mgnieniu oka.

Środowisko pracy, z którego zaczniesz korzystać w FreeCAD, zależy od rodzaju pracy, którą musisz wykonać: Jeśli zamierzasz pracować na modelach mechanicznych lub ogólnie na małych obiektach, prawdopodobnie będziesz chciał wypróbować środowisko [Projekt Części](PartDesign_Workbench/pl.md). Jeśli pracujesz w trybie 2D, przejdź do środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), jeśli potrzebne Ci są określone wymagania. Jeśli chcesz pracować z modelami BIM, uruchom środowisko [Architektura](Arch_Workbench/pl.md). A jeśli pochodzisz ze świata OpenSCAD, wypróbuj Środowisko pracy [OpenSCAD](OpenSCAD_Workbench/pl.md). Dostępnych jest również wiele [zewnętrznych środowisk](External_workbenches/pl.md) opracowanych przez społeczność.

Możesz przełączać Środowisko pracy w dowolnym momencie, a także [dostosować ustawienia](Interface_Customization/pl.md), aby dodać narzędzia z innych Środowisk pracy.



## Pracujemy w PartDesign i Sketcher 

Środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md) służy do budowania złożonych obiektów, począwszy od prostych kształtów i dodawania lub usuwania elementów *(zwanych \" cechami\")*, aż do osiągnięcia ostatecznego wyglądu projektowanego detalu. Wszystkie funkcje zastosowane w procesie modelowania są przechowywane w oddzielnym widoku zwanym [widok drzewa](Document_structure/pl.md), który zawiera również inne obiekty w dokumencie. Obiekt środowiska Projekt Części może być traktowany jako kolejna operacja, z których każda odnosi się do wyniku poprzedniej, tworząc jeden duży łańcuch. W widoku drzewa widzisz swój obiekt końcowy, ale możesz go rozwinąć i przeglądać wszystkie poprzednie stany oraz zmienić dowolny z ich parametrów, które automatycznie aktualizują obiekt końcowy.

Projekt Części mocno bazuje na innym środowisku pracy, [Szkicownik](Sketcher_Workbench/pl.md). Szkicownik umożliwia rysowanie kształtów 2D, które są definiowane przez zastosowanie ograniczeń dla kształtu płaskiego. Na przykład, możesz narysować prostokąt i dodać wymiar boku, stosując ograniczenie długości jednego z boków. Nie można już zmieniać rozmiaru tego boku *(chyba że ograniczenie zostanie zmienione)*.

Te kształty 2D wykonane za pomocą szkicownika są często używane w środowisku pracy PartDesign, na przykład do tworzenia objętości 3D. Używane są też do rysowania obszarów na ścianach obiektów, które następnie zostaną wydrążone z ich głównej objętości. Jest to typowy schemat pracy PartDesign:

1.  Stwórz nowy szkic.
2.  Narysuj zamknięty kształt *(upewnij się, że wszystkie punkty wierzchołków są połączone)*.
3.  Zakończ szkicowanie.
4.  Rozszerz szkicu w bryłę 3D przy użyciu narzędzia wyciągnięcia *(pad)*.
5.  Wybierz jedną ścianę bryły.
6.  Utwórz drugi szkic *(tym razem zostanie on narysowany na wybranej powierzchni)*.
7.  Narysuj zamknięty kształt.
8.  Zamknij szkic.
9.  Stwórz kieszeń z drugiego szkicu, na pierwszym obiekcie.

Oto przykład efektu tego ćwiczenia:

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

W każdej chwili możesz wybrać oryginalne szkice i zmodyfikować je lub zmienić parametry wytłaczania operacji pad lub pocket, co spowoduje że obiekt końcowy zostanie poddany aktualizacji.



## Praca z Draft i Arch 

Środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) i [Architektura](Arch_Workbench/pl.md) zachowują się nieco inaczej niż pozostałe omówione powyżej. Chociaż przestrzegają tych samych zasad, które są wspólne dla wszystkich we FreeCAD. Krótko mówiąc, podczas gdy Szkicownik i Projekt Części są stworzone przede wszystkim do projektowania pojedynczych elementów, Draft i Arch są stworzone, aby ułatwić pracę z kilkoma prostszymi obiektami.

Środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) oferuje narzędzia 2D nieco podobne do tych, które można znaleźć w tradycyjnych aplikacjach 2D CAD, takich jak [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). Jednakże, ponieważ szkic 2D jest daleki od celu twórców programu FreeCAD, nie oczekuj, że znajdziesz tam pełen wachlarz narzędzi, które oferują te dedykowane aplikacje. Większość narzędzi Draft działa nie tylko w płaszczyźnie 2D, ale także w pełnej przestrzeni 3D i korzysta ze specjalnych systemów pomocniczych, takich jak [płaszczyzny robocze](Draft_SelectPlane/pl.md) i [przyciąganie](Draft_Snap/pl.md).

Środowisko pracy [Architektura](Arch_Workbench/pl.md) dodaje narzędzia [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) do FreeCAD, pozwalając na tworzenie modeli architektonicznych zawierających obiekty parametryczne. Środowisko pracy Architektura opiera się w dużym stopniu na innych modułach, takich jak Rysunek Roboczy i Szkicownik. Wszystkie narzędzia do tworzenia szkiców są również obecne w środowisku pracy Architektura, większość narzędzi architrktonicznych korzysta z systemów pomocniczych środowiska Rysunek Roboczy.

Typowy tok pracy z Arch i Draft może wyglądać następująco:

1.  Narysuj kilka linijek przy pomocy narzędzia *\'Draft Line*.
2.  Wybierz każdą linię i naciśnij narzędzie do tworzenia ścian *(Wall)* na każdej z nich.
3.  Dołącz poszczególne linie do ściany wybierając je i naciskając narzędzie **Arch Add**.
4.  Utwórz obiekt podłogi i przenieś ściany, na ta pozycję w widoku drzewa.
5.  Utwórz okno, klikając narzędzie Okno *(Window)*, wybierz ustawienia w jego panelu, a następnie kliknij na wybraną ścianę.
6.  Dodaj wymiary, najpierw ustawiając płaszczyznę roboczą jeśli to konieczne, a następnie użyj narzędzia **Draft Dimension**, aby zdefiniować głębokość osadzenia.

Przykład efektu tego ćwiczenia:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">

Więcej informacji znajdziesz na stronie [Poradniki](Tutorials/pl.md).



## Dodatki, Makrodefinicje i zewnętrzne Środowiska pracy 

FreeCAD, jako oprogramowanie open source, oferuje możliwość uzupełnienia swoich Środowisk pracy o dodatki.

Zasada [Dodatki](Addon.md) opiera się na opracowaniu uzupełnienia Środowiska pracy. Każdy użytkownik może opracować funkcję, której mu brakuje dla własnych potrzeb lub, ostatecznie, dla społeczności. Za pośrednictwem forum, użytkownik może poprosić o opinię, lub pomoc. Może udostępniać, lub nie, obiekt swojej pracy zgodnie z regułami praw autorskich, *(po ich zdefiniowaniu)*. Bezpłatnie dla niej/niego. Do rozwoju, użytkownik ma dostępne funkcje [skrypty](scripting/pl.md).

Istnieją dwa rodzaje dodatków:

1.  [Makrodefinicje](Macros/pl.md): krótkie fragmenty kodu Pythona, które zapewniają nowe narzędzie lub funkcjonalność. Makra zazwyczaj są uruchamiane jako sposób na uproszczenie lub zautomatyzowanie zadania rysowania lub edycji konkretnego obiektu. Jeśli wiele z tych makrodefinicji jest zbieranych w jednym katalogu, cały katalog może być dystrybuowany jako nowe Środowisko pracy.
2.  [Zewnętrzne środowiska pracy](External_workbenches/pl.md): zbiór narzędzi zaprogramowanych w Pythonie lub C++, które rozszerzają FreeCAD w istotny sposób. Jeśli dany stół pracy został wystarczająco rozwinięty i jest dobrze udokumentowany, może zostać włączony do FreeCAD jako jeden z podstawowych stołów roboczych. W sekcji [Zewnętrzne Środowiska pracy](External_workbenches/pl.md) można znaleźć listę i wytyczne dla istniejących bibliotek.



## Tworzenie skryptów 

I na końcu, jedną z najpotężniejszych cech FreeCAD jest środowisko [skryptowe](scripting/pl.md). Ze zintegrowanej konsoli Pythona *(lub dowolnego innego zewnętrznego skryptu Pythona)*, możesz uzyskać dostęp do prawie każdej części FreeCAD. Możesz tworzyć lub modyfikować geometrię, modyfikować reprezentację obiektów w scenie 3D lub dostęp i modyfikować interfejs FreeCAD. Skrypty Pythona mogą być również używane w [makrodefinicjach](macros/pl.md), które zapewniają łatwą metodę tworzenia własnych poleceń.



## Co nowego 

-   Szczegółową listę funkcji można znaleźć w [uwagach do wydania](Feature_list/pl#Uwagach_do_wydania.md).





{{Userdocnavi/pl}}



---
⏵ [documentation index](../README.md) > Getting started/pl
