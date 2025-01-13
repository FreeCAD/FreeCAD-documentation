---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintBodyHeatSource
   MenuLocation: Model , Thermal boundary conditions and loads , Body heat source
   Workbenches: FEM_Workbench
   Version: 0.19
   SeeAlso: FEM_tutorial
}}
{{GuiCommandFemInfo
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintBodyHeatSource/pt-br

## Description

Defines an internally generated body heat given in W/kg.


<small>(v1.0)</small> 

: Can also define the heat source in W.

## Usage

1.  Press the **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> '''Body heat source'''** button or select **Model → Thermal boundary conditions and loads → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Body heat source** from the menu.

2.  
    <small>(v0.21)</small> : Press the **Add** button. For a 3D analysis, select a \'solid\' (body) from your model, for a 2D analysis select a face.

3.  Set the value:
    -   
        {{VersionMinus|0.20}}
        
        : Since the tool has no task dialog, use the [property editor](Property_editor.md) and set the property **Heat Source**.

    -   
        <small>(v0.21)</small> 
        
        : Enter the body heat in W/kg.

    -   
        <small>(v1.0)</small> 
        
        : Select the mode:

        -   *Dissipation Rate* - enter the dissipation rate in W/kg .
        -   *Total Power* - enter the total power in W.



## Limitações

-    {{VersionMinus|0.20}}: The body heat source is applied to the whole model, meaning all bodies of the setup. It is not possible to select an individual body.

-    {{VersionMinus|0.21}}: This feature only works with the Elmer solver.

## Notes

-   For more information see [this forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) and following posts. [This thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=28926) may also be useful.

-   Elmer examples can also be found in [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).

-    <small>(v1.0)</small> : This feature uses the [\*DFLUX card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html).

-    <small>(v1.0)</small> : Since CalculiX expects body heat flux input in W/mm\^3 while for Elmer it\'s W/kg, the conversion of the specified value (in W or W/kg) is done internally for each solver, using the volume of the selected solid and the density of the material assigned to it, if needed.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/pt-br
