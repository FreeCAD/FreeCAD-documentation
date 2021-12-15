# Navigation Cube/ro
{{TOCright}}

The navigational cube control, or **navigation cube**, is a user interface graphic aid for reorienting the 3D view. By default, it is visible and resides in the upper right corner of the 3D display. If you are looking at the standard [3D view](3D_view.md), it looks like the following:

![](images/FreeCAD-v0-18-NavCube_Axonometric.png )

Cubul de navigarea este compus din următoarele piese:

-   Săgețile Direcționale
-   Cubul de Navigație principal
-   Meniul Mini-cubului


<div class="mw-translate-fuzzy">

Planarea/plasarea cursorului indicatorul mouse-ului peste o caracteristică a cubului de navigație transformă funcția în albastru; clic va reorienta vizualizarea 3D așa cum este indicat de către funcție. (Notă: De la această scriere, pointerul nu se înregistrează perfect cu unele caracteristici ale cubului de navigație. Dacă o funcție pe care încercați să o selectați nu devine albastru, mișcați mouse-ul până când găsiți un loc care face ca funcție să devină albastră.) În exemplul de mai jos, vizualizarea 3D a fost rotită printr- un [mouse gesture](Mouse_Model.md) într-o orientare \"non-standard\". Indicatorul este peste un colț (indicat de culoarea albastră); clic va reorienta vizualizarea 3D la o vizualizare axonometrică standard cu colțul care vă privește.


</div>

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

## Săgețile Direcționale 

Există șase săgeți direcționale: patru săgeți triunghiulare, unul în sus, în jos, la stânga și la dreapta; și două săgeți de rotație, una pe fiecare parte a săgeților de mai sus.


<div class="mw-translate-fuzzy">

Dacă faceți clic pe săgețile triunghiulare, rotiți vizualizarea 3D cu 45 de grade în jurul unei linii perpendiculare pe direcția săgeții. Dând clic pe săgețile curbe, rotiți vizualizarea 3D în jurul unei linii care este îndreaptă spre dvs. \<! - Notă: axele de rotație nu sunt definite în mod corespunzător; fiecare este intersecția a două planuri, dar nu-mi dau seama cum să le descriu -\>


</div>

## Main Navigation Cube 


<div class="mw-translate-fuzzy">

## Cubul de navigație principal 

