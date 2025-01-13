---
 GuiCommand:
   Name: Arch Rebar
   Name/de: Arch Bewehrung
   MenuLocation: 3D/BIM , Bewehrungswerkzeuge , Benutzerdefinierte Bewehrung
   Workbenches: BIM_Workbench/de, Reinforcement_Workbench/de
   Shortcut: **R** **B**
   SeeAlso: 
---

# Arch Rebar/de



## Beschreibung

Das Werkzeug **Arch Bewehrung** ermöglicht, [Bewehrungsstäbe](https://de.wikipedia.org/wiki/Bewehrungsstahl) (und Bewehrungsbügel) in [Arch Struktur](Arch_Structure/de.md)-Objekten zu positionieren.

Bewehrungen (Rebar-Objekte) basieren auf 2D-Profilen, wie [Draft-Objekte](Draft_Workbench/de.md) und [Skizzen](Sketcher_Workbench/de.md), die auf einer Fläche des Strukturobjekts gezeichnet werden müssen. Nach der Erstellung können die Eigenschaften der Bewehrung angepasst werden, einschließlich der Anzahl und des Durchmessers der Bewehrungsstäbe sowie des Abstands zwischen ihnen und den Flächen des Strukturelements.

<img alt="" src=images/Arch_Rebar_example.jpg  style="width:400px;"> 
*Strukturobjekt mit zwei auf seinen Flächen gezeichneten Skizzen, die dann in zwei Sätze von Bewehrungsobjekten umgewandelt werden*



## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [BIM](BIM_Workbench/de.md) wechseln.
2.  Ein **<img src="images/Arch_Structure.svg" width=16px> [Arch Struktur](Arch_Structure/de.md)**-Element erstellen
3.  Zum Arbeitsbereich <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/de.md) wechseln.
4.  Eine Fläche des Strukturelements auswählen.
5.  Die Schaltfläche **<img src="images/Sketcher_NewSketch.png" width=16px> [Skizze erstellen](Sketcher_NewSketch/de.md)** drücken, um eine neue Skizze auf der ausgewählten Fläche zu erstellen.
6.  Den Verlauf des Bewehrungsstabes skizzieren.
7.  Die Schaltfläche **<img src="images/Sketcher_LeaveSketch.png" width=16px> [Skizze verlassen](Sketcher_LeaveSketch/de.md)** drücken, um die Skizze fertigzustellen.
8.  Zurück zum Arbeitsbereich <img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [BIM](BIM_Workbench/de.md) wechseln.
9.  Die gerade gezeichnete Skizze auswählen.
10. Die Schaltfläche **<img src="images/Arch_Rebar.svg" width=16px> [Benutzerdefinierte Bewehrung](Arch_Rebar/de.md)** drücken oder das Tastaturkürzel **R** dann **B**.
11. Die gewünschten Eigenschaften anpassen (der Bewehrungsstab erscheint möglicherweise nicht sofort, wenn einige der Eigenschaften einen unmöglichen Zustand schaffen; z.B. wenn der Stabdurchmesser 0 ist oder die Abstände größer sind als die Länge des Strukturelements).

Obwohl eine Bewehrung normalerweise in einer Arch-Struktur verwendet wird, kann sie seit FreeCAD v0.19 auch außerhalb eines Host-Objekts erstellt werden. Um eine Bewehrung in einem Objekt zu platzieren, muss einfach nur dessen {{PropertyData/de|Host}} gesetzt werden.



## Optionen

-   Bewehrungen haben die gleichen Eigenschaften und das gleiche Verhalten aller [Arch-Komponenten](Arch_Component/de.md)
-   Der Verrundungswert wird als Vielfaches des Durchmessers ausgedrückt. Wenn ein Stab einen Durchmesser von 5 mm hat, führt ein Verrundungswert von 3 zu einem Radius von 15 mm in den Ecken.
-   Standardwerte für neue Bewehrungsstäbe können in den Arch-Einstellungsdialogen gesetzt werden.
-   Falls ein Richtungsvektor nicht angegeben wurde, werden die Werte für Richtung und Abstand zwischen den Stäben automatisch abhängig vom Strukturobjekt berechnet, indem die normale Ausrichtung der Basisskizze und der Schnittpunkt mit dem Strukturobjekt genommen werden. Wenn Du einen Richtungsvektor angibst, wird die Länge des Vektor ebenfalls berücksichtigt.
-   Der Abstandswert wird aus der aktuellen Anzahl von Stäben berechnet und stellt den Abstand zwischen den Achsen der Stäbe dar. Du musst daher den Stabdurchmesser subtrahieren, um die Größe des freien Raums zwischen den Stäben zu erhalten.



## Eigenschaften

-    {{PropertyData/de|Anzahl}}: Die Anzahl von Stäben.

-    {{PropertyData/de|Durchmesser}}: Der Durchmesser der Stäbe.

-    {{PropertyData/de|Richtung}}: Die Richtung (und Länge), über die die Stäbe verteilt werden müssen. Wenn der Wert (0,0,0) ist, wird die Richtung automatisch abhängig vom Host-Strukturobjekt gesetzt

-    {{PropertyData/de|Versatzbeginn}}: Der Versatzabstand zwischen dem Rand des Strukturobjekts und dem ersten Stab.

-    {{PropertyData/de|Versatzende}}: Der Versatzabstand zwischen dem Rand des Strukturobjekts und dem letzten Stab.

-    {{PropertyData/de|Verrundung}}: Ein Verrundungswert in den Ecken der Stäbe, ausgedrückt als das Vielfache des Durchmessers.

-    {{PropertyData/de|Leerraum}}: Der Abstand zwischen den Achsen jedes Stabs.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Bewehrung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


```python
Rebar = makeRebar(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name="Rebar")
```

-   Erstellt ein Objekt `Rebar` aus dem gegebenen Objekt `baseobj`, das ein [Struktur](Arch_Structure/de.md)-Objekt ist, und einem Profil `sketch`.
    -   
        `diameter`
        
        , `amount` und `offset` werden verwendet, um die Merkmale der Stäbe festzulegen.

    -   Sind keine Werte für `diameter` (Durchmesser), `amount` (Menge) oder `offset` (Abstand) angegeben, werden die Standardwerte aus den [Arch Einstellungen](Arch_Preferences/de.md) verwendet.

Beispiel:


```python
import FreeCAD, Arch, Part

Structure = Arch.makeStructure(None, length=1000, width=1000, height=3000)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

p1 = FreeCAD.Vector(-400, 400, 0)
p2 = FreeCAD.Vector(400, 400, 0)
Sketch = FreeCAD.ActiveDocument.addObject('Sketcher::SketchObject', 'Sketch')
Sketch.MapMode = "FlatFace"
Sketch.Support = [(Structure, "Face6")]
Sketch.addGeometry(Part.LineSegment(p1, p2))
FreeCAD.ActiveDocument.recompute()

Rebar = Arch.makeRebar(Structure, Sketch, diameter=80, amount=7, offset=50)
Rebar.OffsetStart = 100
Rebar.OffsetEnd = 100
FreeCAD.ActiveDocument.recompute()
```







{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > Arch Rebar/de
