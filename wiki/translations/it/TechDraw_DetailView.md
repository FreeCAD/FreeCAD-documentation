---
- GuiCommand:
   Name: TechDraw_DetailView
   Name/it: Dettaglio
   MenuLocation: TechDraw - Dettaglio
   Workbenches: [TechDraw](TechDraw_Workbench/it.md)
   SeeAlso: [Vista](TechDraw_View/it.md), [Gruppo di proiezioni](TechDraw_ProjectionGroup/it.md)
---

# TechDraw DetailView/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Dettaglio crea una vista che contiene l\'ingrandimento di un\'area di una vista esistente.


</div>

![](images/ViewDetail.png ) 
*Vista di dettaglio con casella di visualizzazione circolare di una vista esistente*



## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare una vista in una pagina o nella struttura.
-   Premere il pulsante **<img src="images/TechDraw_DetailView.svg" width=16px> [Dettaglio](TechDraw_DetailView/it.md)** per creare la vista del dettaglio.
-   Nella finestra di dialogo delle azioni che viene visualizzata è possibile definire il raggio della casella della vista, la scala e la posizione della vista. Per quest\'ultima si può:
    -   editare le coordinate, oppure
    -   premere il pulsante **Drag Highlight**. In questo caso il bordo originale del dettaglio viene evidenziato in grassetto e con l\'etichetta *trascina*. Fare clic sul bordo o sull\'etichetta, tenere premuto il pulsante del mouse e trascinalo nella posizione desiderata. Rilasciare infine il mouse per accettare la modifica.


</div>

La vista Dettaglio può essere visualizzata in una casella rotonda o quadrata. Questo è controllato dalle [preferenze](TechDraw_Preferences/it#Annotazioni.md) impostate in **Contorno del dettaglio**.

## Properties Detail View 

See also [TechDraw View](TechDraw_View#Properties.md).

### Data


{{TitleProperty|Detail}}

-    **Base View|Link**: The view on which this Detail view is based.

-    **Anchor Point|Vector**: The center of the Detail view within the **Base View**.

-    **Radius|Float**: The size of the area in the **Base View** that is displayed in the Detail view.

-    **Reference|String**: An identifier for the Detail view in the **Base View**.

## Properties Base View 


<div class="mw-translate-fuzzy">

### Vista base 

Una vista Dettaglio eredita tutte le proprietà applicabili della vista specificata come **BaseView**. Nelle proprietà di questa vista è possibile modificare l\'aspetto del contorno del dettaglio:


</div>

-    **Highlight Adjust**: angolo di rotazione in senso orario della vista Dettaglio.

-    **Highlight Line Color**: Colore della linea per la forma del contorno. L\'impostazione predefinita per questo è l\'impostazione **Detail Highlight** nelle [preferenze di TechDraw](TechDraw_Preferences/it.md).

-    **Highlight Line Style**: Stile di linea per la forma del contorno. L\'impostazione predefinita per questo è l\'impostazione **Detail Highlight Style** nelle [preferenze di TechDraw](TechDraw_Preferences/it.md).

## Notes


<div class="mw-translate-fuzzy">

## Note

-   [Una buona discussione sull\'impostazione dell\'ancoraggio](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)


</div>



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


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/it
