---
 GuiCommand:
   Name: Arch_Rebar_BentShape
   Name/it: Armatura sagomata
   MenuLocation: Arch , Strumenti armatura , Armatura sagomata o 3D/BIM , Reinforcement , Bent-Shape Rebar
   Workbenches: Reinforcement Workbench/it, Arch Workbench/it, BIM Workbench/it
   SeeAlso: Arch_Rebar_Stirrup/it, Arch Rebar/it
   Version: 0.17
---

# Arch Rebar BentShape/it


</div>



## Descrizione

Lo strumento [Armatura sagomata](Arch_Rebar_BentShape/it.md) consente all\'utente di creare una serie di barre d\'armatura piegate all\'interno di un oggetto [Struttura](Arch_Structure/it.md).

Lo strumento **Armatura sagomata** è anche integrato in [BIM](BIM_Workbench/it.md).


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente aggiuntivo [Reinforcement](Reinforcement_Workbench/it.md), che si può installare con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr/it.md), tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

<img alt="" src=images/Arch_Rebar_BentShape_example.png  style="width:400px;"> 
*Due serie di barre di rinforzo piegate all'interno di una [Struttura](Arch_Structure/it.md)*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una qualsiasi faccia dell\'oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** creato in precedenza.

2.  Quindi selezionare **<img src="images/Arch_Rebar_BentShape.svg" width=16px> [Armatura sagomata](Arch_Rebar_BentShape/it.md)** dagli strumenti dell\'armatura.

3.  Sul lato sinistro dello schermo appare un [pannello delle azioni](task_panel/it.md) come quello sottostante.

4.  Selezionare l\'orientamento desiderato.

5.  Fornire i dati per \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' e \'Diameter\' dell\'armatura.

6.  Selezionare la modalità di distribuzione per \'Amount\' (la quantità) o per \'Spacing\' (la spaziatura).
    -   Se è selezionata la spaziatura, l\'utente può anche optare per una [spaziatura personalizzata](Custom_Spacing/it.md).

7.  
    **Pick Selected Face**serve per verificare o modificare la faccia per la distribuzione dell\'armatura.

8.  Cliccare **OK** o **Apply** per generare l\'armatura.

9.  Cliccare **Cancel** per uscire dal pannello delle azioni.


</div>


:   <img alt="" src=images/BentShapeDialog.png  style="width:250px;">



*Pannello Azioni per lo strumento Armatura sagomata di Arch*



## Proprietà

-    {{PropertyData/it|Orientation}}: Decide l\'orientamento dell\'armatura (es. in basso, in alto, a destra e a sinistra).

-    {{PropertyData/it|Front Cover}}: La distanza tra l\'armatura e la faccia selezionata. Copriferro anteriore

-    {{PropertyData/it|Right Cover}}: La distanza tra l\'estremità destra della barra di destra e la faccia destra della struttura. Copriferro destro

-    {{PropertyData/it|Left Cover}}: La distanza tra l\'estremità sinistra della barra di sinistra e la faccia sinistra della struttura. Copriferro sinistro

-    {{PropertyData/it|Bottom Cover}}: La distanza tra l\'armatura e la parte inferiore della struttura. Copriferro inferiore

-    {{PropertyData/it|Top Cover}}: La distanza tra l\'armatura e la parte superiore della struttura. Copriferro superiore

-    {{PropertyData/it|Anchor Length}}: È la lunghezza del braccio della barra piegata.

-    {{PropertyData/it|Bent Angle}}: L\'angolo di piega

-    {{PropertyData/it|Amount}}: La quantità di barre.

-    {{PropertyData/it|Spacing}}: La distanza tra gli assi di ogni barra.




<div class="mw-translate-fuzzy">

## Scripting


**Vedere anche:**

[API Arch](Arch_API/it.md), [API Reinforcement](Reinforcement_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Lo strumento Armatura sagomata può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
Rebar = makeBentShapeRebar(f_cover, b_cover, l_cover, r_cover,
                           diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                           structure=None, facename=None)
```

-   Crea un oggetto `Rebar` dalla `structure` data, che è una [Struttura](Arch_Structure/it.md), e da una `facename`, che è una faccia di quella struttura.
    -   Se non è data nessuna `structure` e neppure una `facename`, prende come riferimento la faccia selezionata dall\'utente.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover`, e `t_cover` sono le distanze di offset interne per gli elementi dell\'armatura rispetto alle facce della struttura. Sono rispettivamente gli offset anteriore, inferiore, sinistro, destro e superiore.

-    `diameter`è il diametro delle barre di rinforzo all\'interno della struttura.

-    `rounding`è il parametro che determina il raggio di curvatura al centro delle barre di armatura.

-    `bentLength`e `bentAngle` definisce la lunghezza della punta delle barre di rinforzo e l\'angolo di piegatura al centro dalle barre.

-   Se `amount_spacing_check` è `True` crea tante barre di rinforzo quante sono definite da `amount_spacing_value`; se è `False` crea le barre di rinforzo separate dal valore numerico indicato in `amount_spacing_value`.

-    `amount_spacing_value`specifica il numero di barre di rinforzo o il valore della separazione tra di esse, secondo come sono indicate in `amount_spacing_check`.

-    `orientation`specifica l\'orientamento della barra d\'armatura; può essere `"Bottom"`, `"Top"`, `"Left"`, o `"Right"`.



### Esempio


```python
import FreeCAD, Arch, BentShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=100)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = BentShapeRebar.makeBentShapeRebar(50, 20, 20, 20,
                                          8, 40, 100, 135, 2, True, 4, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = BentShapeRebar.makeBentShapeRebar(50, 40, 20, 20,
                                           8, 20, 100, 135, 2, True, 4, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```



### Modifica delle barre 

È possibile modificare le proprietà dell\'armatura con la seguente funzione:


```python
editBentShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                   diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation,
                   structure=None, facename=None)
```

-    `Rebar`è l\'oggetto `BentShapeRebar` creato in precedenza.

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeBentShapeRebar()`.

-    `structure`e `facename` possono essere omesse in modo che l\'armatura rimanga nella struttura originale.


```python
import BentShapeRebar

BentShapeRebar.editBentShapeRebar(Rebar, 50, 20, 20, 20,
                                  12, 20, 100, 155, 2, True, 6, "Top")

BentShapeRebar.editBentShapeRebar(Rebar2, 50, 35, 20, 20,
                                  12, 35, 100, 155, 2, True, 6, "Top")
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar BentShape/it
