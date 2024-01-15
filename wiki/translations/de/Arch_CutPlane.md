---
 GuiCommand:
   Name: Arch CutPlane
   Name/de: Arch Schnittebene
   MenuLocation: Arch , Mit einer Ebene bechneiden
   Workbenches: Arch_Workbench/de
---

# Arch CutPlane/de



## Beschreibung

Das Werkzeug **Arch Schnittebene** beschneidet einen Arch-Festkörper (Arch-Objekt), wie z.B. eine [Arch Wand](Arch_Wall/de.md) oder [Arch Struktur](Arch_Structure.md) mit einer ebenen Fläche.

<img alt="" src=images/Arch_CutPlane_example.jpg  style="width:400px;"> 
*Links: Vor der Anwendung des Werkzeugs Schnittebene. Mitte: Resultierende Wand nach dem Beschnitt. Rechts: Ein weiteres optionales Ergebnis*



## Anwendung

1.  Soll die Schnittebene von einer geraden Kante abgeleitet werden ({{Version/de|0.22}}), kann wahlweise die [Arbeitsebene](Draft_SelectPlane/de.md) ausgerichtet werden:
    -   Die ausgewählte Kante kann (darf) nicht parallel zur Normale der Arbeitsebene sein.
    -   Die erstellte Schnittebene steht senkrecht auf der Arbeitsebene.

2.  Das zu schneidende Objekt auswählen.

3.  Eine der folgende Möglichkeiten auswählen:
    -   Ein Objekt mit einer einzelnen ebenen Fläche auswählen. {{Version/de|0.22}}
    -   Eine ebene Fläche in der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Ein Objekt mit einer einzelnen geraden Kante auswählen. {{Version/de|0.22}}
    -   Eine gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen. {{Version/de|0.22}}

4.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Arch_CutPlane.svg" width=16px> [Mit einer Ebene beschneiden](Arch_CutPlane.md)** drücken.
    -   Den Menüeintrag **Arch → <img src="images/Arch_CutPlane.svg" width=16px> Mit einer Ebene beschneiden** auswählen.

5.  
    **Hinter**oder **Vorne** auswählen, um die Seite der Schnittfläche zu bestimmen, auf der Material entfernt werden soll.

6.  Die Schaltfläche **OK** drücken.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Schnittebene kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden:


```python
cutObj = cutComponentwithPlane(archObject, cutPlane, sideFace)
```

-   Erstellt ein `cutObj`-Objekt aus dem gegebenen `archObject`, das mit `cutPlane` beschnitten wird, das eine Fläche eines anderen Objekts ist.
    -   
        `archObject`
        
        sollte ein `SelectionObject` sein, das aus `FreeCADGui.Selection.SelectionEx()[0]` stammt.

    -   
        `cutPlane`
        
        sollte ein `FaceObject` sein, das aus `FreeCADGui.Selection.SelectionEx()[0].SubObjects[0]` stammt.

-    `sideFace`gibt an, auf welcher Seite des `FaceObject` ein Volumenkörper erzeugt werden soll; dieser Volumenkörper wird dann von dem `archObject` abgezogen (subtracted). Falls `sideFace` den Wert `0` hat, wird ein Volumenkörper hinter der Fläche erzeugt, anderenfalls vor der Fläche.

Beispiel:


```python
import FreeCAD, FreeCADGui, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select the Wall
main_object = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall2
selection = FreeCADGui.Selection.getSelectionEx()[0]
cut_face = selection.SubObjects[0]

cutObj = Arch.cutComponentwithPlane(main_object, cut_face, 0)
FreeCAD.ActiveDocument.recompute()

Wall3 = Draft.move(Wall, FreeCAD.Vector(-4000, 0, 0), copy=True)
Wall4 = Draft.move(Wall2, FreeCAD.Vector(-4000, 0, 0), copy=True)
FreeCAD.ActiveDocument.recompute()

# Select the Wall3
main_object2 = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall4
selection2 = FreeCADGui.Selection.getSelectionEx()[0]
cut_face2 = selection2.SubObjects[0]

cutObj2 = Arch.cutComponentwithPlane(main_object2, cut_face2, 1)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CutPlane/de
