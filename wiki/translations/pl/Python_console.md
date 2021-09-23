# Python console/pl
**''(styczeń 2020)'' FreeCAD został pierwotnie zaprojektowany do współpracy z Pythonem 2. Ponieważ Python 2 osiągnął koniec życia w 2020 roku, dalszy rozwój FreeCAD będzie się odbywał wyłącznie z Pythonem 3, a kompatybilność wsteczna nie będzie utrzymywana.**

## Wprowadzenie

[Konsola Pythona](Python_console.md) to panel, który uruchamia instancję interpretera [Python](Python.md), który może być używany do sterowania procesami FreeCAD oraz tworzenia i modyfikowania obiektów i ich właściwości.

Konsola Pythona w FreeCAD obsługuje podstawowe kolorowanie składni, potrafi rozróżnić różne style i kolory, komentarze, łańcuchy, wartości liczbowe, wbudowane funkcje, wydrukowany tekst wyjściowy i separatory, takie jak nawiasy i przecinki. Te właściwości konsoli można skonfigurować w [Edytor preferencji](Preferences_Editor.md).

<img alt="" src=images/FreeCAD_Python_console.png  style="width:800px;">


*Konsola Pythona pokazująca komunikaty, gdy FreeCAD właśnie się uruchamia.*

## Tworzenie skryptów 


**Dla absolutnie początkujących, zobacz:**

[Wprowadzenie do Pythona](Introduction_to_Python.md), oraz [Samouczek tworzenia skryptów Python](Python_scripting_tutorial.md).


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics.md), oraz [Obiekty skryptowe](Scripted_objects.md).

Konsola Pythona potrafi wykonać uzupełnienie podstawowego kodu. Gdy po obiekcie zostanie zapisana kropka, pokaże na przykład publiczne metody i atrybuty *(zmienne)* bieżącego obiektu *(klasy)*, `obj.`

Konsola jest również w stanie wyświetlić łańcuch dokumentacji konkretnej funkcji, gdy zapisywany jest otwierający nawias, na przykład `function(`

<img alt="" src=images/FreeCAD_Python_console_example.png  style="width:800px;">


*Przykładowy kod Pythona, który generuje obiekty w oknie widoku 3D.*

Skrypty inicjujące FreeCAD automatycznie ładują niektóre moduły i definiują niektóre aliasy. Dlatego też, są one dostępne w konsoli Pythona 
```python
App = FreeCAD
Gui = FreeCADGui
```

W związku z tym są one równe


```python
App.newDocument()
FreeCAD.newDocument()
```


**Note:**

Te wstępnie załadowane moduły i aliasy są dostępne tylko z konsoli Pythona wbudowanej w program FreeCAD. Jeśli używasz FreeCAD jako biblioteki w zewnętrznym programie, musisz pamiętać o załadowaniu modułów `FreeCAD` i `FreeCADGui` i zdefiniowaniu niezbędnych aliasów, jeżeli zachodzi taka potrzeba.

## Działania

Kliknij prawym przyciskiem myszy na konsoli Pythona, aby wyświetlić kilka poleceń:

-    **Copy**: Przechowuje zaznaczony tekst w schowku do późniejszego wklejenia. Funkcja jest wyłączona, jeśli nic nie jest zaznaczone.

-    **Copy command**: Przechowuje wybrane polecenie w schowku do późniejszego wklejenia. Funkcja jest wyłączona, jeśli nic nie jest zaznaczone.

-    **Historia kopiowania**: Skopiuj całą historię poleceń Pythona wprowadzonych w tej sesji.

-    **Zapisz historię jako**: Zapisuje całą historię poleceń Pythona wprowadzonych w tej sesji do pliku tekstowego.

-    **Wklej**: Wklej uprzednio skopiowany tekst ze schowka do konsoli Pythona.

-    **Zaznacz wszystko**: Zaznacza cały tekst w konsoli Pythona.

-    **Wyczyść konsolę**: Usuwa wszystkie polecenia wprowadzone do konsoli Pythona. Jest to przydatne, gdy konsola Pythona jest pełna komunikatów i wcześniej wprowadzonych poleceń, które mogą rozpraszać podczas testowania nowej funkcji. Jest to tylko estetyczne, ponieważ polecenie to nie usuwa istniejących zmiennych ani nie usuwa zaimportowanych modułów w sesji.

-    **Wstaw nazwę pliku**: Otwiera okno dialogowe do wyszukiwania pliku w systemie, a następnie wstawia pełną ścieżkę do pliku. Jest to przydatne do testowania funkcji, które przetwarzają plik wejściowy, bez konieczności zapisywania całej nazwy w konsoli, co jest podatne na błędy. To polecenie nie uruchamia pliku i nie importuje go jako modułu Pythona, tylko zwraca pełną ścieżkę do tego pliku.

-    **Zawijanie linii**: zawijaj bardzo długie linie, które przekraczają poziomy wymiar konsoli Pythona.

## Uwagi

-   Istnieje możliwość przewijania API w konsoli Pythona. Przykład:
    1.  W konsoli wpisz: `FreeCAD.`
    2.  Pojawi się okno dialogowe z opcjonalnymi klasami/funkcjami do wyboru
    3.  Przewiń listę, aby przeczytać opis każdej klasy/funkcji
    4.  Wybierając funkcję i podążając za nią z `.` można powtórzyć kroki 2 i 3, aby zagłębić się w API.
-   Uzupełnianie tabulatorami / słowami jest obsługiwane za pomocą skrótu {{KEY | Ctrl}} + {{KEY | Spacja}}


{{Interface navi

}} {{Std Base navi}}

---
[documentation index](../README.md) > Python console/pl
