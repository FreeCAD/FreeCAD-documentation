---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintSectionPrint
   MenuLocation: Model , Geometrical analysis features , Section print feature
   Workbenches: FEM_Workbench
   Version: 0.19
   SeeAlso: 
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ConstraintSectionPrint/it

## Description

Prints the predefined facial output variables (forces and moments) to the data file.


<small>(v1.0)</small> 

: Can also print heat flux and drag stress (the latter requires the support for 3D fluid analyses with CalculiX which has not yet been implemented).

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintSectionPrint.svg" width=16px> [Section print feature](FEM_ConstraintSectionPrint.md)** button.
    -   Select the **Model → Geometrical analysis features → <img src="images/FEM_ConstraintSectionPrint.svg" width=16px> Section print feature** option from the menu.

2.  Press the **Add** button and select a single face for which the output will be printed.

3.  
    <small>(v1.0)</small> : From the *Variable* list, select the variable that you want to print: *Section Force*, *Heat Flux* or *Drag Stress*.

## Notes

-   The feature uses the \*SECTION PRINT card in CalculiX.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintSectionPrint/it
