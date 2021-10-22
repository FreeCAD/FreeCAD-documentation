---
- GuiCommand:/it
   Name:Draft Stretch
   Name/it:Stira
   MenuLocation:Draft → Stira
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**S** **H**
   Version:0.17
   SeeAlso:[Offset](Draft_Offset/it.md), [Scala](Draft_Scale/it.md)
---

# Draft Stretch/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Stretch.svg  style="width:16px;"> Stira allunga un oggetto spostando alcuni dei suoi vertici selezionati. L\'azione equivalente è la modifica dell\'oggetto e lo spostamento manuale dei punti in una nuova posizione.


</div>

<img alt="" src=images/Draft_Stretch_Example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Allungamento di tre polilinee racchiudendo alcuni vertici e spostandoli in un'altra posizione*


</div>

## Utilizzo

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Uso

1.  Selezionare un oggetto che si desidera stirare
2.  Premere il pulsante **<img src="images/Draft_Stretch.svg" width=16px> [Stira](Draft_Stretch/it.md)**. Se nessun oggetto è selezionato, si viene invitati a selezionarne uno
3.  Fare clic su un primo punto nella vista 3D o digitare una [coordinata](Draft_Coordinates/it.md) e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
4.  \# Fare clic su un secondo punto nella vista 3D o digitare una [coordinata](Draft_Coordinates/it.md) e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**. Questi primi due punti definiscono un rettangolo di selezione. I vertici dell\'oggetto originale racchiusi da questo rettangolo diventano evidenziati.
5.  \# Fare clic su un terzo punto nella vista 3D o digitare una [coordinata](Draft_Coordinates/it.md) e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
6.  \# Fare clic su un quarto punto nella vista 3D o digitare una [coordinata](Draft_Coordinates/it.md) e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**. La seconda coppia di punti definisce una linea, la cui distanza e direzione sono utilizzate per allungare la figura attaccata ai punti evidenziati.


</div>

## Opzioni

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Premere **X**, **Y** o **Z** dopo il primo punto per vincolare il secondo punto su un dato asse.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** tra ciascun componente X, Y e Z.
-   Premere **R** o fare clic sulla casella di controllo per attivare la modalità \"relativa\". Se la modalità relativa è attiva, le coordinate del secondo punto sono relative alla prima; se no, sono assolute, prese dall\'origine (0,0,0).
-   Premere **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Simmetria si riavvia dopo aver assegnato il secondo punto, consentendo di inserire un altro oggetto senza premere nuovamente il pulsante dello strumento.
-   Tenere premuto **Ctrl** mentre si disegna per forzare lo [snap](Draft_Snap.md) al punto di aggancio più vicino, indipendentemente dalla distanza.
-   Tenere premuto **Shift** mentre si disegna per [vincolare](Draft_Constrain.md) il secondo punto in orizzontale o in verticale rispetto al primo.
-   Premere il pulsante **Esc** o **Chiudi** per interrompere il comando corrente.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Per lo strumento Stira non esiste un\'interfaccia di programmazione disponibile. Tutto ciò che fa è cambiare alcuni attributi degli oggetti Draft selezionati, come `Placement`, `Points`, `Length`, o `Height`, che si traduce in una forma stirata.


</div>


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Stretch/it
