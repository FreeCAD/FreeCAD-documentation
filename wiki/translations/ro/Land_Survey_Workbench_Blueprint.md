# Land Survey Workbench Blueprint/ro




{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{VeryImportantMessage|Important note: The Land Survey Workbench has been abandoned. If there are interested developers who want to spearhead it, please let us know on the forum}}


{{TOCright}}

Această pagină enumeră cerințele și implementarea pentru un nou atelier de lucru utilizabil în domeniul [Land Survey](http://en.wikipedia.org/wiki/Land_survey). Pagina este puțin depășită. Găsiți cele mai recente informații pentru FreeCAD în această privință pe un subiect Enerm pe forum :<http://forum.freecadweb.org/viewtopic.php?f=8&t=6973>

## Selecția Rectangulară 

> Este posibil să fie necesar un nou mod mouse:
>
> -   clic stânga pe un obiect selectează obiectul
> -   clic stânga în spațiul gol; - începeți acțiunea de selectare; clic din nou - acțiunea de selecție finală, adăugați la setul de selecție
>     -   CTRL - excludeți din setul deja selectat
> -   țineți apăsat butonul din mijloc pentru a panorama
> -   meniu contextual sau right click
> -   rotiță sus/jos - zoom

## Straturi

-   Proprietățile obiectului, cum ar fi culoarea, grosimea liniei, transparența, capacitatea de imprimare pot fi setate pe bază de obiecte sau pot fi moștenite de la stratul părinte.
-   Fiecare obiect are un strat părinte / un obiect poate face parte dintr-un strat sau nu.

## Blocuri

Blocurile sunt obiecte care se comportă în majoritatea cazurilor ca un singur obiect. Obiectele nu își pierde individualitatea în interiorul blocului.

> Deoarece există o actualizare / downgrade, această funcție poate fi deja prezentă.

### Atribute Dinamice 

Variabile. Componente ale blocului care pot fi modificate fără modificarea definiției blocului. Poziția în interiorul blocului este un astfel de atribut.

> Această caracteristică se va integra bine dacă este exprimată la proprietăți.

## Puncte

În cadstru de teren punctele sunt de obicei asociate cu numere, descriere și alte caracteristici.

> Blocurile cu proprietăți dinamice ar trebui să o facă.

## Querry tools for 2 and a half system 

Poziția plană este de obicei decuplată (în special în aplicațiile de cadastru) de la înălțime.Când doriți să cunoașteți distanța dintre două puncte, doriți să aflați distanța în proiecția orizontală. Planul orizontal este XY, Y indicând spre nord. Z punctează în sus (altitudine pozitivă).

## Rich text; Tabele 

Suport general pentru rich text.

Notă: informațiile din această pagină se bazează pe o înțelegere superficială a internelor FreeCAD. Odată ce acesta aprofundează cerințele, punerea în aplicare poate fi ajustată. Contribuțiile sunt binevenite!\--[Xtnickx](User:Xtnickx.md) 11:00, 26 January 2013 (UTC)



[Category:Roadmap](Category:Roadmap.md) [Category:Developer](Category:Developer.md)
