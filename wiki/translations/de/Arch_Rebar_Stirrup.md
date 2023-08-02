---
- GuiCommand:
   Name: Arch_Rebar_Stirrup   Name/de: Arch Bewehrungsstab bügelförmig
   MenuLocation: Arch -> Rebar tools -> Stirrup oder 3D/BIM -> Reinforcement tools -> Bügel
   Workbenches: Arch_Workbench/de, BIM_Workbench/de
   Version: 0.17
   SeeAlso: Reinforcement_Workbench/de, Arch_Rebar/de, Arch_Rebar_Helical/de
---

# Arch Rebar Stirrup/de


</div>



## Beschreibung

Das [Bügelförmiger Bewehrungsstab](Arch_Rebar_Stirrup/de.md)-Werkzeug erlaubt es dem Anwender, einen Satz von bügelförmigen Bewehrungsstäben in einem [Struktur](Arch_Structure/de.md)-Objekt zu erstellen.

Das [Arch Bügelförmiger Bewehrungsstab](Arch_Rebar_Stirrup/de.md)-Werkzeug ist auch im [BIM-Arbeitsbereich](BIM_Workbench/de.md) integriert.

Dieser Befehl ist Teil des Arbeitsbereichs [Reinforcement](Reinforcement_Workbench/de.md), einem [externen Arbeitsbereich](External_workbenches/de.md), der mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) über das Menü **Werkzeuge → Addon-Manager → Reinforcement** installiert werden kann.

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;"> 
*Ein Satz von bügelförmigen Bewehrungsstäben in einem [Struktur](Arch_Structure/de.md)*-Objekt



## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle eine beliebige Fläche eines vorher erstellten **<img src="images/Arch_Structure.svg" width=16px> [Struktur](Arch_Structure/de.md)**-Objekts.
2.  Wähle dann **<img src="images/Arch_Rebar_Stirrup.svg" width=16px> [Bügelförmiger Bewehrungsstab](Arch_Rebar_Stirrup/de.md)** aus den Bewehrungsstab-Werkzeugen.
3.  Ein [Aufgaben-Paneel](Task_panel/de.md) wird auf der linken Seite des Bildschirm angezeigt wie im folgenden Bild dargestellt.
4.  Wähle die gewünschte Ausrichtung.
5.  Fülle die Werte wie \'Left Cover\' (linke Fläche), \'Right Cover\' (rechte), \'Top Cover\' (obere), \'Bottom Cover\' (untere), \'Front Cover\' (vordere), \'Anchor length\' (Ankerlänge), \'Bent Angle\' (Biegungswinkel), \'Bent Factor\', \'Rounding\' und \'Diameter\' (Durchmesser) des Bewehrungsstabes.
6.  Wähle den Verteilungsmodus, entweder `'Amount'` (Menge) oder `'Spacing'` (Abstand).
7.  Falls \'Spacing\' gewählt wurde, kann auch [benutzerdefinierter Abstand](Custom_Spacing/de.md) gewählt werden.
8.  Wähle **Pick selected face** zur Überprüfung oder ändere die Fläche zur Verteilung der Bewehrungsstäbe.
9.  Klicke **OK** oder **Anwenden** zur Erzeugung der Bewehrungsstäbe.
10. Klicke **Abbrechen** zum Verlassen des Aufgaben-Paneels.


</div>


:   <img alt="" src=images/StirrupDialog.png  style="width:250px;">



*Aufgaben-Ansicht für das Arch Bewehrungsstab bügelförmig-Werkzeug*



## Eigenschaften

-    {{PropertyData/de|Front Cover}}: Der Abstand zwischen Bewehrungsstab und ausgewählter Fläche.

-    {{PropertyData/de|Right Cover}}: Der Abstand zwischen dem rechten Ende des Bewehrungsstabs und der rechten Fläche der Struktur.

-    {{PropertyData/de|Left Cover}}: Der Abstand zwischen dem linken Ende des Bewehrungsstabs und der linken Fläche der Struktur.

