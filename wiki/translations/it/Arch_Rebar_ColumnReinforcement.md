---
 GuiCommand:
   Name: Arch Rebar ColumnReinforcement
   Name/it: Armatura di pilastro
   MenuLocation: Arch , Strumenti armatura , Armatura pilastro<br>3BIM , 3D/BIM , Reinforcement , Armatura pilastro
   Workbenches: Arch_Workbench/it, BIM_Workbench/it
   Version: 0.19
   SeeAlso: Reinforcement_Workbench/it, Arch_Rebar/it, Arch_Rebar_Helical/it, Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/it
---

# Arch Rebar ColumnReinforcement/it



## Descrizione

Lo strumento [Armatura di pilastro](Arch_Rebar_ColumnReinforcement/it.md) consente all\'utente di creare delle barre di rinforzo all\'interno di un oggetto [Struttura](Arch_Structure/it.md) Pilastro.

Lo strumento [Armatura di pilastro](Arch_Rebar_ColumnReinforcement/it.md) è integrato anche nell\'[Ambiente BIM](BIM_Workbench/it.md).

Questo comando fa parte dell\'ambiente [Reinforcement](Reinforcement_Workbench/it.md), un [ambiente esterno](External_workbenches/it.md) che si può installare con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr/it.md), tramite il menu **Strumenti → Addon manager → Reinforcement**.

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

-    **Number#Diameter**: Numero#Diametro del gruppo di armature in direzione x.

**YDir Secondary Rebars:** Armatura lungo la direzione y esclusa l\'armatura principale.

-    **Rebar Type**: Tipo di armatura in direzione y.

-    **Hook Orientation**: Orientamento dei ganci a forma di L.

-    **Hook Extension**: Lunghezza del gancio delle armature a forma di L.

-    **Rounding**: Un valore di arrotondamento da applicare agli angoli delle armature a forma di L, espresso in volte il diametro.

-    **Top Offset**: La distanza tra l\'armatura e la faccia superiore della struttura.

-    **Bottom Offset**: La distanza tra l\'armatura e la faccia inferiore della struttura.

-    **Number#Diameter**: Numero#Diametro del gruppo di armature in direzione y.



## Script


**Vedere anche:**

