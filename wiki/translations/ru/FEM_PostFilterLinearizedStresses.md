---
 GuiCommand:
   Name: FEM PostCreateLinearizedStressesFilter
   Name/ru: FEM PostCreateLinearizedStressesFilter
   Icon: Fem-linearizedstresses.svg
   MenuLocation:  Results , Linearized stresses filter
   Workbenches: FEM_Workbench/ru
   Shortcut: 
   SeeAlso: FEM_tutorial/ru
---

# FEM PostFilterLinearizedStresses/ru


</div>



## Описание

Creates a stress linearization plot.

To learn more about stress linearization plots, you can read [this description](https://www.graspengineering.com/what-is-stress-linearization/).

<img alt="" src=images/FEM_Stress-Linearization-Plot-Example.png  style="width:500px;">

*A stress linearization plot.*



## Применение

1.  Select a previously created [Line clip filter](FEM_PostFilterDataAlongLine.md) with one of the following stress quantities plotted:
    -   Von Mises,

    -   Tresca,

    -   Major principal,

    -   Intermediate principal,

    -   Minor principal,

    -   
        <small>(v0.22)</small> 
        
        : Stress xx component,

    -   
        <small>(v0.22)</small> 
        
        : Stress xy component,

    -   
        <small>(v0.22)</small> 
        
        : Stress xz component,

    -   
        <small>(v0.22)</small> 
        
        : Stress yy component,

    -   
        <small>(v0.22)</small> 
        
        : Stress yz component,

    -   
        <small>(v0.22)</small> 
        
        : Stress zz component.
2.  Invoke the command either by:
    -   Pressing the button **<img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> '''Stress linearization plot'''**.
    -   Using the menu **Results → <img src="images/FEM_PostFilterLinearizedStresses.svg" width=16px> Stress linearization plot**.
3.  An XY plot with linearized stress values (membrane, membrane+bending and total) along the line will be created in a separate window. The stress quantity plotted in the Line clip filter will be used for linearized stresses computation.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterLinearizedStresses/ru
