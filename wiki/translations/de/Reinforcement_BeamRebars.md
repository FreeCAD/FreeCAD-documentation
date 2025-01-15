---
 GuiCommand:
   Name: Reinforcement BeamRebars
   Name/de: Reinforcement Balkenbewehrung
   MenuLocation: 3D/BIM , Bewehrungswerkzeuge , Balkenbewehrung
   Workbenches: Reinforcement_Workbench/de, BIM_Workbench/de
   Version: 0.19
   SeeAlso: 
---

# Reinforcement BeamRebars/de



## Beschreibung

Das Werkzeug [Reinforcement Balkenbewehrung](Reinforcement_BeamRebars/de.md) erlaubt dem Anwender Bewehrungsstäbe innerhalb eines Balkenobjekts ([Arch-Struktur](Arch_Structure/de.md)-Objekt) zu erzeugen.

Dieses Werkzeug ist Teil des Arbeitsbereichs [Reinforcement](Reinforcement_Workbench/de.md); dieser ist ein [externer Arbeitsbereich](External_workbenches/de.md), der mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden kann.

![](images/Arch_Rebar_BeamReinforcement_example.png ) 
*Balkenbewehrung innerhalb eines Balkens ([Arch Struktur](Arch_Structure/de.md))*



## Anwendung

1\. Wähle die rechte Seite eines zuvor erstellten Balkenobjekts **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** mit einer Länge entlang der x-Achse. Oder wähle die Vorderseite eines zuvor erstellten Balkenobjekts **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** mit einer Länge entlang der y-Achse.

2\. Dann **<img src="images/Reinforcement_ColumnRebars.svg" width=16px> [Stützenbewehrung](Reinforcement_ColumnRebars/de.md)** in den Armierungswerkzeugen auswählen.

3\. Eine Dialog-Box wird sich öffnen, wie unten gezeigt.

:   <img alt="" src=images/BeamReinforcementDialog_Stirrups.png  style="width:700px;">

:   
    
*Dialogfeld für das Werkzeug „Bewehrungsstäbe“*
    

4\. Wähle die gewünschte Art der Stützenbewehrung aus.

5\. Gib Eingaben für Daten zu Bindungen ein.

6\. Klicke auf **Weiter** und das Dialogfeld wird wie unten gezeigt aktualisiert.

:   <img alt="" src=images/BeamReinforcementDialog_TopRebars.png  style="width:700px;">

:   
    
*Dialogfeld für Daten zu oberen Bewehrungsstäben*
    

7\. Daten für obere Bewehrungsstäbe festlegen.


{{ColoredParagraph|#f8f9fa|

: Um den Wert „Number#Diameter@Offset“ zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Beschriftung „Number#Diameter@Offset“. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_TopReinforcement_NumberDiameterOffset.png" width=500px>

: Um den Wert für den Bewehrungstyp zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Beschriftung für den Bewehrungstyp. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_TopReinforcement_RebarType.png" width=300px>

: Um den Wert für die Hakenausrichtung zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Beschriftung für die Hakenausrichtung. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_TopReinforcement_HookOrientation.png" width=300px>

: Um den Wert der Hook-Erweiterung zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Bezeichnung der Hook-Erweiterung. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_TopReinforcement_HookExtension.png" width=300px>

: Um den Rundungswert für LRebar zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Rundungsbezeichnung. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_TopReinforcement_LRebarRounding.png" width=300px>

: Um den Wert für den Ebenenabstand zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Beschriftung „Ebenenabstand“. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_TopReinforcement_LayerSpacing.png" width=300px>
}}

8\. Klicke auf **Weiter** und das Dialogfeld wird wie unten gezeigt aktualisiert.

:   <img alt="" src=images/BeamReinforcementDialog_BottomRebars.png  style="width:700px;">

:   
    
*Dialogfeld für Daten zu unteren Bewehrungsstäben*
    

9\. Lege die Daten für die unteren Bewehrungsstäbe ähnlich den Daten für die oberen Bewehrungsstäbe fest.

10\. Klicke auf **Weiter** und das Dialogfeld wird wie unten gezeigt aktualisiert.

:   <img alt="" src=images/BeamReinforcementDialog_LeftRebars.png  style="width:700px;">

:   
    
*Dialogfeld für Daten zu Bewehrungsstäben mit linker Scherung*
    