Cubul principal de navigație (\"nav cub\" pentru această secțiune) urmărește orientarea obiectului real în partea principală a vederii 3D. Orice operație care reorientează vizualizarea 3D principală va reorienta și cubul nav.


</div>


<div class="mw-translate-fuzzy">

Cubul nav este, în esență, o vizualizare 3D a unui cub, cu cele trei tipuri principale de componente (fețe, muchii și colțuri) îmbunătățite, astfel încât acestea pot fi ușor selectate/"clicate" cu pointerul. Dacă faceți clic pe o anumită componentă, se va seta vizualizarea 3D pentru a avea componenta centrată și îndreptată spre dvs. Cubul nav este oarecum \"zdrobit\", ca în cazul în care caracteristica cea mai îndepărtată de dvs. a fost mai mare decât caracteristica îndreptată direct spre dvs. Acest lucru permite ca funcțiile adiacente caracteristicii cu care vă confruntați să fie văzute și, în consecință, selectate. De exemplu, într-o vedere \"normală\" a unui cub obișnuit, atunci când o fațetă este îndreptată spre dvs., puteți vedea și cele patru margini ale feței și cele patru colțuri ale feței respective. În cubul \"plutitor\", puteți vedea și trăsături care reprezintă fiecare dintre fațetele adiacente, cele patru margini care leagă colțurile fațetei din fața dvs. cu fațeta opusă și colțurile unei fațete opuse. Aceasta vă permite să selectați oricare dintre vederile standard posibile, cu excepția feței opuse și a marginilor sale (21 din 26 de vizualizări posibile):

-   Fațeta din fața dvs (does nothing, since that is the current view)
-   Cele 4 muchii ale fațetei curente
-   Cele 4 colțuri ale fațetei curente
-   Cele 4 fațete adiacente
-   Cele 4 muchii care conduc către fațete opusă
-   Cele 4 colțuri ale fațetei opuse

Nu este posibilă vizualizarea pentru:

-   Fațeta opusă privitorului
-   Muchiile fațetei opuse privitorului


</div>

For example, in a \"normal\" view of a regular cube, when one face is facing you, you can also see the four edges of that face and the four corners of that face. In the \"squashed\" nav cube, you can also see features representing each of the adjacent faces, the four edges connecting the corners of the face facing you with the opposite face, and the corners of opposite face. This allows you to select any of the possible standard views except the opposite face and its edges (21 out of 26 possible views):

-   The face facing you (does nothing, since that is the current view)
-   The four edges of the current face
-   The four corners of the current face
-   The four adjacent faces
-   The four edges leading to the opposite face
-   The four corners of the opposite face

Not possible:

-   The opposite face
-   The edges of the opposite face


<div class="mw-translate-fuzzy">

Notă: De la această scriere (v 0.18), există unele probleme privind cubul nav; nu toate caracteristicile sunt selectabile în prezent. În special, marginile nu sunt selectabile, nici cele patru colțuri ale feței cu care se învecinează imediat.


</div>

### Face Selection 


<div class="mw-translate-fuzzy">

### Selectarea Fațetei 

Dacă faceți clic pe o fațetă, orientarea 3D va fi orientată spre fațeta respectivă. Din punctul de vedere al fațetei, sunt disponibile alte puncte de selecție, după cum sa menționat mai sus. Pe fiecare margine exterioară există patru bare \"subțiri\", reprezentând cele patru fețe adiacente; făcând clic pe ele va fi selectată vizualizarea corespunzătoare fațetei adiacente. Există patru colțuri rotunde care pot fi utilizate pentru a seta vederea axonometrică corespunzătoare. Există, de asemenea, un set interior de muchii și colțuri, care sunt în prezent nefuncționale.


</div>

### Edge Selection 


<div class="mw-translate-fuzzy">

### Selecția marginilor 

Din păcate, selecția de margine este nefunțională în prezent. Încercarea de a selecta o margine va selecta fațeta care se află în spatele ei. Dacă faceți clic pe o margine, trebuie să centrați marginea astfel încât aceasta să fie îndreptată spre dvs.


</div>

### Corner Selection 


<div class="mw-translate-fuzzy">

### Selecția colțului 

Dacă faceți clic pe unul dintre colțuri, vi se va oferi o vedere axonometrică din colțul respectiv. După cum s-a menționat mai sus, în momentul în care o fațetă este îndreptată direct spre dvs., colțurile acelei fețe nu pot fi selectate.


</div>

## Meniul Mini-cub 


<div class="mw-translate-fuzzy">

În colțul din dreapta jos al cubului de navigație este un mic cub. Dacă faceți clic pe acest cub va apărea un meniu pe care îl puteți utiliza pentru a schimba tipul de vizualizare (Ortografic, Perspectivă, Isometric) și pentru a face o \"Zoom pentru a se potrivi\".


</div>

## Moving the Navigation Cube Display 


<div class="mw-translate-fuzzy">

## Deplasarea afișajului cubului de navigație 

Puteți mutați întreaga structură de control a cubului de navigație într-o altă locație din afișajul 3D, apăsând mouse-ul oriunde în cubul principal de navigare și trasând. De la această scriere (v 0.18), structura nu va începe să se miște până când indicatorul mouse-ului nu sa deplasat peste marginea cubului principal de navigație.


</div>

## Configuration

The navigation cube is configurable, including adjusting its size: **Edit → Preferences... → Display → Navigation → Navigation cube** <small>(v0.19)</small> .

For more advanced configuration, refer to the [CubeMenu](Interface_Customization#CubeMenu.md) from [external workbenches](External_workbenches.md).


<div class="mw-translate-fuzzy">


{{docnav|Mouse Model|Document structure}}


</div>




_

---
[documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/ro
