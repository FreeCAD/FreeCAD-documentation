---
- GuiCommand:
   Name:Rocket CenteringRing
   MenuLocation:Rocket - Centering Ring
   Workbenches:[Rocket Workbench](Rocket_Workbench.md)
   Version:0.19
---

# Rocket CenteringRing

## Description

A Centering Ring is a solid object used to hold one or more body tubes inside another body tube.
 ![](images/CR_with_tubes.png )  
*Conical*

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Rocket_CenteringRing.svg" width=16px> [Centering Ring](Rocket_CenteringRing.md)** button.
    -   Select the **Rocket → <img src="images/Rocket_CenteringRing.svg" width=16px> Centering Ring** option from the menu.
    -   Double click on a Centering Ring object in the [Tree view](Tree_view.md).
2.  Set options and press **OK**.

## Options

### Notch

Centering rings, especially those used for low power rocketry, often need a notch to accommodate an engine hook. The **Centering Ring** tool can generate those for you.

 ![](images/Notched_CR.png )  
*Centering ring with an engine hook notch*

## Properties


{{TitleProperty|Bulkhead}}

These properties are inherited from the **Bulkhead**, see [Bulkhead](Rocket_Bulkhead.md) for more information.

-    **Diameter**: The outer diameter of the bulkhead

-    **Hole Center**: The distance from the center of the hole to the center of the bulkhead

-    **Hole Count**: The number of holes applied in a radial pattern around the center of the bulkhead

-    **Hole Diameter**: The diameter of the hole

-    **Hole Offset**: Offset from 0 degrees of the first hole

-    **Holes**: True when the the bulkhead has one or more holes, see [Bulkhead Options](Rocket_Bulkhead#Options.md)

-    **Step**: True when the bulkhead includes a step, see [Bulkhead Options](Rocket_Bulkhead#Options.md)

-    **Step Diameter**: The outer diameter of the step

-    **Step Thickness**: The thickness, not including the bulkhead thickness, of the step

-    **Thickness**: The thickness, not including any step, of the bulkhead


{{TitleProperty|Centering Ring}}

-    **Center Diameter**: The diameter of the inner hole

-    **Notch Height**: The notch height

-    **Notch Width**: The notch width

-    **Notched**: True when the center hole includes a notch, see [Options](#Options.md)


{{TitleProperty|Rocket Component}}

These parameters are provided for information and have no effect on the design of the component.

-    **Description**: Description of the component

-    **Manufacturer**: Manufacturer when known

-    **Material**: Material when known

-    **Part Number**: Manufacturer part number

## Scripting

See also: [:Category:API](:Category_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

TBD

## Tutorials and Learning 

[Rocket Workbench Body Tubes, Bulkheads, and Centering Rings](https://youtu.be/xi7acpw3eDA) Tutorial on YouTube



---
![](images/Button_right.svg) [documentation index](../README.md) > [API]] and ](Category_API]] and .md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Rocket CenteringRing
