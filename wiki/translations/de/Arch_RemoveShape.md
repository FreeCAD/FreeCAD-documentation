---
- GuiCommand:
   Name: Arch RemoveShape
   Name/de: Arch FormEntfernen
   Workbenches: [Arch-Arbeitsbereich](Arch_Workbench/de.md)
   MenuLocation: Architektur - Dienstprogramme - Entferne Form
   SeeAlso: [Arch NetzAufteilen](Arch_SplitMesh/de.md), [Arch NetzZuForm](Arch_MeshToShape/de.md)
---

# Arch RemoveShape/de



## Beschreibung

Dieses Werkzeug versucht sich daran, die innere kubische Form einer **<img src="images/Arch_Wall.svg" width=16px> [Wand](Arch_Wall/de.md)** oder einer **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)** zu entfernen sowie ihre Eigenschaften anzupassen und sie damit vollständig zu parametrisieren. Dieses Werkzeug funktioniert nur, wenn die zugrundeliegende Form kubisch ist (genau 6 Flächen, alle Ecken haben nur rechte Winkel).



## Anwendung

1.  Eine **<img src="images/Arch_Wall.svg" width=16px> [Wand](Arch_Wall/de.md)** oder eine **<img src="images/Arch_Structure.svg" width=16px>[Struktur](Arch_Structure/de.md)** auswählen
2.  Die Schaltfläche **<img src="images/Arch_RemoveShape.svg" width=16px> [FormEntfernen](Arch_RemoveShape/de.md)** drücken oder den Menüeintrag **Arch** → **Dientsprogramme** → **<img src="images/Arch_RemoveShape.svg" width=16px> [FormEntfernen](Arch_RemoveShape/de.md)** auswählen.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch folgende Funktion verwendet werden: 
```python
removeShape(objs, mark=True)
```

-   Nimmt eine Liste von Arch Objekten (`objs`) gebaut auf einem quaderförmigen Formteil und entfernt die inneren Formen, wobei Lnge, Breite und Höhe als Eigenschaften des Arch-Objekts beibehalten werden.
    -   
        `objs`
        
        ist ein einzelnes Objekt, [Wand](Arch_Wall/de.md) oder [Arch Bauelement](Arch_Structure/de.md) oder eine daraus bestehende Liste.
-   Falls `mark` den Wert `True` hat, werden Objekte rot markiert, wenn sie von dieser Funktion nicht bearbeitet werden können.


```python
import FreeCAD, Draft, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(Box)
FreeCAD.ActiveDocument.recompute()

Arch.removeShape(Structure)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/de
