---
- GuiCommand:/it
   Name:Arch_Rebar_Straight
   Name/it:Armatura dritta
   MenuLocation:Arch → Strumenti armatura → Armatura dritta o BIM → 3D/BIM → Reinforcement → Straight Rebar
   Workbenches:[Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso:[Distinta dei ferri](Arch_Rebar_BOM/it.md), [Armatura](Arch_Rebar/it.md)
   Version:0.17
---

# Arch Rebar Straight/it

## Descrizione

Lo strumento [Armatura dritta](Arch_Rebar_Straight.md) consente all\'utente di creare un set di staffe d\'armatura all\'interno di un oggetto [Struttura](Arch_Structure/it.md).

Lo strumento **Armatura dritta** è anche integrato in [BIM](BIM_Workbench/it.md).


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente [Reinforcement](Reinforcement_Workbench/it.md), un [ambiente esterno](External_workbenches/it.md) che si può installare con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr/it.md), tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>

<img alt="" src=images/Arch_Rebar_Straight_example.png  style="width:400px;"> 
*Due serie di barre di rinforzo diritte all'interno di una  [Struttura](Arch_Structure/it.md)*

## Utilizzo

1.  Selezionare una qualsiasi faccia dell\'oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** creato in precedenza.
2.  Quindi selezionare **<img src="images/Arch_Rebar_Straight.svg" width=16px> Armatura dritta** dagli strumenti armatura.
3.  Sul lato sinistro dello schermo appare un pannello delle azioni come quello sottostante.
4.  Selezionare l\'orientamento desiderato.
5.  Fornire i dati per front cover, right side cover, left side cover, bottom cover e diameter of the rebar.
6.  Select the mode of distribution either amount or spacing.
7.  Selezionare la modalità di distribuzione per la quantità o per la spaziatura.
8.  Se è selezionata la spaziatura, l\'utente può anche optare per una [spaziatura personalizzata](Custom_Spacing/it.md).
9.  Cliccare sulla faccia selezionata serve per verificare o modificare la faccia per la distribuzione dell\'armatura.
10. Cliccare **OK** o **Apply** per generare l\'armatura.
11. Cliccare **Cancel** per uscire dal pannello delle azioni.

<img alt="" src=images/StraightRebarDialog.png  style="width:250px;"> 
*Pannello Azioni per lo strumento Armatura dritta di Arch*

## Proprietà

-    {{PropertyData/it|Orientation}}: Decide l\'orientamento dell\'armatura (es. in basso, in alto, a destra e a sinistra).

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

Lo strumento Armatura dritta può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione: 
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

### Modifica delle barre 

È possibile modificare le proprietà dell\'armatura con la seguente funzione: 
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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Straight/it
