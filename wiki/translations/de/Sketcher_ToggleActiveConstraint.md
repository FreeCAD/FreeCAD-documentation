---
 GuiCommand:
   Name: Sketcher ToggleActiveConstraint
   Name/de: Sketcher UmschalterAktiveRandbedingung
   Workbenches: Sketcher_Workbench/de
   MenuLocation: Sketch , Skizzen-Beschränkungen , Einschränkung zwischen festlegend und anzeigend umschalten
   Shortcut: **K** **Z**
   Version: 0.19
   SeeAlso: Sketcher_ToggleDrivingConstraint/de
---

# Sketcher ToggleActiveConstraint/de



## Beschreibung


**[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px">[UmschalterAktiveRandbedingung](Sketcher_ToggleActiveConstraint/de.md)**

ermöglicht es, eine bereits platzierte Randbedingung zu aktivieren und zu deaktivieren. Dadurch kann man die Randbedingung im Hintergrund behalten, aber vorübergehend eine andere Anordnung der vorhandenen Geometrie testen.

Das Werkzeug **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [UmschalterFührendeRandbedingung](Sketcher_ToggleDrivingConstraint/de.md)** ist insofern ähnlich, als dass es die Wirkung der Randbedingung deaktiviert; mit diesem Werkzeug behält die Randbedingung jedoch nicht ihren alten Wert. Andererseits kann mit **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [UmschalterAktiveRandbedingung](Sketcher_ToggleActiveConstraint/de.md)** die alte Randbedingung sofort wieder aktiviert werden.



## Anwendung

1.  Eine bereits platzierte Randbedingung auswählen und dann die Schaltfläche **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Einschränkung zwischen festlegend und anzeigend umschalten](Sketcher_ToggleActiveConstraint/de.md)** drücken.
2.  Alternativ kann man im [Aufgabenbereich](task_panel/de.md) zum Abschnitt **Constraints** gehen, die Randbedingung wählen, dann das Kontextmenü öffnen (Rechtsklick) und **Deaktivieren** wählen.
3.  Um die Randbedingung wieder zu aktivieren, wählt man sie aus und drückt die Schaltfläche **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Einschränkung zwischen festlegend und anzeigend umschalten](Sketcher_ToggleActiveConstraint/de.md)** erneut.



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





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleActiveConstraint/de
