---
- GuiCommand:/de
   Name:TechDraw MoveView
   Name/de:TechDraw AnsichtVerschieben
   MenuLocation:TechDraw → Ansicht verschieben
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.20
   SeeAlso:[TechDraw AnsichtTeilen](TechDraw_ShareView/de.md)
---

# TechDraw MoveView/de

## Beschreibung

Das Werkzeug <img alt="" src=images/TechDraw_MoveView.svg  style="width:24px;"> **TechDraw AnsichtVerschieben** bewegt eine Ansicht mit all ihren abhängigen Inhalten (Balloons, Maße usw.) auf eine andere Seite.

## Anwendung

1.  Optional wählt man eine Ansicht, eine Von-Seite und eine Nach-Seite. Die Seiten müssen in dieser Reihenfolge ausgewählt werden.
2.  Es gibt verschiedene Möglichkeiten das Werkzeug aufzurufen:
    -   Drücken der Schaltfläche **<img src="images/TechDraw_MoveView.svg" width=16px> [Ansicht verschieben](TechDraw_MoveView/de.md)**.
    -   Auswahl des Menüeintrags **TechDraw → <img src="images/TechDraw_MoveView.svg" width=16px> Ansicht verschieben**.
3.  Es öffnet sich ein Dialog, der es erlaubt, eine Ansicht, eine Von-Seite und eine Nach-Seite auszuwählen.
4.  Die Schaltfläche **OK** anklicken.

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug AnsichtVerschieben kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
import TechDrawTools
TechDrawTools.MoveView(viewName, fromPageName, toPageName)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw MoveView/de
