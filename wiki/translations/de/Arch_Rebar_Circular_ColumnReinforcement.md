---
- GuiCommand:/de
   Name:Arch Rebar ColumnReinforcement
   Name/de:Architektur Bewehrung Säulenverstärkung
   MenuLocation:Arch → Bewehrungswerkzeuge
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   Version:0.19
   SeeAlso:[SäulenVerstärkung ZweiBinderSechsStäbe](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/de.md), [Arch Bewehrung](Arch_Rebar/de.md)
---

## Beschreibung

Das [Säulenverstärkung](Arch_Rebar_Circular_ColumnReinforcement/de.md) Werkzeug ermöglicht es dem Anwender, Bewehrungsstäbe innerhalb eines Stützen [Architektur Struktur](Arch_Structure/de.md) Objektes zu erzeugen.

Dieser Befehl ist Teil des [Reinforcement-Arbeitsbereichs](Reinforcement_Workbench/de.md), eines [externen Arbeitsbereichs](External_workbenches/de.md), der mit dem <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon-Manager](Addon_Manager/de.md) über das Menü **Werkzeuge → Addon-Manager → Reinforcement** installiert werden kann.

<img alt="" src=images/Arch_Rebar_Circular_ColumnReinforcement_example.png  style="width:400px;"> 
*Bewehrung Rundsäulenverstärkung innerhalb einer Stützen-[Architektur Struktur](Arch_Structure/de.md)*

## Anwendung

1\. Wähle die obere Fläche eines vorher erstellten **<img src="images/Arch_Structure.svg" width=16px> [Arch Struktur](Arch_Structure/de.md)**-Objekt.
2. Wähle dann **<img src="images/Arch_Rebar_ColumnReinforcement.svg" width=16px> [Stützen Verstärkung](Arch_Rebar_ColumnReinforcement.md)** aus den Bewehrungs-Werkzeugen.
3. Eine Dialog-Box wird sich öffnen, wie unten gezeigt.
<img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;"> 
*Dialog-Box für das Arch-Bewehrung-Säulenverstärkungs-Werkzeug*

4\. Select the Circular Column radio button in column reinforcement dialog.

<img alt="" src=images/CircularColumnReinforcementDialog.png  style="width:700px;"> 
*Dialog-Box für Bewehrung Rundsäulenverstärkung*

5\. Give inputs for data related to circular column reinforcement.
6. Click **OK** or **Apply** to generate circular column reinforcement.

7\. Klicke **Abbrechen**, um die Dialog-Box zu verlassen.

## Eigenschaften

**Spiralförmige Bewehrungsstäbe:**

-    {{PropertyData/de|Side Cover}}: Der Abstand zwischen dem Bewehrungsstab und der gekrümmten Fläche.

-    {{PropertyData/de|Top Cover}}: Der Abstand zwischen dem Bewehrungsstab und der oberen Fläche der Struktur.

-    {{PropertyData/de|Bottom Cover}}: Der Abstand zwischen dem Bewehrungsstab und der unteren Fläche der Struktur.

-    {{PropertyData/de|Pitch}}: Die Höhe einer vollständigen Helixumdrehung, gemessen parallel zu der Achse der Helix.

-    {{PropertyData/de|Diameter}}: Durchmesser des Bewehrungsstabs.

**Hauptbewehrungsstäbe:**

-    {{PropertyData/de|Top Offset}}: Der Abstand der Bewehrungsstäbe zur oberen Fläche der Struktur.

-    {{PropertyData/de|Bottom Offset}}: Der Abstand der Bewehrungsstäbe zur unteren Fläche der Struktur.

-    {{PropertyData/de|Diameter}}: Durchmesser der Hauptbewehrungsstäbe.

-    {{PropertyData/de|Number}}: Die Anzahl der Hauptbewehrungsstäbe.

-    {{PropertyData/de|Angle}}: Der Winkelabstand zwischen Spannankern(?; \"ties\").

## Skripten


**Siehe auch:**

[Architektur API](Arch_API/de.md), [Bewehrung API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Säulenverstärkungswerkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md)-Konsole mit der folgenden Funktion verwendet werden:

### Bewehrung Rundsäulenverstärkung erstellen 


```python
RebarGroup = CircularColumn.makeReinforcement(
    s_cover,
    helical_rebar_t_offset,
    helical_rebar_b_offset,
    pitch,
    dia_of_helical_rebar,
    main_rebars_t_offset,
    main_rebars_b_offset,
    dia_of_main_rebars,
    number_angle_check,
    number_angle_value,
    structure=None,
    facename=None,
)

```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `s_cover`, `helical_rebar_t_offset`, and `helical_rebar_b_offset` are inner offset distances for the helical rebar with respect to the faces of the structure. They are respectively the side, top and bottom offsets.

-    `pitch`is the parameter that determines how close or far apart each helical loop is to each other.

-    `dia_of_helical_rebar`is the diameter of the helical rebar inside the structure.

-    `main_rebars_t_offset`and `main_rebars_b_offset` are inner offset distances for the main rebars with respect to the top and bottom faces of the structure, respectively.

-    `dia_of_main_rebars`is the diameter of the main rebars.

-    `number_angle_check`if it is `True` it will create as many main rebars as given by `number_angle_value`; if it is `False` it will create main rebars at an angle of `number_spacing_value`, specified in degrees.

-    `number_angle_value`specifies the number of main rebars, or the value of the angle between the main rebars, depending on `number_angle_check`.

#### Beispiel


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import CircularColumn

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = CircularColumn.makeReinforcement(
    s_cover=20,
    helical_rebar_t_offset=40,
    helical_rebar_b_offset=40,
    pitch=50,
    dia_of_helical_rebar=8,
    main_rebars_t_offset=20,
    main_rebars_b_offset=20,
    dia_of_main_rebars=16,
    number_angle_check=True,
    number_angle_value=6,
    structure=Structure,
    facename="Face3",
).rebar_group

```

### Ändern der Bewehrung Rundsäulenverstärkung 

Du kannst die Eigenschaften der spiralförmigen und der Hauptbewehrungsstäbe mit der folgenden Funktion ändern


```python
rebar_group = editReinforcement(
    rebar_group,
    s_cover,
    helical_rebar_t_offset,
    helical_rebar_b_offset,
    pitch,
    dia_of_helical_rebar,
    main_rebars_t_offset,
    main_rebars_b_offset,
    dia_of_main_rebars,
    number_angle_check,
    number_angle_value,
    structure=None,
    facename=None,
)

```

-    `rebar_group`is a previously created `ColumnReinforcement` group object.

-   The other parameters are the same as required by the `makeSingleTieFourRebars()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.

#### Beispiel 


```python
from ColumnReinforcement import CircularColumn

rebar_group = CircularColumn.editReinforcement(
    rebar_group,
    s_cover=30,
    helical_rebar_t_offset=30,
    helical_rebar_b_offset=30,
    pitch=60,
    dia_of_helical_rebar=10,
    main_rebars_t_offset=-30,
    main_rebars_b_offset=-30,
    dia_of_main_rebars=18,
    number_angle_check=False,
    number_angle_value=45,
    structure=Structure,
    facename="Face3",
)

```










[Category:Reinforcement{{\#translation:}}](Category:Reinforcement.md)
