---
- GuiCommand:
   Name:PartDesign InvoluteGear
   MenuLocation:Part Design → Involute gear...
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   SeeAlso:[FCGear Workbench](FCGear_Workbench.md)
---

# PartDesign InvoluteGear/en

## Description

This tool allows you to create a 2D profile of an involute gear. This 2D profile is fully parametric, and can be padded with the [PartDesign Pad](PartDesign_Pad.md) feature.
For more detailed information see Wikipedia\'s entries for: [Gear](https://en.wikipedia.org/wiki/Gear) and [Involute Gear](https://en.wikipedia.org/wiki/Involute_gear)

![](images/PartDesign_Involute_Gear_01.png ) 

## Usage

1.  Go to the menu **Part Design → <img src=images/PartDesign_InternalExternalGear.svg style="width:24px"> Involute gear...**.
2.  Set the Involute parameters.
3.  Click **OK**
4.  The involute gear is created outside of the active body. Drag and drop it into a body for the application of further features like padding.

## Parameters

-   Number of teeth: Sets the number of teeth.

-   Modules: Pitch diameter divided by the number of teeth.

-   Pressure angle: Acute angle between the line of action and a normal to the line connecting the gear centers. Default is 20 degrees. ([More info](http://en.wikipedia.org/wiki/Involute_gear))

-   High precision: True or false

-   External gear: True or false

## Related

-   [FCGear Workbench](FCGear_Workbench.md)





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/en
