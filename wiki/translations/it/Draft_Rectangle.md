---
- GuiCommand:/it
   Name:Draft Rectangle
   Name/it:Rettangolo
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Rettangolo
   Shortcut:**R** **E**
   SeeAlso:[Ellisse](Draft_Ellipse/it.md), [Cubo](Part_Box/it.md)
   Version:0.7
---

# Draft Rectangle/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Rettangolo crea un rettangolo selezionando due punti. Usa [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati nella [barra di Draft](Draft_Tray/it.md).


</div>

È possibile aggiungere facoltativamente uno smusso di 45 gradi o un raccordo circolare a ogni angolo del rettangolo e dividere il rettangolo in una serie di righe e colonne di uguale dimensione.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Rettangolo definito da due vertici opposti*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Rectangle.svg" width=16px> [Rettangolo](Draft_Rectangle/it.md)**, o premere i tasti **R** e poi **E**.
2.  Selezionare un primo vertice nella vista 3D, oppure digitare le sue coordinate e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
3.  Fare clic su un altro punto sulla vista 3D opposto al primo o digitare le sue coordinate e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.

:   Il secondo punto non deve essere vincolato agli assi X, Y o Z, altrimenti il rettangolo risultante non è corretto.


</div>

## Opzioni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **R** oppure fare clic sulla casella di controllo per attivare la modalità \"relativo\". Se la modalità relativo è attiva, le coordinate del punto successivo sono relative all\'ultimo; in caso contrario, sono assolute, prese dall\'origine (0,0,0).
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Rettangolo si riavvia dopo aver terminato la figura in costruzione, e consente di disegnare un nuovo rettangolo senza premere nuovamente il pulsante dello strumento.
-   Premere il tasto **L** oppure fare clic sulla casella di controllo per attivare la modalità *riempito*. Se la modalità di riempimento è attiva, il rettangolo crea una faccia piena (**Make Face** `True`); in caso contrario, il rettangolo non crea una faccia (**Make Face** `False`).
-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

Il Rettangolo può essere modificato facendo doppio clic sull\'elemento nella vista ad albero o premendo il pulsante **<img src="images/Draft_Edit.svg" width=16px> [Modifica](Draft_Edit/it.md)**. Quindi si può spostare i vertici in una nuova posizione.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Plane](Part_Plane.md) instead of a Draft Rectangle.

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Rectangle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Dati

-    **Length**: specifica la lunghezza della forma nella direzione dell\'asse X.

-    **Height**: specifica la larghezza della forma nella direzione dell\'asse Y.

-    **Chamfer Size**: specifica la lunghezza in diagonale di uno smusso a 45° in ogni angolo del rettangolo.

-    **Fillet Radius**: specifica il raggio di un raccordo a 90° ad ogni angolo del rettangolo.

-    **Rows**: specifica il numero di righe di uguale dimensione in cui è suddivisa la forma originale; per impostazione predefinita, 1 riga.

-    **Columns**: specifica il numero di colonne di uguale dimensione in cui è suddivisa la forma originale; per impostazione predefinita, 1 colonna.

-    **Make Face**: specifica se la forma crea una faccia o no. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### View 

-    **Pattern**: specifica un [Modello](Draft_Pattern/it.md) di disegno con cui riempire la faccia della forma. Questa proprietà funziona solo se **Make Face** è `True`, e se **Display Mode** è \"Flat Lines\".

-    **Pattern Size**: specifica la dimensione del [Modello](Draft_Pattern/it.md) di disegno.

-    **Texture Image**: specifica il percorso di un file immagine da mappare sulla faccia della forma. Cancellando questa proprietà si rimuove l\'immagine.

:   Il rettangolo dovrebbe avere le stesse proporzioni dell\'immagine per evitare distorsioni nella mappatura.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Rettangolo può essere usato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Rectangle` con `length` nella direzione X e `height` in direzione Y, con le unità in millimetri.
    -   La lunghezza è parallela all\'asse X se non è indicato nessun altro posizionamento.
-   Se viene dato un `placement`, esso viene utilizzato; altrimenti la forma viene creata all\'origine.
-   Se `face` è `True`, la forma crea una faccia, cioè appare riempita.


</div>

Esempio: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle1 = Draft.make_rectangle(4000, 1000)
rectangle2 = Draft.make_rectangle(1000, 4000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 45))

rectangle3 = Draft.make_rectangle(3500, 250, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rectangle/it
