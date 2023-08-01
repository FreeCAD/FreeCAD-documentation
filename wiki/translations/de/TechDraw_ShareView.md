---
- GuiCommand:
   Name: TechDraw ShareView
   Name/de: TechDraw AnsichtTeilen
   MenuLocation: TechDraw - TechDraw Ansichten - Ansicht teilen
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   Version: 0.20
   SeeAlso: [TechDraw AnsichtVerschieben](TechDraw_MoveView/de.md)
---

# TechDraw ShareView/de



## Beschreibung

Das Werkzeug **TechDraw AnsichtTeilen** macht eine Ansicht mit all ihren abhängigen Inhalten (Hinweisfelder, Maße usw.) auf einer zweiten Seite sichtbar.



## Anwendung

1.  Wahlweise eine Ansicht, eine Von-Seite und eine Nach-Seite auswählen. Die Seiten müssen in dieser Reihenfolge ausgewählt werden.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ShareView.svg" width=16px> [Ansicht teilen](TechDraw_ShareView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_ShareView.svg" width=16px> Ansicht teilen** auswählen.
3.  Es öffnet sich ein Dialog, der es erlaubt, eine Ansicht, eine Von-Seite und eine Nach-Seite auszuwählen.
4.  Die Schaltfläche **OK** drücken.



## Hinweise

Es gibt nur ein View-Objekt nach der Verteilungsoperation. Sämtliche Änderungen, die an der Ansicht erfolgen, werden auf beiden Seiten angezeigt. Wenn die Ansicht von einer Seite gelöscht wird, wird sie auch von der anderen Seite gelöscht.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Ansicht teilen kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus genutzt werden durch Verwendung der folgenden Funktionen:


```python
import TechDrawTools
#MoveView with a True parameter in the last position performs a copy
TechDrawTools.MoveView(viewName, fromPageName, toPageName, True)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShareView/de
