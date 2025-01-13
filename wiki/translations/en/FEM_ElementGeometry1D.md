---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ElementGeometry1D
   MenuLocation: Model , Element Geometry , Beam cross section
   Workbenches: FEM_Workbench
   Shortcut: **C** **B**
   SeeAlso: FEM_tutorial
}}
{{GuiCommandFemInfo
   Solvers: CalculiX, Mystran, Z88
}}
---

# FEM ElementGeometry1D/en

## Description

**ElementGeometry1D** is used to define cross sections for beam elements. Currently, the following types of cross sections are available: rectangular, circular and pipe.


<small>(v1.1)</small> 

: Box and elliptical cross sections are also available.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [Beam cross section](FEM_ElementGeometry1D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Beam cross section** option from the menu.
2.  Choose the type of cross section and specify the necessary dimensions:
    -   Rectangular: width and height,

    -   Circular: diameter,

    -   Pipe: outer diameter and thickness,

    -   
        <small>(v1.1)</small> 
        
        : Elliptical: axis 1 length and axis 2 length,

    -   
        <small>(v1.1)</small> 
        
        : Box: height, width, thickness T1 - T4.
3.  Optionally, press the **Add** button in the task panel and then click on the edge you want to have a prescribed cross section. If the edge selection is free, all the remaining edges (whose cross section is not defined by other [FEM ElementGeometry1D](FEM_ElementGeometry1D.md) objects) will be automatically assigned.

## Properties

-    **Section Type**: specifies the type of the beam section (*Rectangular*, *Circular*, *Pipe*, <small>(v1.1)</small> : *Elliptical* and *Box*)

-    <small>(v1.1)</small> : **Box Height**: height of box section, used if **Section Type** is *Box*

-    <small>(v1.1)</small> : **Box T1**: thickness T1 of box section, used if **Section Type** is *Box*

-    <small>(v1.1)</small> : **Box T2**: thickness T2 of box section, used if **Section Type** is *Box*

-    <small>(v1.1)</small> : **Box T3**: thickness T3 of box section, used if **Section Type** is *Box*

-    <small>(v1.1)</small> : **Box T4**: thickness T4 of box section, used if **Section Type** is *Box*

-    <small>(v1.1)</small> : **Box Width**: width of box section, used if **Section Type** is *Box*

-    **Circ Diameter**: diameter of circular section, used if **Section Type** is *Circular*

-    <small>(v1.1)</small> : **Axis 1 Length**: lenth of axis 1 of elliptical section, used if **Section Type** is *Elliptical*

-    <small>(v1.1)</small> : **Axis 2 Length**: lenth of axis 2 of elliptical section, used if **Section Type** is *Elliptical*

-    **Pipe Diameter**: outer diameter of pipe section, used if **Section Type** is *Pipe*

-    **Pipe Thickness**: thickness of pipe section, used if **Section Type** is *Pipe*

-    **Rect Height**: height of rectangular section, used if **Section Type** is *Rectangular*

-    **Rect Width**: width of rectangular section, used if **Section Type** is *Rectangular*

## Limitations

-    {{VersionMinus|1.0}}: Other types of cross sections available in CalculiX (elliptical, box and general) are not currently supported. One can edit the input file to use them.

-    <small>(v1.1)</small> : General beam section is not currently supported. One can edit the input file to use it.

## Notes

-   For viewing results from CalculiX solver on the mesh expanded to the prescribed cross section, property `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) needs to be set to `True`.
-   Some sections require specific element types:
    -   circular section - 2nd order elements

    -   pipe section - 2nd order elements with reduced integration (<small>(v1.0)</small> : reduced integration is enabled by default for beam elements and can be switched using the *Beam Reduced Integration* property of the [CalculiX solver](FEM_SolverCalculixCxxtools.md))

    -   
        <small>(v1.1)</small> 
        
        : elliptical section - 2nd order elements

    -   
        <small>(v1.1)</small> 
        
        : box section - 2nd order elements with reduced integration (as explained above)
-   This feature uses the [\*BEAM SECTION card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry1D/en
