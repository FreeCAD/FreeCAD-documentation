---
- GuiCommand:/de
   Name:Arch Rebar LShape   Name/de:Arch Bewehrungsstab L-förmig
   MenuLocation:Arch → Rebar tools → L-Shape Rebar oder 3D/BIM → Reinforcement tools → L-förmige Bewehrung
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   Version:0.17
   SeeAlso:[Verstärkung](Reinforcement_Workbench/de.md), [Bewehrungsstab](Arch_Rebar/de.md), [abgewinkelter Bewehrungsstab](Arch_Rebar_BentShape/de.md)
---

# Arch Rebar LShape/de

## Beschreibung

Das [L-förmiger Bewehrungsstab](Arch_Rebar_LShape/de.md)-Werkzeug erlaubt es dem Anwender, einen Satz von L-förmigen Bewehrungsstäben in einem [Struktur](Arch_Structure/de.md)-Objekt zu erstellen.

Das [Arch L-förmiger Bewehrungsstab](Arch_Rebar_LShape/de.md)-Werkzeug ist auch im [BIM-Arbeitsbereich](BIM_Workbench/de.md) integriert.


<div class="mw-translate-fuzzy">

Dieser Befehl ist Teil des [Verstärkungs](Reinforcement_Workbench/de.md)-Arbeitsbereichs, einem [externen Arbeitsbereich](External_workbenches/de.md), der mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) über das Menü **Werkzeuge → Addon-Manager → Reinforcement** installiert werden kann.


</div>

<img alt="" src=images/Arch_Rebar_LShape_example.png  style="width:400px;"> 
*Vier Sätze von L-förmigen Bewehrungsstäben in einer [Struktur](Arch_Structure/de.md)*

## Anwendung

1.  Wähle eine beliebige Fläche eines vorher erstellten **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**-Objekts.
2.  Wähle dann **<img src="images/Arch_Rebar_LShape.svg" width=16px> [L-förmiger Bewehrungsstab](Arch_Rebar_LShape/de.md)** aus den Bewehrungsstab-Werkzeugen.
3.  Ein [Aufgaben-Paneel](Task_panel/de.md) wird auf der linken Seite des Bildschirm angezeigt wie im folgenden Bild dargestellt.
4.  Wähle die gewünschte Ausrichtung.
5.  Fülle die Werte wie \'Left Cover\' (linke Fläche), \'Right Cover\' (rechte), \'Top Cover\' (obere), \'Bottom Cover\' (untere), \'Front Cover\' (vordere), \'Anchor length\' (Ankerlänge), \'Bent Angle\' (Biegungswinkel), \'Bent Factor\', \'Rounding\' und \'Diameter\' (Durchmesser) des Bewehrungsstabes.
6.  Wähle den Verteilungsmodus, entweder `'Amount'` (Menge) oder `'Spacing'` (Abstand).
7.  Falls \'Spacing\' gewählt wurde, kann auch [benutzerdefinierter Abstand](Custom_Spacing/de.md) gewählt werden.
8.  Wähle **Pick selected face** zur Überprüfung oder ändere die Fläche zur Verteilung der Bewehrungsstäbe.
9.  Klicke **OK** oder **Anwenden** zur Erzeugung der Bewehrungsstäbe.
10. Klicke **Abbrechen** zum Verlassen des Aufgaben-Paneels.

:   <img alt="" src=images/LShapeDialog.png  style="width:250px;">



*Aufgaben-Ansicht für das Arch Bewehrungsstab L-förmig-Werkzeug*

## Eigenschaften

