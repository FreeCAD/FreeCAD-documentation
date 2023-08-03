---
 GuiCommand:
   Name: Arch CutPlane
   Name/de: Arch SchneideEbene
   MenuLocation: Arch , Ebene Schneiden
   Workbenches: Arch_Workbench/de
   SeeAlso: Arch_CutLine/de, Arch_Remove/de
---

# Arch CutPlane/de

## Beschreibung

Das Schnittebenen Werkzeug ermöglicht dir ein Arch Objekt entsprechend einer Ebene schneiden:

-   Du kannst ein Arch Objekt mit der ausgewählten Fläche schneiden, normal oder gegenüber der Flächenebene.
-   Dies fügt dem Arch Objekt eine Subtraktionskomponente SchneideVolumen hinzu.

<img alt="" src=images/Arch_CutPlane_example.jpg  style="width:640px;">



*Links: Vor der Anwendung des Werkzeugs CutPlane. Mitte: resultierende Wand nach dem Schnitt. Rechts: ein weiteres optionales Ergebnis*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle das zu beschneidende Objekt, dann die Fläche (die Fläche muss die letzte sein, die du ausgewählt hast, und muss in der [3D Ansicht](3D_view/de.md) ausgewählt werden).
2.  Drücke die **<img src="images/Arch_CutPlane.svg" width=16px>[Schneide Ebene](Arch_CutPlane/de.md)**Schaltfläche.
3.  Wähle , ob das Objekt **hinter**\' der normalen Fläche oder **\'vor**\' der normalen Fläche geschnitten wird.
4.  Klicke die **OK** Taste


</div>


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Das SchneideEbene Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden:


</div>


```python
cutObj = cutComponentwithPlane(archObject, cutPlane, sideFace)
```

-   Erstellt ein `cutObj`-Objekt aus dem gegebenen `archObject`, das von `cutPlane` geschnitten wird, das eine Fläche eines anderen Objekts ist.
    -   
        `archObject`
        
        sollte ein `SelectionObject` sein, das aus `FreeCADGui.Selection.SelectionEx()[0]` stammt.

    -   
        `cutPlane`
        
        sollte ein `FaceObject` sein, das aus `FreeCADGui.Selection.SelectionEx()[0].SubObjects[0]` stammt.

-    `sideFace`gibt an, auf welcher Seite des `FaceObject` ein Volumenkörpers erzeugt werden soll; dieser Volumenkörper wird dann vom `archObject` subtrahiert (subtracted). Falls `sideFace` den Wert `0` hat, wird ein Volumenkörper hinter der Fläche erzeugt, anderenfalls vor der Fläche.

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


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CutPlane/de
