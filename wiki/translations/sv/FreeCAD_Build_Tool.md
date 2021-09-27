# FreeCAD Build Tool/sv
{{TOCright}}


<div class="mw-translate-fuzzy">

**FreeCAD byggverktyg** eller **fcbt** är ett pythonskript placerat i


</div>


```python
trunc/src/Tools/fcbt.py
```

Det kan användas till att förenkla en del frekventa uppgifter vid byggande, distribution och utökning av FreeCAD.

## Bruk

Med _ korrekt installerat, så kan *fcbt* startas med kommandot 
```python
python fbct.py
``` det visar en meny, där du kan välja den uppgift som du vill använda den till: 
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

Mata vid inmatningsprompten in det förkortade kommandot som du vill använda. Skriv till exempel \"CM\" för [Skapa en modul](Module_Creation/sv.md).


</div>

### DistSrc

Kommandot \"DS\" **skapar en källdistribution** från det gällande källträdet.

### DistBin

Kommandot \"DB\" **skapar en binär distribution** från det gällande källträdet.

### DistSetup

Kommandot \"DI\" **skapar en setup distribution** från det gällande källträdet.

### DistSetup 

Kommandot \"DUI\" \'\'\'skapar en användar setup distribution från det gällande källträdet.

### DistAll

Kommandot \"DA\" utför \"DS\", \"DB\" och \"DI\" i sekvens.

### NextBuildNumber

Kommandot \"NBN\" **ökar byggnumret** för att skapa en ny släppversion av FreeCAD.


<div class="mw-translate-fuzzy">

### CreateModule

Kommandot \"CM\" [skapar en ny applikationsmodul](Module_Creation/sv.md).


</div>


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > FreeCAD Build Tool/sv
