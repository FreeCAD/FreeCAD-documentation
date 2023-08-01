---
- GuiCommand:
   Name:FCGear WormGear
   Name/de:FCGear WormGear
   MenuLocation:Gear → Worm Gear
   Workbenches:[FCGear](FCGear_Workbench/de.md)
   Shortcut:Kein
   Version:v0.16
   SeeAlso:[PartDesign Evolventenrad](PartDesign_InvoluteGear/de.md)
---

# FCGear WormGear/de

## Beschreibung

Die Schneckenwelle kann als Spezialfall einer Schrägverzahnung angesehen werden. Man kann sie sich als Stirnrad mit nur einem Zahn vorstellen. Nun vergrößert man den Schrägungswinkel so sehr, dass sich der Zahn mehrmals um das Stirnrad windet, bevor es die gegenüberliegende Seite erreicht. Das Ergebnis wäre eine eingängige Schneckenwelle.

Eine eingängige Schneckenwelle bewegt das Schneckenrad mit jeder vollen Umdrehung (360°) um einen Zahn weiter. So ergibt sich mit einem Schneckenrad mit 24 Zähnen eine Untersetzung von 24:1. Für mehrgängige Schneckenwellen ergibt sich die Untersetzung aus der Anzahl der Zähne des Schneckenrades, geteilt durch die Anzahl der Gänge der Schneckenwelle.

Eine Schneckenwelle kann nur zusammen mit einem Schneckenrad verwendet werden. Dies wird Schneckenantrieb (oder Schneckengetriebe) genannt. Wie andere Zahnradanordnungen auch, kann ein Schneckengetriebe die Umlaufgeschwindigkeit verringern oder ein höheres Drehmoment übertragen. Ein Hauptvorteil von Schneckenantrieben ist, dass sie eine Bewegung um 90° umlenken können. Ein Schneckengetriebe ist auch selbsthemmend.

![](images/Worm-Gear_example.png ) 
*Dreigängige Schneckenwelle (3 Zähne)*

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_WormGear.svg style="width:16px"> [Worm Gear](FCGear_WormGear/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_WormGear.svg style="width:16px"> Worm Gear** auswählen.
3.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).

## Eigenschaften

Ein FCGear-WormGear-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title|base}}

-    **diameter|Length**: Default is {{Value|5 mm}}. Pitch diameter.

-    **height|Length**: Default is {{Value|5 mm}}. Value of the worm length.

-    **module|Length**: Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **reverse_pitch|Bool**: Default is {{False}}, {{True}} changes the rotating direction from right to left.

-    **teeth|Integer**: Default is {{Value|3}}. Number of teeth (see [Notes](#Notes.md)).


{{Properties_Title|computed}}

-    **beta|Angle**: (read-only) Lead angle (see also the information in [Notes](#Notes.md) and [Useful formulas](#Useful_formulas.md)).


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Default is {{Value|20 °}} (see [Notes](#Notes.md)).


{{Properties_Title|tolerance}}

-    **clearance|Float**: Default is {{Value|0.25}} (see [Notes](#Notes.md)).

-    **head|Float**: Default is {{Value|0}}. This value is used to change the tooth height.


{{Properties_Title|version}}

-    **version|String**:

## Hinweise

-    **beta**: If the lead angle is less than 5°, it is a self-locking gear. A typical example are the tuning pegs on a guitar or ukulele.

-    **clearance**: At a worm gearing, clearance is the distance between the tooth tip of the worm and the tooth root of the worm wheel.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth. If the module is changed, the lead angle also changes (**beta**).

-    **teeth**: The number of teeth in a worm is called the number of threads. Correspondingly, one speaks of single, double or multiple thread worms. In general, mainly single worms are produced, but in special cases the number of starts can be up to four (sometimes also more). If the number of teeth is changed, **beta** also changes.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Nützliche Formeln 

-    **beta (lead angle)**= arctan (**module** \* **teeth** : **pitchdiameter (diameter)**)

-    **axial pitch**= **pi** \* **module** \* **teeth**

-    **beta (lead angle)**= arctan (**axial pitch** : (**pitchdiameter (diameter)** \* **pi**))

-    **worm length**= 4,5 \* **module** \* **pi**

## Schneckenrad

Das Schneckenrad muss von Hand erstellt werden. Ein [FCGear Evolventenrad](FCGear_InvoluteGear/de.md) kann für eine vereinfachte Konstruktion verwendet werden. In jedem Falle wird dafür Fachwissen über Zahnräder benötigt.

![](images/Worm-Gear_example3.png ) 
*Schneckenwelle mit Schneckenrad*



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear WormGear/de
