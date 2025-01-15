---
 GuiCommand:
   Name: Reinforcement LShapeRebar
   Name/de: Reinforcement LBewehrung
   MenuLocation: 3D/BIM , Bewehrungswerkzeuge , L-förmige Bewehrung
   Workbenches: Reinforcement_Workbench/de, BIM_Workbench/de
   Version: 0.17
   SeeAlso: 
---

# Reinforcement LShapeRebar/de



## Beschreibung

Das Werkzeug [Reinforcement LBewehrung](Reinforcement_LShapeRebar.md) ermöglicht dem Anwender, einen Satz von L-förmigen Bewehrungsstäben in einem [Arch Struktur](Arch_Structure/de.md)-Objekt zu erstellen.

Dieses Werkzeug ist Teil des Arbeitsbereichs [Reinforcement](Reinforcement_Workbench/de.md); dieser ist ein [externer Arbeitsbereich](External_workbenches/de.md), der mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden kann.

<img alt="" src=images/Arch_Rebar_LShape_example.png  style="width:400px;"> 
*Vier Sätze von L-förmigen Bewehrungsstäben in einem [Arch Struktur](Arch_Structure/de.md)-Objekt*



## Anwendung

1.  Eine beliebige Fläche eines vorher erstellten **<img src="images/Arch_Structure.svg" width=16px> [Arch-Struktur](Arch_Structure/de.md)**-Objekts auswählen.

2.  Dann **<img src="images/Reinforcement_LShapeRebar.svg" width=16px> [L-förmiger Bewehrungsstab](Reinforcement_LShapeRebar/de.md)** aus den Armierungswerkzeugen auswählen.

3.  Ein [Aufgaben-Bereich](Task_panel/de.md) wird auf der linken Seite des Bildschirm angezeigt wie im folgenden Bild dargestellt.

4.  Die gewünschte Ausrichtung auswählen.

5.  Die Werte für \'Betondeckung links\', \'Betondeckung rechts\', \'Betondeckung oben\', \'Betondeckung unten\', \'Betondeckung vorne\', \'Bent Angle\' (Biegungswinkel), \'Bent Factor\', \'Rundung\' und \'Durchmesser\' des Bewehrungsstabes eingeben.

6.  Verteilungsmodus auswählen, entweder `'Anzahl'` oder `'Abstand'` (Abstand).

7.  Falls \'Abstand\' ausgewählt wurde, kann auch ein [Benutzerdefinierter Abstand](Reinforcement_Custom_Spacing/de.md) ausgewählt werden.

8.  
    **Markierte Seite auswählen**wird zum Überprüfen oder Ändern der Fläche zur Verteilung der Bewehrungsstäbe eingesetzt.

9.  
    **OK**oder **Anwenden** anklicken, um die Bewehrungsstäbe zu erstellen.

10. 
    **Abbrechen**anklicken, um den Aufgaben-Bereich zu verlassen.

<img alt="" src=images/LShapeDialog.png  style="width:250px;"> 
*Aufgaben-Bereich für das Werkzeug*



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

[Arch-API](Arch_API/de.md),[Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Reinforcement LBewehrung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


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



### Bearbeiten der Bewehrung 

Die Eigenschaften des Bewehrungsstabes lassen sich mit der folgenden Funktion verändern:


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
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement LShapeRebar/de
