---
 GuiCommand:
   Name: Sketcher Offset
   Name/de: Sketcher Versatzkontur
   MenuLocation: Skizze , Sketcher Werkzeuge , Geometrie versetzen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **T**
   Version: 0.22
   SeeAlso: 
---

# Sketcher Offset/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Offset.svg  style="width:24px;"> [Sketcher Versatzkontur](Sketcher_Offset/de.md) zeichnet eine equidistante Kante (Versatzkontur) um ausgewählte Kanten herum. Sobald das Werkzeug gestartet wird, wechselt der Mauszeiger zu einem weißen Kreuz mit rotem Offset-Symbol:  <img alt="" src=images/Sketcher_Pointer_Create_Offset.svg  style="width:32px;"> .

<img alt="" src=images/Sketcher_OffsetExample.png‎  style="width:400px;"> 
*Equidistante Kanten um eine geschlossene (O) und eine offene (U) Hilfs-Polylinie*



## Anwendung

1.  Eine oder mehrere Kanten auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Offset.svg" width=16px> [Versatzkontur](Sketcher_Offset/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher Werkzeuge → <img src="images/Sketcher_Offset.svg" width=16px> Versatzkontur** auswählen.
    -   Das Tastaturkürzel **Z** then **T**.
3.  Ein Abschnitt **Versatz Parameter** wird oben im [Aufgaben-Bereich](Task_panel/de.md) des Sketchers hinzugefügt.
4.  Wahlweise im Auswahlfeld **Modus** von {{Value|Arc}} (Standardwert) auf {{Value|Intersection}} umstellen.
5.  Wahlweise die Checkbox **Originalgeometrien löschen** aktivieren, um nur den neuen Umriss zu behalten.
6.  Wahlweise die Checkbox **Offset-Randbedingung hinzufügen** aktivieren, um eine maßliche Randbedingung zwischen dem versetzten Umriss und der originalen Geometrie hinzuzufügen.
7.  Den Mauszeiger ziehen und klicken oder einen Abstandswert eingeben, um den Versatz festzulegen und den Befehl abzuschließen. Dies entfernt auch den Abschnitt **Versatz Parameter** aus dem Aufgaben-Bereich.

Wurde **Offset-Randbedingung hinzufügen** aktiviert, kann der Abstand durch Ändern der maßlichen Randbedingung angepasst werden.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Offset/de
