---
 GuiCommand:
   Name: Sketcher CreateRectangle
   Name/de: Sketcher RechteckErstellen
   MenuLocation: Skizze , Skizzengeometrien , Rechteck erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **R**
   SeeAlso: Sketcher_CreatePolyline/de
---

# Sketcher CreateRectangle/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> [Sketcher RechteckErstellen](Sketcher_CreateRectangle/de.md) erstellt ein Rechteck. {{Version/de|1.0}}: Das Werkzeug besitzt vier Modi, von denen zwei auch Parallelogramme erstellen können. Abgerundeter Ecken und die Erstellung einer versetzten Kopie sind optionale Funktionen.

![](images/SketcherCreateRectangleExample.png‎ )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung). {{Version/de|1.0}}
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung). {{Version/de|1.0}}

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateRectangle.svg" width=16px> [Rechteck](Sketcher_CreateRectangle/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreateRectangle.svg" width=16px> Rechteck erstellen** auswählen.
    -   Ein Rechtsklick in der [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_CreateRectangle.svg" width=16px> Rechteck erstellen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** dann **R**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Der Abschnitt **Rechteckparameter** ({{Version/de|1.0}}) wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.




1.  Wahlweise die **U**-Taste drücken oder die CheckBox **Abgerundete Ecken** aktivieren, um das Rechteck mit Verrundungen zu versehen. {{Version/de|1.0}}
2.  Wahlweise die **J**-Taste drücken oder die CheckBox **Rahmen** aktivieren, um eine zweite versetzte Form zu erstellen. {{Version/de|1.0}}
3.  Wahlweise die **M**-Taste drücken oder in der Ausklappliste \"Modus\" auswählen, um den Werkzeugmodus zu wechseln:
    -   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:16px;"> **Ecke, Breite, Höhe**:
        1.  Die erste Ecke des Rechtecks auswählen. Oder mit Pos-OVP: ihre X- und/oder Y-Koordinate eingeben.
        2.  Die gegenüberliegende Ecke des Rechtecks auswählen. Oder mit Dim-OVP: die Breite und/oder die Höhe des Rechtecks auswählen.
    -   <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:16px;"> **Zentrum, Breite, Höhe**: {{Version/de|1.0}}
        1.  Den Mittelpunkt des Rechtecks auswählen. Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
        2.  Eine Ecke des Rechtecks auswählen. Oder mit Dim-OVP: die Breite und/oder die Höhe des Rechtecks eingeben.
    -   <img alt="" src=images/Sketcher_CreateRectangle3Points.svg  style="width:16px;"> **3 Ecken**: {{Version/de|1.0}}
        1.  Die erste Ecke des Rechtecks auswählen. Oder mit Pos-OVP: ihre X- und/oder Y-Koordinate eingeben.
        2.  Den Endpunkt der ersten Kante des Rechtecks auswählen. Oder mit Dim-OVP: die Länge und/oder den Winkel der ersten Kante eingeben. Der Winkel bezieht sich auf die X-Achse der Skizze.
        3.  Eine dritte Ecke des Rechtecks, gegenüber der ersten auswählen. Oder mit Dim-OVP: die Länge und/oder der Winkel der zweiten Kante eingeben. Der Winkel bezieht sich auf die erste Kante. Nur wenn dieser Winkel 90° ist, wird das Ergebnis ein Rechteck sein.
    -   <img alt="" src=images/Sketcher_CreateRectangle3Points_Center.svg  style="width:16px;"> **Zentrum, 2 Ecken**: {{Version/de|1.0}}
        1.  Den Mittelpunkt des Rechtecks auswählen. Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
        2.  Die erste Ecke des Rechtecks auswählen. Oder mit Pos-OVP: ihre X- und/oder Y-Koordinate eingeben.
        3.  Die zweite Ecke des Rechtecks auswählen. Oder mit Dim-OVP: die Länge und/oder den Winkel der Kante zwischen der ersten und der zweiten Ecke eingeben. Der Winkel bezieht sich auf die andere Kante, die mit der ersten Ecke verbunden ist. Nur wenn dieser Winkel 90° ist, wird das Ergebnis ein Rechteck sein.
4.  Wurde **Abgerundete Ecken** aktiviert: Einen Punkt zum Festlegen des Radius auswählen. Oder mit Dim-OVP: Den Wert eingeben.
5.  Wurde **Rahmen** aktiviert: Einen Punkt zum Festlegen der Breite des Rahmens (Versatz) auswählen. Oder mit Dim-OVP: Den Wert eingeben. Erfolgt der Versatz nach innen und ist größer als der Radius, wird die versetzte Form keine Rundungen enthalten.
6.  Die Geometrie wird erstellt und mögliche auf Pos-OVP und Dim-OVP basierende Randbedingungen hinzugefügt.
7.  Läuft das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md):
    1.  Wahlweise weitere Rechtecke erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/de
