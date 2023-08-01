---
- GuiCommand:
   Name:Part Fillet
   Name/pl:Część: Zaokrąglenie
   MenuLocation:Część → Zaokrąglenie ...
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Sfazowanie](Part_Chamfer/pl.md)
---

# Part Fillet/pl



## Opis

Narzędzie to tworzy łuk *(zaokrąglenie)* na wybranych krawędziach kształtu. Okno dialogowe pozwala wybrać, na których obiektach i na których krawędziach należy pracować.



## Użycie

Wywołaj narzędzie z paska narzędzi Część lub z menu **Część → Zaokrąglenie**. Przed wywołaniem narzędzia można wybrać kształt.

-   Jeśli kształt nie został wybrany przed uruchomieniem narzędzia, wybierz go z rozwijanej listy kształt w [panelu zadań](Task_panel/pl.md).
-   Wybierz typ zaokrąglenia, albo stały promień *(domyślnie)*, albo zmienny promień.
-   Wybierz krawędzie albo w oknie [widoku 3D](3D_view/pl.md), albo zaznaczając je na liście krawędzi w [panelu zadań](Task_panel/pl.md).
-   Ustaw wartość promienia.
-   Kliknij przycisk **OK**, aby zatwierdzić.

![](images/Dialog-fillet.png )

## Zaokrąglenie w środowisku Część kontra Zaokrąglenie w środowisku Projekt Części 

W środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md) znajduje się inne narzędzie do tworzenia zaokrągleń. Należy pamiętać, że ich działanie jest zupełnie inne. Sprawdź stronę <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> [Projekt Części: Zaokrąglenie](PartDesign_Fillet/pl.md) zawierającą więcej szczegółów na temat różnic między nimi.

## Uwagi dotyczące stosowania funkcji zaokrąglenia w Środowisku Part 

Part Filet może nie zrobić nic, jeśli wynikiem będzie dotknięcie lub przekroczenie następnej przyległej krawędzi. Jeśli więc nie otrzymasz oczekiwanego wyniku, spróbuj z mniejszą wartością **Promienia**. To samo dotyczy <img alt="" src=images/Part_Chamfer.svg  style="width:24px;"> [fazek](Part_Chamfer/pl.md).

Narzędzie do zaokrąglania czasem zawodzi przy próbie zaokrąglenia złożonych kształtów. Częstą przyczyną może być to, że kształt, który jest poddawany operacjom zaokrąglania nie jest geometrycznie poprawny. Może to wynikać z nieusunięcia linii / płaszczyzn itp. po wcześniejszych operacjach użytych do skonstruowania kształtu *(np. Wytnij / Przeciągnij / Fuzja)*. W celu zminimalizowania problemów można zastosować kilka kroków:

-   Tam, gdzie to możliwe, pozostawić wypełnianie części do czasu, aż część zostanie całkowicie wygenerowana. Zminimalizuje to interakcję pomiędzy operacjami zaokrąglania a kolejnymi operacjami logicznymi.
-   Użyj polecenia **Część → Sprawdź geometrię**, aby sprawdzić, czy geometria kształtu nie zawiera błędów i skorygować ją.
-   Użyj polecenia **Część → Utwórz kopię → Udoskonal kształt** aby usunąć wszelkie artefakty wprowadzone przez poprzednie operacje logiczne przed wypełnieniem *(a w niektórych przypadkach pomiędzy kolejnymi operacjami wypełniania)*.
-   Rozważyć zastosowanie funkcji **Edycja → Preferencje ... → Część / Projekt Części → Automatycznie sprawdź model po wykonaniu operacji logicznej**, aby umożliwić automatyczne sprawdzanie i udoskonalanie modelu po operacjach logicznych i szkicowych *(wydajność może ulec zmianie, jeśli opcje te pozostaną włączone)*.

Zwróć również uwagę, że na funkcję zaokrąglania części wpływa [Topologiczny problem nazewnictwa](Topological_naming_problem/pl.md), gdy jakakolwiek zmiana jest dokonywana na wcześniejszym etapie modelowania w łańcuchu, który wpływa na liczbę powierzchni lub wierzchołków. Może to powodować nieprzewidywalne rezultaty. Dopóki problem ten nie zostanie rozwiązany, zaleca się stosowanie operacji fazowania i zaokrąglania jako ostatnich kroków w łańcuchu modelowania.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fillet/pl
