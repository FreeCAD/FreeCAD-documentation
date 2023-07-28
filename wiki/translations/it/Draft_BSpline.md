---
- GuiCommand:/it
   Name:Draft BSpline
   Name/it:BSpline
   MenuLocation:Drafting → BSpline
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**B** **S**
   Version:0.7
   SeeAlso:[Polilinea](Draft_Wire/it.md), [Curva di Bezier](Draft_BezCurve/it.md)
---

# Draft BSpline/it



## Descrizione

Il comando <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> **BSpline** crea una [curva B-spline](http://en.wikipedia.org/wiki/B-spline) da diversi punti.

Il comando BSpline specifica i **punti esatti** attraverso i quali passerà la curva. I comandi [Curva di Bézier](Draft_BezCurve/it.md) e [Curva di Bézier cubica](Draft_CubicBezCurve/it.md), invece, utilizzano **punti di controllo** per definire la posizione e la curvatura della spline.

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*Spline definita da più punti*



## Utilizzo

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_BSpline.svg" width=16px> [BSpline](Draft_BSpline/it.md)**.
    -   Selezionare l\'opzione **Drafting → <img src="images/Draft_BSpline.svg" width=16px> BSpline** dal menu.
    -   Usare la scorciatoia da tastiera: **B** poi **S**.
2.  Si apre il pannello attività **BSpline**. Vedere [Opzioni](#Options.md) per maggiori informazioni.
3.  Scegliere il primo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
4.  Scegliere altri punti nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
5.  Premere **Esc** o il pulsante **Chiudi** per terminare il comando.



## Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di essei. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **R** o fare clic sulla casella di controllo **Relativo** per attivare o disattivare la modalità relativa. Se la modalità relativa è attiva, le coordinate sono relative all\'ultimo punto, se disponibile, altrimenti sono relative all\'origine del sistema di coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **L** o fare clic sulla casella di controllo **Riempito** per attivare o disattivare la modalità riempimento. Se la modalità riempimento è attiva, la spline creata avrà **Make Face** impostato su `True` e avrà una faccia piena, a condizione che sia chiusa e non si intersechi. Si noti che una spline autointersecante con una faccia non verrà visualizzata correttamente, per tale spline **Make Face** deve essere impostato su `False`.
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando verrà riavviato dopo aver utilizzato **<img src="images/Draft_FinishLine.svg" width=16px> Fine** o **<img src="images/Draft_CloseLine.svg" width=16px> Chiudi**, o dopo aver creato una spline chiusa eseguendo lo snap al primo punto della spline, consentendo di continuare a creare altre spline.
-   Premere **/** o il pulsante **<img src="images/Draft_UndoLine.svg" width=16px> Annulla** per annullare l\'ultimo punto.
-   Premere **A** o il pulsante **<img src="images/Draft_FinishLine.svg" width=16px> Fine** per terminare il comando e lasciare aperta la spline.
-   Premere **O** o il pulsante **<img src="images/Draft_CloseLine.svg" width=16px> Chiudi** per terminare il comando e chiudere la spline. È inoltre possibile creare una spline chiusa eseguendo lo snap al primo punto della spline.
-   Premere **W** o il pulsante **<img src="images/Draft_Wipe.svg" width=16px> Pulisci** per eliminare i segmenti di curva già posizionati, ma continuare a lavorare dall\'ultimo punto.
-   Premere **U** o il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Imposta il piano di lavoro](Draft_SelectPlane/it.md)** per regolare il piano di lavoro corrente nell\'orientamento definito dal ultimo e il punto precedente.
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premi **Esc** o il pulsante **Chiudi** per terminare il comando.



## Note

-   Una BSpline può essere modificata con il comando [Modifica](Draft_Edit/it.md).
-   Una BSpline può essere convertita in un [Polilinea](Draft_Wire/it.md) con il comando [Convertire tra polilinea e BSpline](Draft_WireToBSpline/it.md).



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento delle coordinate: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per modificare il valore iniziale della modalità riempimento: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Riempi gli oggetti con le facce quando possibile**. La modifica della modalità di riempimento in un pannello delle attività sovrascriverà questa preferenza per la sessione corrente di FreeCAD.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft BSpiline è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Draft}}

-    **Area|Area**: (sola lettura) specifica l\'area della faccia della spline. Il valore sarà {{value|0.0}} se **Make Face** se `False` o la faccia non può essere creata.

-    **Closed|Bool**: specifica se la spline è chiusa o meno. Se la spline è inizialmente aperta questo valore è `False`, impostandolo su `True` disegnerà un segmento di curva per chiudere la spline. Se la spline è inizialmente chiusa, questo valore è `True`, impostandolo su `False` si rimuoverà l\'ultimo segmento di curva e si aprirà la spline.

-    **Make Face|Bool**: specifica se la spline crea o meno una faccia. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto. Questa proprietà funziona solo se **Closed** è `True` e se la spline non si autointerseca.

-    **Parameterization|Float**: influisce sulla forma della spline.

-    **Points|VectorList**: specifica i punti della spline nel suo sistema di coordinate locale.



### Vista


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifica la dimensione del simbolo visualizzato alla fine della spline.

-    **Arrow Type|Enumeration**: specifica il tipo di simbolo visualizzato alla fine della spline, che può essere {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} o {{value|Tick-2}}.

-    **End Arrow|Bool**: specifica se mostrare un simbolo alla fine della spline, in modo che possa essere utilizzato come linea di annotazione.

-    **Pattern|Enumeration**: specifica la [Campitura](Draft_Pattern/it.md) con cui riempire la faccia della spline chiusa. Questa proprietà funziona solo se **Make Face** è `True` e se **Display Mode** è {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una Draft BSpline utilizzare il metodo `make_bspline` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeBSpline`.


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Crea un oggetto `bspline` dalla lista di punti fornita da `pointslist`.
    -   Ogni punto nella lista è definito dal suo `FreeCAD.Vector`, con unità in millimetri.
    -   In alternativa, l\'input può essere una `Part.Wire`, da cui vengono estratti i punti.
-   Se `closed` è `True`, o se il primo e l\'ultimo punto coincidono, la spline è chiusa.
-   Se `placement` è `None` la forma viene creata nell\'origine.
-   Se `face` è `True` e la spline è chiusa, diventa una faccia e appare riempita.

Esempio:


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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/it
