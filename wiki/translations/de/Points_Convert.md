---
- GuiCommand:
   Name: Points Convert
   Name/de: Points umwandeln
   MenuLocation: Punkte - In Punkte umwandeln...
   Workbenches: [Points](Points_Workbench/de.md)
---

# Points Convert/de



## Beschreibung

Der Befehl **Points Umwandeln** erzeugt Punktwolken aus Formobjekten (shape objects) oder Netzobjekten (mesh objects).

Ein Formobjekt bezeichnet hier jedes Objekt mit einer {{PropertyData/de|Shape}}. Objekte, die mit den Arbeitsbereichen [Part](Part_Workbench/de.md) und [PartDesign](PartDesign_Workbench/de.md) erstellt wurden, sind Formobjekte. Aber auch Objekte, die mit den Arbeitsbereichen [Sketcher](Sketcher_Workbench/de.md) und [Draft](Draft_Workbench/de.md) erstellt wurden.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Den Menüeintrag **Punkte → In Punkte umwandeln...** auswählen.
3.  Das Dialogfeld **Abstand** wird geöffnet.
4.  Den **Maximalabstand** eingeben. Der Wert muss im Bereich {{Value|0.05}} - {{Value|10.0}} liegen.
5.  Die Schaltfläche **OK** drücken, um das Dialogfeld zu schließen und den Befehl zu beenden.



## Eigenschaften

Punktwolkenobjekte sind [App GeoFeature](App_GeoFeature/de.md)-Objekte mit den folgenden zusätzlichen Eigenschaften. Die Option **Alles anzeigen** im Kontextmenü des [Eigenschaftseditors](Property_editor/de.md) aktivieren, um die ausgeblendeten Eigenschaften anzuzeigen.



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



---
⏵ [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Convert/de
