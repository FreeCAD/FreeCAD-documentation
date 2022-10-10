---
- GuiCommand   *
   Name   *TechDraw StackTop
   MenuLocation   *TechDraw → Stacking → Move view to top of stack
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   Shortcut   *
   Version   *1.0
   SeeAlso   *[TechDraw StackBottom](TechDraw_StackBottom/de.md), [TechDraw StackUp](TechDraw_StackUp/de.md), [TechDraw StackDown](TechDraw_StackDown/de.md).
---

# TechDraw StackTop/de

## Beschreibung

Das <img alt="" src=images/TechDraw_StackTop.svg  style="width   *24px;"> **TechDraw StackTop** Werkzeug bewegt Ansichten an die Oberseite des Stapels. Die Stapel Reihenfolge bestimmt die Tiefe der Sichtbarkeit von Ansichten auf einer Seite.

## Verwendung

1.  Wähle eine oder mehrere Ansichten auf der [Page](TechDraw_PageDefault.md) oder in der [Tree view](Tree_view.md). Für dieses Werkzeug, und [TechDraw StackBottom](TechDraw_StackBottom.md), ist die Reihenfolge der Auswahl wichtig.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen   *
    -   Wähle das **<img src="images/TechDraw_StackTop.svg" width=16px> [Move view to top of stack](TechDraw_StackTop.md)** Symbol.
    -   Wähle die **TechDraw → Stacking → <img src="images/TechDraw_StackTop.svg" width=16px> Move view to top of stack** Option aus dem Menü.
3.  Die **Stack Order** der Ansichten wird geändert.

## Skripten


**Siehe auch   ***

[TechDraw API](TechDraw_API.md) und [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Die Stapel Reihenfolge kann in Skripts durch Ändern der {{Incode|StackOrder}} Eigenschaft eines {{Incode|ViewObject}} erfolgen.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw StackTop/de
