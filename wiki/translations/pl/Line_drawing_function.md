# Line drawing function/pl
## Wprowadzenie

Ta strona pokazuje, jak łatwo można tworzyć zaawansowane funkcje w środowisku Python. W tym ćwiczeniu zbudujemy nowe narzędzie, które rysuje linię. Narzędzie to można następnie połączyć z poleceniem FreeCAD, a polecenie to można wywołać za pomocą dowolnego elementu interfejsu, takiego jak element menu lub przycisk paska narzędzi.



## Skrypt główny 

Najpierw napiszemy skrypt zawierający całą naszą funkcjonalność. Następnie zapiszemy go w pliku i zaimportujemy do FreeCAD, aby udostępnić wszystkie jego klasy i funkcje. Uruchom swój ulubiony edytor kodu i wpisz następujące linie:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


{{Top}}



## Szczegółowe wyjaśnienia 


```python
import Part, FreeCADGui
from pivy.coin import *
```

W środowisku Python, gdy chcesz użyć funkcji z innego modułu, musisz go zaimportować. W naszym przypadku będziemy potrzebować funkcji z modułu [Część](Part_Workbench/pl.md) do tworzenia linii oraz z modułu Gui `FreeCADGui`, aby uzyskać dostęp do [widoku 3D](3D_view/pl.md). Potrzebujemy również pełnej zawartości biblioteki Coin, abyśmy mogli bezpośrednio korzystać ze wszystkich obiektów Coin, takich jak `SoMouseButtonEvent`, itp.


```python
class line:
```

Tutaj definiujemy naszą główną klasę. Dlaczego używamy klasy, a nie funkcji? Powodem jest to, że potrzebujemy, aby nasze narzędzie pozostało \"żywe\", podczas gdy czekamy na kliknięcie użytkownika na ekranie. Funkcja kończy się, gdy jej zadanie zostanie wykonane, ale obiekt *(klasa definiuje obiekt)* pozostaje aktywny do momentu jego zniszczenia.


```python
"""This class will create a line after the user clicked 2 points on the screen"""
```

W Pythonie każda klasa lub funkcja może mieć ciąg dokumentacji *(docstring)*. Jest to szczególnie przydatne w FreeCAD, ponieważ po wywołaniu tej klasy w interpreterze, ciąg opisu zostanie wyświetlony jako podpowiedź.


```python
def __init__(self):
```

Klasy Python zawsze mogą zawierać funkcję `__init__`, która jest wykonywana, gdy klasa jest wywoływana w celu utworzenia obiektu. Tutaj umieścimy wszystko, co chcemy, aby się działo, gdy nasze narzędzie liniowe się uruchomi.


```python
self.view = FreeCADGui.ActiveDocument.ActiveView
```

W klasie zazwyczaj chcesz poprzedzić nazwy zmiennych słowem kluczowym `self.`, aby umożliwić łatwy dostęp do zmiennych we wszystkich funkcjach wewnątrz i na zewnątrz klasy. Tutaj będziemy używać `self.view` do dostępu i manipulacji aktywnym widokiem 3D.


```python
self.stack = []
```

Tutaj tworzymy pustą listę, która będzie zawierać punkty 3D wysłane przez funkcję `getpoint()`.


```python
self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
```

