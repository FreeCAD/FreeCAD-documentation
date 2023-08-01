---
- GuiCommand:
   Name:Arch_Rebar_BentShape   Name/de:Arch Bewehrungsstab abgewinkelt
   MenuLocation:Arch → Rebar tools → Gebogene Bewehrung oder 3D/BIM → Verstärkung → gebogene Bewehrung 
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   Version:0.17
   SeeAlso:[Reinforcement](Reinforcement_Workbench/de.md), [Arch Bewehrung](Arch_Rebar/de.md), [bügelförmiger Bewehrungsstab](Arch_Rebar_Stirrup/de.md)
---

# Arch Rebar BentShape/de


</div>



## Beschreibung

Das [Abgewinkelter Bewehrungsstab](Arch_Rebar_BentShape/de.md)-Werkzeug erlaubt es dem Anwender, einen Satz von abgewinkelten Bewehrungsstäben in einem [Struktur](Arch_Structure/de.md)-Objekt zu erstellen.

Das [Arch Abgewinkelter Bewehrungsstab](Arch_Rebar_BentShape/de.md)-Werkzeug ist auch im [BIM-Arbeitsbereich](BIM_Workbench/de.md) integriert.

Dieser Befehl ist Teil des Arbeitsbereichs [Reinforcement](Reinforcement_Workbench/de.md), der mit dem ![](images/Std_AddonMgr.svg ) [Addon-Manager](Std_AddonMgr/de.md) über das Menü **Werkzeuge → Addon-Manager → Reinforcement** installiert werden kann.

<img alt="" src=images/Arch_Rebar_BentShape_example.png  style="width:400px;"> 
*Zwei Sätze von abgewinkelten Bewehrungsstäben in einer [Struktur](Arch_Structure/de.md)*



## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle eine beliebige Fläche eines vorher erstellten **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**-Objekts.
2.  Wähle dann **<img src="images/Arch_Rebar_BentShape.svg" width=16px> [Abgewinkelter Bewehrungsstab](Arch_Rebar_BentShape/de.md)** aus den Bewehrungsstab-Werkzeugen.
3.  Ein [Aufgaben-Paneel](Task_panel/de.md) wird auf der linken Seite des Bildschirm angezeigt wie im folgenden Bild dargestellt.
4.  Wähle die gewünschte Ausrichtung.
5.  Fülle die Werte wie \'Left Cover\' (linke Fläche), \'Right Cover\' (rechte), \'Top Cover\' (obere), \'Bottom Cover\' (untere), \'Front Cover\' (vordere), \'Anchor length\' (Ankerlänge), \'Bent Angle\' (Biegungswinkel), \'Bent Factor\', \'Rounding\' und \'Diameter\' (Durchmesser) des Bewehrungsstabes.
6.  Wähle den Verteilungsmodus, entweder `'Amount'` (Menge) oder `'Spacing'` (Abstand).
7.  Falls \'Spacing\' gewählt wurde, kann auch [benutzerdefinierter Abstand](Custom_Spacing/de.md) gewählt werden.
8.  Wähle **Pick selected face** zur Überprüfung oder ändere die Fläche zur Verteilung der Bewehrungsstäbe.
9.  Klicke **OK** oder **Anwenden** zur Erzeugung der Bewehrungsstäbe.
10. Klicke **Abbrechen** zum Verlassen des Aufgaben-Paneels.


</div>


:   <img alt="" src=images/BentShapeDialog.png  style="width:250px;">



*Aufgaben-Ansicht für das Arch Bewehrungsstab abgewinkelt-Werkzeug*



## Eigenschaften

-    {{PropertyData/de|Orientation}}: Legt die Ausrichtung des Bewehrungsstabs fest (wie unten, oben, recht und links).

-    {{PropertyData/de|Front Cover}}: Der Abstand zwischen Bewehrungsstab und ausgewählter Fläche.

-    {{PropertyData/de|Left Cover}}: Der Abstand zwischen dem linken Ende des Bewehrungsstabs und der linken Fläche der Struktur.

-    {{PropertyData/de|Right Cover}}: Der Abstand zwischen dem rechten Ende des Bewehrungsstabs und der rechten Fläche der Struktur.

-    {{PropertyData/de|Bottom Cover}}: Der Abstand zwischen dem Bewehrungsstab und der unteren Fläche der Struktur.

