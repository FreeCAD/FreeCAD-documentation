---
- GuiCommand:/de
   Name:Sketcher ToggleActiveConstraint
   Name/de:Skizzierer UmschaltenAktiveBeschränkung
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   MenuLocation:Skizze → Skizzierer Beschränkungen → Umschalten Aktivieren/Deaktivieren Beschränkung
   SeeAlso:[Sketcher Umschalten treibende Beschränkungen](Sketcher_ToggleDrivingConstraint.md)
   Version:0.19
---

# Sketcher ToggleActiveConstraint/de


</div>

## Beschreibung


**[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px">[UmschaltenAktiveBeschränkung](Sketcher_ToggleActiveConstraint/de.md)**

ermöglicht es dir, eine bereits platzierte Randbedingung zu aktivieren und zu deaktivieren. Dadurch kannst du die Beschränkung im Hintergrund halten, aber vorübergehend eine andere Anordnung der vorhandenen Geometrie testen.

Das **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Umschalten Treibende Beschränkung](Sketcher_ToggleDrivingConstraint/de.md)** Werkzeug ist insofern ähnlich, als es die Wirkung der Beschränkung deaktiviert; mit diesem Werkzeug behält die Beschränkung jedoch nicht ihren alten Wert. Andererseits kann mit **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [UmschaltenAktive Beschränkung](Sketcher_ToggleActiveConstraint/de.md)** kannst du die alte Beschränkung sofort wieder aktivieren.

## Anwendung

1.  Wähle eine bereits platzierte Beschränkung und drücke dann **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [UmschaltenAktiveBeschränkung](Sketcher_ToggleActiveConstraint/de.md)**.
2.  Alternativ kannst du in der [Aufgabenkonsole](task_panel/de.md) zum Abschnitt {{MenuCommand/de|Beschränkungen}} gehen, die Beschränkung wählen, dann das Kontextmenü öffnen (Rechtsklick) und {{MenuCommand/de|Deaktivieren}} wählen.
3.  Um die Beschränkung wieder zu aktivieren, wähle sie aus und drücke **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [UmschaltenAktiveBeschränkung](Sketcher_ToggleActiveConstraint/de.md)** nochmals.

## Beispiele

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:" height="350px;"> 
*Vollständig beschränkte Skizze‎.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:" height="350px;"> <img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:" height="350px;"> 
*Links: Deaktivierte Beschränkung; die Skizze ist nicht mehr vollständig beschränkt. Rechts: die nicht gebundene Geometrie kann verschoben werden; die ältere Abhängigkeit ist immer noch verfügbar und kann reaktiviert werden, um zur vollständig gebundenen Skizze zurückzukehren.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_task_panel.png  style="width:" height="350px;"> 
*Aufgabenbereich mit der deaktivierten Beschränkung.*

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Der aktive Status einer Beschränkung kann in [Makros](macros/de.md) und aus der [Python Konsole](Python_console/de.md) gesteuert werden. 
```python
SketchObject.toggleActive(index)
```

Verwende die `toggleActive` Methode einer vorhandenen [Skizzierer SkizzenObjekt](Sketcher_SketchObject/de.md) und den `index` der Beschränkung, um sie zu aktivieren oder zu deaktivieren. Der Index beginnt bei `0` bis hin zu `N-1`, wobei `N` die Gesamtanzahl der Beschränkungen ist.

Beispiel: 
```python
import FreeCAD as App

sketch = App.ActiveDocument.Sketch
sketch.toggleActive(3)
```


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleActiveConstraint/de
