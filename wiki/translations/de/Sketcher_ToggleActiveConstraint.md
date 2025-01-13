---
 GuiCommand:
   Name: Sketcher ToggleActiveConstraint
   Name/de: Sketcher AktiveRandbedingungUmschalten
   Workbenches: Sketcher_Workbench/de
   MenuLocation: Skizze , Skizzen-Randbedingungen , Randbedingungen aktivieren/deaktivieren
   Shortcut: **K** **Z**
   Version: 0.19
   SeeAlso: Sketcher_ToggleDrivingConstraint/de
---

# Sketcher ToggleActiveConstraint/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:24px;"> [Sketcher AktiveRandbedingungUmschalten](Sketcher_ToggleActiveConstraint/de.md) aktiviert bzw. deaktiviert ausgewählte Randbedingungen. Das Deaktivieren von Randbedingungen erlaubt es andere Anordnungen der Geometrien auszuprobieren, ohne dass Randbedingungen gelöscht werden müssen.

Das Werkzeug ist dem Werkzeug [Sketcher FestlegendeRandbedingungUmschalten](Sketcher_ToggleDrivingConstraint/de.md), kann aber im Gegensatz zu dem auch für geometrische Randbedingungen eingesetzt werden; und die Werte deaktivierter maßlicher Randbedingungen bleiben erhalten.



## Anwendung

1.  Eine oder mehrere Randbedingungen auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> [Randbedingungen aktivieren/deaktivieren](Sketcher_ToggleActiveConstraint/de.md)** drücken.

    -   Den Menüeintrag **Skizze → Skizzen-Randbedingungen → <img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Randbedingungen aktivieren/deaktivieren** auswählen.

    -   
        {{Version/de|1.0}}
        
        : Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Randbedingungen aktivieren/deaktivieren** im Kontextmenü auswählen.

    -   Ein Rechtsklick in den Abschnitt Randbedingungen des [Sketcher-Dialogs](Sketcher_Dialog/de.md) und die Menüoption **Aktivieren** bzw. **Deaktivieren** im Kontextmenü auswählen. Die angebotene Option hängt vom Status der Randbedingung unter dem Mauszeiger ab.

    -   Das Tastaturkürzel **K** dann **Z**.
3.  Aktive ausgewählte Randbedingungen werden deaktiviert und grau ([Standardfarbe](Sketcher_Preferences/de#Darstellung.md)) umgefärbt, während deaktivierte ausgewählte Randbedingungen aktiviert werden und wieder rot (Standardfarbe) dargestellt werden.



## Beispiel

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:400px;"> 
*Eine Vollständig bestimmte Skizze‎.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:400px;"> 
*Einer der Randbedingungen zum Festlegen der Winkel wurde deaktiviert; die Skizze ist jetzt nicht mehr vollständig bestimmt.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:400px;"> 
*Die nicht vollständig bestimmte Geometrie kann bewegt werden. Die deaktivierte Randbedingung ist noch immer vorhanden und kannreaktiviert werden, um zu der vollständig bestimmten Skizze zurückzukehren.*



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Der aktive Status einer Randbedingung kann in [Makros](macros/de.md) und von der [Python-Konsole](Python_console/de.md) aus gesteuert werden. 
```python
SketchObject.toggleActive(index)
```

Man verwendet die Methode `toggleActive` eines vorhandenen [Sketcher SketchObjects](Sketcher_SketchObject/de.md) und den `index` der Randbedingung, um sie zu aktivieren bzw. zu deaktivieren. Der Index beginnt bei `0` und geht bis `N-1`, wobei `N` die Gesamtanzahl der Randbedingungen ist.

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
