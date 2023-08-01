# FreeCAD Build Tool/ro
{{TOCright}}


<div class="mw-translate-fuzzy">

Instrumentul de construcție **FreeCAD build tool** sau **fcbt** este un script python localizat la:


</div>


```python
trunc/src/Tools/fcbt.py
```

Acesta poate fi folosit pentru a simplifica unele sarcini frecvente în construirea, distribuirea și extinderea FreeCAD.

## Utilizare

Cu [Python](wikipedia:Python_(programming_language).md) corect instalat, *fcbt* can poate fi invocat prin comanda 
```python
python fbct.py
``` Afișează un meniu, unde puteți selecta următoarele: 
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
```


<div class="mw-translate-fuzzy">

La promptul de introducere introduceți comanda abreviată pe care doriți să o apelați. De exemplu, tastați \"CM\" pentru crearea unui modul [creating a workbench](Workbench_creation/ro.md).


</div>

### DistSrc

Comanda \"DS\" **creează sursa de distribuire** a arborelui sursă curent

### DistBin

Comanda \"DB\" **creează o distribuție binară** a arborelui sursă curent.

### DistSetup

Comanda \"DI\" \'\'\'creează o distribuție de instalare a arborelui sursă curent.

### DistSetup 

Comanda \"DUI\" \'\'\'creează o distribuție de configurare utilizator a arborelui sursă curent.

### DistAll

Comanda \"DA\" execută secvența \"DS\", \"DB\" and \"DI\" .

### NextBuildNumber

Comanda \"NBN\" \'\'\'incrementează numărul de compilări pentru a crea noua veresiiune FreeCAD.


<div class="mw-translate-fuzzy">

### CreateModule

Comanda \"CM\" [creates a new application module (Workbench)](Workbench_creation/ro.md).


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > FreeCAD Build Tool/ro
