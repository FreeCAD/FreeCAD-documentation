---
- GuiCommand:   Name:Ship New‏‎    MenuLocation:Ship design → Create a new ship   |Workbenches:[[Ship Workbench   Ship]]|Shortcut:   SeeAlso:---


</div>


<div class="mw-translate-fuzzy">

## Introducere

De făcut


</div>

Create a New Ship or new Ship Instance.

## Usage

In order to create a **Ship instance** (in other words, a New Ship), select s60 geometry and execute the **ship creation tool** {{MenuCommand|Ship design → Create a new ship}}


<div class="mw-translate-fuzzy">

Se va afișa un dialog de activități privind nava și unele adnotări la vizualizarea 3D. Adnotările vor fi eliminate atunci când închideți instrumentul de creare a navelor, deci nu vă faceți griji în legătură cu acest lucru.


</div>

Trebuie introduse cele mai importante date despre nave (FreeCAD-Ship utilizează un sistem de introducere progresivă a datelor, astfel încât operațiunile de bază pot fi realizate cunoscând numai datele de bază ale navelor, mai multe informații fiind necesare deoarece operațiunile devin mai complexe).

## Ship data {#ship_data}


<div class="mw-translate-fuzzy">

### Date despre nava {#date_despre_nava}

Dimensiunile principale trebuie introduse aici:

-   Lungime: Lungime între perpendiculare, 25,5 m pentru această navă.
-   Lățimea: Lățimea totală a navei, 3,389 m pentru această navă.
-   Schiță: Pescajul proiectat, 1,0 m pentru această navă.


</div>


<div class="mw-translate-fuzzy">

![Front view annotations](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Length annotations.


</center>


</div>

De obicei, lungimea dintre perpendiculare depinde de schița proiectului, deci dacă nu știți care este lungimea navei dvs. puteți seta schița și potriviți lungimea pentru a obține arcul și cursa intersecție.


<div class="mw-translate-fuzzy">

![Side view annotations](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Beam annotations.


</center>


</div>


<div class="mw-translate-fuzzy">

Acelasi proces este valabil si pentru Beam fit. Rețineți că valoarea solicitată este fasciculul total, dar adnotarea se referă doar la jumătatea navei tribord.


</div>


<div class="mw-translate-fuzzy">

Când apăsați butonul **Accept** programul crează noua Ship instance numită **Ship** la dialogul *Tags & Attributes*. Nu mai avem nevoie de geometrie, ca să-l ascunzi.


</div>


<div class="mw-translate-fuzzy">

De aici mi departe, trebuie să avem **Ship** selectată înainte de a executa orice instrument FreeCAD-Ship .


</div>

## Tutoriale

-   [FreeCAD-Ship s60 tutorial ](FreeCAD-Ship_s60_tutorial.md)
-   [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)

\|[Ship Geometries Examples Loader](Ship_Geometries_Examples.md) \|[Lines drawing](Ship_Outline.md) \|[Ship](Ship_Workbench.md) \|IconL=Ship\_Load.svg \|IconC=Workbench\_Ship.svg \|IconR=Ship\_OutlineDraw.svg }}


{{Ship_Tools_navi

}} 
