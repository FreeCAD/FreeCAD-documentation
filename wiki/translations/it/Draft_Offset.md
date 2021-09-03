---
- GuiCommand:/it
   Name:Draft Offset
   Name/it:Offset
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Offset
   Shortcut:**O** **S**
   SeeAlso:[Scala](Draft_Scale/it.md), [Part Offset 2D](Part_Offset2D/it.md)
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Offset sposta l\'oggetto selezionato di una determinata distanza (offset) perpendicolare a se stesso.


</div>

<img alt="" src=images/Draft_Offset_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Offset di un contorno a una certa distanza da uno dei suoi bordi*


</div>

## Utilizzo

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Selezionare l\'oggetto che si desidera scostare.
2.  Premere il pulsante **<img src="images/Draft_Offset.svg" width=16px> Offset**, o premere i tasti {{KEY/it|O}} e {{KEY/it|S}}. Se nessun oggetto è selezionato, si viene invitati a selezionarne uno.
3.  Selezionare un punto nella vista 3D, o fornire una distanza


</div>

## Opzioni

The single character keyboard shortcuts and the modifier keys mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Premere il tasto **P** o fare clic sulla casella di controllo per attivare la modalità *copia*. Se la modalità copia è attiva, lo strumento Offset mantiene la forma originale al suo posto e crea una copia ridimensionata nel punto selezionato.
-   Tenere premuto **Alt** mentre si seleziona il punto per attivare o disattivare la modalità di copia. Tenendo premuto **Alt** si può continuare a posizionare delle copie offset; rilasciare **Alt** per terminare l\'operazione e vedere tutte le forme di offset.
-   Fare clic sulla casella di controllo \"OCC-style\" per attivare la modalità \"OCC\". Ciò crea un offset da entrambi i lati di un segmento di linea, che produce una speciale forma chiusa con i bordi arrotondati alle estremità dei segmenti.

:   
    **Nota:**con questo stile i segmenti originali vengono rimossi, quindi utilizzare la modalità copia per conservare i bordi originali.

-   Tenere premuto **Ctrl** mentre si si crea l\'offset per [agganciare](Draft_Snap/it.md) in modo forzato il punto di snap più vicino, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** per mantenere la distanza di offset riferita al segmento corrente ed evitare di selezionare un altro riferimento.
-   Premere il tasto **Esc** o il pulsante **Chiudi** per interrompere il comando corrente; le copie offset già posizionate rimangono.


</div>

## Notes

-   To create an offset version of a [Draft BSpline](Draft_BSpline.md) its points are offset individually, and from the new points a new spline is calculated. This new spline is not parallel to the original spline. For an exact parallel offset of a [Draft BSpline](Draft_BSpline.md) the [Part Offset2D](Part_Offset2D.md) command should be used.
-   The Draft Offset command cannot handle [Draft BezCurves](Draft_BezCurve.md). Use the [Part Offset2D](Part_Offset2D.md) command instead.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of the distance: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Offset può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```


<div class="mw-translate-fuzzy">

-   Crea un offset del dato contorno `obj` applicando il `delta` dato, definito come un vettore, al suo primo vertice.
-   Se `copy` è `True` viene creato un altro oggetto invece di ridimensionare l\'oggetto originale.
-   Se `bind` è `True`, e a condizione che l\'oggetto contorno sia aperto, l\'originale e l\'offset sono uniti nei loro punti finali, formando una faccia.
    -   Se `sym` è `True`, e anche `bind` è `True`, e l\'offset è fatto su entrambi i lati del contorno, la larghezza totale è la larghezza del vettore dato.
-   Se `occ` è `True`, utilizzerà lo sfalsamento in stile OCC: crea un offset su entrambi i lati, quindi unisce i nuovi contorni e arrotonda gli angoli.
-   Restituisce un`Offsetobj` con l\'oggetto offset originale o con la nuova copia.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1500, 2000, 0)
p3 = App.Vector(4000, 0, 0)

wire = Draft.make_wire([p1, p2, p3])
doc.recompute()

vector = App.Vector(-200, 150, 0)
offset1 = Draft.offset(wire, vector, copy=True, bind=True, sym=True)
offset2 = Draft.offset(wire, 3*vector, copy=True)
offset3 = Draft.offset(wire, 6*vector, copy=True)
offset4 = Draft.offset(wire, 9*vector, copy=True)
offset5 = Draft.offset(wire, 1.5*vector, copy=True, occ=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
