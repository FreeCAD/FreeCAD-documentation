---
- GuiCommand:/it
   Name:Draft Rotate
   Name/it:Ruota
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Ruota
   Shortcut:**R** **O**
   SeeAlso:[Sposta](Draft_Move/it.md), [Serie](Draft_Array/it.md)
   Version:0.7
---

# Draft Rotate/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento ruota o copia e ruota gli oggetti selezionati di un determinato angolo attorno a un punto di riferimento.


</div>


<div class="mw-translate-fuzzy">

Lo strumento Ruota può essere utilizzato su forme 2D create con [Draft](Draft_Workbench/it.md) o [Schizzo](Sketcher_Workbench/it.md), ma può anche essere utilizzato su molti tipi di oggetti 3D come quelli creati con [Part](Part_Workbench/it.md) o [Arch](Arch_Workbench/it.md).


</div>

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Rotazione di un oggetto usando un punto di riferimento, da un angolo di riferimento a un altro angolo*


</div>

## Utilizzo

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selezionare gli oggetti che si desidera ruotare o copiare
2.  Premere il pulsante **<img src="images/Draft_Rotate.svg" width=16px> [Ruota](Draft_Rotate/it.md)**, or press premere i tasi **R** e poi **O**. Se nessun oggetto è selezionato, si viene inviti a selezionarne uno.
3.  Selezionare un primo punto nella vista 3D, oppure digitare le sue coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Aggiungi punto**. Questo punto serve da punto base dell\'operazione, attraverso il quale passerà l\'asse di rotazione.
4.  Fare clic su un secondo punto nella vista 3D o digitare un angolo base. Questo definisce una linea di base che ruoterà attorno al primo punto.
5.  Fare clic su un terzo punto nella vista 3D o digitare un angolo di rotazione. Questo indica la rotazione della linea di base, e quindi degli oggetti.


</div>

## Opzioni

The single character keyboard shortcuts and the modifier key mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Premere **X**, **Y** o **Z** dopo un punto per vincolare il prossimo punto sull\'asse dato.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati per inserire il punto.
-   Premere **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Ruota viene riavviato al termine dell\'operazione, consentendo di ruotare o copiare nuovamente gli oggetti senza premere nuovamente il pulsante dello strumento.
-   Premere **P** oppure fare clic sulla casella di controllo per attivare la modalità *Copia*. Se la modalità copia è attiva, lo strumento Ruota mantiene la forma originale al suo posto e crea una copia con l\'angolo impostato impostato dal terzo punto.

:   Si possono usare sia **T** che **P** per posizionare più copie in sequenza. In questo caso, l\'elemento che viene duplicato è l\'ultima copia posizionata.

-   Tenere premuto **Alt** dopo il secondo punto per attivare o disattivare la modalità di copia. Tenendo premuto **Alt** dopo aver cliccato sul terzo punto, si può continuare a posizionare le copie usando lo stesso punto base di rotazione e la stessa linea di base; rilasciare **Alt** per terminare l\'operazione e vedere tutte le copie.
-   Tenere premuto **Ctrl** mentre si ruota per forzare lo [snap](Draft_Snap.md) al punto di aggancio più vicino, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si ruota per [vincolare](Draft_Constrain.md) il secondo punto in orizzontale o in verticale rispetto al primo.
-   Premere il pulsante **Esc** o **Chiudi** per interrompere il comando corrente; le copie già posizionate rimangono.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be rotated with the Draft Rotate command. To rotate it either its **Support** object has to be rotated, or its **Attachment Offset** has to be changed.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To store and reuse the same copy mode setting across commands: **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Ruota può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```


<div class="mw-translate-fuzzy">

-   Ruota il punto base degli oggetti della `objectlist` di un dato `angle`.
    -   
        `objectlist`
        
        può essere un singolo oggetto o un elenco di oggetti.

    -   Se sono dati un punto base di rotazione (`center`), e un `axis`, essi sono usati; altrimenti la rotazione è basata sull\'origine e attorno all\'asse Z.

:   L\'angolo di rotazione è relativo al punto base dell\'oggetto, il che significa che se un oggetto viene ruotato di 45 gradi e poi di altri 45 gradi, in totale ruota di 90 gradi dalla sua posizione originale.

-   Se `copy` è `True` vengono create delle copie invece di ruotare gli oggetti originali.
-   Viene restituita una `rotatedlist` con gli oggetti originali ruotati o con le nuove copie.
    -   
        `rotatedlist`
        
        è un singolo oggetto o un elenco di oggetti, a seconda dell\'input di `objectlist`.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=300)
Draft.move(polygon1, App.Vector(1000, 0, 0))

# Rotation around the origin
angle1 = 45
rot2 = Draft.rotate(polygon1, angle1, copy=True)
rot3 = Draft.rotate(polygon1, 2*angle1, copy=True)
rot4 = Draft.rotate(polygon1, 4*angle1, copy=True)

polygon2 = Draft.make_polygon(3, radius=1000)
polygon3 = Draft.make_polygon(5, radius=500)
Draft.move(polygon2, App.Vector(2000, 0, 0))
Draft.move(polygon3, App.Vector(2000, 0, 0))

# Rotation around another point
angle2 = 60
cen = App.Vector(3100, 0, 0)
list2 = [polygon2, polygon3]
rot_list2 = Draft.rotate(list2, angle2, center=cen, copy=True)
rot_list3 = Draft.rotate(list2, 2*angle2, center=cen, copy=True)
rot_list4 = Draft.rotate(list2, 4*angle2, center=cen, copy=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/it
