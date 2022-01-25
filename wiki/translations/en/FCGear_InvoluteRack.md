---
- GuiCommand:
   Name:FCGear InvoluteRack
   MenuLocation:FCGear → Create an Involute rack
   Workbenches:[FCGear](FCGear_Workbench.md)
   Shortcut:None
   Version:v0.16
   SeeAlso:[[FCGear InvoluteGear]]
---

# FCGear InvoluteRack/en

## Description

Gear racks are used to convert a rotary motion into a linear motion or vice versa. The following examples show the different applications:

-   A rack with gear on at a retaining weir.
-   Various rack systems of rack-and-pinion railways.
-   Rack and pinion steering in a vehicle.
-   Rack and pinion winch as mechanical hoist (e.g. car jack).
-   Pneumatic rack and pinion drives used to control valves in pipeline transport.

![](images/Involute-Rack_example.png ) 
*From left to right: Spur gearing, helical gearing, double helical gearing*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  Invoke the command several way:
    -   Press the <img alt="" src=images/FCGear_InvoluteRack.svg  style="width:22px;"> [Create an Involute rack](FCGear_InvoluteRack.md) button in the tool bar.
    -   Using the **Gear Menu → Involute rack**.
3.  Change the gear parameter to the required conditions (see **Properties → Data** below).

## Properties

### Data


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|computed}}

-    **transverse_pitch**: Pitch in the transverse plane -- not changeable, is calculated automatically (see also the information in **Notes**).


{{Properties_Title|gear_parameter}}

-    **add_endings**: If **True**, than the total length of the rack is teeth \* pitch, otherwise the rack starts with a tooth-flank.

-    **beta**: With the helix angle β a helical gear is created (positive value → rotation direction right, negative value → rotation direction left).

-    **clearance**: Default is 0,25 (see also the information in **Notes**).

-    **double_helix**: **True** creates a double helix gear (see also the information in **Notes**)

-    **head**: Default is 0,00. This value is used to change the tooth height.

-    **height**: Value of the gear width.

-    **module**: Module is the ratio of the reference diameter of the gear divided by the number of teeth (see also the information in **Notes**).

-    **properties_from_tool**: If helix angle β is given and **properties_from-tool** is enabled, gear parameters are internally recomputed for the rotated gear.

-    **simplified**: **True** generates a simplified display (without teeth).

-    **teeth**: Number of teeth

-    **thickness**: Height from the tooth root to the lower side of the rod.


{{Properties_Title|involute_parameter}}

-    **pressure_parameter**: Default is 20 (see also the information in **Notes**).

### View

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Notes

-    **transverse_pitch**: The value is the result of multiplication of **module * pi**. This means for the standard involute rack of FCGear: 15 (**teeth**) \* 3,14 (**transverse_pitch**) is 47.12 mm. See also **module** further below.

-    **clearance**: At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **double_helix**: To use the double helical gearing the helix angle β (**beta**) for the helical gearing must first be entered.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth. The result of the multiplication is displayed in **transverse_pitch**

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Useful formulas 

For more information see <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:22px;"> [Involute gear](FCGear_InvoluteGear.md).

## Scripting

Use the power of python to automate your gear modeling: 
```python
import FreeCAD as App
import freecad.gears.commands
gear = freecad.gears.commands.CreateInvoluteRack.create()
gear.teeth = 20
gear.beta = 20
gear.height = 10
gear.double_helix = True
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InvoluteRack/en
