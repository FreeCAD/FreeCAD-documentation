---
 GuiCommand:
   Name: Sketcher CreateLine
   Name/de: Sketcher LinieErstellen
   MenuLocation: Skizze , Skizzengeometrien , Linie erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: L
   SeeAlso: Sketcher_CreatePolyline/de
---

# Sketcher CreateLine/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreateLine.svg  style="width:24px;"> [Sketcher LinieErstellen](Sketcher_CreateLine/de.md) erstellt eine Linie. {{Version/de|1.0}}: Wenn In-Ansicht-Parameter ([On-View-Parameters](Sketcher_Preferences/de#Allgemein.md)) aktiviert wurden, besitzt das Werkzeug drei Modi.

![](images/Sketcher_LineExample1.png‎ )



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung). {{Version/de|1.0}}
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung). {{Version/de|1.0}}

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateLine.svg" width=16px> [Linie erstellen](Sketcher_CreateLine/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreateLine.svg" width=16px> Linie erstellen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_CreateLine.svg" width=16px> Linie erstellen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** then **L**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Die Modi dieses Werkzeugs erfordern einen vorherigen Abschnitt. Dafür eine der folgenden Möglichkeiten auswählen:
    -   Zwei Punkte auswählen, um einen Linienabschnitt festzulegen.
4.  Wenn die [In-Ansicht-Parameter](Sketcher_Preferences/de#Allgemein.md) aktiviert sind wird der Abschnitt **Linienparameter** ({{Version/de|1.0}}) im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) hinzugefügt.
5.  Wahlweise die **M**-Taste drücken oder eine möglichkeit in der Ausklappliste Modus auswählen, um den Werkzeugmodus zu ändern:
    -   <img alt="" src=images/Sketcher_CreateLineAngleLength.svg  style="width:16px;"> **Punkt, Läng, Winkel**: {{Version/de|1.0}}
        1.  Den Startpunkt der Linie auswählen; Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
        2.  Den Endpunkt der Linie auswählen; Oder mit Pos-OVP: ihre Länge und ihren Winkel eingeben. Der Winkel bezieht sich auf die X-Achs der Skizze.
    -   <img alt="" src=images/Sketcher_CreateLineLengthWidth.svg  style="width:16px;"> **Punkt, Breite, Höhe**: {{Version/de|1.0}}
        1.  Den Startpunkt der Linie auswählen; Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
        2.  Den Endpunkt der Linie auswählen; Oder mit Pos-OVP: seinen X- und/oder Y-Abstand zum Startpunkt eingeben.
    -   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:16px;"> **2 Punkte**:
        1.  Den Startpunkt der Linie auswählen; Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
        2.  Den Endpunkt der Linie auswählen; Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
6.  Die Linie wird erstellt und passende Pos-OVP- und Dim-OVP-basierte Randbedingungen werden hinzugefügt.
7.  Wenn das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) läuft:
    1.  Wahlweise weitere Linien erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken, oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/de
