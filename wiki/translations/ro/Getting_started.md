# Getting started/ro
## Cuvânt înainte 


<div class="mw-translate-fuzzy">

FreeCAD este [o aplicaţie parametrică de modelare](About_FreeCAD/ro.md) CAD/CAE. A fost creată în principal pentru desen tehnic, dar de asemenea serveşte tuturor nevoilor de modelare a unor obiecte 3D, cu precizie maximă şi control asupra etapelor de modelare.


</div>


<div class="mw-translate-fuzzy">

FreeCAD se află încă în stadii incipiente de dezvoltare, și oferă o listă largă (și în dezvoltare) de [features](Feature_list.md). Unele capabilități lipsesc încă comparativ cu soluțiile comerciale și le puteți găsi insuficient dezvoltate pentru a le utiliza în mediul industrial. Cu toate acestea, există o comunitate de utilizatori etuziaști [community](http://forum.freecadweb.org/index.php) , și puteți găsi deja [many examples](https://forum.freecadweb.org/viewforum.php?f=24) de proiecte de calitate dezvoltate cu FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Ca toate proiectele open source, proiectul FreeCAD nu este doar o modalitate de a lucra pentru dezvoltatorii săi. Depinde mult de comunitatea sa să crească, să câștige experiență și să se stabilizeze (să se fixeze bug-urile). Nu uitați acest lucru când începeți să utilizați FreeCAD, dacă vă place, puteți influența direct proiectul [help](Help_FreeCAD/ro.md)!


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Which workbench should I choose?](Which_workbench_should_I_choose.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)



## Instalare


<div class="mw-translate-fuzzy">

