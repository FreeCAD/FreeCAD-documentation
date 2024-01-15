---
 GuiCommand:
   Name: TechDraw_DetailView
   Name/it: Dettaglio
   MenuLocation: TechDraw , Dettaglio
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_View/it, TechDraw_ProjectionGroup/it
---

# TechDraw DetailView/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Dettaglio crea una vista che contiene l\'ingrandimento di un\'area di una vista esistente.


</div>

![](images/ViewDetail.png )


<div class="mw-translate-fuzzy">



*Vista di dettaglio con casella di visualizzazione circolare di una vista esistente*


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare una vista in una pagina o nella struttura.
-   Premere il pulsante **<img src="images/TechDraw_DetailView.svg" width=16px> [Dettaglio](TechDraw_DetailView/it.md)** per creare la vista del dettaglio.
-   Nella finestra di dialogo delle azioni che viene visualizzata è possibile definire il raggio della casella della vista, la scala e la posizione della vista. Per quest\'ultima si può:
    -   editare le coordinate, oppure
    -   premere il pulsante **Drag Highlight**. In questo caso il bordo originale del dettaglio viene evidenziato in grassetto e con l\'etichetta *trascina*. Fare clic sul bordo o sull\'etichetta, tenere premuto il pulsante del mouse e trascinalo nella posizione desiderata. Rilasciare infine il mouse per accettare la modifica.


</div>

## Notes

-   To edit a detail view double-click it in the [Tree view](Tree_view.md).
-   The outlines of detail views can be round or square. This is controlled by the **Detail View Outline Shape** [preference](TechDraw_Preferences#Annotation.md).
-   [Forum topic with a good discussion about setting the anchor.](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)

## Properties Detail View 

See also [TechDraw View](TechDraw_View#Properties.md).

### Data


{{TitleProperty|Detail}}

-    **Base View|Link**: The view on which the detail view is based.

-    **Anchor Point|Vector**: The center of the detail view within the **Base View**.

-    **Radius|Float**: The size of the area in the **Base View** that is displayed in the detail view.

-    **Reference|String**: An identifier for the detail view in the **Base View**.

## Properties Base View 


<div class="mw-translate-fuzzy">

### Vista base 

Una vista Dettaglio eredita tutte le proprietà applicabili della vista specificata come **BaseView**. Nelle proprietà di questa vista è possibile modificare l\'aspetto del contorno del dettaglio:


</div>

### View


{{TitleProperty|Hightlight}}


<div class="mw-translate-fuzzy">

-    **Highlight Adjust**: angolo di rotazione in senso orario della vista Dettaglio.

-    **Highlight Line Color**: Colore della linea per la forma del contorno. L\'impostazione predefinita per questo è l\'impostazione **Detail Highlight** nelle [preferenze di TechDraw](TechDraw_Preferences/it.md).

-    **Highlight Line Style**: Stile di linea per la forma del contorno. L\'impostazione predefinita per questo è l\'impostazione **Detail Highlight Style** nelle [preferenze di TechDraw](TechDraw_Preferences/it.md).


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/it
