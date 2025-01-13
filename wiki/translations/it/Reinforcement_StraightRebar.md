---
 GuiCommand:
   Name: Arch Rebar Straight
   Name/it: Armatura diritta
   MenuLocation: Arch , Strumenti di armatura , Armatura diritta<br>3D/BIM , Reinforcement tools , Armatura diritta
   Workbenches: Arch_Workbench/it, BIM_Workbench/it
   Version: 0.17
   SeeAlso: Reinforcement_Workbench/it, Arch_Rebar/it, Arch_Rebar_BOM/it
---

# Reinforcement StraightRebar/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento [Armatura diritta](Arch_Rebar_Straight/it.md) consente all\'utente di creare un set di staffe d\'armatura all\'interno di un oggetto [Struttura](Arch_Structure/it.md).


</div>


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente [Reinforcement](Reinforcement_Workbench/it.md), un [ambiente esterno](External_workbenches/it.md) che si può installare con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md), tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

<img alt="" src=images/Arch_Rebar_Straight_example.png  style="width:400px;"> 
*Due serie di barre di rinforzo diritte all'interno di una  [Struttura](Arch_Structure/it.md)*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una qualsiasi faccia dell\'oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)**.

2.  Quindi selezionare **<img src="images/Arch_Rebar_Straight.svg" width=16px> [Armatura diritta](Arch_Rebar_Straight/it.md)** dagli strumenti dell\'armatura.

3.  Sul lato sinistro dello schermo appare un pannello come quello sottostante.

4.  Selezionare l\'orientamento desiderato.

5.  Fornire i dati per \'Copriferro anteriore\', \'Copriferro lato destro\', \'Copriferro lato sinistro\', \'Copriferro inferiore\' e \'Diametro\' per l\'armatura.

6.  Seleziona la modalità di distribuzione tra \'Quantità\' o \'Passo\'.

7.  Se è selezionato Passo, l\'utente può anche optare per [Passo personalizzato](Custom_Spacing/it.md).

8.  
    **Usa lato selezionato**viene utilizzato per verificare o modificare la faccia per la distribuzione dell\'armatura.

9.  Cliccare **OK** o **Applica** per generare l\'armatura.

10. Cliccare **Annulla** per uscire dal pannello.


</div>

<img alt="" src=images/StraightRebarDialog.png  style="width:250px;">


<div class="mw-translate-fuzzy">



*Pannello per lo strumento Armatura diritta di Arch*


</div>



## Proprietà

-    {{PropertyData/it|Orientamento}}: Decide l\'orientamento dell\'armatura (es. in basso, in alto, a destra e a sinistra).

-    {{PropertyData/it|Copriferro anteriore}}: La distanza tra l\'armatura e la faccia selezionata.

-    {{PropertyData/it|Copriferro lato destro}}: La distanza tra l\'estremità destra dell\'armatura e la faccia destra della struttura.

-    {{PropertyData/it|Copriferro lato sinistro}}: La distanza tra l\'estremità sinistra dell\'armatura e la faccia sinistra della struttura.

-    {{PropertyData/it|Copriferro in direzione}}: Queste proprietà consentono all\'utente di specificare il copriferro superiore o inferiore.

-    {{PropertyData/it|Copriferro inferiore }}: La distanza tra l\'armatura e la faccia inferiore della struttura.

-    {{PropertyData/it|Copriferro superiore}}: La distanza tra l\'armatura e la faccia superiore della struttura.

-    {{PropertyData/it|Quantità}}: La quantità di armature.

-    {{PropertyData/it|Passo}}: La distanza tra gli assi di ciascuna barra.

## Scripting


**Vedere anche:**

