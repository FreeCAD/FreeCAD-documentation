# Draft Constrain/pl
{{TOCright}}

## Opis

Oprócz wprowadzania współrzędnych lub używania [przyciągania](Draft_Snap/pl.md), istnieje funkcja zwana wiązaniem, która pomaga w dokładnym rysowaniu w <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) i <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Architektura](Arch_Workbench/pl.md). Dla każdego kolejnego punktu możesz ograniczyć ruch kursora do kierunku X, Y, lub Z układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md). Można to wykorzystać na przykład do stworzenia idealnie pionowej linii.

Wiązania są dostępne z większością poleceń środowisk [Rysunek Roboczy](Draft_Workbench/pl.md) i [Architektura](Arch_Workbench/pl.md).

![](images/Draft_Constrain_taskpanel_example.png ) 
*Gdy kursor jest związany, panel zadań blokuje wartości, które nie są modyfikowane.*

## Używanie wiązań poziomych i pionowych 

1.  Wybierz środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md) do utworzenia geometrii.
2.  Wybierz pierwszy punkt. Wymagany jest poprzedni punkt.
3.  Wykonaj jedną z następujących czynności:
    -   Dla wiązania poziomego: przesuń kursor w lewo lub w prawo od poprzedniego punktu.
    -   W przypadku wiązania pionowego: przesuń kursor powyżej lub poniżej poprzedniego punktu.
4.  Przytrzymaj wciśnięty klawisz **Shift**.
5.  Kursor jest teraz związany.
6.  Wybierz następny punkt.
7.  Jeśli polecenie jest nadal aktywne: opcjonalnie zwolnij klawisz **Shift**, aby wyłączyć blokadę.
8.  Zawsze zwalniaj klawisz **Shift** po zakończeniu wykonywania polecenia.

## Używanie wiązania X, Y, Z 

1.  Wybierz środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md) do utworzenia geometrii.
2.  Wybierz pierwszy punkt. Wymagany jest poprzedni punkt.
3.  Wciśnij klawisz **X**, **Y** lub **Z** by określić kierunek.
4.  Kursor jest teraz związany.
5.  Wybierz następny punkt.
6.  Jeśli polecenie jest nadal aktywne, opcjonalnie wykonaj jedną z poniższych czynności:
    -   Naciśnij ten sam klawisz, aby wyłączyć ograniczenie.
    -   Naciśnij jeden z dwóch pozostałych klawiszy, aby zmienić kierunek wiązania.
7.  Wiązania X, Y i Z są automatycznie wyłączane po zakończeniu polecenia.

## Uwagi

-   Wiązanie może być połączone z [przyciąganiem](Draft_Snap/pl.md).
-   Polecenia [Odsunięcie](Draft_Offset/pl.md) i [Przytnij](Draft_Trimex/pl.md) środowiska pracy Rysunek Roboczy, używają innego typu wiązania, mianowicie ograniczenia operacji do pewnego segmentu.

## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Preferencje](Draft_Preferences/pl.md).

-   Domyślny klawisz **modyfikujący**, **Shift**, można zmienić w menu: **Edycja → Preferencje → Rysunek Roboczy → Siatka i przyciąganie → Przyciąganie → Modyfikator ograniczania**.
-   Skróty klawiszowe **X**, **Y** i **Z** można zmienić: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia interfejsu użytkownika → Skróty poleceń**.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Constrain/pl
