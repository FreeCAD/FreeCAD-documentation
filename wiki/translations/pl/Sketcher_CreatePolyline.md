---
- GuiCommand:/pl
   Name:Sketcher CreatePolyline
   Name/pl:Szkicownik: Utwórz polilinię
   MenuLocation:Szkic → Elementy geometryczne szkicownika → Utwórz polilinię
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**G** **M**
   SeeAlso:[Szkicownik: Linia](Sketcher_CreateLine/pl.md)
---

# Sketcher CreatePolyline/pl



## Opis

To narzędzie działa podobnie jak narzędzie [Utwórz linię](Sketcher_CreateLine/pl.md), ale tworzy ciągłe odcinki linii i łuków połączone wierzchołkami. Po uruchomieniu narzędzia kursor myszki zmienia kształt na biały krzyż z czerwoną ikoną polilinii. Oprócz niego na niebiesko w czasie rzeczywistym wyświetlane są współrzędne kursora.

![](images/Sketcher_PolylineExample1.png )



*Polilinia zaczynała się od linii, łuku stycznego, łuku prostopadłego następnie linii stycznej.*



## Użycie

Polilinia zawsze zaczyna się od odcinka prostego: kliknij - przesuń kursor myszki - kliknij. Przesuń kursor ponownie. Po umieszczeniu pierwszego segmentu linii, narzędzie polilinia Szkicownika posiada wiele trybów, które można przełączać za pomocą klawisza **M**. Można na przykład rysować łuki styczne lub prostopadłe do linii lub segmentu łuku. Powtórne naciśnięcie klawisza **M** przełącza te różne tryby:

1.  Naciśnij klawisz **M**: nowy odcinek jest prostą prostopadłą do poprzedniego odcinka.
2.  Naciśnij ponownie klawisz **M**: nowy odcinek jest linią styczną do poprzedniego odcinka.
3.  Naciśnij ponownie klawisz **M**: nowy odcinek jest łukiem, który jest styczny do poprzedniego odcinka.
4.  Naciśnij ponownie klawisz **M**: nowy odcinek jest łukiem prostopadłym (w lewo) do poprzedniego odcinka.
5.  Naciśnij ponownie klawisz **M**: nowy odcinek jest łukiem prostopadłym (w prawo) do poprzedniego odcinka.
6.  Naciśnij ponownie klawisz **M**: Znów znajdujesz się w stanie, w którym zacząłeś. Linia jest połączona tylko przypadkiem z poprzednim odcinkiem.

-    {{VersionPlus/pl|0.18}}Podczas pracy w dowolnym trybie łuku, przytrzymanie klawisza **Ctrl** *(MacOS: **CMD**)* i przesuwanie kursora powoduje, że łuk jest przyciągany co 45 stopni, względem wcześniej utworzonego odcinka polilinii.

-   Wybierz punkty na pustym obszarze okna widoku 3D lub na istniejącym obiekcie *(automatyczne wiązania muszą być aktywne w TaskView)*.

-   Naciśnięcie klawisza **Esc** lub kliknięcie prawym przyciskiem myszki *przed* zamknięciem polilinii w pętlę kończy bieżącą polilinię i można kontynuować z nową. Naciśnięcie klawisza **Esc** lub ponowne kliknięcie prawego przycisku myszy kończy działanie narzędzia polilinii.

-   Naciśnięcie klawisza **Esc** lub kliknięcie prawego przycisku myszy *po* zamknięciu polilinii do pętli kończy działanie narzędzia polilinii.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/pl
