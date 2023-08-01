---
- GuiCommand:
   Name:FCGear LanternGear
   Name/de: FCGear Triebstockrad
   MenuLocation:Gear → Lantern Gear
   Workbenches:[FCGear](FCGear_Workbench/de.md)
   Shortcut:Keine
   Version:v0.16
   SeeAlso:
---

# FCGear LanternGear/de

## Beschreibung

Die Triebstockverzahnung ist eine Sonderform der Zykloidenverzahnung, bei der Wälzkreis und Teilkreis gleich groß sind. Außerdem werden die Zähne des größeren Rades in einem Getriebe durch Zylinder ersetzt. Das kleine Rad erhält eine Zykloidenverzahnung. Daraus ergibt sich eine einseitige Punktverzahnung. Triebstockverzahnungen können nur gerade verzahnt sein.

Da sie sehr einfach aufgebaut sind, gehören sie zu den ältesten Formen von Getrieben. Triebstockgetriebe werden eingesetzt, wenn große Übersetzungsverhältnisse erforderlich sind, z. B. in Drehwerken von Mühlen oder Holzumschlagskränen.

Triebstockräder mit Rollenketten sind eine kostengünstige und robuste Alternative zu Zahnstangen- und Ritzelantrieben. Durch die tangentiale Führung der gespannten Triebstockkette entlang des Triebstocks wird eine lineare Bewegung der Kette in eine Drehbewegung des Rades umgesetzt. Umgekehrt kann eine lineare Bewegung der Kette auch durch die Drehbewegung des Triebstockrades (Motorrad/Fahrrad) erreicht werden.

![](images/Lantern-Gear_example.png )

:   
    
*Oben: Triebstockrad*
    

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_LanternGear.svg style="width:16px"> [Lantern Gear](FCGear_LanternGear/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_LanternGear.svg style="width:16px"> Lantern Gear** auswählen.
3.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).

## Eigenschaften

### Daten

Ein FCGear-LanternGear-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:


{{Properties_Title|accuracy}}

-    {{PropertyData/de|num_profiles|Integer}}: Voreingestellt ist {{Value|10}}. Der Wert muss normalerweise nicht geändert werden.


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|bolt_radius|Length}}: Voreingestellt ist {{Value|1 mm}}. Durchmesser des Zylinders auf der drehenden Scheibe, die das zweites \"Zahnrad\" darstellt.

-    {{PropertyData/de|height|Length}}: Voreingestellt ist {{Value|5 mm}}. Wert der Zahnbreite.

-    {{PropertyData/de|module|Length}}: Voreingestellt ist {{Value|1 mm}}. (Der) Modul, das Verhältnis von Teilkreisdurchmesser des Zahnrades zur Anzahl der Zähne (siehe [Hinweise](#Hinweise.md)).


{{Properties_Title|gear_parameter}}

-    {{PropertyData/de|teeth|Integer}}: Voreingestellt ist {{Value|15}}. Anzahl der Zähne.


{{Properties_Title|tolerance}}

-    {{PropertyData/de|head|Float}}: Voreingestellt ist {{Value|0}}.


{{Properties_Title|version}}

-    {{PropertyData/de|version|String}}:

## Hinweise

-    **Modul**: Nach den Regeln der ISO (International Organization for Standardization) ist der Modul das (ganzzahlige) Verhältnis von Teilkreisdurchmesser zur Anzahl der Zähne. Multipliziert man den Modul (m) mit Pi, erhält man die (Zahn-)Teilung (p) (engl. pitch). Moduln (mit zugehörigen Teilungswerten): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Die Teilung ist der Abstand zwischen zwei entsprechenden Punkten (auf dem Teilkreis) zweier benachbarter Zähne.

## Nützliche Formeln 

-    **Kopfkreisdurchmesser**= **Modul** \* **(Anzahl der Zähne +2)**

-    **Teilkreisdurchmesser**= **Modul** \* **Anzahl der Zähne**

-    **Achsabstand**= (**Teilkreisdurchmesser1 (Zahnrad1)** + **Teilkreisdurchmesser2 (Zahnrad 2)**) / 2



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear LanternGear/de
