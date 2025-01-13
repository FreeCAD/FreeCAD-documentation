---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ConstraintHeatflux
   MenuLocation: Model , Thermal boundary conditions and loads , Heat flux load
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
}}
{{GuiCommandFemInfo
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintHeatflux/en

## Description

By default, defines a convective heat flux load on a surface at a temperature $T$ with a film coefficient $h$ and with the environment (sink/ambient) temperature $T_{0}$. The convective heat flux $q$ will satisfy: $q=h(T-T_{0})$. Optionally, can also define a regular surface heat flux load.


<small>(v1.0)</small> 

: Can be also used to define a radiation heat flux on a surface. It satisfies: $q=\epsilon \sigma(T^{4}-T_{0}^{4})$ where $\epsilon$ is the surface emissivity and $\sigma$ is the Stefan-Boltzmann constant.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Heat flux load](FEM_ConstraintHeatflux.md)** button.
    -   Select the **Model → Thermal boundary conditions and loads → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Heat flux load** option from the menu.
2.  Click the **Add** button. In the [3D view](3D_view.md) select the face(s) on which the heat flux load should be applied. Optionally, click the **Remove** button to remove the selected faces from the selection list.
3.  Choose the heat flux type and specify its parameters:
    -   *Surface Convection* (default) - convective heat flux, enter the desired *Film coefficient* and *Ambient temperature*

    -   
        <small>(v1.0)</small> 
        
        : *Surface Radiation* - radiation heat flux, enter the surface *Emissivity* and *Ambient temperature*

    -   *Surface heat flux* - general heat flux, enter the *Surface heat flux* in Watts per surface area (W/m\^2)

## Notes

-   The heat flux load uses the following CalculiX cards depending on the selected mode:
    -   [\*FILM](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html) for *Surface Convection*

    -   
        <small>(v1.0)</small> 
        
        : [\*RADIATE](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node234.html) for *Surface Radiation*

    -   [\*DFLUX](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html) for *Surface heat flux*





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/en
