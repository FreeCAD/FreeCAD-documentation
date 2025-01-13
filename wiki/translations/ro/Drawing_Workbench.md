# Drawing Workbench/ro
**The '''Drawing Workbench''' is no longer included after version 0.20.<br>
The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.**

<img alt="Drawing workbench icon" src=images/Workbench_Drawing.svg  style="width:128px;">



## Introducere

Modulul de desenare vă permite să puneți lucrul 3D pe hârtie. Adică, pentru a afișa vizualizările modelelor dvs. într-o fereastră 2D și pentru a insera acea fereastră într-un desen, de exemplu o foaie cu graniță, un titlu și logo-ul dvs. și, în final, să tipăriți această foaie.




<img alt="" src=images/Drawing_extraction.png  style="width:600px;">



## Instrumente

Unelte pentru crearea, configurarea si exportul foilor de desen 2D

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Deschide imagine vectoriala scalabila - SVG](Drawing_Open_SVG/ro.md): Deschide o foaie de desen salvata anterior ca si fisier SVG

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Desen nou A3 peisaj](Drawing_Landscape_A3/ro.md): Creaza o noua foaie de desen din sablonul implicit FreeCAD

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Inserare vizualizare](Drawing_View/ro.md): Insereaza o vizualizare a obiectelor selectate in foaia din desenul activ

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotation](Drawing_Annotation.md): Adaugă o adnotare în foaia de desen curent

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip.md): Adaugă un grup de clipuri în foaia de desen curent

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open Browser](Drawing_Openbrowser.md): Deschide o previzualizare a foii curente din browser

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews.md): Creează automat vederi ortografice ale unui obiect

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md): Adaugă conținutul unui fișier SVG ca simbol în foaie de desen curentă

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing.md): Inserează o vizualizare specială a unui obiect selectat în foaia de desen curent

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView.md): Inserts a view of a selected spreadsheet in the current drawing sheet

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Salveaza foaie](Drawing_Save/ro.md): Salveaza foaia curenta ca si fisier SVG

-   [Project Shape](Drawing_ProjectShape.md): Creează o proiecție a obiectului selectat (Sursă) în vizualizarea 3D.

-   Notă **Note:**

Instrumentul [Draft View](Draft_Drawing.md) este utilizat în special pentru a plasa obiecte 2D Draft pe hârtie. Acesta are câteva capabilități adiționale și suportă obiecte specifice ca de ex: [Draft dimensions](Draft_Dimension.md).

## Flux de lucru 

Documentul conține un obiect 3D (Schenkel) din care dorim să realizăm un desen. Prin urmare, este creată o \"pagină\". O pagină este instanțiată dintr-un șablon, de exemplu șablonul \"A3_Landscape\". Șablonul este un document [SVG](SVG.md) care poate conține un cadru de pagină, un logo și alte elemente.

În această pagină putem introduce una sau mai multe vizualizări. Fiecare vizualizare are o poziție pe pagină (Proprietăți X, Y), un factor de scară (Scala proprietății) și proprietăți suplimentare. De fiecare dată când pagina sau vizualizarea sau obiectul referință se modifică, pagina este regenerată și actualizarea paginii este actualizată.



## Scrip-Programare 

În prezent, fluxul de lucru al interfeței grafice cu utilizatorul este foarte limitat, astfel încât API-ul de scripting este mai interesant.

Consultați pagina [Drawing API example](Drawing_API_example.md) pentru o descriere a funcțiilor utilizate pentru a crea pagini de desen și vizualizări.



## Extensii la Atelierul de Desen 3D 

Unele note despre partea de programare a modulului de desen vor fi adăugate la pagina [Drawing Documentation](Drawing_Documentation.md) . Acest lucru va ajuta să intelegeți rapid modul în care funcționează modulul de desen, permițând programatorilor sa înceapă rapid programarea pentru aceasta.

## External links 


<div class="mw-translate-fuzzy">

## legături Externe 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)


</div>





{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/ro
