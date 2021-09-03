---
- GuiCommand:/it
   Name:Draft BSpline
   Name/it:B-spline
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → B-spline
   Shortcut:**B** **S**
   SeeAlso:[Polilinea](Draft_Wire/it.md), [Curva di Bezier](Draft_BezCurve/it.md)
   Version:0.7
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_BSpline.svg  style="width:16px;"> B-spline crea una linea flessibile, passante per i punti selezionati nel [piano di lavoro](Draft_SelectPlane/it.md) corrente. La B-spline assume [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati nella [barra di Draft](Draft_Tray/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento B-spline specifica i punti esatti attraverso i quali deve passare la curva; invece lo strumento <img alt="" src=images/Draft_BezCurve.svg  style="width:16px;"> [Curva di Bezier](Draft_BezCurve/it.md) usa i **punti di controllo** per definire l\'andamento della curva. Per creare curve circolari o ellittiche esatte, usare <img alt="" src=images/Draft_Arc.svg  style="width:16px;"> [Arco](Draft_Arc/it.md) e <img alt="" src=images/Draft_Ellipse.svg  style="width:16px;">[Ellisse](Draft_Ellipse/it.md).


</div>

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*S-pline definita da più punti*

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_BSpline.svg" width=16px> [B-spline](Draft_BSpline/it.md)**, o premere i tasti **B** e poi **S**.
2.  Selezionare il primo punto nella vista 3D, o digitare le [coordinate](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
3.  Selezionare un altro punto nella vista 3D, o digitare le sue [coordinate](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
4.  Premere **Esc** o il pulsante **Close** per completare l\'editazione.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opzioni

-   Premere il tasto **A** o il pulsante **<img src="images/Draft_FinishLine.svg" width=12px> [Termina](Draft_FinishLine/it.md)** pulsante per terminare la spline, lasciandola aperta.
-   Premere il tasto **O** o il pulsante **<img src="images/Draft_CloseLine.svg" width=12px> [Chiudi](Draft_CloseLine/it.md)** per chiudere la spline, questo aggiuge una curva dall\'ultimo punto al primo per formare una faccia. Sono necessari almeno tre punti per formare una faccia.
-   Premere il tasto **W** o il pulsante **<img src="images/Draft_Wipe.svg" width=12px> [Pulisci](Draft_Wipe/it.md)** per rimuovere i tratti di curva già posizionati, ma continuare a creare la spline dall\'ultimo punto.
-   Premere il tasto **U** o il pulsante **<img src="images/Draft_SelectPlane.svg" width=12px> [Imposta il piano](Draft_SelectPlane/it.md)** per posizionare il piano di lavoro corrente nell\'orientamento dell\'ultimo punto.
-   Premere il tasto **X**, o **Y** o **Z** dopo un punto per vincolare il successivo punto sul dato asse.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **R** oppure fare clic sulla casella di controllo per attivare la modalità \"relativo\". Se la modalità relativo è attiva, le coordinate del punto successivo sono relative all\'ultimo; in caso contrario, sono assolute, prese dall\'origine (0,0,0).
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento B-spline si riavvia dopo aver terminato la B-spline in costruzione, e consente di disegnare una nuova B-spline senza premere nuovamente il pulsante dello strumento.
-   Premere il tasto **L** oppure fare clic sulla casella di controllo per attivare la modalità *riempito*. Se la modalità di riempimento è attiva una spline chiusa crea una faccia piena (**Make Face** `True`); in caso contrario, la spline chiusa non crea una faccia (**Make Face** `False`).

:   
    **Nota:**la spline non deve essere riempita se si autointerseca, in quanto non crea una faccia corretta. Se la spline è piena ma non è visibile nessuna forma, impostare manualmente **Make Face** su `False` per vedere la spline.

-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il punto successivo in orizzontale o in verticale rispetto all\'ultimo.
-   Premere **Ctrl**+**Z** o il pulsante **<img src="images/Draft_UndoLine.svg" width=12px> [Undo](Draft_UndoLine/it.md)** per annullare l\'ultimo punto.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente; i tratti di linea già posizionati rimangono.


</div>

## Notes


<div class="mw-translate-fuzzy">

Lo strumento B-spline si comporta come lo strumento <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Polilinea](Draft_Wire/it.md), tranne che ciascuno dei suoi tratti è curvo invece di essere un segmento retto. Per convertire tra un tipo l\'altro usare <img alt="" src=images/Draft_WireToBSpline.svg  style="width:16px;"> [Polilinea in B-spline](Draft_WireToBSpline/it.md).


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft BSpline object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Dati

-    **Closed**: specifica se la spline è chiusa o no. Se la spline è inizialmente aperta, questo valore è `False`; impostandolo su `True` viene disegnato un tratto di curva per chiudere la spline. Se la spline è inizialmente chiusa, questo valore è `True`; impostandolo su `False` si rimuove l\'ultimo segmento di curva e si apre la spline.

-    **Make Face**: specifica se la spline crea o no una faccia. Se è `True` crea una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto. Questa proprietà funziona solo se **Closed** è `True`.

:   
    **Nota:**non impostare **Make Face** su `True` se la spline si autointerseca, poiché non crea una faccia corretta.

-    **Parameterization**: influenza la forma della B-spline.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Vista

-    **Arrow Size**: specifica la dimensione del simbolo visualizzato alla fine della spline.

-    **Arrow Type**: specifica il tipo di simbolo visualizzato alla fine della spline, che può essere \"Dot\", \"Circle\", \"Arrow\", o \"Tick\".

-    **End Arrow**: specifica se mostrare il simbolo nell\'ultimo punto della spline, in modo che possa essere usata come una linea di annotazione.

-    **Pattern**: specifica un tipo di [Campitura](Draft_Pattern/it.md) con cui riempire la faccia della spline chiusa. Questa proprietà funziona solo se **Make Face** è `True`, e se **Display Mode** è \"Flat Lines\".

-    **Pattern Size**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento B-spline può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `BSpline` dalla lista di punti fornita da `pointslist`.
    -   Ogni punto nella lista è definito dal suo `FreeCAD.Vector`, con unità in millimetri.
    -   In alternativa, l\'input può essere una `Part.Wire`, da cui vengono estratti i punti.
-   Se `closed` è `True`, o se il primo e l\'ultimo punto coincidono, la spline è chiusa.
-   Se viene dato un `placement` esso viene usato; altrimenti la forma viene creata nell\'origine.
-   Se `face` è `True` e la spline è chiusa, diventa una faccia e appare riempita.


</div>


<div class="mw-translate-fuzzy">

Esempio:


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

spline1 = Draft.make_bspline([p1, p2, p3], closed=False)
spline2 = Draft.make_bspline([p1, 2*p3, 1.3*p2], closed=False)
spline3 = Draft.make_bspline([1.3*p3, p1, -1.7*p2], closed=False)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
