---
 GuiCommand:
   Name: Ship New‏‎
   MenuLocation: Ship design , Create a new ship
   Workbenches: Ship Workbench
   Shortcut: 
   SeeAlso: 
---

# Ship CreateShip/ro


</div>

## Introducere

De făcut

Create a New Ship or new Ship Instance.

Ship works over **Ship entities**, that must be created on top of provided geometry. Geometry must be a solid, or set of solids.The following criteria must be taken into account:

-   All hull geometry must be provided (including symmetric bodies).
-   Starboard geometry must be included at negatives *y* domain.
-   Origin (0,0,0) point is the **Midship section** (Midpoint between after and forward perpendicular) and **base line** intersection.

![](images/FreeCAD-Ship-SignCriteria.jpg ) 
*Ship sign criteria*

## Usage

In order to create a **Ship instance** (in other words, a New Ship), select the hull solid geometry and invoke **Ship design → <img src="images/Ship_CreateShip.svg" width=16px> Create a new ship**.

Se va afișa un dialog de activități privind nava și unele adnotări la vizualizarea 3D. Adnotările vor fi eliminate atunci când închideți instrumentul de creare a navelor, deci nu vă faceți griji în legătură cu acest lucru.

Trebuie introduse cele mai importante date despre nave (FreeCAD-Ship utilizează un sistem de introducere progresivă a datelor, astfel încât operațiunile de bază pot fi realizate cunoscând numai datele de bază ale navelor, mai multe informații fiind necesare deoarece operațiunile devin mai complexe).

## Ship data 

### Date despre nava 

Dimensiunile principale trebuie introduse aici:

-   Lungime: Lungime între perpendiculare, 25,5 m pentru această navă.
-   Lățimea: Lățimea totală a navei, 3,389 m pentru această navă.
-   Schiță: Pescajul proiectat, 1,0 m pentru această navă.

![](images/FreeCAD-Ship-S60ShipCreationFront.png ) ![Front view annotations](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Length annotations.


</center>

De obicei, lungimea dintre perpendiculare depinde de schița proiectului, deci dacă nu știți care este lungimea navei dvs. puteți seta schița și potriviți lungimea pentru a obține arcul și cursa intersecție.

![](images/FreeCAD-Ship-S60ShipCreationSide.png ) ![Side view annotations](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Beam annotations.


</center>

Acelasi proces este valabil si pentru Beam fit. Rețineți că valoarea solicitată este fasciculul total, dar adnotarea se referă doar la jumătatea navei tribord.

Când apăsați butonul **Accept** programul crează noua Ship instance numită **Ship** la dialogul *Tags & Attributes*. Nu mai avem nevoie de geometrie, ca să-l ascunzi.

## Tutoriale

-   [FreeCAD-Ship s60 tutorial ](FreeCAD-Ship_s60_tutorial.md)
-   [FreeCAD-Ship s60 tutorial (II)](FreeCAD-Ship_s60_tutorial_(II).md)



---
⏵ [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship CreateShip/ro
