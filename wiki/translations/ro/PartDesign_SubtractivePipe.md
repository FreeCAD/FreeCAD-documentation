# PartDesign SubtractivePipe/ro
---
- GuiCommand:   Name:PartDesign SubtractivePipe   Workbenches:[MenuLocation:Part Design → Subtractive pipe   Shortcut:None   SeeAlso:[[PartDesign AdditivePipe|Additive pipe](PartDesign_Workbench___PartDesign]].md), [Subtractive loft](PartDesign_SubtractiveLoft.md)---


</div>

## Descriere


<div class="mw-translate-fuzzy">

**Subtractive Pipe** crează un solid substractiv în corpul activ prin baleierea uneia sau mai multor schițe (de asemenea denumite secțiuni transversale) de-a lungul unei traiectorii deschise sau închise. forma sa este apoi scăzută/extrasă din solidul existent.


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Apăsați buntonul **<img src="images/PartDesign_SubtractivePipe.png" width=24px> '''Subtractive pipe'''
**
2.  In dialogul *Select feature*\', selectați o schiță pentru a fi utilizată ca primă scțiune trasnversală și click **OK**.
    -   Ca alternativă, o singură schiță poate fi selectată în prealabil apăsării butonului Subtractive pipe .
3.  In **Pipe parameters** sub **Profile**, apăsați butonul **Object** .
4.  Selectați schița care va fi utilizată ca traiectorie în vizualizarea 3D:
    -   De asemenea, muchiile corpului pot fi selectate prin apăsarea **Add Edge** și selectarea muchiilor în vizualizarea 3D .
5.  Penru a utiliza mai multe secțiuni transversale, sub **Section transformation** setați modul Transform pe *Multisection*; apăsați **Add Section** apoi selectați o schiță în vizulalizarea 3D. Reptați pentru fiecare secțiune transversală adițională.
6.  Setați opțiunile dacă este necesar și click pe **OK**.


</div>

## Opţiuni

**Section Transformation**:

-   Select **Constant** to use a single profile
-   Select **Multisection** to use multiple profiles

**Section Orientation**:

-   Standard
    -   This keeps the cross section shape perpendicular to the path. This is the default setting.
-   Fixed
    -   Orientation set by first profile and constant throughout. This deactivates the alignment to the path normal vector. That means that the cross-section shape will not rotate with the path. Sweep along a circle to see the effect.
-   Frenet
    -   Create minimum possible twisting of profile. For more info, see [Frenet-Serret Formulas](https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas)
-   Auxiliary
    -   Specify secondary path to guide pipe.
    -   For each point **P** along the sweep path, there will be a corresponding point **Q** on the auxiliary path.
    -   As the profile is swept, it will be transformed such that the **PQ** line is the normal of the sweep path.
    -   If **Curvelinear equivalence** is set, then the **Q** points are scaled proportionally along the sweep path, regardless of is length.
-   Binormal
    -   Specify binormal vector in X, Y and Z

**Corner Transition**

-   Transformed
-   Right
-   Rounded

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Label**: nume dat operațiunii, acest nume poate fi schimbat dacă este necesar.

-    **Refine**: true sau false. Dacă este setat true, curăță solidul de muchiile reziduale rămase de la funcționalități. Pentrru mai multe detalii vezi [Part RefineShape](Part_RefineShape.md) .

-    **Sections**: listează secțiunile folosite.

-    **Spine Tangent**: true sau false (valoare implicit). True extinde traiectoria pentru a include muchiile tangente.

-    **Auxiliary Spine Tangent**: true sau false (valorea implită) True extinde traictoria auxiliară pentru include muchiile tangente.

-    **Auxiliary Curvelinear**: true saur false (valoarea implicită). True calculează normala între punctele echididstent la ambele dorsale/curbe.

-    **Mode**: profile mode. See [Options](#Options.md).

-    **Binormal**: binormal vector for corresponding orientation mode.

-    **Transition**: transition mode. Options are *Transformed*, *Right Corner* or *Round Corner*.

-    **Transformation**: *Constant* folosește o singură secțiune transversală . *Multisection* folosește două sau mai multe secțiuni tansversale. *Linear*, *S-shape* și *Interpolation* nu sunt funcționale în acest moment.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Schițele utilizate pentru secțiuni transversale trebuie să formeze profile închise.
-   Nu este posibil să se utilizeze un singur vertex ca secțiune transversală.
-   O secțiune transversală nu poate fi așezată pe același plan ca cea precedentă.
-   Pentru un mai bun control al formei țevii, este recomandat ca toate secțiunile transversale să aibă același număr de segmente. De exemplu, pentru țeavă între un dreptunghi și un cerc, cercul poate fi spart în 4 arce de cerc interconectate.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePipe/ro
