# FreeCAD Build Tool/it
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Introduzione

Lo **Strumento per la costruzione di FreeCAD** (FreeCAD build tool o **fcbt**) è uno script in Python ubicato in 
```python
trunc/src/Tools/fcbt.py
``` Può essere usato per semplificare alcune frequenti operazioni nella costruzione, distribuzione e estensione di FreeCAD.

### Utilizzo

Con [Python](wikipedia:Python_(programming_language).md) installato correttamente, *fcbt* può essere richiamato con il comando 
```python
python fbct.py
``` che visualizza un menu, in cui è possibile selezionare l\'operazione che si desidera utilizzare per: 
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

Al prompt inserire il comando abbreviato che si desidera utilizzare. Ad esempio digitare \"CM\" per [creare un modulo](Module_Creation/it.md).


</div>

#### DistSrc

Il comando \"DS\" **crea una distribuzione di codice sorgente** dell\'albero di codice sorgente attuale.

#### DistBin

Il comando \"DB\" **crea una distribuzione binaria** dell\'albero di codice sorgente attuale.

#### DistSetup

Il comando \"DI\" **crea una distribuzione di setup** dell\'albero di codice sorgente attuale.

#### DistSetup 

Il comando \"DUI\" **crea una distribuzione di setup dell\'utente** dell\'albero di codice sorgente attuale.

#### DistAll

Il comando \"DA\" esegue \"DS\", \"DB\" e \"DI\" in sequenza.

#### NextBuildNumber

Il comando \"NBN\" **incrementa il numero della costruzione** per creare una nuova versione di FreeCAD.


<div class="mw-translate-fuzzy">

#### CreateModule

Il comando \"CM\" [crea un nuovo modulo dell\'applicazione](Module_Creation/it.md).


</div>


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > FreeCAD Build Tool/it
