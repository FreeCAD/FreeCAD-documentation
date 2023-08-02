---
- GuiCommand:
   Name: Draft_Scale
   Name/it: Scala
   MenuLocation: Modifiche -> Scala
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Shortcut: **S** **C**
   SeeAlso: Draft_SubelementHighlight/it, Draft Clone/it
---

# Draft Scale/it



## Descrizione

Il comando <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> **Scala** ridimensiona o copia gli oggetti selezionati intorno ad un punto base. In modalità sottoelemento il comando ridimensiona i punti e i bordi selezionati di [Linee](Draft_Line/it.md) e [Polilinee](Draft_Wire/it.md).

Il comando può essere utilizzato su oggetti 2D creati con [Draft](Draft_Workbench/it.md) o [Sketcher](Sketcher_Workbench/it.md), ma anche su molti oggetti 3D come quelli creati con gli ambienti [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).

<img alt="" src=images/Draft_Scale_example.png  style="width:400px;"> 
*Ridimensionamento di un oggetto attorno a un punto base*



## Utilizzo

Vedere anche: [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Opzionalmente selezionare uno o più oggetti, o uno o più sottoelementi di [Linee](Draft_Line/it.md) o [Polilinee](Draft_Wire/it.md).
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Scale.svg" width=16px> [Scala](Draft_Scale/it.md)**.
    -   Selezionare l\'opzione **Modifica → <img src="images/Draft_Scale.svg" width=16px> Scala** dal menu.
    -   Usare la scorciatoia da tastiera: **S** poi **C**.
3.  Se non si ha ancora selezionato un oggetto: selezionare un oggetto nella [Vista 3D](3D_view/it.md).
4.  Si apre il pannello attività **Scala**. Vedi [Opzioni](#Opzioni.md) per maggiori informazioni.
5.  Se i sottoelementi sono stati selezionati: selezionare la casella **Modifica i sottoelementi** per attivare la modalità sottoelemento.
6.  Scegliere il punto base nella [Vista 3D](3D_view/it.md), oppure digitare le coordinate e premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto**.
7.  Immettere i fattori di scala X, Y e Z.
8.  Premere **Enter** o il pulsante **OK** per terminare il comando.



## Opzioni



### Pannello prima attività 

Le scorciatoie da tastiera a carattere singolo menzionate qui possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per inserire manualmente le coordinate per il punto base, inserire le componenti X, Y e Z e premere **Invio** dopo ciascuna. Oppure si può premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando ha i valori desiderati. Si consiglia di spostare il puntatore fuori dalla [Vista 3D](3D_view/it.md) prima di inserire le coordinate.
-   Premere **G** o fare clic sulla casella di controllo **Globale** per attivare o disattivare la modalità globale. Se la modalità globale è attiva, le coordinate sono relative al sistema di coordinate globale, altrimenti sono relative al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md). {{Version/it|0.20}}
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).
-   Premere il pulsante **Chiudi** per interrompere il comando.



### Pannello seconda attività 

-   Immettere i fattori X, Y e Z per definire il ridimensionamento. I valori devono essere maggiori di zero.
-   Selezionare la casella **Scalatura uniforme** per bloccare i fattori X, Y e Z sullo stesso valore.
-   Se la checkbox **Orientamento del piano di lavoro** è spuntata i fattori di scala sono relativi al sistema di coordinate [piano di lavoro](Draft_SelectPlane/it.md), altrimenti sono relativi al sistema di coordinate globale.
-   Se la checkbox **Copia** è spuntata, viene creata una copia in scala dell\'oggetto originale. Questo funziona solo per gli oggetti Draft che hanno una proprietà **Points**, come [Polilinee](Draft_Wire/it.md).
-   Se la casella di controllo **Modifica i sottoelementi** è selezionata, il comando utilizzerà i sottoelementi selezionati anziché tutti gli oggetti. I sottoelementi devono appartenere a [Linee](Draft_Line/it.md) o [Polilinee](Draft_Wire/it.md).
-   Se la casella di controllo **Crea un clone** è selezionata, vengono creati [cloni](Draft_Clone/it.md) ridimensionati degli oggetti originali. Questo funziona per tutti i tipi di oggetto. Per oggetti che non sono oggetti Draft, o per oggetti Draft che non hanno una proprietà **Points**, questa opzione **deve** essere selezionata.
-   Premere il pulsante **Selezionare i punti da/a** e scegliere due punti aggiuntivi nella [Vista 3D](3D_view/it.md) per calcolare i fattori di scala. Questo selezionerà automaticamente la casella di controllo **Scalatura uniforme**. I fattori di scala X, Y e Z saranno quindi uguali e saranno impostati alla distanza tra il punto base e il punto \'da\', divisa per la distanza tra il punto base e il punto \'a\'.
-   Premere **Esc** o il pulsante **Annulla** per interrompere il comando.



## Note

-   Il comando può anche ridimensionare [Piani Immagine](Image_CreateImagePlane/it.md), ma non in modalità clone.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento dei fattori di scala ({{Version/it|0.20}}) e delle coordinate: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.
-   Per riselezionare gli oggetti di base dopo averli copiati: **Modifica → Preferenze... → Draft → Impostazioni generali → Opzioni strumenti di disegno → Seleziona gli oggetti di base dopo la copia**.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per scalare gli oggetti usare il metodo `scale` del modulo Draft.


```python
scaled_list = scale(objectslist, scale=Vector(1,1,1), center=Vector(0,0,0), copy=False)
```

-    `objectslist`contiene gli oggetti da scalare. È un singolo oggetto o un elenco di oggetti.

-    `scale`è il vettore che specifica i fattori di scala X, Y e Z.

-    `center`è il punto centrale dell\'operazione di ridimensionamento.

-   Se `copy` è `True` vengono create delle copie invece di ridimensionare gli oggetti originali.

-    `scaled_list`viene restituito con gli oggetti ridimensionati originali o con le nuove copie. È un singolo oggetto o un elenco di oggetti, a seconda di `objectslist`.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pts = [App.Vector(0, 0, 0), App.Vector(500, 500, 0), App.Vector(600, 0, 0)]
wire1 = Draft.make_wire(pts, closed=True)
doc.recompute()

scale1 = App.Vector(2.3, 0.75, 0)
wire2 = Draft.scale(wire1, scale1, copy=True)
doc.recompute()

scale2 = App.Vector(-2, -1.5, 0)
wires = Draft.scale([wire1, wire2], scale2, copy=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Scale/it
