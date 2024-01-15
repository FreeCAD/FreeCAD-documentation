# Manual:Parametric objects/ro
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}

FreeCAD este proiectat pentru modelare parametrică. Aceasta înseamnă că geometria pe care o creați, în loc să fie construibilă liber, este produsă prin reguli și parametri. De exemplu, un cilindru ar putea fi produs dintr-o rază și o înălțime. Cu ajutorul acestor doi parametri, programul dispune de suficiente informații pentru a construi cilindrul.

Obiectele parametrice, în FreeCAD, sunt în realitate bucăți mici dintr-un program care rulează ori de câte ori unul dintre parametri s-a schimbat. Obiectele pot avea mai multe tipuri diferite de parametri: numere (numere întregi cum ar fi 1, 2, 3 sau valori în virgulă mobilă cum ar fi 3.1416), dimensiuni în lumea reală (1mm, 2.4m, 4.5ft), coordonate (x,y,z), un șir de caractere (\"hello!\") sau chiar alte obiecte.

Acest ultim tip permite construirea rapidă a unor lanțuri de operații complexe, fiecare obiect nou fiind bazat pe unul precedent și adăugând noi funcționalități/caracteristici.

În exemplul de mai jos, un obiect paralelipipedic solid (Pad) se bazează pe o formă 2D dreptunghiulară (Sketch) și o distanță de extrudare. Cu aceste două proprietăți, aceasta produce o formă solidă prin extrudarea formei de bază pe distanța dată. Apoi puteți folosi acest obiect ca bază pentru operații ulterioare, cum ar fi desenarea unei noi forme 2D pe una dintre fațetele sale (Sketch001) și apoi efectuarea unei extrageri/scăderi (Pocket) până când ajungeți la obiectul final.

Toate operațiunile intermediare (formele 2D, pad-uri, buzunare, etc) sunt încă acolo și puteți schimba oricare dintre parametrii lor oricând. Întregul lanț va fi reconstruit ori de câte ori este necesar.

![](images/Parametric_objects.jpg )

Două lucruri importante sunt necesare pentru a ști:


<div class="mw-translate-fuzzy">

1.  Recalcualrea nu este întotdeauna automată. Operațiile dificile, care pot modifica o mare parte a documentului dvs. și, prin urmare, necesită ceva timp, nu sunt efectuate automat. În schimb, obiectul (și toate obiectele care depind de el) vor fi marcate pentru recalculare (pe afișarea arborescentă va apărea o iconiță albastră mică). Apoi trebuie să apăsați butonul de recalculare (or **Edit->Refresh**) pentru a avea recalcularea tuturor obiectelor marcate.




1.  The dependency tree must always flow in the same direction. Loops are forbidden. ([See DAG](Glossary#Directed_Acyclic_Graph.md)) Puteți avea obiectul A care depinde de obiectul B care depinde de obiectul C. Dar că nu puteți avea un obiect A care depinde de obiectul B care depinde de obiectul A. Aceasta ar fi o dependență circulară. Cu toate acestea, puteți avea mai multe obiecte care depind de același obiect, de exemplu, obiectele B și C depind de A. Meniu**Tools -> Dependency graph** vă arată o diagrama de dependență ca în imaginea de mai sus. Poate fi utilă detectarea problemelor.


</div>

Nu toate obiectele sunt parametrice în FreeCAD. De multe ori, geometria pe care o importați din alte fișiere nu va conține niciun parametru și va fi un obiect simplu, neparametric. Totuși, acestea pot fi adesea folosite ca bază sau punct de plecare pentru obiectele parametrice nou create, în funcție, desigur, de ceea ce necesită obiectul parametric și de calitatea geometriei importate.

Cu toate acestea, toate obiectele, parametrice sau nu, vor avea câțiva dintre parametrii de bază, cum ar fi un nume, care este unic în document și nu poate fi editat, o etichetă, care este un nume definit de utilizator care poate fi editat și un amplasament [placement](placement.md), care definește păstrează poziția sa în spațiul 3D.

În cele din urmă, trebuie remarcat faptul că obiectele parametrice personalizate sunt [easy to program in python](Scripted_objects.md).

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
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/ro
