# Manual:The FreeCAD Interface/ro
{{Manual   *TOC}}


<div class="mw-translate-fuzzy">


{{Manual   *TOC/ro}}

FreeCAD utilizează [Qt framework](https   *//en.wikipedia.org/wiki/Qt_(software)) pentru a desena și administra interfața sa. Acest cadru este folosit într-o gamă largă de aplicații, astfel încât interfața FreeCAD este foarte clasică și nu prezintă dificultăți speciale în înțelegere Cele mai multe butoane sunt standard și vor fi găsite acolo unde vă așteptați(File -\> Open, Edit -\> Paste, etc). Iată aspectul FreeCAD atunci când îl deschideți pentru prima dată, imediat după instalare, afișându-vă centrul de start   *


</div>


<div class="mw-translate-fuzzy">

![](images/Freecad-interface-01.jpg )


</div>

Centrul de start este un \"ecran de întâmpinare\" convenabil, care arată informații utile pentru noii veniți, cum ar fi cele mai recente fișiere pe care le-ați lucrat, ce este nou în lumea FreeCAD sau informații rapide despre cele mai comune ateliere de lucru. De asemenea, vă va notifica dacă este disponibilă o nouă versiune stabilă a FreeCAD.


<div class="mw-translate-fuzzy">

Dar după un timp sau după ce ați făcut unele modificări în preferințe, veți fi mai probabil probabil să vă aflați direct în unul dintre celelalte ateliere de lucru, cu un nou document deschis. Sau pur și simplu, închideți fila de start și creați un nou document   *


</div>


<div class="mw-translate-fuzzy">

![](images/Freecad-interface-02.jpg )


</div>

### Ateliere

Rețineți că unele dintre pictograme s-au schimbat între cele două capturi de ecran de mai sus. Aici intră în joc cel mai important concept utilizat în interfața FreeCAD   * atelierul de lucru.

Atelierele de lucru reprezintă grupuri de instrumente (butoane din bara de instrumente, meniuri și alte controale de interfață) care sunt grupate împreună în funcție de specialitate. Gândiți-vă la un atelier unde aveți oameni care lucrează împreună   * o persoană care lucrează cu metal, altul cu lemn. Fiecare dintre ei are, în atelierul lor, o masă separată cu instrumente specifice pentru slujba sa. Cu toate acestea, toate pot lucra pe aceleași obiecte. Același lucru se întâmplă în FreeCAD.

Cel mai important control al interfeței FreeCAD este selectorul de atelier(Workbench), pe care îl folosiți pentru a comuta de la un ataelier la altul   *


<div class="mw-translate-fuzzy">

![](images/Freecad-interface-03.jpg )


</div>


<div class="mw-translate-fuzzy">

Atelierele de lucru adesea îi lasă confuzi pe utilizatorii noi, deoarece nu este întotdeauna ușor să știți în ce Aelier să căutați un anumit instrument. Dar ei vor învăța rapid contextul și, după un timp scurt, se vor simți în largul lor - realizând că este o modalitate convenabilă de a organiza multitudinea de instrumente pe care FreeCAD le poate oferi. Atelierele de lucru sunt, de asemenea, complet personalizabile (a se vedea mai jos).


</div>

Later in this manual, you will also find a table showing the contents of all Workbenches.

### Interfața

Să aruncăm o privire mai bună asupra diferitelor părți ale interfeței   *


<div class="mw-translate-fuzzy">

![](images/Freecad-interface-04.jpg )


</div>


<div class="mw-translate-fuzzy">

-   **The 3D view** este componentul principal al interfeței. Acesta poate fi deconectat din fereastra principală, într-o fereastră care îi este didicată, puteți avea mai multe vizualizări ale aceluiași document (sau aceleași obiecte) sau mai multe documente deschise în același timp. Puteți selecta obiecte sau părți de obiecte făcând clic pe ele și puteți panorama, mări și roti vizualizarea cu butoanele mouse-ului. Acest lucru va fi explicat în continuare în capitolul următor.
-   **The combo view** has two tab uri   *
    -   Model tab vă arată conținutul și structura documentului de mai sus și proprietățile (sau parametrii) obiectelor selectate mai jos. Aceste proprietăți sunt separate în două categorii   *
        -   Data (proprietăți care privesc geometria însăși)
        -   View (proprietăți care afectează modul în care arată geometria pe ecran).
    -   Tasks Tab este locul în care FreeCAD vă va solicita valori specifice instrumentului pe care îl utilizați în prezent - de exemplu, introduceți o valoare \"lungime\" atunci când este utilizat instrumentul Linie. Se va închide automat după apăsarea butonului OK (sau Cancel). De asemenea, făcând dublu clic pe obiectul asociat în vizualizarea combo, majoritatea instrumentelor vă vor permite să redeschideți panoul de sarcini pentru a modifica setările.
-   **The report view** este în mod normal ascuns, dar este o idee bună să-l lăsați deschis, deoarece va afișa orice informații, avertismente sau erori pentru a vă ajuta să descifrați (sau să depanați) ce ați greșit.
-   **The Python console** este de asemenea ascuns în mod implicit. Aici puteți interacționa cu conținutul documentului folosind [Python language](https   *//en.wikipedia.org/wiki/Python_%28programming_language%29). Deoarece fiecare acțiune pe care o faceți pe interfața FreeCAD execută de fapt o bucată de cod Python, acest lucru vă permite să vizualizați codul în timp real - permițându-vă un mod minunat și ușor de a învăța un pic de Python pe drum, aproape fără să observați aceasta.


</div>

In addition to the 3D view panel, the following information panels are available. They may be made visible or hidden by selecting them from **View → Panels** . The name of the panel appears in the upper left corner of the panel when it is displayed   *

-   **The combo view** has two tabs   *
    -   The Model tab shows you the contents and structure of your document above and the properties (or parameters) of the selected object(s) below. These properties are separated into two categories   *
        -   Data (properties which concern the geometry itself)
        -   View (properties that affect how the geometry looks on screen).
    -   The Tasks tab is where FreeCAD will prompt you for values specific to the workbench and tool you are currently using. For example, entering a \'length\' value when the [Draft Workbench Line Tool](Draft_Line.md) is being used. It will clear and switch back to the Model tab after the **OK** (or Cancel) button is pressed. Double-clicking the related object in the Model tab will usually reopen the corresponding Task tab in order to modify the settings.
        The Tasks tab sometimes has puzzling and frustrating side-effects. If the Task tab is not empty, some FreeCAD operations will not work as expected. For example, if you have a single object in your model such as a cube, double-clicking on it will open the Tasks tab to allow you to modify the parameters characterizing the cube. If you have the [Selection view](#Selection_view.md) open, you will see the cube\'s internal name listed there. The entire cube will turn green in the 3D panel, indicating the entire cube is selected. Clicking on the background will deselect the entire cube and clear the Selection view. So far, this is normal behavior. However, if you now click on a face of the cube, instead of that face being selected, nothing will be selected --- because the Tasks tab has not been completed. Even if you have made no modifications to the parameters there, FreeCAD is waiting for the **OK** (or other) button in the Tasks tab to be clicked.

-   **The report view** is normally hidden, but it is a good idea to open it as it will list any information, warnings or errors to help you decipher (or debug) what you may have done wrong.
-   **The Python console** is also hidden by default. This is where you can interact with the contents of the document using the [Python language](https   *//en.wikipedia.org/wiki/Python_%28programming_language%29). Since every action you do on the FreeCAD interface actually executes a piece of Python code, having this open allows you to watch the code unfold in real time --- allowing you a wonderful and easy way to learn a little Python on the way, almost without noticing it.
-   **The tree view** displays only the object tree shown under the Model tab in the combo view. It is normally hidden.
-   **The property view** displays only the object property information shown at the bottom of the combo view. It is normally hidden.
-   **The selection view** shows the names of any objects which are currently selected. These are the objects to which a workbench operation will be applied. It can be used to refine the selection by deselecting some of those objects before a workbench operation is applied. The selection view can also be used to search for objects by name and then select them. By default, the selection view is hidden. While you can often determine the currently selected object(s) by looking at the object tree in the Model tab of the combo view, for complex operations requiring multiple selections and where selection is difficult it is helpful to make this view visible so you can both see the labels and count the selected objects.


<div class="mw-translate-fuzzy">

![](images/Freecad-interface-07.jpg )


</div>

### Personalizarea interafeței 

Interfața FreeCAD este foarte personalizabilă. Toate panourile și barele de unelte pot fi mutate în locuri diferite sau stive una deasupra celeilalte. De asemenea, acestea pot fi închise și redeschise atunci când este necesar din meniul Vizualizare sau făcând clic dreapta pe o zonă goală a interfeței. Există, însă, mai multe opțiuni disponibile, cum ar fi crearea de bare de instrumente personalizate cu instrumente de la oricare dintre atelierele de lucru sau atribuirea și schimbarea comenzilor rapide de la tastatură.


<div class="mw-translate-fuzzy">

Aceste opțiuni avansate de personalizare sunt disponibile de la **Tools -> Customize menu**   *


</div>


<div class="mw-translate-fuzzy">

![](images/Freecad-interface-06.jpg )


</div>

**De citit în plus**

-   [Getting started with FreeCAD](Getting_started.md)
-   [Customizing the interface](Interface_Customization.md)
-   [Workbenches](Workbenches.md)
-   [More about Python](https   *//www.python.org)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Manual:The FreeCAD Interface/ro
