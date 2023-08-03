---
 GuiCommand:
   Name: FCGear InvoluteGear
   Name/de: FCGear Evolventenzahnrad
   MenuLocation: Gear , Involute Gear
   Workbenches: FCGear_Workbench/de
   Shortcut: Kein
   Version: v0.16
   SeeAlso: FCGear_CycloidGear/de
---

# FCGear InvoluteGear/de

## Beschreibung

Due to the favourable meshing ratio and the relatively simple production, involute gearing is the most common tooth form in mechanical engineering. Gear wheels can be found wherever movement and force are to be transferred from one part to another. For example, they can be found in machines, cars, watches or household appliances. The movement is often transferred directly from one gear wheel to the other, but sometimes also via a chain. In addition, the direction of rotation can be changed. It is also possible to change a radial movement into a linear one via an [involute rack](FCGear_InvoluteRack.md).

![](images/Involute-Gear_example.png )

:   
    
*Von links nach rechts: Stirnräder mit Geradverzahnung, Schrägverzahnung, Pfeilverzahnung
    *
    

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_InvoluteGear.svg style="width:16px"> [Involute Gear](FCGear_InvoluteGear/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_InvoluteGear.svg style="width:16px"> Involute Gear** auswählen.
3.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).

## Eigenschaften

Ein FCGear-InvoluteGear-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: Default is {{Value|6}}. Change of the involute profile. Changing the value can lead to unexpected results.

-    **simple|Bool**: Default is {{False}}, {{True}} generates a simplified display (without teeth and only a cylinder in pitch diameter).


{{Properties_Title|base}}

-    **height|Length**: Default is {{Value|5 mm}}. Value of the gear width.

