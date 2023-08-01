# <img alt="Ikonka FreeCAD dla środowiska pracy Test" src=images/Workbench_Test.svg  style="width:64px;"> Testing/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy [Test](Testing/pl.md) nie jest tak naprawdę programem do modelowania, ale zawiera zestaw skryptów środowiska [Python](Python/pl.md) do wykonywania różnych testów na głównych komponentach programu FreeCAD w celu usuwania problemów. Zobacz także stronę [debugowanie](Debugging/pl.md).

Testy można uruchamiać z wiersza poleceń, używając opcji `-t` lub `--run-test`.

Przeprowadzenie wszystkich testów:


```python
freecad --run-test 0
```

Przeprowadzenie tylko niektórych testów jednostkowych, np:


```python
freecad -t TestDraft
```

Jeśli test nie wymaga GUI, można go także wykonać w trybie konsoli, ustawiając dodatkowo opcję `-c` lub `--console`. Zwykle powoduje to znacznie szybszy czas uruchamiania, ponieważ GUI nie jest ładowane. Na przykład:


```python
freecad -c -t TestPartDesignApp
```

## Menu Narzędzia test 

W każdym katalogu najwyższego poziomu w programie FreeCAD powinien znajdować się plik z testami, które można uruchomić dla danego programu lub modułu. Plik ten zwykle zaczyna się od słowa `Test`.

Aby uruchomić test z poziomu programu FreeCAD, należy przejść do środowiska Test Workbench, następnie **Test commands → TestToolsGui → Self test → Select test name**, a następnie wpisać nazwę pliku Python z testami. Na przykład dla środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) będzie to **TestDraft**, po czym należy nacisnąć przycisk **Start**.

## Funkcje testujące 

To jest lista aplikacji testowych od wersji 0.15 git 4207:

### TestAPP.All

Dodanie funkcji testowania

### Testy podstawowe 

Dodaj funkcje testowania

### Testy jednostkowe 

Dodaj funkcje testowania

### Dokument

Dodaj funkcje testowania

### Testy Unicode 

Dodaj funkcje testowania

### MeshTestsApp

Dodaj funkcje testowania

### Test środowiska Rysunek Roboczy 

Dodaj funkcje testowania

### TestSketcherApp

Dodaj funkcje testowania

### TestPartApp

Dodaj funkcje testowania

### TestPartDesignApp

Dodaj funkcje testowania

### TestPathApp

Testowanie środowiska pracy Path:

-   depthTestCases:
-   PathTestUtils:
-   TestDressupDogbone: Test funkcjonalności ulepszenia podcięcia w narożnikach.
-   TestHoldingTags: Test funkcjonalności ulepszenia mostki utrzymujące.
-   TestPathAdaptive: Testowanie możliwości wyboru trybu pracy adaptacyjnej.
-   TestPathCore:Test głównych funkcji środowiska pracy Path.
-   TestPathDeburr: Test ogólnej funkcjonalności operacji usuwania zadziorów.
-   TestPathGeom: Test różnych funkcji dostępnych w module PathGeom.
-   TestPathHelix: Test ogólnej funkcjonalności działania operacji Helisy.
-   TestPathLog: Przetestuj różne funkcje dostępne w module debugowania i informacji zwrotnej PathLog.
-   TestPathOpTools:
-   TestPathPreferences: Test różnych funkcji dostępnych w module PathPreferences.
-   TestPathPropertyBag:
-   TestPathSetupSheet:
-   TestPathStock:
-   TestPathThreadMilling:
-   TestPathTool:
-   TestPathToolBit:
-   TestPathToolController:
-   TestPathTooltable:
-   TestPathUtil: Test różnych funkcji dostępnych w module PathUtil.
-   TestPathVcarve: Test ogólnej funkcjonalności działania funkcji Vcarve.
-   TestPathVoronoi:

### Środowiska pracy 

Dodaj funkcje testowania

### Menu

Dodaj funkcje testowania

### Menu.MenuDeleteCases

Dodaj funkcje testowania

### Menu.MenuCreateCases

Dodaj funkcje testowania

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

### Wyświetl listę wszystkich modułów testowych najwyższego poziomu 


```python
FreeCAD.__unit_test__
```

Należy zauważyć, że zwracane tutaj moduły testowe zależą od tego, czy dostępny jest interfejs graficzny, czy nie. Tzn. jeśli test jest wykonywany w trybie konsoli, brakuje różnych testów kończących się na \"Gui\".

### Wykonaj określone testy 

Istnieje wiele sposobów uruchamiania testów przy użyciu [biblioteki unittest Python](https://docs.python.org/3/library/unittest.html). Szkielet testowy programu FreeCAD usuwa niektóre z najczęściej występujących przypadków.

Uruchamia wszystkie testy zdefiniowane w module Python: 
```python
import Test, TestFemApp
Test.runTestsFromModule(TestFemApp)
```

Uruchamia wszystkie testy zdefiniowane w klasie Python: 
```python
import Test, femtest.app.test_solver_calculix
Test.runTestsFromClass(femtest.app.test_solver_calculix.TestSolverCalculix)
```

### Przykład 1 

W konsoli Pythona programu FreeCAD do uruchamiania wbudowanych testów można użyć kodu w następującym formacie. Zamień tekst w kolorze czerwonym `"TestFem"` w poniższym kodzie na nazwę żądanego testu modułu.

-   Na przykład użyj `TestPathApp`, aby uruchomić wszystkie testy jednostkowe środowiska pracy Path.
-   Moduły podrzędne są dostępne przy użyciu notacji kropkowej, na przykład `TestPathApp.TestPathAdaptive`, aby uruchomić tylko testy jednostkowe Adaptive w ramach większego frameworka testowego środowiska pracy Path.
-   Wiele modułów testowych lub modułów podrzędnych można połączyć, dodając kolejne wywołanie metody `suite.addTest(...)`, tak jak w poniższym kodzie, ale z innym odniesieniem do modułu lub modułu podrzędnego.
-   Dane wyjściowe poniższego kodu będą znajdować się w panelu Widoku raportu w graficznym interfejsie użytkownika programu FreeCAD.
-   Źródło kodu jest skopiowane z postu użytkownika forum FreeCAD, *sgrogana*, w temacie [testy jednostkowe w pythonie](https://forum.freecadweb.org/viewtopic.php?style=3&p=153251#p153251), z przypisaniem do użytkownika forum, *wmayer*.


```python
import unittest
suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromName("TestFem"))
r = unittest.TextTestRunner()
r.run(suite)
```

## Zasoby dodatkowe 

### Tematy na forum 

-   [Support for running specific test jednostkowy z \--run-test #331](https://forum.freecadweb.org/viewtopic.php?style=3&f=27&t=18379)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Test Framework](Category_Test Framework.md) > [Workbenches](Category_Workbenches.md) > [Testing](Category_Testing.md) > Testing/pl
