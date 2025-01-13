---
 GuiCommand:
   Name: PartDesign Revolution
   Name/pl: Projekt Części: Wyciągnij przez obrót
   MenuLocation: Projekt Części , Utwórz cechę przez dodanie , Wyciągnij przez obrót
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: PartDesign_Groove/pl
---

# PartDesign Revolution/pl



## Opis

Narzędzie **Wyciągnij przez obrót** tworzy bryłę poprzez obrót wybranego szkicu lub obiektu 2D wokół określonej osi.

![](images/PartDesign_Revolution_example.svg )



*Powyżej: szkic ''(A)'' jest obracany o 270 stopni w kierunku przeciwnym do ruchu wskazówek zegara wokół osi ''(B)'', wynikowa bryła ''(C)'' jest pokazana po prawej stronie.*



## Użycie

1.  Wybierz pojedynczy szkic lub jedną lub więcej powierzchni z Zawartości.
2.  Naciśnij przycisk **<img src="images/PartDesign_Revolution.svg" width=24px> '''Wyciągnij przez obrót'''**.
3.  Ustaw parametry wyciągnięcia, patrz sekcja [Opcje](#Opcje.md) poniżej.
4.  Naciśnij przycisk **OK**.



## Opcje

Podczas tworzenia wyciągnięcia lub po dwukrotnym kliknięciu istniejącego obiektu wyciągnięcia w oknie [Widoku drzewa](Tree_view/pl.md), wyświetlany jest panel zadań **Parametry wyciągnięcia przez obrót**. Oferuje on następujące ustawienia:

\| ![](images/partdesign_revolution_parameters.png )



### Typ


{{Version/pl|0.22}}

Typ oferuje pięć różnych sposobów określania wyciągnięcia przez obrót:



#### Wymiar

Wprowadź wartość liczbową dla **Kąta** obrotu. Z opcją *\'Symetrycznie do płaszczyzny* wyciągnięcie przez obrót będzie rozciągć się o połowę podanego kąta po obu stronach szkicu lub powierzchni.



#### Do ostatniego 

Wyciągnięcie przez obrót rozciągnie się do ostatniej powierzchni podpory, którą napotka w swoim kierunku. Jeśli nie ma podpory, pojawi się komunikat o błędzie.



#### Do pierwszego 

Wyciągnięcie przez obrót zostanie wykonane do pierwszej powierzchni podpory napotkanej w danym kierunku. W przypadku braku podpory pojawi się komunikat o błędzie.



#### Do powierzchni 

Wyciągnięcie przez obrót rozszerzy się do powierzchni. Naciśnij przycisk **Ściana** i wybierz ścianę lub [datum plane/pl\|płaszczyzna odniesienia](PartDesign_Plane.md) z listy Zawartości.



#### Dwa wymiary 

Umożliwia to wprowadzenie drugiego kąta, w którym wyciągnięcie przez obrót powininno rozciągać się w przeciwnym kierunku. Kierunki można przełączać, zaznaczając opcję **Odwrócony**.



### Oś

Określa oś obrotu:

-   **Pionowa oś szkicu**: wybiera pionową oś szkicu.
-   **Pozioma oś szkicu**: wybiera poziomą oś szkicu.
-   **Linia konstrukcyjna**: wybiera linię konstrukcyjną ze szkicu używanego przez wyciągnięcie. Lista rozwijana będzie zawierać pozycję dla każdej linii konstrukcyjnej. Pierwsza linia konstrukcyjna będzie oznaczona jako *Linia konstrukcyjna 1*.
-   **Oś bazowa (X/Y/Z)**: wybiera oś X, Y lub Z odniesienia położenia bryły.
-   **Wybierz odniesienie \...**: umożliwia wybór prostej krawędzi lub [linii odniesienia](PartDesign_Line/pl.md) z obiektu Zawartości.

Należy pamiętać, że podczas zmiany osi opcja **Odwrócony** może zostać *(nie)*zaznaczona automatycznie.



### Kąt

Określa kąt obrotu. Ta opcja jest dostępna tylko wtedy, gdy *Typ* to **Wymiar** lub **Dwa wymiary**. Kąty większe niż 360° nie są dostępne. Wartości ujemne również nie są dostępne, zamiast nich należy użyć opcji **Odwrócony**.



### Symetrycznie do płaszczyzny 

Zaznacz tę opcję, aby rozszerzyć obrót o połowę podanego kąta na dowolną stronę szkicu lub powierzchni. Ta opcja jest dostępna tylko wtedy, gdy **Typ** to **Wymiar**.



### Odwrócony

Odwraca kierunek wyciągnięcia.



### Drugi kąt 


{{Version/pl|1.0}}

Określa kąt wyciągnięcia przez obrót w przeciwnym kierunku. Ta opcja jest dostępna tylko wtedy, gdy **Typ** to **Dwa wymiary**, a **Kąt** jest mniejszy niż 360°.



## Właściwości



### Dane


{{TitleProperty|Projekt Części}}

-    **Ulepsz|Bool**
    


{{TitleProperty|Wyciągnięcie przez obrót}}

-    **Typ|Enumeration**
    

-    **Baza|Vector**: (read-only)

-    **Oś|Vector**: (read-only)

-    **Kąt|Angle**
    

-    **Do powierzchni|LinkSub**
    

-    **Kąt2|Angle**
    

-    **Oś odniesienia|LinkSub**
    


{{TitleProperty|Szkic bazowy}}

-    **Profil|LinkSub**
    

-    **Płaszczyzna pośrednia|Bool**
    

-    **Odwrócony|Bool**
    

-    **Zezwalaj na wiele ścian|Bool**
    



## Uwagi

-   Narzędzie <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [Łącznik kształtu](PartDesign_ShapeBinder/pl.md) nie może być użyte dla profilu.
-   Podczas korzystania z narzędzia <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md) dla profilu, wybranie spoiwa w oknie [widoku drzewa](Tree_view/pl.md) nie powiedzie się, zamiast tego powierzchnia wiążąca musi zostać wybrana w oknie [widoku 3D](3D_view/pl.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/pl
