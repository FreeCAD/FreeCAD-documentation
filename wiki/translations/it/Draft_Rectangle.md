---
- GuiCommand:
   Name: Draft Rectangle
   Name/it: Rettangolo
   MenuLocation: Drafting - Rettangolo
   Workbenches: [Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut: **R** **E**
   Version: 0.7
---

# Draft Rectangle/it



## Descrizione

Il comando <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> **Rettangolo** crea un rettangolo nel [piano di lavoro](Draft_SelectPlane/it.md) corrente da due punti.

È possibile aggiungere facoltativamente uno smusso di 45 gradi o un raccordo circolare a ogni angolo del rettangolo e dividere il rettangolo in una serie di righe e colonne di uguale dimensione.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width:400px;"> 
*Rettangolo definito da due punti*



## Utilizzo

Vedere anche: [Barra di Draft](Draft_Tray/it.md), [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Rectangle.svg" width=16px> [Rettangolo](Draft_Rectangle/it.md)**.
    -   Selezionare l\'opzione **Drafting → <img src="images/Draft_Rectangle.svg" width=16px> Rettangolo** dal menu.
    -   Usare la scorciatoia da tastiera: **R** poi **E**.
2.  Si apre il pannello delle attività **Rectangle**. Vedere [Opzioni](#Options.md) per maggiori informazioni.
3.  Scegliere il primo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
4.  Scegliere il secondo punto nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**. Questo punto non deve essere vincolato all\'asse X, Y o Z.



## Opzioni

Le scorciatoie da tastiera a carattere singolo disponibili nel pannello delle attività possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md). Le scorciatoie menzionate qui sono le scorciatoie predefinite.

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **R** o fare clic sulla casella di controllo **Relativo** per attivare o disattivare la modalità relativa. Se la modalità relativa è attiva, le coordinate del secondo punto sono relative al primo punto, altrimenti sono relative all\'origine del sistema di coordinate.
-   Premee **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **L** o fare clic sulla casella di controllo **Riempito** per attivare o disattivare la modalità riempimento. Se la modalità riempimento è attiva, il rettangolo creato avrà **Make Face** impostato su `True` e avrà una faccia piena.
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando verrà riavviato al termine, consentendo di continuare a creare rettangoli.
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Un Rettangolo può essere modificato con il comando [Modifica](Draft_Edit/it.md).



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento delle coordinate: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per modificare il valore iniziale della modalità riempimento: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Riempi gli oggetti con le facce quando possibile**. La modifica della modalità di riempimento in un pannello delle attività sovrascriverà questa preferenza per la sessione corrente di FreeCAD.
-   Se l\'opzione **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti Draft → Usa le primitive di Part quando disponibili** è selezionata, il comando creerà un [Part Piano](Part_Plan/it.md) invece di un Draft Rettangolo.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Rettangolo è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Draft}}

-    **Area|Area**: (sola lettura) specifica l\'area della faccia del rettangolo. Il valore sarà {{value|0.0}} se **Make Face** se `False`.

-    **Chamfer Size|Length**: specifica la lunghezza degli smussi agli angoli del rettangolo.

-    **Columns|Integer**: specifica il numero di colonne di uguali dimensioni in cui è diviso il rettangolo.

-    **Fillet Radius|Length**: specifica il raggio dei raccordi agli angoli del rettangolo.

-    **Height|Distance**: specifica l\'altezza del rettangolo.

-    **Length|Distance**: specifica la lunghezza del rettangolo.

-    **Make Face|Bool**: specifica se il rettangolo crea o meno una faccia. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto.

-    **Rows|Integer**: specifica il numero di righe di uguali dimensioni in cui è diviso il rettangolo.



### Vista


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifica la [Campitura](Draft_Pattern/it.md) con cui riempire la faccia del rettangolo. Questa proprietà funziona solo se **Make Face** è `True` e se **Display Mode** è {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifica la dimensione della [Campitura](Draft_Pattern/it.md).

-    **Texture Image|File**: specifica il percorso del file immagine da mappare sulla faccia del rettangolo. L\'oscuramento di questa proprietà rimuoverà l\'immagine. Il rettangolo dovrebbe avere le stesse proporzioni dell\'immagine per evitare distorsioni.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare un Draft Rettangolo usare il metodo `make_rectangle` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeRectangle`.


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```

-   Crea un oggetto `rectangle` con `length` nella direzione X e `height` nella direzione Y, con unità in millimetri.
-   Se `placement` è `None` il rettangolo viene creato all\'origine e la lunghezza sarà parallela all\'asse X.
-   Se `face` è `True`, il rettangolo formerà una faccia, cioè apparirà pieno.

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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rectangle/it
