# <img alt="FEMbyGEN Workbench icon" src=images/FEMbyGEN.svg  style="width:64px;"> FEMbyGEN Workbench/en


{{TOCright}}

## Introduction

FEMbyGEN is a FreeCAD addon. It provides a simple interface to choose the best solution by showing the structural behavior of your designs on screen for parametric analysis and multiple loading situations.

<img alt="" src=images/Generative_Design.png  style="width:512px;">

### Intended work-flow 

1.  Click initiate button to create parameters for parametric analysis.
2.  By alias button please match size and name of the parameters.
3.  Associate the spreadsheet and your model. ([Spreadsheet Workbench](Spreadsheet_Workbench.md)).
4.  Set up analysis model(s) by [FEM_Workbench](FEM_Workbench.md).
5.  Switch again to the workbench **FEMbyGEN** and by **Generate** button, create all generations.
6.  Click on the button **FEA** and Start FEA to run simulations.
7.  You can check simulation files by clicking rows of the related generation.
8.  Click on the button **Results** to get results to the master file.
9.  Summotion of all loadcases results also will be under Results in tree view.

### Features

-   Parametric FEM analysis
-   Supports multiple loadcases
-   Summarize all the results in a table
-   Sort results by your output weight
-   Summation of all loadcases

### Features to be supported in the future 

-   Topology Analysis
-   Taguchi Method to generate parametric variations

### Limitations

-   Works only for Calculix Solver

## Installation

### Addon Manager 

FEMbyGEN can easily be installed via the FreeCAD <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) from the **Tools → Addon manager** menu.

FEMbyGEN is under active development and will get new features frequently. Therefore you should update it regularly using also the menu **Tools → Addon manager**.

The FEMbyGEN code is hosted and developed [FEMbyGEN on GitHub.com](https://github.com/Serince/FEMbyGEN).

### Manual

See [How to install additional workbenches](How_to_install_additional_workbenches.md)

### Prerequisites

-   FreeCAD 0.19 or newer

## References

-   Author: Serdar Ince, Ögeday Yavuz, Rahul Jhuree
-   Source code: [FEMbyGEN on GitHub.com](https://github.com/Serince/FEMbyGEN)
-   FreeCAD Forum: <https://forum.freecadweb.org/viewtopic.php?p=626306>
-   Report bugs: Please report bugs at [FEMbyGEN on GitHub.com](https://github.com/Serince/FEMbyGEN/issues)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sandbox](Category_Sandbox.md) > [User Documentation](Category_User Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > FEMbyGEN Workbench/en
