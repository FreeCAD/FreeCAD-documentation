---
- GuiCommand:/it
   Name:Draft BezCurve
   Name/it:Curva di Bézier
   MenuLocation:Drafting → Strumenti Beziér → Curva di Bézier
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**B** **Z**
   Version:0.14
   SeeAlso:[Polilinea](Draft_Wire/it.md), [Curva di Bézier cubica](Draft_CubicBezCurve/it.md), [BSpline](Draft_BSpline/it.md)
---

# Draft BezCurve/it



## Descrizione

Il comando <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> **Curva di Bézier** crea una [curva di Bézier](http://en.wikipedia.org/wiki/Bezier_curve) da diversi punti.

Il comando crea una singola curva di Bézier con un **Degree** che è `number_of_points - 1`. Può essere trasformato in una curva di Bézier a tratti riducendo questa proprietà.

I comandi Curva di Bézier e [Curva di Bézier cubica](Draft_CubicBezCurve/it.md) utilizzano **punti di controllo** per definire la posizione e la curvatura della spline. Il comando [BSpline](Draft_BSpline/it.md), invece, specifica i **punti esatti** attraverso i quali passerà la curva.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Curva di Bézier definita da più punti di controllo*



## Utilizzo

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_BezCurve.svg" width=16px> [Curva di Bézier](Draft_BezCurve/it.md)**.
    -   Selezionare l\'opzione **Drafting → Strumenti Bézier → <img src="images/Draft_BezCurve.svg" width=16px> Curva di Bézier** dal menu.
    -   Usare la scorciatoia da tastiera: **B** poi **Z**. {{Version/it|0.20}}
2.  Si apre il pannello delle attività **Curva di Bézier**. Vedere [Opzioni](#Options.md) per maggiori informazioni.
3.  Scegliere il primo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
4.  Scegliere altri punti nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
5.  Premere **Esc** o il pulsante **Chiudi** per terminare il comando.



## Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **R** o fare clic sulla casella di controllo **Relativo** per attivare o disattivare la modalità relativa. Se la modalità relativa è attiva, le coordinate sono relative all\'ultimo punto, se disponibile, altrimenti sono relative all\'origine del sistema di coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **L** o fare clic sulla casella di controllo **Riempito** per attivare o disattivare la modalità riempimento. Se la modalità riempimento è attiva, la curva creata avrà **Make Face** impostato su `True` e avrà una faccia piena, a condizione che sia chiusa e non si autointersechi. Nota che una curva autointersecante con una faccia non verrà visualizzata correttamente, per tale curva **Make Face** deve essere impostata su `False`.
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando verrà riavviato dopo aver utilizzato **<img src="images/Draft_FinishLine.svg" width=16px> Fine** o **<img src="images/Draft_CloseLine.svg" width=16px> Chiudi**, o dopo aver creato una curva chiusa eseguendo lo snap al primo punto della curva, consentendo di continuare a creare curve.
-   Premere **/** o il pulsante **<img src="images/Draft_UndoLine.svg" width=16px> Annulla** per annullare l\'ultimo punto.
-   Premere **A** o il pulsante **<img src="images/Draft_FinishLine.svg" width=16px> Fine** per terminare il comando e lasciare aperta la curva.
-   Premere **O** o il pulsante **<img src="images/Draft_CloseLine.svg" width=16px> Chiudi** per terminare il comando e chiudere la curva. È inoltre possibile creare una curva chiusa eseguendo lo snap al primo punto della curva.
-   Premere **W** o il pulsante **<img src="images/Draft_Wipe.svg" width=16px> Pulisci** per eliminare i segmenti già posizionati, ma continuare a lavorare dall\'ultimo punto.
-   Premere **U** o il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Imposta il piano di lavoro](Draft_SelectPlane.md)** per regolare il piano di lavoro corrente nell\'orientamento definito dal ultimo e il punto precedente.
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per terminare il comando.



## Note

-   Una Curva di Bézier può essere modificata con il comando [Modifica](Draft_Edit/it.md).
-   OpenCascade, e quindi FreeCAD, non supporta le curve di Bézier di gradi maggiori a 25. Questo non dovrebbe essere un problema in pratica, poiché la maggior parte degli utenti usa tipicamente curve di Bézier di gradi da 3 a 5.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento delle coordinate: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per modificare il valore iniziale della modalità riempimento: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Riempi gli oggetti con le facce quando possibile**. La modifica della modalità di riempimento in un pannello delle attività sovrascriverà questa preferenza per la sessione corrente di FreeCAD.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Curva di Bézier è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Draft}}

-    **Area|Area**: (sola lettura) specifica l\'area della faccia della curva. Il valore sarà {{value|0.0}} se **Make Face** se `False` o la faccia non può essere creata.

-    **Closed|Bool**: specifica se la curva è chiusa o meno. Se la curva è inizialmente aperta questo valore è `False`, impostandolo su `True` disegnerà un segmento per chiudere la curva. Se la curva è inizialmente chiusa questo valore è `True`, impostandolo su `False` rimuoverà l\'ultimo segmento e aprirà la curva.

-    **Continuity|IntegerList**: (sola lettura) specifica la continuità della curva.

-    **Degree|Integer**: specifica il grado della curva.

-    **Length|Length**: (sola lettura) specifica la lunghezza totale della curva.

-    **Make Face|Bool**: specifica se la curva crea o meno una faccia. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto. Questa proprietà funziona solo se **Closed** è `True` e se la curva non si autointerseca.

-    **Points|VectorList**: specifica i punti di controllo della curva nel suo sistema di coordinate locale.



### Vista


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifica la dimensione del simbolo visualizzato alla fine della curva.

-    **Arrow Type|Enumeration**: specifica il tipo di simbolo visualizzato alla fine della curva, che può essere {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} o {{value|Tick-2}}.

-    **End Arrow|Bool**: specifica se mostrare un simbolo alla fine della curva, in modo che possa essere utilizzato come linea di annotazione.

-    **Pattern|Enumeration**: specifica il [Campitura](Draft_Pattern/it.md) con cui riempire la faccia della curva chiusa. Questa proprietà funziona solo se **Make Face** è `True` e se **Display Mode** è {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una Draft Curva di Bézier usare il metodo `make_bezcurve` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeBezCurve`.


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```

-   Crea un oggetto `bezcurve` dalla data lista di punti `pointslist`.
    -   Ogni punto della lista è definito dal suo `FreeCAD.Vector`, con unità in millimetri.
    -   In alternativa, l\'input può essere una `Part.Wire`, da cui vengono estratti i punti.
-   Se `closed` è `True`, o se il primo e l\'ultimo punto coincidono, la curva è chiusa.
-   Se `placement` è `None` la forma viene creata nell\'origine.
-   Se `face` è `True` e la curva è chiusa, diventa una faccia e appare riempita.

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



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/it
