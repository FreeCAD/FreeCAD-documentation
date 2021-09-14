---
- GuiCommand:/de
   Name:Points Convert
   Name/de:Punkte umwandeln
   MenuLocation:Punkte → In Punkte umwandeln...
   Workbenches:[Punkte](Points_Workbench/de.md)
---

## Beschreibung

Der **Punkte umwandeln** Befehl erzeugt Punktwolken aus Formobjekten oder Netzobjekten.

Ein Formobjekt bezeichnet hier jedes Objekt mit einer **Form** Eigenschaft. Objekte, die mit dem [Part](Part_Workbench/de.md) und [PartDesign](PartDesign_Workbench/de.md) Arbeitsbereich erzeugt wurden, sind Formobjekte. Aber auch Objekte, die mit dem [Skizzierer](Sketcher_Workbench/de.md) und dem [Entwurf](Draft_Workbench/de.md) Arbeitsbereich erstellt wurden.

## Anwendung

1.  Wähle ein oder mehrere Objekte aus.
2.  Wähle die Option **Punkte → On Punkte umwandeln...** aus dem Menü.
3.  Das Dialogfeld **Abstand** wird geöffnet.
4.  Gib den **Maximalabstand** ein. Der Wert muss im Bereich {{Wert|0.05}} - Bereich von {{Wert|10.0}} liegen.
5.  Drücke die Schaltfläche **OK**, um das Dialogfeld zu schließen und den Befehl zu beenden.

## Eigenschaften

Punktwolkenobjekte sind [App GeoFeature](App_GeoFeature/de.md) Objekte mit den folgenden zusätzlichen Eigenschaften. Wähle die Option **Alles anzeigen** im Kontextmenü des [Eigenschaftseditors](Property_editor/de.md), um die ausgeblendeten Eigenschaften anzuzeigen.

### Daten


{{TitleProperty|Strukturierte Punkte}}

-    **Höhe|Integer**: die Anzahl der eindeutigen Y Koordinaten in der Punktwolke. Diese Eigenschaft ist nur für Punktwolken verfügbar, die mit dem Befehl [Punkte strukturieren](Points_Structure/de.md) erstellt wurden.

-    **Breite|Integer**: die Anzahl der eindeutigen X Koordinaten in der Punktwolke. Diese Eigenschaft ist nur für Punktwolken verfügbar, die mit dem Befehl [Punkte strukturieren](Points_Structure/de.md) erstellt wurden.

#### Versteckte Daten 


{{TitleProperty|Base}}

-    **Punkte|PointsKernel**: ein Punkte PunkteKernel, der mit diesem Objekt verknüpft ist.

-    **Normal|NormalList**: eine Liste von Normalen. Diese Eigenschaft ist nur für Punktwolken verfügbar, die mit dem Befehl [Punkte umeandeln](Points_Convert/de.md) aus Netzobjekten oder Formobjekten mit Flächen erstellt wurden.

### Ansicht


{{TitleProperty|Base}}

-    **Point Size|FloatConstraint**: die Größe der Punkte in Pixeln in der [3D Ansicht](3D_view/de.md).





{{Points Tools navi

}} 
