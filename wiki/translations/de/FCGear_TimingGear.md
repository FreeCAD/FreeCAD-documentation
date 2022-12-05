---
- GuiCommand:/de
   Name:FCGear TimingGear
   Name/de:FCGear Zahnriemenscheibe
   MenuLocation:Gear → Timing Gear
   Workbenches:[FCGear](FCGear_Workbench/de.md)
   Shortcut:Keine
   Version:v0.16
   SeeAlso:
---

# FCGear TimingGear/de

## Beschreibung

Ein Zweck von Zahnriemen ist die Synchronisation von Kurbelwelle und Nockenwelle eines Verbrennungsmotors. Die Kurbelwelle dreht sich, um die Kolben in den Zylindern auf und ab zu bewegen. Die Nockenwelle bewirkt das Öfnen und Schließen der Ein- und Auslassventile der Zylinder. Diese Komponenten (eines Zahnriemenantriebs) sind wichtig für einen korrekten Ablauf aller Bewegungen eines Motors.

Zahnriemenscheiben werden mit einem Zahnriemen (Steueriemen) verbunden. (engl. timing gear kann auch (Steuer-) Kettenantrieb bedeuten)

![](images/Timing-Gear_example.png ) 
*Oben: Zahnriemenscheibe*

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/de.md) wechseln.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/FCGear_TimingGear.svg style="width:16px"> [Timing Gear](FCGear_TimingGear/de.md)** drücken.
    -   Den Menüeintrag **Gear → [<img src=images/FCGear_TimingGear.svg style="width:16px"> Timing Gear** auswählen.
3.  Die Einstellungen den geforderten Randbedingungen entsprechend ändern (siehe [Eigenschaften](#Eigenschaften.md)).

## Eigenschaften

Ein FCGear-TimingGear-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    **height|Length**: Voreingestellt ist {{Value|5 mm}}. Wert der Zahnbreite.

-    **teeth|Integer**: Voreingestellt ist {{Value|15}}. Anzahl der Zähne.

-    **type|Enumeration**: Voreingestellt ist {{Value|gt2}}. Art des Zahnriemens -- Teilung des Zahnriemens (siehe [Hinweise](#Hinweise.md)).


{{Properties_Title|computed}}

-    **h|Length**: (nur Lesezugriff) Radiale Zahnhöhe.

-    **offset|Length**: (nur Lesezugriff) X-Versatz des zweiten Bogenmittelpunktes.

-    **pitch|Length**: (nur Lesezugriff) Zahnteilung.

-    **r0|Length**: (nur Lesezugriff) Radius des ersten Bogens.

-    **r1|Length**: (nur Lesezugriff) Radius des zweiten Bogens.

-    **rs|Length**: (nur Lesezugriff) Radius des dritten Bogens.

-    **u|Length**: (nur Lesezugriff) Radialer Unterschied zwischen Teilkreisdurchmesser und Kopfkreisdurchmesser.


{{Properties_Title|version}}

-    {{PropertyData/de|version|String}}:

## Hinweise

-    **type**: Bestimmt die Teilung der Zahnriemen (Abstand von Zahnmitte zu Zahnmitte aufeinanderfolgender Zähne). GT2 steht für eine Teilung von 2 mm, GT3 für eine von 3 mm, GT5 für eine von 5 mm usw..

## Nützliche Formeln 

-    **Kopfkreisdurchmesser**= **Teilkreisdurchmesser** + 2 \* **Modul**

-    **Riemenlänge**= 2 \* **Achsabstand** + **Zahnriementeilung** : 2 \* **(Zähne 1 + 2)** + **Zahnriementeilung²** : 4 \* pi² \* **Achsabstand** \* **(Zähne 1 - 2)²**

-    **Achsabstand**= **Riemenlänge** : 4 - **Zahnriementeilung** : 8 \* **(Zähne 1+2)** + ¼ \* sqrt \[**Riemenlänge** - ½ \* **Zahnriementeilung** \* **(Zähne 1+2)²** - 2 \* **Zahnriementeilung²** \* **(Zähne 1+2)²** : pi²\]



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear TimingGear/de
