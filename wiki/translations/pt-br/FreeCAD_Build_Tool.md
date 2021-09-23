# FreeCAD Build Tool/pt-br






{{TOCright}}

## Overview

The **FreeCAD build tool** or **fcbt** is a python script located at 
```python
trunc/src/Tools/fcbt.py
``` It can be used to simplify some frequent tasks in building, distributing and extending FreeCAD.

## Usage

With [Python](wikipedia:Python_(programming_language).md) correctly installed, *fcbt* can be invoked by the command 
```python
python fbct.py
``` It displays a menu, where you can select the task you want to use it for: 
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
``` At the input prompt enter the abbreviated command you want to call. For example type \"CM\" for [creating a module](Workbench_creation.md).

### DistSrc

The command \"DS\" **creates a source distribution** of the current source tree.

### DistBin

The command \"DB\" **creates a binary distribution** of the current source tree.

### DistSetup

The command \"DI\" **creates a setup distribution** of the current source tree.

### DistSetup 

The command \"DUI\" **creates a user setup distribution** of the current source tree.

### DistAll

The command \"DA\" executes \"DS\", \"DB\" and \"DI\" in sequence.

### NextBuildNumber

The \"NBN\" command **increments the build number** to create a new release version of FreeCAD.

### CreateModule

The \"CM\" command [creates a new application module (Workbench)](Workbench_creation.md).





 

[Category:Developer Documentation](Category:Developer_Documentation.md)
