---
- GuiCommand:
   Name: Sketcher CreateFillet
   Name/de: Sketcher VerrundungErstellen
   MenuLocation: Sketch - Skizzengeometrie - Verrundung erstellen
   Workbenches: [Sketcher](Sketcher_Workbench/de.md)
   Shortcut: **G** **F** **F**
   SeeAlso: [Sketcher PunktVerrundungErstellen](Sketcher_CreatePointFillet/de.md)
---

# Sketcher CreateFillet/de



## Beschreibung

Dieses Werkzeug erzeugt eine Verrundung zwischen zwei Linien.

Beim Starten des Werkzeugs werden Auswahlen gelöscht und der Mauszeiger ändert sich in ein weißes Kreuz mit einem roten Verrundungssymbol. Es bleibt aktiv, so dass du mehrere Verrundungen vornehmen kannst.

![](images/SketcherCreateFilletExample.png‎ )



## Anwendung

1.  Die Schaltfläche **[<img src=images/Sketcher_CreateFillet.svg style="width:16px"> [Verrundung](Sketcher_CreateFillet/de.md)** drücken.

2.  Einen Knoten, der zwei nicht parallele Linien verbindet auswählen oder zwei Linien, die nicht parallel verlaufen auswählen.

3.  Wird ein Knoten ausgewählt, wird er Verrundungsradius von der Länge der kürzeren Linie abgeleitet. Werden zwei Linien ausgewählt, legt der Abstand des zuerst ausgewählten Punktes zum (virtuellen) Schnittpunkt der Linien den Verrundungsradius fest.

4.  
    **Esc**oder ein Klick mit der rechten Maustaste bricht die Funktion ab oder beendet sie.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/de
