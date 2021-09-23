# UTF Project/pl
**Ten plan jest prawdopodobnie nieaktualny. Więcej informacji można znaleźć na stronie [Plan rozwoju](Development_roadmap.md).<br>
Jeśli nie jesteś zaangażowany w rozwój, o którym tutaj mowa:<br>
PROSZĘ NIE EDYTOWAĆ ANI NIE TŁUMACZYĆ !!!
**


{{TOCright}}

Jest to plan projektu dla części programu FreeCAD w ramach [planu rozwoju](Development_roadmap.md).

## Przeznaczenie i zasady 

Poprawa możliwości wielojęzykowych w programie FreeCAD poprzez wdrożenie obsługi kodowania znaków **UTF** w ramach interfejsu Coin3D.

Pomimo tego, że Coin3D przechodzi obecnie na bardziej otwartą platformę rozwojową, nadal bardzo trudno jest wnieść swój wkład z powrotem do projektu.

*(mrlukeparry)* Nie otrzymałem jeszcze odpowiedzi w sprawie wkładu z powrotem i na razie wydaje się bardziej właściwe utrzymanie tego w ramach projektu FreeCAD i oznaczałoby to, że możemy pozwolić użytkownikom na testowanie bez konieczności używania deweloperskich wersji Coin3D. Zamierzam to osiągnąć do **0.14**, ponieważ jest to duży priorytet dla zwiększenia dostępności FreeCAD dla użytkowników nieanglojęzycznych.

## Organizowanie

-   Udostępnia podstawową funkcjonalność obsługi łańcuchów UTF, która jest niezależna od głównych bibliotek z wyjątkiem STL.
-   Zaimplementuj pola Coin3D i pola tekstowe 3D do obsługi nowego magazynu danych UTF.
-   Migruj moduły, aby używać nowych bloków tekstowych.
-   Rygorystyczne testy

## Kolejne działania 

-   Wdrożenie klasy obsługi ciągów UTF *(**WIP**)*.
-   Obsługa czcionek i glifów.
-   Wdrożenie pól tekstowych i pól Coin3D i węzłów do wykorzystania w projekcie.
-   Migruj moduły wykorzystujące SoText2 i SoText3 do wykorzystania nowych węzłów.



[Category:Roadmap](Category:Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category:Roadmap.md) > UTF Project/pl
