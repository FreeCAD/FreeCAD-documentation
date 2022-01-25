# <img alt="Icône de l\'atelier Test" src=images/Workbench_Test.svg  style="width:64px;"> Testing/fr


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

Si un test ne nécessite pas l\'interface graphique, il peut également être exécuté en mode console en définissant l\'option `-c` ou `--console` en plus. Cela se traduit généralement par un démarrage beaucoup plus rapide car l\'interface graphique n\'est pas chargée. Par exemple :


```python
freecad -c -t TestPartDesignApp
```

## Menu Test 

Chaque répertoire de niveau supérieur de FreeCAD doit contenir un fichier avec les tests pouvant être exécutés pour cet atelier ou ce module particulier. Le fichier commence généralement par le mot `Test`.

Pour exécuter un test depuis FreeCAD, passez à l\'atelier Test puis **Commandes de test → TestToolsGui → Autotest → Sélectionnez le nom du test**, puis entrez le nom du fichier Python avec les tests. Par exemple, pour l\'[atelier Draft](Draft_Workbench/fr.md), il s\'agirait de **TestDraft** puis appuyez sur **Start**.

## Fonctions de test 

Voici la liste des applications de test à partir de 0.15 Git 4207 :

### TestAPP.All

Ajoute la fonction de test

### BaseTests

Ajoute la fonction de test

### UnitTests

Ajoute la fonction de test

### Document

Ajoute la fonction de test

### UnicodeTests

Ajoute la fonction de test

### MeshTestsApp

Ajoute la fonction de test

### TestDraft

Ajoute la fonction de test

### TestSketcherApp

Ajoute la fonction de test

### TestPartApp

Ajoute la fonction de test

### TestPartDesignApp

Ajoute la fonction de test

### TestPathApp

Exemples de tests pour l\'atelier Path :

-   depthTestCases :
-   PathTestUtils :
-   TestDressupDogbone : Tester la fonctionnalité de l\'habillage de Dogbone.
-   TestHoldingTags : Test de la fonctionnalité d\'habillage des étiquettes de maintien.
-   TestPathAdaptive : Test de la capacité de sélection du fonctionnement adaptatif.
-   TestPathCore : Test de la fonctionnalité de base de l\'atelier Path.
-   TestPathDeburr : Test de la fonctionnalité générale de l\'opération Deburr.
-   TestPathGeom : Test de diverses fonctions disponibles dans le module PathGeom.
-   TestPathHelix : Test de la fonctionnalité générale de l\'opération Helix.
-   TestPathLog : Teste diverses fonctions disponibles dans le module de débogage et de feedback PathLog.
-   TestPathOpTools :
-   TestPathPreferences : Testez diverses fonctions disponibles dans le module PathPreferences.
-   TestPathPropertyBag :
-   TestPathSetupSheet :
-   TestPathStock :
-   TestPathThreadMilling :
-   TestPathTool :
-   TestPathToolBit :
-   TestPathToolController :
-   TestPathTooltable :
-   TestPathUtil : Tester diverses fonctions disponibles dans le module PathUtil.
-   TestPathVcarve : Teste la fonctionnalité générale de l\'opération Vcarve.
-   TestPathVoronoi :

### Workbench

Ajoute la fonction de test

### Menu

Ajoute la fonction de test

### Menu.MenuDeleteCases

Ajoute la fonction de test

### Menu.MenuCreateCases

Ajoute la fonction de test

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

### Exemple 1 

Dans la console Python de FreeCAD, le format de code suivant peut être utilisé pour exécuter des tests intégrés. Remplacez le texte rouge \"**TestFem**\" dans le code ci-dessous par le nom du module de test souhaité.

-   Par exemple, utilisez \"**TestPathApp**\" pour exécuter tous les tests unitaires du cadre de test unitaire de l\'atelier Path.
-   Les sous-modules sont disponibles en utilisant la notation par points, comme \"**TestPathApp.TestPathAdaptive**\" pour n\'exécuter que les tests unitaires Adaptive dans le cadre de test plus large de l\'atelier Path.
-   Plusieurs modules ou sous-modules de test peuvent être combinés en ajoutant un autre appel de méthode \**suite.addTest(\...)**\ comme celui du code ci-dessous mais avec une référence de module ou de sous-module différente.
-   La sortie pour le code ci-dessous sera dans le panneau Report View dans le FreeCAD GUI.
-   La source du code est copiée à partir d\'un message de l\'utilisateur du forum FreeCAD, *sgrogan*, dans le sujet [unit tests per python](https://forum.freecadweb.org/viewtopic.php?style=3&p=153251#p153251), avec le crédit donné à l\'utilisateur du forum, *wmayer*.


```python
import unittest
suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromName("TestFem"))
r = unittest.TextTestRunner()
r.run(suite)
```

## Ressources additionnelles 

### Sujets du forum 

-   [Support for running specific unit tests with \--run-test \#331](https://forum.freecadweb.org/viewtopic.php?style=3&f=27&t=18379)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Test Framework](Category_Test Framework.md) > [Workbenches](Category_Workbenches.md) > [Testing](Category_Testing.md) > Testing/fr
