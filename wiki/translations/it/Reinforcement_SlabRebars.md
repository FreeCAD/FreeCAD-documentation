---
 GuiCommand:
   Name: Arch Rebar Slab Reinforcement
   Name/it: Armatura di soletta
   MenuLocation: Arch , Strumenti di armatura , Armatura soletta<br>3D/BIM , Reinforcement tools , Armatura soletta
   Workbenches: Arch_Workbench/it
   SeeAlso: Reinforcement_Workbench/it, Arch_Rebar/it, Arch_Rebar_Helical/it
---

# Reinforcement SlabRebars/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento [Armatura di soletta](Arch_Rebar_Slab_Reinforcement/it.md) consente all\'utente di creare barre d\'armatura all\'interno di un oggetto [Struttura](Arch_Structure/it.md) soletta.


</div>


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'[Ambiente Rinforzi](Reinforcement_Workbench/it.md), un [Ambiente complementare](External_workbenches/it.md) che può essere installato con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md) tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Un esempio di armatura all'interno di una [Struttura](Arch_Structure/it.md) soletta*

<img alt="" src=images/Right_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Vista da destra dell'esempio di armatura della soletta*

<img alt="" src=images/Front_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Vista frontale dell'esempio di armatura della soletta*



## Utilizzo

1\. Selezionare una faccia qualsiasi di un oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** Soletta creato in precedenza. come mostrato nell\'immagine qui sotto.

:   <img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Faccia selezionata per la struttura soletta*


</div>


<div class="mw-translate-fuzzy">

2\. Quindi selezionare **<img src="images/Arch_Rebar_Slab_Reinforcement.svg" width=16px> [Armatura soletta](Arch_Rebar_Slab_Reinforcement/it.md)** dagli strumenti dell\'armatura.


</div>

3\. Sullo schermo verrà visualizzata una finestra di dialogo come mostrato di seguito.

:   <img alt="" src=images/Slab_Reinforcement_input_dialog_box.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per l'armatura di soletta*


</div>

4\. Selezionare il tipo di copertura desiderata per la rete di rinforzo (Superiore o Inferiore).

5\. Selezionare il tipo di armatura desiderata e altri dati di input per le armature nella direzione parallela della faccia selezionata, come mostrato nell\'immagine sottostante.

:   <img alt="" src=images/Bent_Shape_rebars_in_parallel_with_distribution_rebars_inputs_for_Slab_Reinforcement.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per le armature della soletta in direzione parallela alla faccia selezionata*


</div>


<div class="mw-translate-fuzzy">

6\. Ora cliccare sul pulsante **Next** o selezionare Cross Rebars nella visualizzazione elenco.


</div>

7\. Ora impostare i dati desiderati nei dati di input per l\'armatura nella direzione trasversale della faccia selezionata come mostrato nell\'immagine sottostante.

:   <img alt="" src=images/Bent_Shape_rebars_in_cross_direction_with_distribution_rebars.png  style="width:600px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo delle armature di soletta nella direzione trasversale della faccia selezionata*


</div>

8\. Fare clic su **OK** o **Applica** o **Fine** per generare l\'armatura della soletta.

9\. Fare clic su **Annulla** per uscire dalla finestra di dialogo.


## Proprietà

**Proprietà delle barre d\'armatura in direzione parallela alla faccia selezionata:**

-    **Mesh Cover Along**: Rappresenta l\'allineamento della maglia dell\'armatura lungo la faccia superiore o inferiore della struttura. Può avere due valori \"Top\" e \"Bottom\".

-    **Rebar Type**: Tipo di armatura delle armature parallele per l\'armatura della soletta. Può avere quattro valori \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Front Cover**: La distanza tra l\'armatura parallela e la faccia selezionata.\* **Left Cover**: La distanza tra l\'estremità sinistra dell\'armatura parallela e la faccia sinistra della struttura.

-    **Right Cover**: La distanza tra l\'estremità destra dell\'armatura parallela e la faccia destra della struttura.

