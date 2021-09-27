# UTF Project/ro
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Acesta este planul proiectului pentru partea FreeCAD a [Development roadmap](Development_roadmap.md).

## Scop și principii 

Pentru a îmbunătăți capabilitățile multi limbaj în FreeCAD prin implementarea suportului pentru caractere UTF în interiorul interfaței Coin3D .

În ciuda faptului că Coin3D se mișcă acum spre o platformă mult mai deschisă dezoltării, este încă foarte dificil să se contribuie la acest proiect.

(mrlukeparry) Nu am primit încă un răspuns în ceea ce privește contribuția înapoi și, pentru moment, pare mai adecvată păstrarea acestui aspect în cadrul proiectului FreeCAD și ar însemna că putem lăsa utilizatorii să testeze fără a necesita versiuni de dezvoltare ale programului Coin3D. Mi-aș dori să realizez acest lucru cu 0,14, considerând că este o mare prioritate pentru creșterea accesibilității FreeCAD la utilizatorii non-englezi.

## Organizare

-   Prezintă un șir UTF de bază independent de bibliotecile principale STL, cu excepția caracteristicilor de manipulare.
-   Implementează câmpurile Coin3D și nodurile de text 3D pentru administra stocajul noilor date UTF.
-   Migrază modulele pentru a utiliza noile noduri textuale.
-   Testarea riguroasă

## Viitoarele acțiuni 

-   Implementarea clasei UTF String Handling Class **(WIP)**
-   Manipularea fonturilor și a simbolurilor/glifurilor.
-   Implementarea câmpurile și nodurile de text Coin3D pentru utilizare în proiect
-   Migrarea modulele utilizând SoText2 și SoText3 pentru a utiliza noduri noi



_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > UTF Project/ro