-    **module|Length**: Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth (see [Notes](#Notes.md)).


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (read-only)

-    **da|Length**: (read-only) Outside diameter, measured at the addendum (the tip of the teeth).

-    **df|Length**: (read-only) Root diameter, measured at the foot of the teeth.

-    **dw|Length**: (read-only) Working pitch diameter.

-    **transverse_pitch|Length**: (read-only) Pitch in the plane of rotation.


{{Properties_Title|fillets}}

-    **head_fillet|Float**: Default is {{Value|0 mm}}.

-    **root_fillet|Float**: Default is {{Value|0 mm}}.

-    **undercut|Bool**: Default is {{False}}, {{True}} changes the profile of the tooth root (see [Notes](#Notes.md)).


{{Properties_Title|helical}}

-    **beta|Angle**: Default is {{Value|0 °}}. With the helix angle β a helical gear is created -- positive value → rotation direction right, negative value → rotation direction left (see [Notes](#Notes.md)).

-    **double_helix|Bool**: Default is {{False}}, {{True}} creates a double helix gear (see [Notes](#Notes.md)).

-    **properties_from_tool|Bool**: Default is {{False}}. If {{True}} and **beta** is not zero, gear parameters are recomputed internally for the rotated gear.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Default is {{Value|20 °}} (see [Notes](#Notes.md)).

-    **shift|Float**: Default is {{Value|0}}. Generates a positive and negative profile shift (see [Notes](#Notes.md)).


{{Properties_Title|tolerance}}

-    **backlash|Length**: Default is {{Value|0}}. Backlash, also called lash or play, is the distance between the teeth at a gear pair.

-    **clearance|Float**: Default is {{Value|0.25}} (see [Notes](#Notes.md)).

-    **head|Float**: Default is {{Value|0}}. This value is used to change the tooth height.

-    **reversed_backlash|Bool**: {{True}} backlash decrease or {{False}} (default) backlash increase see [Notes](#Notes.md)).


{{Properties_Title|version}}

-    **version|String**:

## Hinweise

-    **beta**: When **beta** is changed, **pitch diameter** also changes. The following formula illustrates how the parameters interact: d = m \* Z / cos beta (Z = number of teeth, d = pitch diameter, m = module). This means for the spur gear: cos beta = 0 and for the helical gear: cos beta \> 0. However, a helix angle of less than 10° has hardly any advantages over straight teeth.

-    **clearance**: At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **double_gear**: To use the double helical gearing the helix angle β (**beta**) for the helical gearing must first be entered.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

-    **shift**: Profile shift is not merely used to prevent undercut. It can be used to adjust center distance between two gears. If a positive correction is applied, such as to prevent undercut in a pinion, the tooth thickness at top is thinner.

-    **teeth**: If the number of teeth is changed, the pitch diameter also changes (**dw**).

-    **undercut**: Undercut is used when the number of teeth of a gear is too small. Otherwise the mating gear will cut into the tooth root. The undercut not only weakens the tooth with a wasp-like waist, but also removes some of the useful involute adjacent to the base circle.

-    **pressure_angle**: 20° is a standard value here. The pressure angle is defined as the angle between the line-of-action (common tangent to the base circles) and a perpendicular to the line-of-centers. Thus, for standard gears, 14.5° pressure angle gears have base circles much nearer to the roots of teeth than 20° gears. It is for this reason that 14.5° gears encounter greater undercutting problems than 20° gears. Important. the pressure angle changes with a profile shift. Only change the parameter, if sufficient knowledge of the gear geometry is available.

-    **reversed_backlash**: If there are several gears, pay attention to which gear the parameter is set for.

## Begrenzungen

Ein 2D-Zahnprofil, erstellt mit der auf null gesetzten {{PropertyData/de|height}}, kann nicht mit Elementen verwendet werden, die eine 2D-Form erfordern. Zum Beispiel akzeptieren [PartDesign Pad](PartDesign_Pad/de.md) und [PartDesign Wendel](PartDesign_AdditiveHelix/de.md) solche Profile nicht als Basis. Technische Details (engl.) findet man unter: [issue on GitHub](https://github.com/looooo/freecad.gears/issues/97).

## Nützliche Formeln 

### Standard-Stirnräder 

Hier bezieht sich "standard" auf Stirnräder ohne Profilverschiebungsbeiwert ($x$).

+++++
| Symbol   | Term                                     | Formula                        | FCGear Parameter                            |
+==========+==========================================+================================+=============================================+
| $m$      | *Module*                                 | \-                             | $\texttt{module}$                           |
+++++
| $z$      | *Number of Teeth*                        | \-                             | $\texttt{teeth}$                            |
+++++
| $\alpha$ | *Pressure Angle*                         | \-                             | $\texttt{pressure} {\_} \texttt{parameter}$ |
|          |                                          | Typically, $\alpha = 20^\circ$ |                                             |
+++++
| d        | *Reference Diameter* or *Pitch Diameter* | $z \cdot m$                    | \-                                          |
+++++
| $h^*_a$  | *Addendum Coefficient*                   | \-                             | $h^*_a = 1 + \texttt{ head}$                |
|          |                                          | Typically, $h^*_a = 1$         |                                             |
+++++
| $h^*_f$  | *Dedendum Coefficient*                   | \-                             | $h^*_f = 1 + \texttt{ clearance}$           |
|          |                                          | Typically, $h^*_f = 1.25$      |                                             |
+++++
| $h_a$    | *Addendum*                               | $h_a = h^*_a \cdot m$          | \-                                          |
+++++
| $h_f$    | *Dedendum*                               | $h_f = h^*_f \cdot m$          | \-                                          |
+++++
| $h$      | *Tooth Height* or *Tooth Depth*          | $h = h_a + h_f$                | \-                                          |
|          |                                          | Typically, $h = 2.25 \cdot m$  |                                             |
+++++
| $x$      | *Profile Shift Coefficient*              | \-                             | $\texttt{shift}$                            |
|          |                                          | For standard gears, $x = 0$    |                                             |
+++++

: style=\"text-align: left;\" \| Basic formulas common to internal and external standard spur gears

++++
| Symbol | Term            | Formula                              |
+========+=================+======================================+
| $d_a$  | *Tip Diameter*  | $d_a = d + 2 \cdot h_a$              |
|        |                 | Typically, $d_a = (z + 2) \cdot m$   |
++++
| $d_f$  | *Root Diameter* | $d_f = d - 2 \cdot h_f$              |
|        |                 | Typically, $d_f = (z - 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Basic formulas specific to external standard spur gears

++++
| Symbol | Term            | Formula                              |
+========+=================+======================================+
| $d_a$  | *Tip Diameter*  | $d_a = d - 2 \cdot h_a$              |
|        |                 | Typically, $d_a = (z - 2) \cdot m$   |
++++
| $d_f$  | *Root Diameter* | $d_f = d + 2 \cdot h_f$              |
|        |                 | Typically, $d_f = (z + 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Basic formulas specific to internal standard spur gears

++++
| Symbol | Term                     | Formula                       |
+========+==========================+===============================+
| $a$    | *Center Distance*        | $d = \frac{d_1 + d_2}{2}$     |
++++
| $c$    | *Tip and Root Clearance* | $c_1 = h_{f2} - h_{a1}$       |
|        |                          | $c_2 = h_{f1} - h_{a2}$       |
|        |                          | Typically, $c = 0.25 \cdot m$ |
++++

: style=\"text-align: left;\" \| Basic formulas specific for a pair of external standard spur gears

-   **Helical and double helical gearing**
    -   
        **pitch diameter (dw)**
        
        = **module** \* **teeth** : **cos beta**

    -   
        **axle base**
        
        = **(pitch diameter (dw) 1 + 2)** : 2

    -   
        **addendum diameter**
        
        = **pitch diameter (dw)** + 2 \* **module**

    -   
        **module**
        
        = **pitch diameter (dw)** \* **cos beta** : **teeth**

## Skripten

Die Macht von Python man nutzen muss, Zahnräder zu modellieren automatisch: 
```python
import FreeCAD as App
import freecad.gears.commands
gear = freecad.gears.commands.CreateInvoluteGear.create()
gear.teeth = 20
gear.beta = 20
gear.height = 10
gear.double_helix = True
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
```



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InvoluteGear/de
