---
- GuiCommand:
   Name: FCGear InvoluteRack
   MenuLocation: Gear - Involute Rack
   Workbenches: [FCGear](FCGear_Workbench.md)
   Shortcut: None
   Version: v0.16
   SeeAlso: [FCGear InvoluteGear](FCGear_InvoluteGear.md)
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

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_InvoluteRack.svg style="width:16px"> [Involute Rack](FCGear_InvoluteRack.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_InvoluteRack.svg style="width:16px"> Involute Rack** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

An FCGear InvoluteRack object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|base}}

-    **add_endings|Bool**: If {{True}} (default), then the total length of the rack is teeth \* pitch. If {{False}}, then the rack starts with a tooth-flank.

-    **height|Length**: Default is {{Value|5 mm}}. Value of the gear width.

-    **module|Length**: Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.

-    **thickness|Length**: Default is {{Value|5}}. Height from the tooth root to the lower side of the rod.


{{Properties_Title|computed}}

-    **transverse_pitch|Length**: (read-only) Pitch in the transverse plane (see [Notes](#Notes.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**: Default is {{Value|0 mm}}.

-    **root_fillet|Float**: Default is {{Value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: Default is {{Value|0 °}}. With the helix angle β a helical gear is created -- positive value → rotation direction right, negative value → rotation direction left.

-    **double_helix|Bool**: Default is {{False}}, {{True}} creates a double helix gear (see [Notes](#Notes.md)).

-    **properties_from_tool|Bool**: Default is {{False}}. If {{True}} and **beta** is not zero, gear parameters are recomputed internally for the rotated gear.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Default is {{Value|20 °}} (see [Notes](#Notes.md)).


{{Properties_Title|precision}}

-    **simplified|Bool**: Default is {{False}}, {{True}} generates a simplified display (without teeth).


{{Properties_Title|tolerance}}

-    **clearance|Float**: Default is {{Value|0.25}} (see [Notes](#Notes.md)).

-    **head|Float**: Default is {{Value|0}}. This value is used to change the tooth height.


{{Properties_Title|version}}

-    **version|String**:

## Notes

-    **transverse_pitch**: The value is the result of multiplication of **module * pi**. This means for the standard involute rack of FCGear: 15 (**teeth**) \* 3.14 (**transverse_pitch**) is 47.12 mm. See also **module** further below.

-    **clearance**: At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **double_helix**: To use the double helical gearing the helix angle β (**beta**) for the helical gearing must first be entered.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth. The result of the multiplication is displayed in **transverse_pitch**

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Useful formulas 

See [FCGear InvoluteGear](FCGear_InvoluteGear#Useful_formulas.md).

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
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InvoluteRack/en
