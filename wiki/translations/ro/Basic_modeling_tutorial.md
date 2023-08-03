# Basic modeling tutorial/ro
---
 TutorialInfo:o
   Topic:  Introduction to modelling
   Level:  Beginner
   Time:  15 minutes
   Author: User:Normandc
   FCVersion: any
   Files: none
}}

## Introduction


<div class="mw-translate-fuzzy">

Acest tutorial de bază de modelare vă va arăta cum să modelați un profil cornier. Unul dintre lucrurile pe care trebuie sa le știți este că FreeCAD este modular prin design, și la fel ca și pentru multe alte aplicații CAD, există întotdeauna mai multe moduri de a face lucrurile. Vom explora două metode aici.


</div>

This tutorial was written with version 0.15 of FreeCAD.

## Înainte de a începe 

Rețineți că FreeCAD se află încă într-un stadiu incipient de dezvoltare, astfel încât este posibil să nu fiți la fel de productiv ca și cu o altă aplicație CAD și veți întâlni cu siguranță bug-uri sau veți experienta diverse accidente. FreeCAD are acum posibilitatea de a salva fișierele de rezervă. Numărul fișierelor de rezervă poate fi specificat în dialogul de preferințe. Nu ezitați să permiteți 2 sau 3 fișiere de rezervă până când știți cum să rezolvați problema cu FreeCAD.

Salvați-vă munca frecvent, din când în când, salvați-vă munca sub un nume diferit, astfel încât să aveți o copie \"sigură\" pentru a reveni înapoi și fiți pregătiți pentru posibilitatea ca unele comenzi să nu vă dea rezultatele așteptate.


<div class="mw-translate-fuzzy">

## Tehnici de modelare Intro 

Prima tehnică  a modelării solide este Constructive Solid Geometry . Lucrați cu forme primitive, cum ar putea fi cuburi, cilindri, sfere și conuri, pentru a vă construi forme geometrice prin combinarea lor, scăzând o formă de alta sau intersectându-le.Aceste instrumente fac parte din Part Workbench. Puteți aplica, de asemenea, transformări pe forme, cum ar fi aplicarea rotunjimilor sau ;anfernului pe margini. Aceste instrumente sunt, de asemenea, în Atelierul Part Workbench.


</div>

Apoi, există instrumente mai avansate. Începeți prin a desena un profil 2D pe care îl veți extinde sau îl veți roti.

Deci, să începem prin încercarea de a face niște picioare de fier pentru o masă cu aceste două metode.


<div class="mw-translate-fuzzy">

## Prima metodă - By Constructive Solid Geometry 

1.  Start cu Atelierul Piese Part Workbench !.
2.  Dacă încă nu aveți deschis un nou document FreeCAD , din meniul derulant, faceți clic pe File -\> New sau faceți clic pe!{width="32"} **Create a new empty document** icon.
3.  Click pe butonul !{width="32"} Box pentru a crea o casetă
4.  Modificați dimensiunile selectând-o fie în spațiul 3D, fie făcând clic pe ele în tab-ul Proiect spre stânga, apoi
5.  Faceți clic pe tab-ul Date din partea de jos și modificați valorile pentru Lungime, Lățime și Înălțime la 50mm, 50 and 750 ** **Note**: *back when these captures were taken, the properties were ordered differently, with Height being first*.
6.  Caseta este acum umplută cu cea mai mare parte a vederii 3D . Click pe !{width="32"} Fit All pentru a potrivi vederea la caseta nou creată.
7.  Creați o a doua casetă în același mod, dar cu valori L=40, W=40 and H=750mm. În mod prestabilit, această casetă va fi suprapusă pe prima. **
8.  Veți scăpa a doua cutie de la prima. Salegeți mai întâi prima formă , apoi a doua , ordinea de selectare este importantă!  la alegerea CAD sau Blender.)
9.  În bara de instrumente a Atelierului Piese, click pe instrumentul !{width="32"} Cut .


</div>

!Fig. 1.1 The first box

!Fig. 1.2 The second box on top of the first one, ready to be subtracted

!Fig. 1.3 After the subtraction


<div class="mw-translate-fuzzy">

Dacă aveți primul cornier din oțel **. Veți observa că, în tab-ul Project din panoul lateral stânga, ambele casete au fost înlocuite cu un obiect \"Cut\". De fapt, formele inițiale nu sunt dispărute, ci mai degrabă grupate sub obiectul Cut. Click pe + situat în fața lui, si veti vedea ca ambele nume sunt încă acolo, dar sunt gri**. Dacă faceți clic pe oricare dintre ele și apăsați bara de spațiu, va apărea caseta în fereastra model. Bara de spațiu este o scurtătură care comută vizibilitatea obiectelor selectate. **


</div>


<div class="mw-translate-fuzzy">

Nu vrei unghiul orientat în acest fel? Trebuie doar să schimbați poziția formei Box001. Selectați-l, afișați-l și în fila Date, faceți clic pe + în fața destinației de plasare, apoi extindeți parametrul Poziție și modificați coordonatele X și Y. Apăsați Enter, ascunde din nou forma Box001, iar orientarea unghiului este acum diferită. **Puteți schimba oricare dintre dimensiunile formelor dvs., iar obiectul Cut va fi actualizat.


</div>

