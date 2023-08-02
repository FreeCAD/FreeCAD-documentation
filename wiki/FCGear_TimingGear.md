---
- GuiCommand:
   Name: FCGear TimingGear
   MenuLocation: Gear -> Timing Gear
   Workbenches: FCGear_Workbench
   Shortcut: None
   Version: v0.16
   SeeAlso: 
---

# FCGear TimingGear

## Description

The purpose of timing gears is to allow the camshaft and crankshaft to turn the timing chain. The crankshaft turns to move pistons up and down inside the cylinders. The camshaft turns to allow intake and exhaust valves on the cylinders to open and close. These components are important for proper engine timing.

Timing gears are connected to a timing belt or timing chain.

 ![](images/Timing-Gear_example.png )  
*Above: Timing gear*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_TimingGear.svg style="width:16px"> [Timing Gear](FCGear_TimingGear.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_TimingGear.svg style="width:16px"> Timing Gear** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

An FCGear TimingGear object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|base}}

-    **height|Length**: Default is {{Value|5 mm}}. Value of the gear width.

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.

-    **type|Enumeration**: Default is {{Value|gt2}}. Type of timing gear -- profile pitch for timing belts (see [Notes](#Notes.md)).


{{Properties_Title|computed}}

-    **h|Length**: (read-only) Radial height of teeth.

-    **offset|Length**: (read-only) X-Offset of second arc mid-point.

-    **pitch|Length**: (read-only) Pitch of gear.

-    **r0|Length**: (read-only) Radius of first arc.

-    **r1|Length**: (read-only) Radius of second arc.

-    **rs|Length**: (read-only) Radius of third arc.

-    **u|Length**: (read-only) Radial difference between pitch ... diameter and head of gear.


{{Properties_Title|version}}

-    **version|String**:

## Notes

-    **type**: The pitch of the timing belts (distance from tooth centre to tooth centre of consecutive teeth) is specified in types. GT2 has a pitch of 2 mm, GT3 of 3 mm, GT5 of 5 mm etc..

## Useful formulas 

-    **addendum diameter**= **pitch diameter** + 2 \* **module**

-    **belt length**= 2 \* **axle base** + **belt tooth pitch** : 2 \* **(teeth 1 + 2)** + **belt tooth pitch²** : 4 \* pi² \* **axle base** \* **(teeth 1 - 2)²**

-    **axle base**= **belt length** : 4 - **belt tooth pitch** : 8 \* **(teeth 1+2)** + ¼ \* sqrt \[**belt length** - ½ \* **belt tooth pitch** \* **(teeth 1+2)²** - 2 \* **belt tooth pitch²** \* **(teeth 1+2)²** : pi²\]



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear TimingGear
