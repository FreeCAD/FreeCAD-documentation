# Testing/it
<div class="mw-translate-fuzzy">


{{docnav/it|[Correggere i bug](Debugging/it.md)|[Integrazione continua](Continuous_Integration/it.md)}}


</div>

<img alt="Test workbench icon" src=images/Workbench_Test.svg  style="width:128px;">


{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

[Test Framework](Test_Framework/it.md) non è in realtà un ambiente di modellazione, ma contiene un set di script [Python](Python/it.md) per eseguire diversi test sui componenti principali di FreeCAD, al fine di eseguire il debug dei problemi. Vedere anche come [eliminare gli errori](debugging/it.md).


</div>

You can run the tests from the command line, by using the `-t` or `--run-test` options.

Run all tests:


```python
freecad --run-test 0
```

Run only some the specified unit test, for example:


```python
freecad -t TestDraft
```

If a test does not need the GUI, it can also be executed in console mode by setting the `-c` or `--console` option in addition. This usually results in much faster startup time as the GUI is not loaded. For example:


```python
freecad -c -t TestPartDesignApp
```

## Test menu 

Each top level directory in FreeCAD should have a file with the tests that can be run for that particular workbench or module. The file usually starts with the word `Test`.

To run a test from within FreeCAD, switch to the Test Workbench, then **Test commands → TestToolsGui → Self test → Select test name**, then enter the name of the Python file with the tests; for example, for the [Draft Workbench](Draft_Workbench.md), this would be **TestDraft**, then press **Start**.

## Test functions 


<div class="mw-translate-fuzzy">

## Funzioni di test 

Questa è la lista delle applicazioni di test di 0.15 Git 4207:


</div>


<div class="mw-translate-fuzzy">

### TestAPP.All

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### BaseTests

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### UnitTests

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### Document

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### UnicodeTests

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### MeshTestsApp

Add test function


</div>

Add test function

### TestDraft

Add test function


<div class="mw-translate-fuzzy">

### TestSketcherApp

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### TestPartApp

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### TestPartDesignApp

Add test function


</div>

Add test function

### TestPathApp

Path workbench test cases:

-   depthTestCases:
-   PathTestUtils:
-   TestDressupDogbone: Test functionality of Dogbone dressup.
-   TestHoldingTags: Test functionality of Holding Tags dressup.
-   TestPathAdaptive: Test selection capability of Adaptive operation.
-   TestPathCore: Test core functionality of Path workbench.
-   TestPathDeburr: Test general functionality of Deburr operation.
-   TestPathGeom: Test various functions available in the PathGeom module.
-   TestPathHelix: Test general functionality of Helix operation.
-   TestPathLog: Test various functions available in the PathLog debugging and feedback module.
-   TestPathOpTools:
-   TestPathPreferences: Test various functions available in the PathPreferences module.
-   TestPathPropertyBag:
-   TestPathSetupSheet:
-   TestPathStock:
-   TestPathThreadMilling:
-   TestPathTool:
-   TestPathToolBit:
-   TestPathToolController:
-   TestPathTooltable:
-   TestPathUtil: Test various functions available in the PathUtil module.
-   TestPathVcarve: Test general functionality of Vcarve operation.
-   TestPathVoronoi:


<div class="mw-translate-fuzzy">

### Workbench

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### Menu

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### Menu.MenuDeleteCases

Add test function


</div>

Add test function


<div class="mw-translate-fuzzy">

### Menu.MenuCreateCases

Add test function


</div>

Add test function

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

### Example 1 

Within the Python Console of FreeCAD, the following code format may be used to run built-in tests. Replace the red \"**TestFem**\" text in the code below with the desired module test name.

-   For example, use \"**TestPathApp**\" to run all unit tests for the Path workbench unit test framework.
-   Submodules are available using dot notation, like \"**TestPathApp.TestPathAdaptive**\" to only run the Adaptive unit tests within the greater Path workbench test framework.
-   Multiple test modules or submodules may be combined by adding another \**suite.addTest(\...)**\ method call just like the one in the code below, but with a different module or submodule reference.
-   Output for the code below will be in the Report View panel within the FreeCAD GUI.
-   Code source is copied from post by FreeCAD forum user, *sgrogan*, in the [unit tests per python](https://forum.freecadweb.org/viewtopic.php?style=3&p=153251#p153251) topic, with credit there given to forum user, *wmayer*.


```python
import unittest
suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromName("TestFem"))
r = unittest.TextTestRunner()
r.run(suite)
```

## Additional Resources 

### Forum Topics 

-   [Support for running specific unit tests with \--run-test \#331](https://forum.freecadweb.org/viewtopic.php?style=3&f=27&t=18379)


<div class="mw-translate-fuzzy">


{{docnav/it|[Correggere i bug](Debugging/it.md)|[Integrazione continua](Continuous_Integration/it.md)}}


</div>




[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Test Framework](Category_Test_Framework.md) [<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md) [<img src="images/Property.png" style="width:16px"> Testing](Category_Testing.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Testing/it
