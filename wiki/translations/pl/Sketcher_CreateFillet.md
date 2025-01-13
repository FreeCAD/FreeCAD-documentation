---
 GuiCommand:
   Name: Sketcher CreateFillet
   Name/pl: Szkicownik: Utwórz zaokrąglenie
   MenuLocation: Szkic , Narzędzia szkicownika , Utwórz zaokrąglenie
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **F** **F**
   SeeAlso: 
---

# Sketcher CreateFillet/pl



## Opis

Narzędzie **Zaokrąglenie** tworzy zaokrąglenie między dwiema nierównoległymi krawędziami. {{Version/pl|1.0}}: Narzędzie może również tworzyć fazę.


{{Version/pl|1.0}}

: Jeśli dwie proste krawędzie połączone [wiązaniem zbieżności](Sketcher_ConstrainCoincident/pl.md) są zaokrąglone lub sfazowane, punkt narożny może opcjonalnie zostać zachowany poprzez dodanie [obiektu punktu](Sketcher_CreatePoint/pl.md), który ma [wiązanie punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) z obiema krawędziami. Wiązania związane z punktem narożnym są następnie przenoszone do nowego obiektu punktu.

![](images/SketcherCreateFilletExample.png‎ )



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów na uruchomienie narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateFillet.svg" width=16px> '''Utwórz zaokrąglenie'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_CreateFillet.svg" width=16px> Utwórz zaokrąglenie**.
    -   Kliknij prawym przyciskiem myszy w widoku 3D i z menu kontekstowego wybierz opcję **<img src="images/Sketcher_CreateFillet.svg" width=16px> Utwórz zaokrąglenie**.
    -   Użyj skrótu klawiaturowego: **G**, **F**, a następnie **F**.
2.  Jeśli istnieje poprzednie zaznaczenie, zostanie wyczyszczone. Narzędzie nie akceptuje wstępnego zaznaczenia.
3.  Kursor zmienia się w krzyżyk z ikoną bieżącego trybu narzędzia.
4.  Sekcja **Parametry zaokrąglenia / sfazowania** ({{Version/pl|1.0}}) zostaje dodana na górze [Okna dialogowego szkicu](Sketcher_Dialog/pl.md).
5.  Opcjonalnie naciśnij klawisz **U** lub odznacz pole wyboru **Zachowaj narożnik**, aby wyłączyć tę opcję. {{Version/pl|1.0}}
6.  Opcjonalnie naciśnij klawisz **M** lub wybierz z listy rozwijanej w sekcji parametrów, aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:16px;"> 
**Zaokrąglenie**
    -   <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:16px;"> 
**Sfazowanie**
7.  Wykonaj jedną z następujących czynności:
    -   Wybierz punkt z wiązaniem [zbieżności](Sketcher_ConstrainCoincident/pl.md), łączący dwa nie równoległe proste krawędzie.
    -   Wybierz dwie nie równoległe krawędzie. Każda krawędź może być prostą [linią](Sketcher_CreateLine/pl.md), [łukiem](Sketcher_CreateArc/pl.md), [łukiem eliptycznym](Sketcher_CreateArcOfEllipse/pl.md), [łukiem hiperbolicznym](Sketcher_CreateArcOfHyperbola/pl.md) lub [łukiem parabolicznym](Sketcher_CreateArcOfParabola/pl.md). [krzywe złożone](Sketcher_Workbench#Sketcher_CompCreateBSpline.md) obecnie nie są obsługiwane.
8.  Zaokrąglenie lub fazka zostanie utworzona, w tym Ścięcie lub rozwarcie obiekt punktu w przypadku zachowanego narożnika. Dla zaokrąglenia utworzony zostanie również konstrukcyjny łuk geometryczny.
9.  Narzędzie to zawsze działa w trybie ciągłym: opcjonalnie kontynuuj wybieranie punktów i / lub krawędzi.
10. Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-   Łuk geometrii konstrukcyjnej fazy nie jest widoczny poza szkicem. Nie można go usunąć bez naruszenia geometrii fazy.
-   Niektóre krzywe *([stożek](Sketcher_Workbench/pl#Sketcher_CompCreateConic.md))* mogą wymagać [przycięcia](Sketcher_Trimming/pl.md) przed ich zaokrągleniem.
-   Promień zaokrąglenia zależy od metody wyboru. Jeśli wybrano [wiązanie zbieżności](Sketcher_ConstrainCoincident/pl.md) łączące dwie proste krawędzie, promień zaokrąglenia jest wyprowadzany z długości najkrótszej krawędzi. Jeśli wybrane są dwie krawędzie, promień jest odległością od pierwszego klikniętego punktu do przecięcia krawędzi *(na przedłużeniu)*.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/pl
