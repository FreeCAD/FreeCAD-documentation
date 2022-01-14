---
- GuiCommand:
   Name:Rocket Fin
   MenuLocation:Rocket → Fin
   Workbenches:[Rocket Workbench](Rocket_Workbench.md)
   Version:0.19
---

# Rocket Fin/en

## Description

Fins are used to aerodynamically control the direction of flight.

<img alt="" src=images/Nike_Fin_TTW_2.png  style="width:256px;"> 
*A Tapered fin with TTW tab*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Rocket_Fin.svg" width=16px> [Fin](Rocket_Fin.md)** button.
    -   Select the **Rocket → <img src="images/Rocket_Fin.svg" width=16px> Fin** option from the menu.
    -   Double click on a Fin object in the model view.
2.  Set options and press **OK**.

## Options

### Fin Type 

At the moment, only *trapezoid* shape fins are supported. This will change as the workbench continues to be developed.

### Cross Section 

The cross sectional shape of a fin can greatly affect its performance at different speeds, as well as the looks of the rocket. A variety of fin cross sections have been implemented. Fins are created by lofting the root cross section to the tip cross section, so not all combinations of **Root Cross Section** and **Tip Cross Section** will produce useful fins.

-   Square. Both the leading and trailing edges are squared.

<img alt="" src=images/CS_Square.png  style="width:128px;"> 
*Square Cross Section*

-   Round. The leading and trailing edges are rounded.

<img alt="" src=images/CS_Round.png  style="width:128px;"> 
*Round cross section*

-   Airfoil. Uses the NACA symmetrical airfoil shape [NACA airfoil](https://en.wikipedia.org/wiki/NACA_airfoil) with maximum thickness at 30% of the chord.

<img alt="" src=images/CS_Airfoil.png  style="width:128px;"> 
*Airfoil cross section*

-   Wedge. The trailing edge of the fin is square, converging to a point at the leading edge.

<img alt="" src=images/CS_Wedge.png  style="width:128px;"> 
*Wedge cross section*

-   Diamond. The diamond shape starts from a point at the leading edge, straight out to the maximum thickness at a point determined by **Length 1**, and back to a point at the trailing edge.

<img alt="" src=images/CS_Diamond.png  style="width:128px;"> 
*Diamond cross section*

-   Leading Edge (LE) Taper. The leading edge is tapered to a point as determined by **Length 1**

<img alt="" src=images/LE_Taper.png  style="width:128px;"> 
*Leading edge taper cross section*

-   Trailing Edge (TE) Taper. The trailing edge is tapered to a point as determined by **Length 1**

<img alt="" src=images/TE_Taper.png  style="width:128px;"> 
*Trailing edge taper cross section*

-   Taper. The leading edge is tapered to a point as determined by **Length 1**, and the trailing edge is tapered to a point as determined by **Length 2**

<img alt="" src=images/CS_Taper.png  style="width:128px;"> 
*Taper cross section*

### Through the Wall (TTW) Tabs 

Through the Wall fins add structural strength by extending though the outer body tube to an inner body tube such as a motor mount. Instead of attaching just to the outside of the outer body tube, it can be attached at multiple points. As such, tthe height of the tab would be the distance from the outer diameter of the inner body tube to the outer diameter of the outer body tube. Other parameters would vary depending on requirements.
![](images/TTWx4.png ) 
*4 TTW fins attached to a central motor mount inside the outer body tube*

## Properties


{{TitleProperty|Rocket Component}}

These parameters are provided for information and have no effect on the design of the component.

-    **Manufacturer**: Manufacturer when known

-    **Part Number**: Manufacturer part number

-    **Description**: Description of the component

-    **Material**: Material when known


{{TitleProperty|Nose Cone}}

-    **Fin Type**: Defines the shape of the fin. At the moment, only Trapezoidal fins are supported.

-    **Height**: The fin height.

-    **Sweep Length**: The distance from the front of the fin root to the front of the fin tip along the x axis. This may be negative. Setting this value will cause the **Sweep Angle** to be adjusted.

-    **Sweep Angle**: The angle of the front of the fin, with a vertical front being 0 degrees. This may be negative. Setting this value will cause the **Sweep Length** to be adjusted.

-    **Fin Root Cross Section**: The cross section shape of the fin at the root, see [Options](#Options.md)

-    **Fin Root Chord**: The distance between the fin leading and trailing edges at the root

-    **Fin Root Thickness**: Maximum thickness at the root of the fin

-    **Fin Root Use Percentage**: Expresses the **Fin Root Length 1** and **Fin Root Length 2** properties as a percentage of the **Fin Root Chord**

-    **Fin Root Length 1**: Usage depends on the **Fin Root Cross Section** and will apply to a taper length or similar, see [Options](#Options.md)

-    **Fin Root Length 2**: Usage depends on the **Fin Root Cross Section** and will apply to a taper length or similar when multiple values are required, see [Options](#Options.md)

-    **Fin Tip Cross Section**: The cross section shape of the fin at the tip, see [Options](#Options.md)

-    **Fin Tip Chord**: The distance between the fin leading and trailing edges at the tip

-    **Fin Tip Thickness**: Maximum thickness at the tip of the fin

-    **Fin Tip Use Percentage**: Expresses the **Fin Tip Length 1** and **Fin Tip Length 2** properties as a percentage of the **Fin Tip Chord**

-    **Fin Tip Length 1**: Usage depends on the **Fin Tip Cross Section** and will apply to a taper length or similar, see [Options](#Options.md)

-    **Fin Tip Length 2**: Usage depends on the **Fin Tip Cross Section** and will apply to a taper length or similar when multiple values are required, see [Options](#Options.md)

-    **TTW Tab**: True when a tab for Through the Wall fins is required, see [Options](#Options.md)

-    **TTW Offset**: Distance from the front of the fin to the front of the TTW tab

-    **TTW Length**: Length of the TTW tab

-    **TTW Height**: Height of the TTW tab

-    **TTW Thickness**: Thickness of the TTW tab

## Scripting

See also: [:<img src="images/Property.png" style="width:16px"> API](:Category_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

TBD

## Tutorials and Learning 

[Rocket Workbench Fins](https://youtu.be/8MmEVyGkA0I) Tutorial on YouTube







[<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md) [<img src="images/Property.png" style="width:16px"> External Workbenches](Category_External_Workbenches.md)

---
[documentation index](../README.md) > [API]] and ](Category_API]] and .md) > Rocket Fin/en
