---
- GuiCommand:
   Name:Arch Pipe
   Name/it:Tubo
   MenuLocation:Arch → Tubazioni → Tubo
   Workbenches:[Arch](Arch_Workbench/it.md)
   Shortcut:**P** **I**
   Version/it:0.17
   SeeAlso:[Raccordo](Arch_PipeConnector/it.md), [Arredo](Arch_Equipment/it.md)
---

# Arch Pipe/it

## Descrizione

Questo strumento permette di creare delle tubazioni partendo da zero, o dagli oggetti selezionati. Gli oggetti selezionati devono essere Part-based (Draft, Schizzo, ecc ..) e contenere una e una sola polilinea (wire) aperta,

## Utilizzo

1.  Facoltativamente, selezionare una forma [Part](Part_Workbench/it.md) lineare come una [Linea](Draft_Line/it.md), una [Wire](Draft_Wire/it.md) o uno [Schizzo](Sketcher_NewSketch/it.md) aperto.
2.  Richiamare questo comando utilizzando uno di questi metodi:
    -   Premere il pulsante **<img src="images/Arch_Pipe.svg" width=16px> [Tubo](Arch_Pipe/it.md)** nella barra degli strumenti.
    -   Premere i tasti **P** e poi **I** da tastiera.
    -   Usare la voce **Arch → Strumenti tubazioni → Tubo** del menu principale.

## Opzioni

-   Gli elementi Tubo condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)

## Proprietà

-    {{PropertyData/it|Length}}: Imposta la lunghezza del tubo, quando non si basa su una polilinea

-    {{PropertyData/it|Diameter}}: Il diametro del tubo, quando non si basa su un profilo

-    {{PropertyData/it|Base}}: L\'eventuale polilinea su cui si basa il tubo

-    {{PropertyData/it|Profile}}: Il profilo di base del tubo. Se non è dato, il tubo è di forma cilindrica.

## Flusso di lavoro tipico 

-   Iniziare collocando degli apparecchi sanitari o idraulici (il wc della figura sottostante è un file step importato). Commutare questi oggetti in Arch Equipment selezionandoli e premendo il tasto [Arredo](Arch_Equipment/it.md).

![](images/Arch_pipe_example_01.jpg )


<div class="mw-translate-fuzzy">

-   Gli oggetti Arch Equipment ora hanno una nuova proprietà **SnapPoints**, che è una lista di vettori 3D. Questo consente di aggiungere dei punti di aggancio personalizzati, a cui è possibile ancorarsi quando il nuovo tasto snap [Speciale](Draft_Snap_Special/it.md) è attivo. Attualmente però la proprietà è disponibile solo per python. Nel caso sopra è stato aggiunto un nuovo punto di snap all\'uscita dell\'apparecchio wc. I vettori all\'interno di SnapPoints appaiono sul modello come puntini bianchi:


</div>

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )

-   Con il nuovo snap [\"Speciale\"](Draft_Snap_Special/it.md) di Draft è possibile agganciarsi a questi punti personalizzati:

![](images/Arch_pipe_example_03.jpg )

-   Ora è possibile disegnare le tubazioni con Linee e Polilineee di Draft, o con Schizzi. Comunque, il modo migliore è quello di usare solo Linee di Draft:

![](images/Arch_pipe_example_04.jpg )


<div class="mw-translate-fuzzy">

-   Vi è ora un nuovo strumento [Pendenza](Draft_Slope/it.md) che permette di modificare la pendenza delle linee Draft, per esempio del 5% (0.05). Così si può rapidamente dare alle linee delle tubazioni di scarico una pendenza corretta. Questo strumento modifica solo le coordinate z, quindi basta agganciarle l\'un l\'altra, la proiezione dall\'alto resta invariata.


</div>

![](images/Arch_pipe_example_05.jpg )

-   Ora basta selezionare tutte le linee, e premere il pulsante [Tubo](Arch_Pipe/it.md). Arch Tubo funziona con qualsiasi oggetto Part-based che contenga una e una sola polilinea aperta.

![](images/Arch_pipe_example_06.jpg )

-   Ora si possono creare le connessioni selezionando 2 o 3 tubi coincidenti, e premendo il tasto [Raccordo](Arch_PipeConnector/it.md). Se sono selezionati 3 tubi, due di essi devono essere allineati per creare un elemento tee o braga:

![](images/Arch_pipe_example_07.jpg )

-   Cambiando il raggio dei raccordi non si non cambia la lunghezza della linea di base sottostante, ma solo la lunghezza del tubo risultante (dato che cambia la sua proprietà OffsetStart o OffsetEnd). Così si può disegnare il percorso solo con linee rette, senza doversi preoccupare delle curve e dei raggi.

È anche possibile creare Tubi Arch senza una linea di base, in questo caso utilizzare la proprietà \"Length\" per definire la lunghezza.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Tubo può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
Pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Creates a `Pipe` object from the given `baseobj` and `diameter`.
    -   
        `baseobj`
        
        is a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).

    -   If `baseobj` is omitted, a straight pipe can be created with just the `diameter` and the `length` in the Z direction.
-   If a `placement` is given, it is used.


```python
import Draft, Arch

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2500, 200, 0)
p3 = FreeCAD.Vector(3100, 1000, 0)
p4 = FreeCAD.Vector(3500, 500, 0)
Line = Draft.makeWire([p1, p2, p3, p4])

Pipe = Arch.makePipe(Line, 200)
FreeCAD.ActiveDocument.recompute()

Pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Pipe/it