[API Arch](Arch_API/it.md), [API Reinforcement](Reinforcement_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Armatura di pilastro può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:



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

-   Crea un oggetto `RebarGroup` dalla `structure` specificata, che è una [Struttura](Arch_Structure/it.md), e dalla `facename`, che è una faccia di quella struttura.
    -   Se non vengono forniti `structure` né `facename`, verrà utilizzata la faccia selezionata dall\'utente come input.

-    `l_cover_of_tie`, `r_cover_of_tie`, `t_cover_of_tie`, `b_cover_of_tie` e `offset_of_tie` sono le distanze di offset interne degli elementi di trazione rispetto alle facce della struttura. Sono rispettivamente gli offset sinistro, destro, superiore, inferiore e anteriore/posteriore.

-    `bent_angle`definisce l\'angolo della punta del gancio di rinforzo.

-    `extension_factor`definisce la lunghezza della punta dell\'anello di rinforzo, espressa in numero di volte il diametro.

-    `dia_of_tie`è il diametro delle legature.

-   se `number_spacing_check` è `True` creerà tante legature quante sono indicate da `number_spacing_value`; se è `False` creerà un numero di legature diverso dal valore numerico di `number_spacing_value`.

-    `number_spacing_value`specifica il numero di legature di un dato valore, o il valore della distanza tra loro, a seconda di `number_spacing_check`.

-    `dia_of_rebars`è il diametro delle armature principali.

-    `t_offset_of_rebars`e `b_offset_of_rebars` sono le distanze di offset interne per le armature principali rispetto alle facce superiore e inferiore della struttura, rispettivamente.

-    `rebar_type`è il tipo delle armature principali; può essere `"StraightRebar"` o `"LShapeRebar"`.

-    `hook_orientation`specifica l\'orientamento del gancio a forma di L; può essere: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, {{ incode\|\"Top Right\"}}, `"Top Left"`, `"Bottom Right"` o `"Bottom Left"`.

-    `hook_extend_along`specifica la direzione per l\'estensione del gancio; può essere `"asse x"` o `"asse y"`.

-    `l_rebar_rounding`è il parametro che determina il raggio di curvatura delle armature principali a forma di L, espresso come multipli del diametro.

-    `hook_extension`è la lunghezza del gancio delle armature a forma di L.



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

-   Crea un oggetto `RebarGroup` dalla `structure` specificata, che è una [Struttura](Arch_Structure/it.md), e dalla `facename`, che è una faccia di quella struttura.
    -   Se non vengono forniti `structure` né `facename`, verrà utilizzata la faccia selezionata dall\'utente come input.

-    `l_cover_of_tie`, `r_cover_of_tie`, `t_cover_of_tie`, `b_cover_of_tie` e `offset_of_tie` sono le distanze di offset interne degli elementi di tiraggio rispetto alle facce della struttura. Sono rispettivamente gli offset sinistro, destro, superiore, inferiore e anteriore/posteriore.

-    `bent_angle`definisce l\'angolo della punta del gancio di rinforzo.

-    `extension_factor`definisce la lunghezza della punta dell\'anello di rinforzo, espressa in numero di volte il diametro.

-    `dia_of_tie`è il diametro delle legature.

-   Se `number_spacing_check` è `True` creerà tante legature quante sono indicate da `number_spacing_value`; se è `False` creerà un numero di legature diverso dal valore numerico di `number_spacing_value`.

-    `number_spacing_value`specifica il numero di legature di un dato valore, o il valore della distanza tra loro, a seconda di `number_spacing_check`.

-    `dia_of_main_rebars`è il diametro delle armature principali.

-    `main_rebars_t_offset`e `main_rebars_b_offset` sono le distanze di offset interne per le armature principali rispetto alle facce superiore e inferiore della struttura, rispettivamente.

-    `main_rebars_type`è il tipo delle armature principali; può essere `"StraightRebar"` o `"LShapeRebar"`.

-    `main_hook_orientation`specifica l\'orientamento del gancio a forma di L; può essere: `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, `"Top Right"`, `"Top Left"`, `"Bottom Right"` o `"Bottom Left"`.

-    `main_hook_extend_along`specifica la direzione per l\'estensione del gancio; può essere `"x-axis"` o `"y-axis"`.

-    `l_main_rebar_rounding`è il parametro che determina il raggio di curvatura delle armature principali a forma di L, espresso come multipli del diametro.

-    `main_hook_extension`è la lunghezza del gancio delle armature a forma di L.

-    `sec_rebars_t_offset`e `sec_rebars_b_offset` sono tuple (xdir_rebars_t_offset, ydir_rebars_t_offset) e (xdir_rebars_b_offset, ydir_rebars_b_offset) rispettivamente, che definiscono le distanze di offset interne per le barre secondarie in direzione x e y secondo rispettivamente le facce superiore e inferiore della struttura.

-    `sec_rebars_number_diameter`è una tupla (xdir_rebars_number_diameter, ydir_rebars_number_diameter) che definisce l\'insieme numero#diametro delle armature secondarie nella direzione x e nella direzione y, rispettivamente.

-    `sec_rebars_type`è una tupla (xdir_rebars_type, ydir_rebars_type) che definisce rispettivamente il tipo di armature secondarie nella direzione x e nella direzione y; può avere `"StraightRebar"` o `"LShapeRebar"` come tipo di armatura.

-    `sec_hook_orientation`è una tupla (xdir_hook_orientation, ydir_hook_orientation) che definisce l\'orientamento del gancio a forma di L della direzione x secondaria e della direzione y; può avere `"Top Inside"`, `"Top Outside"`, `"Bottom Inside"`, `"Bottom Outside"`, {{incode |"Top Right"}}, `"Top Left"`, `"Bottom Right"` o `"Bottom Left"` come orientamento del gancio.

-    `l_sec_rebar_rounding`è una tupla (l_xdir_rebar_rounding, l_ydir_rebar_rounding) che determina il raggio di piegatura delle barre d\'armatura secondarie a forma di L nella direzione x e nella direzione y, espresso come multiplo del diametro delle barre d\'armatura a forma di L nella direzione x e nella direzione y, rispettivamente.

-    `sec_hook_extension`è una tupla (xdir_hook_extension, ydir_hook_extension) che definisce la lunghezza del gancio delle armature secondarie a forma di L nella direzione x e nella direzione y.



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



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar ColumnReinforcement/it
