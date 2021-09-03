---
- GuiCommand:/de
   Name/de:Punkte strukturieren
   MenuLocation:Punkte → Strukturierte Punktwolke 
   Workbenches:[Punkte](Points_Workbench/de.md)
---

## Beschreibung

Der Befehl **Punkte strukturieren** erzeugt eine strukturierte Punktwolke aus den Punkten einer vorhandenen verstreuten Punktwolke. Eine strukturierte Punktwolke hat den Vorteil, dass die Tesselierung wesentlich einfacher ist.

Der Befehl funktioniert nur für Punktwolken, deren Punkte, aus einer bestimmten Richtung betrachtet, in einem regelmäßigen 2D Gitter organisiert sind. Diese Punktwolken werden typischerweise von [Streifenlicht 3D Scanner](https://en.wikipedia.org/wiki/Structured-light_3D_scanner) erzeugt und haben keine Hinterschneidungen. Für komplexe Objekte müssen Punktwolken aus vielen verschiedenen Blickrichtungen kombiniert werden.

## Anwendung

1.  Der Befehl geht davon aus, dass die Blickrichtung der Punktwolke parallel zur Z Achse des globalen Koordinatensystems ist. Wenn dies nicht der Fall ist: Passe die **Platzierung** des Punktwolkenobjekts entsprechend an.
2.  Wähle das Punktwolkenobjekt.
3.  Wähle die **Punkte → Strukturierte Punktwolke** Option aus dem Menü.

## Eigenschaften

Siehe [Punkte konvertieren](Points_Convert/de.md).





{{Points Tools navi

}} 
