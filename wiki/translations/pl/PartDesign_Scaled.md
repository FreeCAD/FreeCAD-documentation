---
- GuiCommand:/pl
   Name:PartDesign Scaled
   Name/pl:Projekt Części: Skaluj
   MenuLocation:Brak ''(Opcja dostępna w menu Projekt Części → Zastosuj przekształcenie → Utwórz Transformację wielokrotną)''
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[Transformacja wielokrotna](PartDesign_MultiTransform/pl.md)
---

# PartDesign Scaled/pl



## Opis

Funkcja <img alt="" src=images/PartDesign_Scaled.svg  style="width:24px;"> **Skaluj** jest jedną z opcji transformacji narzędzia <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:16px;">. [Transformacji wielokrotnej](PartDesign_MultiTransform/pl.md). W przeciwieństwie do innych opcji, nie jest ona dostępna jako osobne narzędzie. Przekształca ona wynik transformacji w sekwencję przeskalowanych obiektów o równomiernie rozłożonych współczynnikach skali. Zaczynając od obiektu bazowego z poprzedniej transformacji, współczynnik skali wzrasta lub maleje, aż do osiągnięcia podanej wartości na ostatnim elemencie.

<img alt="" src=images/PartDesign_Scaled-01.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/PartDesign_Scaled-02.png  style="width:300px;"> 
*Wzorzec liniowy i biegunowy → Skalowanie wzorca liniowego z 3 krokami ''(wystąpieniami)'' i wzorca biegunowego z 12 krokami.*

Jeśli w obrębie elementu nie było wcześniejszego przekształcenia <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:16px;"> <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:16px;"> [Transformacji wielokrotnej](PartDesign_MultiTransform/pl.md), przeskalowane elementy zostaną umieszczone w tej samej pozycji co element bazowy. Może to skutkować nieoczekiwanymi kształtami, jeśli element bazowy nie jest całkowicie objęty skalowanym obiektem. Dlatego nie zaleca się używania **Skalowania** jako pierwszej transformacji dla funkcji Transformacji wielokrotnej.

<img alt="" src=images/PartDesign_Scaled-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/PartDesign_Scaled-04.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/PartDesign_Scaled-05.png  style="width:200px;"> 
*Cecha podstawowa z otworem → Obiekt skalowany z 2 wystąpieniami → Obiekt skalowany z 4 wystąpieniami.*



## Użycie



### Zmiana skali przekształconej cechy 

1.  Wykonaj jedną z następujących czynności:
    -   Kliknij dwukrotnie obiekt Transformacji wielokrotnej w oknie [Widoku Drzewa](Tree_view/pl.md).
    -   Kliknij prawym przyciskiem myszki obiekt Transformacji wielokrotnej w [Widoku Drzewa](Tree_view/pl.md) i wybierz **Edycja funkcji Transformacji wielokrotnej** z menu podręcznego.
2.  Otworzy się [Panel zadań](Task_panel.md) **Parametry Transformacji wielokrotnej**.
3.  Kliknij prawym przyciskiem myszki na liście **Transformacje** i wybierz **Dodaj transformację zmiany skali** z menu podręcznego.
4.  Pozycja **Zmiana skali** zostanie dodana do listy, a panel zadań zostanie rozszerzony u dołu, aby umożliwić ustawienie **Współczynnik** i **Wystąpienia**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
5.  Naciśnij **OK** na pasku u dołu.
6.  Naciśnij przycisk **OK** u góry, aby zakończyć operację.



## Zmiana skali wybranej cechy 

=

1.  Wybierz element bieżącej Zawartości w oknie [Widoku Drzewa](Tree_view/pl.md).
2.  Wykonaj jedną z następujących czynności:
    -   Naciśnij przycisk **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Utwórz transformację wielokrotną](PartDesign_MultiTransform/pl.md)**.
    -   Wybierz z menu opcję **Projekt Części → Zastosuj przekształcenie → <img src="images/PartDesign_MultiTransform.svg" width=16px> Utwórz wielokrotna transformację**.
3.  Otworzy się [Panel zadań](Task_panel/pl.md) **Parametry Transformacji wielokrotnej**. Zobacz powyżej.



## Opcje

-    **Współczynnik**: Współczynnik, do którego skalowana jest ostatnia cecha.

-    **Wystąpienia**: Liczba kroków od obiektu nieskalowanego *(1)* do wartosci **Współczynnika** *(w tym element bazowy i ostatni)*.

    -   Transformacja skalowana akceptuje liczbę wystąpień poprzedniej transformacji jako wartość maksymalną lub dowolny dzielnik tej liczby zwracający wynik całkowity. Tak więc {{Value|12}}, {{Value|6}}, {{Value|4}}, {{Value|3}} i {{Value|2}} są prawidłowe dla wzoru liniowego lub biegunowego z 12 wystąpieniami.
    -   Skalowana pojedyncza cecha akceptuje dowolną liczbę całkowitą większą niż 1.



## Uwagi

-   Środek skalowania jest środkiem ciężkości elementu, co może powodować:
    -   rosnący element będzie wystawał po przeciwnej stronie elementu nadrzędnego,
    -   kurczący się element straci kontakt z elementem nadrzędnym i zniknie,
    -   zmniejszająca się kieszeń stanie się niewidocznym zagłębieniem wewnątrz elementu nadrzędnego.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Scaled/pl
