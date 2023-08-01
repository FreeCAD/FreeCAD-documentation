---
- GuiCommand:
   Name:PartDesign AdditivePipe
   Name/ro:PartDesign AdditivePipe
   Workbenches:[PartDesign](PartDesign_Workbench/ro.md)
   MenuLocation:PartDesign → Additive pipe
   Version:0.17
   SeeAlso:[PartDesign Additive Loft](PartDesign_AdditiveLoft/ro.md)
---

# PartDesign AdditivePipe/ro


</div>

## Descriere

**Additive Pipe** creează un solid în corpul activ, prin baleierea uneia sau a mai multor schițe (denumite și secțiuni transversale) de-a lungul unei căi deschise sau închise. Dacă corpul conține deja funcții(onalități), conductele aditive vor fi îmbinate cu ele.

![](images/PartDesign_AdditivePipe_example.svg )


<div class="mw-translate-fuzzy">

*On the left: cross-sections (A) and (B) to be swept along path (C); resulting Additive pipe on the right.*


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Press the **<img src="images/PartDesign_AdditivePipe.png" width=24px> '''Additive pipe'''** button.
2.  In the **Select feature** dialog, select a sketch to be used as first cross-section and click **OK**.
    -   Alternatively, a single sketch can be selected prior to pressing the Additive pipe button.
3.  In the **Pipe parameters** under **Profile**, press the **Object** button.
4.  Select the sketch to be used as path in the 3D view:
    -   Alternatively, edges of the body can be selected by pressing **Add Edge** and selecting edges in the 3D view.
5.  To use more than one cross-section, under **Section transformation** set the Transform mode to *Multisection*; press **Add Section** then select a sketch in the 3D view. Repeat for each additional cross-section.
6.  Set options if needed and click **OK**.


</div>

To use more than one cross-section, start with the first cross-section sketch as described above. Then under **Section transformation** set the Transform mode to *Multisection*; press **Add Section** then select a sketch in the [3D view](3D_view.md). Repeat for each additional cross-section.

## Options


<div class="mw-translate-fuzzy">

## Opţiuni


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Label**: nume dat operațiunii, acest nume poate fi schimbat dacă este necesar.

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

-    **Sections**: lists the sections used.

-    **Spine Tangent**: true or false (default). True extends the path to include tangent edges.

-    **Auxiliary Spine Tangent**: true or false (default). True extends the auxiliary path to include tangent edges.

-    **Auxiliary Curvelinear**: true or false (default). True calculates normal between equidistant points on both spines.

-    **Mode**: profile mode. See [Options](#Options.md).

-    **Binormal**: binormal vector for corresponding orientation mode.

-    **Transition**: transition mode. Options are *Transformed*, *Right Corner* or *Round Corner*.

-    **Transformation**: \"Constant\" folosește o singură secțiune transversală. \"Multisecția\" utilizează două sau mai multe secțiuni transversale. *Linear*, *S-shape* și *Interpolation* nu sunt în prezent funcționale.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Schițele utilizate pentru secțiunile transversale trebuie să formeze profile închise.
-   Nu este posibil să se utilizeze un vertex ca secțiune transversală.
-   O secțiune transversală nu poate fi așezată pe același plan ca cea precedentă.
-   Pentru a controla mai bine forma conductei/țevii, se recomandă ca toate secțiunile transversale să aibă același număr de segmente. De exemplu, pentru o țeavă între un dreptunghi și un cerc, cercul poate fi împărțit în 4 arce conectate.


</div>





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePipe/ro