!Fig. 1.4 The cut operation retains its original objects ")

!Fig. 1.5 You can still make the original boxes visible


<div class="mw-translate-fuzzy">

Apropo, putem adăuga rotunjiri la unghi astfel încât piesa pare mai realistă, folosind!{width="32"} Fillet tool. **


</div>

!Fig. 1.6 The filleted edges


<div class="mw-translate-fuzzy">

## a 2-a Metodă - Prin extruderea unui profil 

Această metodă necesită pentru început începerea desenarea unui profil 2D. Trebuie să activați Draft workbench !.

-   Dacă nu ați deschis un document FreeCAD nou , din meniul derulant faceți clic pe File -\> New sau clic pe !{width="32"} **Create a new empty document** icon.


</div>

### Definirea planului de lucru 

Prima dată trebuie să definim pe care plan working plane desen 2D profilul nostru.

1.  Localizați bara de instrumente afișată mai jos. În funcție de preferințele dvs. de proiect, este posibil să fie sub bara principală de instrumente, spre stânga sau spre dreapta.

    :   !
2.  Press the **Auto** button .
3.  În funcție de preferințele dvs. de proiect, aceasta extinde a **Select Plane**în panoul lateral Tasks sau o bară de instrumente orizontală etichetate \"active command: **Select Plane**\". See the Note on Draft Working Plane Button pentru capturile de ecran care arată cele două moduri extinse.
4.  vom lăsa câmpul *Offset* la valoarea zero.
5.  Press the **XY** pentru a seta planul de lucru la XY. Aceasta închide panoul Lucrări sau butoanele extinse.Butonul \"Auto\" va fi acum redenumit ca fiind \"Top\" pentru a arăta că este planul activ.


<div class="mw-translate-fuzzy">

### Elaborarea profilului 

1.  Select the !{width="32"} DWire  tool.
2.  Check the \"Relative\" and \"Filled\" boxes.
3.  Rather than drawing the shape in the 3D view, we\'ll enter coordinates in the *Global X*, *Global Y* and *Global Z* input fields. The process is the following:
    1.  Click in the *Global X* input field;
    2.  Enter a value as listed in the bullet list below and press **TAB** to go to the *Global Y* input field;
    3.  Enter the *Global Y* value and press **TAB** to go to the *Global Z* input field;
    4.  In the *Global Z* field, leave the zero value and press **ENTER** to validate the coordinates for the point;
    5.  Repeat for the next 5 points.
        -   **Coordinates** 
        -   1st point: 0, 0, 0
        -   2nd point: 50, 0, 0
        -   3rd point: 0,10, 0
        -   4th point: -40, 0, 0 **Note:** *in FreeCAD 0.16, there is a bug that removes the previous point when entering the minus sign in the input field. A workaround is to enter a positive value, then place the cursor before the number and add the minus sign. *
        -   5th point: 0, 40, 0
        -   6th point: -10, 0, 0
4.  Press the **Close** button to close the profile. You should now have this profile, titled **DWire** in the Model tab:


</div>

!Fig. 1.7 The base DWire


<div class="mw-translate-fuzzy">

Apăsați tasta zero de pe tastatura numerică pentru a seta vederea axonometrică.


</div>


<div class="mw-translate-fuzzy">

### Extrudarea profilului 

Activați atelierul Piese Part Workbench fie din selectorul de bara de lucru, fie din**View -\> Workbench -\> Part** menu.


</div>


<div class="mw-translate-fuzzy">

Click on the **Image:Part_Extrude.png   32px Part_Extrude**{: mediawiki} tool.


</div>

În tab-ul Task din stânga, selectați. Obiectul **Wire** . Apoi introduceți lungimea dorită, să zicem 750mm. Leave the direction at Z = 1. Press **OK**. Ar trebui să aveți acum un obiect **Extrude** în tab-ul Model **

!Fig. 1.8 The extruded object

Deși această metodă necesită mai puțină operațiune decât prima, aceasta are un ușor dezavantaj : pentru a modifica forma, trebuie să modificați obiectul Wire, care este mai puțin ușoară decât editarea unor forme primitive, cum ar fi cuburile metodei anterioare.


<div class="mw-translate-fuzzy">

Și există și alte câteva modalități de a obține acest rezultat! Sper că aceste două exemple vor fi un început. Veți fi siguri că ați lovit câteva momente de-a lungul drumului , dar nu ezitați să puneți întrebări cu privire la FreeCAD forum!


</div>

### Notă cu privire la butonul de plan de lucru 

Eticheta de pe butonul dvs. poate fi diferită, în funcție de versiunea dvs. și de ceea ce ați făcut în prealabil. Eticheta cu buton poate citi: \"Top\", \"Front\", \"Side\", \"None\" sau o reprezentare a Vector ca de exemplu d. De asemenea, poate fi gol. De exemplu:

!Select Plane None

!Select Plane Top

!Select Plane View  După apăsarea butonului, opțiunile vor fi extinse în una din următoarele configurații.

!**Select Plane** parameters as shown in Tasks panel mode.

!**Select Plane** parameters as shown in Toolbar mode. 

Instrucțiunile de mai sus vor funcționa, indiferent de eticheta pe care o are butonul.


 {{Userdocnavi
---



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > Basic modeling tutorial/ro
