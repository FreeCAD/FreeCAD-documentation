---
- GuiCommand:/it
   Name:Draft CubicBezCurve
   Name/it:Curva di Bézier cubica
   MenuLocation:Draft → Strumenti Bezier → Curva di Bézier cubica
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Version/it:0.19
   SeeAlso:[Polilinea](Draft_Wire/it.md), [B-spline](Draft_BSpline/it.md), [Curva di Bézier](Draft_BezCurve/it.md)
---

# Draft CubicBezCurve/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento [Curva di Bézier cubica](Draft_CubicBezCurve/it.md) crea una[Curva di Bézier](http://en.wikipedia.org/wiki/Bezier_curve) di terzo grado (sono richiesti quattro punti). Questa è una delle curve di Bezier più usate nelle applicazioni di computer grafica. Questo strumento consente di creare una grande spline composta da diversi segmenti Bezier di 3° grado, in un modo simile allo strumento Bezier in Inkscape. Una curva generica di Bezier di qualsiasi grado può essere creata con lo strumento [Curva di Bézier](Draft_BezCurve/it.md).


</div>

The Bézier Curve is one of the most commonly used curves in computer graphics. This command allows you to create a continuous spline made up of several 3rd-degree Bézier segments, in a way that is similar to the Bézier tool in [Inkscape](https://inkscape.org/). A general Bézier curve of any degree can be created with the [Draft BezCurve](Draft_BezCurve.md) command.


<div class="mw-translate-fuzzy">

Gli strumenti [Curva di Bézier](Draft_BezCurve/it.md) e [Curva di Bézier cubica](Draft_CubicBezCurve/it.md) utilizzano i **punti di controllo** per definire la posizione e la curvatura della spline; invece lo strumento [B-spline](Draft_BSpline/it.md) specifica i punti esatti attraverso i quali passa la curva.


</div>

<img alt="" src=images/Draft_CubicBezCurve_example.png  style="width:500px;">


<div class="mw-translate-fuzzy">


*Spline cubica di Bezier definita da tre segmenti. Ogni Bezier cubica è definita da quattro punti, ma quando lo strumento viene utilizzato graficamente, vengono posizionati solo tre di questi punti: 1-2-3 per il primo segmento, 3-4-5 per il secondo segmento e 5-6-7 per il terzo segmento; il quarto punto in ciascun segmento è definito implicitamente; l'ultimo punto 8 è necessario per completare l'operazione e farebbe parte di un quarto segmento di Bezier se l'operazione viene continuata.*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_CubicBezCurve.svg" width=16px> [Curva di Bézier cubica](Draft_CubicBezCurve/it.md)**.
2.  Fare clic su un primo punto nella vista 3D e tenere premuto il pulsante del mouse (1); questo è il primo punto finale..
3.  Trascinare il puntatore su un altro punto della vista 3D e rilasciare il pulsante del mouse (2); questo è il primo punto di controllo..
4.  Spostare il puntatore su un altro punto della vista 3D, fare clic e tenere premuto il pulsante del mouse su questo punto (3); questo è il secondo punto finale.
5.  Spostare il puntatore su un altro punto della vista 3D per regolare la curvatura finale della spline, quindi rilasciare il pulsante del mouse (4)
6.  A questo punto si ha già una curva di Bezier di terzo grado. Il comando può essere completato premendo **Esc** o il pulsante **Chiudi**, oppure si può ripetere il processo facendo clic e tenendo premuto (5), trascinando e rilasciando (6) per aggiungere altri segmenti di Bezier di terzo grado.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Vedere le opzioni in [Curva di Bezier](Draft_BezCurve/it.md).


</div>

## Note

-   A Draft CubicBezCurve can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See [Draft BezCurve](Draft_BezCurve#Preferences.md).

## Proprietà


<div class="mw-translate-fuzzy">

Vedere le proprietà in [Curva di Bezier](Draft_BezCurve/it.md).


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Per informazioni di carattere generale vedere [Curva di Bézier](Draft_BezCurve/it.md). Una Bezier cubica viene creata passando l\'opzione degree=3 a `makeBezCurve()`.


</div>


<div class="mw-translate-fuzzy">

Per ogni segmento di Bezier cubica devono essere utilizzati quattro punti, di cui i due punti estremi indicano dove passa la spline e i due punti intermedi sono punti di controllo.

-   Se vengono assegnati solo 3 punti, viene invece creata una Bezier quadratica, con un solo punto di controllo..
-   Se vengono assegnati solo 2 punti, viene creata una Bezier lineare, ovvero una linea retta.
-   Se vengono assegnati 5 punti, i primi 4 creano un segmento di Bezier cubico; il quarto e il quinto punto vengono utilizzati per creare una linea retta.
-   Se vengono assegnati 6 punti, i primi 4 creano un segmento cubico di Bezier; il quarto e gli altri due punti vengono utilizzati per creare un segmento quadratico di Bezier.
-   Se vengono assegnati 7 punti, i primi 4 creano un segmento cubico di Bezier; il quarto e gli altri tre punti sono usati per creare un secondo segmento cubico di Bezier.
-   In generale, l\'ultimo punto in un gruppo di quattro è condiviso al massimo con i seguenti tre punti per creare un altro segmento di Bezier.
-   \* Per avere curve morbide, senza segmenti diritti, il numero di punti dovrebbe essere `3n + 1` o `3n`, dove `n` è il numero di segmenti, per n >= 1.


</div>

<img alt="" src=images/Draft_CubicBezCurve_API_example.png  style="width:600px;">


<div class="mw-translate-fuzzy">


*Esempi di curve di Bezier prodotte utilizzando 2, 3, 4, 5, 6, 7 e 8 punti. Le linee continue indicano segmenti cubici di Bezier; le altre linee sono quadratiche o lineari.*


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(-3500, 0, 0)
p2 = App.Vector(-3000, 2000, 0)
p3 = App.Vector(-1100, 2000, 0)
p4 = App.Vector(0, 0, 0)

p5 = App.Vector(1500, -2000, 0)
p6 = App.Vector(3000, -1500, 0)
p7 = App.Vector(5000, 0, 0)
p8 = App.Vector(6000, 1500, 0)
rot = App.Rotation()

c1 = Draft.make_circle(100, placement=App.Placement(p1, rot), face=False)
c1.Label = "B1_E1"
c2 = Draft.make_circle(50, placement=App.Placement(p2, rot), face=True)
c2.Label = "B1_c1"
c3 = Draft.make_circle(50, placement=App.Placement(p3, rot), face=True)
c3.Label = "B1_c2"
c4 = Draft.make_circle(100, placement=App.Placement(p4, rot), face=False)
c4.Label = "B1_E2"
c5 = Draft.make_circle(50, placement=App.Placement(p5, rot), face=True)
c5.Label = "B2_c3"
c6 = Draft.make_circle(50, placement=App.Placement(p6, rot), face=True)
c6.Label = "B2_c4"
c7 = Draft.make_circle(100, placement=App.Placement(p7, rot), face=False)
c7.Label = "B2_E3"
c8 = Draft.make_circle(50, placement=App.Placement(p8, rot), face=True)
c8.Label = "B3_c5"

doc.recompute()

B1 = Draft.make_bezcurve([p1, p2], degree=3)
B1.Label = "B_lin"
B1.ViewObject.DrawStyle = "Dashed"

B2 = Draft.make_bezcurve([p1, p2, p3], degree=3)
B2.Label = "B_quad"
B2.ViewObject.DrawStyle = "Dotted"

B3 = Draft.make_bezcurve([p1, p2, p3, p4], degree=3)
B3.Label = "B_cub"
B3.ViewObject.LineWidth = 4

B4 = Draft.make_bezcurve([p1, p2, p3, p4, p5], degree=3)
B4.Label = "B_cub+lin"
B4.ViewObject.DrawStyle = "Dashed"

B5 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6], degree=3)
B5.Label = "B_cub+quad"
B5.ViewObject.DrawStyle = "Dotted"

B6 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6, p7], degree=3)
B6.Label = "B_cub+cub"
B6.ViewObject.LineWidth = 2

B7 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6, p7, p8], degree=3)
B7.Label = "B_cub+cub+lin"
B7.ViewObject.DrawStyle = "Dashed"

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CubicBezCurve/it