-    {{PropertyData/de|Top Cover}}: Der Abstand zwischen dem Bewehrungsstab und der oberen Fläche der Struktur.

-    {{PropertyData/de|Anchor Length}}: Die \"Armlänge\" des abgewinkelten Bewehrungsstabs.

-    {{PropertyData/de|Bent Angle}}: Definiert den Winkel zwischen den Enden eines Bügels.

-    {{PropertyData/de|Amount}}: Die Anzahl von Bewehrungsstäben.

-    {{PropertyData/de|Spacing}}: Der Abstand zwischen den Achsen jedes Bewehrungsstabs.




<div class="mw-translate-fuzzy">

## Scripting


**Siehe auch:**

[Arch API](Arch_API/de.md),[Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/de.md).


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Das Abgewinkelter Bewehrungsstab-Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion angesprochen werden:


</div>


```python
Rebar = makeBentShapeRebar(f_cover, b_cover, l_cover, r_cover,
                           diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                           structure=None, facename=None)
```

-   Erstellt ein `Rebar`-Objekt aus der gegebenen `structure`, die eine [Arch Struktur](Arch_Structure/de.md) ist, und `facename`, die eine Fläche dieser Struktur ist.
    -   Falls weder `structure` noch `facename` gegeben sind, wird die vom Benutzer gewählte Fläche als Eingabe genommen.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover`, und `t_cover` sind innere Abstände von den Bewehrungsstabelementen zu den Flächen der Struktur. Dies sind entsprechend die vorderen, unteren, linken, rechten und oberen Abstände.

-    `diameter`ist der Durchmesser der Verstärkungsstäbe innerhalb der Struktur.

-    `rounding`ist der Parameter, der den Biegeradius der center Verstärkungsstäbe angibt.

-    `bentLength`und `bentAngle` definieren die Länge der Spitze der Verstärkungsstäbe und den Biegewinkel der center Stäbe.

-    `amount_spacing_check`Falls `True` werden so viele Bewehrungsstäbe erstellt, wie unter `amount_spacing_value` angegeben; falls `False` werden die Bewehrungsstäbe im Abstand von `amount_spacing_value` erstellt.

-    `amount_spacing_value`gibt die Anzahl von Bewehrungsstäben an oder den Abstandswert, abhängig von `amount_spacing_check`.

-    `orientation`gibt die Ausrichtung der Bewehrung an; möglich sind `"Bottom"` (unten), `"Top"` (oben), `"Left"` (links) oder `"Right"` (rechts) sein.



### Beispiel


```python
import FreeCAD, Arch, BentShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=100)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = BentShapeRebar.makeBentShapeRebar(50, 20, 20, 20,
                                          8, 40, 100, 135, 2, True, 4, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = BentShapeRebar.makeBentShapeRebar(50, 40, 20, 20,
                                           8, 20, 100, 135, 2, True, 4, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```



### Anpassung des Bewehrungsstabs 

Die Eigenschaften des Bewehrungsstabs lassen sich mit der folgenden Funktion verändern


```python
editBentShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                   diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation,
                   structure=None, facename=None)
```

-    `Rebar`ist ein vorher erzeugtes `BentShapeRebar`-Objekt.

-   Die anderen Parameter sind die gleichen wie die für die `makeBentShapeRebar()`-Funktion erforderlichen.

-    `structure`und `facename` können weggelassen werden, so dass die Bewehrung in der ursprünglichen Struktur bleibt.


```python
import BentShapeRebar

BentShapeRebar.editBentShapeRebar(Rebar, 50, 20, 20, 20,
                                  12, 20, 100, 155, 2, True, 6, "Top")

BentShapeRebar.editBentShapeRebar(Rebar2, 50, 35, 20, 20,
                                  12, 35, 100, 155, 2, True, 6, "Top")
```


<div class="mw-translate-fuzzy">


{{docnav/de
|[L-förmiger Bewehrungsstab](Arch_Rebar_LShape/de.md)
|[Bügelförmiger Bewehrungsstab](Arch_Rebar_Stirrup/de.md)
|[Arch-Arbeitsbereich](Arch_Workbench/de.md)
|IconL=Arch_Rebar_LShape.svg
|IconR=Arch_Rebar_Stirrup.svg
|IconC=Workbench_Arch.svg
}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar BentShape/de