-    **Orientation**: Legt die Ausrichtung der Bewehrungsstäbe fest (\"Bottom Right\", \"Bottom Left\", \"Top Right\" und \"Top Left\").

-    **Front Cover**: Der Abstand zwischen Bewehrungsstab und gewählter Fläche.

-    **Right Cover**: Der Abstand zwischen dem rechten Ende des Bewehrungsstabs bis zur rechten Fläche der Struktur.

-    **Left Cover**: Der Abstand zwischen dem linken Ende des Bewehrungsstabs bis zur linken Fläche der Struktur.

-    **Bottom Cover**: Der Abstand zwischen Bewehrungsstab bis zur unteren Fläche der Struktur.

-    **Top Cover**: Der Abstand zwischen dem Bewehrungsstab bis zur oberen Fläche der Struktur.

-    **Rounding**: A rounding value to be applied to the corners of the bars, expressed in times the diameter.

-    **Amount**: Die Anzahl der Bewehrungsstäbe.

-    **Spacing**: Der Abstand zwischen den Achsen der Bewehrungsstäbe.

## Scripting


**Siehe auch:**

[Arch API](Arch_API/de.md), [Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das L-förmiger Bewehrungsstab-Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion angesprochen werden: 
```python
Rebar = makeLShapeRebar(f_cover, b_cover, l_cover, r_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom Left",
                        structure=None, facename=None):
```

-   Erstellt ein `Rebar`-Objekt aus der gegebenen `structure`, die eine [Arch Struktur](Arch_Structure/de.md) ist, und `facename`, die eine Fläche dieser Struktur ist.
    -   Falls weder `structure` noch `facename` gegeben sind, wird die vom Benutzer gewählte Fläche als Eingabe genommen.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover`, und `t_cover` sind innere Abstände von den Bewehrungsstabelementen zu den Flächen der Struktur. Dies sind entsprechend die vorderen, unteren, linken, rechten und oberen Abstände.

-    `diameter`ist der Durchmesser der Verstärkungsstäbe innerhalb der Struktur.

-    `rounding`ist der Parameter, der den Biegeradius der Verstärkungsstäbe angibt.

-    `amount_spacing_check`Falls `True` werden so viele Bewehrungsstäbe erstellt, wie unter `amount_spacing_value` angegeben; falls `False` werden die Bewehrungsstäbe im Abstand von `amount_spacing_value` erstellt.

-    `amount_spacing_value`gibt die Anzahl von Bewehrungsstäben an oder den Abstandswert, abhängig von `amount_spacing_check`.

-    `orientation`gibt die Ausrichtung der Bewehrung an; möglich sind `"Bottom Right"` (unten rechts), `"Top Rechts"` (oben rechts), `"Bottom Left"` (unten links) oder `"Bottom Right"` (unten rechts).

### Beispiel


```python
import FreeCAD, Arch, LShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = LShapeRebar.makeLShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom Left", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = LShapeRebar.makeLShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom Left", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```

### Anpassung des Bewehrungsstabs 

Die Eigenschaften des Bewehrungsstabs lassen sich mit der folgenden Funktion verändern 
```python
editLShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None)
```

-    `Rebar`ist ein vorher erzeugtes `LShapeRebar`-Objekt.

-   Die anderen Parameter sind die gleichen wie die für die `makeLShapeRebar()`-Funktion erforderlichen.

-    `structure`und `facename` können weggelassen werden, so dass die Bewehrung in der ursprünglichen Struktur bleibt.


```python
import LShapeRebar

LShapeRebar.editLShapeRebar(Rebar, 50, 50, 20, 20,
                            12, 50, 6, True, 5, "Top Right")

LShapeRebar.editLShapeRebar(Rebar2, 50, 50, 20, 20,
                            12, 70, 6, True, 5, "Top Right")
```


{{docnav/de
|[U-förmiger Bewehrungsstab](Arch_Rebar_UShape/de.md)
|[abgewinkelter Bewehrungsstab](Arch_Rebar_BentShape/de.md)
|[Arch-Arbeitsbereich](Arch_Workbench/de.md)
|IconL=Arch_Rebar_UShape.svg
|IconR=Arch_Rebar_BentShape.svg
|IconC=Workbench_Arch.svg
}}







[<img src="images/Property.png" style="width:16px"> Reinforcement](Category_Reinforcement.md)

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar LShape/de
