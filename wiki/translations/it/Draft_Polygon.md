---
- GuiCommand:/it
   Name:Draft Polygon
   Name/it:Poligono
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Poligono    Shortcut:**P** **G**
   SeeAlso:[Cerchio](Draft_Circle/it.md), [Campitura](Draft_Pattern/it.md)
   Version:0.7
---

# Draft Polygon/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Poligono crea un poligono regolare inscritto in una circonferenza selezionando due punti, il centro e il raggio. Il poligono assume [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati nella [barra di Draft](Draft_Tray/it.md).


</div>


<div class="mw-translate-fuzzy">

Il poligono viene creato inscritto in un cerchio di raggio specificato; dopo la creazione può essere convertito in circoscritto cambiando la proprietà della sua modalità di disegno.


</div>

<img alt="" src=images/Draft_polygon_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Poligono regolare definito dal punto centrale e dal raggio*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Polygon.svg" width=16px> [Poligono](Draft_Polygon/it.md)**, o premere i tasti **P** e poi **G**.
2.  Definire il numero di lati desiderato nella finestra di dialogo delle opzioni.
3.  Selezionare un primo punto nella vista 3D per stabilire il centro, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)**.
4.  Fare clic su un altro punto nella vista 3D o digitare un valore di raggio per definire il raggio del poligono.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opzioni

-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Poligono si riavvia dopo aver terminato la forma in costruzione, e consente di disegnare un nuovo poligono senza premere nuovamente il pulsante dello strumento.
-   Premere il tasto **L** oppure fare clic sulla casella di controllo per attivare la modalità *riempito*. Se la modalità di riempimento è attiva, il poligono crea una faccia piena (**Make Face** `True`); in caso contrario, il poligono non crea una faccia (**Make Face** `False`).
-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il prossimo punto in orizzontale o in verticale rispetto all\'ultimo.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

Il poligono può essere modificato facendo doppio clic sull\'elemento nella vista ad albero o premendo il pulsante **<img src="images/Draft_Edit.svg" width=16px> [Modifica](Draft_Edit/it.md)**. Quindi si può spostare il il centro e il raggio in una nuova posizione.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part RegularPolygon](Part_RegularPolygon.md) instead of a Draft Polygon.

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Polygon object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Dati

-    **Radius**: specifica il raggio del cerchio che definisce il poligono.

-    **Draw Mode**: specifica se il poligono è inscritto in un cerchio o circoscritto attorno a un cerchio.

-    **Faces Number**: specifica il numero di lati del poligono.

-    **Chamfer Size**: specifica la dimensione degli smussi (segmenti retti) creati agli angoli del poligono.

-    **Fillet Radius**: specifica il raggio dei raccordi (segmenti di arco) creati agli angoli del poligono.

-    **Make Face**: specifica se la forma è una faccia o no. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Vista

-    **Pattern**: specifica un [Modello](Draft_Pattern/it.md) con cui riempire la faccia del poligono. Questa proprietà funziona solo se **Make Face** è `True`, e se **Display Mode** è \"Flat Lines\".

-    **Pattern Size**: specifica la dimensione del [Modello](Draft_Pattern/it.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Poligono può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
polygon = make_polygon(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Polygon` con il dato numero di lati (`nfaces`), e basato su un cerchio di `radius` in millimettri.
-   Se `inscribed` è `True`, il poligono è inscritto nel cerchio, altrimenti è circoscritto.
    -   Uno dei vertici del poligono giace sull\'asse X se non viene assegnato nessun altro posizionamento.
-   Se è dato un `placement`, esso viene usato; altrimenti la forma viene creata all\'origine.
-   Se `face` è `True`, la forma crea una faccia, cioè appare riempita.


</div>

Esempio: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(4, radius=500)
polygon2 = Draft.make_polygon(5, radius=750)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

Polygon3 = Draft.make_polygon(6, radius=1450, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Polygon/it
