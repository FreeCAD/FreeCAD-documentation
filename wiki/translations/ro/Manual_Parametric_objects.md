# Manual:Parametric objects/ro
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD este proiectat pentru modelare parametrică. Aceasta înseamnă că geometria pe care o creați, în loc să fie construibilă liber, este produsă prin reguli și parametri. De exemplu, un cilindru ar putea fi produs dintr-o rază și o înălțime. Cu ajutorul acestor doi parametri, programul dispune de suficiente informații pentru a construi cilindrul.


</div>


<div class="mw-translate-fuzzy">

Obiectele parametrice, în FreeCAD, sunt în realitate bucăți mici dintr-un program care rulează ori de câte ori unul dintre parametri s-a schimbat. Obiectele pot avea mai multe tipuri diferite de parametri: numere (numere întregi cum ar fi 1, 2, 3 sau valori în virgulă mobilă cum ar fi 3.1416), dimensiuni în lumea reală (1mm, 2.4m, 4.5ft), coordonate (x,y,z), un șir de caractere (\"hello!\") sau chiar alte obiecte.


</div>


<div class="mw-translate-fuzzy">

În exemplul de mai jos, un obiect paralelipipedic solid (Pad) se bazează pe o formă 2D dreptunghiulară (Sketch) și o distanță de extrudare. Cu aceste două proprietăți, aceasta produce o formă solidă prin extrudarea formei de bază pe distanța dată. Apoi puteți folosi acest obiect ca bază pentru operații ulterioare, cum ar fi desenarea unei noi forme 2D pe una dintre fațetele sale (Sketch001) și apoi efectuarea unei extrageri/scăderi (Pocket) până când ajungeți la obiectul final.


</div>

![](images/FreeCAD_022_PArametricDesignPlate.png )

On the top face of the plate you sketch a circle of a given diameter d. You then use this circle to create a pocket (remove material) from the original plate.

![](images/FreeCAD_022_ParametricDesignPocket.png )

If you decide to change either of the dimensions of the plate, or of the circle, the final object would be also modified. Thanks to the use of a parametric design approach, there is no need to redo the object from the beginning.


<div class="mw-translate-fuzzy">

1.  Recalcualrea nu este întotdeauna automată. Operațiile dificile, care pot modifica o mare parte a documentului dvs. și, prin urmare, necesită ceva timp, nu sunt efectuate automat. În schimb, obiectul (și toate obiectele care depind de el) vor fi marcate pentru recalculare (pe afișarea arborescentă va apărea o iconiță albastră mică). Apoi trebuie să apăsați butonul de recalculare (or **Edit->Refresh**) pentru a avea recalcularea tuturor obiectelor marcate.




1.  The dependency tree must always flow in the same direction. Loops are forbidden. ([See DAG](Glossary#Directed_Acyclic_Graph.md)) Puteți avea obiectul A care depinde de obiectul B care depinde de obiectul C. Dar că nu puteți avea un obiect A care depinde de obiectul B care depinde de obiectul A. Aceasta ar fi o dependență circulară. Cu toate acestea, puteți avea mai multe obiecte care depind de același obiect, de exemplu, obiectele B și C depind de A. Meniu**Tools -> Dependency graph** vă arată o diagrama de dependență ca în imaginea de mai sus. Poate fi utilă detectarea problemelor.


</div>

In FreeCAD\'s parametric modeling process, examining the dependency tree of an object provides a clear insight into the sequential build and relationships within a model. At the foundation of the structure in the above example is the \'Plate Sketch,\' which serves as the base for the initial form of the model. A \'Pad\' operation is then applied, which adds material to this foundational sketch, effectively creating a three-dimensional structure from the two-dimensional base.

Following this, a \'Circle Sketch\' is drafted on the newly formed surface. This circle forms the basis for the subsequent \'Pocket\' operation. The pocket operation strategically removes material from the structure, essentially carving out a portion based on the circle sketch. This process of adding and then subtracting material allows for complex geometries and features to be integrated into the basic model seamlessly.

Through this sequence of operations---starting from the base sketch, adding volume with a pad, and creating detailed features with additional sketches and pockets---the final object takes shape. Each step in this chain depends on its predecessor, illustrating the interconnected nature of parametric design in FreeCAD.

![](images/FreeCAD_022_ParametricDesignDependGraph.png )


<div class="mw-translate-fuzzy">

Nu toate obiectele sunt parametrice în FreeCAD. De multe ori, geometria pe care o importați din alte fișiere nu va conține niciun parametru și va fi un obiect simplu, neparametric. Totuși, acestea pot fi adesea folosite ca bază sau punct de plecare pentru obiectele parametrice nou create, în funcție, desigur, de ceea ce necesită obiectul parametric și de calitatea geometriei importate.


</div>

Cu toate acestea, toate obiectele, parametrice sau nu, vor avea câțiva dintre parametrii de bază, cum ar fi un nume, care este unic în document și nu poate fi editat, o etichetă, care este un nume definit de utilizator care poate fi editat și un amplasament [placement](placement.md), care definește păstrează poziția sa în spațiul 3D.


<div class="mw-translate-fuzzy">

În cele din urmă, trebuie remarcat faptul că obiectele parametrice personalizate sunt [easy to program in python](Scripted_objects.md).


</div>

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [The properties editor](Property_editor.md)
-   [How to program parametric objects](Scripted_objects.md)
-   [Positioning objects in FreeCAD](Placement.md)
-   [Enabling the dependency graph](Std_DependencyGraph.md)


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/ro
