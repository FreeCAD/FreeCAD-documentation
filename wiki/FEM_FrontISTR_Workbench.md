# FEM FrontISTR Workbench
 

<img alt="FEM FrontISTR Workbench icon" src=images/FrontISTR.svg  style="width:128px;">

 

## Introduction

The <img alt="" src=images/FrontISTR.svg  style="width:24px;"> FEM FrontISTR Workbench is a FreeCAD addon that enables FrontISTR, an open-source large-scale parallel FEM program for nonlinear structural analysis.

 <img alt="" src=images/FEM_FrontISTR_bikeframe_screenshot.png  style="width:512px;"> 

### Intended work-flow 

1.  Set up an analysis model by FEM module (in the same way as calculiX).
2.  Switch to the workbench **FrontISTR** and create a FrontISTR solver object by clicking on the toolbar button <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;">.
3.  Double-click on the solver object in the document tree and set working directory.
4.  Click on the button **Write input file**
5.  Click on the button **Run FrontISTR**
6.  Check FISTR\_Results for post processing.

### Features

-   static analysis, element check
-   geometrical linear\|nonlinear analysis
-   elements: 1st/2nd order tetrahedron
-   loads: mechanical concentrated and distributed loads, gravity
-   boundary: points fixed or displacement
-   step control: auto time increment and cutback
-   linear equation solver
    -   iterative
        -   preconditioner: AMG, SSOR, Diagonal, ILU(k)(k=0,1,2)
        -   method: CG, BiCGSTAB, GMRES, GPBiCG
    -   direct: MUMPS
-   output file format: AVS, VTK(paraview required)

### Features to be supported in the future 

-   analysis: thermal transfer, dynamic, eigen, frequency
-   materials(mechanical): elastoplastic, hyper elastic, creep, visco elastic
-   contact
-   MPC(TIE)
-   elements: prism, hexa, beam, shell, truss etc.

### Limitations

-   FISTR\_Results only contains results for surfaces. If you need the interior results, change Output File Format to VTK and visualize the results with paraview.
-   The FEM FrontISTR workbench does not yet support thermal analyses. FISTR itself can perform thermal analyses and support for this is planned in the near future.
-   Mechanical analyses for different material in a model is not yet possible.

### Benchmark results 

See <https://github.com/FrontISTR/FEM_FrontISTR/tree/master/sample/benchmarks>.

## Installation

### Addon Manager 

FEM\_FrontISTR can easily be installed via the FreeCAD <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) from the **Tools → Addon manager** menu. FEM\_FrontISTR is under active development and will get new features frequently. Therefore you should update it regularly using also the menu **Tools → Addon manager**. The FEM\_FrontISTR code is hosted and developed [on GitHub](https://github.com/FrontISTR/FEM_FrontISTR).

### Manual

See [How to install additional workbenches](How_to_install_additional_workbenches.md)

### Prerequisites

-   FreeCAD 0.19 or newer
-   [Paraview](https://www.paraview.org/) (optional)

### FrontISTR Solver Installation 

FrontISTR binaries will be automatically downloaded and installed on the first run. If the download does not proceed, please follow the steps below to install the solver.

#### Windows

1.  Download [FrontISTR-latest.zip](https://www.frontistr.com/download/link.php?https://frontistr-commons.gitlab.io/FrontISTR/release/x86_64-w64-mingw32-msmpi/FrontISTR-latest.zip)
2.  Create directory FEM\_FrontISTR/bin
3.  Extract FrontISTR-latest.zip and put all files in FEM\_FrontISTR/bin directory.

#### Linux

Under preparation.

#### Mac

Under preparation.

## Tools

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> **Solver FrontISTR Standard**: Creates a new FrontISTR solver for this analysis.

## References

-   Author: kinagaki rigarashi
-   Source code: [Github.com](https://github.com/FrontISTR/FEM_FrontISTR)
-   FreeCAD Forum: [58019](https://forum.freecadweb.org/viewtopic.php?t=58019)
-   Tutorials: <https://frontistr-commons.gitlab.io/FEM_FrontISTR/en/>
-   FrontISTR solver documentation: <https://manual.frontistr.com/en/>
-   Report bugs: Please report bugs at [Github.com](https://github.com/FrontISTR/FEM_FrontISTR)



[Category:Sandbox](Category:Sandbox.md) [Category:User Documentation](Category:User_Documentation.md) [Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md)