-    **Bottom Cover**: La distanza tra le armature parallele e la faccia inferiore della struttura.

-    **Top Cover**: La distanza tra le armature parallele e la faccia superiore della struttura.

-    **Rear Cover**: Copriferro posteriore per il rinforzo delle armature parallele della soletta.

-    **Anchor Length**: Rappresenta la lunghezza del braccio dell\'armatura parallela sagomata quando il tipo di armatura parallela è BentShapeRebar.

-    **Bent Angle**: Rappresenta l\'angolo per l\'armatura parallela sagomata quando il tipo di armatura parallela è BentShapeRebar.

-    **Rounding**: Un valore di arrotondamento da applicare agli spigoli delle barre, espresso in numero di volte il diametro delle barre parallele.

-    **Diameter**: Diametro delle armature parallele.

-    **Amount**: Contiene il conteggio delle armature parallele.

-    **Spacing**: Contiene il passo delle armature parallele.

**Proprietà di distribuzione delle barre d\'armatura per barre d\'armatura piegate in direzione parallela alla faccia selezionata:**

-    **Amount**: contiene il conteggio delle Armature di Ripartizione per le Armature Sagomate in direzione parallela.

-    **Spacing**: contiene il passo tra le Armature di Ripartizione per le Armature Sagomate in direzione parallela.

**Proprietà per le barre d\'armatura in direzione trasversale rispetto alla faccia selezionata:**

-    **Rebar Type**: Tipo di armatura per armature trasversali per l\'armatura della soletta. Può avere quattro valori \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **Front Cover**: La distanza tra l\'armatura trasversale e la faccia selezionata.

-    **Left Cover**: La distanza tra l\'estremità sinistra dell\'armatura trasversale e la faccia sinistra della struttura.

-    **Right Cover**: La distanza tra l\'estremità destra dell\'armatura trasversale e la faccia destra della struttura.

-    **Bottom Cover**: La distanza tra le armature trasversali e la faccia inferiore della struttura.

-    **Top Cover**: La distanza tra le armature trasversali e la faccia superiore della struttura.

-    **Rear Cover**: Copriferro posteriore per le armature trasversali di rinforzo della soletta.

-    **Anchor Length**: Rappresenta la lunghezza del braccio dell\'armatura trasversale sagomata quando il tipo di armatura trasversale è BentShapeRebar.

-    **Bent Angle**: Rappresenta l\'angolo per l\'armatura trasversale sagomata quando il tipo di armatura trasversale è BentShapeRebar.

-    **Rounding**: Un valore di arrotondamento da applicare agli spigoli delle barre, espresso numero di volte il diametro delle armature trasversali.

-    **Diameter**: Diametro delle armature trasversali

-    **Amount**: Contiene il conteggio delle armature trasversali.

-    **Spacing**: Contiene il passo delle armature trasversali.

**Proprietà di distribuzione delle barre d\'armatura per barre d\'armatura piegate in direzione trasversale rispetto alla faccia selezionata:**

-    **Amount**: contiene il conteggio delle Armature di Ripartizione per le Armature Sagomate in direzione trasversale.

