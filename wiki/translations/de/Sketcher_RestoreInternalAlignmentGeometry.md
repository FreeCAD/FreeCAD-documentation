---
 GuiCommand:
   Name: Sketcher RestoreInternalAlignmentGeometry
   Name/de: Sketcher InterneAusrichtungsgeometrieWiederherstellen
   MenuLocation: Skizze , Sketcher visuell , Interne Geometrie anzeigen / ausblenden
   Workbenches: Sketcher_Workbench/de
   Shortcut: **Z** **I**
   SeeAlso: 
---

# Sketcher RestoreInternalAlignmentGeometry/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:24px;"> [Sketcher InterneAusrichtungsgeometrieWiederherstellen](Sketcher_RestoreInternalAlignmentGeometry/de.md) löscht die internen Geometrien von Elementen oder erstellt fehlende interne Geometrien neu. Das Werkzeug löscht keine internen Geometrien, denen Randbedingungen zugeordnet sind.



## Anwendung

1.  Ein oder mehrere Skizzenelemente auswählen, die interne Geometrie verwenden ([Ellipse](Sketcher_CreateEllipseByCenter/de.md), [Ellipsenbogen](Sketcher_CreateArcOfEllipse/de.md), [Hyperbelbogen](Sketcher_CreateArcOfHyperbola/de.md), [Parabelbogen](Sketcher_CreateArcOfParabola/de.md) oder [B-Spline](Sketcher_CreateBSpline/de.md)).
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Interne Geometrie anzeigen / ausblenden](Sketcher_RestoreInternalAlignmentGeometry/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher visuell → [<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> Interne Geometrie anzeigen / ausblenden** auswählen.
    -   Das Tastaturkürzel **Z** dann **I**.
3.  Im Falle von Elementen mit vollständiger interner Geometrie, wird die interne Geometrie gelöscht, andernfalls wird nicht vorhandene Geometrie wiederhergestellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/de
