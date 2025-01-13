# PartDesign Preferences/pl
## Wprowadzenie

Środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) oraz <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt części](PartDesign_Workbench/pl.md) używają tych samych preferencji. Można je znaleźć w [Edytorze preferencji](Preferences_Editor/pl.md). W menu wybierz **Edycja → Preferencje...** a następnie **<img src="images/Preferences-part_design.svg" width=16px> Część/Projekt Części**. Ta grupa jest widoczna tylko gdy jedno z tych środowisk pracy zostało załadowane w bieżącej sesji programu FreeCAD.

Niektóre zaawansowane preferencje mogą być zmienione tylko w [Edytorze parametrów](Std_DlgParameter/pl.md). Zobacz stronę [Dostrajanie parametrów](Fine-tuning/pl#środowisko_pracy_Projekt_Części.md).

Ta strona została zaktualizowana do wersji 1.0.



## Dostępne ustawienia 

Dostępne są trzy strony: [Ogólne](#Ogólne.md), [Widok kształtu](#Widok_kształtu.md) i [Wygląd kształtu](#Wygląd_kształtu.md).



### Ogólne

<img alt="" src=images/Preferences_PartDesign_Page_General.png  style="width:400px;">

Na tej stronie można określić następujące parametry:

+++
| Nazwa                                                                                          | Opis                                                                                                                                                                                                                                      |
+================================================================================================+===========================================================================================================================================================================================================================================+
|                                                                                 | Jeśli opcja jest zaznaczona, [reprezentacja granicy](https://en.wikipedia.org/wiki/Boundary_representation) *(BRep)* modelu jest [weryfikowana](Part_CheckGeometry/pl.md) po [operacjach logicznych](Part_Boolean/pl.md). |
| **Automatycznie sprawdź model po zakończeniu operacji logicznej**                  |                                                                                                                                                                                                                                           |
|                                                                                             |                                                                                                                                                                                                                                           |
+++
|                                                                                 | Jeśli opcja jest zaznaczona, model zostanie [udoskonalony](Part_RefineShape/pl.md) po zakończeniu [operacji logicznej](Part_Boolean/pl.md).                                                                               |
| **Automatycznie udoskonal model po wykonaniu operacji logicznej.**                 |                                                                                                                                                                                                                                           |
|                                                                                             |                                                                                                                                                                                                                                           |
+++
|                                                                                 | Jeśli opcja jest zaznaczona, model zostanie [udoskonalony](Part_RefineShape/pl.md) po wprowadzeniu zmian do źródłowych szkiców obiektów.                                                                                          |
| **Automatycznie udoskonal model po wykonaniu operacji opartej na szkicu.**         |                                                                                                                                                                                                                                           |
|                                                                                             |                                                                                                                                                                                                                                           |
+++
|                                                                                 | Jeśli zaznaczone, obiekty Zawartość mogą mieć wiele oddzielnych brył. {{Version/pl|1.0}}                                                                                                                                    |
| **Zezwalaj domyślnie na wiele brył w środowisku Projekt Części (eksperymentalne)** |                                                                                                                                                                                                                                           |
|                                                                                             |                                                                                                                                                                                                                                           |
+++



### Widok kształtu 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_view.png  style="width:400px;">

Na tej stronie można określić następujące parametry:

+++
| Nazwa                                                                                | Opis                                                                                                                                                                                                                                 |
+======================================================================================+======================================================================================================================================================================================================================================+
|                                                                       | Maksymalne [odchylenie liniowe](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) [teselowanych](#Tesselacja.md) obiektów od ich powierzchni.                 |
| **Maksymalne dopuszczalne odchylenie w zależności od ramki otaczającej** |                                                                                                                                                                                                                                      |
|                                                                                   |                                                                                                                                                                                                                                      |
+++
|                                                                       | Maksymalne [odchylenie kątowe](https://www.opencascade.com/doc/occt-7.3.0/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_11_2) od jednej sekcji [teselowanego](#Tesselacja.md) obiektu do następnej sekcji. |
| **Maksymalne odchylenie kątowe**                                         |                                                                                                                                                                                                                                      |
|                                                                                   |                                                                                                                                                                                                                                      |
+++



### Wygląd kształtu 

<img alt="" src=images/Preferences_PartDesign_Page_Shape_appearance.png  style="width:400px;">

Wyjaśnienie kolorów można znaleźć [tutaj](Part_ColorPerFace/pl#Użycie.md).

Na tej stronie można określić następujące parametry:

+++
| Nazwa                                              | Opis                                                                                                                                                                                                                                                                   |
+====================================================+========================================================================================================================================================================================================================================================================+
|                                     | Kolor rozproszony dla nowych kształtów. Jeśli ustawiona jest opcja **Losowo**, używany jest przypadkowy kolor zamiast tego.                                                                                                                  |
| **Kolor kształtu**                     |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Kolor otoczenia dla nowych kształtów. {{Version/pl|1.0}}                                                                                                                                                                                                 |
| **Kolor kształtu otoczenia**           |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Kolor emisji dla nowych kształtów. {{Version/pl|1.0}}                                                                                                                                                                                                    |
| **Kolor emisji kształtu**              |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Kolor odbicia dla nowych kształtów. {{Version/pl|1.0}}                                                                                                                                                                                                   |
| **Kolor odbicia kształtu**             |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Przezroczystość dla nowych kształtów {{Version/pl|0.21}}.                                                                                                                                                                                                |
| **Przezroczystość kształtu**           |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Połysk dla nowych kształtów. {{Version/pl|1.0}}                                                                                                                                                                                                          |
| **Połysk kształtu**                    |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Barwa linii dla nowych kształtów.                                                                                                                                                                                                                                      |
| **Kolor linii**                        |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Grubość linii dla nowych kształtów.                                                                                                                                                                                                                                    |
| **Szerokość linii**                    |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Barwa nadawana nowym [wierzchołkom](Glossary/pl#V.md).                                                                                                                                                                                                         |
| **Kolor wierzchołka**                  |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Rozmiar nadawany nowym [wierzchołkom](Glossary/pl#V.md).                                                                                                                                                                                                       |
| **Rozmiar wierzchołka**                |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Barwa [ramki otaczającej](Property_editor/pl#Widok.md) w oknie widoku 3D.                                                                                                                                                                                      |
| **Kolor ramki otaczającej**            |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Rozmiar czcionki [ramek otaczających](Property_editor/pl#Widok.md) w widoku 3D. {{Version/pl|1.0}}                                                                                                                                               |
| **Rozmiar czcionki ramki otaczającej** |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | IJeśli opcja jest zaznaczona, barwa wewnętrznej strony powierzchni będzie taka sama jak zewnętrznej. Jeśli nie jest zaznaczona, będzie używany [kolor podświetlenia](Preferences_Editor/pl#Widok_3D.md), jeśli jest włączony, lub będzie używany kolor czarny. |
| **Rendering dwustronny**               |                                                                                                                                                                                                                                                                        |
|                                                 |                                                                                                                                                                                                                                                                        |
+++
|                                     | Kolor tekstu dla nowych adnotacji w dokumentach.                                                                                                                                                                                                                       |
| **Kolor tekstu**                       |                                                                                                                                                                                                                                                                        |
|                                                 | Obecnie te adnotacje można dodać tylko przy pomocy [konsoli Pythona](Python_console/pl.md):                                                                                                                                                                    |
|                                                    |                                                                                                                                                                                                                                                                        |
|                                                    | obj = App.ActiveDocument.addObject("App::Annotation", "Label")                                                                                                                                                                                                       |
+++



## Teselacja

W celu efektywnego wyświetlania obiektu jego powierzchnia jest [teselowana](https://pl.wikipedia.org/wiki/Teselacja), tzn. jest wyświetlana z pewnymi niewielkimi odchyleniami od jego rzeczywistej powierzchni. Dotyczy to nie tylko modeli środowiska Projekt Części, ale także innych obiektów w programie FreeCAD.

Dolna granica teselacji wynosi 0,01%. Jeśli naprawdę chcesz poświęcić dodatkowy czas, możesz jeszcze bardziej zmniejszyć dolną granicę, otwierając [Edytor parametrów](Std_DlgParameter/pl.md).

W edytorze parametrów przejdź do **BaseApp → Preferences → Mod → Part**, kliknij prawym przyciskiem myszy na pozycji **Mesh deviation** i wybierz z menu kontekstowego **Zmień wartość elementu**. Ustaw wartość na wybraną minimalną teselację. Należy pamiętać, że wartość podawana jest w %, tzn. dla wartości 0,005% należy wpisać \"0,00005\". Najmniejsza możliwa wartość to 1e-7. Zauważ, że w [Edytorze preferencji](Preferences_Editor/pl.md) nadal będzie widoczna wartość 0,01%, nawet jeśli ustawiłeś niższą wartość.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Preferences/pl
