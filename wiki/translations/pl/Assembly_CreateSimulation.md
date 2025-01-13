---
 GuiCommand:
   Name: Assembly CreateSimulation
   Name/pl: Złożenie: Utwórz symulację
   MenuLocation: Złożenie , Utwórz symulację
   Workbenches: Assembly_Workbench/pl
   Shortcut: **S**
   Version: 1.1
   SeeAlso: 
---

# Assembly CreateSimulation/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateSimulation.svg  style="width:24px;"> [Utwórz symulację](Assembly_CreateSimulation/pl.md) tworzy symulację bieżącego złożenia.



## Użycie

1.  Upewnij się, że złożenie jest aktywne.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateSimulation.svg" width=16px> [Utwórz symulację](Assembly_CreateSimulation/pl.md)**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_CreateSimulation.svg" width=16px> Utwórz symulację** z menu.
    -   Użyj skrótu klawiaturowego: **S**.
3.  Jeśli nie ma jeszcze obiektu Simulations: kontener Simulations zostanie dodany do aktywnego złożenia.
4.  Obiekt Simulation zostanie dodany do kontenera Simulations.
5.  Otwarty zostanie [panel zadań](Task_panel/pl.md) **Utwórz symulację**.
6.  Wciśnij przycisk z zielonym plusem aby otworzyć okno dialogowe.
    -   Wybierz jedno połączenie z listy.
    -   Jeśli to konieczne, wybierz Typ Ruchu.
    -   Opcjonalnie edytuj Równanie.
    -   Wciśnij przycisk **OK** aby zamknąć okno dialogowe.
7.  Opcjonalnie dostosuj ustawienia Symulacji.
8.  Wciśnij przycisk **Generuj**.
9.  Sekcja **Odtwarzacz Animacji** zostanie dodana do panelu zadań.
    -   Użyj widżetów odtwarzacza aby animować złożenie.
10. Wciśnij przycisk **OK** aby zakończyć działanie narzędzia i zamknąć panel zadań.



## Uwagi

-   Nienazwane okno dialogowe pomaga zdefiniować siłownik:
    1.  Wybierz żądane połączenie z listy **Połączenia**.
    2.  Jeśli z wybranym połączeniem jest dostępna więcej niż jedna transformacja, wybierz jedną z listy **Typ Ruchu**.
    3.  Edytuj równanie opisujące zależność między upływem czasu a sterowanym kątem/odległością.
    4.  Opcjonalnie naciśnij przycisk Pomoc, aby zobaczyć przykłady opisów **Równania**.
-   W Równaniu **czas** wydaje się reprezentować 1 radian na sekundę, a przy 360° = 6,283 radianów dla pełnego obrotu możemy zrobić jedno z poniższych:
    -   Wprowadź {{Value|6.283 * czas}} w polu Równanie i ustaw czas trwania (wartość końcowa - wartość początkowa) na jedną sekundę w ustawieniach symulacji w panelu zadań.
    -   Wprowadź {{Value|1 * czas}} w polu Równanie i ustaw czas trwania (wartość końcowa - wartość początkowa) na 6,283 sekundy w ustawieniach symulacji w panelu zadań.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).



### Symulacje

Kontener **Simulations** jest obiektem {{Incode|Assembly::SimulationGroup}}, który wywodzi się z obiektu [App DocumentObjectGroup](App_DocumentObjectGroup/pl.md) i dziedziczy wszystkie jego właściwości. Nie ma żadnych dodatkowych właściwości.



### Symulacja

Obiekt **Simulation** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Ma też następujące dodatkowe właściwości:



#### Dane


{{Properties_Title|Podstawowe}}

-    **Group|LinkList**: Obiekty Ruchu obiektu.

-    **_ Group Touched|Bool|hidden**:


{{Properties_Title|Symulacja}}

-    **a Czas początkowy|Czas**: Domyślnie {{value|0,0 s}}. Czas rozpoczęcia symulacji.

-    **b Czas końcowy|Czas**: Domyślnie {{value|4,0 s}}. Czas zakończenia symulacji.

-    **c Krok czasowy wyjściowy|Czas**: Domyślnie {{value|0,01 s}}. Krok czasowy symulacji dla wyjścia.

-    **f Globalna tolerancja błędu|Float**: Domyślnie {{value|1e-06}}. Globalna tolerancja błędu integracji.

-    **j Liczba klatek na sekundę|Integer**: Domyślnie {{value|30}}. Liczba klatek na sekundę.



### Widok


{{Properties_Title|Space}}

-    **Decimals|Integer**: Domyślna wartość to {{value|9}}. Liczba miejsc dziesiętnych dla obliczanych tekstów.



### Ruch

Obiekt **Motion** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Ma też następujące dodatkowe właściwości:



#### Dane 


{{Properties_Title|Ruch}}

-    **Równanie|String**: Równanie ruchu. Na przykład {{Value|1.0*czas}}.

-    **Połączenie|XLinkSubHidden**: Połączenie poruszane przez ruch.

-    **Typ Ruchu|Enumeration**: Typ ruchu. Opcje to: {{Value|Kątowy}} i {{Value|Liniowy}}.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateSimulation/pl
