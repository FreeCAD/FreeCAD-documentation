---
- GuiCommand:/it
   Name:Draft Wire
   Name/it:Polilinea
   MenuLocation:Drafting → Polilinea
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   Shortcut:**P** **L**
   Version:0.7
   SeeAlso:[Linea](Draft_Line/it.md), [BSpline](Draft_BSpline/it.md)
---

# Draft Wire/it

## Descrizione

Il comando <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> **Polilinea** [crea](#Create.md) una polilinea, ovvero una sequenza di segmenti di linea collegati. Il comando può anche essere usato per [unire](#Join.md) [Linee](Draft_Line.md) e Polilinee.

I vertici di una Polilinea possono essere raccordati (stondati) o smussati cambiando le sue **Fillet Radius** or **Chamfer Size** rispettivamente. E\' anche possibile suddividere i bordi di una Polilinea cambiando la sua **Subdivisions** proprietà.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;"> 
*Polilinea definita da più punti*

## Create


<div class="mw-translate-fuzzy">

## Utilizzo


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Wire.svg" width=16px> [Polilinea](Draft_Wire/it.md)**, o premere i tasti **P** e **L**.
2.  Selezionare il primo punto nella vista 3D, o digitare le coordinate e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**.
3.  Selezionare un punto successivo nella vista 3D, o digitare le coordinate e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**.
4.  Premere **Esc** o il pulsante **Chiudi** per completare l\'editazione.


</div>


<div class="mw-translate-fuzzy">

## Opzioni


</div>

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Premere il tasto **A** o il pulsante **<img src="images/Draft_FinishLine.svg" width=12px> |Termina** per finire la polilinea lasciandola aperta.
-   Premere il tasto **O** o il pulsante **<img src="images/Draft_CloseLine.svg" width=12px> Chiudi** per chiudere la polilinea, prciò viene aggiunto un segmento dall\'ultimo punto al primo per formare una faccia. Per formare una faccia sono necessari almeno tre punti.
-   Premere il tasto **W** o il pulsante **<img src="images/Draft_Wipe.svg" width=12px> Pulisci** per rimuovere i segmenti di linea già posizionati, ma continuare a editare la polilinea dall\'ultimo punto.
-   Premere il tasto **U** o il pulsante **<img src="images/Draft_SelectPlane.svg" width=12px> [Imposta il piano](Draft_SelectPlane.md)** per adattare il piano di lavoro corrente all\'orientamento dell\'ultimo punto.
-   Premere il tasto **X**, o **Y** o **Z** dopo un punto per vincolare il prossimo punto sull\'asse dato.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z.. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **R** oppure fare clic sulla casella di controllo per attivare la modalità \"relativo\". Se la modalità relativo è attiva, le coordinate del punto successivo sono relative all\'ultimo; in caso contrario, sono assolute, prese dall\'origine (0,0,0).
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Polilinea si riavvia dopo aver terminato la polilinea in costruzione, e consente di disegnare una nuova polilinea senza premere nuovamente il pulsante dello strumento.
-   Premere il tasto **L** oppure fare clic sulla casella di controllo per attivare la modalità *riempito*. Se la modalità di riempimento è attiva, una polilinea chiusa crea una faccia piena (**Make Face** `True`); in caso contrario, la polilinea chiusa non crea una faccia (**Make Face** `False`).

:   
    **Note:**la polilinea non deve essere riempita se si autointerseca , perché in questo caso non crea una faccia corretta. Se la polilinea è piena ma non è visibile alcuna forma, impostare manualmente **Make Face** su `False` per vedere la polilinea.

-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il prossimo punto in orizzontale o in verticale rispetto all\'ultimo.
-   Premere i tasti **Ctrl**+**Z** o premere il pulsante {{button|<img src="images/Draft_UndoLine.svg" width=12px> Undo}} per annullare l\'ultimo punto.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente; i segmenti di linea già posizionati rimamgono.


</div>

## Join

### Usage

1.  The end points of the [Draft Lines](Draft_Line.md) and/or Draft Wires to be joined must be exactly coincident. If required first adjust points to ensure that this is the case.
2.  Select two or more [Draft Lines](Draft_Line.md) and/or Draft Wires.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Wire.svg" width=16px> [Draft Wire](Draft_Wire.md)** button.
    -   Select the **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polyline** option from the menu.
    -   Use the keyboard shortcut: **P** then **L**.

## Notes


<div class="mw-translate-fuzzy">

La polilinea può essere modificata facendo doppio clic sull\'elemento nella vista ad albero o premendo il pulsante **<img src="images/Draft_Edit.svg" width=16px> [Modifica](Draft_Edit/it.md)**. Quindi si può spostare i punti in una nuova posizione o fare clic su **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto** o **<img src="images/Draft_DelPoint.svg" width=16px> rimuovi punto** e quindi fare clic sul wire per aggiungere o rimuovere punti.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Wire object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Dati

-    **Start**: specifica il primo punto nel filo.

-    **End**: specifica l\'ultimo punto nel filo, senza contare il punto iniziale se il filo è chiuso.

-    **Closed**: specifica se il filo è chiuso o meno. Se il filo è inizialmente aperto, questo valore è `False`; impostandolo su `True` disegna un segmento di linea per chiudere il filo. Se il filo è inizialmente chiuso, questo valore è `True`; impostandolo su `False` si rimuove l\'ultimo segmento di linea e si apre il filo.

-    **Chamfer Size**: specifica la dimensione degli smussi (segmenti retti) creati agli angoli del filo.

-    **Fillet Radius**: specifica il raggio dei raccordi (segmenti di arco) creati agli angoli del filo.

-    **Make Face**: specifica se il filo crea una faccia o no. Se è `True` viene creata una faccia, altrimenti solo i bordi sono considerati parte dell\'oggetto. Questa proprietà funziona solo se **Closed** è `True`.

:   
    **Note:**non impostare **Make Face** su `True` se il filo si interseca, poiché non crea una faccia corretta.

-    **Subdivisions**: specifica il numero di nodi interni in ciascun segmento del filo. {{version/it|0.16}}

-    **Length**: (sola lettura) specifica la lunghezza dell\'intero filo.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Vista

-    **End Arrow**: se è `True` viene visualizzato un simbolo all\'ultimo punto del wire, quindi può essere usato come una linea di annotazione.

-    **Arrow Size**: specifica la dimensione del simbolo visualizzato alla fine del wire.

-    **Arrow Type**: specifica il tipo di simbolo visualizzato alla fine del filo, che può essere \"Dot\", \"Circle\", \"Arrow\", o \"Tick\".

-    **Pattern**: specifica un tipo di [Campitura](Draft_Pattern/it.md) con cui riempire la faccia del filo chiuso. Questa proprietà funziona solo se **Make Face** è `True`, e se **Display Mode** è \"Flat Lines\".

-    **Pattern Size**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento DWire può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Wire` con l\'elenco di punti indicato, `pointslist`.
    -   Ogni punto nella lista è definito dal suo `FreeCAD.Vector`, con unità in millimetri.
    -   In alternativa, l\'input può essere una `Part.Wire`, da cui vengono estratti i punti.
-   Se `closed` è `True`, o se il primo e l\'ultimo punto coincidono, la polilinea è chiusa.
-   Se viene dato un `placement` esso viene usato; altrimenti la forma viene creata nell\'origine.
-   Se `face` è `True` e la polilinea è chiusa, diventa una faccia e appare riempita.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/it
