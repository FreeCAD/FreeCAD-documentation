---
 GuiCommand:
   Name: Arch Rebar ColumnReinforcement
   Name/it: Armatura di colonna
   MenuLocation: Reinforcement , Column Reinforcement, Arch , Strumenti armatura
   Workbenches: Arch_Workbench/it, BIM_Workbench/it
   Version: 0.19
   SeeAlso: Reinforcement_Workbench/it, Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/it, Arch_Rebar/it
---

# Reinforcement ColumnRebars Circular/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento [Armatura di colonna](Arch_Rebar_Circular_ColumnReinforcement/it.md) consente all\'utente di creare delle barre di rinforzo all\'interno di un oggetto [Struttura](Arch_Structure/it.md) Colonna.


</div>


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente aggiuntivo [Reinforcement](Reinforcement_Workbench/it.md), che si può installare con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr/it.md), tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

Three usage examples are available:

-   [Single tie rectangular column](Reinforcement_ColumnRebars.md)
-   [Two ties six rebars rectangular column](Reinforcement_ColumnRebars_TwoTiesSixRebars.md)
-   [Circular column (see below)](#Usage.md)

<img alt="" src=images/Arch_Rebar_Circular_ColumnReinforcement_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Rinforzo di colonna all'interno di una [Struttura](Arch_Structure/it.md) colonna*


</div>



## Utilizzo

1\. Select top face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object.

2\. Then select **<img src="images/Reinforcement_ColumnRebars.svg" width=16px> [Column Reinforcement](Reinforcement_ColumnRebars.md)** from the rebar tools.

3\. A dialog box will pop-out on screen as shown below.

:   <img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per lo strumento Armatura di colonna*


</div>

4\. Select the Circular Column radio button in column reinforcement dialog.

:   <img alt="" src=images/CircularColumnReinforcementDialog.png  style="width:700px;">


<div class="mw-translate-fuzzy">



*Finestra di dialogo per l'armatura della colonna circolare*


</div>

5\. Give inputs for data related to circular column reinforcement.

6\. Click **OK** or **Apply** to generate circular column reinforcement.

7\. Click **Cancel** to exit the dialog box.



## Proprietà

**Helical Rebars:**


<div class="mw-translate-fuzzy">

**Helical Rebars:**

-    {{PropertyData/it|Side Cover}}: La distanza tra l\'armatura e la faccia curva.

-    {{PropertyData/it|Top Cover}}: La distanza tra l\'armatura e la parte superiore della struttura. Copriferro superiore

-    {{PropertyData/it|Bottom Cover}}: La distanza tra l\'armatura e la parte inferiore della struttura. Copriferro inferiore

-    {{PropertyData/it|Pitch}}: Il passo dell\'elica, che è l\'altezza di un giro completo di elica, misurato parallelo all\'asse dell\'elica.

-    {{PropertyData/it|Diameter}}: Diametro della barra elicoidale.


</div>

**Main Rebars:**


<div class="mw-translate-fuzzy">

**Main Rebars:**

-    **Top Offset**: La distanza tra l\'armature e la faccia superiore della struttura.

-    **Bottom Offset**: La distanza tra l\'armature e la faccia inferiore della struttura.

-    **Diameter**: Diametro delle armature principali.

-    **Number**: Il numero di armature principali.

-    **Angle**: La distanza angolare tra le legature.


</div>



## Script


**Vedere anche:**

[API Arch](Arch_API/it.md), [API di Reinforcement](Reinforcement_API/it.md) e [Basi di script per FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Armatura di colonna può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>



### Creare una armatura di colonna 


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

-   Crea un oggetto `RebarGroup` dalla `structure` data, che è una [Arch Structure](Arch_Structure/it.md), e `facename`, che è una faccia di quella struttura .
    -   Se non vengono forniti né `structure` né `facename`, verrà utilizzata la faccia selezionata dall\'utente come input.

-    `s_cover`, `helical_rebar_t_offset` e `helical_rebar_b_offset` sono le distanze di offset interne per l\'armatura elicoidale rispetto alle facce della struttura. Sono rispettivamente gli offset laterale, superiore e inferiore.

-    `pitch`è il parametro che determina quanto vicini o distanti sono tra loro ciascun anello elicoidale.

-    `dia_of_helical_rebar`è il diametro dell\'armatura elicoidale all\'interno della struttura.

-    `main_rebars_t_offset`e `main_rebars_b_offset` sono le distanze di offset interne per le armature principali rispetto alle facce superiore e inferiore della struttura, rispettivamente.

-    `dia_of_main_rebars`è il diametro delle armature principali.

-    `number_angle_check`se è `True` creerà tante armature principali quante indicate da `number_angle_value`; se è `False` creerà le armature principali con un angolo di `number_spacing_value`, specificato in gradi.

-    `number_angle_value`specifica il numero di armature principali o il valore dell\'angolo tra le armature principali, a seconda del valore di `number_angle_check`.



#### Esempio


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

### Edition of Circular Column Reinforcement 


<div class="mw-translate-fuzzy">

### Modificare una armatura di colonna 

È possibile modificare le proprietà delle armature elicoidali e principali con la seguente funzione


</div>


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

-    `rebar_group`è il gruppo di oggetti `ColumnReinforcement` creato in precedenza..

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeSingleTieFourRebars()`.

-    `structure`e `facename` possono essere omesse in modo che l\'armatura rimanga nella struttura originale..



#### Esempio 


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


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement ColumnRebars Circular/it
