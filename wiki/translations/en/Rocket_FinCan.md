---
- GuiCommand:
   Name:Rocket FinCan
   MenuLocation:Rocket → Fin Can
   Workbenches:[Rocket Workbench](Rocket_Workbench.md)
   Version:0.19
---

# Rocket FinCan/en

## Description

Fins are used to aerodynamically control the direction of flight. A fin can is a complete assembly including fins and body tube, often fitted over the outside of the main rocket body tube. Optionally, a fin can may include a launch lug.

<img alt="" src=images/FinCan.png  style="width:256px;"> 
*A fin can with launch lug*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Rocket_FinCan.svg" width=16px> [Fin Can](Rocket_FinCan.md)** button.
    -   Select the **Rocket → <img src="images/Rocket_FinCan.svg" width=16px> Fin Can** option from the menu.
    -   Double click on a Fin Can object in the [Tree view](Tree_view.md).
2.  Set options and press **OK**.

## Options

### Fin Options 

Fin options for the fin can are the same as for individual fins. See <img alt="" src=images/Rocket_Fin.svg  style="width:16px;"> [Fin](Rocket_Fin.md) for more details

However due to the one piece nature of fin cans, they do not have the option to include Through The Wall (TTW) tabs.

### Fin Can Options 

### Launch Lug Options 

## Properties


{{TitleProperty|Fin Can}}

-    **Fin Type**: Defines the shape of the fins.

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


{{TitleProperty|Rocket Component}}

These parameters are provided for information and have no effect on the design of the component.

-    **Description**: Description of the component

-    **Manufacturer**: Manufacturer when known

-    **Material**: Material when known

-    **Part Number**: Manufacturer part number

## Tutorials and Learning 

[Rocket Workbench Fins](https://youtu.be/8MmEVyGkA0I) Tutorial on YouTube



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Rocket FinCan/en
