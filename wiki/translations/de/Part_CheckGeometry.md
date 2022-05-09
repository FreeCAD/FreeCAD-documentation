---
- GuiCommand   */de
   Name   *Part CheckGeometry‏‎
   Name/de   *Part GeometriePrüfen
   MenuLocation   *Formteil → Geometrie überprüfen
   Workbenches   *[Part](Part_Workbench/de.md)
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
2.  Rufe das Werkzeug auf, durch entweder   *
    -   Klicke auf die **<img src="images/Part_CheckGeometry.svg" width=16px>** Schaltfläche, die in der Werkzeugleiste des Teil Arbeitsbereichs verfügbar ist.
    -   Verwenden des **Part → <img src="images/Part_CheckGeometry.svg" width=16px> Geometrie prüfen** Eintrags im oberen Menü.


</div>


<div class="mw-translate-fuzzy">

Ergebnisse werden im [Aufgabenpaneel](Task_panel/de.md) aufgeführt.


</div>

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 


<div class="mw-translate-fuzzy">

Die Funktion PrüfeGeometrie prüft, ob die [Randdarstellung](https   *//en.wikipedia.org/wiki/Boundary_representation) korrekt ist. (BRep oder B-rep) des Modells ist gültig. Zusätzlich zu dieser BRep Prüfung ist es möglich, eine zusätzliche BOP Prüfung (BOP= Boolesche OPerationen) durchzuführen.


</div>

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md). <small>(v0.19)</small> 

## Shape Content 

In addition to detecting potential geometry errors, this tool shows a range of properties regarding the selected object   *

-   Checked object
-   Shape type
-   Number of geometric entities   * vertices, edges, wires, faces, shells, solids, compsolids, compounds, total shapes
-   Geometric and mass properties   *
    -   Area
    -   Volume
    -   Mass
    -   Length
    -   Center of mass
    -   Orientation
    -   Symmetry axis
    -   Symmetry point
    -   Moments
    -   First axis of inertia
    -   Second axis of inertia
    -   Third axis of inertia
    -   Radius of gyration
    -   Global placement

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be checked using this tool. For [App Links](App_Link.md) the shape of the linked object is checked. For [App Part](App_Part.md) containers the visible objects within are checked as compounds. <small>(v0.20)</small> 
-   FreeCAD has no methods to automatically repair geometry. If faults are detected the steps involved to create the model need to be examined and fixed manually.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/de
