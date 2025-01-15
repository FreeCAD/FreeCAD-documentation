---
 GuiCommand:
   Name: Sketcher Rotate
   Name/de: Sketcher Schwenken
   MenuLocation: Skizze , Sketcher-Werkzeuge , Polar transform
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **P**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Rotate/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Rotate.svg  style="width:24px;"> [Sketcher Schwenken](Sketcher_Rotate/de.md) versetzt ausgewählte elemente oder erstellt wahlweise Kopien und verteilt sie gleichmäßig über einen Schwenkwinkel.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung).
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung).

1.  Eine oder mehrere Kanten und/oder [Punktobjekte](Sketcher_CreatePoint/de.md) auswählen. Randbedingungen, die ausschließlich zu den ausgewählten Elementen gehören, außer [HorizontalFestlegen](Sketcher_ConstrainHorizontal/de.md) und [VerticalFestlegen](Sketcher_ConstrainVertical/de.md), werden auch verarbeitet. Werden die originalen Elemente verschwenkt, werden alle anderen Randbedingungen, die mit den Elementen verknüpft sind, werden gelöscht.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Rotate.svg" width=16px> [Polar transform](Sketcher_Rotate/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_Rotate.svg" width=16px> Polar transform** auswählen.
    -   Ein Rechtsklick in der [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_Rotate.svg" width=16px> Polar transform** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **Z** then **P**.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Der Abschnitt **Parameter der Drehung** wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog/de.md) eingefügt.
5.  Wahlweise die \"Anzahl der Kopien\" ändern (ist die Anzahl Null, werden die originalen Elemente verschwenkt):
    -   Eine Anzahl eingeben.
    -   Die **U**-Taste drücken, un die Anzahl zu erhöhen.
    -   Die **J** -Taste drücken, un die Anzahl zu verringern.
6.  Wahlweise die CheckBox **Randbedingung Gleichheit festlegen** aktivieren, um maßliche Randbingungen von diesem Vorgang auszunehmen und stattdessen jeweils eine Randbedingung [GleichheitFestlegen](Sketcher_ConstrainEqual/de.md) zwischen den originalen Objekten und deren Kopien einzusetzen.
7.  Den Schwenkmittelpunkt auswählen. Oder mit Pos-OVP: seine X- und/oder Y-Koordinate eingeben.
8.  Einen Punkt auswählen, um den Startwinkel festzulegen. Oder mit Dim-OVP: Den Wert des Winkels eingeben.
9.  Einen Punkt auswählen, um den Schwenkwinkel festzulegen. Oder mit Dim-OVP: Den Wert des Winkels eingeben.
10. Die originalen Elemente werden verschwenkt oder es werden verschwenkte Kopien erstellt. Es werden keine auf Pos-OVP oder Dim-OVP basierenden Randbedingungen hinzugefügt.



## Hinweise

-   Es kann ratsam sein, [Sketcher AchsenausrichtungenEntfernen](Sketcher_RemoveAxesAlignment/de.md) anzuwenden, bevor dieses Werkzeug eingesetzt wird.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Rotate/de
