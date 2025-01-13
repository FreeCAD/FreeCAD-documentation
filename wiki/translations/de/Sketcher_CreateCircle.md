---
 GuiCommand:
   Name: Sketcher CreateCircle
   Name/de: Sketcher KreisErstellen
   MenuLocation: Skizze , Skizzengeometrien , Kreis um Mittelpunkt erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **C**
   SeeAlso: Sketcher_CreateArc/de
---

# Sketcher CreateCircle/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:24px;"> [Sketcher KreisErstellen](Sketcher_CreateCircle/de.md) erstellt einen Kreis durch Festlegen seines Mittelpunktes und eines Punktes im Verlauf seines Umfangs. {{Version/de|1.0}}: Oder wahlweise durch Festlegen dreier Punkte im Verlauf seines Umfangs.

![](images/Sketcher_CircleExample1.png‎ )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung). {{Version/de|1.0}}
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung). {{Version/de|1.0}}

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateCircle.svg" width=16px> [Kreis um Mittelpunkt erstellen](Sketcher_CreateCircle/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreateCircle.svg" width=16px> Kreis um Mittelpunkt erstellen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_CreateCircle.svg" width=16px> Kreis um Mittelpunkt erstellen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** dann **C**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Der Abschnitt **Kreisparameter** ({{Version/de|1.0}}) wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.
4.  Wahlweise die **M**-Taste drücken oder einen Eintrag in der Ausklappliste **Modus** im Abschnitt **Kreisparameter** auswählen, um den Werkzeugmodus zu wechseln:
    -   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:16px;"> **Mitte**:
        1.  Den Mittelpunkt des Kreises auswählen; oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
        2.  Einen Punkt auswählen, um den Radius des Kreises festzulegen; oder mit Dim-OVP: den Radius eingeben.
    -   <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:16px;"> **3 Punkte auf Kreisbogen**. {{Version/de|1.0}}
        1.  Drei Punkte auswählen, um den den Kreis festzulegen; oder mit Pos-OVP: ihre X- und/oder Y-Koordinaten eingeben. Für diese Punkte werden keine Randbedingungen hinzugefügt.
5.  Der Kreis wird erstellt und mögliche auf Pos-OVP und Dim-OVP basierende Randbedingungen hinzugefügt.
6.  Läuft das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md):
    1.  Wahlweise weitere Kreise erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateCircle/de
