# FreeCAD Scripting Basics/pl
{{TOCright}}

## Tworzenie skryptów Python w środowisku FreeCAD 

FreeCAD jest zbudowany od podstaw tak, aby być całkowicie kontrolowanym przez skrypty Python. Prawie wszystkie komponenty programu FreeCAD, takie jak interfejs, zawartość sceny, a nawet reprezentacja tej zawartości w widokach 3D, są dostępne z wbudowanego interpretera Pythona lub z własnych skryptów. W rezultacie, FreeCAD jest prawdopodobnie jedną z najgłębiej konfigurowalnych aplikacji inżynierskich dostępnych obecnie.

Jeśli nie znasz Pythona, zalecamy poszukać poradników w internecie i szybko zapoznać się z jego strukturą. Python jest bardzo łatwym językiem do nauki, zwłaszcza, że może być uruchamiany wewnątrz interpretera, gdzie proste polecenia, aż do kompletnych programów, mogą być wykonywane w locie, bez konieczności kompilowania czegokolwiek. FreeCAD posiada wbudowany interpreter Pythona. Jeśli nie widzisz okna oznaczonego jako konsola Pythona, jak pokazano poniżej, możesz go aktywować pod menu **Widok → Panele → konsola Python**.

### Interpreter

Z poziomu interpretera masz dostęp do wszystkich zainstalowanych w systemie modułów Pythona, jak również do wbudowanych modułów FreeCAD oraz wszystkich dodatkowych modułów FreeCAD, które zainstalowałeś później. Poniższy zrzut ekranu przedstawia interpreter Pythona   *

![Interpreter Python programu FreeCAD](images/screenshot_pythoninterpreter.jpg )

Z poziomu interpretera można wykonać kod Python i przeglądać dostępne klasy i funkcje. FreeCAD zapewnia bardzo poręczną przeglądarkę klas do eksploracji   * Po wpisaniu nazwy znanej klasy, po której następuje kropka *(co oznacza, że chcesz dodać coś z tej klasy)*, otwiera się okno przeglądarki klas, gdzie możesz poruszać się pomiędzy dostępnymi podklasami i metodami. Kiedy coś wybierzesz, wyświetli się powiązany tekst pomocniczy *(jeśli istnieje)*   *

![Przeglądarka klas programu FreeCAD](images/screenshot_classbrowser.jpg )

Więc, zacznij od wpisania `App.` albo `Gui.` i zobacz co się stanie. Innym, bardziej ogólnym sposobem eksplorowania zawartości modułów i klas w Pythonie jest użycie polecenia `print(dir())`. Na przykład, wpisanie `print(dir())` wyświetli listę wszystkich modułów aktualnie załadowanych w FreeCAD. `print(dir(App))` pokaże ci wszystko wewnątrz modułu App, itd.

Kolejną przydatną funkcją interpretera jest możliwość cofnięcia się przez całą historię poleceń i odtworzenia linii kodu, którą już wcześniej wpisałeś. Aby poruszać się po historii poleceń, wystarczy użyć klawisza **Strzałka w górę** lub **Strzałka w dół**.

Klikając prawym przyciskiem myszy w oknie interpretera, masz również kilka innych opcji, takich jak skopiowanie całej historii *(przydatne, gdy chcesz eksperymentować z rzeczami przed utworzeniem pełnego skryptu)*, lub wstawienie nazwy pliku z pełną ścieżką. {{Top}}

### Pomoc dla Pythona 

W menu FreeCAD **Pomoc** znajdziesz wpis oznaczony **Automatyczna dokumentacja modułów Python**, który otworzy okno przeglądarki zawierające pełną, rzeczywistą dokumentację wszystkich modułów Pythona dostępnych dla interpretera FreeCAD, w tym modułów wbudowanych Pythona i FreeCAD, modułów zainstalowanych w systemie oraz modułów dodatkowych FreeCAD. Dostępna tam dokumentacja jest uzależniona od tego, ile wysiłku każdy programista wkłada w dokumentację swojego kodu, ale moduły Python mają reputację dość dobrze udokumentowanych. Okno Twojego FreeCAD musi pozostać otwarte, aby ten system dokumentacji mógł działać. Wprowadzenie do **dokumentacji skryptowej Python** zapewni Ci szybki link do sekcji wiki [Centrum Power użytkownika](Power_users_hub/pl.md). {{Top}}

## Moduły wbudowane 

