# PartDesign SubtractiveLoft/ro
---
- GuiCommand   *   Name   *PartDesign SubtractiveLoft   Workbenches   *[MenuLocation   *Part Design → Subtractive loft   Shortcut   *None   SeeAlso   *[[PartDesign AdditiveLoft|Additive loft](PartDesign_Workbench___PartDesign]].md), [Subtractive pipe](PartDesign_SubtractivePipe.md)---


</div>

## Descriere

Instrumentul **Subtractive Loft** creează un solid substractiv în Corpul activ făcând o tranziție lisă între două sau mai multe schițe (denumite și secțiuni transversale). Forma sa este scăzută din solidul existent.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

### Dialog-based workflow 

1.  Press the **[<img src=images/PartDesign_SubtractiveLoft.svg style="width   *24px"> [Subtractive loft](PartDesign_SubtractiveLoft.md)** button.
2.  In the **Select feature** dialog, select a sketch to be used as base profile object and click **OK**.
    -   Alternatively, either a single sketch or the face of a 3D object (<small>(v0.20)</small> ) can be selected prior to pressing the subtractive loft button.
3.  In the **Loft parameters**, press the **Add Section** button.
4.  Select the next sketch in the [3D view](3D_view.md). Repeat to select more sketches in the order you want them to be lofted through. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
5.  Set options if needed and click **OK**.

### Selection-based workflow 


<small>(v0.19)</small> 

1.  Select several sketches. It is hereby important in what order you select them   *
    -   The sketch selected at first will become the base profile object in the next step
    -   The sketches selected after the first one will become the loft sections. Also here the selection order is important   * The sketch selected as second will become the first loft section, the one selected as third becomes the second section and so on. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
    -   The first or last selection can also be a face of a 3D object (<small>(v0.20)</small> )
2.  Press the **[<img src=images/PartDesign_SubtractiveLoft.svg style="width   *24px"> [Subtractive loft](PartDesign_SubtractiveLoft.md)** button.
3.  Set options if needed and click **OK**.

## Opţiuni


<div class="mw-translate-fuzzy">

-   **Ruled surface**   * face tranziții drepte între secțiuni transversale. Dos nu se aplică la o mansardă cu două secțiuni transversale. Dacă nu este bifată, tranzițiile vor fi netede.
-   **Closed**   *face o tranziție de la ultima secțiune transversală la prima, creând o buclă.
-   Apăsați butonul **Remove Section** pentru a șterge o schiță, prin selectarea ei într-o vizualizarea 3D.


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Label**   * numele dat operațiiunii, acest nume poate fi schimbat la nevoie.

-    **Sections**   * listează secțiunile utilizate.

-    **Ruled**   * a se vedea [Options](#Options.md).

-    **Closed**   * a se vedea [Options](#Options.md).

-    **Midplane**   * non applicable.

-    **Reversed**   * non applicable.

-    **Refine**   * adevărat sau fals. Dacă este setat la true, curăță solidul de margini reziduale lăsate de funcții. Consultați [Part RefineShape](Part_RefineShape.md) pentru mai multe detalii.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Schițele trebuie să formeze profiluri închise.
-   Nu se poate folosi instrumentul loft către un punct/ vertex.
-   O secțiune transversală nu poate fi așezată pe același plan ca cea precedentă.
-   Pentru a controla mai bine forma loftului, se recomandă ca toate secțiunile transversale să aibă același număr de segmente. De exemplu, pentru un loft între un dreptunghi și un cerc, cercul poate fi împărțit în 4 arce conectate.


</div>

## Legături


<div class="mw-translate-fuzzy">

-   [Part Loft Technical Details](Part_Loft_Technical_Details.md) explică cum o [Part Loft](Part_Loft.md) este creată, o mare parte din conținutul său este relevant pentru instrumetnul Loft(mansardarea) subtractivă PartDesign.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveLoft/ro
