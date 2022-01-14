# <img alt="Icono del ambiente Prueba" src=images/Workbench_Test.svg  style="width:64px;"> Testing/es


{{TOCright}}

## Introducción


<div class="mw-translate-fuzzy">

El [Ambiente de trabajo del marco Pruebas](Testing/es.md) no es realmente un ambiente de trabajo de modelado, pero contiene un conjunto de scripts de [Python](Python/es.md) para realizar diferentes pruebas en los componentes principales de FreeCAD, con el fin de depurar problemas. Ver también [depuración](debugging/es.md).


</div>

Puede ejecutar las pruebas desde la línea de comandos, utilizando las opciones `-t` o `--run-test`.

Ejecutar todas las pruebas:


```python
freecad --run-test 0
```

Ejecutar sólo algunas de las pruebas unitarias especificadas, por ejemplo:


```python
freecad -t TestDraft
```

## Menú de prueba 

Cada directorio de nivel superior en FreeCAD debe tener un archivo con las pruebas que se pueden ejecutar para ese ambiente de trabajo o módulo en particular. El archivo suele empezar con la palabra `Test`.

Para ejecutar una prueba desde FreeCAD, cambia al ambiente de trabajo Pruebas, luego **Comandos de prueba → TestHierramientasGui → Autoprueba → Seleccionar nombre de la prueba**, luego introduce el nombre del archivo Python con las pruebas; por ejemplo, para el [Ambiente de trabajo Borrador](Draft_Workbench/es.md), esto sería **PruebaBorrador**, luego presiona **Inicio**.

## Funciones de prueba 

Esta es la lista de aplicaciones de prueba a partir de la versión 0.15 git 4207:

### TestAPP.All

Add test function

### BaseTests

Add test function

### UnitTests

Add test function

### Documento

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

### Ambiente de trabajo 

Add test function

### Menú

Add test function

### Menu.MenuDeleteCases

Add test function

### Menu.MenuCreateCases

Add test function

## Guionización


**Ver también:**

[Básicos de Guionización FreeCAD](FreeCAD_Scripting_Basics/es.md).

### Ejemplo 1 

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

## Recursos adicionales 

### Temas del foro 

-   [Support for running specific unit tests with \--run-test \#331](https://forum.freecadweb.org/viewtopic.php?style=3&f=27&t=18379)







[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Test Framework](Category_Test_Framework.md) [<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md) [<img src="images/Property.png" style="width:16px"> Testing](Category_Testing.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Testing/es
