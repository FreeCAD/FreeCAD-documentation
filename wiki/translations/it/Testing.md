# <img alt="Test workbench icon" src=images/Workbench_Test.svg  style="width:64px;"> Testing/it


{{TOCright}}



## Introduzione

[Test Framework](Testing/it.md) non è in realtà un ambiente di modellazione, ma contiene un set di script [Python](Python/it.md) per eseguire diversi test sui componenti principali di FreeCAD, al fine di eseguire il debug dei problemi. Vedere anche come [individuare gli errori](debugging/it.md).

Puoi avviare i test dalla riga di comando, usando le opzioni `-t` o `--run-test`.

Avvia tutti i test:


```python
freecad --run-test 0
```

Avvia solo alcuni test specificati, per esempio


```python
freecad -t TestDraft
```

Se un test non ha bisogno della GUI, può anche essere eseguito in modalità console impostando l\'opzione `-c` o `--console` in aggiunta. Questo di solito si traduce in tempi di avvio molto più rapidi poiché la GUI non viene caricata. Per esempio:


```python
freecad -c -t TestPartDesignApp
```

## Test menu 

Ogni directory di primo livello in FreeCAD dovrebbe avere un file con i test che possono essere eseguiti per quel particolare ambiente di lavoro o modulo. Il file di solito inizia con la parola `Test`.

Per eseguire un test da FreeCAD, passare all\'Ambiente Test, quindi **Test commands → TestToolsGui → Self test → Select test name**, quindi immettere il nome del file Python con i test; ad esempio, per l\' [ Ambiente Draft](Draft_Workbench/it.md), sarebbe **TestDraft**, quindi premere **Start**.



## Funzioni di test 

Questa è la lista delle applicazioni di test di 0.15 Git 4207:

### TestAPP.All

Aggiungi funzione di test

### BaseTests

Aggiungi funzione di test

### UnitTests

Aggiungi funzione di test

### Document

Aggiungi funzione di test

### UnicodeTests

Aggiungi funzione di test

### MeshTestsApp

Aggiungi funzione di test

### TestDraft

Aggiungi funzione di test

### TestSketcherApp

Aggiungi funzione di test

### TestPartApp

Aggiungi funzione di test

### TestPartDesignApp

Aggiungi funzione di test

### TestPathApp

Ambiente Path casistiche di test:

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

Aggiungi funzione di test

### Menu

Aggiungi funzione di test

### Menu.MenuDeleteCases

Aggiungi funzione di test

### Menu.MenuCreateCases

Aggiungi funzione di test

## Scripting


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)



### Ottienere un elenco di tutti i moduli di test di primo livello 


```python
FreeCAD.__unit_test__
```

Si noti che i moduli di test restituiti qui dipendono dal fatto che una GUI sia disponibile o meno. Cioè, quando viene eseguito in modalità console, mancano vari test che terminano in \"Gui\".



### Eseguire test specifici 

Esistono vari modi per eseguire test utilizzando [Python\'s unittest library](https://docs.python.org/3/library/unittest.html). Il framework di test di FreeCAD porta alla luce i casi più comuni.

Eseguire tutti i test definiti in un modulo Python: 
```python
import Test, TestFemApp
Test.runTestsFromModule(TestFemApp)
```

Eseguire tutti i test definiti in una classe Python: 
```python
import Test, femtest.app.test_solver_calculix
Test.runTestsFromClass(femtest.app.test_solver_calculix.TestSolverCalculix)
```



### Esempio 1 

All\'interno della console Python di FreeCAD, il seguente formato di codice può essere utilizzato per eseguire test incorporati. Sostituire il testo rosso \"**TestFem**\" nel codice sottostante con il nome del test del modulo desiderato.

-   Ad esempio, utilizzare \"**TestPathApp**\" per eseguire tutti gli unit test per il framework di unit test Path workbench.
-   I sottomoduli sono disponibili utilizzando la notazione a punti, ad esempio \"**TestPathApp.TestPathAdaptive**\" per eseguire solo gli unit test adattivi all\'interno del framework di test workbench Path più grande.
-   Più moduli di test o sottomoduli possono essere combinati aggiungendo un\'altra chiamata al metodo \**suite.addTest(\...)**\ proprio come quella nel codice seguente, ma con un modulo o un riferimento di sottomodulo diverso.
-   L\'output per il codice riportato di seguito sarà nel pannello Report View all\'interno della GUI di FreeCAD.
-   Il codice sorgente è copiato dal post dell\'utente del forum FreeCAD, *sgrogan*, nell\'argomento [unit test per python](https://forum.freecadweb.org/viewtopic.php?style=3&p=153251#p153251), con credito lì dato all\'utente del forum, *wmayer*.


```python
import unittest
suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromName("TestFem"))
r = unittest.TextTestRunner()
r.run(suite)
```



## Risorse aggiuntive 



### Argomenti del Forum 

-   [Support for running specific unit tests with \--run-test #331](https://forum.freecadweb.org/viewtopic.php?style=3&f=27&t=18379)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Test Framework](Category_Test Framework.md) > [Workbenches](Category_Workbenches.md) > [Testing](Category_Testing.md) > Testing/it
