---
 GuiCommand:
   Name: Sketcher NewSketch
   Name/de: Sketcher NeueSkizze
   MenuLocation:  Skizze , Skizze erstellen
   Workbenches: Sketcher Workbench/de
   SeeAlso: PartDesign_NewSketch/de,Sketcher_MapSketch/de, Sketcher_ReorientSketch/de
---

# Sketcher NewSketch/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher NeueSkizze](Sketcher_NewSketch/de.md) erstellt eine neue Skizze und öffnet den [Sketcher-Dialog](Sketcher_Dialog/de.md), um sie zu bearbeiten.

Man beachte, dass der Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;">[PartDesign](PartDesign_Workbench/de.md) seinen eigenen Befehl [NeueSkizze](PartDesign_NewSketch/de.md) besitzt. Bei der Arbeit an einem [PartDesign-Körper](PartDesign_Body/de.md) sollte dafür jenes Werkzeug eingesetzt werden.



## Anwendung

1.  Wenn die Skizze an vorhandene Geometrie [befestigt](Part_EditAttachment/de.md) werden soll: Ein Objekt mit einer Form, eine oder mehrere Knoten, Kanten und/oder Flächen und/oder eine Ebene auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_NewSketch.svg" width=16px> [Skizze erstellen](Sketcher_NewSketch/de.md)** drücken.
    -   Den Menüeintrag **Skizze → <img src="images/Sketcher_NewSketch.svg" width=16px> Skizze erstellen** auswählen.
3.  Wenn Geometrie ausgewählt wurde:
    1.  Der Dialog **Befestigungsmodus der Skizze** wird geöffnet.
    2.  Eine [ Befestigungsmethode](Part_EditAttachment/de#Befestigungsverfahren.md) in der Ausklappliste auswählen. Oder **Nicht befestigen** auswählen, um die Auswahl zu ignorieren.
    3.  Die Schaltfläche **OK** drücken.
4.  Ist keine Auswahl vorhanden oder wurde im vorherigen Schritt **Nicht befestigen** ausgewählt:
    1.  Der Dialog **Orientatierung Wählen** wird geöffnet.
    2.  Die Ebene für die Ausrichtung auswählen. Die Ebene bezieht sich auf das lokale Koordinatensystem im dem sich die Skizze befindet:
        -   Wenn die Checkbox **Umgekehrte Richtung** nicht aktiviert ist:
            -   Draufsicht: **XY-Ebene**
            -   Vorderansicht: **XZ-Ebene**
            -   Ansicht von Rechts: **YZ-Ebene**
        -   Wenn die Checkbox **Umgekehrte Richtung** aktiviert ist:
            -   Untersicht: **XY-Ebene**
            -   Rückansicht: **XZ-Ebene**
            -   Ansicht von Links: **YZ-Ebene**
    3.  Wahlweise den Wert von **Versatz** anpassen. Der Versatz wird entlang der X-, Y- oder Z-Achse des lokalen Koordinatensystems gemessen.
    4.  Die Schaltfläche **OK** drücken.
5.  Eine Skizze wird erstellt.
6.  Die Skizze wird in den Bearbeitungsmodus versetzt und der [Sketcher-Dialog](Sketcher_Dialog/de.md) geöffnet.
7.  Zum Beenden des Bearbeitungsmodus siehe <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:16px;"> [Sketcher SkizzeVerlassen](Sketcher_LeaveSketch/de.md).



## Hinweise

-   Vorhandene Skizzen können mit [Sketcher SkizzeZuordnen](Sketcher_MapSketch/de.md) an verschiedene Objekte befestigt werden oder mit [Sketcher SkizzeAnordnen](Sketcher_ReorientSketch/de.md) abgetrennt und neu ausgerichtet werden.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher NewSketch/de