11\. Daten für linksseitige Scherbewehrungsstäbe festlegen.


{{ColoredParagraph|#f8f9fa|

: Um den Wert „Number#Diameter@Offset“ zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Beschriftung „Number#Diameter@Offset“. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_ShearReinforcement_NumberDiameterOffset.png" width=500px>

: Um den Wert für den Bewehrungstyp zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Beschriftung für den Bewehrungstyp. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_ShearReinforcement_RebarType.png" width=300px>

: Um den Wert für die Hakenausrichtung zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Beschriftung für die Hakenausrichtung. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_ShearReinforcement_HookOrientation.png" width=300px>

: Um den Wert der Hook-Erweiterung zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Bezeichnung der Hook-Erweiterung. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_ShearReinforcement_HookExtension.png" width=300px>

: Um den Rundungswert für LRebar zu bearbeiten, klicke auf die Schaltfläche **Bearbeiten** neben der Rundungsbezeichnung. Ein Dialogfeld wie unten gezeigt wird eingeblendet.

: <img src="images/Beam_ShearReinforcement_LRebarRounding.png" width=300px>
}}

12\. Klicke auf **Weiter** und das Dialogfeld wird wie unten gezeigt aktualisiert.

:   <img alt="" src=images/BeamReinforcementDialog_RightRebars.png  style="width:700px;">

:   
    
*Dialogfeld für Daten zu Bewehrungsstäben mit rechter Scherung*
    

13\. Lege die Daten für Bewehrungsstäbe mit rechter Scherung ähnlich den Daten für Bewehrungsstäbe mit linker Scherung fest.

14\. Klicke auf **OK** oder **Übernehmen**, um die Balkenbewehrung zu erzeugen.

15\. **Abbrechen** anklicken, um die Dialog-Box zu verlassen.



## Eigenschaften

**Bügel:**

-    **Linke Abdeckung**: Der Abstand zwischen dem linken Ende des Bügels und der linken Seite der Struktur.

-    **Rechte Abdeckung**: Der Abstand zwischen dem rechten Ende des Bügels und der rechten Seite der Struktur.

-    **Obere Abdeckung**: Der Abstand zwischen dem Bügel und der oberen Seite der Struktur.

-    **Untere Abdeckung**: Der Abstand zwischen dem Bügel und der unteren Seite der Struktur.

-    **Versatz**: Der Abstand zwischen dem Bügel und der ausgewählten/hinteren Seite der Struktur.

-    **Durchmesser**: Durchmesser des Bügels.

-    **Biegewinkel**: Der Biegungswinkel definiert den Winkel an den Enden eines Bügels.

-    **Verlängerungsfaktor**: Der Verlängerungsfaktor definiert die Länge des Bügelendes, ausgedrückt als multipliziert mit dem Durchmesser.

-    **Nummer**: Die Nummer des Bügels.

-    **Spacing**: Der Abstand zwischen den Achsen jedes Bügels.

**Obere/untere Bewehrungsstäbe:** An der Ober-/Unterseite des Balkens vorhandene Bewehrungsstäbe

-    **NumberDiameterOffset**: Ein Tupel aus der Zeichenfolge Number#Diameter@Offset. Jedes Element des Tupels stellt die Bewehrung für jede neue Schicht dar.

-    **Rebar Type**: Liste von Tupeln mit Bewehrungsstabtypen.

-    **Hook Orientation**: Liste von Tupeln mit der Ausrichtung von L-förmigen Haken.

-    **Hook Extension**: Liste von Tupeln mit der Länge des Hakens von L-förmigen Bewehrungsstäben.

-    **Rounding**: Liste von Tupeln mit einem Rundungswert, der auf die Ecken der L-förmigen Bewehrungsstäbe angewendet werden soll, ausgedrückt als multipliziert mit dem Durchmesser.

-    **Layer Spacing**: Liste mit dem Abstand zwischen zwei aufeinanderfolgenden Bewehrungsschichten.

**Linke/rechte Bewehrungsstäbe:** Bewehrungsstäbe auf der linken/rechten Seite des Balkens vorhanden

-    **NumberDiameterOffset**: Zeichenfolge mit Number#Diameter@Offset für Bewehrungsstäbe.

-    **Bewehrungsstabtyp**: Liste der Bewehrungsstabtypen.

