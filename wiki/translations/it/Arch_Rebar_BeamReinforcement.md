---
- GuiCommand:/it
   Name:Arch_Rebar_BeamReinforcement
   Name/it:Armatura di trave
   MenuLocation:Arch → Strumenti armatura → Armatura di trave o 3D/BIM → Reinforcement → Beam Reinforcement
   Workbenches:[Reinforcement](Reinforcement_Workbench/it.md), [Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso:[Armatura di pilastro con due staffe e sei barre](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/it.md), [Armatura](Arch_Rebar/it.md)
   Version:0.19
---

# Arch Rebar BeamReinforcement/it


</div>

## Descrizione

Lo strumento [Rinforzo di trave](Arch_Rebar_BeamReinforcement/it.md) consente all\'utente di creare delle barre di rinforzo all\'interno di un oggetto [Struttura](Arch_Structure/it.md) Trave.

The [Beam Reinforcement](Arch_Rebar_BeamReinforcement.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente aggiuntivo _, tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

![](images/Arch_Rebar_BeamReinforcement_example.png )



*Rinforzo di trave all'interno di una [Struttura](Arch_Structure/it.md) trave*

## Utilizzo

1\. Seleziona la faccia destra di un oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** trave precedentemente creata, avente la lunghezza sull\'asse x. Oppure seleziona la faccia anteriore di un oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** trave precedentemente creata, avente la lunghezza sull\'asse y.

2\. Quindi selezionare **<img src="images/Arch_Rebar_ColumnReinforcement.svg" width=16px> [Rinforzo di trave](Arch_Rebar_BeamReinforcement/it.md)** dagli Strumenti armatura.

3\. Appare una finestra di dialogo come quella mostrata sotto.

:   <img alt="" src=images/BeamReinforcementDialog_Stirrups.png  style="width:700px;">



*Finestra di dialogo per lo strumento Rinforzo di trave*

4\. Selezionare il tipo desiderato di rinforzo di trave.

5\. Fornire gli input per i dati relativi alle staffe.

6\. Fare clic su **Avanti** e la finestra di dialogo viene aggiornata come mostrato di seguito.

:   <img alt="" src=images/BeamReinforcementDialog_TopRebars.png  style="width:700px;">



*Finestra di dialogo per i dati della parte superiore dell'armatura*

7\. Impostare i dati per le armature superiori.


{{ColoredParagraph|#f8f9fa|

: Per editare i valori Number#Diameter@Offset, fare clic sul pulsante **Modifica** accanto all'etichetta Number#Diameter@Offset. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_TopReinforcement_NumberDiameterOffset.png" width=500px>

: Per modificare il valore di Rebar Type, fare clic sul pulsante **Modifica** accanto all'etichetta Rebar Type. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_TopReinforcement_RebarType.png" width=300px>

: Per modificare il valore di Orientamento gancio, fare clic sul pulsante **Modifica** accanto all'etichetta Hook Orientation. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_TopReinforcement_HookOrientation.png" width=300px>

: Per modificare il valore dell'estensione del gancio, fare clic sul pulsante **Modifica** accanto all'etichetta Hook Extension. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_TopReinforcement_HookExtension.png" width=300px>

: Per modificare il valore dell'arrotondamento della barra, fare clic sul pulsante **Modifica** accanto all'etichetta Rounding. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_TopReinforcement_LRebarRounding.png" width=300px>

: Per modificare il valore di spaziatura dei livelli, fare clic sul pulsante **Modifica** accanto all'etichetta Layer Spacing. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_TopReinforcement_LayerSpacing.png" width=300px>
}}

8\. Fare clic su **Avanti** e la finestra di dialogo viene aggiornata come mostrato di seguito.

:   <img alt="" src=images/BeamReinforcementDialog_BottomRebars.png  style="width:700px;">



*Finestra di dialogo per i dati della parte inferiore dell'armatura*

9\. Impostare i dati per le armature inferiori in modo simile ai dati delle armature superiori.

10\. Fare clic su **Avanti** e la finestra di dialogo viene aggiornata come mostrato di seguito.

:   <img alt="" src=images/BeamReinforcementDialog_LeftRebars.png  style="width:700px;">



*Definire i dati per le barre di rinforzo sul lato sinistro.*

11\. Impostare i dati per le armature di taglio a sinistra.


{{ColoredParagraph|#f8f9fa|

: Per editare i valori Number#Diameter@Offset, fare clic sul pulsante **Modifica** accanto all'etichetta Number#Diameter@Offset. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_ShearReinforcement_NumberDiameterOffset.png" width=500px>

: Per modificare il valore di Rebar Type, fare clic sul pulsante **Modifica** accanto all'etichetta Rebar Type. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_ShearReinforcement_RebarType.png" width=300px>

: Per modificare il valore di Orientamento gancio, fare clic sul pulsante **Modifica** accanto all'etichetta Hook Orientation. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_ShearReinforcement_HookOrientation.png" width=300px>

: Per modificare il valore dell'estensione del gancio, fare clic sul pulsante **Modifica** accanto all'etichetta Hook Extension. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_ShearReinforcement_HookExtension.png" width=300px>

: Per modificare il valore dell'arrotondamento della barra, fare clic sul pulsante **Modifica** accanto all'etichetta Rounding. Appare una finestra di dialogo come mostrato di seguito.

:<img src="images/Beam_ShearReinforcement_LRebarRounding.png" width=300px>
}}

12\. Fare clic su **Avanti** e la finestra di dialogo viene aggiornata come mostrato di seguito.

:   <img alt="" src=images/BeamReinforcementDialog_RightRebars.png  style="width:700px;">



*Definire i dati per le barre di rinforzo sul lato destro.*

13\. Impostare i dati per le armature di taglio a destra in modo simile ai dati delle armature di taglio a sinistra.

14\. Cliccare su **OK** o su **Applica** per generare l\'armatura.

15\. Cliccare **Cancella** per uscire dalla finestra di dialogo.

## Proprietà


<div class="mw-translate-fuzzy">

**Stirrups:**

-    **Left Cover**: a distanza tra l\'estremità sinistra della staffa e la faccia sinistra della struttura - copriferro a sinistra.

-    **Right Cover**: la distanza tra l\'estremità destra della staffa e la faccia destra della struttura - copriferro a destra.

-    **Top Cover**: la distanza tra la staffa e la faccia superiore della struttura.

-    **Bottom Cover**: la distanza tra la staffa e la faccia inferiore della struttura.

-    **Offset**: la distanza tra la staffa e la faccia superiore e inferiore della struttura.

-    **Diameter**: diametro della staffa.

-    **Bent Angle**: l\'angolo dipiega definisce l\'angolo alle estremità di una staffa.

-    **Extension Factor**: il fattore di estensione definisce la lunghezza dell\'estremità della staffa, espressa in volte il diametro.

-    **Number**: il numero di staffe.

-    **Spacing**: la distanza tra gli assi di ogni staffa.


</div>

**Top/Bottom Reinforcement Rebars:** barre di armatura presenti nella parte superiore e inferiore della trave

-    **NumberDiameterOffset**: Una tupla della stringa Number\#Diameter\@Offset. Ogni elemento della tupla rappresenta il rinforzo per ogni nuovo livello.

-    **Rebar Type**: Elenco di tuple del tipo di barre di rinforzo.

-    **Hook Orientation**: Elenco di tuple di orientamento dei ganci a forma di L.

-    **Hook Extension**: Elenco di tuple di lunghezza del gancio a forma di L delle armature.

-    **Rounding**: Elenco di tuple del valore di arrotondamento da applicare agli angoli delle armature a forma di L, espresse in volte il diametro.

-    **Layer Spacing**: Elenco di spaziatura tra due strati di rinforzo consecutivi.

**Left/Right Reinforcement Rebars:** barre di armatura presenti nella parte sinistra e destra della trave

-    **NumberDiameterOffset**: Stringa di Number\#Diameter\@Offset per barre di rinforzo..

-    **Rebar Type**: Elenco dei tipi di barre di rinforzo.

-    **Hook Orientation**: Lista per l\'orientamento dei ganci a forma di L..

-    **Hook Extension**: Lista per la lunghezza del gancio a forma di L delle armature.

-    **Rounding**: Lista per il valore di arrotondamento da applicare agli angoli delle armature a forma di L, espresse in volte il diametro.

-    **Rebar Spacing**: Elenco di spaziatura tra due strati di rinforzo consecutivi.

## Script


**Vedere anche:**

[API Arch](Arch_API/it.md), [API di Reinforcement](Reinforcement_API/it.md) e [Basi di script per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Rinforzo di trave può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:

### Creare staffe con due ganci 


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

-    `top_reinforcement_number_diameter_offset`and `bottom_reinforcement_number_diameter_offset` are tuple of number\_diameter\_offset string. Each element of tuple represents reinforcement for each new layer.

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

-    `left_rebars_number_diameter_offset`and `right_rebars_number_diameter_offset` are string of number\_diameter\_offset.

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

#### Esempio


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


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar BeamReinforcement/it
