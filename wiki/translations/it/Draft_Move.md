---
- GuiCommand:/it
   Name:Draft_Move
   Name/it:Sposta
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Sposta
   Shortcut:**M** **V**
   SeeAlso:[Schiera](Draft_Array/it.md), [Copie su tracciato](Draft_PathArray/it.md)
   Version:0.7
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento sposta o copia gli oggetti selezionati da un punto ad un altro punto.


</div>


<div class="mw-translate-fuzzy">

Lo strumento Sposta può essere utilizzato su forme 2D create con [Draft](Draft_Workbench/it.md) o [Schizzo](Sketcher_Workbench/it.md), ma può anche essere utilizzato su molti tipi di oggetti 3D come quelli creati con [Part](Part_Workbench/it.md) o [Arch](Arch_Workbench/it.md).


</div>

<img alt="" src=images/Draft_Move_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Spostare un oggetto da un punto a un altro*


</div>

## Utilizzo

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selezionare gli oggetti che si desidera spostare o copiare
2.  Premere il pulsante **<img src="images/Draft_Move.svg" width=16px> [Sposta](Draft_Move/it.md)**, o premere i tasti **M** e poi **V**. Se nessun oggetto è selezionato, viene chiesto di selezionarne uno.
3.  Selezionare un primo punto nella vista 3D, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**. Questo punto serve come punto base dell\'operazione.
4.  Fare clic su un altro punto nella vista 3D o digitare una [coordinata](Draft_Coordinates/it.md) e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**. Questo punto è la nuova posizione del punto base.


</div>

## Opzioni

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Premere **X**, **Y** o **Z** dopo il primo punto per vincolare il secondo punto su un dato asse.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** tra ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)** quando si hanno i valori desiderati per inserire il punto.
-   Premere **R** o fare clic sulla casella di controllo per attivare la modalità \"relativa\". Se la modalità relativa è attiva, le coordinate del secondo punto sono relative alla prima; altrimenti sono assolute, prese dall\'origine (0,0,0).
-   Premere **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Sposta verrà riavviato al termine dell\'operazione, consentendo di spostare o copiare nuovamente gli oggetti senza premere nuovamente il pulsante dello strumento.
-   Premere **P** oppure fare clic sulla casella di controllo per attivare la modalità *Copia*. Se la modalità copia è attiva, lo strumento Sposta mantiene la forma originale al suo posto e crea una copia nel secondo punto.

:   Si possono usare sia **T** che **P** per posizionare più copie in sequenza. In questo caso, l\'elemento che viene duplicato è l\'ultima copia posizionata.

-   Tenere premuto **Alt** dopo il secondo punto per attivare o disattivare la modalità di copia. Tenendo premuto **Alt** dopo aver cliccato sul secondo punto, si può continuare a posizionare altre copie; rilasciare **Alt** per terminare l\'operazione e vedere tutte le copie.
-   Tenere premuto **Ctrl** mentre si sposta per forzare lo [snap](Draft_Snap.md) al punto di aggancio più vicino, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si ruota per [vincolare](Draft_Constrain.md) il secondo punto in orizzontale o in verticale rispetto al primo.
-   Premere il pulsante **Esc** o il pulsante **Chiudi** per interrompere il comando corrente; le copie già posizionate rimangono.


</div>

## Notes

-   An Object that is [attached](Part_Attachment.md) cannot be moved with the Draft Move command. To move it either its **Support** object has to be moved, or its **Attachment Offset** has to be changed.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles: {{MenuCommand|Edit → Preferences... → General → Units → Units settings → Number of decimals}}.
-   To change the initial focus of the task panel to the {{MenuCommand|Length}} input box: {{MenuCommand|Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate}}. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   To store and reuse the same copy mode setting across commands: {{MenuCommand|Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode}}.
-   To reselect the base objects after copying objects: {{MenuCommand|Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying}}.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Sposta può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
moved_list = move(objectslist, vector, copy=False)
```


<div class="mw-translate-fuzzy">

-   Sposta il punto base degli oggetti della `objectslist` di una distanza e nella direzione indicati da `vector`.
    -   
        `objectslist`
        
        può essere un singolo oggetto o un elenco di oggetti.

:   Il vettore di spostamento è relativo al punto base dell\'oggetto, il che significa che se un oggetto viene spostato di 2 unità e poi di altre 2 unità, in totale viene spostato di 4 unità dalla sua posizione originale.

-   Se `copy` è `True` vengono create delle copie invece di spostare gli oggetti originali.
-   Viene restituita una `movedlist` con gli oggetti originali spostati o con le nuove copie..
    -   
        `movedlist`
        
        è un singolo oggetto o un elenco di oggetti, a seconda dell\'input di `objectslist`.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
