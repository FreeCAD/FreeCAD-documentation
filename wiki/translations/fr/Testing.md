




<img alt="Icône de l\'atelier Test" src=images/Workbench_Test.svg  style="width:128px;">


{{TOCright}}

## Introduction

L\'[atelier Test](Testing/fr.md) n\'est pas vraiment un atelier de modélisation, mais il contient un ensemble de scripts [Python](Python/fr.md) permettant d\'effectuer différents tests sur les composants principaux de FreeCAD, afin de résoudre les problèmes. Voir aussi [Débogage](Debugging/fr.md).

Vous pouvez lancer les tests depuis la ligne de commande, en utilisant les options `-t` ou `--run-test`.

Lancer tous les tests :


```python
freecad --run-test 0
```

Exécutez uniquement quelques tests spécifiques, par exemple :


```python
freecad -t TestDraft
```

## Menu Test {#menu_test}

Chaque répertoire de niveau supérieur de FreeCAD doit contenir un fichier avec les tests pouvant être exécutés pour cet atelier ou ce module particulier. Le fichier commence généralement par le mot `Test`.

Pour exécuter un test depuis FreeCAD, passez à l\'atelier Test puis {{MenuCommand|Commandes de test → TestToolsGui → Autotest → Sélectionnez le nom du test}}, puis entrez le nom du fichier Python avec les tests. Par exemple, pour l\'[atelier Draft](Draft_Workbench/fr.md), il s\'agirait de {{MenuCommand|TestDraft}} puis appuyez sur **Start**.

## Test functions {#test_functions}


<div class="mw-translate-fuzzy">

## Fonctions de test {#fonctions_de_test}

Voici la liste des applications de test à partir de 0.15 Git 4207 :


</div>


<div class="mw-translate-fuzzy">

### TestAPP.All

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### BaseTests

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### UnitTests

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### Document

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### UnicodeTests

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### MeshTestsApp

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### TestDraft

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### TestSketcherApp

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### TestPartApp

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### TestPartDesignApp

Ajoute la fonction de test


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

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### Menu

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### Menu.MenuDeleteCases

Ajoute la fonction de test


</div>

Add test function


<div class="mw-translate-fuzzy">

### Menu.MenuCreateCases

Ajoute la fonction de test


</div>

Add test function

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

### Example 1 {#example_1}

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

## Additional Resources {#additional_resources}

### Forum Topics {#forum_topics}

-   [Support for running specific unit tests with \--run-test \#331](https://forum.freecadweb.org/viewtopic.php?style=3&f=27&t=18379)







[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Test Framework{{\#translation:}}](Category:Test_Framework.md) [Category:Workbenches{{\#translation:}}](Category:Workbenches.md) [Category:Testing{{\#translation:}}](Category:Testing.md)
