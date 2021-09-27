---
- GuiCommand:/it
   Name:Arch_Rebar_Stirrup
   Name/it:Staffe armatura
   MenuLocation:Arch → Strumenti armatura → Staffe armatura o BIM → 3D/BIM → Reinforcement → Stirrup
   Workbenches:[Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso:[Armatura elicoidale](Arch_Rebar_Helical/it.md), [Armatura personalizzata](Arch_Rebar/it.md)
   Version:0.17
---

# Arch Rebar Stirrup/it


</div>

## Descrizione

Lo strumento [Staffe armatura](Arch_Rebar_Stirrup/it.md) consente all\'utente di creare un set di staffe d\'armatura all\'interno di un oggetto [Struttura](Arch_Structure/it.md).

Lo strumento **Staffe armatura** è anche integrato in [BIM](BIM_Workbench/it.md).

Questo comando fa parte dell\'ambiente _, tramite il menu **Strumenti → Addon manager → Reinforcement**.

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;"> 
*Un set di staffe di rinforzo all'interno di una [Struttura](Arch_Structure/it.md)*

## Utilizzo

1.  Selezionare una qualsiasi faccia dell\'oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** creato in precedenza.

2.  Quindi selezionare **<img src="images/Arch_Rebar_Stirrup.svg" width=16px> [Staffa armatura](Arch_Rebar_Stirrup/it.md)** dagli strumenti armatura.

3.  Sul lato sinistro dello schermo appare un [pannello delle azioni](task_panel/it.md) come sottostante.

4.  Selezionare l\'orientamento desiderato.

5.  Fornire i dati per \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' e \'Diameter\' dell\'armatura.

6.  Selezionare la modalità di distribuzione \'Amount\' o \'Spacing\' (quantità o spaziatura).

7.  Se è selezionata \'Spacing\', la spaziatura, l\'utente può anche optare per una [spaziatura personalizzata](Custom_Spacing/it.md).

8.  
    **Pick Selected Face**serve per verificare o modificare la faccia per la distribuzione dell\'armatura.

9.  Cliccare **OK** o **Applica** per generare l\'armatura.

10. Cliccare **Annulla** per uscire dal pannello delle azioni.

:   <img alt="" src=images/StirrupDialog.png  style="width:250px;">


*Pannello Azioni per lo strumento Staffe armatura di Arch*

## Proprietà

-    {{PropertyData/it|Orientation}}: Decide l\'orientamento dell\'armatura (es. in basso, in alto, a destra e a sinistra).

-    {{PropertyData/it|Front Cover}}: La distanza tra l\'armatura e la faccia selezionata. Copriferro anteriore

-    {{PropertyData/it|Right Cover}}: La distanza tra l\'estremità destra della barra di destra e la faccia destra della struttura. Copriferro destro

-    {{PropertyData/it|Left Cover}}: La distanza tra l\'estremità sinistra della barra di sinistra e la faccia sinistra della struttura. Copriferro sinistro

-    {{PropertyData/it|Bottom Cover}}: La distanza tra l\'armatura e la parte inferiore della struttura. Copriferro inferiore

-    {{PropertyData/it|Top Cover}}: La distanza tra l\'armatura e la parte superiore della struttura. Copriferro superiore

-    {{PropertyData/it|Bent Angle}}: L\'angolo del gancio finale della staffa.

-    {{PropertyData/it|Bent Factor}}: Lunghezza del gancio finale della staffa.

-    {{PropertyData/it|Amount}}: La quantità di barre.

-    {{PropertyData/it|Spacing}}: La distanza tra gli assi di ogni barra.

## Scripting


**Vedere anche:**

[API Arch](Arch_API/it.md), [API Reinforcement](Reinforcement_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Staffe armatura può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione: 
```python
Rebar = makeStirrup(l_cover, r_cover, t_cover, b_cover, f_cover,
                    bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
                    structure=None, facename=None)
```

-   Crea un oggetto `Rebar` dalla `structure` data, che è una [Struttura](Arch_Structure/it.md), e da una `facename`, che è una faccia di quella struttura.
    -   Se non è data nessuna `structure` e neppure una `facename`, prende come riferimento la faccia selezionata dall\'utente.

-    `l_cover`, `r_cover`, `t_cover`, `b_cover`, e `f_cover` sono le distanze di offset interne per gli elementi dell\'armatura rispetto alle facce della struttura. Sono rispettivamente gli offset sinistro, destro, superiore, inferiore e frontale.

-    `diameter`è il diametro delle barre di rinforzo all\'interno della struttura.

-    `rounding`è il parametro che determina il raggio di curvatura delle barre di armatura quando creano un giro.

-    `bentLength`e `bentAngle` definiscono la lunghezza e l\'angolo della punta dell\'anello di rinforzo.

-   Se `amount_spacing_check` è `True` creerà tanti giri come indicato in `amount_spacing_value`; se è `False` crea loop di rinforzo separati dal valore numerico di `amount_spacing_value`.

-    `amount_spacing_value`specifica il numero di barre di rinforzo o il valore della separazione tra di esse, secondo come sono indicato in `amount_spacing_check`.

### Esempio


```python
import Draft, Arch, Stirrup

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = Stirrup.makeStirrup(20, 20, 20, 20, 20,
                            115, 4, 8, 2, True, 10, Structure, "Face6")
```

### Modifica delle barre 

È possibile modificare le proprietà dell\'armatura con la seguente funzione: 
```python
editStirrup(Rebar, l_cover, r_cover, t_cover, b_cover, f_cover,
            bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
            structure=None, facename=None)
```

-    `Rebar`è l\'oggetto `StirrupRebar` creato in precedenza.

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeStirrup()`.

-    `structure`e `facename` possono essere omesse in modo che l\'armatura rimanga nella struttura originale.


```python
import Stirrup

Stirrup.editStirrup(Rebar, 20, 20, 20, 20, 50,
                    100, 4, 14, 8, True, 8)
```


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Stirrup/it
