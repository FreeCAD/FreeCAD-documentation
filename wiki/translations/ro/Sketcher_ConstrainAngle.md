---
- GuiCommand:
   Name: Constraint InternalAngle
   Workbenches: Sketcher Workbench
   Shortcut: A
   MenuLocation: Sketch -> Sketcher constraints -> Constrain angle
   SeeAlso: Sketcher ConstrainDistance, Sketcher ConstrainPerpendicular
---

# Sketcher ConstrainAngle/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Constrângerea de unghi este o [datum constraint](Sketcher_Workbench#Sketcher_Constraints.md) având ca scop fixarea unghiurilor unei schițe. Este capabilă să definească pantele liniilor individuale, unghiurile dintre linii, unghiurile de intersecții ale curbelor și deschiderile unghiulare ale arcurilor circulare.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 

Sunt patru căi diferite pentru ca această constrângere să fie aplicată:

1.  Liniilor individuale
2.  între linii
3.  asupra interesecțiilor curbelor
4.  Arcurilor de cercuri


</div>

There are four different ways the constraint can be applied:

-   to individual lines
-   between lines
-   to intersections of curves
-   to arcs of circles


<div class="mw-translate-fuzzy">

Pentru a aplica constrângerea de unghi, trebuie urmați următorii pași:

-   Selectați una, două sau trei entități în schiță. Modul va fi ales în funcție de selecție.
-   Invocați constrângerea făcând clic pe pictograma de pe bara de instrumente sau selectând elementul din meniu sau utilizând comanda rapidă de la tastatură. Se afișează o fereastră de dialog contextual pentru editarea referinței.
-   Modificați unghiul, dacă este necesar. Unghiul poate fi introdus ca o expresie care va fi evaluată și rezultatul va fi stocat. Faceți clic pe OK.


</div>

Ca și în cazul oricărei constrângeri de referință, este posibil să modificați unghiul prin lista constrângerilor. Introducerea unei valori negative va determina unghiul să se răstoarne.




<div class="mw-translate-fuzzy">

## Moduri de Constrângere 

### linie pantă unghi 

**Accepted selection:** linie


</div>

### Line slope angle 

**Accepted selection:** line

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:600px;">

Constrângerea stabilește unghiul polar al direcției liniei. Este unghiul dintre linie și axa X a schiței.

### Span of a circular arc 


<div class="mw-translate-fuzzy">

### arc span (v0.15) 

**Accepted selection:** arc de cerc


</div>

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:600px;">

In acest mod, constrângerea fixată unghiulară a unui arc circular.

### Between lines 


<div class="mw-translate-fuzzy">

### between lines 

**Accepted selection:** line + line


</div>

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:600px;">

În acest mod, constrângerea stabilește unghiul dintre două linii. Nu este necesar ca liniile să se intersecteze.

### Between curves at intersection (angle-via-point) 


<div class="mw-translate-fuzzy">

### între curve la interseția (angle-via-point) (v0.15) 

**Accepted selection:** any line/curve + any line/curve + any point


</div>

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:600px;">

În acest mod, unghiul dintre două curbe este limitat la punctul de intersecție. Punctul de intersecție poate fi pe extensiile curbelor. Punctul trebuie specificat explicit, deoarece curbele se intersectează de obicei în mai multe puncte.


<div class="mw-translate-fuzzy">

Pentru ca constrângerea să funcționeze corect, punctul trebuie să fie pe ambele curbe. Deci, constrângerea este invocată, punctul va fi automat constrâns([helper constraints](Sketcher_helper_constraint.md) va fi adăugat dacă este necesar), și unghiul dintre curbe va fi constrâns la acest punct. Aceste [helper constraints](Sketcher_helper_constraint.md) sunt constrângeri pur și simplu. Ele pot fi adăugate manual sau șterse. Nu există constrângeri de ajutor pe imaginea de mai sus, deoarece punctul selectat este deja intersecția curbelor.


</div>



## Script


<div class="mw-translate-fuzzy">

Constrângerea Unghiulară poate fi creată cu [macros](macros.md) și de la consola Python console utilizând următoarele:


</div>


```python
# line slope angle
Sketch.addConstraint(Sketcher.Constraint('Angle',iline,angle))

# angular span of arc
Sketch.addConstraint(Sketcher.Constraint('Angle',iarc,angle))

# angle between lines
Sketch.addConstraint(Sketcher.Constraint('Angle',iline1,pointpos1,iline2,pointpos2,angle))

# angle-via-point (no helper constraints are added automatically when from python)
Sketch.addConstraint(Sketcher.Constraint('AngleViaPoint',icurve1,icurve2,geoidpoint,pointpos,angle))
```


<div class="mw-translate-fuzzy">

unde:

  - Sketch este un obiect tip schiță

  - iline, iline1, iline2 sunt numere întregi specificând liniile printr-un număr ordinal in Sketch.

  - pointpos1, pointpos2 should be 1 for start point and 2 for end point. The choice of endpoints allows to set internal angle (or external), and it affects how the constraint is drawn on the screen.

  - geoidpoint and pointpos in AngleViaPoint are the indexes specifying the point of intersection.

  - angle este valoarea unghiului în radiani. Unghiul este contorizat între vectorii tangenți în sens antiorar. Vectorii tangenți indică de la început până la capăt liniile (sau invers, dacă punctul final este indicat liniar) și în sens antiorar pentru cercuri, arce și elipse. Cantitatea este, de asemenea, acceptată ca un unghi (de exempluApp.Units.Quantity('45 deg'))


</div>

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/ro
