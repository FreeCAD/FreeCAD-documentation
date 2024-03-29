---
 GuiCommand:
   Name: Arch Rebar LShape
   Name/de: Arch Armierung LForm
   MenuLocation: Arch , Rebar tools , L-Shape Rebar<br>3D/BIM , Reinforcement tools , L-förmige Bewehrung
   Workbenches: Arch_Workbench/de, BIM_Workbench/de
   Version: 0.17
   SeeAlso: Reinforcement_Workbench/de, Arch_Rebar/de, Arch_Rebar_BentShape/de
---

# Arch Rebar LShape/de



## Beschreibung

Das Werkzeug [Armierung L-Form](Arch_Rebar_LShape/de.md) ermöglicht dem Anwender, einen Satz von L-förmigen Bewehrungsstäben in einem [Arch Struktur](Arch_Structure/de.md)-Objekt zu erstellen.

Das Werkzeug [Armierung L-Form](Arch_Rebar_LShape/de.md) ist auch im Arbeitsbereich [BIM](BIM_Workbench/de.md) integriert.

Dieser Befehl ist Teil des Arbeitsbereichs [Reinforcement](Reinforcement_Workbench/de.md), ein [externer Arbeitsbereich](External_workbenches/de.md), der mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) über das Menü **Werkzeuge → Addon-Manager → Reinforcement** installiert werden kann.

<img alt="" src=images/Arch_Rebar_LShape_example.png  style="width:400px;"> 
*Vier Sätze von L-förmigen Bewehrungsstäben in einem [Arch Struktur](Arch_Structure/de.md)-Objekt*



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

<img alt="" src=images/LShapeDialog.png  style="width:250px;"> 
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



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md),[Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Armierung AbgesetzteBewehrung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden: 
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



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar LShape/de