Ponieważ FreeCAD został zaprojektowany tak, aby mógł być uruchamiany również bez graficznego interfejsu użytkownika *(GUI)*, prawie cała jego funkcjonalność jest podzielona na dwie grupy   * Podstawowa funkcjonalność, nazwana `App`, oraz funkcjonalność GUI, nazwana `Gui`. Te dwa moduły mogą być również dostępne ze skryptów poza interpreterem, odpowiednio o nazwach `FreeCAD` i `FreeCAD`.

-   W module `App` znajdziesz wszystko, co jest związane z samą aplikacją, np. Metody otwierania lub zamykania plików oraz dokumentów, takie jak ustawianie aktywnego dokumentu lub lista ich zawartości.

-   W module `Gui` znajdziesz narzędzia do uzyskiwania dostępu i zarządzania elementami Gui, takimi jak Środowiska pracy i ich paski narzędzi oraz, co ciekawsze, graficzną reprezentację całej zawartości FreeCAD.

Listowanie zawartości tych modułów nie jest zbyt przydatne, ponieważ rozwijają się one dość szybko w miarę rozwoju FreeCAD. Ale dwa dostarczone narzędzia do przeglądania *(przeglądarka klasy i pomoc dla Pythona)* powinny w każdej chwili dostarczyć Ci kompletną i aktualną dokumentację. {{Top}}

### Obiekty App i Gui 

Jak już wspomniano, w FreeCAD wszystko jest rozdzielone na rdzeń i reprezentację. Dotyczy to również obiektów 3D. Możesz uzyskać dostęp do definiowania właściwości obiektów *(nazywanych w FreeCAD funkcjami)* poprzez moduł `App`, a także zmienić sposób ich reprezentacji na ekranie poprzez moduł `Gui`. Na przykład, sześcian posiada właściwości, które go definiują *(jak szerokość, długość, wysokość)*, które są przechowywane w obiekcie `App`, oraz właściwości reprezentacji *(jak kolor powierzchni, tryb rysowania)*, które są przechowywane w odpowiednim obiekcie `Gui`.

Ten sposób działania pozwala na bardzo szeroki zakres zastosowań, jak np. zlecanie algorytmów pracy tylko na części definicyjnej cech, bez konieczności dbania o część wizualną, a nawet przekierowywania zawartości dokumentu do aplikacji niegraficznych, takich jak listy, arkusze kalkulacyjne, czy analiza elementów.

Dla każdego obiektu `App` w Twoim dokumencie istnieje odpowiedni obiekt `Gui`. W rzeczywistości, sam dokument posiada zarówno `App` i obiekt `Gui`. Ma to oczywiście zastosowanie tylko wtedy, gdy uruchomisz FreeCAD z jego pełnym interfejsem. W wersji z wierszem poleceń nie istnieje GUI, więc dostępne są tylko obiekty `App`. Zauważ, że część obiektów `Gui` jest regenerowana za każdym razem, kiedy obiekt `App` jest oznaczony jako \"do ponownego obliczenia\" *(np. kiedy jeden z jego parametrów ulegnie zmianie)*, więc wszelkie zmiany dokonane bezpośrednio w obiekcie `Gui` mogą zostać utracone.

Aby uzyskać dostęp przez `App` do dowolnych części, wpisz   *


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```

gdzie `"ObjectName"` jest nazwą twojego obiektu. Możesz też wpisać   *


```python
myObject = App.ActiveDocument.ObjectName
```

Aby uzyskać dostęp do `Gui` części tego samego obiektu, wpisz   *


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```

