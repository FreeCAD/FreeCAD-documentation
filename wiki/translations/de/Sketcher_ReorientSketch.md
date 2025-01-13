---
 GuiCommand:
   Name: Sketcher ReorientSketch
   Name/de: Sketcher SkizzeAusrichten
   MenuLocation: Skizze , Skizze neu ausrichten...
   Workbenches: Sketcher_Workbench/de, PartDesign_Workbench/de
   SeeAlso: Sketcher_MapSketch/de, Sketcher_NewSketch/de
---

# Sketcher ReorientSketch/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:24px;"> [Sketcher SkizzeAusrichten](Sketcher_ReorientSketch/de.md) verlegt eine Skizze auf eine der Hauptebenen, wahlweise mit einem Abstand. Es kann auch zum Ablösen der Skizze eingesetzt werden.



## Anwendung

1.  Eine Skizze auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ReorientSketch.svg" width=16px> [Skizze neu ausrichten...](Sketcher_ReorientSketch/de.md)** drücken (steht im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md)) nicht zur Verfügung.
    -   Den Menüeintrag **Skizze → <img src="images/Sketcher_ReorientSketch.svg" width=16px> Skizze neu ausrichten...** auswählen.
3.  Wenn die Skizze angeheftet ist:
    1.  Ein Dialogfenster wird geöffnet.
    2.  Die Schaltfläche **Ja** drücken, um die Skizze abzulösen.
4.  Das Dialogfenster **Orientierung wählen** wird geöffnet.
5.  Wahlweise die Schaltfläche **Abbrechen** drücken, um die Skizze nur abzulösen und das Werkzeug zu beenden.
6.  Die Ebene für die Ausrichtung auswählen. Die Ebene bezieht sich auf das lokale Koordinatensystem, in dem sich die Skizze befindet:
    -   Wenn die CheckBox **Richtung umkehren** nicht aktiviert ist:
        -   Draufsicht: **XY-Ebene**
        -   Vorderansicht: **XZ-Ebene**
        -   Ansicht von rechts: **YZ-Ebene**
    -   Wenn die CheckBox **Richtung umkehren** aktiviert ist:
        -   Untersicht: **XY-Ebene**
        -   Rückansicht: **XZ-Ebene**
        -   Ansicht von links: **YZ-Ebene**
7.  Wahlweise den Wert für den **Versatz** anpassen. Der Abstand wird entlang der Z-, Y- oder X-Achse des lokalen Koordinatensystems gemessen.
8.  Die Schaltfläche **OK** drücken.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ReorientSketch/de
