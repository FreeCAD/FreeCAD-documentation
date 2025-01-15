---
 TutorialInfo:o
   Topic:  Modeling an architectural panel
   Level:  Beginner
   Time:  60 minutes
   Author:  Yorik
   FCVersion: 
   Files: 
---

# Arch panel tutorial/ro





Acesta este un cross-post(duplicat) al tutorialului [1](http://opensourceecology.org/wiki/FreeCAD_Architecture_Tutorial) inițial scris pentru [Open-Source Ecology](http://opensourceecology.org).



## Prezentarea FreeCAD 

<img alt="" src=images/Arch_panel_tutorial_01.jpg  style="width:800px;">

FreeCAD este un modelator 3D parametric. Modelarea parametrică vă permite să vă modificați designul, revenind în istoricul modelului dvs. și să schimbați parametrii săi. FreeCAD este un software open source (LGPL license) și foarte modular, permițând o extindere și o personalizare foarte avansate, mulțumită utilizării intensive a limbajului de script-programare Python.


<div class="mw-translate-fuzzy">

-   FreeCAD website: <http://www.freecadweb.org/>
-   FreeCAD documentation wiki: <http://www.freecadweb.org/wiki/index.php?title=Main_Page>
-   FreeCAD workbenches: <http://www.freecadweb.org/wiki/index.php?title=Workbench_Concept>
-   FreeCAD forum: <http://forum.freecadweb.org/>
-   Getting started with FreeCAD: <http://www.freecadweb.org/wiki/index.php?title=Getting_started>
-   Architecture tutorial: <http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial>


</div>



## Instalarea FreeCAD 

Aveți posibilitatea de a instala cea mai recentă versiune stabilă (de astăzi, mai 2015: versiunea 0.15) sau o versiune de dezvoltare (în prezent 0.16). De fapt, versiunile de dezvoltare ale FreeCAD sunt, de obicei, destul de stabile și sunteți puternic încurajați să încercați o versiune de dezvoltare, cu excepția cazului în care aveți un anumit motiv să nu faceți acest lucru. Deoarece dezvoltarea FreeCAD este destul de rapidă, asigurați-vă că, dacă îl descărcați manual, verificați din când în când și reinstalați / actualizați pentru a beneficia de ultimele îmbunătățiri.

-   Pe Windows: Descărcați cea mai recentă versiune pentru versiunea Windows (32 sau 64 de biți) de la <https://github.com/FreeCAD/FreeCAD/releases>. Faceți dublu clic pe fișierul de instalat.
-   Pe Mac OS: Descărcați cea mai recentă versiune de la <https://github.com/FreeCAD/FreeCAD/releases>. Faceți dublu clic pe fișierul de instalat.
-   Pe Ubuntu: Versiunea FreeCAD furnizată de Ubuntu este de obicei depășită, deci vă recomandăm să utilizați în schimb PPA menținut de comunitatea FreeCAD. Pentru a instala, deschideți aplicația \"Sursa de software\" a Ubuntu și adăugați ppa: freecad-maintainers / freecad-stable pentru versiunea stabilă sau ppa: freecad-maintainers / freecad-daily pentru versiunea de dezvoltare pentru sursele software.
-   Pe alte platforme: În majoritatea distribuțiilor mainstream Linux (Debian, Fedora, etc), FreeCAD este inclus în depozitele oficiale de software. S-ar putea să nu fie totuși cea mai actualizată versiune. Dacă versiunea de care aveți nevoie nu este disponibilă, singura opțiune este să compilați gratuit FreeCAD (instrucțiuni de pe site-ul FreeCAD)



## Conținut opțional Adițional 

-   Activarea importului / exportului IFC: Pentru a importa și a exporta proiecte în / din formatul fișierului IFC, FreeCAD se bazează pe importatorul IfcOpenShell, pe care trebuie să îl instalați separat de la <http://ifcopenshell.org/python.html>. Asigurați-vă că alegeți o versiune bazată pe python2.7, aceeași versiune Python folosită de FreeCAD.
-   Baza de lucru pentru dimensionarea desenelor: Un Atelier de lucru suplimentar pentru FreeCAD, care oferă multe instrumente convenabile pentru a adăuga dimensiuni și adnotări la foile de desen 2D ale FreeCAD: <https://github.com/hamish2014/FreeCAD_drawing_dimensioning> (Instalați instrucțiunile de pe pagina web)
-   Workbench Assembly2: Un Atelier de lucru suplimentar pentru FreeCAD, care oferă o serie de instrumente de asamblare de bază: <https://github.com/hamish2014/FreeCAD_assembly2> (Instalați instrucțiuni de pe pagina web)



## Sfaturi pentru startup rapid 

Colecția de tutoriale disponibile pe wiki-ul FreeCAD este încă foarte redusă. Cu toate acestea, mulți membri ai comunității FreeCAD folosesc youtube pentru a publica tutoriale video. Asigurați-vă că ați căutat conținut FreeCAD pe YouTube, care este cu siguranță cea mai bună sursă de materiale de învățare.

FreeCAD este o aplicație foarte tehnică, iar curba de învățare poate fi abruptă. Asigurați-vă că vă bazați pe tutoriale, documentația wiki și nu ezitați să adresați întrebări pe forum dacă întâlniți o problemă specifică. Întrebările care sunt clar enunțate primesc de obicei răspunsuri rapide și extinse.



### O listă foarte aproximativă de lucruri pe care trebuie să le știi 

-   Interfața FreeCAD este împărțită în aateliere de lucru. Aatelierele de lucru reprezintă pur și simplu colecții de instrumente (butoane și meniuri din bara de instrumente) care sunt grupate împreună, de obicei pentru o anumită sarcină. Când treceți la un atelier la un alt atelier, interfața vă arată instrumentele de pe acel banc de lucru. Dar conținutul documentului dvs. 3D nu se modifică. Încă lucrați la același document și la aceleași obiecte.

-   FreeCAD este încă în curs de dezvoltare, există încă multe bug-uri, iar aplicația se poate bloca uneori. Salvați frecvent și activați fișierele de rezervă din Modificați → Preferințe → Document

-   Majoritatea obiectelor din FreeCAD sunt parametrice. Înseamnă că geometria lor este creată automat dintr-o serie de parametri. Acești parametri sunt întotdeauna editabili în vizualizarea Proprietăți. Ele sunt întotdeauna divizate între parametrii care afectează geometria însăși (fila Date) și parametrii care afectează numai afișarea obiectului (fila Vizualizare). Cu toate acestea, obiectele create cu alte aplicații și importate în FreeCAD nu vor fi de obicei definite de parametri și, prin urmare, nu pot fi modificate.

-   Câteva ateliere de lucru (PartDesign și Arch) sunt create pentru a lucra numai cu obiecte solide și vor refuza să lucreze pe obiecte care nu sunt solide. O regulă bună este ca întotdeauna să încercați să lucrați cu obiecte solide.

-   Deși FreeCAD poate importa și lucra cu obiecte tip plasă (mesh workbench), este proiectat în primul rând pentru a lucra cu un tip de obiect mai avansat, denumit "brep", utilizat de majoritatea atelierelor de lucru (Part, PartDesign, Draft, Sketcher, Arch). Când importați fișiere bazate pe fișiere (.dae, .orb, .stl \...), va trebui de obicei să transformați aceste obiecte în brep, înainte de a putea face ceva interesant cu ele. Formatele de fișier pe bază de solide (.step, .iges), atunci când sunt importate în FreeCAD, produc direct obiecte brep. Formatele 2D (.dxf, .svg) produc, de asemenea, conținut brep.


<div class="mw-translate-fuzzy">

-   FreeCAD are căi diferite, sau modalități, pentru a folosi butoanele mouse-ului. Aceste moduri pot fi setate în preferințe sau în modificările efectuate, făcând clic dreapta pe fundalul vizualizării 3D. Acestea sunt descrise pe <http://www.freecadweb.org/wiki/index.php?title=Mouse_Model>. Cele mai potrivite moduri pentru lucrul în FreeCAD sunt CAD sau gesturi.


</div>



## Exercițiu: modelarea unui panou de acoperiș 

Pentru a prezenta un flux de lucru tipic în FreeCAD, să modelăm un panou de acoperiș așa cum este descris în <http://opensourceecology.org/wiki/MicroHouse_4_Roof_-_Module_-_Build_Instructions>. Pentru a face acest lucru, vom începe să desenăm diferitele piese într-o schiță cu constrângeri 2D, apoi vom profita de obiectul special Window, care este capabil să construiască obiecte 3D complexe dintr-o schiță 2D care conține conturul mai multor piese. În cele din urmă, din moment ce ceea ce avem nevoie nu este o fereastră, ci un panou de acoperiș, vom transforma pur și simplu obiectul ferestrei în alt tip Arch.

### 1. Open FreeCAD, then set your preferred units to "imperial" 

In meniul Edit → Preferences → General → Units

### 2. Switch to the sketcher workbench and create a new sketch in the XY plane. 

![](images/Arch_panel_tutorial_02.jpg )

Usually, unless there is a specific reason not to do so,you\'ll always want to start drawing your 2D sketches on the ground plane, around the (0,0) origin point. Then, it is the 3D object generated from that, that will be moved/rotated into position.

### 3. Draw two rectangles. On each of them, place a vertical constraint of 16 ft and an horizontal constraint of 2 in. 

![](images/Arch_panel_tutorial_03.jpg )

Don\'t worry about the dimensions your pieces have when you draw them, the constraints will resize them accordingly. To add a dimension constraint (vertical or horizontal), you can either select a line, or two points (with CTRL pressed).

### 4. Once your two rectangles have the correct size, place a vertical constraint of 0 in between their corner points, and a horizontal constraint of 4 ft. 

![](images/Arch_panel_tutorial_04.jpg )

This ensures that our two rectangles are correctly positioned in relation to each other.

### 5. Add the two additional 2 in x 6 in pieces 

![](images/Arch_panel_tutorial_05.jpg )

Add two more rectangles and repeat the process. Note that in the example above, we didn\'t specify the length of these pieces, but rather placed a distance constraint between their extremities and the long vertical pieces, and we let a small gap of 0.05 inches between them. This is because if we make the rectangles touch each other, FreeCAD might deduce the loops wrongly, and we might get strange results with the Arch window tool. This little trick ensures that each rectangle will be recognized as an independent loop by the Arch window tool.

### 6. Add the corner reinforcement pieces 

![](images/Arch_panel_tutorial_06.jpg )

Same thing. Make them 6 inches wide, and separated them from other rectangles by 0.05 inches.

### 7. Draw 7 intermediary reinforcement pieces, set their width to 2 inches, and constrain their left and right endpoints at 0.05 inches of the vertical rectangles (or at 0 inch of the endpoints of the other horizontal rectangles) 

![](images/Arch_panel_tutorial_07.jpg )

Depending on your system, FreeCAD might begin to be slow to process new constraints. This is the disadvantage of using constrained objects, they quickly swallow up a lot of system resources. You must always consider if you absolutely need them. You can also delete constraints when they have done their job. These dimensions won\'t be fixed anymore, but unless you move the pieces around, they won\'t change. If needed, you can also always re-add constraints later.

### 8. Calculate the spacing between the 7 reinforcement pieces and set vertical constraints between them. 

In our case, our total length is 192 inches, minus the two end pieces (2 x 2 inches) and the two corner reinforcements (2 x 6 inches), = 192 -- (4 + 12) = 176. Removing the 7 reinforcement pieces ( 7 x 2 ) = 162. Dividing this by 8 gives us the space between each reinforcement: 20.25.

![](images/Arch_panel_tutorial_08.jpg )

### 9. Obtaining a fully constrained sketcher 

On the right panel (Tasks tab in the Combo View -\> Solver messages), you can see the message "\... 2 degrees of freedom". This means that our sketch is not fully constrained (it still has two "ways" of being deformed). This is because, although no piece of it can now move in relation to the others, the whole sketch can still move vertically and horizontally. To prevent this, we can simply take one of its corner points, select the origin point of the grid (where the green and red axes intersect) and press the Point Constraint button. This turns our sketch green, meaning it is fully constrained, no part of it can move anymore.

![](images/Arch_panel_tutorial_09.jpg )

This is actually not absolutely necessary. But it is always better to keep track of the exact position of objects (we are now certain that our corner is at the (0,0) point). In case something goes wrong later, or we need to figure out the position of an object built upon this sketch, this will be useful.

We can now press the "close" button and our base sketch is built:

![](images/Arch_panel_tutorial_10.jpg )

### 10. Switch to the Arch workbench and, with the sketch selected, press the "window" button 

Our sketch has now vanished and one of its rectangles has been extruded slightly into a solid piece:

![](images/Arch_panel_tutorial_11.jpg )

Although this seems wrong, it is simply because the Arch Window tool has created a default piece from the biggest loop it could find in the base sketch. We will fix that soon. Also, notice take note that the sketch has not disappeared, it has simply been turned off and "swallowed" by its new parent object. You can still find it in the tree view, by expanding the window object, and turn its display on/off by pressing the SPACE key.

### 11. Edit the window components by double-clicking it in the tree view 

![](images/Arch_panel_tutorial_12.jpg )

When double-clicking the window, its base sketch becomes visible again, and we get its edit interface: At the left, a list of the loops found in the base sketch, at the right the solid pieces built on it.

Begin with removing the "Default" piece.

Then, select the first loop (Wire0). It will highlight in the 3D view. Press the "Add" button to create a new piece from it. Give it a name, make sure the correct wire is set, and give it a 6 inches extrusion. The offset should stay 0 since we want it placed "on the ground".

The "Type" value will be used to attribute materials to the window (not implemented yet), so you can currently leave to "Frame".

![](images/Arch_panel_tutorial_13.jpg )

Then press the "Create component" button. Sometimes FreeCAD fails to guess correctly the direction of the extrusion, and you must therefore edit your component and change the 6 inches value by -6 inches.

Repeat this for all the needed pieces:

![](images/Arch_panel_tutorial_14.jpg )

When closing the edit panel we obtain the object above. Note that by default, window objects are represented semi-transparent. Since this will actually not be a window, we can just turn that off by setting its Transparency value to 0 in its View properties.

### 12. Add the cover panel 

We now have our panel frame, but not the base panel itself. To do that, the best way is to open our base sketch, and add a new rectangle. Remember though to not make any of the corners of that rectangle coincident to corners of other rectangles, in order not to confuse our window object, which might require us to redo the whole series of components if the order of the loops would change.

We can therefore constrain this new rectangle 0.05 inches inside the perimeter. This will require us to place 4 new constraints.

We can then edit our window again, and add new components. We can see that a new Wire has been found. This time, we will use it to add a 8mm polycarbonate panel (note that you can mix units without problems in FreeCAD, and write "8mm" as the thickness, even if you are working in inches). We will also give it an offset of 0.05 inches, so it is slightly offsetted from the frame, just for consistency, as all the parts of our object have that offest between them.

![](images/Arch_panel_tutorial_15.jpg )

We can now create another component based on the same Wire, in order to place another panel on top of our frame. This time, we will give it an offset of 6.05 inches. Our panel is finally complete:

![](images/Arch_panel_tutorial_16.jpg )



### 13. Comutarea ferestrei în alt tip de componentă Arch 

Acest lucru nu este cu adevărat necesar în acest moment, dar ar putea deveni important mai târziu când exportăm sau lucrăm la alte aplicații orientate spre construcții, de exemplu prin IFC, nu dorim ca panoul nostru să fie identificat ca o fereastră.

The Arch workbench of FreeCAD provides an easy way to handle that, which is that any object type can always become another, by being the base of another type. In this case, let\'s turn our window into a Panel object, simply by selecting the window and pressing the Panel tool.

![](images/Arch_panel_tutorial_17.jpg )

Notice that the color of the resulting panel has changed, that is because materials support in FreeCAD and the Arch module is still incomplete. When it is finished, this will be properly handled.



### 14. Duplicarea panourilor 

Panoul nostru poate fi apoi duplicat și copiat în mai multe moduri, de exemplu prin copiere / lipire. Dar o modalitate mai interesantă este să folosiți instrumentul Draft Clone (prezentat și în Atelierul Arch, la fel ca toate celelalte instrumente Draft). Instrumentul de clonare menține relația dintre obiectul de bază și clona, astfel încât orice modificare a obiectului de bază se va reflecta în toate clonele acestuia.

![](images/Arch_panel_tutorial_18.jpg )

În versiunea actuală de dezvoltare a FreeCAD, clonele obiectelor Arch sunt acum tot obiecte Arch.



### 15. Rotirea și poziționarea panourilor. 

În timp ce atelierul de asamblare a FreeCAD nu este încă pregătit, trebuie să ne poziționăm manual piesele, fie prin manipularea Placement proprietății de plasare, fie prin utilizarea instrumentelor Draft Move și rotire a proiectelor, care sunt de fapt modalități vizuale de modificare a plasamentului obiectelor.

Atât instrumentele Draft Rotire cât și Move utilizează sistemul de ancorare Drafting Snapping. Sunt disponibile diferite poziții de fixare (puncte finale, puncte medii, etc), care pot fi activate/dezactivate, permițând poziționarea și rotirea foarte precise.

![](images/Arch_panel_tutorial_19.jpg )

![](images/Arch_panel_tutorial_20.jpg )


 {{Draft_Tools_navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Category_Sketcher.md) > [BIM](Category_BIM.md) > [Draft](Category_Draft.md) > Arch panel tutorial/ro
