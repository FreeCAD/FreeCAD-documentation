# <img alt="Логотип верстака для тестирования" src=images/Workbench_Test.svg  style="width:64px;"> Testing/ru


{{TOCright}}

## Введение


<div class="mw-translate-fuzzy">

FreeCAD поставляется с обширным модулем тестирования. Тестирование основано на наборе Python сценариев расположенных в тестовом(test) модуле.


</div>

You can run the tests from the command line, by using the `-t` or `--run-test` options.

Запустите все тесты:


```python
freecad --run-test 0
```

Run only some the specified unit test, for example:


```python
freecad -t TestDraft
```

## Меню тестирования 

Each top level directory in FreeCAD should have a file with the tests that can be run for that particular workbench or module. The file usually starts with the word `Test`.

To run a test from within FreeCAD, switch to the Test Workbench, then **Test commands → TestToolsGui → Self test → Select test name**, then enter the name of the Python file with the tests; for example, for the [Draft Workbench](Draft_Workbench.md), this would be **TestDraft**, then press **Start**.

## Test functions 


<div class="mw-translate-fuzzy">

## Функции тестирования 

Это список тестовых приложений на 0.15 Git 4207:


</div>


<div class="mw-translate-fuzzy">

### TestAPP.All

Добавить функцию тестирования


</div>

Add test function

### BaseTests

Add test function

### UnitTests

Add test function

### Document

Add test function

### UnicodeTests

Add test function

### MeshTestsApp

Add test function

### TestDraft

Add test function

### TestSketcherApp

Add test function

### TestPartApp

Add test function

### TestPartDesignApp

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

### Workbench

Add test function

### Menu

Add test function

### Menu.MenuDeleteCases

Add test function

### Menu.MenuCreateCases

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







[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Test Framework](Category_Test_Framework.md) [<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md) [<img src="images/Property.png" style="width:16px"> Testing](Category_Testing.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Testing/ru
