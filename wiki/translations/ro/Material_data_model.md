# Material data model/ro



**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

## Scop și principii 

Prin stocarea proprietăților materialelor într-o structură de date unificată, se urmărește facilitarea recuperării datelor care pot fi efectuate în diferite contexte:

-   la construirea unui model cu element finit
-   când faceți un model 3D
-   pentru a putea urmări modificările într - un material al unei \"componente\" create în FreeCAD, pentru aplicații [PDM](http://en.wikipedia.org/wiki/Product_Data_Management) applications,
-   Aplicație BIM (arhitectură și industria construcțiilor)

Pentru a gestiona proprietățile materialelor, se propune crearea unui model specific de date care va fi instanțiat când se creează un material nou în cadrul FreeCAD.

Va fi posibil să creați un material fie prin definirea manuală a proprietăților sale printr-un atelier de lucru material, fie prin citirea proprietăților materialelor dintr-un fișier. Formatele unor astfel de fișiere trebuie definite (unele există deja, cum ar fi MatML, STEP AP235 & IGR45\...).

De asemenea, va fi posibilă salvarea proprietăților materiale într-o colecție de fișiere într-un format care urmează să fie ales, de asemenea. Colecția de fișiere care pot fi stocate într-un director comun va forma baza de date a materialelor FreeCAD.

Prin acest model de date, materialul poate fi definit în FreeCAD fără a fi nevoie să se definească o \"componentă\".

Un nou indicator va fi creat în modelul de date \"component\", pentru a se conecta la un material care a fost definit prin modelul de date material.

## Rezultat

Prin acest model de date material, se propune să ofere un instrument pentru a gestiona ușor datele materiale în cadrul FreeCAD.

## Brainstorming

## Organizare

Diferitele tipuri de date trebuie gestionate pentru a descrie un material. Un model de date despre material este propus mai jos. Sunt date și câteva exemple de date care pot fi stocate în cadrul acestei structuri.

### Material data model 

În plus față de atributele clasice de \"înlănțuite\" cum ar fi un nume și o familie, 3 tipuri diferite de informații specifice trebuie gestionate pentru a descrie un material în FreeCAD.

-   proprietăți: structura generică pentru stocarea datelor care descriu proprietățile inginerești ale materialului
-   compoziția chimică: compoziția chimică a materialului
-   aspect: informații care descriu cum va arăta materialul în FreeCAD (culoare, strălucire \...)

Nu este necesar ca toate aceste tipuri de informații să fie definite în mod necesar pentru ca materialul să existe. În final, mai jos este lista de atribute reținute pentru a descrie un material în FreeCAD.

#### Nume

Un șir text indicând numele materialului. Este desemnarea sa.

#### Familia

Un șir text indicând familia materialului, cum ar fi de exemplu:

-   metal
-   plastic
-   \...

În plus, se propune crearea unei hărți între familii (de exemplu stocate într-un fișier XML), astfel încât să se poată naviga în baza de date a materialului FreeCAD.

O astfel de hartă ar putea conține, de exemplu, un copac care prezintă relații între familii, cum ar fi:

-   metal -\> steel -\> flat carbon steel -\> advanced high strength steel
-   metal -\> aluminium -\> casted aluminium

#### Manufacturer

Un șir text indicând producătorul materialului.

#### URL

A string indicating the web page presenting the material.

#### Properties

##### Description

The material data model includes a collection of properties. The size of such a collection is not fixed and may be extended with new user-defined properties.

O proprietate conține următoarele atribute.

