---
 GuiCommand:
   Name: Sketcher CreateArc
   Name/de: Sketcher KreisbogenErstellen
   MenuLocation: Skizze , Skizzengeometrien , Kreisbogen um Mittelpunkt erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **A**
   SeeAlso: Sketcher_CreateCircle/de
---

# Sketcher CreateArc/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreateArc.svg  style="width:24px;"> [KreisbogenErstellen](Sketcher_CreateArc/de.md): Erstellt einen Kreisbogen durch Festlegen seines Mittelpunktes und seiner Endpunkte. {{Version/de|1.0}}: Oder durch Festlegen seiner Endpunkte und eines Punktes im Verlauf des Bogens.

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:400px;"> 
*Ein im Mittelpunkt-Modus erstellter Kreisbogen mit den Randbedingungen, die automatisch hinzugefügt werden, wenn alle In-Ansicht-Parametern eingegeben wurden*



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung). {{Version/de|1.0}}
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung). {{Version/de|1.0}}

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateArc.svg" width=16px> [Kreisbogen um Mittelpunkt erstellen](Sketcher_CreateArc/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_CreateArc.svg" width=16px> Kreisbogen um Mittelpunkt erstellen** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_CreateArc.svg" width=16px> Kreisbogen um Mittelpunkt erstellen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** dann **A**.
2.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
3.  Der Abschnitt **Bogenparameter** ({{Version/de|1.0}}) wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.
4.  Wahlweise die **M**-Taste drücken oder einen Eintrag in der Ausklappliste **Modus** im Abschnitt **Bogenparameter** auswählen, um den Werkzeugmodus zu wechseln:
    -   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:16px;"> **Mitte**:
        1.  Den Mittelpunkt des Kreisbogens auswählen; oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
        2.  Den Startpunkt des Bogens auswählen; dies legt auch den Radius des Kreisbogens fest; oder mit Dim-OVP: den Radius und/oder den Startwinkel des Bogens eingeben. Der Winkel bezieht sich auf die X-Achse der Skizze. Für diesen Winkel wird keine Randbedingung hinzugefügt.
        3.  Den Endpunkt des Bogens auswählen; oder mit Dim-OVP: den überstrichenen Winkel des Bogens eingeben.
    -   <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:16px;"> **3 Punkte auf Kreisbogen**. {{Version/de|1.0}}
        1.  Start- und Endpunkt des Kreisbogens auswählen; oder mit Pos-OVP: ihre X- und/oder Y-Koordinaten eingeben.
        2.  Einen weiteren Punkt auswählen, um den Radius festzulegen; oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben. Für diesen Punkt werden keine Randbedingungen hinzugefügt.
5.  Der Kreisbogen wird erstellt und mögliche auf Pos-OVP und Dim-OVP basierende Randbedingungen hinzugefügt.
6.  Läuft das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md):
    1.  Wahlweise weitere Kreisbögen erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zum Erstellen von Geometrien oder Randbedingungen aufrufen.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArc/de
