---
 GuiCommand:
   Name: TechDraw MoveView
   Name/de: TechDraw AnsichtVerschieben
   MenuLocation: TechDraw , TechDraw Ansichten , Ansicht verschieben
   Workbenches: TechDraw_Workbench/de
   Version: 0.20
   SeeAlso: TechDraw_ShareView/de
---

# TechDraw MoveView/de



## Beschreibung

Das Werkzeug **TechDraw AnsichtVerschieben** bewegt eine Ansicht mit all ihren abhängigen Inhalten (Hinweisfelder, Maße usw.) auf eine andere Seite.



## Anwendung

1.  Wahlweise eine Ansicht, eine Von-Seite und eine Nach-Seite auswählen. Die Seiten müssen in dieser Reihenfolge ausgewählt werden.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_MoveView.svg" width=16px> [Ansicht verschieben](TechDraw_MoveView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_MoveView.svg" width=16px> Ansicht verschieben** auswählen.
3.  Es öffnet sich ein Dialog, der es erlaubt, eine Ansicht, eine Von-Seite und eine Nach-Seite auszuwählen.
4.  Die Schaltfläche **OK** drücken.



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
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw MoveView/de
