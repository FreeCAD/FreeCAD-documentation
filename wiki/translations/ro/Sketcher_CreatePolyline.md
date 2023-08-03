# Sketcher CreatePolyline/ro
---
 GuiCommand:   Name: Sketcher CreatePolyline   Name/ro: Sketcher CreatePolyline   Workbenches: Sketcher Workbench/ro   Sketcher---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Această unealtă funcționează ca un instrument [Sketcher CreateLine](Sketcher_CreateLine/ro.md), dar crează linii și arce de cerc conectate prin vârfuri/vertex-uri. Când pornește instrumentul, indicatorul mouse se modifică într-o cruce albă și o iconiță roșie tip polilinie. coordonatele indicatorului sunt afișate alături în albastru și în timp real.


</div>

![](images/Sketcher_PolylineExample1.png )


<div class="mw-translate-fuzzy">

*Polyline începe cu o linie, un arc de cerc tangent, un arc de cerc perpendicular și apoi cu o linie tangentă*


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

Polilinia începe întotdeauna cu un segment de linie dreaptă: faceți clic pe - mutați clic pe mouse. Mutați mouse-ul din nou. După plasarea segmentului de primă linie, instrumentul de polilinie Sketcher are mai multe moduri care pot fi comutate cu tasta **M**. De exemplu, puteți desena arce tangente sau perpendiculare după o linie sau un segment de arc. Apăsarea repetată a tastei {{KEY | M}} comută prin aceste moduri diferite:

1.  Apăsați tasta **M** : noul segment este o linie perpendiculară cu segmentul precedent.
2.  Apăsați încă o dată tasta**M** : noul segment este o linie care este tangențială la segmentul precedent.
3.  Apăsați a treia oară taswta **M**: noul segment este un arc de cerc care este tangențial la segmentul precedent.
4.  Apăsați a patra oară tasta **M** : noul segment este un arc de cerc care este perpendicular (stânga) la segmentul precedent.
5.  Apăsați a cincea oară tasta **M**: noul segment este un arc care este perpendicular (dreapta) la

segmentul precedent.

1.  Apăsați a șasea oară tasta **M**: Reveniți în starea în care ați început; linia este conectată doar cu o conexiune la segmentul anterior.


<div class="mw-translate-fuzzy">

-   v0.18 and above While in any of the arc modes, holding down the **Ctrl** key (MacOS: **CMD** key) iar mișcarea cursorului determină apăsarea arcului în trepte de 45 de grade față de segmentul de polilinie creat anterior.
-   Selectați o zonă goală a vizualizării 3D sau pe un obiect existent (constrângerile automate trebuie să fie active în TaskView).
-   Apăsați tasta **Esc** sau clic butonul dreapta al mouse-ului *before* de închiderea poliliniei într-o buclă închide lpolilina curentă și puteți continua cu una nouă.
-   Apăsați tasta **Esc** sau click pe butonul drepta al mouse-ului din nou finalizează funcția polilinie.
-   Apăsând tasta **Esc** sau făcând click butonul dreapta *after* închiderea poliliniei într-o buclă închide funcția polilinie.


</div>





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/ro
