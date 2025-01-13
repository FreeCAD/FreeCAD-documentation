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

Dank des günstigen Eingriffverhältnisses und der relativ einfachen Herstellung, ist die Evolventenverzahnung die am weitesten verbreitete Zahnform in der mechanischen Konstruktion. Zahnräder findet man überall, wo Bewegung und Kraft von einem Bauteil auf ein anderes übertragen werden. Sie befinden sich z.B. in Maschinen, Autos, Uhren und Haushaltsgeräten. Die Bewegung wird oft direkt von einem Zahnrad auf ein anderes übertragen, aber manchmal auch über eine Kette. Außerdem kann die Drehrichtung geändert werden. Es ist auch möglich, mit Hilfe einer [Evolventenzahnstange](FCGear_InvoluteRack/de.md), eine Drehbewegung in eine lineare Bewegung umzuwandeln.

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

-    {{PropertyData/de|numpoints|Integer}}: Standardwert {{Value|20}}. Change of the involute profile. Das Ändern des Wertes kann zu unerwarteten Ergebnissen führen.

-    {{PropertyData/de|simple|Bool}}: Standardwert {{False}}, {{True}} erstellt eine vereinfachte Darstellung (ohne Zähne, nur ein Zylinder mit Teilkreisdurchmesser).


{{Properties_Title|base}}

-    {{PropertyData/de|height|Length}}: Standardwert {{Value|5 mm}}. Zahnbreite.

