---
- GuiCommand:/de
   Name:Arch RemoveShape
   Name/de:Arch FormEntfernen
   Workbenches:[Arch-Arbeitsbereich](Arch_Workbench/de.md)
   MenuLocation:Architektur → Dienstprogramme → Entferne Form
   SeeAlso:[Arch NetzAufteilen](Arch_SplitMesh/de.md), [Arch NetzZuForm](Arch_MeshToShape/de.md)
---

# Arch RemoveShape/de

## Beschreibung

Dieses Werkzeug versucht, beim entfernen der inneren kubische Form eines **<img src="images/Arch_Wall.svg" width=16px> [Arch Wand](Arch_Wall/de.md)** oder **<img src="images/Arch_Structure.svg" width=16px> [Arch Struktur](Arch_Structure/de.md)**, und einstellen seiner Eigenschaften, es vollständig parametrisch zu machen. Dieses Werkzeug funktioniert nur, wenn die zugrunde liegende Form kubisch ist (genau 6 Flächen, alle Ecken haben nur rechte Winkel).

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle eine **<img src="images/Arch_Wall.svg" width=16px> [Wand](Arch_Wall/de.md)
** oder ein **<img src="images/Arch_Structure.svg" width=16px>[Arch Struktur](Arch_Structure/de.md)**
2.  Drücke die **<img src="images/Arch_RemoveShape.svg" width=16px>** Schaltfläche oder verwende **Arch** → **Dientsprogramme** → **<img src="images/Arch_RemoveShape.svg" width=16px> [Entferne Form](Arch_RemoveShape/de.md)** aus dem Hauptmenü.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Dieses Werkzeug kann in [Makros](macros/de.md) ebenso wie aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion angesprochen werden:


</div>


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


<div class="mw-translate-fuzzy">





</div>


{{Arch_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/de
