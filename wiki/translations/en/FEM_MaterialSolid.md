---
 GuiCommand:
   Name: FEM MaterialSolid
   MenuLocation: Model , Materials , Material for solid
   Workbenches: FEM_Workbench
   Shortcut: **M** **S**
   SeeAlso: FEM_tutorial
---

# FEM MaterialSolid/en

## Description

Creates a material for solid.

![](images/FEMMaterialSolidProperties.png ) 
*The FEM material task panel*

## Usage

1.  To create a new MaterialSolid object do one of the following:
    -   Press the **<img src="images/FEM_MaterialSolid.svg" width=16px> [Material for solid](FEM_MaterialSolid.md)** button.
    -   Select the **Model → Materials → <img src="images/FEM_MaterialSolid.svg" width=16px> Material for solid‏‎** option from the menu.
2.  To edit an existing MaterialSolid object:
    -   Double-click it in the [Tree view](Tree_view.md).
3.  The FEM material task panel opens.
4.  Select a material. For example, for engineering mechanical analysis, *CalculiX-Steel* is a common option.
5.  Provided you are applying material to the whole object, don\'t select any geometrical entities (leave the reference list empty). Material will be applied to the whole model. Otherwise, assign material to particular model parts manually by selecting some of them for each inserted material, but don\'t leave any part of the model without material assigned.
6.  You can adjust material properties such as density, Young\'s modulus, Poisson\'s ratio, etc., however, most of the common materials are already available in the presets and they don\'t need any tweaking.
7.  If you make modifications, you can save your customized material.
8.  Press the **Close** button to close the task panel.

## Notes

1.  The mechanical material uses the \*MATERIAL card in CalculiX. Details about the mechanical material is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialSolid/en
