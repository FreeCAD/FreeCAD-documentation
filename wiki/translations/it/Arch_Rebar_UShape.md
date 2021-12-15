---
- GuiCommand:/it
   Name:Arch_Rebar_UShape
   Name/it:Armatura ad U
   MenuLocation:Arch → Strumenti armatura → Armatura ad U o BIM → 3D/BIM → Reinforcement → Rebar UShape
   Workbenches:[Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso:[Armatura a L](Arch_Rebar_LShape/it.md), [Armature](Arch_Rebar/it.md)
   Version:0.17
---

# Arch Rebar UShape/it

## Descrizione

Lo strumento [Armatura ad U](Arch_Rebar_UShape/it.md) consente all\'utente di creare un set di barre d\'armatura a forma di U all\'interno di un oggetto [Struttura](Arch_Structure/it.md).

The **<img src="images/Arch_Rebar_UShape.svg" width=16px> [UShape Rebar](Arch_Rebar_UShape.md)** tool is also integrated into [BIM Workbench](BIM_Workbench.md).


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente aggiuntivo _, tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

<img alt="" src=images/Arch_Rebar_UShape_example.png  style="width:400px;"> 
*Due serie di barre di rinforzo a forma di U all'interno di una [Struttura](Arch_Structure/it.md)*

## Utilizzo

1.  Selezionare una qualsiasi faccia dell\'oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** creato in precedenza.

2.  Quindi selezionare **<img src="images/Arch_Rebar_UShape.svg" width=16px> [Armatura ad U](Arch_Rebar_UShape/it.md)** dagli strumenti dell\'armatura.

3.  Sul lato sinistro dello schermo appare un [pannello delle azioni](task_panel/it.md) come sottostante.

4.  Selezionare l\'orientamento desiderato.

5.  Fornire i dati per \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' e \'Diameter\' dell\'armatura.

6.  Selezionare la modalità di distribuzione \'Amount\' o \'Spacing\' (quantità o spaziatura).

7.  Se è selezionata \'Spacing\', la spaziatura, l\'utente può anche optare per una [spaziatura personalizzata](Custom_Spacing/it.md).

8.  
    **Pick Selected Face**serve per verificare o modificare la faccia per la distribuzione dell\'armatura.

9.  Cliccare **OK** o **Applica** per generare l\'armatura.

10. Cliccare **Annulla** per uscire dal pannello delle azioni.

:   <img alt="" src=images/UShapeDialog.png  style="width:250px;">



*Pannello Azioni per lo strumento Armatura ad U di Arch*

## Proprietà

-    {{PropertyData/it|Orientation}}: Decide l\'orientamento dell\'armatura (es. verso il basso, verso l\'alto, a destra o a sinistra).

-    {{PropertyData/it|Front Cover}}: La distanza tra l\'armatura e la faccia selezionata. Copriferro anteriore

-    {{PropertyData/it|Right Cover}}: La distanza tra l\'estremità destra della barra di destra e la faccia destra della struttura. Copriferro destro

-    {{PropertyData/it|Left Cover}}: La distanza tra l\'estremità sinistra della barra di sinistra e la faccia sinistra della struttura. Copriferro sinistro

-    {{PropertyData/it|Bottom Cover}}: La distanza tra l\'armatura e la parte inferiore della struttura. Copriferro inferiore

-    {{PropertyData/it|Top Cover}}: La distanza tra l\'armatura e la parte superiore della struttura. Copriferro superiore

-    {{PropertyData/it|Rounding}}: Il raggio di curvatura da applicare agli angoli delle barre, espresso quantità di diametro delle barre.

-    {{PropertyData/it|Amount}}: La quantità di barre.

-    {{PropertyData/it|Spacing}}: La distanza tra gli assi di ogni barra.

## Scripting


**Vedere anche:**

[API Arch](Arch_API/it.md), [API Reinforcement](Reinforcement_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Armatura a U può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
Rebar = makeUShapeRebar(f_cover, b_cover, r_cover, l_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                        structure=None, facename=None)
```

-   Crea un oggetto `Rebar` dalla `structure` data, che è una [Struttura](Arch_Structure/it.md), e da una `facename`, che è una faccia di quella struttura.
    -   Se non è data nessuna `structure` e neppure una `facename`, prende come riferimento la faccia selezionata dall\'utente.

-    `f_cover`, `b_cover`, `r_cover`, `l_cover`, e `t_cover` sono le distanze interne di offset per gli elementi dell\'armatura rispetto alle facce della struttura. Sono rispettivamente gli offset anteriore, inferiore, sinistro, destro e superiore.

-    `diameter`è il diametro delle barre di rinforzo all\'interno della struttura.

-    `rounding`è il parametro che determina il raggio di curvatura al centro delle barre di armatura.

-   Se `amount_spacing_check` è `True` crea tante barre di rinforzo quante sono definite da `amount_spacing_value`; se è `False` crea le barre di rinforzo separate dal valore numerico indicato in `amount_spacing_value`.

-    `amount_spacing_value`specifica il numero di barre di rinforzo o il valore della separazione tra di esse, secondo come sono indicate in `amount_spacing_check`.

-    `orientation`specifica l\'orientamento della barra d\'armatura; può essere `"Bottom"`, `"Top"`, `"Right"`, o `"Left"`.

### Esempio


```python
import FreeCAD, Arch, UShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = UShapeRebar.makeUShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = UShapeRebar.makeUShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```

### Modifica delle barre 

È possibile modificare le proprietà dell\'armatura con la seguente funzione: 
```python
editUShapeRebar(Rebar, f_cover, b_cover, r_cover, l_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None) 
```

-    `Rebar`è l\'oggetto `UShapeRebar` creato in precedenza.

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeUShapeRebar()`.

-    `structure`e `facename` possono essere omesse in modo che l\'armatura rimanga nella struttura originale.


```python
import UShapeRebar

UShapeRebar.editUShapeRebar(Rebar, 50, 50, 20, 20,
                            16, 20, 5, True, 5, "Top")

UShapeRebar.editUShapeRebar(Rebar2, 70, 50, 20, 20,
                            16, 70, 5, True, 5, "Top")
```


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar UShape/it
