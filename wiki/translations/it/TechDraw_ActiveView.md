---
- GuiCommand:/it
   Name:TechDraw_ActiveView
   Name/it:Vista attiva
   Icon:TechDraw_ActiveView.svg
   MenuLocation:TechDraw → Vista attiva
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Simbolo](TechDraw_Symbol/it.md)
   Version:0.19
---


</div>

## Descrizione

Lo strumento Vista attiva inserisce una copia di una finestra 3D in una pagina di disegno.

![](images/TechDraw_ActiveView_example.png )


*Una vista semplice dal modello 3D.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Passare alla finestra 3D che si desidera copiare.
2.  Se nel documento sono presenti più pagine di disegno, è necessario selezionare nella struttura ad albero anche la pagina desiderata.
3.  Premere il pulsante **<img src="images/TechDraw_ActiveView.svg" width=16px> [Vista attiva](TechDraw_ActiveView/it.md)**.
4.  Si apre una finestra di dialogo che consente di specificare le dimensioni, il colore del bordo e dello sfondo della copia.


</div>

## Note

-   Le viste attive sono statiche, una volta generate non vengono mai aggiornate con le modifiche al modello 3D.
-   Vista attiva in realtà è un <img alt="" src=images/TechDraw_Symbol.svg  style="width:24px;"> [Simbolo](TechDraw_Symbol/it.md). La sua proprietà **Scale Type** viene quindi sempre inizializzata come *Personalizzata*.
-   Questo strumento è ancora in qualche modo **sperimentale**.

## Proprietà


<div class="mw-translate-fuzzy">

Vedere <img alt="" src=images/TechDraw_Symbol.svg  style="width:16px;"> [Simbolo](TechDraw_Symbol/it.md)


</div>

### Campi di dialogo 

-    **Width**: la larghezza della vista generata.

-    **Height**: l\'altezza della vista generata.

-    **Border**: la quantità di spazio vuoto da lasciare intorno alla vista, ma all\'interno di Larghezza x Altezza.

-    **Background**: mostra o nasconde lo sfondo.

-    **Background Color**: colore dello sfondo, se applicabile.

-    **Line Width**: spessore delle singole linee nella vista.

-    **Render Mode**: il [render mode](https://grey.colorado.edu/coin3d/classSoRenderManager.html#a4b8d99cff0fd91e31bc2c5d33610f6eb) della libreria [Coin3d](https://en.wikipedia.org/wiki/Coin3D). Le modalità possibili sono:

    -   **AS\_IS** rende le primitive come sono
    -   **WIREFRAME** rende i poligoni come polilinee
    -   **POINTS** rende solo i vertici dei poligoni e delle linee
    -   **WIREFRAME\_OVERLAY** rende una polilinea sovrapposta alla modalità AS\_IS
    -   **HIDDEN\_LINE** come **WIREFRAME**, ma elimina le linee che altrimenti non verrebbero mostrate a causa dell\'abbattimento geometrico
    -   **BOUNDING\_BOX** mostra solo il parallelepipedo di contenimento di ciascun oggetto

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[TechDraw API](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Vista attiva può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
