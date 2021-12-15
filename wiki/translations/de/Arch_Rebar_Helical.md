---
- GuiCommand:/de
   Name:Arch_Rebar_Helical   Name/de:Arch Bewehrungsstab spiralförmig
   MenuLocation:Arch → Rebar tools → Spiralförmige Bewehrung oder 3D/BIM → Verstärkung → Spiralförmige Bewehrung 
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   Version:0.17
   SeeAlso:[Reinforcement](Reinforcement_Workbench/de.md), [Arch Bewehrung](Arch_Rebar/de.md), [bügelförmiger Bewehrungsstab](Arch_Rebar_Stirrup/de.md),[Arch Stützenverstärkung](Arch_Rebar_ColumnReinforcement/de.md)
---

# Arch Rebar Helical/de

## Beschreibung

Das [spiralförmiger Bewehrungsstab](Arch_Rebar_Helical/de.md)-Werkzeug erlaubt es dem Anwender, einen fortlaufenden spiralförmigen Bewehrungsstab in einem [Struktur](Arch_Structure/de.md)-Objekt zu erstellen.

Das [Arch Spiralförmiger Bewehrungsstab](Arch_Rebar_Helical/de.md)-Werkzeug ist auch im [BIM-Arbeitsbereich](BIM_Workbench/de.md) integriert.


<div class="mw-translate-fuzzy">

Dieser Befehl ist Teil des _ über das Menü **Werkzeuge → Addon-Manager → Reinforcement** installiert werden kann.


</div>


:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">



*Ein fortlaufender spiralförmiger Bewehrungsstab in einer [Struktur](Arch_Structure/de.md)*

## Anwendung

1.  Wähle eine beliebige Fläche eines vorher erstellten **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**-Objekts.
2.  Wähle dann **<img src="images/Arch_Rebar_Helical.svg" width=16px> [Spiralförmiger Bewehrungsstab](Arch_Rebar_Helical/de.md)** aus den Bewehrungsstab-Werkzeugen.
3.  Ein [Aufgaben-Paneel](Task_panel/de.md) wird auf der linken Seite des Bildschirm angezeigt wie im folgenden Bild dargestellt.
4.  Wähle die gewünschte Ausrichtung.
5.  Fülle die Werte wie \'Left Cover\' (linke Fläche), \'Right Cover\' (rechte), \'Top Cover\' (obere), \'Bottom Cover\' (untere), \'Front Cover\' (vordere), \'Anchor length\' (Ankerlänge), \'Bent Angle\' (Biegungswinkel), \'Bent Factor\', \'Rounding\' und \'Diameter\' (Durchmesser) des Bewehrungsstabes.
6.  Wähle den Verteilungsmodus, entweder `'Amount'` (Menge) oder `'Spacing'` (Abstand).
7.  Falls \'Spacing\' gewählt wurde, kann auch [benutzerdefinierter Abstand](Custom_Spacing/de.md) gewählt werden.
8.  Wähle **Pick selected face** zur Überprüfung oder ändere die Fläche zur Verteilung der Bewehrungsstäbe.
9.  Klicke **OK** oder **Anwenden** zur Erzeugung der Bewehrungsstäbe.
10. Klicke **Abbrechen** zum Verlassen des Aufgaben-Paneels.

:   <img alt="" src=images/HelicalRebarDialog.png  style="width:250px;">



*Aufgaben-Ansicht für das Arch Bewehrungsstab spiralförmig-Werkzeug*

## Eigenschaften

-    {{PropertyData/de|Side Cover}}: Der Abstand zwischen dem Bewehrungsstab und der gekrümmten Fläche.

-    {{PropertyData/de|Top Cover}}: Der Abstand zwischen dem Bewehrungsstab und der oberen Fläche der Struktur.

-    {{PropertyData/de|Bottom Cover}}: Der Abstand zwischen dem Bewehrungsstab und der unteren Fläche der Struktur.

-    {{PropertyData/de|Pitch}}: Die Höhe einer vollständigen Helixumdrehung, gemessen parallel zu den Achsen der Helix.

-    {{PropertyData/de|Diameter}}: Durchmesser des Bewehrungsstabs.

## Scripting


**Siehe auch:**

[Arch API](Arch_API/de.md),[Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/de.md).

Das Spiralförmiger Bewehrungsstab-Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion angesprochen werden:


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-   Erstellt ein `Rebar`-Objekt aus der gegebenen `structure`, die eine [Arch Struktur](Arch_Structure/de.md) ist, und `facename`, die eine Fläche dieser Struktur ist.
    -   Falls weder `structure` noch `facename` gegeben sind, wird die vom Benutzer gewählte Fläche als Eingabe genommen.

-    `s_cover`, `b_cover` und `t_cover` sind innere Abstände von den Bewehrungsstabelementen zu den Flächen der Struktur. Dies sind entsprechend die seitlichen, unteren und oberen Abstände.

-    `diameter`ist der Durchmesser der Verstärkungsstäbe innerhalb der Struktur.

-    `pitch`ist der Parameter, der festlegt, wie groß der Abstand der Windungen von einander ist.

### Beispiel


```python
import FreeCAD, Draft, Arch, HelicalRebar

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = HelicalRebar.makeHelicalRebar(10, 50, 8, 50, 50, structure, "Face2")
```

### Anpassung des Bewehrungsstabs 

Die Eigenschaften des Bewehrungsstabs lassen sich mit der folgenden Funktion verändern


```python
editHelicalRebar(Rebar, s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-    `Rebar`ist ein vorher erzeugtes `HelicalRebar`-Objekt.

-   Die anderen Parameter sind die gleichen wie die für die `makeHelicalRebar()`-Funktion erforderlichen.

-    `structure`und `facename` können weggelassen werden, so dass die Bewehrung in der ursprünglichen Struktur bleibt.


```python
import HelicalRebar

HelicalRebar.editHelicalRebar(Rebar, 20, 100, 20, 20, 100)
```


{{docnav/de
|[bügelförmiger Bewehrungsstab](Arch_Rebar_Stirrup/de.md)
|[Bewehrung Rundsäulenverstärkung](Arch_Rebar_Circular_ColumnReinforcement/de.md)
|[Arch-Arbeitsbereich](Arch_Workbench/de.md)
|IconL=Arch_Rebar_Stirrup.svg
|IconR=Arch_Rebar_ColumnReinforcement.svg
|IconC=Workbench_Arch.svg
}}


 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Helical/de
