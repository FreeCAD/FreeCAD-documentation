---
- GuiCommand:Addon
   Name: BIM IfcQuantities
   Workbenches: <img src="images/IFC.svg" width=16px> [BIM](BIM_Workbench.md)
   Addon: BIM
   MenuLocation: Manage - IFC Quantities
   SeeAlso: [[BIM IfcElements]],[[BIM IfcProperties]]
---

# BIM IfcQuantities/pl

## Description

<img alt="" src=images/BIM_ifcquantities_screenshot.png  style="width:1024px;">

The IFC quantities manager allows you to check the **explicit quantities** attached to objects, to be exported to IFC.

The IFC format allows to include, for any object, explicit quantities, that can be things like \"Width\" or \"Height\" or \"Area\". There is no standard that defines which object type must include which kind of quantity, and there is also no guarantee that such explicit quantities actually reflect the geometry of the object. In other words, these quantities could have wrong values or even lie. A wall could have its geometry as a cube with a length of 10 meters, but have an attached \"Length\" quantity of 8 meters.

The idea behind explicit quantities is to make them available to applications that are unable to read geometry, such as a spreadsheet application. Such application, when reading an IFC file with explicit quantities, could still get an idea of the dimensions of an object and use them for example for quantities calculations.

By default, when exporting an IFC file from FreeCAD, no explicit quantities are exported. With the IFC quantities manager, you are able to mark which quantities should be exported, and check their values. Warning signs will be displayed next to zero values, notifying you of possible problems you might want to fix before exporting.

You can also use the quantities manager to change or fix the actual **Height**, **Width** and **Length** values of objects. But this will affect the object geometry in FreeCAD.



---
⏵ [documentation index](../README.md) > BIM IfcQuantities/pl
