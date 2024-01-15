---
 GuiCommand:
   Name: FEM PostPipelineFromResult
   Name/pl: Prezentacja graficzna wyników
   MenuLocation: Wyniku , Prezentacja graficzna wyników
   Workbenches: FEM_Workbench/pl
   Version: 0.17
   SeeAlso: FEM_ResultShow/pl, FEM_tutorial/pl
---

# FEM PostPipelineFromResult/pl



## Opis

Obiekt prezentacji graficznej wyników tworzy nową graficzną reprezentację wyników analizy MES na badanej części. Dodaje skalę kolorów i opcje wyświetlania.



## Użycie

1.  Zaznacz obiekt wyników.
2.  Wciśnij przycisk **<img src="images/FEM_PostPipelineFromResult.svg" width=16px> '''Prezentacja graficzna wyników'''** lub wybierz opcję **Wyniki → <img src="images/FEM_PostPipelineFromResult.svg" width=16px> Prezentacja graficzna wyników** z menu.
3.  Nowy obiekt nazwany \"Pipeline\" zostanie dodany do analizy.
4.  Dwukrotnie kliknij nowy obiekt Pipeline w [widoku drzewa](Tree_view/pl.md) i wybierz tryb wyświetlania oraz pole wyników. Przykładowo, dla trybu {{Value|Powierzchnia}} i pola {{Value|Naprężenia von Mises}} obiekt prezentacji graficznej wyników wygląda następująco:

<img alt="" src=images/Pipeline.PNG  style="width:500px;">

Jeśli nie widzisz modelu w obszarze graficznym, użyj **Edycja → Preferencje → Wyświetlanie → Widok 3D → Renderowanie → Kolor podświetlenia**.

Jeśli korzystasz z pochodzącego od [układu SI](https://pl.wikipedia.org/wiki/Uk%C5%82ad_SI) [systemu jednostek](Preferences_Editor/pl#Jednostki.md), wartości na skali będą również oparte o jednostki SI. To oznacza, że przemieszczenia są w metrach, naprężenia w Paskalach a temperatura w Kelvinach.



## Właściwości



### Okno dialogowe 

Okno dialogowe obiektu prezentacji graficznej wyników ma następujące ustawienia:

-   **Tryb**: Jak wyświetlać wyniki. Możliwe tryby to
    -   **Kontur**: Kontur siatki wynikowej. Nie wyświetla wyników tylko brzegi siatki.
    -   **Węzły**: Węzły siatki wynikowej.
    -   **Powierzchnia**: To domyślny tryb, wyświetla powierzchnię siatki wynikowej.
    -   **Powierzchnia z krawędziami**: Jak **Powierzchnia**, ale z krawędziami elementów siatki.
-   **Pole**: Który wynik wyświetlać.
-   **Wektor**: Aktywne tylko jeśli **Pole** jest wektorem. Możesz wybrać czy wyświetlać *Wartość* (wypadkową) wektora czy jego składowe X, Y, Z.



### Skala

Jeśli dwukrotnie klikniesz na skali, zobaczysz to okno dialogoweː

![](images/SIMTUT_05.PNG )

i będziesz mógł zmodyfikować następujące ustawienia:

-   **Gradient**: Możesz wybrać odwróconą kolejność domyślnego graidentu kolorów, wariant *Red-White-Blue*, *Black-White* lub *White-Black*.
-   **Styl**: Domyślna opcja *Przepływ* używa pełnego zakresu gradientu kolorów. Opcja *Zero* używa tylko zakresu gradientu kolorów zaczynającego się od koloru, który wyświetlałby średnią wartość do maksimum.
-   **Widoczność**: Opcja *Deaktywuj* pokoloruje wszystkie węzły siatki, których wartości są poza podanym zakresem min/max na szaro. Opcja *Na zewnątrz przezroczysty* sprawi, że te węzły będą przezroczyste.
-   **Zakres parametru**: Wartości minimalne i maksymalne są wypełniane automatycznie. Możesz je zmodyfikować, ale upewnij się, że wiesz co robisz. Możesz również zmienić liczbę wyświetlanych miejsc dziesiętnych i liczbę etykiet rozłożonych w zakresie parametrów legendy.



### Edytor właściwości 

W [edytorze właściwości](Property_editor/pl.md) możesz zmienić w zakładce *Widok* ustawienia z okna dialogowego. W zakładce *Dane* możesz dodatkowo ustawić:

-    **Mode**: Jak filtry używane na obiekcie prezentacji graficznej wyników będą traktowane. Możliwe tryby to:

    -   **Serial**: W tym trybie każdy filtr bierze poprzedni filtr jako wejście. Kolejność jest więc kolejnością tworzenia filtrów. Pierwszy utworzony filtr bierze obiekt prezentacji graficznej wyników jako wejście. Jego właściwość **Input** jest więc pusta.
    -   **Parallel**: W tym trybie wszystkie filtry biorą obiekt prezentacji graficznej wyników jako wejście.
    -   **Custom**: {{Version/pl|0.20}} To jest domyślne ustawienie. Zachowuje wejście filtrów takie, jakie jest. Zatem pozwala mieć np. dwa filtry, które biorą obiekt prezentacji graficznej wyników jako wejście i trzeci, który bierze jeden z dwóch pozostałych filtrów jako wejście.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostPipelineFromResult/pl
