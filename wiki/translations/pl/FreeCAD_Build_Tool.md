# FreeCAD Build Tool/pl
## Przegląd

**FreeCAD Narzędzie do kompilacji** lub **FreeCAD build tool *(fcbt)*** jest skryptem Python znajdującym się pod adresem: 
```python
trunc/src/Tools/fcbt.py
``` Może być używany do uproszczenia niektórych częstych zadań w budowaniu, dystrybucji i rozszerzaniu FreeCAD.

## Użycie

Z prawidłowo zainstalowanym środowiskiem [Python](wikipedia:Python_(programming_language).md), *fcbt* może być wywołane poleceniem: 
```python
python fbct.py
``` Wyświetla menu, w którym można wybrać zadanie, do którego ma być używana: 
```python
FreeCAD Build Tool
 Usage:
    fcbt <command name> [command parameter]
 possible commands are:
  - DistSrc         (DS)   Build a source Distr. of the current source tree
  - DistBin         (DB)   Build a binary Distr. of the current source tree
  - DistSetup       (DI)   Build a Setup Distr. of the current source tree
  - DistSetup       (DUI)  Build a User Setup Distr. of the current source tree
  - DistAll         (DA)   Run all three above modules
  - NextBuildNumber (NBN)  Increase the Build Number of this Version
  - CreateModule    (CM)   Insert a new FreeCAD Module (Workbench) in the module directory
 
 For help on the modules type:
   fcbt <command name> ?
``` W wierszu poleceń wpisz skrót polecenia, które chcesz wywołać. Na przykład wpisz \"CM\" dla [Tworzenie środowiska pracy](Workbench_creation/pl.md).

### DistSrc

Polecenie \"DS\" **tworzy źródła dystrybucji** bieżącego drzewa źródeł.

### DistBin

Polecenie \"DB\" **tworzy binarja dystrybucji** bieżącego drzewa źródeł.

### DistSetup

Polecenie \"DI\" **tworzy konfigurację dystrybucji** bieżącego drzewa źródeł.

### DistSrc 

Polecenie \"DUI\" **tworzy konfigurację użytkownika dystrybucji** bieżącego drzewa źródeł.

### DistAll

Polecenie \"DA\" wykonuje kolejno polecenia \"DS\", \"DB\" i \"DI\".

### NextBuildNumber

Polecenie \"NBN\" **zwiększa numer kompilacji**, aby utworzyć nową wersję FreeCAD.

### CreateModule

Polecenie \"CM\" [tworzy nowy moduł aplikacji *(środowisko pracy)*](Workbench_creation/pl.md).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > FreeCAD Build Tool/pl
