---
 TutorialInfo:l
   Topic: środowisko pracy Architektura
   Level: zaawansowany
   Time: 120 minut
   Author: Pablo Gil
   FCVersion: 0.19.x
   Files: brak
}}

## Wprowadzenie

To było tak trudne dochodzenie, jak uzyskać działającą kopię IfcOpenShell-python na OSX/macOS w celu importowania/eksportowania plików IFC, że dzielę się tym poradnikiem na wypadek, gdyby pomógł większej liczbie osób. Mój system to OSX 10.11.6, 64bity z środowiskiem Python 2.7.11, może to zadziałać, jeśli masz również OSX, ponieważ często są one 64-bitowe, ale mogą się różnić od mojego. Procedura może być bardzo podobna, jeśli używasz Linuksa lub Windowsa, ale prawdopodobnie ma pewne różnice.



## Wymagania

-   IfcOpenShell
-   FreeCAD w wersji 0.19 lub nowszej

## Kroki

1\. Pobierz lub sklonuj pełny projekt GitHub pod adresem <https://github.com/IfcOpenShell/IfcOpenShell> **

:   
    `git clone https://github.com/IfcOpenShell/IfcOpenShell
---

# Import/Export IFC - compiling IfcOpenShell/pl

     

2\. Z terminala przejdź do folderu **/nix/** i uruchom skrypt. W systemie OSX jest on wykonywany za pomocą: 
```python
cd nix/
./build-all.sh
``` Kompilacja zajmie od 30 do 120 minut. Nie jest to najmądrzejszy sposób kompilacji [IfcOpenShell](IfcOpenShell/pl.md), ale ten prosty skrypt skompiluje wszystkie zależności, wersje Python itp.

3\. Po zakończeniu *(nie pamiętam teraz, ale zostanie wypisane coś w stylu \"Built IfcOpenShell\...\" i powróci do monitu)* będziesz miał nowy folder **/IfcOpenShell/build/** pełen plików i folderów. Z mojego osobistego doświadczenia wynika, że dwa tygodnie temu skrypt nix \"build-all.sh\" nie zakończył się pomyślnie, ale po wypróbowaniu go wczoraj z najnowszymi aktualizacjami działał dobrze, więc przypuszczam, że możesz doświadczyć czegoś podobnego w przypadku dalszego rozwoju\... Więc teraz masz wszystko, czego potrzebujesz, ale musisz wykonać trochę samodzielnej pracy, aby to zadziałało:

4\. Otwórz FreeCAD i otwórz okna [konsola Python](Python_console/pl.md) i [Widok raportu](Report_view/pl.md). Następnie wpisz w konsoli Python następujące polecenie: 
```python
import sys
print sys.path
``` Otrzymasz długą linię ze wszystkimi ścieżkami, które odczytuje FreeCAD. Możesz być w stanie zainstalować IfcOpenShell w dowolnej z nich, ale sugeruję umieszczenie go w takiej, w której znajdziesz **/site-packages/** po **/Python/** lub **/python-something/**. W moim przypadku był to **/Library/Python/2.7/site-packages**. *(Uwaga: znajdziesz ścieżki wewnątrz katalogu aplikacji, ale sugeruję ich nie używać, ponieważ wtedy IfcOpenShell będzie dostępny tylko dla tej aplikacji)*.

5\. Po zlokalizowaniu miejsca, w którym chcesz / musisz go zainstalować, przejdź tam za pomocą przeglądarki plików *(Finder w OSX)*. To znaczy, przejdź do folderu **/site-packages/**

:   
    {{incode|cd site-packages/`.

