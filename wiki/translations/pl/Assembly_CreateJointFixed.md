---
 GuiCommand:
   Name: Assembly CreateJointFixed
   Name/pl: Złożenie Utwórz połączenie stałe
   MenuLocation: Złożenie , Utwórz połączenie stałe
   Workbenches: Assembly_Workbench/pl
   Shortcut: **F**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointFixed/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateJointFixed.svg  style="width:24px;"> [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl.md) tworzy połączenie blokujące dwie części złożenia razem, zapobiegając jakimkolwiek przesunięciom i obrotom.



## Użycie

1.  Opcjonalnie wybierz dwa obiekty geometryczne należące do dwóch różnych części. Inne wskazania będą odrzucane.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateJointFixed.svg" width=16px> [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl.md)**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_CreateJointFixed.svg" width=16px> Utwórz połączenie stałe** z menu.
    -   Użyj skrótu: **F**.
3.  Wcześniej wybrane części zostaną przesunięte do zetknięcia się ich wskazanych obiektów geometrycznych.
4.  Okno dialogowe **Utwórz połączenie** zostanie otwarte w [panelu zadań](Task_panel/pl.md), wymieniając wcześniej wskazane obiekty.
5.  Opcjonalnie zmień typ połączenia na liście rozwijanej:
    -   Wybierz **Stałe**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne.
        2.  Części zostaną przesunięte do zetknięcia się ich wskazanych obiektów geometrycznych.
        3.  Opcjonalnie wprowadź wartość *Odsunięcie*.
        4.  Opcjonalnie wprowadź wartość *Obrót*.
        5.  Opcjonalnie wciśnij przycisk **<img src="images/Button_sort.svg" width=16px>** aby zmienić kierunek połączenia.
    -   Wybierz **Obrotowe**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne.
        2.  Części zostaną przesunięte do zetknięcia się ich wskazanych obiektów geometrycznych.
        3.  Opcjonalnie wprowadź wartość *Odsunięcie*.
        4.  Opcjonalnie wciśnij przycisk **<img src="images/Button_sort.svg" width=16px>** aby zmienić kierunek połączenia.
        5.  Opcjonalnie zaznacz opcję **Kąt minimalny** i wprowadź wartość.
        6.  Opcjonalnie zaznacz opcję **Kąt maksymalny** i wprowadź wartość.
    -   Wybierz **Cylindryczne**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne.
        2.  Opcjonalnie wciśnij przycisk **<img src="images/Button_sort.svg" width=16px>** aby zmienić kierunek połączenia.
        3.  Opcjonalnie zaznacz opcję **Długość minimalnie** i wprowadź wartość.
        4.  Opcjonalnie zaznacz opcję **Długość maksymalnie** i wprowadź wartość.
        5.  Opcjonalnie zaznacz opcję **Kąt minimalny** i wprowadź wartość.
        6.  Opcjonalnie zaznacz opcję **Kąt maksymalny** i wprowadź wartość.
    -   Wybierz **Przesuwne**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne.
        2.  Opcjonalnie wprowadź wartość *Obrót*.
        3.  Opcjonalnie wciśnij przycisk **<img src="images/Button_sort.svg" width=16px>** aby zmienić kierunek połączenia.
        4.  Opcjonalnie zaznacz opcję **Długość minimalnie** i wprowadź wartość.
        5.  Opcjonalnie zaznacz opcję **Długość maksymalnie** i wprowadź wartość.
    -   Wybierz **Przegub kulowy**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne.
    -   Wybierz **Odległość**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne.
        2.  Opcjonalnie wprowadź wartość *Odległość*.
        3.  Opcjonalnie wciśnij przycisk **<img src="images/Button_sort.svg" width=16px>** aby zmienić kierunek połączenia.
    -   Wybierz **Równoległe**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne.
        2.  Opcjonalnie wciśnij przycisk **<img src="images/Button_sort.svg" width=16px>** aby zmienić kierunek połączenia.
    -   Wybierz **Prostopadłe**.
        1.  If the selection list is empty: select two geometric entities.
    -   Select **Angle**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne.
        2.  Opcjonalnie wprowadź wartość *Kąt*.
    -   Wybierz **Przekładnia zębata**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne należące do dwóch różnych części, które wcześniej zostały użyte do zdefiniowania połączeń typu Przesuwne i Obrotowe. *(kierunek i oś obrotu połączenia przesuwnego muszą być prostopadłe)*
        2.  Opcjonalnie wprowadź wartość *Promień skoku*.
    -   Wybierz **Śruba**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne należące do dwóch różnych części, które wcześniej zostały użyte do zdefiniowania połączeń typu Przesuwne i Obrotowe. *(kierunek i oś obrotu połączenia przesuwnego muszą być równoległe)*
        2.  Opcjonalnie wprowadź wartość *Promień skoku*.
    -   Wybierz **Koła zębate**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne należące do dwóch różnych części, które wcześniej zostały użyte do zdefiniowania dwóch różnych połączeń typu Obrotowe.
        2.  Opcjonalnie wprowadź wartość *Promień 1*.
        3.  Opcjonalnie wprowadź wartość *Promień 2*.
        4.  Opcjonalnie zaznacz/odznacz opcję **Obroty w przeciwnym kierunku**. *(odznaczenie wybiera opcję **Pas**)* - nie działa w wersji 1.0 RC póki co
    -   Wybierz **Pas**.
        1.  Jeśli lista wskazań jest pusta: wybierz dwa obiekty geometryczne należące do dwóch różnych części, które wcześniej zostały użyte do zdefiniowania dwóch różnych połączeń typu Obrotowe.
        2.  Opcjonalnie wprowadź wartość *Promień 1*.
        3.  Opcjonalnie wprowadź wartość *Promień 2*.
        4.  Opcjonalnie zaznacz/odznacz opcję **Obroty w przeciwnym kierunku**. *(zaznaczenie wybiera opcję **Koła zębate**)* - nie działa w wersji 1.0 RC póki co
