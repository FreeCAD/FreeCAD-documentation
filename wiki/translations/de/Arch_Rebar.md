---
- GuiCommand:/de
   Name:Arch Rebar
   Name/de:Architektur Bewehrung oder 3D/BIM-Verstärkung
   MenuLocation:Architektur → Bewehrung
   Workbenches:[Architektur](Arch_Workbench/de.md),[BIM](BIM_Workbench/de.md)
   Shortcut:**R** **B**
   SeeAlso:[Architektur Struktur](Arch_Structure/de.md), [Verstärkungserweiterung](Reinforcement_Workbench/de.md)
---

# Arch Rebar/de

## Beschreibung

Das [Architektur Bewehrung](Arch_Rebar/de.md) Werkzeug erlaubt es, [Bewehrungsstäbe](https://de.wikipedia.org/wiki/Bewehrungsstahl) in [Struktur](Arch_Structure/de.md) Objekten zu platzieren.

Das [Arch Bewehrung](Arch_Rebar/de.md)-Werkzeug ist auch im [BIM-Arbeitsbereich](BIM_Workbench/de.md) integriert.

Bewehrungsobjekte basieren auf 2D Profilen wie [Entwurfsobjekten](Draft_Workbench/de.md) und [Skizzen](Sketcher_Workbench/de.md), die auf einer Fläche des Strukturobjekts gezeichnet werden müssen. Nach der Erstellung kannst du die Eigenschaften des Bewehrungsstabs anpassen, einschließlich der Anzahl und des Durchmessers der Stäbe und des Versatzabstands zwischen ihnen und den Flächen des Strukturelements.

<img alt="" src=images/Arch_Rebar_example.jpg  style="width:400px;"> 
*Strukturobjekt mit zwei auf seinen Flächen gezeichneten Skizzen, die dann in zwei Sätze von Bewehrungsobjekten umgewandelt werden*

## Verfügbare Erweiterung 


<div class="mw-translate-fuzzy">

Das Bewehrungswerkzeug wird durch den [Bewehrung-Arbeitsbereich](Reinforcement_Workbench/de.md) erweitert, der über den [Erweiterungsverwalter](Std_AddonMgr/de.md) installiert wird. Die zusätzlich verfügbaren Bewehrungstypen der Erweiterung sind:

-   <img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Gerader Bewehrungsstab](Arch_Rebar_Straight/de.md)
-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [U-förmiger Bewehrungsstab](Arch_Rebar_UShape/de.md)
-   <img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [L-förmiger Bewehrungsstab](Arch_Rebar_LShape/de.md)
-   <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Gebogener Formstab](Arch_Rebar_BentShape/de.md)
-   <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Bügelförmiger Bewehrungsstab](Arch_Rebar_Stirrup/de.md)
-   <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Spiralförmiger Bewehrungsstab](Arch_Rebar_Helical/de.md)


</div>

## Anwendung

1.  Wechsle zum <img alt="" src=images/Workbench_Arch.svg  style="width:16px;"> [Architektur Arbeitsbereich](Arch_Workbench/de.md)
2.  Erstelle ein **<img src="images/Arch_Structure.svg" width=16px> [Architektur Struktur](Arch_Structure/de.md)** Element
3.  Wechsle zum <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md).
4.  Wähle eine Fläche des Strukturelements.
5.  Drücke die **<img src="images/Sketcher_NewSketch.png" width=16px> [Neue Skizze](Sketcher_NewSketch/de.md)** Schaltfläche, um eine neue Skizze auf der gewählten Fläche zu erstellen.
6.  Zeichne das Balkendiagramm.
7.  Drücke die **<img src="images/Sketcher_LeaveSketch.png" width=16px> [Skizze verlassen](Sketcher_LeaveSketch/de.md)** Schaltfläche zum Beenden.
8.  Wechsle zurück zum [Arch Arbeitsbereich](Arch_Workbench/de.md)
9.  Wähle die gerade gezeichnete Skizze
10. Drücke die **<img src="images/Arch_Rebar.svg" width=16px> [Bewehrungsstab](Arch_Rebar/de.md)** Schaltfläche oder drücke die **R**, dann **B** Tasten.
11. Passe die gewünschten Eigenschaften an (Dein Bewehrungsstab erscheint möglicherweise nicht sofort, wenn einige der Eigenschaften eine unmögliche Situation schaffen, wie z.B. wenn der Stabdurchmesser 0 ist oder die Versatzabstände größer als die Länge des Strukturelements sind).

Obwohl ein Bewehrungsstab normalerweise in einem Architekturelement verwendet wird, kann er seit FreeCAD v0.19 auch außerhalb eines Host-Objekts erstellt werden. Um einen Bewehrungsstab in einem Objekt zu platzieren, muss einfach nur dessen **Host** gesetzt werden.

## Optionen

-   Bewehrungsstäbe haben die gleichen Eigenschaften und das gleiche Verhalten aller [Arch-Komponenten](Arch_Component/de.md)
-   Der Verrundungswert wird als Vielfaches des Durchmessers ausgedrückt. Wenn Dein Stab einen Durchmesser von 5 mm hat, wird ein Verrundungswert von 3 zu einem Radius von 15 mm in den Ecken führen.
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

Das Bewehrungsstabwerkzeug kann in [Makros](macros/de.md) und aus der [PythonKonsole](Python/de.md) aus mit folgender Funktion verwendet werden: 
```python
Rebar = makeRebar(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name="Rebar")
```

-   Erstellt ein `Rebar` Objekt aus dem gegebenen `baseobj` Objekt, das eine [Struktur](Arch_Structure/de.md)-Objekt ist und ein `sketch` als Profil.
    -   
        `diameter`
        
        , `amount` und `offset` werden verwendet, um die Charakteristiken der Stäbe zu definieren.
-   Falls `diameter` (Durchmesser), `amount` (Menge) oder `offset` (Abstand) nicht angegeben sind, werden die Standardwerte aus den [Arch Einstellungen](Arch_Preferences/de.md) verwendet.

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





 

[<img src="images/Property.png" style="width:16px"> External Command Reference](Category_External_Command_Reference.md) [<img src="images/Property.png" style="width:16px"> Reinforcement](Category_Reinforcement.md)

---
[documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Arch](Arch_Workbench.md) > Arch Rebar/de
