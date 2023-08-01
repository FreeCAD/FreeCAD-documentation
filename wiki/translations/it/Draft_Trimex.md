---
- GuiCommand:
   Name:Draft Trimex
   Name/it:Taglia/Estendi
   MenuLocation:Modifiche - Taglia/Estendi
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**T** **R**
   SeeAlso:Parte - [Estrudi](Part_Extrude/it.md)
---

# Draft Trimex/it



## Descrizione

Il comando <img alt="" src=images/Draft_Trimex.svg  style="width:24px;"> **Taglia/Estendi** [taglia o estende](#Taglia_o_estendi.md) un oggetto selezionato. Le intersezioni con il bordo di un altro oggetto possono essere utilizzate per determinare nuovi punti finali. Il comando può essere utilizzato anche per [estrudere](#Estrusione.md) una faccia, nel qual caso crea un oggetto [Part Estrusione](Part_Extrude/it.md).

<img alt="" src=images/Draft_trimex_example.jpg  style="width:400px;"> 
*In alto: una polilinea estesa e poi tagliata.<br>
In basso: una faccia estrusa in un corpo solido.*



## Taglia o estendi 



### Utilizzo

1.  Facoltativamente selezionare un oggetto. L\'oggetto deve essere una [Linea](Draft_Line/it.md), un [Polilinea](Draft_Wire/it.md), un [Arco](Draft_Arc/it.md) o un [Cerchio](Draft_Circle/it.md) (che può solo essere tagliato) . Se l\'oggetto selezionato è chiuso, deve avere la proprietà **Make Face** impostata su `False`.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Trimex.svg" width=16px> [Taglia/Estendi](Draft_Trimex/it.md)**.
    -   Selezionare l\'opzione **Modifica → <img src="images/Draft_Trimex.svg" width=16px> Taglia/Estendi** dal menu.
    -   Usare la scorciatoia da tastiera: **T** poi **R**.
3.  Se non si ha ancora selezionato un oggetto: selezionare un oggetto nella [Vista 3D](3D_view/it.md).
4.  Si apre il pannello delle attività **Taglia/Estendi**. Vedere [Opzioni](#Opzioni.md) per maggiori informazioni.
5.  Spostare il puntatore nella [VIsta 3D](3D_view/it.md) in modo che l\'anteprima corrisponda al risultato desiderato. Se necessario utilizzare i tasti modificatori come spiegato nelle [Opzioni](#Opzioni.md).
6.  Effettuare una delle seguenti operazioni:
    -   Scegliere un punto nella [Vista 3D](3D_view/it.md).
    -   Inserire una **Distanza** o un **Angolo**. La distanza è una distanza delta. Questa opzione non funziona se vengono utilizzati i tasti modificatori.
    -   Spostare il puntatore su un bordo appartenente a un altro oggetto e fare clic quando questo bordo è evidenziato, per tagliare o estendere l\'oggetto selezionato utilizzando un\'intersezione con il bordo evidenziato come nuovo punto finale. Durante il taglio, la proiezione del punto in cui è selezionato il bordo di taglio sull\'oggetto da tagliare determina il risultato predefinito. Notare che gli [Snap](Draft_Snap/it.md) possono avere un impatto indesiderato. In alcuni casi può essere utile disattivarli temporaneamente.



### Opzioni

Le scorciatoie da tastiera a carattere singolo menzionate qui possono essere modificate. Vedere [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Tenere premuto **Alt** per invertire il risultato predefinito del comando.
-   Tenere premuto **Maiusc** per restringere l\'operazione al segmento corrente di una [Polilinea](Draft_Wire/it.md).
-   Premere **S** per attivare o disattivare [Aggancia](Draft_Snap/it.md).

Ecco un esempio per spiegare i tasti modificatori. Il bordo sinistro o il bordo inferiore della polilinea a forma di U è stato esteso. Tutti gli [Snap](Draft_Snap/it.md) sono stati disattivati.

![](images/Draft_Trimex_example2.png )

1.  L\'arco è stato cliccato vicino all\'angolo in basso a sinistra della polilinea. Questo è il risultato predefinito.

2.  
    **Alt**è stato tenuto premuto mentre si faceva clic sull\'arco vicino all\'angolo in basso a sinistra del filo.

3.  
    **Y**è stato premuto, e mentre si passava sopra il bordo sinistro **Maiusc** è stato tenuto premuto e quindi è stato fatto clic sull\'arco. La pressione di **Y** è richiesta solo per i bordi che sono più o meno paralleli all\'asse Y.



## Estrusione



### Utilizzo 

Vedere anche: [Aggancio](Draft_Snap/it.md) e [Vincolare](Draft_Constrain/it.md).

1.  Può essere utile modificare prima il [piano di lavoro](Draft_SelectPlane/it.md) in modo che non sia complanare con la faccia che si desidera estrudere.
2.  Facoltativamente, selezionare una faccia singola o un oggetto con una faccia singola.
3.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Trimex.svg" width=16px> [Taglia/Estendi](Draft_Trimex/it.md)**.
    -   Selezionare l\'opzione **Modifiche → <img src="images/Draft_Trimex.svg" width=16px> Taglia/Estendi** dal menu.
    -   Usare la scorciatoia da tastiera: **T** poi **R**.
4.  Se non si ha ancora selezionato un oggetto o una faccia: selezionare un oggetto con una sola faccia nella [Vista 3D](3D_view/it.md).
5.  Si apre il pannello delle attività **Taglia/Estendi**. Vedere [Opzioni](#Opzioni_2.md) per ulteriori informazioni.
6.  Per definire la direzione e la distanza di estrusione, eseguire una delle seguenti operazioni:
    -   Scegliere un punto nella [Vista 3D](3D_view/it.md) che non giace sullo stesso piano della faccia.
    -   Assicurarsi che il puntatore si trovi sul lato corretto della faccia nella [ista 3D](3D_view/it.md) ed inserire una **Distanza**.



### Opzioni 

Il tasto modificatore menzionato qui può essere modificato. Vedere [Preferenze di Draft](Draft_Preferences/it.md).

-   Tenere premuto **Maiusc** per estrudere in una direzione che non è parallela alla normale della faccia.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Per modificare il numero di decimali utilizzati per l\'inserimento delle coordinate: **Modifica → Preferenze... → Generale → Unità → Impostazioni unità → Numero di cifre decimali**.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Non esiste un metodo Python per tagliare gli oggetti. Per estrudere oggetti usa il metodo `extrude` del modulo Draft.


```python
extrusion = extrude(obj, vector, solid=False)
```

-    `obj`è l\'oggetto da estrudere.

-    `vector`è la direzione e la distanza di estrusione.

-   Se `solid` è `True` viene creato un solido invece di un guscio.

-    `extrusion`viene restituito con l\'oggetto creato.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(1500, 500)
doc.recompute()

vector = App.Vector(0, 0, 300)
solid = Draft.extrude(rectangle, vector, solid=True)
doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Trimex/it
