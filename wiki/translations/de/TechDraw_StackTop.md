---
 GuiCommand:
   Name: TechDraw StackTop
   Name/de: TechDraw StapelOberseite
   MenuLocation: TechDraw , Stacking , Ansicht auf die Stapeloberseite bewegen
   Workbenches: TechDraw_Workbench/de
   Shortcut: 
   Version: 0.21
   SeeAlso: TechDraw_StackBottom/de, TechDraw_StackUp/de, TechDraw_StackDown/de.
---

# TechDraw StackTop/de



## Beschreibung

Das Werkzeug **TechDraw StapelOberseite** bewegt Ansichten auf die Oberseite des Stapels. Die Stapelreihenfolge bestimmt, welche Ansicht auf dem Zeichnungsblatt dargestellt wird (und welche bei Überschneidung verdeckt wird).



## Verwendung

1.  Eine oder mehrere Ansichten auf dem [Zeichnungsblatt](TechDraw_PageDefault/de.md) oder in der [Baumansicht](Tree_view/de.md) auswählen. Für dieses Werkzeug und für [TechDraw StapelUnterseite](TechDraw_StackBottom/de.md), ist die Reihenfolge der Auswahl wichtig.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_StackTop.svg" width=16px> [Stapel Oben](TechDraw_StackTop/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Stacking → <img src="images/TechDraw_StackTop.svg" width=16px> Ansicht auf die Stapeloberseite bewegen** auswählen.
3.  Die {{PropertyView/de|Stack Order}} der Ansichten wird geändert.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Die Stapelreihenfolge kann in Skripten durch Ändern der Eigenschaft {{Incode|StackOrder}} des {{Incode|ViewObject}}s einer Ansicht erfolgen.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw StackTop/de
