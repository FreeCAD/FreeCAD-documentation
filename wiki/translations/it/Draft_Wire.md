---
- GuiCommand:
   Name:Draft Wire
   Name/it:Polilinea
   MenuLocation:Drafting → Polilinea
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   Shortcut:**P** **L**
   Version:0.7
   SeeAlso:[Linea](Draft_Line/it.md), [BSpline](Draft_BSpline/it.md)
---

# Draft Wire/it



## Descrizione

Il comando <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> **Polilinea** [crea](#Create.md) una polilinea, ovvero una sequenza di segmenti di linea collegati. Il comando può anche essere usato per [unire](#Join.md) [Linee](Draft_Line/it.md) e Polilinee.

I vertici di una Polilinea possono essere raccordati (stondati) o smussati cambiando le sue **Fillet Radius** or **Chamfer Size** rispettivamente. E\' anche possibile suddividere i bordi di una Polilinea cambiando la sua **Subdivisions** proprietà.

<img alt="" src=images/Draft_Polyline_example.jpg  style="width:400px;"> 
*Polilinea definita da più punti*



## Creazione



### Utilizzo

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Wire.svg" width=16px> [Polilinea](Draft_Wire/it.md)**.
    -   Selezionare l\'opzione **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polilinea** dal menu.
    -   Usare la scorciatoia da tastiera: **P** poi **L**.
2.  Si apre il pannello attività **Polilinea**. Vedi [Opzioni](#Options.md) per maggiori informazioni.
3.  Scegliere il primo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
4.  Scegliere altri punti nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
5.  Premere **Esc** o il pulsante **Chiudi** per terminare il comando.



### Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **R** o fare clic sulla casella di controllo **Relativo** per attivare o disattivare la modalità relativa. Se la modalità relativa è attiva, le coordinate sono relative all\'ultimo punto, se disponibile, altrimenti sono relative all\'origine del sistema di coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate del [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **L** o fare clic sulla casella di controllo **Riempito** per attivare o disattivare la modalità riempimento. Se la modalità di riempimento è attiva, la polilinea creata avrà **Make Face** impostato su `True` e avrà una faccia piena, a condizione che sia chiusa e non si autointersechi. Si noti che una polilinea autointersecante con una faccia non verrà visualizzata correttamente, per tale polilinea **Make Face** deve essere impostata su `False`.
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando verrà riavviato dopo aver utilizzato **<img src="images/Draft_FinishLine.svg" width=16px> Fine** o **<img src="images/Draft_CloseLine.svg" width=16px> Chiudi**, o dopo aver creato una polilinea chiusa eseguendo lo snap al primo punto della stessa, consentendo di continuare a creare ulteriori polilinee.
-   Premere **/** o il pulsante **<img src="images/Draft_UndoLine.svg" width=16px> Annulla** per annullare l\'ultimo punto.
-   Premere **A** o il pulsante **<img src="images/Draft_FinishLine.svg" width=16px> Fine** per terminare il comando e lasciare la polilinea aperta.
-   Premere **O** o il pulsante **<img src="images/Draft_CloseLine.svg" width=16px> Chiudi** per terminare il comando e chiudere la polilinea. È inoltre possibile creare una polilinea chiusa eseguendo lo snap al primo punto della stessa.
-   Premere **W** o il pulsante **<img src="images/Draft_Wipe.svg" width=16px> Pulisci** per eliminare i segmenti già posizionati, ma continuare a lavorare dall\'ultimo punto.
-   Premere **U** o il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Imposta il piano di lavoro](Draft_SelectPlane/it.md)** per regolare il piano di lavoro corrente nell\'orientamento dell\'ultimo segmento.
-   Premere **S** per attivare o disattivare lo [Snap](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per terminare il comando.



## Unione



### Utilizzo 

1.  I punti finali delle [Linee](Draft_Line/it.md) e/o Polilinee da unire devono essere esattamente coincidenti. Se necessario, prima regolare i punti per assicurarsi che sia così.
2.  Selezionare due o più [Linee](Draft_Line/it.md) e/o Polilinee.
3.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Wire.svg" width=16px> [Polilinea](Draft_Wire/it.md)**.
    -   Selezionare l\'opzione **Drafting → <img src="images/Draft_Wire.svg" width=16px> Polilinea** dal menu.
    -   Usare la scorciatoia da tastiera: **P** poi **L**.



## Note

-   Un Polilinea può essere modificata con il comando [Modifica](Draft_Edit/it.md).
-   Una Polilinea può essere convertita in una [BSpline](Draft_BSpline/it.md) con il comando [Polilinea in BSpline](Draft_WireToBSpline/it.md).
-   [Linee](Draft_Line/it.md) e Polilinee possono anche essere unite con il comando [Unisci](Draft_Join/it.md) o il comando [Promuovi](Draft_Upgrade/it.md).



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento delle coordinate: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per modificare il valore iniziale della modalità riempimento: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Riempi gli oggetti con le facce quando possibile**. La modifica della modalità di riempimento in un pannello delle attività sovrascriverà questa preferenza per la sessione corrente di FreeCAD.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Polilinea è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Draft}}

-    **Area|Area**: (sola lettura) specifica l\'area della faccia della polilinea. Il valore sarà {{value|0.0}} se **Make Face** è `False` o la faccia non può essere creata.

-    **Base|Link**
    

-    **Chamfer Size|Lenght**: specifica la lunghezza degli smussi agli angoli della polilinea.

-    **Closed|Bool**: specifica se la polilinea è chiusa o meno. Se la polilinea è inizialmente aperta questo valore è `False`, impostandolo su `True` disegnerà un segmento di linea per chiudere la polilinea. Se la polilinea è inizialmente chiusa questo valore è `True`, impostandolo su `False` rimuoverà l\'ultimo segmento di linea e aprirà la polilinea.

-    **End|VectorDistance**: specifica il punto finale dela polilinea.

-    **Fillet Radius|Lenght**: specifica il raggio dei raccordi agli angoli della polilinea.

-    **Length|Length**: (sola lettura) specifica la lunghezza totale della polilinea.

-    **Make Face|Bool**: specifica se la polilinea forma o meno una faccia. Se è `True` viene creata una faccia, altrimenti solo i bordi sono considerati parte dell\'oggetto. Questa proprietà funziona solo se **Closed** è `True` e se il collegamento non si autointerseca.

-    **Points|VectorList**: specifica i punti della polilinea nel suo sistema di coordinate locale.

-    **Start|VectorDistance**: specifica il punto iniziale della polilinea.

-    **Subdivisions|Integer**: specifica il numero di suddivisioni per ogni bordo della polilinea. Se è {{value|1}} ogni spigolo sarà diviso in {{value|2}} segmenti uguali. Le suddivisioni vengono applicate prima di smussi e raccordi.

-    **Tool|Link**
    



### Vista


{{TitleProperty|Draft}}

-    **Arrow Size|Lenght**: specifica la dimensione del simbolo visualizzato all\'estremità della polilinea.

-    **Arrow Type|Enumeration**: specifica il tipo di simbolo visualizzato all\'estremità della polilinea, che può essere {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} o {{value|Tick-2}}.

-    **End Arrow|Bool**: specifica se mostrare un simbolo all\'estremità della polilinea, in modo che possa essere utilizzato come linea di annotazione.

-    **Pattern|Enumeration**: specifica la [Campitura](Draft_Pattern/it.md) con cui riempire la faccia del contorno chiuso. Questa proprietà funziona solo se **Make Face** è `True` e se **Display Mode** è {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una Draft Polilinea usare il metodo `make_wire` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeWire`.


```python
wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
wire = make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
```

-   Crea un oggetto `Wire` con l\'elenco di punti indicato, `pointslist`.
    -   Ogni punto nella lista è definito dal suo `FreeCAD.Vector`, con unità in millimetri.
    -   In alternativa, l\'input può essere una `Part.Wire`, da cui vengono estratti i punti.
-   Se `closed` è `True`, o se il primo e l\'ultimo punto coincidono, la polilinea è chiusa.
-   Se `placement` è `None` la forma viene creata nell\'origine.
-   Se `face` è `True` e la polilinea è chiusa, diventa una faccia e appare riempita.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

wire1 = Draft.make_wire([p1, p2, p3], closed=True)
wire2 = Draft.make_wire([p1, 2*p3, 1.3*p2], closed=True)
wire3 = Draft.make_wire([1.3*p3, p1, -1.7*p2], closed=True)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Wire/it
