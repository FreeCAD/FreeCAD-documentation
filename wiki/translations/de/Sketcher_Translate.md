---
 GuiCommand:
   Name: Sketcher Translate
   Name/de: Sketcher Translate
   MenuLocation: Skizze , Sketcher-Werkzeuge , Linear anordnen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Translate/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Translate.svg  style="width:24px;"> [Sketcher LinearAnordnen](Sketcher_Translate.md) versetzt ausgewählte elemente oder erstellt wahlweise Kopien und verteilt sie gleichmäßig entlang einer oder zweier Richtungen.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung).
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung).



### Geometrie versetzen 

1.  Eine oder mehrere Kanten und/oder [Punktobjekte](Sketcher_CreatePoint/de.md) auswählen. Randbedingungen, die ausschließlich zu den ausgewählten Elementen gehören, werden auch verarbeitet. Alle anderen Randbedingungen, die mit den Elementen verknüpft sind, werden gelöscht.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Translate.svg" width=16px> [Linear anordnen](Sketcher_Translate/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_Translate.svg" width=16px> Linear anordnen** auswählen.
    -   Ein Rechtsklick in der [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_Translate.svg" width=16px> Linear anordnen** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **W**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Der Abschnitt **Parameter der Translation** wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.
5.  Den Startpunkt des Verschiebevektors auswählen. Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
6.  Den Endpunkt des Verschiebevektors auswählen. Oder mit Dim-OVP: die Länge und/oder den Winkel des Vektors eingeben. Der Winkel bezieht sich auf die X-Achse der Skizze.
7.  Die Elemente werden versetzt. Keine auf Pos-OVP oder Dim-OVP basierenden Randbedingungen werden hinzugefügt.



### Geometrie kopieren 

1.  Eine oder mehrere Kanten und/oder [Punktobjekte](Sketcher_CreatePoint/de.md) auswählen. Randbedingungen, die ausschließlich zu den ausgewählten Randbedingungen gehören, werden auch verarbeitet.
2.  Das Werkzeug aufrufen, wie oben beschrieben.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Der Abschnitt **Parameter der linearen Anordnung** wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.
5.  Wahlweise die **Anzahl der Kopien** entlang des ersten Vektors ändern:
    -   Eine Anzahl eingeben.
    -   Die **U**-Taste drücken, um die Anzahl zu erhöhen.
    -   Die **J**-Taste drücken, um die Anzahl zu verringern.
6.  Wahlweise die Anzahl der **Reihen** in Richtung des zweiten Vektors ändern:
    -   Eine Anzahl eingeben.
    -   Die **R**-Taste drücken, um die Anzahl zu erhöhen.
    -   Die **F**-Taste drücken, um die Anzahl zu verringern.
7.  Wahlweise die CheckBox **Randbedingung Gleichheit festlegen** aktivieren, um maßliche Randbingungen von diesem Vorgang auszunehmen und stattdessen jeweils eine Randbedingung <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [GleichheitFestlegen](Sketcher_ConstrainEqual/de.md) zwischen den originalen Objekten und deren Kopien einzusetzen.
8.  Den Startpunkt des ersten Vektors auswählen. Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben. Dieser Vektor bestimmt den Abstand zwischen den Kopien.
9.  Den Endpunkt des ersten Vektors auswählen. Oder mit Dim-OVP: die Länge und/oder den Winkel des Vektors eingeben. Der Winkel bezieht sich auf die X-Achse der Skizze.
10. Gibt es zwei oder mehr Reihen: den Endpunkt des zweiten Vektors auswählen. Oder mit Dim-OVP: die Länge und/oder den Winkel des Vektors eingeben. Der Winkel bezieht sich auf die X-Achse der Skizze. Dieser Vektor bestimmt den Abstand zwischen den Reihen.
11. Die Elemente werden Kopiert. Keine auf Pos-OVP oder Dim-OVP basierenden Randbedingungen werden hinzugefügt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Translate/de