[API Arch](Arch_API/it.md), [API Reinforcement](Reinforcement_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">

Lo strumento Armatura diritta può essere usato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
Rebar = makeStraightRebar(f_cover, coverAlong, rt_cover, lb_cover,
                          diameter, amount_spacing_check, amount_spacing_value, orientation="Horizontal",
                          structure=None, facename=None)
```

-   Crea un oggetto `Rebar` dalla `structure` data, che è una [Struttura](Arch_Structure/it.md), e da una `facename`, che è una faccia di quella struttura.
    -   Se non è data nessuna `structure` e neppure una `facename`, prende come riferimento la faccia selezionata dall\'utente.

-    `f_cover`, `coverAlong`, `rt_cover`, e `lb_cover` sono le distanze di offset interne per gli elementi dell\'armatura rispetto alle facce della struttura.

    -   
        `f_cover`
        
        è l\'offset del copriferro frontale.

    -   
        `coverAlong`
        
        è una tupla `(position, value)` che definisce il valore di offset in una posizione (top, bottom, left, right) che dipende da `orientation`.

    -   
        `rt_cover`
        
        è l\'offset del copriferro destro o superiore, a seconda del valore di `coverAlong` e `orientation`.

    -   
        `lb_cover`
        
        è l\'offset del copriferro sinistro o inferiore, a seconda del valore di `coverAlong` e `orientation`.

-    `diameter`è il diametro delle barre di rinforzo all\'interno della struttura.

-   Se `amount_spacing_check` è `True` crea tante barre di rinforzo quante sono definite da `amount_spacing_value`; se è `False` crea le barre di rinforzo separate dal valore numerico indicato in `amount_spacing_value`.

-    `amount_spacing_value`specifica il numero di barre di rinforzo o il valore della separazione tra di esse, secondo come sono indicate in `amount_spacing_check`.

-    `orientation`specifica l\'orientamento della barra d\'armatura; può essere `"Horizontal"` o `"Vertical"`.

A seconda dell\'orientamento della barra di armatura, la funzione può essere chiamata in due modi generali impostando `coverAlong` in modo appropriato.



### La barra è orizzontale 


```python
Rebar = makeStraightRebar(f_cover, ("Top Side", value), right_cover, left_cover, ...)
Rebar = makeStraightRebar(f_cover, ("Bottom Side", value), right_cover, left_cover, ...)
```

-    `coverAlong`è una tupla con un `value` di offset `"Top Side"` o `"Bottom Side"`.

-   In questo caso `rt_cover` si riferisce all\'offset `right_cover`, e `lb_cover` si riferisce all\'offset `left_cover`.



### La barra è verticale 


```python
Rebar = makeStraightRebar(f_cover, ("Left Side", value), top_cover, bottom_cover, ...)
Rebar = makeStraightRebar(f_cover, ("Right Side", value), top_cover, bottom_cover, ...)
```

-    `coverAlong`è una tupla con un `value` di offset `"Left Side"` o `"Right Side"`.

-   In questo caso `rt_cover` si riferisce all\'offset `top_cover`, e `lb_cover` si riferisce all\'offset `bottom_cover`.



### Esempio orizzontale 


```python
import Arch, Draft, StraightRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = StraightRebar.makeStraightRebar(50, ("Bottom Side", 20), 100, 100,
                                        12, True, 5, "Horizontal", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = StraightRebar.makeStraightRebar(50, ("Bottom Side", 50), 100, 100,
                                         12, True, 5, "Horizontal", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```



### Esempio vericale 


```python
import Arch, Draft, StraightRebar

Structure2 = Arch.makeStructure(length=1000, width=1000, height=400)
Structure2.ViewObject.Transparency = 80
Draft.move(Structure2, FreeCAD.Vector(1500, 0, 0))
FreeCAD.ActiveDocument.recompute()

Rebar3 = StraightRebar.makeStraightRebar(50, ("Left Side", 20), 100, 100,
                                         12, True, 5, "Vertical", Structure2, "Face4")
Rebar3.ViewObject.ShapeColor = (0.9, 0.5, 0.0)

Rebar4 = StraightRebar.makeStraightRebar(50, ("Left Side", 50), 100, 100,
                                         12, True, 5, "Vertical", Structure2, "Face6")
Rebar4.ViewObject.ShapeColor = (0.0, 0.5, 0.5)
```

### Edition of rebar 


<div class="mw-translate-fuzzy">

### Modifica delle barre 

È possibile modificare le proprietà dell\'armatura con la seguente funzione:


</div>


```python
editStraightRebar(Rebar, f_cover, coverAlong, rt_cover, lb_cover,
                  diameter, amount_spacing_check, amount_spacing_value, orientation,
                  structure=None, facename=None)
```

-    `Rebar`è l\'oggetto `StraightRebar` creato in precedenza.

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeStraightRebar()`.

-    `structure`e `facename` possono essere omesse in modo che l\'armatura rimanga nella struttura originale.

Esempio:


```python
import StraightRebar

StraightRebar.editStraightRebar(Rebar, 50, ("Top Side", 20), 100, 100,
                                24, True, 7, "Horizontal")

StraightRebar.editStraightRebar(Rebar2, 50, ("Top Side", 50), 100, 100,
                                24, True, 7, "Horizontal")

StraightRebar.editStraightRebar(Rebar3, 50, ("Right Side", 20), 100, 100,
                                24, True, 7, "Vertical")

StraightRebar.editStraightRebar(Rebar4, 50, ("Right Side", 50), 100, 100,
                                24, True, 7, "Vertical")
```


<div class="mw-translate-fuzzy">





</div>

{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement StraightRebar/it
