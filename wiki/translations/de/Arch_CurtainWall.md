---
- GuiCommand:/de
   Name:Arch CurtainWall
   Name/de:Architektur Vorhangfassade
   MenuLocation:Arch → Vorhandene Fassade
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**C** **W**
   Version:0.19
   SeeAlso:[Architektur Wand](Arch_Wall/de.md), [Architektur Gitter](Arch_Grid/de.md)
---

## Beschreibung

Dieses Werkzeug erstellt eine [Vorhangfassade](https://de.wikipedia.org/wiki/Vorhangfassade), indem es eine Grundfläche in viereckige Flächen unterteilt, dann vertikale Pfosten an den vertikalen Kanten und horizontale Pfosten an den horizontalen Kanten erzeugt und die Zwischenräume zwischen den Pfosten mit Paneelen füllt.

<img alt="" src=images/Arch_CurtainWall_example.png  style="width:780px;">

Vorhangwände können aus jeder Art von bestehendem Objekt erstellt werden, wobei alle Flächen des Objekts unterteilt werden. Es funktioniert daher am besten, wenn es mit einem Objekt verwendet wird, das nur eine Fläche hat. Typischerweise würdest du zuerst eine Fläche erstellen, vorzugsweise mit genau 4 Kanten, die den Bereich repräsentiert, den du mit einer Vorhangwand füllen möchtest, und dann das Werkzeug anwenden.

Vorhangwände können auch aus einem linearen Objekt, wie z. B. einer Linie, einem Bogen oder einer Polylinie, aufgebaut werden, wie das normale Werkzeug [Wand](Arch_Wall/de.md).

Flächen, die eine doppelte Krümmung haben, oder Flächen mit mehr als 4 Kanten funktionieren auch, aber das Ergebnis ist weniger vorhersehbar.

Die Flächen werden in viereckige Facetten aufgeteilt. Wenn die 4 Punkte der Facette koplanar sind, wird eine quadratische Facette erzeugt. Wenn nicht, wird sie in zwei Dreiecke geteilt und ein diagonaler Pfosten wird hinzugefügt.

Falls Sie eine unregelmäßige Unterteilung benötigen, ist es auch möglich, ein eigenes unterteiltes Objekt zu bauen, z. B. mit [Arch Grid/de](Arch_Grid/de.md), und die vertikale und horizontale Unterteilung der Vorhangfassade auf 1 zu setzen.

Du kannst das Vorhangwand Werkzeug auch ohne ein ausgewähltes Objekt verwenden. In diesem Fall kannst du eine Grundlinie zeichnen, die dann vertikal extrudiert wird, um die Fläche zu bilden, auf der die Vorhangwand aufgebaut wird.

## Anwendung

### Zeichnung einer Vorhangwand von Grund auf 

1.  Stelle sicher, dass nichts ausgewählt ist
2.  Drücke die Schaltfläche **<img src="images/Arch_CurtainWall.svg" width=16px> [[Arch CurtainWall/de]]
** oder drücke die Tasten **C** und dann **W**
3.  Klicke auf einen ersten Punkt in der 3D Ansicht oder gib eine Koordinate ein
4.  Klicke auf einen zweiten Punkt in der 3D Ansicht oder gib eine Koordinate ein
5.  Stelle die benötigten Eigenschaften ein

### Erstellung einer Vorhangwand aus einem gewählten Objekt 

1.  Wähle ein oder mehrere Basisgeometrieobjekte (Entwurfsobjekt, Skizze, usw.).
2.  Drücke die **<img src="images/Arch_CurtainWall.svg" width=16px> [[Arch CurtainWall/de]]**, oder drücke die Tasten **C** und dann **W**.
3.  Stelle die benötigten Eigenschaften ein.

## Optionen

-   Curtain walls share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   Curtain wall mullions can be made from an automatic square profile (set their **Mullion Size** properties) or from a custom profile (set their **Mullion Profile** property). The mullions can be centered over each edge, or placed relatively to the (0,0,0) point by turning off the **Center Profile** property. For example, if you want a profile to be placed slightly behind the panels, you would draw that profile slightly below the (0,0,0) origin point
-   Curtain walls support [Multi-materials](Arch_MultiMaterial.md). Inside the multi-material, the **Frame** layer will be used for the mullions, and the **Glass panel** layer for panels, or **Solid panel** if no Glass panel layer exists in the multi-material.
-   Curtain walls can be based on a linear object such as a line, arc or polyline. In that case, internally, a base surface will be built by extruding the linear object along the direction given by the **Vertical Direction** property, by the length given by the **Height** property.

## Eigenschaften

Vorhangfassaden erben die Eigenschaften von [Arch Komponenten](Arch_Component/de.md) Objekten und habe ebenfalls die folgenden zusätzlichen Eigenschaften:

-    **Vertical Mullion Number**:The number of vertical mullions

-    **Vertical Mullion Alignment**: If the profile of the vertical mullions get aligned with the surface or not

-    **Vertical Sections**: The number of vertical sections of this curtain wall

-    **Vertical Mullion Height**: The height of the vertical mullions profile, if no profile is used

-    **Vertical Mullion Width**: The width of the vertical mullions profile, if no profile is used

-    **Vertical Mullion Profile**: A profile for vertical mullions (disables vertical mullion size)

-    **Horizontal Mullion Number**: The number of horizontal mullions

-    **Horizontal Mullion Alignment**: If the profile of the horizontal mullions gets aligned with the surface or not

-    **Horizontal Sections**: The number of horizontal sections of this curtain wall

-    **Horizontal Mullion Height**: The height of the horizontal mullions profile, if no profile is used

-    **Horizontal Mullion Width**: The width of the horizontal mullions profile, if no profile is used

-    **Horizontal Mullion Profile**: A profile for horizontal mullions (disables horizontal mullion size)

-    **Diagonal Mullion Number**: The number of diagonal mullions

-    **Diagonal Mullion Size**: The size of the diagonal mullions, if any, if no profile is used

-    **Diagonal Mullion Profile**: A profile for diagonal mullions, if any (disables horizontal mullion size)

-    **Panel Number**: The number of panels

-    **Panel Thickness**: The thickness of the panels

-    **Swap Horizontal Vertical**: Swaps horizontal and vertical lines

-    **Refine**: Perform subtractions between components so none overlap

-    **Center Profiles**: Centers the profile over the edges or not

-    **Vertical Direction**: The vertical direction reference to be used by this object to deduce vertical/horizontal directions. Keep it close to the actual vertical direction of your curtain wall

-    **Height**: The height of this curtain wall, in case it is based on a linear object

-    **Host**: The host of this curtain wall. The curtain wall will appear embedded in its host object in the tree view (no other action is performed)

## Making frame walls 

Curtain walls are convenient to use in conjunction with [walls](Arch_Wall.md) to create frame walls (walls where an inner, structural layer is made of frames, usually wooden or metal, instead of an homogeneous material such as concrete of brick).

<img alt="" src=images/Frame_wall_example.png  style="width:780px;">

Die nachfolgend beschriebene Prozedur erstellt eine Wand und eine Vorhangfassade basierend auf der gleichen Basislinie, gibt der Wand dann ein Mehrfachmaterial, das einen leeren Platz lässt, wo die Vorhangfassade platziert wird.

1.  Create a normal [Arch Wall](Arch_Wall.md), either by clicking two points of from an existing linear object
2.  Select the base object of the newly created arch wall
3.  Press the **<img src="images/Arch_CurtainWall.svg" width=16px> [[Arch CurtainWall]]** button, or press the **C** then **W** keys to create a curtain wall from the same baseline as the wall
4.  Make sure both the wall and curtain wall have the same **Height**
5.  Set the number of **horizontal sections** of the curtain wall to zero if you wish only vertical frames
6.  Set the desired **horizontal mullion width** and **horizontal mullion height** (or use a mullion profile)
7.  Prepare two (or more) [materials](Arch_SetMaterial.md), one for the panels, one for the void where the frame will be
8.  Make one [multi-material](Arch_MultiMaterial.md), using one layer of the panel material, one layer of the void material with a negative width value (which will make it not drawn) corresponding to the vertical mullion height of the curtain wall, and another layer of panel material
9.  Attribute the multi-material to the wall
10. Set the **Host** property of the curtain wall to the wall we created in first point

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Vorhangfassaden Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole aus mit folgender Funktion verwendet werden: 
```python
MyCurtainWall = makeCurtainWall(baseobj)
```

Beispiel:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseface = Free.ActiveDocument.addObject('Part::Extrusion','Extrusion')
baseface.Base = baseline
baseface.DirMode = "Normal"
baseface.LengthFwd = 2000
curtainwall = Arch.makeCurtainWall(baseface)
curtainWall.VerticalSections = 6
FreeCAD.ActiveDocument.recompute()
```





 
