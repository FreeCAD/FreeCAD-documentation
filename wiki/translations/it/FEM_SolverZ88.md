# FEM SolverZ88/it
---
- GuiCommand:   Name:FEM_SolverZ88   Name/it:Risolutore Z88   MenuLocation: Solve - Risolutore Z88   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Da fare


</div>

## Installation

To use the Z88 solver, the OpenSource version of Z88 (Z88OS) needs to be installed:

1.  Download the ZIP file from the [Z88OS website](https://en.z88.de/download-z88os).
2.  Extract the ZIP to a folder of your choice.
3.  In the [FEM preferences](FEM_Preferences.md) go to the Z88 tab and there set the path to the **z88r** binary. If you are on Windows this would be the path to the file **z88r.exe** that is in the subfolder **~\bin\win64** of the folder where your extracted the ZIP.



## Utilizzo


<div class="mw-translate-fuzzy">



</div>

As a result you get an object called *Z88_xxx_results* (depending on the run simulation) in the [Tree view](Tree_view.md). This is the same kind of result object one gets when running the [CalculiX solver](FEM_SolverCalculixCxxtools.md). Starting from this, you can visualize the results using [Post Pipeline](FEM_PostPipelineFromResult.md) and [Clip Filters](FEM_Workbench#Menu__Results.md).

## Preferences

See the [Z88 preferences](FEM_Preferences#Z88.md) for the possible solver settings like the used solver method.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverZ88/it
