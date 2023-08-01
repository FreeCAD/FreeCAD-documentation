# Path Helix/ro
---
- GuiCommand:   Name: Path Helix   Workbenches: [[Path Workbench   Path]]|MenuLocation: Path - Helix   Shortcut:    SeeAlso: ---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Comanda Helix a adăugat o operație de interpolare elicoidală la lucrare. Mișcarea orară de interpolare Helix de interpolare (G2) în Comenzile G-Code. Comenzile codului G de ieșire în sens antiorar (G3). Procentul de trepte specifică trecerea concentrică ca procent din diametrul sculei.


</div>

## Usage


<div class="mw-translate-fuzzy">

-   Selectați instrumentul Helix din Path-\>menu sau butonul GUI și apăsați.
-   Alegeți un controler de instrument din fereastra de selecție pop-up(contextuală) și confirmați apăsând OK.
-   Toate găurile disponibile din modelul de lucrări vor fi disponibile pentru procesare, listate în fila Geometrie de bază. Confirmați că lista corespunde găurilor destinate procesării și ajustați adăugarea, activarea sau dezactivarea, după cum este necesar. Găurile pot fi adăugate prin selectarea fețelor de perete ale găurilor.
-   Asigurați-vă că adâncimile, adâncimea finală sunt corecte și ajustați dacă nu.
-   Asigurați-vă că înălțimile, înălțimile de siguranță și înălțimea sunt corecte și ajustați dacă nu.
-   În tab-ul Operare, specificați Start From, Direcția, și procentajul de Step Over.


</div>

## Options

Extra Offset adds a margin of material to be left unmachined. This is typically to allow a light finishing pass as a separate operation.

## Comments

-   Step Down is not respected exactly. It is always rounded to give a complete number of turns from Start Depth to Final Depth.
-   Similarly Step Over is not respected exactly. It is always rounded to give a number of equal steps.

The feedrate parameter is constant across all cuts and is based on the position of the tool\'s axis, thus actual feedrate of the cutting edge of the tool can vary considerably between the inner most cut and the outside surface. If the job dimensions produce a path diameter smaller than the tool diameter, this can lead to much faster cutting speeds than the feedrate given for the tool in the tool controller. This may need to considered when selecting \"feed and speeds\" for the job.

## Properties

### Data

Empty

### View

Empty

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Helix/ro
