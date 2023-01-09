---
- GuiCommand:/it
   Name:Draft Arc
   Name/it:Arco
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Arco
   Shortcut:**A** **R**
   SeeAlso:[Circonferenza](Draft_Circle/it.md), [Ellipse](Draft_Ellipse/it.md), [Arco da 3 punti](Draft_Arc_3Points/it.md)
   Version:0.7
---

# Draft Arc/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Crea un arco nel [piano di lavoro](Draft_SelectPlane/it.md). Si può definire l\'arco inserendo quattro punti, il centro, il raggio, il primo punto e l\'ultimo punto, oppure selezionando le tangenti, oppure con qualsiasi combinazione di questi elementi. L\'arco assume [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati in precedenza nella [barra di Draft](Draft_Tray/it.md).


</div>

A Draft Arc is in fact a [Draft Circle](Draft_Circle.md) with a **First Angle** that is not the same as its **Last Angle**.

<img alt="" src=images/Draft_Arc_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Arco definito da quattro punti: centro, raggio, punto iniziale dell'arco e punto finale dell'arco.*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

### Utilizzo

1.  Premere il pulsante **<img src="images/Draft_Arc.svg" width=16px> [Arco](Draft_Arc/it.md)
**, o premere i tasti **A** e **R**
2.  Selezionare un primo punto nella vista 3D per stabilire il centro, oppure digitare le sue coordinate poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**.
3.  Selezionare un secondo punto nella vista 3D, o introdurre il valore del raggio.
4.  Selezionare un terzo punto nella vista 3D, o introdurre l\'angolo iniziale
5.  Selezionare un quarto punto nella vista 3D, o introdurre l\'angolo di apertura


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opzioni

-   L\'uso principale dello strumento arco è selezionando quattro punti: il centro, un punto sulla circonferenza, l\'inizio dell\'arco e la sua fine.
    -   Premendo **Alt**, si può selezionare una tangente invece diselezionare un punto, per definire il cerchio di base dell\'arco. È quindi possibile costruire diversi tipi di cerchi selezionando una, due o tre tangenti.
-   La direzione dell\'arco dipende dal movimento che si sta facendo con il mouse. Se si inizia il movimento in senso orario dopo aver inserito il terzo punto, l\'arco va in senso orario. Per andare in senso antiorario, spostare semplicemente il mouse indietro sul terzo punto, finché l\'arco inizia a disegnare nell\'altra direzione.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Arco si riavvia dopo aver terminato l\'arco in costruzione, e consente di disegnarne un nuovo arco senza premere nuovamente il pulsante dello strumento.
-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il prossimo punto in orizzontale o in verticale rispetto all\'ultimo.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

L\'arco può essere modificato facendo doppio clic sull\'elemento nella vista ad albero o premendo il pulsante **<img src="images/Draft_Edit.svg" width=16px> [Modifica](Draft_Edit/it.md)**. Quindi si può spostare il punto centrale in una nuova posizione.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, radii and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.

## Properties


<div class="mw-translate-fuzzy">

## Proprietà

Un oggetto Arco condivide tutte le proprietà di un [Cerchio](Draft_Circle/it.md), ma alcune proprietà hanno senso solo per il cerchio.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Arco può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](FreeCAD_Scripting_Basics/it.md) utilizzando la stessa funzione per creare cerchi, con argomenti aggiuntivi. Vedi le informazioni in [Cerchio](Draft_Circle/it.md).


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

arc1 = Draft.make_circle(200, startangle=0, endangle=90)
arc2 = Draft.make_circle(500, startangle=20, endangle=160)
arc3 = Draft.make_circle(750, startangle=-30, endangle=-150)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Arc/it
