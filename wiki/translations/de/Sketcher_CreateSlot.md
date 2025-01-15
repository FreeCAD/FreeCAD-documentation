---
 GuiCommand:
   Name: Sketcher CreateSlot
   Name/de: Sketcher NutErstellen
   MenuLocation: Sketch , Skizzengeometrien , Nut erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **S**
   SeeAlso: Sketcher_CreateArcSlot/de
---

# Sketcher CreateSlot/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [Sketcher NutErstellen](Sketcher_CreateSlot/de.md) erstellt eine \"Nut\", ein geschlossenen Linienzug, der aus zwei Halbkreisen besteht, die mit zwei parallelen geraden Linien verbunden sind.

![](images/SketcherCreateSlotExample.png‎ )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung). {{Version/de|1.0}}
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung). {{Version/de|1.0}}

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateSlot.svg" width=16px> [NutErstellen](Sketcher_CreateSlot/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreateSlot.svg" width=16px> Nut erstellen** auswählen.
    -   Das Tastaturkürzel **G** dann **S**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Den Mittelpunkt des ersten Halbkreises auswählen. Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
4.  Den Mittelpunkt des zweiten Halbkreises auswählen. Oder mit Dim-OVP: den Abstand zwischen den Mittelpunkten und/oder den Winkel der \"Nut\" eingeben. Der Winkel bezieht sich auf die X-Achse der Skizze.
5.  Einen Punkt auswählen, um den Radius der \"Nut\" festzulegen. Oder mit Dim-OVP: diesen Radius eingeben.
6.  Die \"Nut\" wird erstellt und passende auf Pos-OVP und Dim-OVP basierenden Randbedingungen werden hinzugefügt.
7.  Wenn das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) läuft:
    1.  Wahlweise weitere \"Nuten\" erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-    {{VersionMinus/de|0.21}}({{Version/de|0.20}}): Wird **Ctrl** bzw. **Strg** gedrückt gehalten, während man den zweiten Mittelpunkt auswählt, wird die \"Nut\" horizontal oder vertikal ausgerichtet.

-    {{Version/de|1.0}}: [Einrasten auf Winkel](Sketcher_Snap/de.md) kann eingesetzt werden, um den Winkel der \"Nut\" zu beeinflussen.

-    {{Version/de|0.20}}: Eine \"Nut\" kann auch horizontal oder vertikal festgelegt werden, wenn die Option [Automatische Randbedingungen](Sketcher_Workbench/de#Automatische_Randbedingungen.md) aktiviert ist.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateSlot/de
