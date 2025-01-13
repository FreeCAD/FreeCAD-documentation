---
 GuiCommand:
   Name: Arch Frame
   Name/de: Arch Rahmen
   MenuLocation: 3D/BIM , Rahmen
   Workbenches: BIM_Workbench/de
   Shortcut: **F** **R**
   SeeAlso: 
---

# Arch Frame/de



## Beschreibung

Das Werkzeug **<img src="images/Arch_Frame.svg" width=16px> [Arch Rahmen](Arch_Frame/de.md)** wird verwendet, um alle Arten von Rahmenobjekten basierend auf einem Profil und einem Layout zu erstellen. Das Profil wird entlang der Kanten des Layouts extrudiert, bei dem es sich um ein beliebiges 2D-Objekt handeln kann, z. B. eine [Skizze](Sketcher_Workbench/de.md) oder ein [Draft-Objekt](Draft_Workbench/de.md). Es ist besonders nützlich, um Geländer oder Rahmenwände zu erstellen. Rahmenobjekte können dann leicht in [Wände](Arch_Wall/de.md) oder [Struktur](Arch_Structure/de.md)-Objekte umgewandelt werden.

<img alt="" src=images/Arch_Frame_example.jpg  style="width:640px;"> 
*Rahmenobjekt erstellt mit dem Werkzeug [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md) aus einer [Draft-Linie](Draft_Line/de.md), unter Verwendung eines [Draft-Kreises](Draft_Circle/de.md) als Profil*



## Anwendung

1.  Ein Layout- und ein Profilobjekt erstellen, beispielsweise mit dem Arbeitsbereich [Draft](Draft_Workbench/de.md) oder dem Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md).
2.  Zuerst das Layoutobjekt auswählen und danach mit gedrückter **Strg**-Taste das Profilobjekt.
3.  Die Schaltfläche **<img src="images/Arch_Frame.svg" width=16px> [Rahmen](Arch_Frame/de.md)** drücken oder das Tastaturkürzel **F** dann **R**.



## Optionen

-   Frames teilen die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch-Komponenten](Arch_Component/de.md)
-   Das Rahmenobjekt kann in einem bestimmten Abstand vom Layoutobjekt platziert werden, indem seine Versatz Eigenschaft eingestellt wird.
-   Das Profil wird an der Basis jeder Kante des Layoutobjekts kopiert und dann entlang dieser Kante extrudiert. Du kannst mit den Eigenschaften Ausrichten und Drehen steuern, wie das Profil an der Basis jeder Kante platziert wird.



## Eigenschaften



### Daten


{{TitleProperty|Component}}

-    {{PropertyData/de|Base|Link}}: Das Layout auf dem dieser Rahmen basiert.

Für die anderen Eigenschaften in dieser Gruppe siehe [Arch Komponente](Arch_Component/de#Eigenschaften.md).


{{TitleProperty|Frame}}

-    {{PropertyData/de|Align|Bool}}: Legt fest, ob das Profil gedreht werden muss, damit seine Normale zu der jeweiligen Kante ausgerichtet wird.

-    {{PropertyData/de|Base Point|Integer}}: Bei Null startender Index, der den Kreuzungspunkt von Pfad und Profil indiziert:

    -   
        {{Value|0}}
        
        : Die **Basis** der Positionierung, **Placement**, des Profils. Dieser Punkt wird auch im Falle eines ungültigen Indexes verwendet.

    -   
        {{Value|1}}
        
        : Der Mittelpunkt der ersten Kante des Profils.

    -   
        {{Value|2}}
        
        : Der Endpunkt der ersten Kante des Profils.

    -   
        {{Value|3}}
        
        : Der Mittelpunkt der zweiten Kante des Profils.

    -   
        {{Value|4}}
        
        : Der Endpunkt der zweiten Kante des Profils.

    -   \...

    -   
        {{Value|n*2-1}}
        
        : Der Mittelpunkt der n-ten Kante des Profils.

    -   
        {{Value|n*2}}
        
        : Der Endpunkt der n-ten Kante des Profils.

-    {{PropertyData/de|Edges|Enumeration}}: Die Art der Kanten, die berücksichtigt werden sollen. Die Optionen sind:

    -   
        {{Value|All edges}}
        
        : Alle Kanten.

    -   
        {{Value|Vertical edges}}
        
        : Vertikale Kanten.

    -   
        {{Value|Horizontal edges}}
        
        : Horizontale Kanten.

    -   
        {{Value|Bottom horizontal edges}}
        
        : Basiert auf der globalen Z-Koordinate des Schwerpunktes der Kante.

    -   
        {{Value|Top horizontal edges}}
        
        : Wie vorher.

-    {{PropertyData/de|Fuse|Bool}}: Wenn auf true gesetzt, werden überlappende Festkörper vereinigt.

-    {{PropertyData/de|Offset|VectorDistance}}: Ein optionaler Abstand zwischen Layout-Objekt und Frame-Objekt (Rahmen).

-    {{PropertyData/de|Profile|Link}}: Das Profil, auf dem dieser Rahmen (frame) basiert.

-    {{PropertyData/de|Profile Placement|Placement}}: Eine optionale zusätzliche Positionierung, die dem Profil hinzugefügt wird, bevor es extrudiert wird. Es wird nur die **Rotation** der Eigenschaft **Placement** verwendet. Wird ignoriert, wenn die {{PropertyData/de|Align}} auf `True` gesetzt ist.

-    {{PropertyData/de|Rotation|Angle}}: Die Drehung des Profils um seine Extrusionsachse.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Rahmen kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit der folgenden Funktion verwendet werden:


```python
Frame = makeFrame(baseobj, profile)
```

-   Erstellt ein `Frame`-Objekt aus den gegebenen Objekten `baseobj` und `profile`.
    -   
        `baseobj`
        
        ist ein beliebiges Objekt, das Linienzüge enthält, wie ein [Draft Linienzug](Draft_Wire/de.md) oder eine [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md), die eine Ansammlung davon enthält.

-    `profile`ist ein extrudierbares 2D-Objekt, das Flächen oder geschlossene Linienzüge enthält.

Beispiel:


```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Frame/de
