---
 GuiCommand:
   Name: Arch Stairs
   Name/it: Scala
   MenuLocation: Arch , Scala
   Workbenches: Arch_Workbench/it
   Shortcut: **S** **R**
   Version: 0.14
   SeeAlso: Arch_Structure/it, Arch_Equipment/it
---

# Arch Stairs/it


</div>



## Descrizione

Lo strumento [Scale](Arch_Stairs/it.md) consente di creare automaticamente i diversi tipi di scale. Al momento, sono supportate solo le scale dritte (con o senza pianerottolo). Le scale possono essere costruite da zero, o da una [linea](Draft_Line/it.md) dritta, nel qual caso le scale seguono la linea. Se la linea non è orizzontale, ma è inclinata verticalmente, anche le scale seguono la sua pendenza.

Vedere in [Stairs entry in wikipedia](https://en.wikipedia.org/wiki/Stairs) la definizione dei diversi termini usati per descrivere le parti delle scale.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:600px;"> 
*Due scale, uno con una struttura massiccia e un pianerottolo, e l'altra con un solo montante.*



## Opzioni

-   Gli elementi Scala condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Facoltativamente selezionare uno o più oggetti base, ad esempio [Linee di Draft](Draft_Line/it.md) e [Polilinea di Draft](Draft_Wire/it.md):
    -   Per creare i pianerottoli verranno utilizzate polilinee con due o più segmenti. Devono trovarsi su un piano parallelo al piano XY globale. Ad esempio, selezionare una polilinea a forma di U per un pianerottolo a mezzo giro e una polilinea a forma di L per un pianerottolo d\'angolo.
    -   Le linee di bozza verranno utilizzate per creare le rampe.
    -   Se i vertici di tutte le linee e polilinee hanno coordinate Z corrette, le scale create utilizzeranno queste informazioni.
    -   Gli oggetti di base devono essere selezionati nell\'ordine corretto iniziando dall\'oggetto in basso.
2.  Premere il pulsante **<img src="images/Arch_Stairs.svg" width=16px> [Scala](Arch_Stairs/it.md)**, oppure premere i tasti **S**, **R**.
3.  Impostare le proprietà desiderate. Alcune parti delle scale, come la struttura, potrebbero non essere visualizzate immediatamente se una qualsiasi delle proprietà lo rende impossibile, ad esempio uno spessore della struttura pari a 0.


</div>

<img alt="" src=images/Stairs_and_Landing_02.png  style="width:600px;">

<img alt="" src=images/Stairs_and_Landing_01.png  style="width:600px;">

<img alt="" src=images/Arch_Stairs_Complex_Example.png  style="width:600px;">



*Scale complesse basate su una selezione di linee e collegate come mostrato a sinistra.<br>
In rosso i cavi utilizzati per gli atterraggi a Z=1500mm, Z=3000mm e Z=4500mm.<br>
In nero le linee che li collegano utilizzate per le rampe.*



## Proprietà



### Dati


{{TitleProperty|Segment and Parts}}


<div class="mw-translate-fuzzy">

-    **Abs Top|Vector**: (sola lettura) Il livello più alto assoluto a cui conducono le scale.

-    **Last Segment|Link**: Ultimo tratto (rampa o pianerottolo) di una scala ad arco che si collega a questo tratto. Il livello iniziale delle scale sarà il livello finale di quest\'ultimo tratto.

-    **Outline Left|VectorList**: Il profilo sinistro delle scale.

-    **Outline Left All|VectorList**: Il profilo sinistro di tutti i segmenti delle scale.

-    **Outline Right|VectorList**: Il profilo destro delle scale.

-    **Outline Right All|VectorList**: Il profilo destro di tutti i segmenti delle scale.

-    **Railing Height Left|Length**: Altezza della ringhiera sinistra della scala o del pianerottolo.

-    **Railing Height Right|Length**: Altezza della ringhiera destra della scala o del pianerottolo.

-    **Railing Left|LinkHidden**: L\'oggetto ringhiera sinistra. {{Version/it|0.20}}: tipo di proprietà aggiornato da {{Incode|String}} a {{Incode|LinkHidden}}.

-    **Railing Offset Left|Length**: Scostamento della ringhiera sinistra dal bordo della scala o del pianerottolo.

-    **Railing Offset Right|Length**: Scostamento della ringhiera destra dal bordo delle scale o del pianerottolo.

-    **Railing Right|LinkHidden**: L\'oggetto ringhiera destra. {{Version/it|0.20}}: tipo di proprietà aggiornato da {{Incode|String}} a {{Incode|LinkHidden}}.


</div>


{{TitleProperty|Stairs}}

-    **Align|Enumeration**: L\'allineamento delle scale sulla linea di base. Utilizzato solo se è definita una linea di base. Può essere {{value|Left}}, {{value|Right}} o {{value|Center}}.

-    **Height|Length**: L\'altezza totale delle scale. Utilizzato solo se non è definita alcuna linea di base o se la linea di base è orizzontale. Ignorato se **Riser Height Enforce** è diverso da zero.

-    **Length|Length**: La lunghezza totale delle scale se non è definita alcuna linea base. Ignorato se **Tread Depth Enforce** è diverso da zero.

-    **Width|Length**: La larghezza delle scale.

-    **Width of Landing|FloatList**: Se **Number Of Steps** è 1, l\'oggetto scala funge da pianerottolo. Quando questo è il caso e la linea di base è multisegmento, la larghezza del primo segmento del pianerottolo segue **Width**, le larghezze dei segmenti successivi seguono l\'elenco qui impostato.


{{TitleProperty|Steps}}

-    **Blondel Ratio|Float**: (sola lettura) Il calcolo del rapporto Blondel. Questo rapporto indica scale comode e dovrebbe essere compreso tra 62 e 64 cm o 24,5 e 25,5 pollici.

-    **Landing Depth|Length**: La profondità del pianerottolo della rampa, se abilitato in **Landings**. Il valore predefinito va a **Width** se impostato a 0.

-    **Nosing|Length**: La dimensione del paragradino.

-    **Number Of Steps|Integer**: Il numero di gradini (alzate). Devono essere almeno 2 per una rampa unica, e almeno 4 per una scala con pianerottolo centrale.

-    **Riser Height|Length**: (sola lettura) L\'altezza delle alzate. Se **Riser Height Enforce** è 0 viene calcolato (**Height** / **Number of Steps**). Altrimenti è uguale a **Riser Height Enforce**.

-    **Riser Height Enforce|Length**: L\'altezza imposta alle alzate.

-    **Riser Thickness|Length**: Lo spessore dei montanti.

-    **Tread Depth|Length**: (sola lettura) La profondità dei gradini. Se **Tread Depth Enforce** è 0 viene calcolato (**Length** / **Number of Steps**). Altrimenti è uguale a **Tread Depth Enforce**.

-    **Tread Depth Enforce|Length**: La profondità imposta ai gradini.

-    **Tread Thickness|Length**: Lo spessore dei gradini.


{{TitleProperty|Structure}}

-    **Connection Down Start Stairs|Enumeration**: Il tipo di collegamento tra il solaio del piano inferiore e l\'inizio delle scale. Può essere {{value|HorizontalCut}}, {{value|VerticalCut}} o {{value|HorizontalVerticalCut}}.

-    **Connection End Stairs Up|Enumeration**: Il tipo di collegamento tra l\'estremità delle scale e il solaio del piano superiore. Può essere {{value|toFlightThickness}} o {{value|toSlabThickness}}.

-    **Down Slab Thickness|Length**: Lo spessore della soletta del piano inferiore.

-    **Flight|Enumeration**: La direzione della rampa dopo il pianerottolo. Può essere {{value|Straight}}, {{value|HalfTurnLeft}} o {{value|HalfTurnRight}}.

-    **Landings|Enumeration**: Il tipo di pianerottoli. Può essere {{value|None}} o {{value|At center}} ({{value|At each corner}} non ancora implementato).

-    **Stringer Overlap|Length**: La sovrapposizione dei traversi nella parte inferiore dei gradini.

-    **Stringer Width|Length**: La larghezza delle traverse.

-    **Structure|Enumeration**: Il tipo di struttura delle scale. Può essere{{value|None}}, {{value|Massive}}, {{value|One stringer}} o {{value|Two stringers}}.

-    **Structure Offset|Length**: distanza tra il bordo degli scalini e la struttura di sostegno.

-    **Structure Thickness|Length**: Lo spessore della struttura.

-    **Up Slab Thickness|Length**: Lo spessore della soletta del piano superiore.

-    **Winders|Enumeration**: Il tipo di gradini a ventaglio. Non implementato.



## Limitazioni


<div class="mw-translate-fuzzy">

-   Al momento sono disponibili solo scale dritte
-   Vedere [nel forum](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) per scale circolari.
-   Per seguire l\'evoluzione dello strumento consultare la pagina [Arch Stairs](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564) nel forum


</div>



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Le Scale possono essere create con le [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione: 
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
⏵ [documentation index](../README.md) > Arch Stairs/it
