# Manual:Navigating in the 3D view/ro
{{Manual:TOC}}



### O vorbă despre spațiul 3D 


<div class="mw-translate-fuzzy">

Dacă acesta este primul dvs. contact cu o aplicație 3D, va trebui să înțelegeți mai întâi câteva concepte. Dacă nu este primul contact, puteți sări peste această secțiune.


</div>


<div class="mw-translate-fuzzy">

Spațiul FreeCAD 3D este un spațiu euclidian [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space). Este un punct de origine și trei axe: X, Y și Z. Dacă vă uitați la scena dvs. de sus, în mod convențional, axa X indică spre dreapta, axa Y spre spate și axa Z în sus. În colțul din dreapta jos al vizualizării FreeCAD, vizionați mereu scena:


</div>


<div class="mw-translate-fuzzy">

Fiecare punct al fiecărui obiect care există în acest spațiu poate fi localizat prin coordonatele sale (x, y, z). De exemplu, un punct cu coordonate (2, 3, 1), se va situa la 2 unități pe axa X, 3 unități pe axa Y și 1 unitate pe axa Z:


</div>

![](images/3dspace_coordinates.jpg )

### The FreeCAD 3D view 

#### Mouse navigation 


<div class="mw-translate-fuzzy">

Navigarea în vizualizarea 3D FreeCAD se poate face cu un mouse, cu un dispozitiv Navigator spațial, tastatură, touchpad sau o combinație a acestora. FreeCAD implementează mai multe moduri de navigare [navigation modes](http://www.freecadweb.org/wiki/index.php?title=Mouse_Model), care determină cum cele 3 operații de manipulare a vederii sunt utilizate în procesul de operare (pan, rotire și zoom). Modurile de navigare sunt accesate din ecranul Preferințe sau direct făcând clic dreapta oriunde în vizualizarea 3D:


</div>

![](images/FreeCAD_022_NavigationMethod.png )


<div class="mw-translate-fuzzy">

Fiecare dintre aceste moduri alocă diferite butoane mouse-ului sau combinații de mouse-uri sau tastaturi mouse-ul pentru aceste patru operații. Următorul tabel prezintă principalele moduri disponibile:


</div>


<div class="mw-translate-fuzzy">

++++++
| Mod                | Panoramare                                                                                                                                                                                                           | Rotație                                                                                                                                                                                                 | Zoom                                                                                                                                                                                               | Selectare                                                                                       |
+====================+======================================================================================================================================================================================================================+=========================================================================================================================================================================================================+====================================================================================================================================================================================================+=================================================================================================+
| OpenInventor       | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                              | ![Click left button mouse](images/Select-mouse.svg )                                                                                                                                  | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                             | ține CTRL + glisare ![Click left button mouse](images/Select-mouse.svg )      |
++++++
| CAD **(implicit)** | ![Click middle button mouse](images/Pan-mouse.svg ) sau ![Click right button mouse + CTRL key](images/Pan-mouse-CTRL.svg )                                         | ![Hold middle then left mouse button](images/Rotate-mouse.svg ) sau ![Click right button mouse + SHIFT key](images/Rotate-mouse-SHIFT.svg ) | ![Roll middle button mouse](images/Zoom-mouse.svg ) sau ![Click right button mouse + CTRL + SHIFT key](images/Zoom-mouse-CTRL-SHIFT.svg ) | ![Click left button mouse](images/Select-mouse.svg )                          |
++++++
| Blender            | ține SHIFT + glisare ![Click middle button mouse](images/Pan-mouse.svg ) sau glisare ![Click left + right button mouse and drag](images/Mouse_LMB%2BRMB.svg ) | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                 | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                             | ![Click left button mouse](images/Select-mouse.svg )                          |
++++++
| Touchpad           | ține SHIFT + glisare ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                            | ALT + ![Touchpad (mouse) pointer](images/Touchpad.png )                                                                                                                              | PGUP / PGDOWN                                                                                                                                                                                      | ![Click touchpad (mouse) left button](images/Select-touchpad.png ) |
++++++
| Gesture            | glisare ![Click right button mouse](images/Pan-mouse-Ctrl.svg )                                                                                                                                   | glisare ![Click left button mouse](images/Select-mouse.svg )                                                                                                                          | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                             | ![Click left button mouse](images/Select-mouse.svg )                          |
++++++
| OpenCascade        | ![Click middle button mouse](images/Pan-mouse.svg )                                                                                                                                              | ![Hold middle then right mouse button](images/Rotate-mouse-MMB+RMB.svg )                                                                                                  | ![Roll middle button mouse](images/Zoom-mouse.svg )                                                                                                                             | ![Click left button mouse](images/Select-mouse.svg )                          |
++++++


</div>

It\'s worth noting that when a user hovers over the navigation styles menu located at the bottom right of the screen, a tooltip will appear. This tooltip provides a brief description of the highlighted navigation style, offering immediate guidance on its use.

![](images/FreeCAD_022_NavigationHover.png )

#### Keyboard navigation 


<div class="mw-translate-fuzzy">

În mod alternativ, unele comenzi de la tastatură sunt întotdeauna disponibile, indiferent de modul de navigare:


</div>


<div class="mw-translate-fuzzy">

-   **CTRL +** and **CTRL -** pentru zoom in/mărire și zoom out/micșorare
-   Tastele **arrow keys** pentru a comuta vizualizarea stânga / dreapta și sus / jos
-   **SHIFT + left arrow** and **SHIFT + right arrow** pentru a roti vederea cu 90 de grade
-   tatele numerice, **1 la 6**, pentru cele șase vederi standard, de sus, din față, din dreapta, din fund, din spate și din stânga
-   **O** va seta camera în modul ortogonal,
-   iar **P** o setează în modul perspectivă.
-   **CTRL** vă va permite să selectați mai multe obiecte sau elemente


</div>


<div class="mw-translate-fuzzy">

Aceste comenzi sunt de asemenea disponibile din meniul Vizualizare și unele din bara de instrumente Vizualizare.


</div>

#### Using the Navigation Cube 

In the default setup, there is a [Navigation Cube](Navigation_Cube.md) in the upper right corner of the 3D view. This may be used to change the view.

![](images/FreeCAD_022_Cube.png )

Clicking on a face of the cube will switch the view to that face. Clicking one of the four triangular arrows rotates the view 45 degrees in the indicated direction. Clicking one of the two curved arrows rotates the view 45 degrees in the indicated direction around a line pointing towards you. Clicking the round button in the top right corner of the cube rotates the view 180 degrees around the vertical axis of the view.

There is a smaller mini-cube in the lower right of the Navigation Cube which activates a drop-down menu with several options, including an option to make the cube movable, which allows to temporarily move the cube to a different position by dragging.



### Selectarea obiectelor 


<div class="mw-translate-fuzzy">

Obiectele din vizualizarea 3D pot fi selectate făcând clic pe ele cu ajutorul butonului mouse-ului corespunzător, în funcție de modul de navigare. Un singur clic va selecta obiectul și unul dintre subcomponentele sale (margine, fațetă, vârf). Dacă faceți dublu clic, veți selecta obiectul și toate subcomponentele acestuia. Puteți selecta mai multe subcomponente sau chiar subcomponente diferite din diferite obiecte, apăsând tasta CTRL. Dacă faceți clic cu butonul de selecție pe o porțiune goală a vederii 3D, veți deselcta totul.


</div>

Poate fi activat și un panou numit \"Selection view\", disponibil din meniul Vizualizare, care vă arată ce este selectat în prezent:

![](images/Selection_view.jpg )

De asemenea, puteți utiliza Selection View pentru a selecta obiecte prin căutarea unui anumit obiect.

**De citit în plus**


<div class="mw-translate-fuzzy">

-   [The FreeCAD navigation modes](Mouse_Model.md)


</div>



---
⏵ [documentation index](../README.md) > Manual:Navigating in the 3D view/ro