-    **Hakenausrichtung**: Liste der Ausrichtung von L-förmigen Haken.

-    **Hakenverlängerung**: Liste der Hakenlängen von L-förmigen Bewehrungsstäben.

-    **Rundung**: Liste eines Rundungswerts, der auf die Ecken der L-förmigen Bewehrungsstäbe angewendet werden soll, ausgedrückt als multipliziert mit dem Durchmesser.

-    **Bewehrungsstababstand**: Freier Abstand zwischen aufeinanderfolgenden Bewehrungsstäben.



## Skripten


**Siehe auch:**

[Architektur API](Arch_API/de.md), [Bewehrung API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug „Reinforcement BeamRebars" kann in [Makros](Makros/de.md) und von der [Python](Python/de.md)-Konsole aus mithilfe der folgenden Funktion verwendet werden:



### Zweibeinige Bügel erstellen 


```python
RebarGroup = makeReinforcement(
    l_cover_of_stirrup,
    r_cover_of_stirrup,
    t_cover_of_stirrup,
    b_cover_of_stirrup,
    offset_of_stirrup,
    bent_angle,
    extension_factor,
    dia_of_stirrup,
    number_spacing_check,
    number_spacing_value,
    top_reinforcement_number_diameter_offset,
    top_reinforcement_rebar_type,
    top_reinforcement_layer_spacing,
    bottom_reinforcement_number_diameter_offset,
    bottom_reinforcement_rebar_type,
    bottom_reinforcement_layer_spacing,
    left_rebars_number_diameter_offset,
    left_rebars_type,
    left_rebars_spacing,
    right_rebars_number_diameter_offset,
    right_rebars_type,
    right_rebars_spacing,
    top_reinforcement_l_rebar_rounding=2,
    top_reinforcement_hook_extension=40,
    top_reinforcement_hook_orientation="Front Inside",
    bottom_reinforcement_l_rebar_rounding=2,
    bottom_reinforcement_hook_extension=40,
    bottom_reinforcement_hook_orientation="Front Inside",
    left_l_rebar_rounding=2,
    left_rebars_hook_extension=40,
    left_rebars_hook_orientation="Front Inside",
    right_l_rebar_rounding=2,
    right_rebars_hook_extension=40,
    right_rebars_hook_orientation="Front Inside",
    structure=None,
    facename=None,
)
```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `l_cover_of_stirrup`, `r_cover_of_stirrup`, `t_cover_of_stirrup`, `b_cover_of_stirrup` and `offset_of_stirrup` are inner offset distances for the stirrup elements with respect to the faces of the structure. They are respectively the left, right, top, bottom and front/rear offsets.

-    `bent_angle`define the angle of the tip of the reinforcement loop of stirrup.

-    `extension_factor`define the length of the tip of the reinforcement loop of stirrup, expressed in times the diameter.

-    `dia_of_stirrup`is the diameter of the stirrup.

-    `number_spacing_check`if it is `True` it will create as many stirrup as given by `number_spacing_value`; if it is `False` it will create stirrup separated by the numerical value of `number_spacing_value`.

-    `number_spacing_value`specifies the number of stirrups, or the value of the separation between them, depending on `number_spacing_check`.

-    `top_reinforcement_number_diameter_offset`and `bottom_reinforcement_number_diameter_offset` are tuple of number_diameter_offset string. Each element of tuple represents reinforcement for each new layer.

   Syntax: (
               "number1#diameter1@offset1+number2#diameter2@offset2+...",
               "number3#diameter3@offset3+number4#diameter4@offset4+...",
               ...,
           )

-    `top_reinforcement_rebar_type`and `bottom_reinforcement_rebar_type` specifies type of top/bottom reinforcement bars.

   Possible values:
   1. 'StraightRebar' or 'LShapeRebar'
', ...) and number of elements of tuple must be equal to number of reinforcement
      layers.
   3. [
', ...),
', ...),
          ...,
      ]
      each element of list is a tuple, which specifies rebar type of each reinforcement layer. And each element of
      tuple represents rabar_type for each set of rebars.
   4. [
,
', ...),
          ...,
      ]

-    `top_reinforcement_layer_spacing`and `bottom_reinforcement_layer_spacing` is the spacing between two consecutive reinforcement layers.

   Possible values:

, ...) and number of elements of tuple must be
      equal to one less than number of layers.

