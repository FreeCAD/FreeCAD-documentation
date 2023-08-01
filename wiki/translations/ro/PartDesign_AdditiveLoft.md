---
- GuiCommand:
   Name:PartDesign AdditiveLoft
   Name/ro:PartDesign Loft Aditivă
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:Part Design → Additive loft
   Version:0.17
   SeeAlso:[[PartDesign AdditivePipe/ro]]
---

# PartDesign AdditiveLoft/ro


</div>



## Descriere

**Additive Loft** creează un solid (printr-o extrudarea gen suprafață riglată) în corpul activ (Body) prin realizarea unei tranziții între două sau mai multe polilinii închise sau deschise (denumite și schițe sau secțiuni transversale) Dacă corpul conține deja funcții , Additiv Loft va fi lipit de ele.

![](images/PartDesign_AddLoft_example.png )


<div class="mw-translate-fuzzy">

*În partea dreaptă: cross-sections (A), (B) and (C); Additive loft creat în partea dreaptă.*


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

### Dialog-based workflow 


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/PartDesign_AdditiveLoft.png" width=24px> '''Additive loft'''** button.
2.  In the **Select feature** dialog, select a sketch to be used as first cross-section and click **OK**.
    -   Alternatively, a single sketch can be selected prior to pressing the Additive loft button.
3.  In the **Loft parameters**, press the **Add Section** button.
4.  Select a sketch in the 3D view. Repeat to select more sketches.
5.  Definiți opțiunile dacă trebuie și click pe **OK**.


</div>

### Selection-based workflow 

1.  Select several sketches. It is hereby important in what order you select them:
    -   The sketch selected at first will become the base profile object in the next step
    -   The sketches selected after the first one will become the loft sections. Also here the selection order is important: The sketch selected as second will become the first loft section, the one selected as third becomes the second section and so on. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.
    -   The first or last selection can also be a face of a 3D object (<small>(v0.20)</small> )
2.  Press the **[<img src=images/PartDesign_AdditiveLoft.svg style="width:24px"> [Additive loft](PartDesign_AdditiveLoft.md)** button.
3.  Set options if needed and click **OK**.



## Opţiuni


<div class="mw-translate-fuzzy">

-   **Ruled surface**: face tranziții drepte între secțiuni transversale. Dos nu se aplică la o mansardă/loft cu două secțiuni transversale. Dacă nu este bifată, tranzițiile vor fi netede.
-   **Closed**: makes a transition from the last cross-section to the first, creating a loop.
-   Apăsați butonul **Remove Section** pentru a șterge schița, selectându-l în vizualizarea 3D.


</div>



## Proprietăți


<div class="mw-translate-fuzzy">

-    **Label**: numele dat operațiiunii, acest nume poate fi schimbat la ușurință.

-    **Sections**: lists the sections used.

-    **Ruled**: see [Options](#Options.md).

-    **Closed**: see [Options](#Options.md).

-    **Midplane**: non applicable.

-    **Reversed**: non applicable.

-    **Refine**: adevărat sau fals. Dacă este setat la true, curăță solidul de margini reziduale lăsate de caracteristici. Consultați [Part RefineShape](Part_RefineShape.md) pentru mai multe detalii.


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

-   [Part Loft Technical Details](Part_Loft_Technical_Details.md) explains how a [Part Loft](Part_Loft.md) is created, much of its content is relevant to the PartDesign Additive loft.


</div>





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveLoft/ro