-    {{PropertyData/de|Bottom Cover}}: Der Abstand zwischen dem Bewehrungsstab und der unteren Fläche der Struktur.

-    {{PropertyData/de|Top Cover}}: Der Abstand zwischen dem Bewehrungsstab und der oberen Fläche der Struktur.

-    {{PropertyData/de|Bent Angle}}: Definiert den Winkel zwischen den Enden eines Bügels.

-    {{PropertyData/de|Bent Factor}}: Definiert die Länge des Bügelendes.

-    {{PropertyData/de|Amount}}: Die Anzahl von Bewehrungsstäben.

-    {{PropertyData/de|Spacing}}: Der Abstand zwischen den Achsen jedes Bewehrungsstabs.




<div class="mw-translate-fuzzy">

## Scripten


**Siehe auch:**

[Arch API](Arch_API/de.md),[Reinforcement-API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Das Bügelförmiger Bewehrungsstab-Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole heraus durch folgende Funktion angesprochen werden:


</div>


```python
Rebar = makeStirrup(l_cover, r_cover, t_cover, b_cover, f_cover,
                    bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
                    structure=None, facename=None)
```

-   Erstellt ein `Rebar`-Objekt aus der angegebenen `structure`, die ein [Bauelement](Arch_Structure/de.md) ist und `facename`, das eine Fläche dieser Struktur ist.
    -   Falls weder `structure` noch `facename` angegeben werden, wird die vom Benutzer ausgewählte Fläche als Eingabe verwendet.

-    `l_cover`, `r_cover`, `t_cover`, `b_cover` und `f_cover` sind innere Abstände zwischen den Bewehrungsstab-Elementen bezogen auf die Flächen der Struktur. Es sind die linken, rechten, oberen, unteren und vorderen Abstände.

-    `diameter`ist der Durchmesser der Verstärkungsstäbe innerhalb der Stuktur.

-    `rounding`ist der Parameter, der den Biegeradius der Verstärkungsstäbe bei einer Windung.

-    `bentLength`und `bentAngle` definieren Länge und Winkel der Spitze der Verstärkungswindung.

-    `amount_spacing_check`, falls `True` werden soviele Windungen erzeugt wie durch `amount_spacing_value` angegeben; falls `False` werden Windungen im Abstand des numerischen Werts von `amount_spacing_value` erzeugt.

-    `amount_spacing_value`gibt die Anzahl der Verstärkungswindungen an oder den Wert des Abstand zwischen ihnen, abhängig von `amount_spacing_check`.



### Beispiel


```python
import Draft, Arch, Stirrup

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = Stirrup.makeStirrup(20, 20, 20, 20, 20,
                            115, 4, 8, 2, True, 10, Structure, "Face6")
```

### Anpassung des Bewehrungsstabs 

Die Eigenschaften des Bewehrungsstabs lassen sich mit der folgenden Funktion verändern 
```python
editStirrup(Rebar, l_cover, r_cover, t_cover, b_cover, f_cover,
            bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
            structure=None, facename=None)
```

-    `Rebar`ist ein vorher erzeugtes `StirrupRebar`-Objekt.

-   Die anderen Parameter sind die gleichen wie die für die `makeStirrup()`-Funktion erforderlichen.

-    `structure`und `facename` können weggelassen werden, so dass die Bewehrung in der ursprünglichen Struktur bleibt.


```python
import Stirrup

Stirrup.editStirrup(Rebar, 20, 20, 20, 20, 50,
                    100, 4, 14, 8, True, 8)
```


<div class="mw-translate-fuzzy">


{{docnav/de
|[Abgewinkelter Bewehrungsstab](Arch_Rebar_BentShape/de.md)
|[Spiralförmiger Bewehrungsstab](Arch_Rebar_Helical/de.md)
|[Arch-Arbeitsbereich](Arch_Workbench/de.md)
|IconL=Arch_Rebar_BentShape.svg
|IconR=Arch_Rebar_Helical.svg
|IconC=Workbench_Arch.svg
}}


</div>



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Stirrup/de