gdzie `"ObjectName"` jest nazwą twojego obiektu. Możesz też wpisać   *


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```

Jeśli jesteś w trybie linii poleceń i nie masz GUI, ostatnia linia zwróci `None`. {{Top}}

### Obiekty dokumentu 

W FreeCAD całość Twojej pracy znajduje się wewnątrz dokumentów. Dokument zawiera Twoją geometrię i może być zapisany do pliku. Można otworzyć kilka dokumentów w tym samym czasie. Dokument, podobnie jak geometria zawarta wewnątrz, posiada obiekty `App` i `Gui`. Obiekt `App` zawiera twoje aktualne definicje geometrii, podczas gdy obiekt `Gui` zawiera różne widoki twojego dokumentu. Możesz otworzyć kilka okien, z których każde przedstawia Twoją pracę z innym współczynnikiem powiększenia lub z innego kierunku. Wszystkie te widoki są częścią obiektu `Gui` twojego dokumentu.

Aby uzyskać dostęp przez `App` do części aktualnie otwartego *(aktywnego)* dokumentu, należy wpisać   *


```python
myDocument = App.ActiveDocument
```

Aby utworzyć nowy dokument, wpisz   *


```python
myDocument = App.newDocument("Document Name")
```

Aby uzyskać dostęp przez `Gui` do części aktualnie otwartego *(aktywnego)* dokumentu, wpisz   *


```python
myGuiDocument = Gui.ActiveDocument
```

Aby uzyskać dostęp do bieżącego widoku, należy wpisać   *


```python
myView = Gui.ActiveDocument.ActiveView
```


{{Top}}

## Używanie dodatkowych modułów 

Moduły `FreeCAD` i `FreeCADGui` są odpowiedzialne tylko za tworzenie i zarządzanie obiektami w dokumencie FreeCAD. W rzeczywistości nie robią one nic więcej, jak tworzenie lub modyfikowanie geometrii. Dzieje się tak, ponieważ geometria ta może być kilku typów i dlatego wymaga dodatkowych modułów, z których każdy jest odpowiedzialny za zarządzanie danym typem geometrii. Na przykład, środowisko pracy [Część](Part_Workbench/pl.md), używa jądra OpenCascade, jest ono w stanie tworzyć i manipulować geometrią typu [BRep](http   *//en.wikipedia.org/wiki/Boundary_representation). Natomiast środowisko pracy [Sziatka](Mesh_Workbench/pl.md) jest w stanie budować i modyfikować obiekty typu siatka. W ten sposób FreeCAD jest w stanie obsłużyć wiele różnych typów obiektów, które mogą współistnieć w tym samym dokumencie, a nowe typy mogą być łatwo dodawane w przyszłości. {{Top}}

### Tworzenie obiektów 

Każdy moduł ma swój własny sposób zarządzania geometrią, ale jedną rzeczą, którą zazwyczaj mogą zrobić wszystkie, jest tworzenie obiektów w dokumencie. Ale dokument FreeCAD jest również świadomy dostępnych typów obiektów dostarczanych przez te moduły   *


```python
FreeCAD.ActiveDocument.supportedTypes()
```

wyświetli listę wszystkich możliwych obiektów, które można utworzyć. Na przykład, stwórzmy siatkę *(obsługiwaną przez moduł `Mesh`)* i część *(obsługiwaną przez moduł `Part`)*   *


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh   *   *Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part   *   *Feature", "myPartName")
```

Pierwszym argumentem jest typ obiektu, drugim nazwa obiektu. Nasze dwa obiekty wyglądają prawie tak samo   * nie zawierają jeszcze żadnej geometrii, a większość ich właściwości jest taka sama, gdy sprawdzamy je przy pomocy `dir(myMesh)` i `dir(myPart)`. Z wyjątkiem jednej rzeczy, `myMesh` ma własność `Mesh` i `myPart` ma własność `Shape`. Tam właśnie przechowywane są dane siatki i części. Na przykład, stwórzmy kostkę `Part` i przechowujmy ją w naszym obiekcie `myPart`   *


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Możesz spróbować przechować kostkę wewnątrz właściwości `Mesh` obiektu `myMesh`, ale operacja zwróci błąd. To dlatego, że każda właściwość jest stworzona do przechowywania tylko pewnego typu. We właściwości `Mesh` można zapisywać tylko rzeczy utworzone za pomocą Środowiska pracy `Mesh`. Zauważ, że większość modułów posiada również skrót do dodania ich geometrii do dokumentu   *


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```


{{Top}}

### Modyfikowanie obiektów 

Modyfikowanie obiektu odbywa się w ten sam sposób   *


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Teraz zmieńmy kształt na większy   *


```python
biggercube = Part.makeBox(5, 5, 5)
myPart.Shape = biggercube
```


{{Top}}

### Zapytania o obiekty 

Zawsze możesz sprawdzić typ obiektu w ten sposób   *


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```

lub sprawdzić, czy obiekt jest pochodną jednej z podstawowych własności (część, siatka itp.)   *


```python
print(myObj.isDerivedFrom("Part   *   *Feature"))
```

Teraz naprawdę możesz zacząć zabawę z FreeCAD! Pełna lista dostępnych modułów i ich narzędzi znajduje się w sekcji [Category   *API](   *Category_API.md). {{Top}}


{{docnav/pl
|[Poradnik   * Tworzenie skryptów Python](Python_scripting_tutorial/pl.md)
|[Skrypty w środowisku Część](Part_scripting/pl.md)
}}




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > FreeCAD Scripting Basics/pl
