# FreeCAD Build Tool/fr
## Présentation

L**\'outil build de FreeCAD** (build pour construction) ou **fcbt** est un script python qui se trouve ici : 
```python
trunc/src/Tools/fcbt.py
``` Il peut être utilisé pour simplifier certaines tâches fréquemment utilisées dans la construction (compilation), la distribution et l\'extension de FreeCAD.

## Utilisation

Quand [Python](http://fr.wikipedia.org/wiki/Python_(langage)) est correctement installé, **fcbt** peut être lancé par la commande : 
```python
python fbct.py
``` Il affiche un menu, où vous pouvez sélectionner la tâche, que vous souhaitez utiliser pour : 
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
``` À l\'invite de commande, entrez la commande abrégée que vous voulez appeler. Par exemple, tapez \"CM\" pour la [création d\'atelier](Workbench_creation/fr.md).

### DistSrc

La commande \"DS\" **Crée le source de la distribution** de l\'arborescence source en court.

### DistBin

La commande \"DB\" **Créer une distribution binaire** de l\'arborescence source en court.

### DistSetup

La commande \"DI\" **crée une distribution d\'installation** de l\'arborescence source en court.

### DistSetup 

La commande \"DUI\" **crée une distribution de configuration utilisateur** de l\'arborescence source en court.

### DistAll

La commande \"DA\" exécute les séquences **\"DS\"**, **\"DB\"** et **\"DI\"**.

### NextBuildNumber

La commande \"NBN\" **incrémente le numéro de compilation** pour créer une nouvelle version de FreeCAD.

### CreateModule

La commande \"CM\" [crée un nouveau module d\'application (atelier)](Workbench_creation/fr.md).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > FreeCAD Build Tool/fr
