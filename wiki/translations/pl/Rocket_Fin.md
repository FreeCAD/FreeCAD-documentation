---
- GuiCommand:
   Name:Rocket Fin
   MenuLocation:Rocket → Fin
   Workbenches:[Rocket Workbench](Rocket_Workbench.md)
   Version:0.19
---

# Rocket Fin/pl

## Opis

Płetwy służą do aerodynamicznej kontroli kierunku lotu.

<img alt="" src=images/Nike_Fin_TTW_2.png  style="width:256px;"> 
*Płetwa zwężana z wypustką TTW*

## Użycie

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Rocket_Fin.svg" width=16px> [Fin](Rocket_Fin.md)** button.
    -   Select the **Rocket → <img src="images/Rocket_Fin.svg" width=16px> Fin** option from the menu.
    -   Double click on a Fin object in the [Tree view](Tree_view.md).
2.  Set options and press **OK**.

## Options

### Fin Type 

The general shape of the fin.

-   Trapezoid.

This fin type is used for almost all 4 sided fins. The root remains fixed, but the leading and trailing edges can have variable amounts of sweep. The chord length of the root and tip are set independently.

<img alt="" src=images/Fin_Trapezoid_small.png  style="width:128px;"> 
*Trapezoid fin type*

-   Elliptical.

A generalized rounded shape. Circular fins are a special case where the height is 1/2 of the root chord.

<img alt="" src=images/Fin_Elliptical_small.png  style="width:128px;"> 
*Elliptical fin type*

-   Custom.

Most fins will fit into one of the standard shapes. In cases where they don\'t it\'s possible to create a custom shape using a sketch.

The sketch must be created first. The fin root is drawn along the positive X axis. With the sketch selected in the model tree, selecting the Fin icon will create the custom fin. The fin profile can be changed at this time.

There is no way to associate a custom fin with a sketch within the dialog after it\'s been created, so it is important to create the sketch first. It can be selected from the Properties view. Updating the sketch will update the fin.

<img alt="" src=images/Fin_Sketch_small.png  style="width:128px;"> 
*Sketch used to create a custom fin shape* <img alt="" src=images/Fin_Custom_small.png  style="width:128px;"> 
*The custom fin created from the sketch*

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

-   Leading Edge (LE) Taper. The leading edge is tapered to a point as determined by **Length 1**.

<img alt="" src=images/LE_Taper.png  style="width:128px;"> 
*Leading edge taper cross section*

-   Trailing Edge (TE) Taper. The trailing edge is tapered to a point as determined by **Length 1**.

<img alt="" src=images/TE_Taper.png  style="width:128px;"> 
*Trailing edge taper cross section*

-   Taper. The leading edge is tapered to a point as determined by **Length 1**, and the trailing edge is tapered to a point as determined by **Length 2**.

<img alt="" src=images/CS_Taper.png  style="width:128px;"> 
*Taper cross section*

### Through the Wall (TTW) Tabs 

Through the Wall fins add structural strength by extending though the outer body tube to an inner body tube such as a motor mount. Instead of attaching just to the outside of the outer body tube, it can be attached at multiple points. As such, the height of the tab would be the distance from the outer diameter of the inner body tube to the outer diameter of the outer body tube. Other parameters would vary depending on requirements.

![](images/TTWx4.png ) 
*4 TTW fins attached to a central motor mount inside the outer body tube*

## Properties


{{TitleProperty|Fin}}

-    **Fin Type**: Defines the shape of the fin.

-    **Height**: The fin height.

-    **Profile**: The sketch associated with the custom fin type.

-    **Root Chord**: The distance between the fin leading and trailing edges at the root

-    **Root Cross Section**: The cross section shape of the fin at the root, see [Options](#Options.md)

-    **Root Length 1**: Usage depends on the **Fin Root Cross Section** and will apply to a taper length or similar, see [Options](#Options.md)

-    **Root Length 2**: Usage depends on the **Fin Root Cross Section** and will apply to a taper length or similar when multiple values are required, see [Options](#Options.md)

-    **Root Per Cent**: Expresses the **Fin Root Length 1** and **Fin Root Length 2** properties as a percentage of the **Fin Root Chord**

-    **Root Thickness**: Maximum thickness at the root of the fin

-    **Sweep Angle**: The angle of the front of the fin, with a vertical front being 0 degrees. This may be negative. Setting this value will cause the **Sweep Length** to be adjusted.

-    **Sweep Length**: The distance from the front of the fin root to the front of the fin tip along the x axis. This may be negative. Setting this value will cause the **Sweep Angle** to be adjusted.

-    **Tip Chord**: The distance between the fin leading and trailing edges at the tip

-    **Tip Cross Section**: The cross section shape of the fin at the tip, see [Options](#Options.md)

-    **Tip Length 1**: Usage depends on the **Fin Tip Cross Section** and will apply to a taper length or similar, see [Options](#Options.md)

-    **Tip Length 2**: Usage depends on the **Fin Tip Cross Section** and will apply to a taper length or similar when multiple values are required, see [Options](#Options.md)

-    **Tip Per Cent**: Expresses the **Fin Tip Length 1** and **Fin Tip Length 2** properties as a percentage of the **Fin Tip Chord**

-    **Tip Thickness**: Maximum thickness at the tip of the fin

-    **Ttw**: True when a tab for Through the Wall fins is required, see [Options](#Options.md)

-    **Ttw Height**: Height of the TTW tab

-    **Ttw Length**: Length of the TTW tab

-    **Ttw Offset**: Distance from the front of the fin to the front of the TTW tab

-    **Ttw Thickness**: Thickness of the TTW tab


{{TitleProperty|Rocket Component}}

These parameters are provided for information and have no effect on the design of the component.

-    **Description**: Description of the component

-    **Manufacturer**: Manufacturer when known

-    **Material**: Material when known

-    **Part Number**: Manufacturer part number

## Tutorials and Learning 

[Rocket Workbench Fins](https://youtu.be/8MmEVyGkA0I) Tutorial on YouTube



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Rocket Fin/pl
