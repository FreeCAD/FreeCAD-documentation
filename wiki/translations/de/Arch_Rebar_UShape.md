---
 GuiCommand:
   Name: Arch Rebar UShape
   Name/de: Arch Armierung UForm
   MenuLocation: Arch , Rebar tools , U-förmige Bewehrung<br>3D/BIM , Reinforcement tools , U-förmige Bewehrung
   Workbenches: Arch Workbench/de, BIM Workbench/de
   Version: 0.17
   SeeAlso: Reinforcement_Workbench/de, Arch_Rebar/de,Arch_Rebar_LShape/de
---

# Arch Rebar UShape/de



## Beschreibung

Das Werkzeug [Armierung U-Form](Arch_Rebar_UShape/de.md) erlaubt dem Anwender, einen Satz U-förmiger Bewehrungsstäbe in einem [Arch Struktur](Arch_Structure/de.md)-Objekt zu erstellen.

Das Werkzeug **<img src="images/Arch_Rebar_UShape.svg" width=16px>[Armierung U-Form](Arch_Rebar_UShape/de.md)** ist auch in den Arbeitsbereich [BIM](BIM_Workbench/de.md) integriert.

Dieser Befehl ist Teil des Arbeitsbereichs [Reinforcement](Reinforcement_Workbench/de.md), einem [externen Arbeitsbereich](External_workbenches/de.md), der mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) über das Menü **Werkzeuge → Addon-Manager → Reinforcement** installiert werden kann.

<img alt="" src=images/Arch_Rebar_UShape_example.png  style="width:400px;"> 
*Zwei Sätze U-förmiger Bewehrungsstäbe in einem [Arch Struktur](Arch_Structure/de.md)-Objekt*



## Anwendung

1.  Eine beliebige Fläche eines vorher erstellten **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**-Objekts auswählen.

2.  Dann **<img src="images/Arch_Rebar_UShape.svg" width=16px> [U-förmige Bewehrung](Arch_Rebar_UShape/de.md)** aus den Bewehrungswerkzeugen auswählen.

3.  Der [Aufgaben-Bereich](Task_panel/de.md) wird auf der linken Seite des Bildschirm angezeigt, wie im folgenden Bild dargestellt.

4.  Die gewünschte Ausrichtung auswählen.

5.  Die Werte wie \'Left Cover\' (linke Fläche), \'Right Cover\' (rechte), \'Top Cover\' (obere), \'Bottom Cover\' (untere), \'Front Cover\' (vordere), \'Anchor length\' (Ankerlänge), \'Bent Angle\' (Biegungswinkel), \'Bent Factor\', \'Rounding\' und \'Diameter\' (Durchmesser) des Bewehrungsstabes eingeben.

6.  Den Verteilungsmodus auswählen, entweder `'Amount'` (Menge) oder `'Spacing'` (Abstand).

7.  Falls \'Spacing\' ausgewählt wurde, kann auch [benutzerdefinierter Abstand](Custom_Spacing/de.md) ausgewählt werden.

8.  
    **Pick selected face**wird verwendet, um die Fläche für die Verteilung der Bewehrungsstäbe zu bestätigen oder zu ändern.

9.  Schaltfläche **OK** oder **Anwenden** drücken, um die Bewehrungsstäbe zu erstellen.

10. Schaltfläche **Abbrechen** drücken, um den Aufgaben-Bereich zu verlassen.

<img alt="" src=images/UShapeDialog.png  style="width:250px;"> 
*Aufgaben-Ansicht für das Arch Bewehrungsstab U-förmig-Werkzeug*



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

[Arch API](Arch_API/de.md),[Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Armierung U-Form kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden: 
```python
Rebar = makeUShapeRebar(f_cover, b_cover, r_cover, l_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                        structure=None, facename=None)
```

-   Erstellt ein `Rebar`-Objekt aus dem gegebenen `structure`-Objekt, das eine [Arch Struktur](Arch_Structure/de.md) ist, und `facename`, das eine Fläche dieser Struktur ist.
    -   Falls weder `structure` noch `facename` gegeben sind, wird die vom Benutzer gewählte Fläche als Eingabe genommen.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover`, und `t_cover` sind innere Abstände von den Bewehrungselementen zu den Flächen der Struktur. Dies sind entsprechend die vorderen, unteren, linken, rechten und oberen Abstände.

-    `diameter`ist der Durchmesser der Bewehrungsstäbe innerhalb der Struktur.

-    `rounding`ist der Parameter, der den Biegeradius der Bewehrungsstäbe angibt.

-    `amount_spacing_check`Falls `True` werden so viele Bewehrungsstäbe erstellt, wie unter `amount_spacing_value` angegeben; falls `False` werden die Bewehrungsstäbe im Abstand von `amount_spacing_value` erstellt.

-    `amount_spacing_value`gibt die Anzahl von Bewehrungsstäben an oder den Abstandswert, abhängig von `amount_spacing_check`.

-    `orientation`gibt die Ausrichtung der Bewehrung an; möglich sind `"Bottom"` (unten), `"Top"` (oben), `"Right"` (rechts) oder `"Left"` (links).



### Beispiel


```python
import FreeCAD, Arch, UShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = UShapeRebar.makeUShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = UShapeRebar.makeUShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```



### Bearbeiten der Bewehrung 

Die Eigenschaften des Bewehrungsstabs lassen sich mit der folgenden Funktion verändern


```python
editUShapeRebar(Rebar, f_cover, b_cover, r_cover, l_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None) 
```

-    `Rebar`ist ein vorher erzeugtes `UShapeRebar`-Objekt.

-   Die anderen Parameter sind die gleichen wie die für die `makeUShapeRebar()`-Funktion erforderlichen.

-    `structure`und `facename` können weggelassen werden, so dass die Bewehrung in der ursprünglichen Struktur bleibt.


```python
import UShapeRebar

UShapeRebar.editUShapeRebar(Rebar, 50, 50, 20, 20,
                            16, 20, 5, True, 5, "Top")

UShapeRebar.editUShapeRebar(Rebar2, 70, 50, 20, 20,
                            16, 70, 5, True, 5, "Top")
```


{{docnav/de
|[Armierung GeradlinigeBewehrung](Arch_Rebar_Straight/de.md)
|[Armierung LForm](Arch_Rebar_LShape/de.md)
|[Arch](Arch_Workbench/de.md)
|IconL=Arch_Rebar_Straight.svg
|IconR=Arch_Rebar_LShape.svg
|IconC=Workbench_Arch.svg
}}



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar UShape/de
