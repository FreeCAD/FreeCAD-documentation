---
- GuiCommand:/it
   Name:Draft_Line
   Name/it:Linea
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Linea   Shortcut:**L** **I**
   SeeAlso:[DWire](Draft_Wire/it.md), [Punto](Draft_Point/it.md)
   Version:0.7
---

# Draft Line/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Crea un segmento tra due punti nel [piano di lavoro](Draft_SelectPlane/it.md) corrente. Il segmento assume [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati in precedenza nella [barra di Draft](Draft_Tray/it.md). Lo strumento Linea si comporta esattamente come lo strumento [DWire](Draft_Wire/it.md) di Draft, tranne che si disattiva dopo che sono stati definiti due punti.


</div>

A Draft Line is in fact a [Draft Wire](Draft_Wire.md) with only two points.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Linea creata da due punti*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Line.svg" width=16px> [Linea](Draft_Line/it.md)
** o premere i tasti **L** e **I**
2.  Fare clic su un primo punto nella vista 3D, o digitare le sue coordinate e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> inserisci punto**.
3.  Fare clic su un secondo punto nella vista 3D, o digitare le sue coordinate e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> inserisci punto**.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Opzioni

-   Premere **X**, o **Y**, o **Z** dopo il primo punto per vincolare il secondo punto su un dato asse.
-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** tra ciascun componente X, Y e Z.
    -   Si possono anche definire le coordinate polari del punto dando un valore a \"Lunghezza\" e \"Angolo\". Fare clic sulla casella accanto a \"Angolo\" per vincolare il puntatore all\'angolo specificato.
    -   È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> inserisci punto** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **R** oppure fare clic sulla casella di controllo per attivare la modalità \"relativo\". Se la modalità relativo è attiva, le coordinate del punto successivo sono relative all\'ultimo; in caso contrario, sono assolute, prese dall\'origine (0,0,0).
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Linea si riavvia dopo aver terminato la linea in costruzione, e consente di disegnarne una nuova linea senza premere nuovamente il pulsante dello strumento
-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il prossimo punto in orizzontale o in verticale rispetto all\'ultimo.
-   Premere i tasti **Ctrl**+**Z** o premere il pulsante {{button|<img src="images/Draft_UndoLine.svg" width=12px> Undo}} per annullare l\'ultimo punto.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

La linea può essere modificata facendo doppio clic sull\'elemento nella vista ad albero o premendo il pulsante **<img src="images/Draft_Edit.svg" width=16px> [Modifica](Draft_Edit/it.md)**. Quindi si possono spostare i punti in una nuova posizione.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box: **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Line](Part_Line.md) instead of a Draft Line.

## Properties


<div class="mw-translate-fuzzy">

## Proprietà

Un oggetto Linea condivide tutte le proprietà di una <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Polilinea](Draft_Wire/it.md), tuttavia solo alcune di queste proprietà sono applicabili alla Linee.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Linea può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```

-   Crea un oggetto `Line` tra i punti `p1` e `p2`, ciascuno definito dal suo `FreeCAD.Vector`, con unità in millimetri.
-   Crea un oggetto `Line` da un `Part.LineSegment`.
-   Crea un oggetto `Line` dal primo vertice all\'ultimo vertice della data `Shape`.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/it
