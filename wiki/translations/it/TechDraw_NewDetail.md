---
- GuiCommand:/it
   Name:TechDraw_DetailView
   Name/it:Dettaglio
   MenuLocation:TechDraw → Dettaglio
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Vista](TechDraw_View/it.md), [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)
---


</div>

## Descrizione

Lo strumento Dettaglio crea una vista che contiene l\'ingrandimento di un\'area di una vista esistente.

![](images/ViewDetail.png ) *Vista di dettaglio con casella di visualizzazione circolare di una vista esistente*

## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare una vista in una pagina o nella struttura.
-   Premere il pulsante **<img src="images/TechDraw_DetailView.svg" width=16px> [Dettaglio](TechDraw_DetailView/it.md)** per creare la vista del dettaglio.
-   Nella finestra di dialogo delle azioni che viene visualizzata è possibile definire il raggio della casella della vista, la scala e la posizione della vista. Per quest\'ultima si può:
    -   editare le coordinate, oppure
    -   premere il pulsante **Drag Highlight**. In questo caso il bordo originale del dettaglio viene evidenziato in grassetto e con l\'etichetta *trascina*. Fare clic sul bordo o sull\'etichetta, tenere premuto il pulsante del mouse e trascinalo nella posizione desiderata. Rilasciare infine il mouse per accettare la modifica.


</div>

La vista Dettaglio può essere visualizzata in una casella rotonda o quadrata. Questo è controllato dalle [preferenze](TechDraw_Preferences/it#Annotazioni.md) impostate in **Contorno del dettaglio**.

## Proprietà

### Vista dettaglio 

-    **BaseView**: la vista su cui si basa questa vista di dettaglio.

-    **Anchor Point**: il centro della vista Dettaglio all\'interno di **BaseView**.

-    **Radius**: la dimensione dell\'area in **BaseView** che viene visualizzata nella vista Dettaglio.

-    **Scale Type**: Tipo di scala. Le scelte sono:

    -   *Page*: Viene utilizzato il fattore di scala della [Pagina](TechDraw_PageDefault/it.md) del disegno
    -   *Automatic*: Nel caso in cui la vista di dettaglio sia più grande della pagina, viene ridimensionata per adattarsi alla pagina
    -   *Custom*: Un fattore di scala personalizzato impostato da **Scale**

-    **Scale**: grado di ingrandimento.

-    **Reference**: un identificatore per indicare l\'area di **BaseView** che viene visualizzata.

### Vista base 

Una vista Dettaglio eredita tutte le proprietà applicabili della vista specificata come **BaseView**. Nelle proprietà di questa vista è possibile modificare l\'aspetto del contorno del dettaglio:

-    **Highlight Adjust**: angolo di rotazione in senso orario della vista Dettaglio.

-    **Highlight Line Color**: Colore della linea per la forma del contorno. L\'impostazione predefinita per questo è l\'impostazione **Detail Highlight** nelle [preferenze di TechDraw](TechDraw_Preferences/it.md).

-    **Highlight Line Style**: Stile di linea per la forma del contorno. L\'impostazione predefinita per questo è l\'impostazione **Detail Highlight Style** nelle [preferenze di TechDraw](TechDraw_Preferences/it.md).

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Dettaglio può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
Detail = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDetail','Detail')
...TBA
```

## Suggerimenti


<div class="mw-translate-fuzzy">

-   Lo spazio attorno al contorno della vista e al bordo dell\'oggetto vista è di default un\'area bianca. Ciò significa che copre tutto ciò che c\'è dietro. A volte non c\'è abbastanza spazio sulla pagina e si può risparmiare spazio riducendo questa area bianca non necessaria. Questo viene fatto inserendo la vista Dettaglio in un [gruppo di clip](TechDraw_ClipGroup/it.md):


</div>

This is done by putting the Detail view into a [clip group](TechDraw_ClipGroup.md):

![](images/TechDraw_DetailClipped.png ) *Vista di dettaglio in un gruppo di clip*

-   Per le viste di dettaglio con un contorno arrotondato, la posizione dell\'etichetta di riferimento nella vista di base può essere modificata tramite la proprietà **Highlight Adjust** della vista di base.

## Note

-   [Una buona discussione sull\'impostazione dell\'ancoraggio](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
