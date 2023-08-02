---
- GuiCommand:
   Name: TechDraw_ActiveView
   Name/it: Vista attiva
   Icon: TechDraw_ActiveView.svg
   MenuLocation: TechDraw -> Vista attiva
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw Symbol/it
   Version: 0.19
---

# TechDraw ActiveView/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Vista attiva inserisce una copia di una finestra 3D in una pagina di disegno.


</div>

![](images/TechDraw_ActiveView_example.png )


<div class="mw-translate-fuzzy">



*Una vista semplice dal modello 3D.*


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Passare alla finestra 3D che si desidera copiare.
2.  Se nel documento sono presenti più pagine di disegno, è necessario selezionare nella struttura ad albero anche la pagina desiderata.
3.  Premere il pulsante **<img src="images/TechDraw_ActiveView.svg" width=16px> [Vista attiva](TechDraw_ActiveView/it.md)**.
4.  Si apre una finestra di dialogo che consente di specificare le dimensioni, il colore del bordo e dello sfondo della copia.


</div>

## Options

The following can be specified:

-    **Crop**: Crop the generated bitmap.

-    **Width**: The width (in mm) to crop the generated view.

-    **Height**: The height (in mm) to crop the generated view.

-    **No Background**: If checked, the generated bitmap will have a transparent background.

-    **Solid Background**: If checked, the generated will have a background of the selected color.

-    **Use 3d Background**: If checked, the generated bitmap will use the background from the 3D window.



## Note


<div class="mw-translate-fuzzy">

-   Le viste attive sono statiche, una volta generate non vengono mai aggiornate con le modifiche al modello 3D.
-   Vista attiva in realtà è un <img alt="" src=images/TechDraw_Symbol.svg  style="width:24px;"> [Simbolo](TechDraw_Symbol/it.md). La sua proprietà **Scale Type** viene quindi sempre inizializzata come *Personalizzata*.
-   Questo strumento è ancora in qualche modo **sperimentale**.


</div>



## Proprietà


<div class="mw-translate-fuzzy">

Vedere <img alt="" src=images/TechDraw_Symbol.svg  style="width:16px;"> [Simbolo](TechDraw_Symbol/it.md)


</div>


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/it
