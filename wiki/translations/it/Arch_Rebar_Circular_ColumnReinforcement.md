---
- GuiCommand:
   Name:Arch_Rebar_ColumnReinforcement
   Name/it:Armatura di colonna
   MenuLocation:Reinforcement - Column Reinforcement, Arch - Strumenti armatura
   Workbenches:[Reinforcement](Reinforcement_Workbench/it.md), [Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso:[Armatura di pilastro con 2 staffe e 6 barre](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/it.md), [Armatura personalizzata](Arch_Rebar/it.md)
   Version:0.19
---

# Arch Rebar Circular ColumnReinforcement/it


</div>

## Descrizione

Lo strumento [Armatura di colonna](Arch_Rebar_Circular_ColumnReinforcement/it.md) consente all\'utente di creare delle barre di rinforzo all\'interno di un oggetto [Struttura](Arch_Structure/it.md) Colonna.


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente aggiuntivo [Reinforcement](Reinforcement_Workbench/it.md), che si può installare con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr/it.md), tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

<img alt="" src=images/Arch_Rebar_Circular_ColumnReinforcement_example.png  style="width:400px;"> 
*Rinforzo di colonna all'interno di una [Struttura](Arch_Structure/it.md) colonna*

## Utilizzo

1\. Selezionare una faccia di un oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** creato precedentemente.
2. Quindi selezionare **<img src="images/Arch_Rebar_ColumnReinforcement.svg" width=16px> [Armatura di colonna](Arch_Rebar_ColumnReinforcement/it.md)** dagli strumenti armatura.
3. Sullo schermo appare una finestra di dialogo come mostrato sotto.
<img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;"> 
*Finestra di dialogo per lo strumento Armatura di colonna*

4\. Selezionare il pulsante di opzione Colonna circolare nella finestra di dialogo di rinforzo della colonna.

<img alt="" src=images/CircularColumnReinforcementDialog.png  style="width:700px;"> 
*Finestra di dialogo per l'armatura della colonna circolare*

5\. Fornire gli input per i dati relativi al rinforzo della colonna.
6. Cliccare **OK** o **Applica** per generare il rinforzo della colonna.

15\. Cliccare **Cancella** per uscire dalla finestra di dialogo.

## Proprietà

**Helical Rebars:**

-    {{PropertyData/it|Side Cover}}: La distanza tra l\'armatura e la faccia curva.

-    {{PropertyData/it|Top Cover}}: La distanza tra l\'armatura e la parte superiore della struttura. Copriferro superiore

-    {{PropertyData/it|Bottom Cover}}: La distanza tra l\'armatura e la parte inferiore della struttura. Copriferro inferiore

-    {{PropertyData/it|Pitch}}: Il passo dell\'elica, che è l\'altezza di un giro completo di elica, misurato parallelo all\'asse dell\'elica.

-    {{PropertyData/it|Diameter}}: Diametro della barra elicoidale.

**Main Rebars:**

-    **Top Offset**: La distanza tra l\'armature e la faccia superiore della struttura.

-    **Bottom Offset**: La distanza tra l\'armature e la faccia inferiore della struttura.

-    **Diameter**: Diametro delle armature principali.

-    **Number**: Il numero di armature principali.

-    **Angle**: La distanza angolare tra le legature.

## Script


**Vedere anche:**

[API Arch](Arch_API/it.md), [API di Reinforcement](Reinforcement_API/it.md) e [Basi di script per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Armatura di colonna può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:

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

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `s_cover`, `helical_rebar_t_offset`, and `helical_rebar_b_offset` are inner offset distances for the helical rebar with respect to the faces of the structure. They are respectively the side, top and bottom offsets.

-    `pitch`is the parameter that determines how close or far apart each helical loop is to each other.

-    `dia_of_helical_rebar`is the diameter of the helical rebar inside the structure.

-    `main_rebars_t_offset`and `main_rebars_b_offset` are inner offset distances for the main rebars with respect to the top and bottom faces of the structure, respectively.

-    `dia_of_main_rebars`is the diameter of the main rebars.

-    `number_angle_check`if it is `True` it will create as many main rebars as given by `number_angle_value`; if it is `False` it will create main rebars at an angle of `number_spacing_value`, specified in degrees.

-    `number_angle_value`specifies the number of main rebars, or the value of the angle between the main rebars, depending on `number_angle_check`.

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


{{docnav/it
|[Armatura elicoidale](Arch_Rebar_Helical/it.md)
|[Armatura di pilastro](Arch_Rebar_ColumnReinforcement/it.md)
|[Arch](Arch_Workbench/it.md)
|IconL=Arch_Rebar_Helical.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_Rebar_ColumnReinforcement.svg
}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Circular ColumnReinforcement/it
