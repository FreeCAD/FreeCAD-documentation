---
 GuiCommand:
   Name: Sketcher CreateEllipseByCenter
   Name/de: Sketcher EllipseUmMittelpunktErstellen
   MenuLocation: Skizze , Skizzengeometrien , Ellipse um Mittelpunkt erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **E** **E**
   Version: 0.15
   SeeAlso: Sketcher_CreateArcOfEllipse/de
---

# Sketcher CreateEllipseByCenter/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:24px;"> [EllipseUmMittelpunktErstellen](Sketcher_CreateEllipseByCenter/de.md): Erstellt eine Ellipse durch Festlegen ihres Mittelpunktes, eines Endpunktes einer ihrer Achsen und eines Punktes im Verlauf ihres Umfangs. {{Version/de|1.0}}: Oder durch Festlegen beider Endpunkte einer Achse und eines Punktes im Verlauf ihres Umfangs.

![](images/Sketcher_CreateEllipseByCenter_Example.png ) 
*Ellipse (weiß) mit interner Geometrie (dunkelgelb)*



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung). {{Version/de|1.0}}
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung). {{Version/de|1.0}}

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateEllipseByCenter.svg" width=16px> [Ellipse um Mittelpunkt erstellen](Sketcher_CreateEllipseByCenter/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreateEllipseByCenter.svg" width=16px> Ellipse um Mittelpunkt erstellen** auswählen.
    -   Das Tastaturkürzel **G** dann **E** dann **E**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Der Abschnitt **Ellipsenparameter** ({{Version/de|1.0}}) wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.
4.  Wahlweise die **M**-Taste drücken oder einen Eintrag in der Ausklappliste **Modus** im Abschnitt **Ellipsenparameter** auswählen, um den Werkzeugmodus zu wechseln:
    -   <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:16px;"> **Mitte**:
        1.  Den Mittelpunkt der Ellipse auswählen; oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
        2.  Einen Endpunkt einer der Achsen der Ellipse auswählen; dies legt auch einen der Radien fest; oder mit Dim-OVP: diesen Radius und/oder den Winkel der Achse eingeben.
        3.  Einen Punkt auswählen, um den anderen Radius der Ellipse festzulegen; oder mit Dim-OVP: diesen Radius eingeben.
    -   <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:16px;"> **Achsen-Endpunkte**: {{Version/de|1.0}}
        1.  Die Endpunkte einer der Achsen der Ellipse auswählen; dies legt auch einen der Radien fest; oder mit Pos-OVP: ihre X- und/oder Y-Koordinaten eingeben. Für diese Punkte werden keine Randbedingungen hinzugefügt.
        2.  Einen Punkt auswählen, um den anderen Radius der Ellipse festzulegen; oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben. Für diese Punkt wird keine Randbedingung hinzugefügt.
5.  Die Ellipse wird erstellt inklusive der internen Geometrie (Hauptachse, Nebenachse und zwei Fokus-Punkte) und mögliche auf Pos-OVP und Dim-OVP basierende Randbedingungen hinzugefügt.
6.  Läuft das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md):
    1.  Wahlweise weitere Ellipsen erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Die Elemente der internen Geometrie können gelöscht werden. Sie können jederzeit mit [Sketcher RestoreInterna/delInterneAusrichtungsgeometrieWiederherstellen](Sketcher_RestoreInternalAlignmentGeometry.md) wiederhergestellt werden.
-   Einmal erstellt, sind Haupt- und Nebenachse einer Ellipse fest zugeordnet und können nicht durch Ändern der Längen getauscht werden. Dies ist eine Folge der Parametrisierung des Gleichungslösers und des gleichen strengen Verhaltens von [OpenCASCADE](OpenCASCADE/de.md). Ein Ellipsenbogen muss gedreht werden, um die Achsen zu tauschen.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/de
