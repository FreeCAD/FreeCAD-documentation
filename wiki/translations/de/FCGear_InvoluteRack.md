---
- GuiCommand   */de
   Name   *FCGear InvoluteRack
   Name/de   *FCGear InvoluteRack
   MenuLocation   *Gear → Involute Rack
   Workbenches   *[FCGear](FCGear_Workbench/de.md)
   Shortcut   *Kein
   Version   *v0.16
   SeeAlso   *[FCGear Evolventenzahnrad](FCGear_InvoluteGear/de.md)
---

# FCGear InvoluteRack/de

## Beschreibung

Zahnstangen werden verwendet, um eine drehende Bewegung in eine geradlinige Bewegung zu wandeln und umgekehrt. Beispiele für unterschiedliche Anwendungen   *

-   Eine Zahnstange mit Zahnrad (Triebrad) an einem Wehr.
-   Verschiedene Systeme von Zahnradbahnen.
-   Zahnstangenlenkung im Fahrzeug.
-   Zahnstangenwinde als Hebevorrichtung (z.B. Wagenheber).
-   Pneumatische Zahnstangenantriebe zur Steuerung der Ventile von Rohrleitungsanlagen.

![](images/Involute-Rack_example.png )

   *   
    
*Von links nach rechts   * Zahnstangen mit Geradverzahnung, Schrägverzahnung, Pfeilverzahnung
    *
    

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width   *16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen   *
    -   Die Schaltfläche **[<img src=images/FCGear_InvoluteRack.svg style="width   *16px"> [Involute Rack](FCGear_InvoluteRack/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_InvoluteRack.svg style="width   *16px"> Involute Rack** auswählen.
3.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).

## Eigenschaften

Ein FCGear-InvoluteRack-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften   *

### Daten


{{Properties_Title|base}}

-    **add_endings|Bool**   * If {{True}} (default), then the total length of the rack is teeth \* pitch. If {{False}}, then the rack starts with a tooth-flank.

-    **height|Length**   * Default is {{Value|5 mm}}. Value of the gear width.

-    **module|Length**   * Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **teeth|Integer**   * Default is {{Value|15}}. Number of teeth.

-    **thickness|Length**   * Default is {{Value|5}}. Height from the tooth root to the lower side of the rod.


{{Properties_Title|computed}}

-    **transverse_pitch|Length**   * (read-only) Pitch in the transverse plane (see [Notes](#Notes.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**   * Default is {{Value|0 mm}}.

-    **root_fillet|Float**   * Default is {{Value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**   * Default is {{Value|0 °}}. With the helix angle β a helical gear is created -- positive value → rotation direction right, negative value → rotation direction left.

-    **double_helix|Bool**   * Default is {{False}}, {{True}} creates a double helix gear (see [Notes](#Notes.md)).

-    **properties_from_tool|Bool**   * Default is {{False}}. If {{True}} and **beta** is not zero, gear parameters are recomputed internally for the rotated gear.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**   * Default is {{Value|20 °}} (see [Notes](#Notes.md)).


{{Properties_Title|precision}}

-    **simplified|Bool**   * Default is {{False}}, {{True}} generates a simplified display (without teeth).


{{Properties_Title|tolerance}}

-    **clearance|Float**   * Default is {{Value|0.25}} (see [Notes](#Notes.md)).

-    **head|Float**   * Default is {{Value|0}}. This value is used to change the tooth height.


{{Properties_Title|version}}

-    {{PropertyData/de|version|String}}   *

## Hinweise

-    **transverse_pitch**   * The value is the result of multiplication of **module * pi**. This means for the standard involute rack of FCGear   * 15 (**teeth**) \* 3.14 (**transverse_pitch**) is 47.12 mm. See also **module** further below.

-    **clearance**   * At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **double_helix**   * To use the double helical gearing the helix angle β (**beta**) for the helical gearing must first be entered.

-    **module**   * Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m)   * m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth. The result of the multiplication is displayed in **transverse_pitch**

-    **pressure_parameter**   * Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Nützliche Formeln 

See [FCGear InvoluteGear](FCGear_InvoluteGear#Useful_formulas.md).

## Skripten

Use the power of python to automate your gear modeling   * 
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




[Category   *Addons](Category_Addons.md) [Category   *FCGear](Category_FCGear.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InvoluteRack/de
