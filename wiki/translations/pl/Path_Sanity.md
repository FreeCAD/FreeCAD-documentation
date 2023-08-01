---
- GuiCommand:
   Name:Path Sanity
   Name/pl:Path: Bezpieczeństwo
   MenuLocation:Ścieżka - Sprawdź zadanie ścieżki pod kątem typowych błędów
   Workbenches:[Path](Path_Workbench/pl.md)
   Shortcut:**P** **S**
   Version:0.19
---

# Path Sanity/pl



## Opis

Wielu użytkowników środowiska pracy Path to hobbyści i majsterkowicze. W związku z tym używają oni swoich maszyn CNC do uruchamiania G-kodu, który sami skonfigurowali i wygenerowali. Inaczej jest w przypadku większości profesjonalnych / komercyjnych użytkowników. W profesjonalnych warsztatach za tworzenie G-kodu odpowiadają *(programiści CNC)* inni ludzie, niż ci, którzy uruchamiają go na maszynach *(operator CNC)*.

Hobbyści zwykle uruchamiają G-kod zaledwie kilka minut po jego przetworzeniu i prawdopodobnie tylko raz lub dwa razy. W profesjonalnym warsztacie sprawdzony G-kod może być uruchamiany wiele razy przez miesiące lub lata po jego wygenerowaniu.

Jedną z kwestii, która pojawia się w profesjonalnym warsztacie CNC, jest to, że programista przyjmuje wiele założeń, które NIE są przekazywane w samym G-kodzie. Na przykład, G-kod może wywoływać narzędzie \"T3\", ale o ile nie jest to skomentowane, G-kod nie mówi, do jakiego rodzaju narzędzia odnosi się \"T3\". Zakłada się po prostu, że T3 w systemie CAM jest tym samym, co T3 na maszynie. Istnieje wiele takich założeń dotyczących konfiguracji maszyny, narzędzi, materiału, orientacji części itp. Nawet jeśli G-kod jest doskonały, jeśli operator nie skonfiguruje maszyny z tymi samymi założeniami, może dojść do awarii.

Komercyjne warsztaty często tworzą \"książkę ustawień\", która dokumentuje wszystkie te założenia i daje operatorom wszystko, czego potrzebują do skonfigurowania maszyny i wyprodukowania części.

<img alt="" src=images/Path_Sanity.svg  style="width:16px;"> **Path: Bezpieczeństwo** jest narzędziem w środowisku pracy Path do generowania tego rodzaju informacji. Wynikiem tego polecenia jest samodzielny plik {{Value|.html}} z osadzonymi obrazami.

<img alt="" src=images/Sanity.jpg  style="width:600px;">



*Powyżej: Przykład wygenerowanego raportu Path Bezpieczeństwo*



## Informacje o raporcie 

O ile to możliwe, treść jest niezależna od programu FreeCAD. Operator CNC może nigdy nie używać FreeCAD, więc terminologia specyficzna dla FreeCAD / Path jest myląca. Raport ma odrębne sekcje i jest sformatowany tak, aby wyszukiwanie było łatwe i przewidywalne.



## Informacje o detalu 

Ta sekcja zawiera przegląd tego, co jest tworzone. Idealnie obraz powinien pokazywać obiekty bazowe. Jeśli istnieje wiele obiektów bazowych, obraz powinien pokazywać sposób ich zagnieżdżania.



### Podsumowanie procesu 

Umożliwia szybki podgląd minimalnej i maksymalnej wysokości oraz czasu pracy.



### Surowe naddatki 

Szczegóły obiektu naddatków z zadania. Jest to obszar, w którym środowisku Path przydałaby się pewna poprawa. Przydałaby się tutaj podstawowa właściwość materiału dla naddatku, a także mogłaby zostać wykorzystana do sugerowania posuwów / prędkości.



### Dane narzędzi 

Zawiera sekcje dla każdego numeru narzędzia używanego w zadaniu. Zawiera szczegółowe informacje na temat tego, co programista zakłada jako narzędzie i które operacje go używają. Ta sekcja działa tylko z nowym systemem magazynu narzędzi. Jest to kolejny obszar, w którym środowisko Path wymaga poprawy. W szczególności zestawy narzędzi wymagają dodatkowych atrybutów dotyczących narzędzia, takich jak producent / url / numer części.



### Rezultat

Podaje szczegółowe informacje o tym, gdzie i kiedy G-kod został przetworzony. Pokazuje również, czy zadanie zawiera opcjonalne / obowiązkowe postoje, dzięki czemu operator wie, czy można bezpiecznie odejść od maszyny podczas pracy.



### Chłodzenie

Jaki rodzaj chłodziwa jest wymagany, jeżeli jest stosowane.



### Oprawki i uchwyty robocze 

Wyświetla części w kontekście obszaru magazynowego, a także pokazuje pochodzenie części.



### Problemy

Ostrzeżenia i błędy wykryte przez funkcję **Bezpieczeństwo**. Mogą to być problemy lub nie, ale są one odnotowywane w celu zwrócenia dodatkowej uwagi. Na przykład, jeśli ten sam numer narzędzia jest używany dla różnych zestawów narzędzi, zostanie to wyświetlone jako błąd. Jeśli kontroler narzędzia nie ma skonfigurowanego posuwu/prędkości, zostanie to wyświetlone jako ostrzeżenie. Wykryje również i ostrzeże o nieużywanych kontrolerach narzędzi. Środowisko Path skorzystałoby tutaj z możliwości dodawania dowolnych notatek lub ostrzeżeń.



## Użycie

1.  Wybierz <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Zadanie](Path_Job/pl.md) w oknie [Widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Path_Sanity.svg" width=16px> '''Sprawdź zadanie ścieżki pod kątem typowych błędów'''**.
    -   Wybierz z menu opcję **Ścieżka → <img src="images/Path_Sanity.svg" width=16px> Sprawdź zadanie ścieżki pod kątem typowych błędów**.
    -   Użyj skrótu klawiaturowego: **P**, a następnie **S**.
3.  Odpowiednie informacje są gromadzone w słowniku Python, a następnie formatowane do formatu asciidoc.
4.  Plik asciidoc jest zapisywany na dysku w tej samej lokalizacji, co plik, który zostanie przetworzony.
5.  Zewnętrzny proces wywołuje asciidoctor, aby odczytać asciidoc i wygenerować plik w formacie {{Value|.html}}.
6.  Spowoduje to automatyczne uruchomienie systemowej przeglądarki internetowej w celu wyświetlenia wygenerowanego samodzielnego raportu HTML.



## Uwagi

-   Asciidoc to lekki format znaczników do tworzenia notatek, artykułów, książek itp. Jest czytelny dla człowieka i łatwy do przetłumaczenia na inne formaty.

-   Asciidoctor to szybki procesor tekstu o otwartym kodzie źródłowym do konwersji asciidoc na HTML, PDF lub inne formaty. Jest dostępny dla systemów Linux, Windows i MacOS. Asciidoctor nie jest instalowany z programem FreeCAD. Jeśli użyjesz **Path Bezpieczeństwo** bez zainstalowania Asciidoctor, plik źródłowy asciidoc zostanie wygenerowany, ale wynikowy HTML nie zostanie wygenerowany. Zobacz informacje na stronie [domowej tego narzędzia](https://asciidoctor.org/).





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Sanity/pl
