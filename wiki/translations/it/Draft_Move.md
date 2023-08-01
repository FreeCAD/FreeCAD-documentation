---
- GuiCommand:
   Name: Draft_Move
   Name/it: Sposta
   MenuLocation: Modifiche - Sposta
   Workbenches: [Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut: **M** **V**
   Version: 0.7
   SeeAlso: [Evidenzia i sottoelementi](Draft_SubelementHighlight/it.md)
---

# Draft Move/it



## Descrizione

Il comando <img alt="" src=images/Draft_Move.svg  style="width:24px;"> **Sposta** sposta o copia gli oggetti selezionati da un punto all\'altro. In modalità sottoelemento il comando sposta i punti e gli spigoli selezionati, o copia gli spigoli selezionati, di [Linee](Draft_Line/it.md) e [Polilinee](Draft_Wire/it.md).

Il comando può essere utilizzato su oggetti 2D creati con [Draft](Draft_Workbench/it.md) o [Sketcher](Sketcher_Workbench/it.md), ma anche su molti oggetti 3D come quelli creati con gli ambienti [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).

<img alt="" src=images/Draft_Move_example.jpg  style="width:400px;"> 
*Spostare un oggetto da un punto a un altro punto*



## Utilizzo

Vedere anche: [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Opzionalmente selezionare uno o più oggetti, o uno o più sottoelementi di [Linee](Draft_Line/it.md) o [Polilinee](Draft_Wire/it.md).
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Move.svg" width=16px> [Sposta](Draft_Move.md)**.
    -   Selezionare l\'opzione **Modifica → <img src="images/Draft_Move.svg" width=16px> Sposta** dal menu.
    -   Usare la scorciatoia da tastiera: **M** poi **V**.
3.  Se non si ha ancora selezionato un oggetto: selezionare un oggetto nella [Vista 3D](3D_view/it.md).
4.  Si apre il pannello delle attività **Sposta**. Vedere [Opzioni](#Opzioni.md) per maggiori informazioni.
5.  Se i sottoelementi sono stati selezionati: selezionare la casella **Modifica i sottoelementi** per attivare la modalità sottoelemento.
6.  Scegliere il primo punto, il punto base, nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
7.  Scegliere il secondo punto, il punto di destinazione, nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.



## Opzioni

Le scorciatoie da tastiera a carattere singolo menzionate qui possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per inserire manualmente le coordinate, inserire le componenti X, Y e Z e premere **Enter** dopo ognuna di esse. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Per usare le coordinate polari inserire un valore per **Lunghezza** e un valore per **Anglo**, e premere **Enter** dopo ciascuno.
-   Selezionare la casella **Anglo** per vincolare il puntatore all\'angolo specificato.
-   Premere **H** per cambiare il focus dalla casella di input **X** alla casella di input **Lunghezza** e viceversa. A seconda della casella di input che riceve il focus, la casella di controllo **Anglo** è selezionata o deselezionata.
-   Premere **R** o fare clic sulla casella di controllo **Relativo** per attivare o disattivare la modalità relativa. Se la modalità relativa è attiva, le coordinate del secondo punto sono relative al primo punto, altrimenti sono relative all\'origine del sistema di coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **T** o fare clic sulla casella di controllo **Continua** per attivare o disattivare la modalità continua. Se la modalità continua è attiva, il comando verrà riavviato al termine. Questa modalità ha davvero senso solo se la modalità di copia è attivata. A seconda della preferenza **Seleziona gli oggetti di base dopo la copia**, per la successiva chiamata al comando vengono selezionati gli oggetti originali o le copie create per ultime. Vedi [Preferenze](#Preferenze.md).
-   Premere **P** o fare clic sulla casella di controllo **Copia** per attivare o disattivare la modalità di copia. Se la modalità copia è attiva, il comando creerà copie spostate invece di spostare gli oggetti originali.
-   Premere **D** o fare clic sulla casella di controllo **Modifica sottoelementi** per attivare o disattivare la modalità sottoelemento. Se la modalità sottoelemento è attiva, il comando utilizzerà i sottoelementi selezionati invece degli oggetti interi. I sottoelementi devono appartenere a [Linee](Draft_Line/it.md) o [Polilinee](Draft_Wire/it.md).
-   Se la modalità copia e la modalità sottoelemento sono entrambe attive e sono selezionati i bordi di [Polilinee](Draft_Wire/it.md), verranno creati nuove polilinee da quei bordi.
-   Tenendo premuto **Alt** dopo aver scelto il punto base si attiverà anche la modalità di copia. Mentre **Alt** viene tenuto premuto, è possibile selezionare più punti bersaglio. Rilasciare **Alt** per terminare il comando e vedere le copie create.
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Un Oggetto che è [allegato](Part_EditAttachment/it.md) non può essere spostato con il comando Sposta. Per spostarlo è necessario spostare il suo oggetto **Support** o modificare il suo **Attachment Offset**.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento di coordinate, lunghezze e angoli: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per modificare il focus iniziale del pannello delle attività nella casella di immissione **Lunghezza**: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti di Draft → Imposta il focus sulla Lunghezza invece che sulla coordinata X**. Tenere presente che si deve spostare il puntatore nella [Vista 3D](3D_view/it.md) affinché la modifica abbia effetto.
-   Per memorizzare e riutilizzare la stessa impostazione della modalità di copia tra i comandi: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti di Draft → Modalità di copia globale**.
-   Per riselezionare gli oggetti di base dopo averli copiati: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti di Draft → Seleziona gli oggetti di base dopo la copia**.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per spostare gli oggetti usare il metodo `move` del modulo Draft.


```python
moved_list = move(objectslist, vector, copy=False)
```

-    `objectslist`contiene gli oggetti da spostare. È un singolo oggetto o un elenco di oggetti.

-    `vector`è lo spostamento.

-   Se `copy` è `True` vengono create delle copie invece di spostare gli oggetti originali.

-    `moved_list`viene restituito con gli oggetti spostati originali o con le nuove copie. È un singolo oggetto o un elenco di oggetti, a seconda di `objectslist`.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/it
