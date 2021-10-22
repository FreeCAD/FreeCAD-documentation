---
- GuiCommand:/de
   Name:Std Placement
   Name/de : Std Positionierung
   MenuLocation:Bearbeiten → Platzierung...
   Workbenches:Alle
   SeeAlso:[Std Ausrichtung](Std_Alignment/de.md), [Platzierung](Placement/de.md)
---

# Std Placement/de

## Beschreibung

Der **Std Platzierung** Befehl zeigt die Platzierung [ Aufgabenkonsole](Task_panel/de.md) für ein ausgewähltes Objekt an.

![](images/Std_Placement_taskpanel.png ) 
*Die Positionierungsaufgabenkonsole*

## Verwendung

1.  Wähle ein einzelnes Objekt aus, das eine **Platzierung**seigenschaft im [Eigenschaftseditor](Property_editor/de.md) hat.
2.  Wähle die **Bearbeiten → Platzierung...** Option aus dem Menü.
3.  Ändere einen oder mehrere der Translations- und Rotationsparameter.
4.  Mache eins der folgenden:
    -   Drücke die **OK** Schaltfläche, um die Änderungen zu übernehmen und die Aufgabenkonsole zu schließen.
    -   Drücke die **Apply** Schaltfläche, um die Änderungen zu übernehmen, aber lasse die Aufgabenkonsole für weitere Änderungen offen.
5.  Drücke die **esc** oder die **Abbruch** Taste um die Aufgabe abzubrechen. Dies wird alle Änderungen, die nicht übernommen wurden, zurücksetzen.

Der Dialog kann auch durch Klicken auf die Ellipsentaste **...** gestartet werden, die im [Eigenschafteneditor](Property_editor/de.md) erscheint, wenn man auf die **Platzierung** Eigenschaft klickt.

## Hinweise

-   Für weitere Informationen zu den Positionierungsparametern siehe die [Platzierungs](Placement/de.md) Seite und und das [Flugzeug](Aeroplane/de.md) Tutorium.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Siehe das [Python Skipterstellung Tutorium](Python_scripting_tutorial/de#Vektoren_und_Platzierungen.md).

Eine Positionierung wird intern durch eine Matrix bestimmt; in vielen Fällen ist es einfacher, dies durch zwei Komponenten darzustellen, einem `Base`-Punkt (Vektor) und einem `Rotation`-Wert. `Rotation` selbst hat verschiedene Entsprechungen. Es kann vollständig durch den Wert einer \"[quaternion](https://en.wikipedia.org/wiki/Quaternion)\" `(xi + yj + zk + w)` bestimmt werden. Es kann aber auch durch eine Rotations `Axis` (Einheitsvektor) und eine Rotations `Angle` (Bogenmaß) bestimmt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Cylinder", "Cylinder")

print(obj.Placement)
# Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
print(obj.Placement.Base)
# Vector (0.0, 0.0, 0.0)
print(obj.Placement.Rotation)
# Rotation (0.0, 0.0, 0.0, 1.0)

print(obj.Placement.Rotation.Angle)
# 0.0
print(obj.Placement.Rotation.Axis)
# Vector (0.0, 0.0, 1.0)
print(obj.Placement.Rotation.Q)
# (0.0, 0.0, 0.0, 1.0)
```

Verschiebe den Basispunkt des Objekts und drehe dann das Objekt um 45 Grad um die x-Achse. 
```python
import math

obj.Placement.Base = App.Vector(5, 3, 1)
obj.Placement.Rotation.Axis = App.Vector(1, 0, 0)
obj.Placement.Rotation.Angle = math.radians(45)

print(obj.Placement)
# Placement [Pos=(5,3,1), Yaw-Pitch-Roll=(0,0,45)]
print(obj.Placement.Rotation.Q)
# (0.3826834323650898, 0.0, 0.0, 0.9238795325112867)
print(obj.Placement.Matrix)
# Matrix ((1,0,0,5),(0,0.707107,-0.707107,3),(0,0.707107,0.707107,1),(0,0,0,1))
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Placement/de