-    `left_rebars_number_diameter_offset`and `right_rebars_number_diameter_offset` are string of number_diameter_offset.

   Syntax: "number1#diameter1@offset1+number2#diameter2@offset2+..."

-    `left_rebars_type`and `right_rebars_type` specifies type of left/right reinforcement bars.

   Possible values:
   1. 'StraightRebar' or 'LShapeRebar'
', ...) and each element of tuple represents rabar_type for each set of rebars.

-    `left_rebars_spacing`and `right_rebars_spacing` is clear spacing between consecutive reinforcement bars.

-    `top_reinforcement_l_rebar_rounding`and `bottom_reinforcement_l_rebar_rounding` is the parameter that determines the bending radius of the LShaped top/bottom rebars, expressed as times the diameter. Possible syntax are similar to as discussed above for `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `top_reinforcement_hook_extension`and `bottom_reinforcement_hook_extension` is the length of hook of LShaped rebars. Possible syntax are similar to as discussed above for `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `top_reinforcement_hook_orientation`and `bottom_reinforcement_hook_orientation` specifies the orientation of LShaped hook; it can be `"Front Inside"`, `"Front Outside"`, `"Rear Inside"` or `"Rear Outside"`. Possible syntax are similar to as discussed above for `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `left_l_rebar_rounding`and `right_l_rebar_rounding` is the parameter that determines the bending radius of the LShaped left/right rebars, expressed as times the diameter. Possible syntax are similar to as discussed above for `left_rebars_type` / `right_rebars_type`.

-    `left_rebars_hook_extension`and `right_rebars_hook_extension` is the length of hook of LShaped rebars. Possible syntax are similar to as discussed above for `left_rebars_type` / `right_rebars_type`.

-    `left_rebars_hook_orientation`and `right_rebars_hook_orientation` specifies the orientation of LShaped hook; it can be `"Front Inside"`, `"Front Outside"`, `"Rear Inside"` or `"Rear Outside"`. Possible syntax are similar to as discussed above for `left_rebars_type` / `right_rebars_type`.

#### Example


```python
import FreeCAD, Arch
from BeamReinforcement import TwoLeggedBeam

Structure = Arch.makeStructure(length=3000.0,width=200.0,height=400.0)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = TwoLeggedBeam.makeReinforcement(
    l_cover_of_stirrup=20,
    r_cover_of_stirrup=20,
    t_cover_of_stirrup=20,
    b_cover_of_stirrup=20,
    offset_of_stirrup=100,
    bent_angle=135,
    extension_factor=4,
    dia_of_stirrup=8,
    number_spacing_check=False,
    number_spacing_value=200,
    top_reinforcement_number_diameter_offset=("1#20@-60+2#16@-60+1#20@-60", "3#16@-100"),
    top_reinforcement_rebar_type="LShapeRebar",
    top_reinforcement_layer_spacing=30,
    bottom_reinforcement_number_diameter_offset=("1#20@-60+2#16@-60+1#20@-60", "3#16@-100"),
    bottom_reinforcement_rebar_type="LShapeRebar",
    bottom_reinforcement_layer_spacing=30,
    left_rebars_number_diameter_offset="1#16@-100+1#16@-100+1#16@-100",
    left_rebars_type="LShapeRebar",
    left_rebars_spacing=30,
    right_rebars_number_diameter_offset="1#16@-100+1#16@-100+1#16@-100",
    right_rebars_type="LShapeRebar",
    right_rebars_spacing=30,
    top_reinforcement_l_rebar_rounding=2,
    top_reinforcement_hook_extension=100,
    top_reinforcement_hook_orientation="Rear Outside",
    bottom_reinforcement_l_rebar_rounding=2,
    bottom_reinforcement_hook_extension=100,
    bottom_reinforcement_hook_orientation="Rear Outside",
    left_l_rebar_rounding=2,
    left_rebars_hook_extension=80,
    left_rebars_hook_orientation=("Rear Inside", "Front Inside", "Rear Inside"),
    right_l_rebar_rounding=2,
    right_rebars_hook_extension=80,
    right_rebars_hook_orientation=("Front Inside", "Rear Inside", "Front Inside"),
    structure=Structure,
    facename="Face6",
)
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement BeamRebars/de
