---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintCentrif
   MenuLocation: Model , Mechanical boundary conditions and loads , Centrifugal load
   Workbenches: FEM_Workbench
   Shortcut: 
   Version: 0.20
   SeeAlso: 
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ConstraintCentrif/ru



## Описание

Defines a centrifugal body load.



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintCentrif.svg" width=16px> [Centrifugal load](FEM_ConstraintCentrif.md)** button.
    -   Select the **Model → Mechanical boundary conditions and loads → <img src="images/FEM_ConstraintCentrif.svg" width=16px> Centrifugal load** option from the menu.
2.  Specify the rotation frequency in Hz.
3.  Click on **Add** in **Geometry reference selector for a Solid** window and select a solid to which the load will be applied in the [3D view](3D_view.md).
4.  Click on **Add** in **Geometry reference selector for a Edge** window and select an edge about which the rotation will occur in the [3D view](3D_view.md).

## Notes

-   This feature uses the [\*DLOAD card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintCentrif/ru
