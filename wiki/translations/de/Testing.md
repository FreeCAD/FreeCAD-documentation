# <img alt="Erprobung Arbeitsbereichssymbol" src=images/Workbench_Test.svg  style="width   *64px;"> Testing/de


{{TOCright}}

## Einführung


<div class="mw-translate-fuzzy">

Die [Erprobung](Testing/de.md) ist nicht wirklich eine Modellierungsarbeitsbereich, aber sie enthält einen Satz von [Python](Python/de.md) Skripten, um verschiedene Tests an den Kernkomponenten von FreeCAD durchzuführen, um Probleme zu beheben. Siehe auch [Fehlerdiagnose](Debugging/de.md).


</div>

Du kannst die Tests auf der Kommandozeile ausführen, indem du die Optionen `-t` oder `--run-test` verwendest.

Führe alle Tests durch   *


```python
freecad --run-test 0
```

Führe nur einen Teil des angegebenen Komponententests aus, z.B.   *


```python
freecad -t TestDraft
```

If a test does not need the GUI, it can also be executed in console mode by setting the `-c` or `--console` option in addition. This usually results in much faster startup time as the GUI is not loaded. For example   *


```python
freecad -c -t TestPartDesignApp
```

## Testmenü

Jedes oberste Verzeichnis in FreeCAD sollte eine Datei mit den Tests haben, die für diesen speziellen Arbeitsbereich oder dieses Modul ausgeführt werden können. Die Datei beginnt normalerweise mit dem Wort `Test`.

Um einen Test aus FreeCAD heraus auszuführen, wechsle in den Test Arbeitsbereich, dann {{MenuCommand/de|Testbefehle → TestWerkzeugeGui → Selbsttest → Wähle Testbezeichnung}}, gib dann den Namen der Python Datei mit den Tests ein; z.B. für die [Draft Arbeitsbereich](Draft_Workbench/de.md) wäre dies {{MenuCommand/de|TestEntwurf}}, dann drücke **Start**.

## Testfunktionen

Dies ist die Liste der Testanwendungen ab 0.15 git 4207   *

### TestAPP.All

Testfunktion hinzufügen

### Basistests

Testfunktion hinzufügen

### EinheitTests

Testfunktion hinzufügen

### Dokument

Testfunktion hinzufügen

### UnicodeTests

Testfunktion hinzufügen

### MeshTestsApp

Testfunktion hinzufügen

### TestDraft

Testfunktion hinzufügen

### TestSketcherApp

Testfunktion hinzufügen

### TestPartApp

Testfunktion hinzufügen

### TestPartDesignApp

Testfunktion hinzufügen

### TestPartApp 

Path workbench test cases   *

-   depthTestCases   *
-   PathTestUtils   *
-   TestDressupDogbone   * Test functionality of Dogbone dressup.
-   TestHoldingTags   * Test functionality of Holding Tags dressup.
-   TestPathAdaptive   * Test selection capability of Adaptive operation.
-   TestPathCore   * Test core functionality of Path workbench.
-   TestPathDeburr   * Test general functionality of Deburr operation.
-   TestPathGeom   * Test various functions available in the PathGeom module.
-   TestPathHelix   * Test general functionality of Helix operation.
-   TestPathLog   * Test various functions available in the PathLog debugging and feedback module.
-   TestPathOpTools   *
-   TestPathPreferences   * Test various functions available in the PathPreferences module.
-   TestPathPropertyBag   *
-   TestPathSetupSheet   *
-   TestPathStock   *
-   TestPathThreadMilling   *
-   TestPathTool   *
-   TestPathToolBit   *
-   TestPathToolController   *
-   TestPathTooltable   *
-   TestPathUtil   * Test various functions available in the PathUtil module.
-   TestPathVcarve   * Test general functionality of Vcarve operation.
-   TestPathVoronoi   *

### Arbeitsbereich

Testfunktion hinzufügen

### Menü

Testfunktion hinzufügen

### Menu.MenuDeleteCases

Testfunktion hinzufügen

### Menu.MenuCreateCases

Testfunktion hinzufügen

## Skripten


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

### Get a list of all top-level test modules 


```python
FreeCAD.__unit_test__
```

Note that the test modules returned here depend on whether a GUI available or not. I.e. when executed in console mode, various tests ending in \"Gui\" are missing.

### Run specific tests 

There are various ways of running tests using [Python\'s unittest library](https   *//docs.python.org/3/library/unittest.html). FreeCAD\'s test framework removes some of the boiler plate for the most common cases.

Run all tests defined in a Python module   * 
```python
import Test, TestFemApp
Test.runTestsFromModule(TestFemApp)
```

Run all tests defined in a Python class   * 
```python
import Test, femtest.app.test_solver_calculix
Test.runTestsFromClass(femtest.app.test_solver_calculix.TestSolverCalculix)
```

### Beispiel 1 

Innerhalb der Python-Konsole von FreeCAD kann das folgende Code-Format benutzt werden, um eingebaute Tests auszuführen. Ersetze den roten \"**TestFem**\"-Text im folgenden Code mit dem gewünschten Namen des Testmoduls.

-   Benutze bspw. \"**TestPathApp**\", um alle Einheitentests für das Path-Arbeitsgebiet Einheitentest-Gerüst auszuführen.

-   Untermodule sind über die Punktnotation verfügbar, wie \"**TestPathApp.TestPathAdaptive**\", um nur die adaptiven Einheitentestd innerhalb des größeren Path-Arbeitsgebiets-Test-Gerüsts auszuführen.
-   Mehrere Testmodule oder Untermodule können kombiniert werden durch hinzufügen eines weiteren \**suite.addTest(\...)**\-Methoden-Aufrufs genau wie der im folgenden Code, aber mit einer anderen Modul- oder Untermodul-Referenz.
-   Die Ausgaben des folgenden Codes werden im Reportansichts-Paneel innerhalb der FreeCAD-GUI angezeigt.
-   Der Quell-Code wurde aus dem Beitrag des FreeCAD-Forum-Benutzers *sgrogan* kopiert, im [unit tests per python](https   *//forum.freecadweb.org/viewtopic.php?style=3&p=153251#p153251)-Thema, mit dortiger Nennung von Forum-Benutzer *wmayer*.


```python
import unittest
suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromName("TestFem"))
r = unittest.TextTestRunner()
r.run(suite)
```

## Zusätzliche Quellen 

### Forum-Themen 

-   [Support for running specific unit tests with \--run-test \#331](https   *//forum.freecadweb.org/viewtopic.php?style=3&f=27&t=18379) (Unterstützung für die Ausführung bestimmter Einheitentests mit \--run-test \#331)







[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Test Framework](Category_Test_Framework.md) [Category   *Workbenches](Category_Workbenches.md) [Category   *Testing](Category_Testing.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Test Framework](Category_Test Framework.md) > [Workbenches](Category_Workbenches.md) > [Testing](Category_Testing.md) > Testing/de