-    **Spacing**: contiene il passo tra le Armature di Ripartizione per le Armature Sagomate in direzione trasversale.



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md), [API di Reinforcement](Reinforcement_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Armatura solaio può essere utilizzato dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>



### Crea Armatura di soletta 


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-   Crea un oggetto `SlabReinforcementGroup` dalla data `structure`, che è una Soletta di una [Struttura di Arch](Arch_Structure/it.md), e da una `facename`, che è una faccia di quella struttura.
    -   Se non vengono forniti `structure` né `facename`, verrà utilizzata come input la faccia selezionata dall\'utente.

**Proprietà per le barre d\'armatura in direzione parallela alla faccia selezionata:**

-    **parallel_rebar_type**: Tipo di armatura per armature parallele per l\'armatura della soletta. Può avere quattro valori \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **parallel_front_cover**: La distanza tra l\'armatura parallela e la faccia selezionata.

-    **parallel_rear_cover**: Copriferro posteriore di rinforzo per le armature parallele della soletta.

-    **parallel_left_cover**: La distanza tra l\'estremità sinistra dell\'armatura parallela e la faccia sinistra della struttura.

-    **parallel_right_cover**: La distanza tra l\'estremità destra dell\'armatura parallela e la faccia destra della struttura.

-    **parallel_top_cover**: La distanza tra le armature parallele dalla faccia superiore della struttura.

-    **parallel_bottom_cover**: La distanza tra le armature parallele dalla faccia inferiore della struttura.

-    **parallel_diameter**: Diametro delle armature parallele.

-    **parallel_amount_spacing_check**: Se è impostato su True, il valore di parallel_amount_spacing_value viene utilizzato come numero delle barre d\'armatura, altrimenti il ​​valore di parallel_amount_spacing_value viene utilizzato come spaziatura nelle barre d\'armatura parallele.

-    **parallel_amount_spacing_value**: Contiene il numero delle barre d\'armatura o il passo tra le barre d\'armatura parallele in base al valore di amount_spacing_check.

-    **parallel_rounding**: Un valore di arrotondamento da applicare agli angoli delle barre, espresso in volte il diametro_parallelo.

-    **parallel_bent_bar_length**: Rappresenta la lunghezza del braccio dell\'armatura parallela sagomata quando parallel_rebar_type è BentShapeRebar.

-    **parallel_bent_bar_angle**: Rappresenta l\'angolo per l\'armatura parallela sagomata quando parallel_rebar_type è BentShapeRebar.

-    **parallel_l_shape_hook_orintation**: Rappresenta l\'orientamento del gancio dell\'armatura parallela a forma di L se parallel_rebar_type è LShapeRebar. Può avere tre valori \"Left\", \"Right\", \"Alternate\"

-    **parallel_distribution_rebars_check**: Se True, aggiunge le armature di distribuzione per le armature sagomate parallele. L\'impostazione predefinita è False.

-    **parallel_distribution_rebars_diameter**: Diametro delle armature distribuite per le armature sagomate parallele.

-    **parallel_distribution_rebars_amount_spacing_check**: Se è impostato su True, il valore di parallel_distribution_rebars_amount_spacing_value viene utilizzato come numero delle barre d\'armatura, altrimenti il ​​valore di parallel_distribution_rebars_amount_spacing_value viene utilizzato come passo in parallel_distribution_rebars. L\'impostazione predefinita è True.

-    **parallel_distribution_rebars_amount_spacing_value**: Contiene il numero o il passo delle barre d\'armatura di distribuzione per un lato delle barre d\'armatura parallele sagomate in base al valore di parallel_distribution_rebars_check. L\'impostazione predefinita è 2.

**Proprietà per le barre d\'armatura in direzione trasversale rispetto alla faccia selezionata:**

-    **cross_rebar_type**: Tipo di armatura per le armature trasversali della soletta. Può avere quattro valori \'StraightRebar\', \'LShapeRebar\', \'UShapeRebar\', \'BentShapeRebar\'.

-    **cross_front_cover**: La distanza tra l\'armatura trasversale e cross_face (la faccia perpendicolare alla faccia selezionata).

-    **cross_rear_cover**: Copriferro posteriore per le armature trasversali di rinforzo dell\'armatura di soletta.

-    **cross_left_cover**: La distanza tra l\'estremità sinistra dell\'armatura trasversale e la faccia sinistra della struttura.

-    **cross_right_cover**: La distanza tra l\'estremità destra dell\'armatura e la faccia destra della struttura rispetto a cross_face.

-    **cross_top_cover**: La distanza dell\'armatura trasversale dalla faccia superiore della struttura.

-    **cross_bottom_cover**: La distanza dell\'armatura trasversale dalla faccia inferiore della struttura.

-    **cross_diameter**: Diametro delle armature trasversali.

-    **cross_amount_spacing_check**: Se è impostato su True, il valore di cross_amount_spacing_value viene utilizzato come numero delle barre d\'armatura, altrimenti il valore di cross_amount_spacing_value viene utilizzato come passo delle barre d\'armatura.

-    **cross_amount_spacing_value**: Contiene il numero delle armature o il passo tra le armature in base al valore di cross_amount_spacing_check.

-    **cross_rounding**: Un valore di arrotondamento da applicare agli angoli delle barre, espresso in numero di volte il cross_diameter.

-    **cross_bent_bar_length**: Rappresenta la lunghezza del braccio dell\'armatura sagomata trasversale quando cross_rebar_type è BentShapeRebar

-    **cross_bent_bar_angle**: Rappresenta l\'angolo per l\'armatura trasversale sagomata quando cross_rebar_type è BentShapeRebar

-    **cross_l_shape_hook_orintation**: Rappresenta l\'orientamento del gancio dell\'armatura trasversale a forma di L se cross_rebar_type è LShapeRebar. Può avere tre valori \"Left\", \"Right\", \"Alternate\"

-    **cross_distribution_rebars_check**: Se Vero, aggiungere le armature di distribuzione per le armature sagomate trasversali. L\'impostazione predefinita è False.

-    **cross_distribution_rebars_diameter**: Diametro delle armature di distribuzione per armature sagomate trasversali.

-    **cross_distribution_rebars_amount_spacing_check**: Se è impostato su True, il valore di cross_distribution_rebars_amount_spacing_value viene utilizzato come numero delle barre d\'armatura, altrimenti il valore di cross_distribution_rebars_amount_spacing_value viene utilizzato come passo in cross_distribution_rebars. L\'impostazione predefinita è Vero.

-    **cross_distribution_rebars_amount_spacing_value**: Contiene il numero o il passo tra le barre d\'armatura di distribuzione per un lato delle barre d\'armatura sagomate trasversali in base al valore di cross_distribution_rebars_check. L\'impostazione predefinita è 2.

**Proprietà comuni per le barre d\'armatura parallele e trasversali:**

-    **mesh_cover_along**: può avere due valori \"Top\" e \"Bottom\". Rappresenta l\'allineamento della maglia dell\'armatura lungo la faccia superiore o inferiore della struttura.

-    **structure**: oggetto struttura ad arco. L\'impostazione predefinita è None

-    **facename**: faccia selezionata della struttura. L\'impostazione predefinita è None



### Modifica delle Armature di Soletta 


<div class="mw-translate-fuzzy">

È possibile modificare le proprietà dell\'Armatura del Solaio con la seguente funzione


</div>


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
slabReinforcementGroup = editSlabReinforcement(
    slabReinforcementGroup,
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along: str = "Bottom",
    structure = None,
    facename = None,
)
```

-    `slabReinforcementGroup`è un oggetto del gruppo `Slab Reinforcement` creato in precedenza.

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeSlabReinforcement()`.



### Esempi di Armature di Soletta 

-   [Soletta che si estende in due direzioni](Example_Slab_Spanning_in_Two_Directions/it.md)

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;">

-   [Soletta che si estende in una direzione](Example_Slab_Spanning_in_One_Direction/it.md)

<img alt="" src=images/Slab_spanning_in_one_Direction.png  style="width:800px;">

-   [Soletta con rete di rinforzo con armature diritte](Example_Slab_Having_Mesh_Of_Straight_Rebars/it.md)

<img alt="" src=images/Slab_having_straight_rebars_in_both_direction.png  style="width:800px;">

-   [Soletta con rete di rinforzo con armature a forma di U](Example_Slab_Having_UShape_Rebars_Reinforcement_Mesh/it.md)

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width:800px;">

-   [Soletta con rete di rinforzo con armature a forma di L](Example_Slab_Having_LShape_Rebars_Reinforcement_Mesh/it.md)

<img alt="" src=images/L-Shape_Rebars_isometric_view.png  style="width:800px;">


<div class="mw-translate-fuzzy">





</div>

{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement SlabRebars/it
