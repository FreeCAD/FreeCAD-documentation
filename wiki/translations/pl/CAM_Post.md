---
 GuiCommand:
   Name: CAM Post
   Name/pl: CAM: Przetwarzanie końcowe
   MenuLocation: CAM , Przetwarzanie końcowe
   Workbenches: CAM_Workbench/pl
   Shortcut: **P** **P**
---

# CAM Post/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Post.svg  style="width:16px;"> [Przetwarzanie końcowe](CAM_Post/pl.md) eksportuje wybrane <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Zadanie CAM](CAM_Job/pl.md) do pliku G-code.

**Każdy kontroler CNC korzysta ze specyficznego dialektu G-code, co wymaga postprocessora zgodnego z tym dialektem do przetłumaczenia finalnych wyników z wewnętrznego dialektu G-code programu FreeCAD.**



### Typowe funkcje postprocessora obejmują 

-   Użycie poprawnego rozszerzenia pliku wyjściowego G-code dla zadania.
-   Wybór poleceń G-code. Sterowniki CNC zazwyczaj obsługują podzbiór dostępnych poleceń G-code. Pełny zestaw poleceń G-code zawiera zaawansowane i specjalistyczne komendy, które w przeciwnym razie muszą być przetwarzane za pomocą prostszych poleceń. Postprocessory są pisane w celu wybrania najlepszego G-code dla operacji, dostępnego na danej maszynie.
-   Formatowanie składni G-code poprzez uporządkowanie wartości Posuw, X, Y, Z, A i B oraz precyzji.
-   Wstawienie preambuły, aby ustawić jednostki, format jednostek, płaszczyznę roboczą, system współrzędnych itp.
-   Wstawienie postambuły w celu zaparkowania maszyny, zatrzymania jej, przetworzenia argumentów.
-   Wstawienie zmian narzędzi lub ich pominięcie w przypadku kolejnych operacji z użyciem tego samego narzędzia.
-   Formatowanie informacji o prędkości posuwu i obrotów na minutę lub sekundę.
-   Formatowanie nazewnictwa i wywołań funkcji.



### Dostosowywanie postprocessora 

Jeśli chcesz napisać swój własny postprocessor, zobacz stronę [CAM: Dostosowywanie przetwarzania końcowego](CAM_Postprocessor_Customization/pl.md).

**Uwaga:** Kilka zapewnionych postprocessorów generuje odpowiedni kod dla wielu kontrolerów CNC lub może być używanych jako szablony do modyfikacji.

Postprocessory zawierają flagi konfiguracji i są zaprojektowane do dostosowywania poprzez dodawanie kodów G-code i M-code do zapewnionych definicji dla:

-   Inicjalizacji obrabiarki
-   Finalizacji zadania
-   Zmian narzędzi
-   Włączania i wyłączania chłodzenia
-   itd\...

