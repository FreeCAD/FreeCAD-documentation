---
 GuiCommand:
   Name: Part Loft
   Name/pl: Part: Wyciągnij po profilach
   MenuLocation: Część , Wyciągnięcie po profilach...
   Workbenches: Part_Workbench/pl
   Version: 0.13
   SeeAlso: Part_Sweep/pl
---

# Part Loft/pl



## Opis

Polecenie <img alt="" src=images/Part_Loft.svg  style="width:24px;"> **Wyciągnięcie przez profile** tworzy ścianę, powłokę lub bryłę z dwóch lub więcej profili (przekrojów).

<img alt="" src=images/Part_Loft_solid_ruled_from3profiles_example_FreeCAD_0_13.jpg  style="width:400px;"> 
*Obiekt wyciągnięcia przez profile z trzech profili, które są dwoma [okręgami](Part_Circle/pl.md) i jedną [elipsą](Part_Ellipse/pl.md). Parametry to: Utwórz bryłę "Zaznaczone" i Powierzchnia prostokreślna "Zaznaczone".*



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Loft.svg" width=16px> [Wyciągnięcie przez profile ...](Part_Loft/pl.md)**.
    -   Wybierz opcję z menu **Część → <img src="images/Part_Loft.svg" width=16px> Wyciągnięcie przez profile ...**.
2.  Otworzy się [Panel zadań](Task_panel/pl.md) Wyciągnięcie przez profile.
3.  Na liście *Dostępne profile* po lewej stronie wybierz pierwszy profil i kliknij strzałkę w prawo, aby umieścić go na liście *Wybrane profile* po prawej stronie.
4.  Powtórz tę czynność dla drugiego profilu i kolejnych, jeśli wymagane są więcej niż dwa profile.
5.  Opcjonalnie użyj strzałek w górę i w dół, aby zmienić kolejność wybranych profili.
6.  Zdefiniuj opcje [Utwórz bryłę](#Dane.md), [Powierzchnia prostokreślna](#Dane.md) i [Zamknięty](#Dane.md).
7.  Kliknij **OK**.



### Akceptowana geometria 

-   **Profile**: mogą być punktem *(wierzchołkiem)*, linią *(krawędzią)*, konturem lub ścianą. Krawędzie i kontury mogą być otwarte lub zamknięte. Istnieją różne [ograniczenia](#Ograniczenia.md), patrz poniżej.

-   Obiekty typu [łącze](App_Link/pl.md) powiązane z odpowiednimi typami obiektów oraz kontenery typu [Część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako profile. {{Version/pl|0.20}}



## Opcje



#### Utwórz bryłę 

Jeśli opcja **Utwórz bryłę** ma wartość {{True/pl}}, FreeCAD utworzy bryłę pod warunkiem, że profile są zamknięte. Jeśli wartością jest {{False/pl}}, FreeCAD utworzy ścianę lub powłokę dla profili otwartych lub zamkniętych.



#### Powierzchnia prostokreślna 

Jeśli *Powierzchnia prostokreślna* ma wartość {{true/pl}}, FreeCAD tworzy powierzchnię, powłokę lub bryłę z [powierzchni prostokreślnych](http://en.wikipedia.org/wiki/Ruled_surface).



#### Zamknięty

Jeśli parametr \"Zamknięty\" ma wartość {{true/pl}}, FreeCAD próbuje połączyć ostatni profil z pierwszym profilem, aby utworzyć zamkniętą figurę.

Więcej informacji na temat sposobu łączenia profili można znaleźć na stronie [Szczegóły techniczne wyciągnięcia przez profile](Part_Loft_Technical_Details/pl.md).



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Wyciągnięcia przez profile** wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Wyciągnięcie przez profile}}

-    **Profile|LinkList**: lista używanych profili.

-    **Bryła|Bool**: przyjmuje wartości {{true/pl}} lub {{false/pl}} *(domyślnie)*. Wartość true określa utworzenie bryły.

-    **Powierzchnia prostokreślna|Bool**: {{true/pl}} lub {{false/pl}} *(domyślnie)*. True tworzy powierzchnię prostokreślną.

-    **Zamknięty|Bool**: {{true/pl}} lub {{false/pl}} *(domyślnie)*. True tworzy obiekt zamknięty poprzez połączenie profilu ostatniego z pierwszym.

-    **Maksymalnie stopni|IntegerConstraint**: ilość stopni maksymalnie.



## Ograniczenia

Funkcja Wyciągnięcie przez profile ma takie same ograniczenia jak [Przeciągnięcie wzdłuż ścieżki](Part_Sweep/pl#Ograniczenia.md).



### Opcja Zamknięty 

-   Wyniki aktywnej opcji *Zamknięty* dla funkcji wyciągnięcia przez profile mogą generować nieoczekiwane rezultaty - wyciągnięcie może się skręcać lub załamywać. Wyciąganie jest bardzo wrażliwe na rozmieszczenie profili i złożoność krzywych wymaganych do połączenia odpowiednich wierzchołków we wszystkich profilach.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Loft/pl