-    {{PropertyData/de|module|Length}}: Standardwert {{Value|1 mm}}. Der Modul ist das Verhältnis des Teilkreisdurchmessers zur Zähnezahl (siehe [Hinweise](#Hinweise.md)).

-    {{PropertyData/de|num_teeth|Integer}}: Standardwert {{Value|15}}. Zähnezahl (siehe [Hinweise](#Hinweise.md)).


{{Properties_Title|computed}}

-    {{PropertyData/de|addendum_diameter|Length}}: Standardwert {{Value|17 mm}}. Kopfkreisdurchmesser, am Zahnkopf gemessen (Außendurchmesser).

-    {{PropertyData/de|angular_backlash|Angle}}: (Schreibgeschützt) Zahnspiel (-winkel), der Winkel, um den sich dieses Zahnrad drehen kann, ohne das andere Zahnrad der Paarung zu bewegen.

-    {{PropertyData/de|pitch_diameter|Length}}: Standardwert {{Value|15 mm}}. Der Teilkreisdurchmesser (Wälzkreisdurchmesser).

-    {{PropertyData/de|root_diameter|Length}}: (Schreibgeschützt) Fußkreisdurchmesser, am Zahnlückengrund gemessen.

-    {{PropertyData/de|transverse_pitch|Length}}: Standardwert {{Value|3.14 mm}}. The transverse pitch.

-    {{PropertyData/de|traverse_module|Length}}: Standardwert {{Value|1 mm}}. The traverse module of the generated gear.


{{Properties_Title|fillets}}

-    {{PropertyData/de|head_fillet|Float}}: Standardwert {{Value|0 mm}}. Kopfrundung

-    {{PropertyData/de|root_fillet|Float}}: Standardwert {{Value|0 mm}}. Fußrundung

-    {{PropertyData/de|undercut|Bool}}: Standardwert {{False}}, {{True}} ändert das Profil des Zahnlückengrundes (siehe [Hinweise](#Hinweise.md)).


{{Properties_Title|helical}}

-    {{PropertyData/de|double_helix|Bool}}: Standardwert {{False}}, {{True}} erstellt ein pfeilverzahntes Stirnrad (siehe [Hinweise](#Hinweise.md)).

-    {{PropertyData/de|helix_angle|Angle}}: Standardwert {{Value|0 °}}. Mit dem Schrägungswinkel β wird ein schrägverzahtes Stirnrad (Schrägstirnrad) erstellt -- positiver Wert → Drehrichtung nach rechts, negativer Wert → Drehrichtung nach links (siehe [Hinweise](#Hinweise.md)).

-    {{PropertyData/de|properties_from_tool|Bool}}: Standardwert {{False}}. Wenn {{True}} und die {{PropertyData/de|helix_angle}} ist nicht Null, werden die Parameter intern für das umgedrehte Zahnrad berechnet.


{{Properties_Title|hole}}

-    {{PropertyData/de|Axle_hole|Bool}}: Standardwert {{False}}. {{True}} aktiviert eine Bohrung in der Mitte zum Verbinden mit einer Welle.

-    {{PropertyData/de|Axle_holesize|Length}}: Standardwert {{Value|10 mm}}. Durchmesser der Wellenbohrung.

-    {{PropertyData/de|offset_hole|Bool}}: Standardwert {{False}}, {{True}} aktiviert eine versetzte Bohrung.

-    {{PropertyData/de|offset_holeoffset|Length}}: Standardwert {{Value|10 mm}}. Der Versatz der versetzten Bohrung.

-    {{PropertyData/de|offset_holesize|Length}}: Standardwert {{Value|10 mm}}. Der Durchmesser der versetzten Bohrung.


{{Properties_Title|involute}}

-    {{PropertyData/de|pressure_angle|Angle}}: Standardwert {{Value|20 °}}, Eingriffwinkel (siehe [Hinweise](#Hinweise.md)).

-    {{PropertyData/de|shift|Float}}: Standardwert {{Value|0}}. Erstellt eine positive oder negative Profilverschiebung (siehe [Hinweise](#Hinweise.md)).


{{Properties_Title|tolerance}}

-    **backlash|Length**: Default is {{Value|0}}. Backlash, also called lash or play, is the distance between the teeth at a gear pair.

-    **clearance|Float**: Default is {{Value|0.25}} (see [Notes](#Notes.md)).

-    **head|Float**: Default is {{Value|0}}. This value is used to change the tooth height.

-    **reversed_backlash|Bool**: {{True}} backlash decrease or {{False}} (default) backlash increase see [Notes](#Notes.md)).


{{Properties_Title|version}}

-    {{PropertyData/de|version|String}}:



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
| Symbol   | Begriff                                            | Formel                            | FCGear-Parameter                        |
+==========+====================================================+===================================+=========================================+
| $m$      | (der) *Modul*                                      | \-                                | $\texttt{module}$                       |
+++++
| $z$      | *Zähnezahl*                                        | \-                                | $\texttt{teeth}$                        |
+++++
| $\alpha$ | *Eingriffwinkel*                                   | Üblicherweise $\alpha = 20^\circ$ | $\texttt{pressure} {\_} \texttt{angle}$ |
+++++
| $d$      | *Teilkreisdurchmesser* oder *Wälzkreisdurchmesser* | $z \cdot m$                       | $\texttt{dw}$                           |
+++++
| $h^*_a$  | *Addendum Coefficient*                             | Üblicherweise $h^*_a = 1$         | $h^*_a = 1 + \texttt{ head}$            |
+++++
| $h^*_f$  | *Dedendum Coefficient*                             | Üblicherweise $h^*_f = 1.25$      | $h^*_f = 1 + \texttt{ clearance}$       |
+++++
| $h_a$    | *Kopfhöhe*                                         | $h_a = h^*_a \cdot m$             | \-                                      |
+++++
| $h_f$    | *Fußhöhe*                                          | $h_f = h^*_f \cdot m$             | \-                                      |
+++++
| $h$      | *Zahnhöhe*                                         | $h = h_a + h_f$                   | \-                                      |
|          |                                                    | Üblicherweise $h = 2.25 \cdot m$  |                                         |
+++++
| $x$      | *Profilverschiebungsfaktor*                        | Für Standard-Stirnräder, $x = 0$  | $\texttt{shift}$                        |
+++++

: style=\"text-align: left;\" \| Grundlegende Formeln für sowohl Innenräder als auch Stirnräder

++++
| Symbol | Begriff                | Formel                                  |
+========+========================+=========================================+
| $d_a$  | *Kopfkreisdurchmesser* | $d_a = d + 2 \cdot h_a$                 |
|        |                        | Üblicherweise $d_a = (z + 2) \cdot m$   |
++++
| $d_f$  | *Fußkreisdurchmesser*  | $d_f = d - 2 \cdot h_f$                 |
|        |                        | Üblicherweise $d_f = (z - 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Grundlegende Formeln für Standard-Stirnräder

++++
| Symbol | Begriff                | Formel                                  |
+========+========================+=========================================+
| $d_a$  | *Kopfkreisdurchmesser* | $d_a = d - 2 \cdot h_a$                 |
|        |                        | Üblicherweise $d_a = (z - 2) \cdot m$   |
++++
| $d_f$  | *Fußkreisdurchmesser*  | $d_f = d + 2 \cdot h_f$                 |
|        |                        | Üblicherweise $d_f = (z + 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Grundlegende Formeln für Standard-Innenräder

++++
| Symbol | Begriff       | Formel                           |
+========+===============+==================================+
| $a$    | *Achsabstand* | $a = \frac{d_1 + d_2}{2}$        |
++++
| $c$    | *Kopfspiel*   | $c_1 = h_{f2} - h_{a1}$          |
|        |               | $c_2 = h_{f1} - h_{a2}$          |
|        |               | Üblicherweise $c = 0.25 \cdot m$ |
++++

: style=\"text-align: left;\" \| Grundlegende Formeln für eine Standard-Stirnradpaarung

-   **Schrägverzahnung und Pfeilverzahnung**
    -   
        **Teilkreisdurchmesser (dw)**
        
        = **Modul** \* **Zähnezahl** : **cos beta**

    -   
        **Achsabstand**
        
        = **(Teilkreisdurchmesser (dw) 1 + Teilkreisdurchmesser (dw) 2)** : 2

    -   
        **Kopfkreisdurchmesser**
        
        = **Teilkreisdurchmesser (dw)** + 2 \* **Modul**

    -   
        **Modul**
        
        = **Teilkreisdurchmesser (dw)** \* **cos beta** : **Zähnezahl**



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