Postprocesory używają [wewnętrznego dialektu G-code programu FreeCAD](CAM_scripting/pl#Wewnętrzny_format_G-code_programu_FreeCAD.md) w połączeniu z definicjami konfiguracji Postprocessora, aby generować G-code zgodny z danym dialektem dla docelowych maszyn. Dzięki temu środowisko pracy CAM we FreeCAD może generować poprawny G-code dla różnych sterowników maszyn CNC, wywołując różne postprocessory.

Typy sterowników maszyn CNC obejmują:

-   Frezarki CNC
-   Tokarki CNC
-   Drukarki 3D
-   Noże wleczone
-   Przecinarki laserowe
-   Maszyny do grawerowania
-   Przecinarki plazmowe
-   Giętarki do drutu
-   Maszyny do cięcia EDM
-   Itp\...

Jeśli używana jest tylko jedna obrabiarka CNC lub wszystkie obrabiarki CNC korzystają ze wspólnego postprocessora, środowisko pracy CAM potrzebuje tylko jednego postprocessora. Jeśli jeden postprocessor nie jest wystarczający do generowania kodu G-code dla wszystkich docelowych sterowników CNC, konieczne jest zainstalowanie wielu postprocessorów.



## Użycie

1.  Wybierz <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Zadanie CAM](CAM_Job/pl.md) w [widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/CAM_Post.svg" width=16px> [Przetwarzanie końcowe](CAM_Post/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_Post.svg" width=16px> Przetwarzanie końcowe** z menu.
    -   Użyj skrótu klawiaturowego: **P** a następnie **P**.
3.  Potwierdź nazwę i katalog dla **Pliku wyjściowego**.



## Opcje

Właściwości pliku wyjściowego i postprocessora mogą zostać ustawione w [Zadaniu](CAM_Job/pl.md) w dowolnej chwili przed wywołaniem postprocessora.

Zapewnione postprocessory są napisane z komentarzami wskazującymi obszary zawierające flagi, zmienne konfiguracyjne i sekcje kodów G-code oraz M-code, które są używane przez postprocessor do konfiguracji danych wyjściowych.

Typowe flagi konfiguracyjne Prawda/Fałsz obejmują:

-   \*\*OUTPUT_COMMENTS\*\* (Prawda = Zezwól, Fałsz = Pomijaj): Służy do wstawiania komentarzy tekstowych w pliku wyjściowym G-code.
-   \*\*OUTPUT_HEADER\*\* (Prawda = Zezwól, Fałsz = Pomijaj): Służy do wstawiania nagłówków tekstowych w pliku wyjściowym G-code.
-   \*\*OUTPUT_LINE_NUMBERS\*\* (Prawda = Zezwól, Fałsz = Pomijaj): Służy do wstawiania numerów linii w pliku wyjściowym G-code.
-   \*\*SHOW_EDITOR\*\* (Prawda = Zezwól, Fałsz = Pomijaj): Służy do wyświetlania wyjściowego kodu G w oknie wyskakującym po uruchomieniu postprocesora.
-   \*\*MODAL\*\* (Prawda = Zezwól, Fałsz = Pomijaj): Służy do redukcji liczby linii wyjściowych G-code poprzez pomijanie informacji o trybie, jeśli tryb się nie zmienia.

Typowe zmienne konfiguracyjne obejmują:

-   \*\*LINENR\*\* (Numer linii): Służy do ustawienia indeksu numeru linii.
-   \*\*UNITS\*\* (G20 lub G21): Używane do jawnego informowania docelowego kontrolera CNC, jakich jednostek używać do interpretacji pliku wyjściowego.
-   \*\*MACHINE_NAME\*\* (Nazwa docelowej frezarki CNC): Służy do wstawiania etykiety z nazwą maszyny w pliku wyjściowym.
-   \*\*PRECISION\*\*: Służy do ustawienia liczby cyfr po przecinku w pliku wyjściowym.

Typowe sekcje konfiguracji obejmują:

-   **PREAMBLE**: Konfiguracja kodu wstawiana na początku zadania.
-   **POSTAMBLE**: Konfiguracja kodu dołączana na końcu zadania, zapewniająca zaparkowanie maszyny, itp.
-   **TOOL_CHANGE**: Kod wstawiany przy każdej zmianie narzędzia w zadaniu.

Opcja **Edycja** → **Preferencje...** → **CAM** → **Preferencje zadania** → **Domyślne** → **CAM** służy do ustawienia domyślnego postprocessora wybranego podczas tworzenia zadania. Umożliwia to skonfigurowanie środowiska pracy CAM tak, aby wyświetlał tylko żądane postprocessory i ustawić domyślny.

Dołączone postprocessory są domyślnie zapisane w lokalizacji **FreeCAD/Mod/CAM/CAM/Post/scripts**:

-   centroid
-   comparams
-   dxf
-   dynapath
-   grbl, łącznie ze wsparciem dla bloków bCNC przy użyciu argumentu zadania \--bcnc
-   jtech (laser)
-   [linuxcnc](http://linuxcnc.org/docs/html/gcode/g-code.html#gcode:g17-g19.1)
-   mach3_mach4
-   nccad
-   opensbp
-   phillips
-   przebudowane\* (te postprocessory są w trakcie tworzenia i będą się znacznie zmieniały)
-   rml
-   smoothie
-   uccnc



## Ograniczenia

-   **Nie** używaj menu **Plik** → **Eksport** do eksportu kodu G-code, powstanie w ten sposób uszkodzony G-code!





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Post/pl
