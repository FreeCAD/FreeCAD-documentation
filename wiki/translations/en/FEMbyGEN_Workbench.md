# <img alt="FEMbyGEN Workbench icon" src=images/FEMbyGEN.svg  style="width:64px;"> FEMbyGEN Workbench/en




## Introduction

FEMbyGEN is a FreeCAD addon. It provides a simple interface to choose the best solution by showing the structural behavior of your designs on screen for parametric analysis and multiple loading situations.

<img alt="" src=images/Generative_Design.png  style="width:512px;">

### Intended work-flow 

1.  Click the **Initiate** button to create the parameters for the parametric analysis.
2.  Using the **Alias** button please match the size and name of the parameters.
3.  Associate the [Spreadsheet](Spreadsheet_Workbench.md) and your model.
4.  Set up analysis model(s) with the [FEM Workbench](FEM_Workbench.md).
5.  Switch back to the **FEMbyGEN Workbench** and with the **Generate** button, create all generations.
6.  Click on the **FEA** button and Start FEA to run simulations.
7.  You can check simulation files by clicking rows of the related generation.
8.  Click on the **Results** button to get results into the master file.
9.  Summation of all load case results will also be under Results in the [tree view](Tree_view.md).
10. If you want to get a recommendation for your design instead of parametric analysis, click on **CreatGeo** to define the boundary conditions of your design, such as loads, supports, protection geometries. After that it will create a boundbox and then optimize it to suggest you the most suitable geometry. You can use the slider to see previous suggestions.
11. Click **Topology** to run the topology simulation for generations or just the file with FEM analysis defined. On the screen you can define your optimization parameter and it will eventually show the results. the bottom slider will help you to see the progress of the topology optimization.

### Features

-   Parametric FEM analysis
-   Supports multiple load cases
-   Summarize all the results in a table
-   Sort results by your output weight
-   Summation of all load cases
-   Geometry suggestion based on your boundary condition
-   Topology optimization

### Features to be supported in the future 

-   Implementation other than BESO topology method

### Limitations

-   Works only with CalculiX Solver

## Installation

### Addon Manager 

FEMbyGEN can easily be installed via the FreeCAD <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) from the **Tools → Addon manager** menu.

FEMbyGEN is under active development and will get new features frequently. Therefore you should update it regularly using also the menu **Tools → Addon manager**.

The FEMbyGEN code is hosted and developed on [GitHub.com](https://github.com/Serince/FEMbyGEN).

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
⏵ [documentation index](../README.md) > [User Documentation](Category_User%20Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > FEMbyGEN Workbench/en
