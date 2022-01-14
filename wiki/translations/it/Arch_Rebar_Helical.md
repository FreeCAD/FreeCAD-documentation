---
- GuiCommand:/it
   Name:Arch Rebar Helical
   Name/it:Armatura elicoidale
   MenuLocation:Arch → Strumenti armatura → Armatura elicoidale o 3D/BIM → Reinforcement → Helical Rebar
   Workbenches:[Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso:[Staffa armatura](Arch_Rebar_Stirrup/it.md), [Rinforzo di pilastro](Arch_Rebar_ColumnReinforcement/it.md)
   Version:0.17
---

# Arch Rebar Helical/it


</div>

## Descrizione

Lo strumento [Armatura elicoidale](Arch_Rebar_Helical/it.md) consente all\'utente di creare una barra di rinforzo elicoidale continua all\'interno di un oggetto [Struttura](Arch_Structure/it.md).

Lo strumento **Armatura elicoidale** è anche integrato in [BIM](BIM_Workbench/it.md).


<div class="mw-translate-fuzzy">

Questo comando fa parte dell\'ambiente [Reinforcement](Reinforcement_Workbench/it.md), un [ambiente esterno](External_workbenches/it.md) che si può installare con <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon manager](Std_AddonMgr/it.md), tramite il menu **Strumenti → Addon manager → Reinforcement**.


</div>


:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">



*Una barra di rinforzo elicoidale continua all'interno di una [Struttura](Arch_Structure/it.md)*

## Utilizzo

1.  Selezionare qualsiasi faccia di un oggetto **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)** creato in precedenza.

2.  Quindi selezionare **<img src="images/Arch_Rebar_Helical.svg" width=16px> [Armatura elicoidale](Arch_Rebar_Helical/it.md)** dal menu Armature.

3.  Sul lato sinistro dello schermo appare un [pannello delle azioni](task_panel/it.md) come sottostante.

4.  Selezionare l\'orientamento desiderato.

5.  Fornire i dati per \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' e \'Diameter\' dell\'armatura.

6.  Selezionare la modalità di distribuzione \'Amount\' o \'Spacing\' (quantità o spaziatura).

7.  Se è selezionata \'Spacing\', la spaziatura, l\'utente può anche optare per una [spaziatura personalizzata](Custom_Spacing/it.md).

8.  
    **Pick Selected Face**serve per verificare o modificare la faccia per la distribuzione dell\'armatura.

9.  Cliccare **OK** o **Applica** per generare l\'armatura.

10. Cliccare **Annulla** per uscire dal pannello delle azioni.

:   <img alt="" src=images/HelicalRebarDialog.png  style="width:250px;">



*Pannello Azioni per lo strumento Armatura elicoidale di Arch*

## Proprietà

-    {{PropertyData/it|Side Cover}}: La distanza tra l\'armatura e la faccia curva.

-    {{PropertyData/it|Bottom Cover}}: La distanza tra l\'armatura e la parte inferiore della struttura. Copriferro inferiore

-    {{PropertyData/it|Top Cover}}: La distanza tra l\'armatura e la parte superiore della struttura. Copriferro superiore

-    {{PropertyData/it|Pitch}}: Il passo dell\'elica, che è l\'altezza di un giro completo di elica, misurato parallelo all\'asse dell\'elica.

-    {{PropertyData/it|Diameter}}: Diametro della barra elicoidale.

## Scripting


**Vedere anche:**

[API Arch](Arch_API/it.md), [API Reinforcement](Reinforcement_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Armatura elicoidale può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-   Crea un oggetto `Rebar` da una data `structure`, che è una [Struttura](Arch_Structure/it.md), e da una `facename`, che è una faccia di quella struttura.
    -   Se non è data nessuna `structure` e neppure una `facename`, prende come riferimento la faccia selezionata dall\'utente..

-    `s_cover`, `b_cover`, e `t_cover` sono le distanze di offset interne per gli elementi dell\'armatura rispetto alle facce della struttura. Sono rispettivamente gli offset laterali, inferiori e superiori.

-    `diameter`è il diametro della spirale di rinforzo all\'interno della struttura.

-    `pitch`è il parametro che determina la distanza tra le spire dell\'armatura.

### Esempio


```python
import FreeCAD, Draft, Arch, HelicalRebar

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = HelicalRebar.makeHelicalRebar(10, 50, 8, 50, 50, structure, "Face2")
```

### Modifica delle barre 

È possibile modificare le proprietà dell\'armatura con la seguente funzione:


```python
editHelicalRebar(Rebar, s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-    `Rebar`è l\'oggetto `HelicalRebar` creato in precedenza.

-   Gli altri parametri sono gli stessi richiesti dalla funzione `makeHelicalRebar()`.

-    `structure`e `facename` possono essere omesse in modo che l\'armatura rimanga nella struttura originale.


```python
import HelicalRebar

HelicalRebar.editHelicalRebar(Rebar, 20, 100, 20, 20, 100)
```


<div class="mw-translate-fuzzy">





</div>


 

[<img src="images/Property.png" style="width:16px"> Reinforcement](Category_Reinforcement.md)

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Helical/it
