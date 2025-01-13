---
 GuiCommand:
   Name: PartDesign Groove
   Name/pl: Projekt Części: Rowek
   MenuLocation: Projekt Części , Utwórz cechę przez odjęcie , Rowek
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: PartDesign_Revolution/pl
---

# PartDesign Groove/pl



## Opis

Narzędzie **Rowek** obraca wybrany szkic lub profil wokół danej osi, wycinając materiał z podpory.

![](images/PartDesign_Groove_example.svg )



*Powyżej: szkic ''(A)'' jest obracany wokół osi ''(B)''. Wynikowy rowek na bryle ''(C)'' jest pokazany po prawej stronie.*



## Użycie

1.  Wybierz pojedynczy szkic lub jedną lub więcej powierzchni na istniejącej bryle.
2.  Naciśnij przycisk **<img src="images/PartDesign_Groove.svg" width=16px> '''Rowek'''**.
3.  Ustaw parametry wyżłobienia, patrz sekcja [Opcje](#Opcje.md) poniżej.
4.  Naciśnij przycisk **OK**.



## Opcje

Podczas tworzenia rowka lub po dwukrotnym kliknięciu istniejącego rowka w oknie [Widok drzewa](Tree_view/pl.md) wyświetlany jest panel zadań **Parametry rowka**. Oferuje on następujące ustawienia:

\| ![](images/partdesign_groove_parameters.png )



### Typ


{{Version/pl|1.0}}

Typ oferuje pięć różnych sposobów określania kąta rowka:



#### Wymiar

Podaj wartość numeryczną dla **Kąta** rowka. W przypadku opcji **Symetryczne do płaszczyzny** rowek będzie rozszerzony o połowę podanego kąta na obie strony względem szkicu lub powierzchni.



#### Przez wszystkie 

Rowek będzie rozciągał się do ostatniej powierzchni podpory, którą napotka w swoim kierunku. Z opcją **Symetrycznie do płaszczyzny** rowek będzie przecinał cały materiał w obu kierunkach.



#### Do pierwszego 

Rowek będzie sięgać do pierwszej powierzchni podpory, którą napotka w swoim kierunku.



#### Do powierzchni 

Rowek będzie rozciągał się aż do powierzchni. Naciśnij przycisk **Ściana** i wybierz powierzchnię lub [płaszczyzna odniesienia](PartDesign_Plane/pl.md) z listy Zawartości.



#### Dwa wymiary 

Umożliwia to wprowadzenie drugiego kąta, w którym rowek powinien rozciągać się w przeciwnym kierunku. Kierunki można przełączać, zaznaczając opcję **Odwrócony**.



### Oś

Określa oś rowka:

-   **Pionowa oś szkicu**: wybiera pionową oś szkicu.
-   **Pozioma oś szkicu**: wybiera poziomą oś szkicu.
-   **Linia konstrukcyjna**: wybiera linię konstrukcyjną ze szkicu używanego przez rowek. Lista rozwijana będzie zawierać pozycję dla każdej linii konstrukcyjnej. Pierwsza linia konstrukcyjna będzie oznaczona jako *Linia konstrukcyjna 1*.
-   **Oś bazowa (X/Y/Z)**: wybiera oś X, Y lub Z odniesienia położenia bryły.
-   **Wybierz odniesienie \...**: umożliwia wybór prostej krawędzi lub [linii odniesienia](PartDesign_Line/pl.md) z obiektu Zawartości.

Należy pamiętać, że podczas zmiany osi opcja **Odwrócony** może zostać *(nie)*zaznaczona automatycznie.



### Kąt

Określa kąt rowka. Ta opcja jest dostępna tylko wtedy, gdy **Typ** to **Wymiar** lub **Dwa wymiary**. Kąty większe niż 360° nie są dostępne. Wartości ujemne również nie są dostępne, zamiast nich należy użyć opcji **Odwrócony**.



### Symetrycznie do płaszczyzny 

Zaznacz tę opcję, aby rozszerzyć rowek o połowę podanego kąta po obu stronach szkicu lub powierzchni, jeśli **Typ** to **Wymiar**, lub **Przez wszystkie**, jeśli taki jest **Typ**.



### Odwrócony

Odwraca kierunek rowka.



### Drugi kąt 


{{Version/pl|1.0}}

Określa kąt rowka w przeciwnym kierunku. Ta opcja jest dostępna tylko wtedy, gdy **Typ** to **Dwa wymiary**, a **Kąt** jest mniejszy niż 360°.



## Właściwości



### Dane


{{TitleProperty|Rowek}}

-    **Typ|Enumeration**
    

-    **Baza|Vector**: (read-only)

-    **Oś|Vector**: (read-only)

-    **Kąt|Angle**
    

-    **Kąt2|Angle**
    

-    **Do powierzchni|LinkSub**
    

-    **Oś odniesienia|LinkSub**
    


{{TitleProperty|Projekt Części}}

-    **Ulepsz|Bool**
    


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
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/pl
