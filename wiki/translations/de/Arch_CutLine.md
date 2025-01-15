---
 GuiCommand:
   Name: Arch CutLine
   Name/de: Arch Schnittlinie
   MenuLocation: Arch , Mit einer Linie beschneiden
   Workbenches: Arch_Workbench/de
   SeeAlso: Arch_CutPlane/de
   Version: 0.19
---

# Arch CutLine/de



## Beschreibung

Das Werkzeug **Arch Schnittlinie** beschneidet einen Arch-Festkörper (Arch-Objekt), wie z.B. eine [Arch Wand](Arch_Wall/de.md) oder [Arch Struktur](Arch_Structure/de.md) mit einer geraden Kante. Bassierend auf dieser Kante und der Normale der [Draft-Arbeitebene](Draft_SelectPlane/de.md) wird eine Schnittfläche erstellt.

<img alt="" src=images/Arch_CutLine_example_1.png  style="width:" height="300px;"> <img alt="" src=images/Arch_CutLine_example_2.png  style="width:" height="300px;">



*[Arch-Wand](Arch_Wall/de.md) mit einer Schnittlinie beschnitten. Links: Subtraktiver Quader, der bei der Anwendung des Werkzeugs erscheint. Rechts: Die Wand nach dem Beschnitt.*



## Anwendung

1.  Wenn nötig, die Arbeisebene ausrichten:
    -   Die ausgewählte Kante darf nicht parallel zur Normale der Arbeisebene verlaufen.
    -   Die erstellte Schnittfläche steht senkrecht auf der Arbeisebene.

2.  Das Objekt, das beschnitten werden soll, in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.

3.  Eine gerade Kante auswäheln. Diese muss in der [3D-Ansicht](3D_view/de.md) ausgewählt werden.

4.  Die Schaltfläche **<img src="images/Arch_CutLine.svg" width=16px> [Mit einer Linie beschneiden](Arch_CutLine/de.md)** drücken.

5.  
    **hinter**oder **Vorne** auswählen, um die Seite der Schnittfläche zu bestimmen, auf der Material entfernt werden soll.

6.  Die Schaltfläche **OK** drücken.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).



---
⏵ [documentation index](../README.md) > Arch CutLine/de
