---
 GuiCommand:
   Name: Arch AxisSystem
   Name/de: Arch Achsensystem
   MenuLocation: Anmerkung , Achsensystem
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_Axis/de, Arch_Grid/de
---

# Arch AxisSystem/de



## Beschreibung

Das Werkzeug [Achsensystem](Arch_AxisSystem/de.md) ermöglicht zwei oder drei [Achsensystem](Arch_Axis/de.md)-Objekte zu kombinieren.

Dies ist nützlich, um die Schnittpunkte zwischen den verschiedenen Achsen festzulegen. Arch Objekte können dann dieses System verwenden, um ihre Form an den verschiedenen Schnittpunkten zu duplizieren.

<img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;"> 
*Drei [Arch Achsen](Arch_Axis/de.md)-Objekte zu einem [Arch Achsensystem](Arch_AxisSystem/de.md) zusammengefasst. Ein [Arch Struktur](Arch_Structure/de.md)-Objekt verwendet dieses System als seine {{PropertyData/de|Achsen*, um seine Form an jedem Schnittpunkt zu duplizieren.}}



## Anwendung

1.  Wahlweise die [Arch Achsen](Arch_Axis/de.md)-Objekte auswählen, die in dieses System aufgenommen werden sollen.
2.  Die Schaltfläche **<img src="images/Arch_AxisSystem.svg" width=16px> [Achsensystem](Arch_AxisSystem/de.md)** drücken.
3.  Mit der rechten Maustaste auf das neu erstellte Achsensystem Objekt in der Baumansicht klicken, um die in diesem System enthaltenen [Arch Achsen](Arch_Axis/de.md)-Objekte hinzuzufügen/zu bearbeiten.
4.  Eine vorhandene [Arch Achse](Arch_Axis/de.md) auswählen und die Schaltfläche **<img src="images/Arch_Add.svg" width=16px> [Hinzufügen](Arch_Add/de.md)** oder **<img src="images/Arch_Remove.svg" width=16px> [Entfernen](Arch_Remove/de.md)** drücken, um sie zu diesem System hinzuzufügen bzw. zu entfernen.
5.  Die {{PropertyData/de|Achse}} eines beliebigen Arch-Objekts so festlegen, dass es auf dieses System zeigt, damit seine Form auf die Schnittpunkte dieses Systems dupliziert wird.



## Optionen

-   Dasselbe [Arch Achsen](Arch_Axis/de.md)-Objekt kann Teil von mehr als einem System sein.
-   Jedes formbasierte Objekt kann auch als Eigenschaft **Achse** von Arch-Objekten verwendet werden. In diesem Fall wird die Objektform entlang der Knoten des Achsen Objekts dupliziert.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Achsensystem kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus verwendet werden, indem die folgende Funktion verwendet wird: 
```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```

-   Erstellt aus den gegebenen `Achsen` ein `AchsenSystem`-Objekt, das aus einer einzelnen [Arch Achse](Arch_Axis/de.md) besteht oder aus einer Liste von ihnen.

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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch AxisSystem/de
