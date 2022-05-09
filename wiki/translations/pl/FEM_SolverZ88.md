---
- GuiCommand   *
   Name   *FEM SolverZ88
   MenuLocation   *Solve → Solver Z88
   Workbenches   *[FEM](FEM_Workbench.md)
   Shortcut   ***S** **Z**
   SeeAlso   *[FEM tutorial](FEM_tutorial.md)
---

# FEM SolverZ88/pl

## Description

[SolverZ88](FEM_SolverZ88.md) enables usage of the [Z88](https   *//en.wikipedia.org/wiki/Z88_FEM_software) solver. It may be used for   *

1.  Setting analysis parameters
2.  Selecting working directory
3.  Running the Z88 solver

## Installation

To use the Z88 solver, the OpenSource version of Z88 (Z88OS) needs to be installed   *

1.  Download the ZIP file from the [Z88OS website](https   *//en.z88.de/download-z88os).
2.  Extract the ZIP to a folder of your choice.
3.  In the [FEM preferences](FEM_Preferences.md) go to the Z88 tab and there set the path to the **z88r** binary. If you are on Windows this would be the path to the file **z88r.exe** that is in the subfolder **~\bin\win64** of the folder where your extracted the ZIP.

## Usage

1.  After the creation of an <img alt="" src=images/FEM_Analysis.svg  style="width   *16px;"> [Analysis container](FEM_Analysis.md) use one of the following alternatives   *
    -   Select **Solve → <img src="images/FEM_SolverZ88.svg" width=x16px> Solver Z88** from the menu.
    -   Press the **S** then **Z** shortcut keys.
2.  Double click the <img alt="" src=images/FEM_SolverZ88.svg  style="width   *" height="16px;"> SolverZ88 object.
3.  Select the **Analysis type**.
4.  Click the **Write** button.
5.  Click the **Run** button.

As a result you get an object called *Z88\_xxx\_results* (depending on the run simulation) in the [Tree view](Tree_view.md). This is the same kind of result object one gets when running the [CalculiX solver](FEM_SolverCalculixCxxtools.md). Starting from this, you can visualize the results using [Post Pipeline](FEM_PostPipelineFromResult.md) and [Clip Filters](FEM_Workbench#Menu__Results.md).

## Preferences

See the [Z88 preferences](FEM_Preferences#Z88.md) for the possible solver settings like the used solver method.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverZ88/pl
