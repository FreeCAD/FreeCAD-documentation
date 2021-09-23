---
- GuiCommand:/it
   Name:Draft BezCurve
   Name/it:Curva di Bezier
   MenuLocation:Draft → Strumenti Beziér → Curva di Bézier
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**B** **Z**
   SeeAlso:[Polilinea](Draft_Wire/it.md), [CubicBezCurve](Draft_CubicBezCurve/it.md), [B-spline](Draft_BSpline/it.md)
   Version:0.14
---

# Draft BezCurve/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_BezCurve.svg  style="width:16px;"> Curva di Bézier crea una [Curva di Bezier](http://en.wikipedia.org/wiki/Bezier_curve), o un suo tratto, da più punti. Assume [lo spessore e il colore](Draft_Linestyle/it.md) precedentemente impostati nella [barra di Draft](Draft_Tray/it.md).


</div>


<div class="mw-translate-fuzzy">

L\'oggetto viene creato come una unica curva di Bezier di grado uguale a `number_of_points - 1` (al numero di punti - 1). Dopo la creazione può essere commutato in tratti di curva di Bezier di determinato grado modificando le sue [proprietà](Property/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Curva di Bezier utilizza **i punti di controllo** per definire la direzione della curva; invece lo strumento [B-spline](Draft_BSpline/it.md) specifica i punti esatti attraverso i quali deve passare la curva. Per creare curve circolari o ellittiche esatte, usare [Arco](Draft_Arc/it.md) e [Ellisse](Draft_Ellipse/it.md).


</div>

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;">


<div class="mw-translate-fuzzy">


*Curva di Bézier definita da più punti di controllo*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_BezCurve.png" width=16px> [Curva di Bézier](Draft_BezCurve/it.md)**, o premere i tasti **B** e poi **Z**.
2.  Selezionare un primo punto nella vista 3D, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
3.  Selezionare un nuovo punto nella vista 3D, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.
4.  Premere il tasto **Esc** o il pulsante {{button|Chiudi}}, o fare doppio clic sull\'ultimo punto per terminare l\'edizione.


</div>

## Opzioni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Premere il tasto **A** o il pulsante **<img src="images/Draft_FinishLine.svg" width=12px> [Termina](Draft_FinishLine/it.md)** per terminare la curva, lasciandola aperta.
-   Premere il tasto **O** o il pulsante **<img src="images/Draft_CloseLine.svg" width=12px> [Chiudi](Draft_CloseLine.md)** per chiudere la curva, cioè per aggiungere un segmento dall\'ultimo punto al primo per formare una faccia. Per formare una faccia sono necessari almeno quattro punti, e una curva di grado tre.
-   Premere il tasto **W** o il pulsante **<img src="images/Draft_Wipe.svg" width=12px> [Pulisci](Draft_Wipe.md)** per rimuovere i segmenti della curva già posizionati, ma continuare a creare la curva dall\'ultimo punto.
-   Premere il tasto **U** o il pulsante **<img src="images/Draft_SelectPlane.svg" width=12px> [Imposta il piano](Draft_SelectPlane/it.md)** per posizionare il piano di lavoro corrente nell\'orientamento dell\'ultimo punto.
-   Premere il tasto **X**, o **Y** o **Z** dopo un punto per vincolare il successivo punto sul dato asse.
-   Per inserire le coordinate manualmente, basta inserire i valori e poi premere **Invio** per ciascun componente X, Y e Z.
-   Premere il tasto **R** oppure fare clic sulla casella di controllo per attivare la modalità \"relativo\". Se la modalità relativo è attiva, le coordinate del punto successivo sono relative all\'ultimo; in caso contrario, sono assolute, prese dall\'origine (0,0,0).
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Curva di Bézier si riavvia dopo aver terminato la Curva di Bézier in costruzione, e consente di disegnare una nuova Curva di Bézier senza premere nuovamente il pulsante dello strumento.
-   Premere il tasto **L** oppure fare clic sulla casella di controllo per attivare la modalità *riempito*. Se la modalità di riempimento è attiva una Curva di Bézier chiusa crea una faccia piena (**Make Face** `True`); in caso contrario, la Curva di Bézier chiusa non crea una faccia (**Make Face** `False`).

:   
    **Nota:**la curva non deve essere riempita se si autointerseca, in quanto non crea una faccia corretta. Se la curva è piena ma non è visibile nessuna forma, impostare manualmente **Make Face** su `False` per vedere la spline.

-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il punto successivo in orizzontale o in verticale rispetto all\'ultimo.
-   Premere **Ctrl**+**Z** o il pulsante **<img src="images/Draft_UndoLine.svg" width=12px> [Undo](Draft_UndoLine/it.md)** per annullare l\'ultimo punto.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente; le curve già posizionate rimamgono.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Limitazioni

-   Le proprietà Punti non compaiono ancora nell\'elenco delle proprietà.
-   OpenCascade, e quindi FreeCAD, non supporta le curve di Bézier di grado superiore a 25. Questo non dovrebbe essere un problema nella pratica, poiché la maggior parte degli utenti usa tipicamente le curve di Bézier da 3 a 5 gradi.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft BezCurve object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Dati

-    **Degree**: specifica il grado della curva di Bezier o dei singoli segmenti.

-    **Closed**: specifica se la curva è chiusa o no. Se la curva è inizialmente aperta, questo valore è `False`; impostandolo su `True` viene disegnato un segmento per chiudere la curva. Se la curva è inizialmente chiusa, questo valore è `True`; impostandolo su `False` si rimuove l\'ultimo segmento e si apre la curva.

-    **Make Face**: specifica se la spline crea o no una faccia. Se è `True` crea una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto. Questa proprietà funziona solo se **Closed** è `True`.

:   
    **Nota:**non impostare **Make Face** su `True` se la curva si autointerseca, poiché non crea una faccia corretta.

-    **Continuity**: (sola lettura) quando la curva è chiusa, indica la continuità della curva `[0]`, o `[0,0]`. Altrimenti è `[]`.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Vista

-    **Arrow Size**: specifica la dimensione del simbolo visualizzato alla fine della curva.

-    **Arrow Type**: specifica il tipo di simbolo visualizzato alla fine della curva, che può essere dot, circle, arrow, o tick.

-    **End Arrow**: specifica se mostrare un simbolo nell\'ultimo punto della curva, in modo che possa essere usata come una linea di annotazione.

-    **Pattern**: specifica un tipo di [Campitura](Draft_Pattern/it.md) con cui riempire la faccia della curva chiusa. Questa proprietà funziona solo se **Make Face** è `True`, e se **Display Mode** è \"Flat Lines\".

-    **Pattern Size**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Curva di Bézier può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `BezCurve` dalla data lista di punti `pointslist`.
    -   Ogni punto della lista è definito dal suo `FreeCAD.Vector`, con unità in millimetri.
    -   In alternativa, l\'input può essere una `Part.Wire`, da cui vengono estratti i punti.
-   Se `closed` è `True`, o se il primo e l\'ultimo punto coincidono, la curva è chiusa.
-   Se viene dato un `placement` esso viene usato; altrimenti la forma viene creata nell\'origine.
-   Se `face` è `True` e la curva è chiusa, diventa una faccia e appare riempita.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)
p4 = App.Vector(1500, -2000, 0)

bezcurve1 = Draft.make_bezcurve([p1, p2, p3, p4], closed=True)
bezcurve2 = Draft.make_bezcurve([p4, 1.3*p2, p1, 4.1*p3], closed=True)
bezcurve3 = Draft.make_bezcurve([1.7*p3, 1.5*p4, 2.1*p2, p1], closed=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/it