6\. Otwórz nowe okno przeglądarki plików i przejdź do pobranego projektu GitHub: **/IfcOpenShell/src/ifcopenshell-python/** i skopiuj cały folder **/ifcopenshell/**.

7\. Wklej go do folderu **/site-packages/**. Teraz powinieneś mieć coś takiego: 
```python
/site-packages/ifcopenshell/__init__.py
/site-packages/ifcopenshell/entity_instance.py
/site-packages/ifcopenshell/file.py
/site-packages/ifcopenshell/geom/app.py
/site-packages/ifcopenshell/geom/main.py
/site-packages/ifcopenshell/geom/occ_utils.py
/site-packages/ifcopenshell/geom/__init__.py
/site-packages/ifcopenshell/guid.py
```

8\. Teraz musimy wybrać dwa pliki wewnątrz folderu /build/, są to: 
```python
_ifcopenshell_wrapper.so
ifcopenshell_wrapper.py
``` ale ponieważ skompilowaliśmy wszystko, będziesz musiał wybrać ten, który pasuje do twojej wersji Python FreeCAD. Sprawdź to łatwo czytając pierwszą linię w widoku [konsoli Python](Python_console/pl.md) FreeCAD. W moim przypadku był to Python 2.7.11.

9\. Teraz skopiujmy pliki do miejsca odpowiadającego wersji Python. W moim przypadku było to: 
```python
/IfcOpenShell/build/Darwin/x86_64/build/ifcopenshell/[b]python-2.7[/b].10/ifcwrap/
```

10\. Wklej je wewnątrz **/site-packages/ifcopenshell/**

11\. Sprawdź, czy wszystko jest na swoim miejscu: 
```python
/site-packages/ifcopenshell/__init__.py                  (1)
/site-packages/ifcopenshell/entity_instance.py           (1)
/site-packages/ifcopenshell/_ifcopenshell_wrapper.so     (2)
/site-packages/ifcopenshell/file.py                      (1)
/site-packages/ifcopenshell/geom/__init__.py             (1)
/site-packages/ifcopenshell/geom/app.py                  (1)
/site-packages/ifcopenshell/geom/main.py                 (1)
/site-packages/ifcopenshell/geom/occ_utils.py            (1)
/site-packages/ifcopenshell/guid.py                      (1)
/site-packages/ifcopenshell/ifcopenshell_wrapper.py      (2)
```

*(1)* z projektu GitHub
*(2)* z folderu /build/

12\. Zamknij i ponownie otwórz program FreeCAD.

## Testowanie

Po zainstalowaniu sprawdźmy, czy wszystko działa zgodnie z oczekiwaniami:

12.1 w konsoli Python: 
```python
import ifcopenshell
from ifcopenshell import geom
``` jeśli nie wyrzuci żadnego błędu, oznacza to, że może być poprawnie zainstalowany.

12.2 Przejdź do [poradnika FreeCAD użytkownika Yorik](Manual:BIM_modeling/pl.md), nawigacji do dolnej części strony i pobierz następujące pliki do przetestowania: 
```python
house.FCStd
house.ifc
```

12.3 Otwórz **house.FCStd**, wybierz główny obiekt \"Building\" i wyeksportuj go (**Plik → Eksport**) ustawiając typ pliku na \"Industry Foundation Classes (\*.ifc)\". Naciśnij **Zapisz** i jeśli to zadziała i nie wyrzuci błędu w oknie [Widoku raportu](Report_view/pl.md), to znaczy, że działa.

12.4 Test końcowy, import **house.ifc** do nowego pliku, więc otwórz nowy plik i zaimportuj go \... to trochę potrwa.

13\. Ciesz się BIM dzięki FreeCAD!

## Przemyślenia końcowe 

Moim zdaniem sam FreeCAD powinien mieć prekompilowane wersje IfcOpenShell dołączone do dystrybucji, ponieważ samodzielne budowanie go jest totalnym bólem i przeciętny użytkownik tego nie zrobi *(nie wie, jak kompilować, zarządzać GitHubem itp.)*, ale cóż, może w przyszłości.

Mam nadzieję, że to ci pomoże.

Dzięki.



## Odnośniki internetowe 

-   Powiązany wątek na forum [dyskusyjnym](http://forum.freecadweb.org/viewtopic.php?f=23&t=17536)
-   [IfcOpenShell](IfcOpenShell/pl.md)


{{Userdocnavi

}}



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > [3rd Party](Category_3rd Party.md) > [File_Formats](Category_File_Formats.md) > Import/Export IFC - compiling IfcOpenShell/pl
