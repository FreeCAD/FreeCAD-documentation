---
- GuiCommand:/cs   Name:Constraint EqualLength   Name/cs:Constraint EqualLength   Workbenches:[PartDesign](Sketcher_Workbench/cs___Sketcher]],_[[PartDesign_Workbench/cs.md)|MenuLocation:Sketch → Sketcher constraints → Constrain equal   Shortcut:E   SeeAlso:[Constraint Radius](Constraint_Radius/cs.md)---


</div>


<div class="mw-translate-fuzzy">

#### Popis

Vazba Shodné zajistí, že dva nebo více přímkových segmentů v přímce, lomené čáře nebo obdélníku budou mít stejnou délku. Je-li aplikováno na úhel nebo kružnici, jsou úhly nastaveny na stejnou velikost. Vazba nemůže být použita na základní konstrukce, které nejsou stejného typu (např. na segment přímky a úhel).


</div>

The Constrain Equal constraint forces two or more line segments in a line, poly-line or rectangle to have equal length. If applied to arcs or circles the radii are constrained to be equal. It cannot be applied to geometry primitives which are not of the same type (e.g. line segments and arcs).


<div class="mw-translate-fuzzy">

#### Použití

Zde uvedený náčrt obsahuje několik nakreslených základních prvků (přímka, lomená čára, obdélník, úhel a kružnice).
<img alt="" src=images/EqualConstraint1.png  style="width:256px;">
Vyberte dva nebo více segmentů (např. přímka a jedna strana obdélníka).
<img alt="" src=images/EqualConstraint2.png  style="width:256px;">
Klikněte na ikonu Shodné (EqualLength) <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> v pruhu nástrojů kreslení (na náčrtové pracovní ploše nebo ploše pro Díl) nebo vyberte položku menu Vazba Shodné ze submenu Náčrty Vazba v hlavním menu Náčrtové pracovní plochy nebo plochy Díl, podle toho ve které pracovní ploše jste. Tím aplikujete tuto vazbu na vybrané položky.
<img alt="" src=images/EqualConstraint3.png  style="width:256px;">
Teď na náčrtu vyberte úhel a kružnici.
<img alt="" src=images/EqualConstraint4.png  style="width:256px;">
a aplikujte vazbu Shodné (Equal)<img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> jako předtím.
<img alt="" src=images/EqualConstraint5.png  style="width:256px;">
Teď vyberte přímkový segment, všechny segmenty lomené čáry a jednu ze zbývajících neupravených stran obdélníka
<img alt="" src=images/EqualConstraint6.png  style="width:256px;">
a aplikujte vazbu Shodné (Equal) <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> jako předtím.
<img alt="" src=images/EqualConstraint7.png  style="width:256px;">
Vyberet přímkový segment a úhel
<img alt="" src=images/EqualConstraint8.png  style="width:256px;">
a aplikujte vazbu Shodné (Equal) <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> jako předtím. Vyskakovací okénko zobrazí zprávu, která indikuje, že vybrané položky musejí být stejného konstrukčního typu (přímky s nulovým úhlem nebo přímky s nenulovým úhlem).
<img alt="" src=images/EqualConstraint9.png  style="width:256px;">


</div>

The example sketch below contains a number of sketch primitives (line, poly-line, rectangle, arc and circle).

![](images/EqualConstraint1.png )

Select two or more line segments (e.g. line and one side of the rectangle).

![](images/EqualConstraint2.png )

Click on **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** in the Sketcher toolbar (in either the Sketcher or Part Design workbenches) or select the Constrain Equal menu item from the Sketcher constraints sub menu item in either the Sketch or Part Design menu item depending upon which workbench is selected (Sketcher or Part Design) to apply the constraint to the selected items.

![](images/EqualConstraint3.png )

Now select the arc and the circle in the sketch.

![](images/EqualConstraint4.png )

and apply **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint5.png )

Now select the line segment, all segments of the poly-line and one of the remaining unconstrained sides of the rectangle

![](images/EqualConstraint6.png )

and apply **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint7.png )

Select the line segment and the arc

![](images/EqualConstraint8.png )

and apply **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before. A pop-up message indicates that the constrained items have to be of the same geometrical type (lines of zero curvature or lines of non-zero curvature).

![](images/EqualConstraint9.png )

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1` and `Edge2` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}  