6.  Części zostaną przesunięte do zetknięcia się ich wskazanych obiektów geometrycznych.
7.  Wciśnij przycisk **OK** aby zakończyć używanie narzędzia.



## Uwagi

-   Połączenie stałe można wykorzystać jako siłownik do kontroli ruchu w symulacji kinematycznej. Użycie kółka myszy w panelu zadań natychmiast przestawia połączone części.
    -   Odsunięcie działa wzdłuż jego lokalnej osi Z, ujemne wartości są akceptowane.
    -   Obrót działa wokół jego lokalnej osi, kąty \> 360° a nawet ujemne są akceptowane.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Fixed** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Ma też następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Joint}}

-    **Activated|Bool**: Wskazuje czy połączenie jest aktywne.

-    **Distance|Float**: Przechowuje **Odległość** połączenia typu Odległość. Jest też używana przez połączenia Przekładnia zębate i Śruba do przechowywania **Promienia skoku** i przez połączenia Koła zębate oraz Pas do przechowywania **Promienia 1**.

-    **Distance2|Float**: Druga odległość połączenia. Używana tylko przez połączenia Koła zębate i Pas do przechowywania **Promienia 2**.

-    **Joint Type|Ennumeration**: Typ połączenia. ({{Value|Fixed}}, {{Value|Revolute}}, {{Value|Cylindrical}}, {{Value|Slider}}, {{Value|Ball}}, {{Value|Distance}}, {{Value|Parallel}}, {{Value|Perpendicular}}, {{Value|Angle}}, {{Value|RackPinion}}, {{Value|Screw}}, {{Value|Gears}}, {{Value|Belt}})

Usunięte właściwości (v.1.0.0-RC-38728) To były właściwości, których można było użyć do tworzenia animacji:

-    **Offset|Vector**: Wektor odsunięcia połączenia.

-    **Rotation|Float**: Obrót połączenia.


{{TitleProperty|Joint Connector 1}}

-    **Detach1|Bool**: Zapobiega ponownemu przeliczaniu właściwości placement1, umożliwiając własne pozycjonowanie.

-    **Offset1|Placement**: To odsunięcie mocowania pierwszego łącznika połączenia. (dodane w v.1.0.0-RC-38728)

-    **Placement1|Placement**: To jest lokalny układ współrzędnych w obrębie obiektu reference1, który będzie używany dla połączenia.

-    **Reference1|XlinkSubHidden**: Pierwsze odniesienie połączenia.

Usunięte właściwości:

-    **Element1|String**: Wskazany element pierwszego obiektu.

-    **Object1|String**: Pierwszy obiekt połączenia.

-    **Part1|Link**: Pierwsza część w połączeniu.

-    **Vertex1|String**: Wskazany wierzchołek pierwszego obiektu.


{{TitleProperty|Joint Connector 2}}

-    **Detach2|Bool**: Zapobiega ponownemu przeliczaniu właściwości placement2, umożliwiając własne pozycjonowanie.

-    **Offset2|Placement**: To odsunięcie mocowania drugiego łącznika połączenia. (dodane w v.1.0.0-RC-38728)

-    **Placement2|Placement**: To jest lokalny układ współrzędnych w obrębie obiektu reference2, który będzie używany do połączenia.

-    **Reference2|XlinkSubHidden**: Drugie odniesienie połączenia.

Usunięte właściwości:

-    **Element2|String**: Wskazany element drugiego obiektu.

-    **Object2|String**: Drugi obiekt połączenia.

-    **Part2|Link**: Druga część w połączeniu.

-    **Vertex2|String**: Wskazany wierzchołek drugiego obiektu.


{{TitleProperty|Limits}}

-    **Angle Max|Float**: Maksymalny limit dla kąta pomiędzy układami współrzędnych (ich osiami X).

-    **Angle Min|Float**: Minimalny limit dla kąta pomiędzy układami współrzędnych (ich osiami X).

-    **Enable Angle Max|Bool**: Włącz ograniczenie maksymalnego kąta tego połączenia.

-    **Enable Angle Min|Bool**: Włącz ograniczenie minimalnego kąta tego połączenia.

-    **Enable Length Max|Bool**: Włącz ograniczenie maksymalnej długości tego połączenia.

-    **Enable Length Min|Bool**: Włącz ograniczenie minimalnej długości tego połączenia.

-    **Length Max|Float**: Maksymalny limit odległości między oboma układami współrzędnych *(wzdłuż ich osi Z)*.

-    **Length Min|Float**: Minimalny limit odległości między oboma układami współrzędnych *(wzdłuż ich osi Z)*.

Usunięta właściwość:

-    **Enable Limits|Bool**: Czy to połączenie korzysta z ograniczeń?





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointFixed/pl
