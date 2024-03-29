---
 GuiCommand:
   Name: Points Structure
   Name/de: Points Strukturieren
   MenuLocation: Punkte , Strukturierte Punktwolke
   Workbenches: Points_Workbench/de
---

# Points Structure/de



## Beschreibung

Der Befehl **Points Strukturieren** erzeugt eine strukturierte Punktwolke aus den Punkten einer vorhandenen verstreuten Punktwolke. Eine strukturierte Punktwolke hat den Vorteil, dass die Tesselierung wesentlich einfacher ist.

Der Befehl funktioniert nur für Punktwolken, deren Punkte, aus einer bestimmten Richtung betrachtet, in einem regelmäßigen 2D-Gitter organisiert sind. Diese Punktwolken werden typischerweise von [Streifenlicht-3D-Scanner](https://en.wikipedia.org/wiki/Structured-light_3D_scanner) erzeugt und haben keine Hinterschneidungen. Für komplexe Objekte müssen Punktwolken aus vielen verschiedenen Blickrichtungen kombiniert werden.



## Anwendung

1.  Der Befehl geht davon aus, dass die Blickrichtung der Punktwolke parallel zur Z-Achse des globalen Koordinatensystems ist. Wenn dies nicht der Fall ist: Die {{PropertyData/de|Placement}} des Punktwolkenobjekts entsprechend anpassen.
2.  Das Punktwolkenobjekt auswählen.
3.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Points_Structure.svg" width=16px> [Strukturierte Punktwolke](Points_Structure/de.md)** drücken.
    -   Den Menüeintrag **Punkte → <img src="images/Points_Structure.svg" width=16px> Strukturierte Punktwolke** auswählen.



## Eigenschaften

Siehe [Points Konvertieren](Points_Convert/de.md).





{{Points Tools navi

}}



---
⏵ [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Structure/de