Mai întâi de toate, descărcați și instalați FreeCAD. Consultați pagina [Download](Download.md) pentru informații despre versiunile și actualizările curente și pagina [Installing](Installing.md) pentru instrucțiuni de instalare. Există pachete de instalare gata pentru Windows (.msi), Debian și Ubuntu (.deb), openSUSE (.rpm) și Mac OSX. FreeCAD este disponibil la administratorii pachetelor de la mai multe distribuții Linux. Este disponibil și un executabil standalone [AppImage](https://appimage.org/), care va funcționa pe cele mai recente sisteme Linux pe 64 de biți. Deoarece FreeCAD este open-source, poți descărca și codul sursă și [compila](Compiling.md) pe tine însuți.


</div>




<div class="mw-translate-fuzzy">

## Explorarea aplicației FreeCAD 


</div>

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface.png  style="width:1024px;">


</div>


<div class="mw-translate-fuzzy">

1.  Vederea 3D, afișează conținutul documentului
2.  Vizualizarea arborescentă, care prezintă ierarhia și istoricul construcțiilor tuturor obiectelor din document
3.  [properties editor](Property_editor/ro.md), care vă permite să vizualizați și să modificați proprietățile obiectelor selectate,
4.  Vizualizarea raportului (sau fereastra de ieșire), în care FreeCAD imprimă mesaje, avertismente și erori
5.  Consola python, în care sunt tipărite toate comenzile executate de FreeCAD și unde puteți introduce codul python
6.  [ workbench selector](Workbenches/ro.md), unde selectați atelierul de lucru activ


</div>


<div class="mw-translate-fuzzy">

Conceptul principal din spatele interfeței FreeCAD este că este separat în [ateliere](workbenches/ro.md). Un Atelier de lucru este o colecție de instrumente pentru o anumită sarcină, cum ar fi plase/rețele de discretizare [meshes](Mesh_Workbench/ro.md), sau desen [2D objects](Draft_Workbench/ro.md), sau [constrained sketches](Sketcher_Workbench/ro.md). Puteți schimba atelierul de lucru curent cu selectorul de bibliotecă de lucru (6). Poți [customize](Interface_Customization/ro.md) Instrumentele incluse în fiecare atelier de lucru, adăugați unelte de la alte ateliere de lucru sau chiar unelte create de noi, pe care le numim [macros](macros/ro.md). Punctele de pornire utilizate pe scară largă sunt [PartDesign Workbench](PartDesign_Workbench/ro.md) and [Part Workbench](Part_Workbench/ro.md).


</div>


<div class="mw-translate-fuzzy">

Când porniți FreeCAD pentru prima dată, vi se prezintă centrul de pornire. Iată cum arată acesta pentru versiunea 0.16


</div>

<img alt="" src=images/Start_center_0.19_screenshot.png  style="width:600px;">


<div class="mw-translate-fuzzy">

Pagina de Start vă permite să vă îndreptaţi rapid către unul atelierele obişnuite, să deschideţi fişierele folosite recent sau să citiţi cele mai noi ştiri din lumea FreeCAD. Puteţi schimba atelierul implicit cu opţiunea [Preferinţe](Preferences_Editor/ro.md) din meniul \"Editare\".


</div>



## Navigarea în spatiul 3D 


<div class="mw-translate-fuzzy">

FreeCAD vă oferă mai multe [moduri de navigare cu mouse-ul](Mouse_Model.md) diferite, ceea ce schimbă felul în care mouse-ul Dvs. interacţionează cu obiectele reprezentate 3D şi cu însuşi felul de vizualizare. Unul dintre ele este făcut anume pentru [touchpads](Mouse_Model#Touchpad_Navigation/ro.md), unde nu se foloseşte butonul din mijloc. Următorul tabel descrie modul implicit, numit **Navigare CAD** (puteţi schimba rapid modul de navigare curent prin clic cu butonul drept pe un o porţiune goală din spaţiul 3D):


</div>

Exista moduri de vizualizare predefinite (de sus, din fata, etc) ce se schimba folosind meniul Vizualizare, comenzile din bara de unelte Vizualizare sau scurtaturile numerice (**1**, **2**, etc\...) . Făcând clic dreapta pe un obiect sau pe o zonă goală a vizualizării 3D, aveți acces rapid la unele operații comune, cum ar fi setarea unei anumite vizualizări sau localizarea unui obiect în vizualizarea tip Arbore.



## Primii paşi în FreeCAD 


<div class="mw-translate-fuzzy">

Aplicația FreeCAD este de a vă permite să realizați modele 3D de înaltă precizie, să păstrați controlul strict al acestor modele (să reveniți la istoricul de modelare și să modificați parametrii) și să construiți aceste modele (prin imprimare 3D, prelucrare CNC sau chiar în construcții civile). Prin urmare, este foarte diferit de alte aplicații 3D realizate în alte scopuri, cum ar fi filmul de animație sau jocurile de noroc. Curba de învățare poate fi abruptă, mai ales dacă acesta este primul dvs. contact cu modelarea 3D. Dacă vă înpotmoliți într-un anumit moment, nu uitați că există o comunitate prietenoasă a utilizatorilor de pe forumul [FreeCAD](http://forum.freecadweb.org/index.php) care ar putea să vă aducă în cel mai scurt timp pe linia de plutire.


</div>


<div class="mw-translate-fuzzy">

Atelierul pe care îl veți utiliza în FreeCAD depinde de tipul de lucru pe care trebuie să-l faceți: Dacă intenționați să lucrați pe modele mecanice sau, mai general, la orice obiecte la scară redusă, probabil veți dori să încercați [PartDesign Workbench](PartDesign_Workbench.md). Dacă veți lucra în 2D, atunci veți comuta pe [Draft Workbench](Draft_Workbench.md), sau pe [Sketcher Workbench](Sketcher_Workbench.md) dacă aveți nevoie de constrângeri. Dacă veți dori să faceți construcții civile, atunci lansați [Arch Workbench](Arch_Workbench.md). Dacă lucrați cu proiectarea navelor , există un atelier specializat pentru dvs [Ship Workbench](Ship_Workbench.md). Iar dacă veniți din lumea OpenSCAD, încercați atelierul [OpenSCAD Workbench](OpenSCAD_Workbench.md)..


</div>


<div class="mw-translate-fuzzy">

Puteți comuta atelirele în orice moment, și de asemenea [customize](Interface_Customization.md) atelierul favorit pentru a adăuga scule de la alte atelire.


</div>



## Folosirea panourilor Proiectare componente (PartDesign) şi Schiţă 


<div class="mw-translate-fuzzy">

Atelierul [PartDesign Workbench](PartDesign_Workbench.md) a fost creat special pentru a făuri obiecte complexe, pornind de la forme simple, prin adăugarea sau înlăturarea unor piese (pe care le numim \"funcţii\"), până la obţinerea obiectului în final. Toate funcţiile aplicate pe parcursul procesului de modelare sunt păstrate într-o mică fereastră numită [Vizualizare Combo](Document_structure/ro.md), care conţine şi celelalte obiecte din documentul Dvs. Practic, un obiect realizat cu \"Proiectare componente\" reprezintă o succesiune de operaţii, fiecare aplicată la lucrul produs în faza precedentă, astfel încât ele formează un lanţ prelung. În \"Vizualizare Combo\", vedeţi obiectul finalizat, dar el poate fi expandat astfel încât să-i regăsiţi toate stările precedente, să le modificaţi parametrii, schimbări care vor actualiza în mod automat aspectul final al obiectului.


</div>


<div class="mw-translate-fuzzy">

Atelierul PartDesign utilizează intens un alt atelier de lucru, [Sketcher Workbench](Sketcher_Workbench.md). vă permite să desenați figuri 2D, care sunt definite prin aplicarea Constrângerilor la forma 2D. De exemplu, puteți trage un dreptunghi și puteți seta dimensiunea unei părți aplicând o constrângere de lungime pe una din laturi. Această parte nu mai poate fi redimensionată (cu excepția cazului în care constrângerea este modificată).


</div>

Aceste forme 2D realizate cu sketcher-ul sunt folosite foarte mult în bara de lucru PartDesign, de exemplu pentru a crea volume 3D sau pentru a desena zone pe fețele obiectului dvs. care vor fi apoi scoase din volumul principal. Acesta este un flux de lucru tipic PartDesign:

1.  Creați o schiță nouă
2.  Desenați o formă închisă (asigurați-vă că toate punctele sunt legate)
3.  Închideți schița
4.  Extindeți schița într-un solid 3D utilizând instrumentul de blocare
5.  Selectați o față a solidului
6.  Creați o a doua schiță (de data aceasta va fi desenată pe fața selectată)
7.  Desenați o formă închisă
8.  Închideți schița
9.  Creați un buzunar din a doua schiță, pe primul obiect

Care vă dă un obiect ca acesta:

<img alt="" src=images/Partdesign_example.jpg  style="width:600px;">

În orice moment, puteți selecta schițele originale și le puteți modifica sau puteți schimba parametrii de extrudare ai operațiilor de blocare sau buzunar, care vor actualiza obiectul final.




<div class="mw-translate-fuzzy">

## Lucrând cu atelierele Desen 2D și Arhitectură 


</div>


<div class="mw-translate-fuzzy">

Atelierele [Draft Workbench](Draft_Workbench.md) și [Arch Workbench](Arch_Workbench.md) se comporta un pic diferit fata de celelalte ateliere de mai sus, deși urmează aceleași reguli, care sunt comune tuturor FreeCAD-urilor. Pe scurt, în timp ce Sketcher și PartDesign sunt create în primul rând pentru a proiecta piese unice, Draft și Arch sunt făcute pentru a vă ușura munca atunci când lucrați cu mai multe obiecte mai simple.


</div>


<div class="mw-translate-fuzzy">

Atelierul [Draft Workbench](Draft_Workbench.md) vă oferă instrumente 2D cumva similare cu ceea ce puteți găsi în aplicațiile tradiționale 2D CAD cum ar fi[AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). Totuși, desenarea 2D fiind departe de domeniul FreeCAD, nu vă așteptați să găsiți acolo o gamă completă de instrumente care oferă aceste aplicații dedicate. Majoritatea instrumentelor de proiectare funcționează nu numai într-un plan 2D, ci și în întreg spațiul 3D și beneficiază de sisteme speciale de ajutor, cum ar fi [Work planes](Draft_SelectPlane.md) și [object snapping](Draft_Snap.md).


</div>


<div class="mw-translate-fuzzy">

Atelierul [Arch Workbench](Arch_Workbench/ro.md) adaugă [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) tools to FreeCAD, permițându-vă să construiți modele arhitecturale cu obiecte parametrice. Baza de lucru Arch se bazează extensiv pe alte module cum ar fi Draft și Sketcher. Toate instrumentele de proiectare sunt de asemenea prezente în Atelierul de lucru Arch și majoritatea instrumentelor Arch utilizează sistemele Helper desen 2D (Draft).


</div>


<div class="mw-translate-fuzzy">

Un flux de lucru tipic cu atelierele de lucru Arch și Draft ar putea fi:


</div>


<div class="mw-translate-fuzzy">

1.  Desenați câteva linii cu ajutorul instrumentului Draft Line
2.  Selectați fiecare linie și apăsați instrumentul Perete pentru a construi un perete pe fiecare dintre ele
3.  Alăturați pereții selectând-i și apăsând instrumentul Arch Add
4.  Creați un obiect tip pardoseală și mutați pereții în el din vizualizarea Arbore
5.  Creați un obiect construit și mutați podeaua în el din vizualizarea Arbore
6.  Creați o fereastră făcând clic pe instrumentul Fereastră, selectați o presetare în panoul său, apoi faceți clic pe o față a unui perete
7.  Adăugați cotele prin setarea inițială a planului de lucru, dacă este necesar, apoi utilizând instrumentul Draft Dimension


</div>

Ceea ce vă va aduce asta:

<img alt="" src=images/Arch_workflow_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

Mai mult în pagina [Tutorials](Tutorials.md).


</div>




<div class="mw-translate-fuzzy">

## Script


</div>

Any user can develop their own new features for FreeCAD and make them available to the FreeCAD community as an [addon](Addon.md).

There are three types of addons:

-   [Macros](Macros.md): short snippet of [Python](Python.md) code that provides a new tool or functionality in a single file ending with `.FCMacro`.
-   [Workbenches](External_workbenches.md): collections of Python files that provide related [Gui Commands](Gui_Command.md) (tools) centered around a particular topic.
-   [Preference Packs](Preference_Packs.md): distributable collections of user preferences.

## Scripting


<div class="mw-translate-fuzzy">

Iar, la sfârşit, să remarcăm că una dintre cele mai puternice caracteristici ale FreeCAD este mediul creat de [script-programare](scripting.md). De la consola integrata Python (sau oricare alt script extern Python) se poate controla aproape orice parte a programului, se pot crea si modifica geometrii, se poate modifica reprezentarea obiectelor in scena 3D sau accesa si modifica interfata FreeCAD. Script-urile Python pot fi folosite si in [macroinstructiuni](macros.md), ceea ce furnizeaza o metoda usoara de creare a comenzilor personalizate.


</div>




<div class="mw-translate-fuzzy">

## Ce e nou 


</div>


<div class="mw-translate-fuzzy">

-   [Version 0.17 Release notes](Release_notes_0.17.md) : Verificați ce este nou în varianta 0.17 de FreeCAD
-   [Version 0.16 Release notes](Release_notes_0.16.md) : Verificați ce este nou în varianta 0.16 de FreeCAD
-   [Version 0.15 Release notes](Release_notes_0.15.md) : Verificați ce este nou în varianta 0.15 de FreeCAD
-   [Version 0.14 Release notes](Release_notes_0.14.md) : Verificați ce este nou în varianta 0.14 de FreeCAD
-   [Version 0.13 Release notes](Release_notes_0.13.md) : Verificați ce este nou în varianta 0.13 de FreeCAD
-   [Version 0.12 Release notes](Release_notes_0.12.md) : Verificați ce este nou în varianta 0.12 de FreeCAD
-   [Version 0.11 Release notes](Release_notes_0.11.md) : Verificați ce este nou în varianta 0.11 de FreeCAD


</div>


<div class="mw-translate-fuzzy">


{{docnav/ro|Install on Mac/ro|Mouse Model/ro}}


</div>



---
⏵ [documentation index](../README.md) > Getting started/ro
