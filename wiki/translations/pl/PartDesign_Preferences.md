# PartDesign Preferences/pl
{{TOCright}}

## Wprowadzenie

Środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Część](Part_Workbench/pl.md) oraz <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [Projekt części](PartDesign_Workbench/pl.md) używają tych samych preferencji. Można je znaleźć w <img alt="" src=images/Preferences-part_design.svg  style="width   *24px;"> sekcji [Edytora ustawień](Preferences_Editor/pl.md) **Projekt Części**. Sekcja ta będzie dostępna tylko wtedy, gdy w bieżącej sesji programu FreeCAD załadowano jedno z tych środowisk pracy.

## Dostępne ustawienia 

Dostępne są cztery zakładki   * Ogólne, Widok kształtu, Wygląd kształtu i Wymiarowanie.

### Ogólne

W zakładce **Ogólne** można zdefiniować następujące parametry   *

+++
| Nazwa                                                                                  | Opis                                                                                                                                                                                                                                      |
+========================================================================================+===========================================================================================================================================================================================================================================+
|                                                                         | Jeśli opcja jest zaznaczona, [reprezentacja granicy](https   *//en.wikipedia.org/wiki/Boundary_representation) *(BRep)* modelu jest [weryfikowana](Part_CheckGeometry/pl.md) po [operacjach logicznych](Part_Boolean/pl.md). |
| **Automatycznie sprawdź model po zakończeniu operacji logicznej**          |                                                                                                                                                                                                                                           |
|                                                                                     |                                                                                                                                                                                                                                           |
+++
|                                                                         | Jeśli opcja jest zaznaczona, model zostanie [udoskonalony](Part_RefineShape/pl.md) po zakończeniu [operacji logicznej](Part_Boolean/pl.md).                                                                               |
| **Automatycznie udoskonal model po wykonaniu operacji logicznej.**         |                                                                                                                                                                                                                                           |
|                                                                                     |                                                                                                                                                                                                                                           |
+++
|                                                                         | Jeśli opcja jest zaznaczona, model zostanie [udoskonalony](Part_RefineShape/pl.md) po wprowadzeniu zmian do źródłowych szkiców obiektów.                                                                                          |
| **Automatycznie udoskonal model po wykonaniu operacji opartej na szkicu.** |                                                                                                                                                                                                                                           |
|                                                                                     |                                                                                                                                                                                                                                           |
+++

![](images/Preferences_Part_design_Tab_General.png )

### Widok kształtu 

W zakładce *Widok kształtu* można zdefiniować następujące parametry   *

+++
| Nazwa                                                                                | Opis                                                                                                                                                                                                                                 |
+======================================================================================+======================================================================================================================================================================================================================================+
|                                                                       | Maksymalne [odchylenie liniowe](https   *//www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) [teselowanych](#Tesselacja.md) obiektów od ich powierzchni.                 |
| **Maksymalne dopuszczalne odchylenie w zależności od ramki otaczającej** |                                                                                                                                                                                                                                      |
|                                                                                   |                                                                                                                                                                                                                                      |
+++
|                                                                       | Maksymalne [odchylenie kątowe](https   *//www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) od jednej sekcji [teselowanego](#Tesselacja.md) obiektu do następnej sekcji. |
| **Maksymalne odchylenie kątowe**                                         |                                                                                                                                                                                                                                      |
|                                                                                   |                                                                                                                                                                                                                                      |
+++

![](images/Preferences_Part_design_Tab_Shape_view.png )

### Wygląd kształtu 

W zakładce *Wygląd kształtu* można zdefiniować następujące parametry   *

+++
| Nazwa                                    | Opis                                                                                                                                                                                                                                                                   |
+==========================================+========================================================================================================================================================================================================================================================================+
|                           | Barwa dla nowych kształtów. Jeśli aktywna jest opcja **Losowy**, wówczas stosowany jest losowy kolor.                                                                                                                                        |
| **Kolor kształtu**           |                                                                                                                                                                                                                                                                        |
|                                       |                                                                                                                                                                                                                                                                        |
+++
|                           | Przezroczystość dla nowych kształtów {{Version/pl|1.0}}.                                                                                                                                                                                                 |
| **Przezroczystość kształtu** |                                                                                                                                                                                                                                                                        |
|                                       |                                                                                                                                                                                                                                                                        |
+++
|                           | Barwa linii dla nowych kształtów.                                                                                                                                                                                                                                      |
| **Kolor linii**              |                                                                                                                                                                                                                                                                        |
|                                       |                                                                                                                                                                                                                                                                        |
+++
|                           | Grubość linii dla nowych kształtów.                                                                                                                                                                                                                                    |
| **Szerokość linii**          |                                                                                                                                                                                                                                                                        |
|                                       |                                                                                                                                                                                                                                                                        |
+++
|                           | Barwa nadawana nowym [wierzchołkom](Glossary/pl#V.md).                                                                                                                                                                                                         |
| **Kolor wierzchołka**        |                                                                                                                                                                                                                                                                        |
|                                       |                                                                                                                                                                                                                                                                        |
+++
|                           | Rozmiar nadawany nowym [wierzchołkom](Glossary/pl#V.md).                                                                                                                                                                                                       |
| **Rozmiar wierzchołka**      |                                                                                                                                                                                                                                                                        |
|                                       |                                                                                                                                                                                                                                                                        |
+++
|                           | Barwa [ramki otaczającej](Property_editor/pl#Widok.md) w oknie widoku 3D.                                                                                                                                                                                      |
| **Kolor ramki otaczającej**  |                                                                                                                                                                                                                                                                        |
|                                       |                                                                                                                                                                                                                                                                        |
+++
|                           | IJeśli opcja jest zaznaczona, barwa wewnętrznej strony powierzchni będzie taka sama jak zewnętrznej. Jeśli nie jest zaznaczona, będzie używany [kolor podświetlenia](Preferences_Editor/pl#Widok_3D.md), jeśli jest włączony, lub będzie używany kolor czarny. |
| **Rendering dwustronny**     |                                                                                                                                                                                                                                                                        |
|                                       |                                                                                                                                                                                                                                                                        |
+++
|                           | Kolor tekstu w adnotacjach na dokumentach. Obecnie nie ma okna dialogowego umożliwiającego dodawanie adnotacji do dokumentów. Adnotacje można dodawać wyłącznie za pomocą poleceń w konsoli Python   *                                                                    |
| **Kolor tekstu**             |                                                                                                                                                                                                                                                                        |
|                                       | obj = App.ActiveDocument.addObject("App   *   *Annotation", "Label")                                                                                                                                                                                                       |
|                                          |                                                                                                                                                                                                                                                                        |
|                                          | Konsole można aktywować w menu **Widok → Panele → konsola Python**.                                                                                                                                                                          |
+++

![](images/Preferences_Part_design_Tab_Shape_appearance.png )

### Pomiary

Te preferencje kontrolują wygląd miar utworzonych za pomocą narzędzi [Pomiaru](Part_Module/pl#Pomiary.md) dostępnych w środowiskach pracy [Część](Part_Workbench/pl.md) i [Projekt Części](PartDesign_Workbench/pl.md).

W zakładce **Wymiarowanie** *({{Version/pl|1.0}})* można wybrać następujące narzędzia   *

+++
| Nazwa                               | Opcje                                                               |
+=====================================+=====================================================================+
|                      | Kolor dla wymiarów liniowych 3D.                                    |
| **kolor w widoku 3D**   |                                                                     |
|                                  |                                                                     |
+++
|                      | Kolor dla wymiarów delta *(równolegle do globalnych osi X, Y i Z)*. |
| **kolor Delta**         |                                                                     |
|                                  |                                                                     |
+++
|                      | Kolor dla wymiarów kątowych.                                        |
| **kolor ką↑tów**        |                                                                     |
|                                  |                                                                     |
+++
|                      | Rozmiar fontów w pikselach.                                         |
| **Rozmiar czcionki**    |                                                                     |
|                                  |                                                                     |
+++
|                      | Jeśli opcja jest zaznaczona, używany jest pogrubiony styl czcionki. |
| **Bold**                |                                                                     |
|                                  |                                                                     |
+++
|                      | Jeśli opcja jest zaznaczona, używany jest pochylony styl czcionki.  |
| **Italic**              |                                                                     |
|                                  |                                                                     |
+++
|                      | Czcionka do użycia.                                                 |
| **Nazwa czcionki**      |                                                                     |
|                                  |                                                                     |
+++
|                      | Naciśnij ten przycisk, aby zaktualizować istniejące miary.          |
| **Odśwież istniejące miary** |                                                                     |
|                                  |                                                                     |
+++

![](images/Preferences_Part_design_Tab_Measure.png )

## Tesselacja

W celu efektywnego wyświetlania obiektu jego powierzchnia jest [tesselowana](https   *//en.wikipedia.org/wiki/Tessellation_(computer_graphics)), tzn. jest wyświetlana z pewnymi niewielkimi odchyleniami od jego rzeczywistej powierzchni. Dotyczy to nie tylko modeli środowiska Projekt Części, ale także innych obiektów w programie FreeCAD.

Dolna granica teselacji wynosi 0,01%. Jeśli naprawdę chcesz poświęcić dodatkowy czas, możesz jeszcze bardziej zmniejszyć dolną granicę, otwierając menu **Przybory → Edycja parametrów ...**. Otworzy to edytor parametrów, gdzie przechodzimy do **BaseApp → Preferences → Mod → Part**.

Kliknij prawym przyciskiem myszy na pozycji **Mesh deviation** i wybierz z menu kontekstowego **Zmień wartość elementu**. Ustaw wartość na wybraną minimalną teselację. Należy pamiętać, że wartość podawana jest w %, tzn. dla wartości 0,005% należy wpisać \"0,00005\". Najmniejsza możliwa wartość to 1e-7. **Uwaga   *** W menu preferencji nadal będzie widoczna wartość 0,01%, nawet jeśli ustawisz niższą wartość.





{{PartDesign Tools navi

}} 

[Category   *Preferences](Category_Preferences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/pl
