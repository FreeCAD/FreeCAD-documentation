---
- GuiCommand   */de
   Name   *TechDraw ShareView
   Name/de   *TechDraw AnsichtTeilen
   MenuLocation   *TechDraw → Ansicht teilen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   Version   *0.20
   SeeAlso   *[TechDraw AnsichtVerschieben](TechDraw_MoveView/de.md)
---

# TechDraw ShareView/de

## Beschreibung

Das Werkzeug <img alt="" src=images/TechDraw_ShareView.svg  style="width   *24px;"> **TechDraw AnsichtTeilen** macht eine Ansicht mit all ihren abhängigen Inhalten (Balloons, Maße usw.) auf einer zweiten Seite sichtbar.

## Anwendung

1.  Optional wählt man eine Ansicht, eine Von-Seite und eine Nach-Seite. Die Seiten müssen in dieser Reihenfolge ausgewählt werden.
2.  Es gibt verschiedene Möglichkeiten das Werkzeug aufzurufen   *
    -   Drücken der Schaltfläche **<img src="images/TechDraw_ShareView.svg" width=16px> [Ansicht teilen](TechDraw_ShareView/de.md)**.
    -   Auswahl des Menüeintrags **TechDraw → <img src="images/TechDraw_ShareView.svg" width=16px> Ansicht teilen**.
3.  Es öffnet sich ein Dialog, der es erlaubt, eine Ansicht, eine Von-Seite und eine Nach-Seite auszuwählen.
4.  Die Schaltfläche **OK** anklicken.

## Hinweise

Es gibt nur ein View-Objekt nach der Verteilungsoperation. Sämtliche Änderungen, die an der Ansicht erfolgen, werden auf beiden Seiten angezeigt. Wenn die Ansicht von einer Seite gelöscht wird, wird sie auch von der anderen Seite gelöscht.

## Skripten


**Siehe auch   ***

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Ansicht teilen kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus genutzt werden durch Verwendung der folgenden Funktionen   *


```python
import TechDrawTools
#MoveView with a True parameter in the last position performs a copy
TechDrawTools.MoveView(viewName, fromPageName, toPageName, True)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShareView/de