To ważna część. Ponieważ mamy do czynienia z sceną [Coin3D](https://github.com/coin3d/coin/wiki), używamy mechanizmu zwrotnego Coin, który pozwala na wywołanie funkcji za każdym razem, gdy wystąpi określone zdarzenie sceny. W naszym przypadku tworzymy zwrotkę dla zdarzeń [SoMouseButtonEvent](https://coin3d.github.io/Coin/html/classSoMouseButtonEvent.html) i wiążemy ją z funkcją `getpoint()`. Teraz za każdym razem, gdy zostanie naciśnięty lub zwolniony przycisk myszy, zostanie wykonana funkcja `getpoint()`.

Należy pamiętać, że istnieje również alternatywa dla `addEventCallbackPivy()` o nazwie `addEventCallback()`, która nie opiera się na pivy. Ale ponieważ pivy jest bardzo wydajnym i naturalnym sposobem dostępu do dowolnej części sceny Coin, jest to lepszy wybór. {{Top}} 
```python
def getpoint(self, event_cb):
```

Teraz zdefiniujemy funkcję `getpoint()`, która będzie wykonywana po naciśnięciu przycisku myszy w widoku 3D. Funkcja ta otrzyma argument, który nazwiemy `event_cb`. Z tego wywołania zwrotnego zdarzenia możemy uzyskać dostęp do obiektu zdarzenia, który zawiera kilka informacji *(więcej informacji znajdziesz na stronie [wycinki kodu](Code_snippets/pl#Obserwowanie_zdarzeń_myszy_w_przeglądarce_3D_za_pomocą_środowiska_Python.md))*.


```python
if event.getState() == SoMouseButtonEvent.DOWN:
```

Funkcja `getpoint()` zostanie wywołana, gdy zostanie naciśnięty lub zwolniony przycisk myszy. Jednak chcemy wybrać punkt 3D tylko wtedy, gdy zostanie naciśnięty przycisk, w przeciwnym razie otrzymalibyśmy dwa punkty 3D bardzo blisko siebie. Dlatego musimy to sprawdzić tutaj.


```python
pos = event.getPosition()
```

Tutaj otrzymujemy współrzędne ekranowe kursora myszy.


```python
point = self.view.getPoint(pos[0], pos[1])
```

Funkcja ta daje nam wektor FreeCAD (x,y,z) zawierający punkt 3D, który leży na płaszczyźnie ogniskowej, tuż pod kursorem myszy. Jeśli jesteś w widoku kamery, wyobraź sobie promień wychodzący z kamery, przechodzący przez kursor myszy i uderzający w płaszczyznę ogniskową. Jest to lokalizacja naszego punktu 3D. Jeśli jesteśmy w widoku ortogonalnym, promień jest równoległy do kierunku widoku.


```python
self.stack.append(point)
```

Dodajemy nasz nowy punkt do stosu.


```python
if len(self.stack) == 2:
```

Czy mamy już wystarczająco dużo punktów? Jeśli tak, to wyznaczmy granicę!


```python
l = Part.LineSegment(self.stack[0], self.stack[1])
```

Tutaj używamy funkcji `LineSegment()` z modułu Część, która tworzy linię z dwóch wektorów FreeCAD. Linia nie jest powiązana z żadnym obiektem w naszym aktywnym dokumencie, więc nic nie pojawia się na ekranie.


```python
shape = l.toShape()
```

Dokument FreeCAD może akceptować tylko kształty z modułu Część. Kształty są najbardziej ogólnym typem modułu Część. Musimy więc przekonwertować naszą linię na kształt przed dodaniem jej do dokumentu.


```python
Part.show(shape)
```

Moduł Część posiada bardzo przydatną funkcję `show()`, która tworzy nowy obiekt w dokumencie i wiąże z nim kształt. Mogliśmy również najpierw utworzyć nowy obiekt w dokumencie, a następnie ręcznie powiązać z nim kształt.


```python
self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```

Ponieważ skończyliśmy z naszą linią, usuwamy tutaj mechanizm wywołania zwrotnego. 

## Testowanie skryptu 

Teraz zapiszmy nasz skrypt w folderze, w którym interpreter Python dla FreeCAD może go znaleźć. Podczas importowania modułów interpreter będzie szukał w następujących miejscach: w ścieżkach instalacji Pythona, w folderze **bin** FreeCAD oraz we wszystkich folderach **Mod** *(modułowych)* FreeCAD. Dlatego najlepszym rozwiązaniem jest utworzenie nowego folderu w jednym z folderów **Mod**. Utwórzmy tam folder o nazwie **MyScripts** i zapiszmy w nim nasz skrypt jako **exercise.py**.

Teraz wszystko jest gotowe. Uruchommy FreeCAD, utwórzmy nowy dokument i w interpreterze Python wpiszmy:


```python
import exercise
```

Jeśli nie pojawi się żaden komunikat o błędzie, nasz skrypt został pomyślnie załadowany. Możemy teraz sprawdzić jego zawartość za pomocą:


```python
dir(exercise)
```

Polecenie `dir()` jest wbudowanym poleceniem Python, które wyświetla zawartość modułu. Możemy sprawdzić, czy nasza klasa `line()` tam jest za pomocą:


```python
'line' in dir(exercise)
```

Przetestujmy to teraz:


```python
exercise.line()
```

Kliknij dwa razy w widoku 3D i bingo: oto nasza linia! Aby ją powtórzyć, wystarczy ponownie wpisać 

## Zarejestrowanie skryptu 

Aby nasze nowe narzędzie do rysowania linii było naprawdę użyteczne i uniknąć konieczności wpisywania wszystkich tych komend, powinno ono mieć przycisk w interfejsie. Jednym sposobem na to jest przekształcenie naszego nowego folderu **MyScripts** w pełne środowisko pracy FreeCAD. To jest proste, wystarczy umieścić plik o nazwie **InitGui.py** wewnątrz folderu **MyScripts**. Plik **InitGui.py** będzie zawierać instrukcje do stworzenia nowego środowiska pracy oraz dodania naszego nowego narzędzia do niego. Poza tym będziemy musieli trochę zmodyfikować nasz kod ćwiczenia, aby narzędzie `line()` było rozpoznawane jako oficjalna komenda FreeCAD. Zacznijmy od stworzenia pliku **InitGui.py** i wpisanie w nim następującego kodu:


```python
class MyWorkbench (Workbench):

    MenuText = "MyScripts"

    def Initialize(self):
        import exercise
        commandslist = ["line"]
        self.appendToolbar("My Scripts", commandslist)

Gui.addWorkbench(MyWorkbench())
```

Do tej pory prawdopodobnie rozumiesz powyższy skrypt. Tworzymy nową klasę, którą nazywamy `MyWorkbench`, nadajemy jej tytuł `MenuText`, i definiujemy funkcję `Initialize()`, która zostanie wykonana, gdy środowisko pracy zostanie załadowane do FreeCAD. W tej funkcji wczytujemy zawartość naszego pliku ćwiczenia i dodajemy znalezione w nim komendy FreeCAD do listy komend. Następnie tworzymy pasek narzędzi o nazwie \"Moje skrypty\" i przypisujemy naszą listę komend do niego. Aktualnie, oczywiście, mamy tylko jedno narzędzie, więc nasza lista komend zawiera tylko jeden element. Następnie, gdy nasze środowisko pracy jest gotowe, dodajemy je do głównego interfejsu.

Ale to wciąż nie zadziała, ponieważ komenda FreeCAD musi być sformatowana w określony sposób, będziemy musieli zmienić nasze narzędzie `line()`. Nasz nowy skrypt **exercise.py** powinien wyglądać tak:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('line', line())
```

To, co tutaj zrobiliśmy, to przekształcenie naszej funkcji `__init__()` w funkcję `Activated()`. Gdy komendy FreeCAD są uruchamiane, automatycznie wykonują funkcję `Activated()`. Dodaliśmy również funkcję `GetResources()`, która informuje FreeCAD, gdzie można znaleźć ikonę narzędzia, oraz jak będą nazywać się i co będą wyświetlać wskazówki dotyczące naszego narzędzia. Każdy obraz **jpg**, **png** lub **svg** będzie działał jako ikona, może mieć dowolny rozmiar, ale najlepiej używać rozmiaru zbliżonego do ostatecznego wyglądu, np. 16x16, 24x24 lub 32x32. Następnie dodajemy klasę `line()` jako oficjalną komendę FreeCAD za pomocą metody `addCommand()`.

To wszystko, teraz musimy tylko ponownie uruchomić FreeCAD i będziemy mieli ładne nowe środowisko pracy z naszym nowym narzędziem do linii! 

## Chcesz czegoś więcej? 

Jeśli spodobało Ci się to ćwiczenie, dlaczego nie spróbujesz ulepszyć tego narzędzia? Jest wiele rzeczy, które można zrobić, na przykład:

-   Dodaj informacje zwrotne dla użytkownika: do tej pory stworzyliśmy bardzo podstawowe narzędzie, więc użytkownik może trochę się zgubić podczas jego użytkowania. Możemy dodać jakieś komunikaty zwrotne, informujące użytkownika, co zrobić następnie. Możesz wyświetlać komunikaty w konsoli FreeCAD. Spójrz na moduł `FreeCAD.Console`.
-   Dodaj możliwość wprowadzania współrzędnych punktów 3D ręcznie. Zajrzyj do funkcji Pythona `input()` na przykład.
-   Dodaj możliwość dodawania więcej niż 2 punktów.
-   Dodaj zdarzenia dla innych elementów: Obecnie sprawdzamy tylko zdarzenia przycisków myszy, ale co jeśli chcielibyśmy zrobić coś także, gdy myszka jest przesuwana, na przykład wyświetlanie aktualnych współrzędnych?
-   Nadaj nazwę utworzonemu obiektowi.

Nie wahaj się zadawać pytań lub dzielić się pomysłami na forum [1](https://forum.freecadweb.org/)! {{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Line drawing function/pl