-   name: string
-   symbol: string to write the symbol of the properties (?in Latex math format?)
-   type: \"scalar\" or \"array\"
-   value: scalar (if it is a scalar)
-   values: array (if it is an array)
-   parameterNames: array of strings (for \"array\" type property)
-   parameterValues: array of scalars (for \"array\" type property)
-   unit & unitMagnitude (specific object described in [Units](Units.md)) (pentru a fi notat: exemplele includ unitMagnitude, în timp ce nu sunt complet sigur că ar trebui să fie definită la nivel de proprietate. Sistemul unitar poate fi definit la nivel de material)
-   direction: un vector care indică în ce direcție se înțelege valoarea proprietății. Vectorul este el însuși un obiect FreeCAD exprimat în sistemul global de coordonate sau într-un sistem de coordonate definit de utilizator
-   note: șir text care poate fi folosit pentru a descrie un pic mai mult proprietatea cum ar fi semnificația acesteia, cum a fost măsurată \... De asemenea, poate ajuta la înțelegerea numelui proprietăților

Proprietățile materialelor vor fi identificate datorită numelui lor pentru a le prelucra, adică, de exemplu, scrierea limita de elasticitate într-un model cu elemente finite. Pentru a facilita crearea de materiale în cadrul FreeCAD, o listă standardizată a numelor de proprietăți împreună cu unitățile de măsură standard va fi propusă utilizatorului. Cu toate acestea, utilizatorul este liber să creeze proprietăți noi, cu nume noi, unități noi și așa mai departe \...

Mai jos, o propunere pentru o bibliotecă standard de proprietăți. Nu ezitați să adăugați altele noi \...


<?xml version="1.0" encoding="UTF-8"?>



  
        
     








Note: \"Coeficientul Mean Lankford este reprezentativ pentru anizotropia unei foi metalice subțiri\". \"Coeficientul de întărire este reprezentativ pentru capacitatea de durificare a unui metal\". Apare în formula Hollomon care poate conectată cu alungirea la rupere.\"

##### Examplul 1: Cost per tonne 

Un prim exemplu este dat mai jos care arată cum o proprietate *Cost per tonne* poate fi stocată.

-   name: Cost per tonne
-   symbol: not applicable
-   type: scalar
-   value: 500
-   values: not applicable (but could be: for instance different cost values per different countries)
-   parameterNames: not applicable (but could be: for instance different cost values for different countries)
-   parameterValues: not applicable (but could be: for instance different cost values for different countries)
-   parameterUnits: not applicable
-   unit & unitMagnitude: \[\[ 0, -3, 0, 0, 0, 0, 0\], 1\]
    -   meaning m\^(-3) (more details about unit & unit system specifications in [Units](Units.md) page)
-   direction: not applicable

##### Examplul 2: Yield strength 

Un al doilea exemplu este dat mai jos pentru a arăta cum poate fi stocată proprietatea \'Yield strength\'\' (limita de elasticitate).

-   name: Yield stress
-   symbol: YS
-   type: scalar
-   value: 450
-   values: not applicable
-   parameterNames: not applicable
-   parameterValues: not applicable
-   parameterUnits: not applicable
-   unit & unitMagnitude: \[\[ -1, 1, -2, 0, 0, 0, 0\], 1\]
    -   meaning Pa (more details about unit & unit system specifications in [Units](Units.md) page)
-   direction: \[ 1, 0, 0\] in global coordinate system
    -   given a steel sheet, this means that the *Yield strength* given is expressed in *x* direction, that can be for instance the rolling direction

##### Examplul 3: Durificarea 

Un al treilea exemplu este prezentat mai jos, pentru a arăta cum poate fi stocată proprietatea de durificare *Strain hardening*. Acesta este un exemplu mai complex, deoarece durificarea este reprezentată de o serie de curbe. Curbele reprezintă evoluția stresului în raport cu epruveta de plastic. 3 curbe au fost obținute la rate diferite de tensiune. Toate curbele au fost obținute la temperatura camerei.

-   name: Strain hardening
-   symbol: not applicable
-   type: scalar
-   value: not applicable
-   values: \[\[0., 100, 150, 200\], \[ 0., 120, 180, 210\], \[ 0., 140, 190, 220\]\]
-   parameterNames: \[Plastic strain, Strain rate, Temperature\]
-   parameterValues:
    -   The 1st three arrays represents plastic strain evolutions
    -   The 2nd serie of three arrays represents the strain rate evolutions. A single value is given in each of the arrays, meaning that the strain rate doesn\'t change for each the corresponding stress evolutions.
    -   The last serie of a single array represents temperature evolutions. This time a single value is written in a single array, meaning that temperature doesn\'t change for a given array of stress, and this applies for all stress arrays.
        1.  1st serie: \[\[\[0. , 0.4, 0.8, 1\], \[ 0, 0.4, 0.8, 1\], \[ 0, 0.4, 0.8, 1\]\],
        2.  2nd serie: \[\[0.\] , \[100\] , \[1000.\] \],
        3.  3rd serie: \[\[18.\] \],\]
-   parameterUnits & parameterUnitMagnitudes: \[\[\[ 0, 0, 0, 0, 0, 0, 0\], 1\], \[\[ 0, 0, -1, 0, 0, 0, 0\], 1\], \[\[ 0, 0, 0, 0, 1, 0, 0\], 1\]\]
    -   meaning none, s\^(-1) and, K (more details about unit & unit system specifications in [Units](Units.md) page)
-   unit & unitMagnitude: \[\[ -1, 1, -2, 0, 0, 0, 0\], 1\]
    -   meaning Pa (more details about unit & unit system specifications in [Units](Units.md) page)
-   direction: not applicable

#### compoziția Chimică 

\[Yet to be filled up\]

#### Aparența

\[Yet to be filled up\]

#### Note

Un șir în care utilizatorul poate adăuga propriile comentarii despre material.

### Aplicarea datelor modelului hard: câteva exemple 

##### Example 1: Cărămidă de zidar 

###### Nume 

Cărămidă de zidarie

###### Familie

?string?

###### Proprietăți

-   *Weight*: 1kg/m³
-   *Cost per cubic meter*: 1€/m³
-   *Number of bricks por base unit*: ?float?
-   *Volume of mortar por base unit*: ?float?
-   *Mortar type*: ?string?
-   *Brick type*: ?string?
-   *Fire resistance class*: ?string?
-   *Thermal conductivity*: 1 W/mK

###### Producător

?string?

###### URL 

?string?

###### Note 

Note despre întreținere, precauții speciale de luat etc.

codul CSI/MasterFormat (întrucât există mai multe sisteme utilizate în industrie care dau tuturor materialelor un cod special, propun să le introducem în note, deoarece nu mi se pare relevant să se creeze anumite proprietăți pe care nu le vom putea numi exact).

## Următoarele acțiuni 

-   Definiți un set de nume pentru proprietățile clasice, pe care le putem defini într-un dicționar (fișier de configurare FreeCAD). Aceste proprietăți vor fi reutilizate în mod special în alte contexte, cum ar fi modulul FEM.
-   Completați secțiunea *Chemical composition*.
-   Completați secțiunea *Appearance* .
-   Definiți un set de componente chimice implicite.
-   Revizuirea de către alte persoane.
-   Implementarea în modelul de date C ++ și abilitatea de a scrie / citi într-un fișier (ISO 10303-45 prin SCL?).
-   Implementați dicționare XML pentru a stoca proprietățile implicite, cu unitățile acestora, care pot fi utilizate de utilizator.
-   Implementați GUI-ul python pentru a gestiona aceste date.



[Category:Roadmap](Category:Roadmap.md)
