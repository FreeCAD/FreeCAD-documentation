---
- GuiCommand:/it
   Name:Arch_Rebar_ColumnReinforcement
   Name/it:Armatura di pilastro
   MenuLocation:Arch → Strumenti armatura → Armatura di colonna o BIM → 3D/BIM → Reinforcement → Column Reinforcement
   Workbenches:[Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso:[Armatura elicoidale](Arch_Rebar_Helical/it.md), [Armatura di pilastro con due staffe e sei barre](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/it.md)
   Version:0.19
---

# Arch Rebar ColumnReinforcement/it


</div>

## Descrizione

Lo strumento [Armatura di pilastro](Arch_Rebar_ColumnReinforcement/it.md) consente all\'utente di creare delle barre di rinforzo all\'interno di un oggetto [Struttura](Arch_Structure/it.md) Pilastro.

The [Column Reinforcement](Arch_Rebar_ColumnReinforcement.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

Questo comando fa parte dell\'ambiente _, tramite il menu **Strumenti → Addon manager → Reinforcement**.

<img alt="" src=images/Arch_Rebar_ColumnReinforcement_example.png  style="width:400px;"> 
*Armatura di pilastro all'interno di un [Struttura](Arch_Structure/it.md) pilastro*

## Utilizzo

1\. Selezionare una faccia di un oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** creato precedentemente.
2. Quindi selezionare **<img src="images/Arch_Rebar_ColumnReinforcement.svg" width=16px> [Armatura di pilastro](Arch_Rebar_ColumnReinforcement/it.md)** dagli strumenti armatura.
3. Sullo schermo appare una finestra di dialogo come mostrato sotto.
<img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">
*Finestra di dialogo per lo strumento Armatura di pilastro*

4\. Selezionare il tipo di rinforzo.
5. Fornire gli input per i dati relativi alla staffatura.
6. Fare clic su **Avanti** per passare alla finestra di dialogo successiva.
<img alt="" src=images/ColumnReinforcementDialog_MainRebars.png  style="width:700px;">
*Finestra di dialogo per i dati dell'armatura principale*

7\. Selezionare il tipo di armatura desiderata e riempire i dati per le armature principali.
8. Fare clic su **Avanti** per passare alla finestra di dialogo successiva.
<img alt="" src=images/ColumnReinforcementDialog_XDirRebars.png  style="width:700px;">
*Finestra di dialogo per i dati Armature di direzione X.*

9\. Selezionare il tipo di armatura desiderata e compilare i dati per le armature in direzione x.
10. Fare clic su **Avanti** per passare alla finestra di dialogo successiva.
<img alt="" src=images/ColumnReinforcementDialog_YDirRebars.png  style="width:700px;">
*Finestra di dialogo per i dati Armature di direzione Y.*

11\. Selezionare il tipo di armatura desiderata e compilare i dati per le armature in direzione y.
12. Cliccare su **OK** o su **Applica** per generare il rinforzo del pilastro.
13. Cliccare su **Cancella** per uscire dalla finestra di dialogo.

## Proprietà

**Staffe:**

-    **Left Cover**: La distanza tra l\'estremità sinistra della staffa e la faccia sinistra della struttura - copriferro sul lato sinistro.

-    **Right Cover**: La distanza tra l\'estremità destra della staffa e la faccia destra della struttura - copriferro sul lato destro.

-    **Top Cover**: La distanza tra la staffa e la faccia posteriore della struttura.

-    **Bottom Cover**: La distanza tra la staffa e la faccia anteriore della struttura.

-    **Offset**: La distanza tra la staffa e la faccia superiore e inferiore della struttura.

-    **Diameter**: Diametro del tondino della staffa.

-    **Bent Angle**: L\'angolo di piega definisce l\'angolo alle estremità della staffa.

-    **Extension Factor**: Il fattore di estensione definisce la lunghezza dell\'estremità della staffa, espressa in volte il diametro.

-    **Number**: Numero di staffe.

-    **Spacing**: La distanza tra gli assi di ciascuna staffa.

**Main Rebars:** Tondini per cemento armato posizionati negli angoli della staffa

-    **Rebar Type**: Tipo di armatura principale.

-    **Hook Orientation**: Orientamento dei ganci a forma di L.

-    **Hook Extend Along**: Direzione per l\'estensione del gancio.

-    **Hook Extension**: Lunghezza del gancio delle armature a forma di L.

-    **Rounding**: Un valore di arrotondamento da applicare agli angoli delle armature a forma di L, espresso in volte il diametro.

-    **Top Offset**: La distanza tra l\'armatura e la faccia superiore della struttura.

-    **Bottom Offset**: La distanza tra l\'armatura e la faccia inferiore della struttura.

-    **Diameter**: Diametro delle armature principali.

**XDir Secondary Rebars:** Armatura lungo la direzione x esclusa l\'armatura principale.

-    **Rebar Type**: Tipo di armatura in direzione x.

-    **Hook Orientation**: Orientamento dei ganci a forma di L.

-    **Hook Extension**: Lunghezza del gancio delle armature a forma di L.

-    **Rounding**: Un valore di arrotondamento da applicare agli angoli delle armature a forma di L, espresso in volte il diametro.

-    **Top Offset**: La distanza tra l\'armatura e la faccia superiore della struttura.

-    **Bottom Offset**: La distanza tra l\'armatura e la faccia inferiore della struttura.

-    **Number#Diameter**: Numero\#Diametro del gruppo di armature in direzione x.

**YDir Secondary Rebars:** Armatura lungo la direzione y esclusa l\'armatura principale.

-    **Rebar Type**: Tipo di armatura in direzione y.

-    **Hook Orientation**: Orientamento dei ganci a forma di L.

-    **Hook Extension**: Lunghezza del gancio delle armature a forma di L.

-    **Rounding**: Un valore di arrotondamento da applicare agli angoli delle armature a forma di L, espresso in volte il diametro.

-    **Top Offset**: La distanza tra l\'armatura e la faccia superiore della struttura.

-    **Bottom Offset**: La distanza tra l\'armatura e la faccia inferiore della struttura.

-    **Number#Diameter**: Numero\#Diametro del gruppo di armature in direzione y.

## Script


**Vedere anche:**

[API Arch](Arch_API/it.md), [API Reinforcement](Reinforcement_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Armatura di pilastro può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:

### Creare una singola staffa e quattro barre 


```python
RebarGroup = makeSingleTieFourRebars(
    l_cover_of_tie,
    r_cover_of_tie,
    t_cover_of_tie,
    b_cover_of_tie,
    offset_of_tie,
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=None,
    facename=None,
).rebar_group

```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `l_cover_of_tie`, `r_cover_of_tie`, `t_cover_of_tie`, `b_cover_of_tie` and `offset_of_tie` are inner offset distances for the tie elements with respect to the faces of the structure. They are respectively the left, right, top, bottom and front/rear offsets.

-    `bent_angle`define the angle of the tip of the reinforcement loop.

-    `extension_factor`define the length of the tip of the reinforcement loop, expressed in times the diameter.

-    `dia_of_tie`is the diameter of the ties.

-    `number_spacing_check`if it is `True` it will create as many ties as given by `number_spacing_value`; if it is `False` it will create ties separated by the numerical value of `number_spacing_value`.

-    `number_spacing_value`specifies the number of ties, or the value of the separation between them, depending on `number_spacing_check`.

-    `dia_of_rebars`is the diameter of the main rebars.

-    `t_offset_of_rebars`and `b_offset_of_rebars` are inner offset distances for the main rebars with respect to the top and bottom faces of the structure, respectively.

-    `rebar_type`is the type of the main rebars; it can be `"StraightRebar"` or `"LShapeRebar"`.

-    `hook_orientation`specifies the orientation of LShaped hook; it can be: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` or `"Bottom Left"`.

-    `hook_extend_along`specifies direction for hook extension; it can be `"x-axis"` or `"y-axis"`.

-    `l_rebar_rounding`is the parameter that determines the bending radius of the LShaped main rebars, expressed as times the diameter.

-    `hook_extension`is the length of hook of LShaped rebars.

#### Esempio


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTie

# Non funziona se la struttura non si basa su una faccia
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Per armature diritte

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=Structure,
    facename="Face6",
).rebar_group

# Per barre a forma di L con gancio lungo l'asse x

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=Structure,
    facename="Face6",
).rebar_group

# Per barre a forma di L con gancio lungo l'asse y

RebarGroup = SingleTie.makeSingleTieFourRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="y-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=Structure,
    facename="Face6",
).rebar_group

```

### Creare una singola staffa e multiple barre 


```python
RebarGroup = makeSingleTieMultipleRebars(
    l_cover_of_tie,
    r_cover_of_tie,
    t_cover_of_tie,           
    b_cover_of_tie,                      
    offset_of_tie,                       
    bent_angle,                          
    extension_factor,
    dia_of_tie,     
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    main_rebars_t_offset,
    main_rebars_b_offset,
    main_rebars_type="StraightRebar",
    main_hook_orientation="Top Inside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=None,
    main_hook_extension=None,
    sec_rebars_t_offset=None,
    sec_rebars_b_offset=None,
    sec_rebars_number_diameter=None,
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=("Top Inside", "Top Inside"),
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)

```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `l_cover_of_tie`, `r_cover_of_tie`, `t_cover_of_tie`, `b_cover_of_tie` and `offset_of_tie` are inner offset distances for the tie elements with respect to the faces of the structure. They are respectively the left, right, top, bottom and front/rear offsets.

-    `bent_angle`define the angle of the tip of the reinforcement loop.

-    `extension_factor`define the length of the tip of the reinforcement loop, expressed in times the diameter.

-    `dia_of_tie`is the diameter of the ties.

-    `number_spacing_check`if it is `True` it will create as many ties as given by `number_spacing_value`; if it is `False` it will create ties separated by the numerical value of `number_spacing_value`.

-    `number_spacing_value`specifies the number of ties, or the value of the separation between them, depending on `number_spacing_check`.

-    `dia_of_main_rebars`is the diameter of the main rebars.

-    `main_rebars_t_offset`and `main_rebars_b_offset` are inner offset distances for the main rebars with respect to the top and bottom faces of the structure, respectively.

-    `main_rebars_type`is the type of the main rebars; it can be `"StraightRebar"` or `"LShapeRebar"`.

-    `main_hook_orientation`specifies the orientation of main LShaped hook; it can be: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` or `"Bottom Left"`.

-    `main_hook_extend_along`specifies direction for main hook extension; it can be `"x-axis"` or `"y-axis"`.

-    `l_main_rebar_rounding`is the parameter that determines the bending radius of the LShaped main rebars, expressed as times the diameter.

-    `main_hook_extension`is the length of hook of main LShaped rebars.

-    `sec_rebars_t_offset`and `sec_rebars_b_offset` are tuples (xdir\_rebars\_t\_offset, ydir\_rebars\_t\_offset) and (xdir\_rebars\_b\_offset, ydir\_rebars\_b\_offset) respectively, that defines inner offset distances for the secondary x-direction and y-direction rebars with respect to the top and bottom faces of the structure, respectively.

-    `sec_rebars_number_diameter`is a tuple (xdir\_rebars\_number\_diameter, ydir\_rebars\_number\_diameter) that defines number\#diameter set of the secondary x-direction and y-direction rebars, respectively.

-    `sec_rebars_type`is a tuple (xdir\_rebars\_type, ydir\_rebars\_type) that defines the type of secondary x-direction and y-direction rebars ,respectively; it can have `"StraightRebar"` or `"LShapeRebar"` as rebar type.

-    `sec_hook_orientation`is a tuple (xdir\_hook\_orientation, ydir\_hook\_orientation) that defines the orientation of secondary x-direction and y-direction LShaped hook; it can have `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` or `"Bottom Left"` as hook\_orientation.

-    `l_sec_rebar_rounding`is a tuple (l\_xdir\_rebar\_rounding, l\_ydir\_rebar\_rounding) that determines the bending radius of the LShaped secondary x-direction and y-direction LShaped rebars, expressed as times the diameter of x-direction and y-direction LShaped rebars, respectively.

-    `sec_hook_extension`is a tuple (xdir\_hook\_extension, ydir\_hook\_extension) that defines the length of hook of secondary x-direction and y-direction LShaped rebars.

#### Esempio 


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTieMultipleRebars

# Non funziona se la struttura non si basa su una faccia
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = SingleTieMultipleRebars.makeSingleTieMultipleRebars(
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    main_rebars_t_offset=-40,
    main_rebars_b_offset=-40,
    main_rebars_type="LShapeRebar",
    main_hook_orientation="Top Outside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=2,
    main_hook_extension=40,
    sec_rebars_t_offset=(-40, -40),
    sec_rebars_b_offset=(-40, -40),
    sec_rebars_number_diameter=("2#20mm+1#16mm+2#20mm", "1#20mm+1#16mm+1#20mm"),
    sec_rebars_type=("LShapeRebar", "LShapeRebar"),
    sec_hook_orientation=("Top Outside", "Top Outside"),
    l_sec_rebar_rounding=(2, 2),
    sec_hook_extension=(40, 40),
    structure=Structure,
    facename="Face6",
)

```

### Modifica di una singola staffa e quattro barre 

È possibile modificare le proprietà della staffa e delle barre con la seguente funzione:


```python
rebar_group = editSingleTieFourRebars(
    rebar_group,
    l_cover_of_tie,
    r_cover_of_tie,    
    t_cover_of_tie,           
    b_cover_of_tie,
    offset_of_tie,
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_rebars,
    t_offset_of_rebars,
    b_offset_of_rebars,
    rebar_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    structure=None,
    facename=None,
)

```

-    `rebar_group`è il gruppo di oggetti `ColumnReinforcement` creato in precedenza..

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeSingleTieFourRebars()`.

-    `structure`e `facename` possono essere omesse in modo che l\'armatura rimanga nella struttura originale..

#### Esempio 


```python
from ColumnReinforcement import SingleTie

rebar_group = SingleTie.editSingleTieFourRebars(
    rebar_group,                                
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_rebars=16,
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    rebar_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    structure=None,
    facename=None,
)

```

### Modifica di una singola staffa e multiple barre 

È possibile modificare le proprietà della staffa e delle barre con la seguente funzione:


```python
rebar_group = editSingleTieMultipleRebars(
    rebar_group,
    l_cover_of_tie,      
    r_cover_of_tie,       
    t_cover_of_tie,                       
    b_cover_of_tie,                       
    offset_of_tie,                        
    bent_angle,
    extension_factor,
    dia_of_tie,
    number_spacing_check,
    number_spacing_value,
    dia_of_main_rebars,
    main_rebars_t_offset,
    main_rebars_b_offset,
    main_rebars_type="StraightRebar",
    main_hook_orientation="Top Inside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=None,
    main_hook_extension=None,
    sec_rebars_t_offset=None,
    sec_rebars_b_offset=None,
    sec_rebars_number_diameter=None,
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=("Top Inside", "Top Inside"),
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)

```

-    `rebar_group`è il gruppo di oggetti `ColumnReinforcement` creato in precedenza.

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeSingleTieMultipleRebars()`.

-    `structure`e `facename` possono essere omesse in modo che l\'armatura rimanga nella struttura originale.

#### Esempio 


```python
from ColumnReinforcement import SingleTieMultipleRebars

rebar_group = SingleTieMultipleRebars.editSingleTieMultipleRebars(
    rebar_group,                                
    l_cover_of_tie=40,        
    r_cover_of_tie=40,
    t_cover_of_tie=40,
    b_cover_of_tie=40,
    offset_of_tie=100,
    bent_angle=135,
    extension_factor=2,
    dia_of_tie=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    main_rebars_t_offset=-40,
    main_rebars_b_offset=-40,
    main_rebars_type="LShapeRebar",
    main_hook_orientation="Top Outside",
    main_hook_extend_along="x-axis",
    l_main_rebar_rounding=2,
    main_hook_extension=40,
    sec_rebars_t_offset=(-40, -40),
    sec_rebars_b_offset=(-40, -40),
    sec_rebars_number_diameter=("2#20mm+1#16mm+2#20mm", "1#20mm+1#16mm+1#20mm"),
    sec_rebars_type=("StraightRebar", "StraightRebar"),
    sec_hook_orientation=None,
    l_sec_rebar_rounding=None,
    sec_hook_extension=None,
    structure=None,
    facename=None,
)
```


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar ColumnReinforcement/it
