---
- GuiCommand:/it
   Name:Draft Fillet
   Name/it:Raccordo
   MenuLocation:Draft → Raccordo
   Workbenches:[Draft](Draft_Module/it.md)
   SeeAlso:[Linea](Draft_Line/it.md), [Polilinea](Draft_Wire/it.md)
   Version:0.19
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento [Raccordo](Draft_Fillet/it.md) crea un raccordo, un angolo arrotondato, tra due semplici [Linee](Draft_Line/it.md). In alternativa, può creare uno smusso, un bordo dritto, tra queste due linee.


</div>

<img alt="" src=images/Draft_Fillet_example.png  style="width:400px;"> 
*Diversi raccordi e smussi creati tra due linee*

### Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare due [linee](Draft_Line/it.md) già inserite nel documento e che si incontrano in un punto.
2.  Premere il pulsante **<img src="images/Draft_Fillet.svg" width=16px> [Raccordo](Draft_Fillet/it.md)**.
3.  Scegliere il raggio del raccordo, quindi premere **Invio**.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   Selezionare la casella di controllo \"Elimina oggetti originali\" se si desidera eliminare le due linee originali e lasciare solo il nuovo oggetto raccordo.
-   Selezionare la casella di controllo \"Crea smusso\" se si desidera creare un bordo dritto, anziché un bordo arrotondato, tra le due linee.
-   Premere **Esc** o **Chiudi** per annullare il comando corrente.


</div>

## Notes


<div class="mw-translate-fuzzy">

Note:

-   Se il raggio è troppo grande in modo che l\'arco prodotto non sia tangente a una delle linee, l\'operazione non avrà un esito positivo.
-   Al momento sono supportate solo singole linee; le [polilinee](Draft_Wire/it.md), ovvero linee con più punti, potrebbero non produrre il risultato desiderato.


</div>

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Fillet object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Dati


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **Start**: (sola lettura) specifica il punto iniziale.

-    **End**: (sola lettura) specifica il punto finale.

-    **Length**: (sola lettura) specifica la lunghezza dell\'intero segmento.

-    **Fillet Radius**: (sola lettura) raggio con cui è stato creato il raccordo.


</div>

### Vista


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    **End Arrow**: se è `True` verrà visualizzato un simbolo nell\'ultimo punto della linea, quindi può essere usata come una linea di annotazione.

-    **Arrow Size**: specifica la dimensione del simbolo visualizzato alla fine della linea.

-    **Arrow Type**: specifica il tipo di simbolo visualizzato alla fine della linea, che può essere \"Dot\", \"Circle\", \"Arrow\", o \"Tick\", or \"Tick-2\" (\"Punto\", \"Cerchio\", \"Freccia\", o \"Tratto\").


</div>

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Fillet può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
fillet = make_fillet([line1, line2], radius=100, chamfer=False, delete=False)
```

-   Crea un oggetto `Fillet` tra le linne `line1` e `line2`, usando `radius` come raggio di curvatura.
-   Se `chamfer` è `True` crea un bordo dritto con la lunghezza di `radius`, invece di un bordo arrotondato.
-   Se `delete` è `True` cancella le `line1` e `line2`, e lascia solo il nuovo oggetto.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p2, p3)

doc.recompute()

fillet = Draft.make_fillet([line1, line2], radius=500)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
