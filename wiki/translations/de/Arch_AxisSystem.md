---
- GuiCommand:/de
   Name:Arch AxisSystem
   Name/de:Arch AchsenSystem
   Icon:Arch Axis System.svg
   MenuLocation:Arch → Achsen System
   Workbenches:[Arch](Arch_Workbench/de.md)
   SeeAlso:[Arch Achse](Arch_Axis/de.md), [Arch Gitter](Arch_Grid/de.md)
---

## Beschreibung

Das [AchsenSystem](Arch_AxisSystem/de.md) Werkzeug ermöglicht dir zwei oder drei [AchsenSystem](Arch_Axis/de.md) Objekte zu kombinieren.

Dies ist nützlich, um die Schnittpunkte zwischen den verschiedenen Achsen zu definieren.Arch Objekte können dann dieses System verwenden, um ihre Form an den verschiedenen Schnittpunkten zu duplizieren.

<img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;"> 
*Drei [Arch Achsen](Arch_Axis/de.md) Objekte zu einem [Arch AchsenSystem](Arch_AxisSystem/de.md) zusammengefasst. Ein [Arch Struktur](Arch_Structure/de.md) Objekt verwendet dieses System als seine **Achsen* Eigenschaft, um seine Form an jedem Schnittpunkt zu duplizieren.**

## Anwendung

1.  Wähle wahlweise die [ArchAchse](Arch_Axis/de.md) Objekte aus, die du in dieses System aufnehmen möchtest.
2.  Drücke die **<img src="images/Arch_Axis_System.svg" width=16px> [Arch AchsenSystem](Arch_AxisSystem/de.md)** Schaltfläche.
3.  Rechtsklicke auf das neu erstellte Achsensystem Objekt in der Baumansicht, um die in diesem System enthaltenen [ Arch Achsen](Arch_Axis/de.md) Objekte hinzuzufügen/zu bearbeiten.
4.  Wähle eine vorhandene [ Arch Achse](Arch_Axis/de.md) und drücke **<img src="images/Arch_Add.svg" width=16px> [Arch hinzufügen](Arch_Add/de.md)** or **<img src="images/Arch_Remove.svg" width=16px> [Arch entfernene](Arch_Remove/de.md)** Schaltflächen um es zu diesem System hinzuzufügen oder zu entfernen.
5.  Lege die **Achse** Eigenschaft eines beliebigen Arch Objekts so fest, dass es auf dieses System zeigt, damit seine Form auf die Schnittpunkte dieses Systems dupliziert wird.

## Optionen

-   Ein gleiches [Arch Achsen](Arch_Axis/de.md) Objekt kann Teil von mehr als einem System sein.
-   Jedes formbasierte Objekt kann auch als **Achse** Eigenschaft von Arch Objekten verwendet werden. In diesem Fall wird die Objektform entlang der Knoten des Achsen Objekts dupliziert.

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Versatzwerkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus verwendet werden, indem die folgende Funktion verwendet wird: 
```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```

-   Erstellt ein `AchsenSystem` Objekt aus den gegebenen `Achsen`, das eine einzelne [Arch Achsen](Arch_Axis/de.md) oder eine Liste von ihnen ist.

Beispiel: 
```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()

AxisSystem = Arch.makeAxisSystem([Axes, Axes2])

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = AxisSystem
FreeCAD.ActiveDocument.recompute()
```





 
