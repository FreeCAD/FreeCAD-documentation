# Units project/ro
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Acesta este un proiect în FreeCAD. Aceasta respectă regulile din \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\] . Proiectele sunt colectate în [Development roadmap](Development_roadmap.md).

## Scopuri și principii 

Acesta este un cadru de dezvoltare software pentru FreeCAD.

Pașii de dezvoltare sunt planificați aici (acțiunile următoare) și sunt urmăriți în sistemul de urmărire a problemelor pentru a obține un jurnal de schimburi bine format: [Issue tracker](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)

## Rezultat

Acesta va permite FreeCAD să se ocupe de sistemele de măsurare prin cablu, cum ar fi sistemul imperial și unitățile complexe [SI](http://en.wikipedia.org/wiki/International_System_of_Units). De asemenea, să se ocupe de formatele de import / export care pot transporta Unități (cum ar fi STEP). Și permiteți scalarea pe baza ipotezelor de unități (mm-\> m, m-\> in).

## Brainstorming

O mulțime de discuții au fost făcute aici: <http://forum.freecadweb.org/viewtopic.php?f=10&t=1616>

Și multe informații pe care le veți găsi în articolul [ Units](Units.md).

## Organizare

### Actualizarea analizorului sintatic (parser) de unități de măsură 

Actualizarea parserului pentru a gestiona și a genera semnături așa cum este discutat în articolul [ Units](Units.md).

### Proprietăți

Schimbați proprietățile de ex din PropertyLength în PropertyUntit cu o semnătură a unității de măsurare.

În cele din urmă un editor de proprietate pentru PropertyUntit.

### Ateliere

-   Actualizarea Atelierelor de lucru pentru a utiliza cadrul unităților de măsură. Aș începe cu Sketcher și PartDesign și du-te mai departe \...
-   Documentarea procesului de actualizare, astfel încât alți oameni să poată face același lucru cu alte ateliere de lucru -_ 13:13, 28 November 2011 (UTC)

## Umătorii pași 

-   Upgradarea analizorului sintactic (parser) a unităților de măsură (jriegel)



_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > Units project/ro
