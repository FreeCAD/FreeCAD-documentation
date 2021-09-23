---
- GuiCommand:/de
   Name:Part Plane   Name/de:Part Ebene
   MenuLocation:Part → [Grundkörper erstellen](Part_Primitives/de.md) → Ebene
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Grundkörper](Part_Primitives/de.md)
---

# Part Plane/de


</div>

## Description


<div class="mw-translate-fuzzy">

## Beschreibung

Erstellt eine einfache parametrische Ebene 10 x 10 mm mit den Parametern für Position, Länge und Breite. Als Vorgabe wird die Ebene am Ursprung (0,0,0) platziert.


</div>

![](images/PartPlane.png )

## Anwendung

Die Standardebene wird erstellt mit der linken unteren Ecke im Ursprung (0,0,0). Um diese Parameter zu ändern, öffne den Location-Abschnitt und gib die gewünschten Werte in die entsprechenden Eingabefelder ein oder klicke auf die 3D-Ansicht und wähle einen Punkt, die Koordinaten des Punktes werden aus den Feldern übernommen. Im Direction-Menü kannst Du auch einen Standard-Vektor (X, Y oder Z) senkrecht zur Ebene definieren oder \'Benutzerdefiniert\...\' klicken, um in der sich öffnenden Dialogbox eine abweichende Richtung (z.B. 1, 0, -1 erstellt eine um 45° geneigte Ebene in Bezug auf die X und Z Achse) zu definieren.


<div class="mw-translate-fuzzy">

Die Eigenschaften können später in **Combo Ansicht → Daten** nach der Auswahl des Elements verändert werden.


</div>

## Eigenschaften

### Daten


{{TitleProperty|Base}}

-    **Label**: String name of the object, defaults to \'Plane\'. User may rename it.

-    **Placement**: Placement of feature is defined by below angle, axis and position.

-    **Angle**: Angle of rotation relative to the below axis.

-    **Axis**: Defines the axis of rotation plane: X, Y, or Z. Defaults to Z axis, Z = 1

-    **Position**: Position X, Y, Z, relative to the origin 0, 0, 0.


{{TitleProperty|Plane}}

-    **Length**: Length is the dimension along the X axis The default value is 10 mm

-    **Width**: Width is the size of the Y-axis The default value is 10 mm

### Ansicht

You have the standard properties view.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Plane/de
