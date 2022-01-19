---
- GuiCommand:/de
   Name:Arch Frame
   Name/de:Arch Rahmen
   MenuLocation:Arch → Rahmen
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**F** **R**
   SeeAlso:[Arch Wand](Arch_Wall/de.md), [Arch Struktur](Arch_Structure/de.md)
---

# Arch Frame/de

## Beschreibung

Das **<img src="images/Arch_Frame.svg" width=16px> [Arch Rahmen](Arch_Frame/de.md)**-Werkzeug wird verwendet, um alle Arten von Rahmenobjekten basierend auf einem Profil und einem Layout zu erstellen. Das Profil wird entlang der Kanten des Layouts extrudiert, bei dem es sich um ein beliebiges 2D-Objekt handeln kann, z. B. ein [Skizze](Sketcher_Workbench/de.md) oder ein [Entwurfsobjekt](Draft_Workbench/de.md). Es ist besonders nützlich, um Geländer oder Rahmenwände zu erstellen. Rahmenobjekte können dann leicht in [Wände](Arch_Wall/de.md) oder [Struktur](Arch_Structure/de.md)-Objekte umgewandelt werden.

<img alt="" src=images/Arch_Frame_example.jpg  style="width:640px;"> 
*Rahmenobjekt erstellt aus einem [Entwurf orthogonales Feld](Draft_OrthoArray/de.md) aus einer [Entwurf Linie](Draft_Line/de.md), unter Verwendung eines [Kreises](Draft_Circle/de.md) als Profil*

## Anwendung

1.  Erstelle ein Layout- und ein Profilobjekt, beispielsweise mit dem [Draft-Arbeitsbereich](Draft_Workbench/de.md) oder dem [Skizzen-Arbeitsbereich](Sketcher_Workbench/de.md).
2.  Wähle zuerst das Layoutobjekt, mit gedrückter **Strg**-Taste wähle das Profilobjekt.
3.  Drücke die **<img src="images/Arch_Frame.svg" width=16px> [Rahmen](Arch_Frame/de.md)**-Schaltfläche oder drücke die Tasten **F**, dann **R**.

## Optionen

-   Frames teilen die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch-Komponenten](Arch_Component/de.md)
-   Das Rahmenobjekt kann in einem bestimmten Abstand vom Layoutobjekt platziert werden, indem seine Versatz Eigenschaft eingestellt wird.
-   Das Profil wird an der Basis jeder Kante des Layoutobjekts kopiert und dann entlang dieser Kante extrudiert. Du kannst mit den Eigenschaften Ausrichten und Drehen steuern, wie das Profil an der Basis jeder Kante platziert wird.

## Eigenschaften

-    {{PropertyData/de|Basis}}: Das Layout, auf dem dieser Rahmen basiert.

-    {{PropertyData/de|Profil}}: Das Profil, auf dem dieser Rahmen basiert.

-    {{PropertyData/de|Ausrichten}}: Legt fest, ob das Profil gedreht werden muss, um die (Hoch)-Achse an jeder Kante auszurichten.

-    {{PropertyData/de|Versatz}}: Ein optionaler Abstand zwischen Layout- und Rahmen-Objekt.

-    {{PropertyData/de|Drehung}}: Die Drehung des Profils um die Extrusionsachse.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>

Das Rahmen Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch Verwendung der folgenden Funktionen verwendet werden: 
```python
Frame = makeFrame(baseobj, profile)
```

-   Erstellt ein `Frame` Objekt aus dem gegebenen `baseobj` und `profile`.
    -   
        `baseobj`
        
        ist ein beliebiges Objekt, das Polygonzüge enthält, wie ein [Entwurf Draht](Draft_Wire/de.md) oder ein [Entwurf orthogonales Feld](Draft_OrthoArray/de.md), die eine Ansammlung davon enthält.

-    `profile`ist ein extrudierbares 2D-Objekt, das Fläche oder geschlossene Linienzüge enthält.

Beispiel: 
```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Frame/de
