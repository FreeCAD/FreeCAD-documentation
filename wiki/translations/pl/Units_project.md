# Units project/pl
**
Ten plan jest prawdopodobnie nieaktualny. Więcej informacji można znaleźć na stronie [Plan rozwoju](Development_roadmap.md).<br>
Jeśli nie jesteś zaangażowany w rozwój, o którym tutaj mowa:<br>
PROSZĘ NIE EDYTOWAĆ ANI NIE TŁUMACZYĆ !!!
**


{{TOCright}}

Ten projekt ma na celu wdrożenie porządnego systemu jednostek w programie FreeCAD. Jest on zgodny z zasadami procesu \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Realizacja zadań\]. Projekty są zebrane w [Planie rozwoju](Development_roadmap/pl.md).

## Cel i zasady 

Jest to projekt programistyczny mający na celu zaimplementowanie systemu jednostek do programu FreeCAD.

Kroki rozwoju *(następne działania)* są zaplanowane tutaj, i śledzone w systemie śledzenia problemów, aby uzyskać dobrze uformowany dziennik zmian: [Issue tracker](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)

## Rezultat

Umożliwi to programowi FreeCAD obsługę połączonych systemów miar, takich jak system imperialny i złożone jednostki [SI](http://en.wikipedia.org/wiki/International_System_of_Units). Obsłuży również formaty importu/eksportu, które są w stanie transportować jednostki *(jak STEP)*. I pozwoli na skalowanie w oparciu o założenia jednostek *(mm-\>m, m-\>in)*.

## Burza mózgów 

Dużo dyskusji odbyło się tutaj: <http://forum.freecadweb.org/viewtopic.php?f=10&t=1616>

A wiele informacji znajdziesz w artykule [Jednostki](Units/pl.md).

## Organizowanie

### Uaktualnienie parsera jednostek 

Uaktualnienie parsera do obsługi i generowania podpisów, jak to zostało omówione w artykule [Jednostki](Units/pl.md).

### Właściwości

Zmiana formy właściwości np. \"Właściwości długości\" na \"Właściwości jednostek\" z sygnaturą jednostki.

Ostatecznie edytor właściwości dla \"Właściwości jednostek\".

### Środowiska pracy 

-   Ulepszanie środowisk pracy, aby używać frameworka Jednostek. Zacząłbym od środowiska Szkicownika i Projekt Części, a następnie poszedł dalej\...
-   Dokumentując proces aktualizacji, aby inni ludzie mogli zrobić to samo z innymi środowiskami \--_. 13:13, 28 listopad 2011 (UTC)

## Następne działania 

-   Uaktualnienie parsera jednostek *(jriegel)*



_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > Units project/pl
