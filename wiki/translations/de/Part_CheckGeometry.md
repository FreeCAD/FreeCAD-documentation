---
- GuiCommand:/de
   Name:Part CheckGeometry‏‎
   Name/de:Part GeometriePrüfen
   MenuLocation:Formteil → Geometrie überprüfen
   Workbenches:[Part](Part_Workbench/de.md)
---

# Part CheckGeometry/de

## Beschreibung


<div class="mw-translate-fuzzy">

## Beschreibung 

Das **<img src="images/Part_CheckGeometry.svg" width=16px> [Part GeometriePrüfen](Part_CheckGeometry.md)** Werkzeug führt eine Überprüfung durch und meldet, ob die Geometrie ein gültiger Körper ist.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle ein Teil aus (achte darauf, das gesamte Teil auszuwählen und nicht nur eine Fläche, um auf ein gültiges Volumenmodell zu prüfen)
2.  Rufe das Werkzeug auf, durch entweder:
    -   Klicke auf die **<img src="images/Part_CheckGeometry.svg" width=16px>** Schaltfläche, die in der Werkzeugleiste des Teil Arbeitsbereichs verfügbar ist.
    -   Verwenden des **Part → <img src="images/Part_CheckGeometry.svg" width=16px> Geometrie prüfen** Eintrags im oberen Menü.


</div>


<div class="mw-translate-fuzzy">

Ergebnisse werden im [Aufgabenpaneel](Task_panel/de.md) aufgeführt.


</div>

**Note:** FreeCAD has no automatic repair methods for solids, so you need to look at the steps involved to model this specific geometry and try to fix the error on your own.

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 


<div class="mw-translate-fuzzy">

Die Funktion PrüfeGeometrie prüft, ob die _) des Modells ist gültig. Zusätzlich zu dieser BRep Prüfung ist es möglich, eine zusätzliche BOP Prüfung (BOP= Boolesche OPerationen) durchzuführen.


</div>

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md). <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/de
