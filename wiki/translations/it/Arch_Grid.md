---
- GuiCommand:
   Name: Arch Grid
   Name/it: Griglia
   MenuLocation: Arch -> Assi -> Griglia
   Workbenches: Arch_Workbench/it
   SeeAlso: Arch Axis/it, Arch AxisSystem/it
---

# Arch Grid/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Arch_Grid.svg  style="width:16px;"> Griglia consente di posizionare nel documento un oggetto simile a una griglia. Questo oggetto ha lo scopo di fungere da base per costruire oggetti Arch che richiedono una trama regolare ma complessa, come finestre, facciate continue, griglie di colonne, ringhiere, ecc. L\'oggetto Grid è modificabile come un foglio di calcolo, dove è possibile aggiungere o rimuovere colonne e righe, definire le loro dimensioni e unire le celle.


</div>


<div class="mw-translate-fuzzy">

La Griglia è un oggetto 2D e quindi può essere utilizzato ovunque sia necessaria una forma 2D, ad esempio in un [Disegno](Draft_Workbench/it.md) o uno [Schizzo](Sketcher_Workbench/it.md), ma può anche comportarsi come un [Sistema di assi ](Arch_AxisSystem/it.md), e può essere utilizzato per propagare il posizionamento di altri oggetti Arch.


</div>

<img alt="" src=images/Arch_Grid_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">



*Una serie di colonne, un sistema di ringhiere e una finestra, ciascuna basata su un oggetto [Griglia](Arch_Grid/it.md).*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Presmere il pulsante **<img src="images/Arch_Grid.svg" width=16px> [Griglia](Arch_Grid/it.md)**.
2.  Impostare **Larghezza** e **Altezza** della griglia nelle proprietà.
3.  Entrare nella modalità di modifica facendo doppio clic sull\'oggetto griglia nella vista ad albero.
4.  Aggiungere righe e colonne.
5.  Impostare la larghezza e l\'altezza desiderate di righe e colonne facendo doppio clic sulle intestazioni delle righe o colonne.


</div>

## Opzioni

-   Una larghezza di colonna o altezza di riga pari a 0 significa che le sue dimensioni saranno adattate automaticamente per adattarsi alla larghezza o altezza totale della griglia.
-   Le celle possono essere unite e separate selezionandole e facendo clic sul pulsante appropriato.
-   Quando viene usata come proprietà **Axis** di altri oggetti Arch, la griglia guida il posizionamento di questi oggetti. La proprietà **Points Output** definisce come sono posizionati gli oggetti sulla griglia: ai vertici, nei punti medi del bordo o al centri delle facce.
-   Impostando le proprietà **Auto Height** o **Auto Width** su un valore diverso da zero, il numero totale di righe o colonne e le loro altezze o larghezze individuali viene ignorato. Invece, viene automaticamente creato il numero massimo di colonne o righe della larghezza o altezza automatica specificata.

## Proprietà

-    {{PropertyData/it|Rows}}: Numero di righe

-    {{PropertyData/it|Columns}}: Numero di colonne

-    {{PropertyData/it|Row Size}}: Dimensione delle righe

-    {{PropertyData/it|Column Size}}: Dimensione delle colonne

-    {{PropertyData/it|Points Output}}: Il tipo di punti 3D prodotti da questo oggetto griglia

-    {{PropertyData/it|Width}}: La larghezza totale di questa griglia

-    {{PropertyData/it|Height}}: L\'altezza totale di questa griglia

-    {{PropertyData/it|Auto Width}}: Crea divisioni di colonna automatiche (impostare su 0 per disabilitare)

-    {{PropertyData/it|Auto Height}}: Crea divisioni di riga automatiche (impostare su 0 per disabilitare)

-    {{PropertyData/it|Reorient}}: Quando si trova in modalità punto medio, stabilisce se questa griglia deve riorientamento i propri figli lungo le normali del bordo o meno

-    {{PropertyData/it|Hidden Faces}}: Gli indici delle facce da nascondere

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Griglia può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
Grid = makeGrid(name="Grid")
```

-   Crea un oggetto `Grid`.

I suoi attributi `Width`, `Height`, `Rows`, e `Columns` possono essere modificati direttamente per definire l\'aspetto della griglia.


```python
import FreeCAD, Draft, Arch
Grid = Arch.makeGrid()

Grid.Width = 5000
Grid.Height = 5000
Grid.Rows = 4
Grid.Columns = 6
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = Grid
FreeCAD.ActiveDocument.recompute() 
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Grid/it
