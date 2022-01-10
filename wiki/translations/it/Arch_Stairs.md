---
- GuiCommand:/it
   Name:Arch_Stairs
   Name/it:Scala
   Workbenches:[Arch](Arch_Workbench/it.md)
   MenuLocation:Arch → Scala
   Shortcut:**S** **R**
   SeeAlso:[Struttura](Arch_Structure/it.md), [Arredo](Arch_Equipment/it.md)
   Version:0.14
---

# Arch Stairs/it


</div>

## Descrizione

Lo strumento [Scale](Arch_Stairs/it.md) consente di creare automaticamente i diversi tipi di scale. Al momento, sono supportate solo le scale dritte (con o senza pianerottolo) sono supportati. Le scale possono essere costruite da zero, o da una [linea](Draft_Line/it.md) dritta, nel qual caso le scale seguono la linea. Se la linea non è orizzontale, ma è inclinata verticalmente, anche le scale seguono la sua pendenza.

Vedere in [Stairs entry in wikipedia](http://en.wikipedia.org/wiki/Stairs) la definizione dei diversi termini usati per descrivere le parti delle scale.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;"> 
*Due scale, uno con una struttura massiccia e un pianerottolo, e un'altra con un solo montante.*

## Opzioni

-   Gli elementi Scala condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)

## Utilizzo

-   Premere il pulsante **<img src="images/Arch_Stairs.svg" width=16px> [Scala](Arch_Stairs/it.md)**, oppure i tasti {{KEY/it|S}}, {{KEY/it|R}}.

1.  Adeguare le proprietà desiderate. Alcune parti delle scale potrebbero non apparire immediatamente se una qualsiasi delle proprietà lo rende impossibile. Ad esempio, potrebbe non apparire la struttura se il suo spessore è impostato pari a 0.

## Proprietà

![](images/StairsProperties_it.png )

#### Dati


{{KEY/it|Arch}}

-    {{ProprietaDati|Align}}: L\'allineamento delle scale sulla loro linea base, se applicabile.

-    {{ProprietaDati|Base}}: La linea base delle scale, se presente.

-    {{ProprietaDati|Height}}: Interpiano. L\'altezza totale delle scale, se non sono basate su una linea base o se la linea base è orizzontale.

-    {{ProprietaDati|Length}}: La lunghezza totale delle scale se non è definita una linea base.

-    {{ProprietaDati|Width}}: La larghezza della scala


{{KEY/it|Base}}

-    {{ProprietaDati|Label}}: nome

-    {{ProprietaDati|Placement}}: [posizionamento](Placement/it.md) del punto base della scala (angolo anteriore sinistro del primo scalino)


{{KEY/it|Steps}}

-    {{ProprietaDati|Nosing}}: lunghezza di sovrapposizione degli scalini

-    {{ProprietaDati|Number of risers}}: numero di scalini, numero di alzate

-    {{ProprietaDati|Riser Height}}: alzata, altezza del gradino

-    {{ProprietaDati|Tread Depth}}: pedata, larghezza del gradino

-    {{ProprietaDati|Tread Thickness}}: spessore degli scalini (aggiunto verso il basso)


{{KEY/it|Structure}}

-    {{ProprietaDati|Landigs}}: pianerottoli

-    {{ProprietaDati|Stringer Offset}}: distanza tra il bordo degli scalini e la struttura di sostegno

-    {{ProprietaDati|Stringer Width}}: larghezza della struttura di sostegno

-    {{ProprietaDati|Structure}}: tipo di struttura della scala

-    {{ProprietaDati|Structure...}}: dimensione per la struttura massiccia, piena

-    {{ProprietaDati|Winders}}: gradini a ventaglio

## Limitazioni

-   Al momento sono disponibili solo scale dritte
-   Vedere [nel forum](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) per scale circolari.
-   Per seguire l\'evoluzione dello strumento consultare la pagina [Arch Stairs](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564) nel forum

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Le Scale possono essere create con le [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```

-   Crea un oggetto `Stairs` da un dato `baseobj`.
-   Se non viene fornito il `baseobj`, usa `length`, `width`, `height`, e `steps`, per costruire un oggetto solido.

Esempio: 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Stairs/it
