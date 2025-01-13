---
 GuiCommand:
   Name: Arch RemoveShape
   Name/de: Arch FormEntfernen
   MenuLocation: Utils , Form entfernen
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_SplitMesh/de, Arch_MeshToShape/de
---

# Arch RemoveShape/de



## Beschreibung

Das Werkzeug **Arch FormEntfernen** versucht sich daran, die innere kubische Form einer [Arch-Wand](Arch_Wall/de.md) oder einer [Arch-Struktur](Arch_Structure/de.md) zu entfernen sowie ihre Eigenschaften anzupassen und sie damit vollständig zu parametrisieren. Dieses Werkzeug funktioniert nur, wenn die zugrundeliegende Form kubisch ist (genau 6 Flächen, alle Ecken haben nur rechte Winkel).



## Anwendung

1.  Eine [Arch-Wand](Arch_Wall/de.md) oder eine [Arch-Struktur](Arch_Structure/de.md) auswählen.
2.  Den Menüeintrag **Utils → <img src="images/Arch_RemoveShape.svg" width=16px> Form entfernen** auswählen.



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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch RemoveShape/de
