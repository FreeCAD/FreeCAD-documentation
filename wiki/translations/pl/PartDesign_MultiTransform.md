---
- GuiCommand:/pl
   Name:PartDesign MultiTransform
   Name/pl:Projekt Części: Transformacja wielokrotna
   MenuLocation:Projekt Części → Zastosuj przekształcenie → Utwórz transformację wielokrotną
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[Odbicie lustrzane](PartDesign_Mirrored/pl.md), [Szyk liniowy](PartDesign_LinearPattern/pl.md), [Szyk kołowy](PartDesign_PolarPattern/pl.md), [Skaluj](PartDesign_Scaled/pl.md)
---

# PartDesign MultiTransform/pl



## Opis

Narzędzie <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:24px;"> **Transformacja wielokrotna** tworzy szyk jednego lub więcej elementów. Szyk może zawierać wiele przekształceń, gdzie każde kolejne przekształcenie jest stosowane do wyniku poprzedniego przekształcenia.

Dostępne transformacje to: <img alt="" src=images/PartDesign_Mirrored.svg  style="width:16px;"> [Odbicie lustrzane](PartDesign_Mirrored/pl.md), <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:16px;"> [Szyk liniowy](PartDesign_LinearPattern/pl.md), <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:16px;"> [Szyk kołowy](PartDesign_PolarPattern/pl.md) i <img alt="" src=images/PartDesign_Scaled.svg  style="width:16px;">. [Skaluj](PartDesign_Scaled/pl.md). Pierwsze trzy są również dostępne jako osobne narzędzia.

<img alt="" src=images/multitransform_example.png  style="width:600px;"> 
*Wzór otworów utworzony z pojedynczej cechy Otwór poprzez zastosowanie Szyku liniowego z 2 wystąpieniami, a następnie Szyku kołowego z 8 wystąpieniami.*



## Użycie



### Tworzenie

1.  Opcjonalnie [aktywuj](PartDesign_Body/pl#Aktywny_status.md) właściwą bryłę.
2.  Opcjonalnie wybierz jedną lub więcej cech w oknie [widoku drzewa](Tree_view/pl.md) lub w oknie [widoku 3D](3D_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/PartDesign_MultiTransform.svg" width=16px> '''Utwórz transformację wielokrotną'''**.
    -   Wybierz z menu opcję **Projekt Części → Zastosuj przekształcenie → <img src="images/PartDesign_MultiTransform.svg" width=16px>. Utwórz transformację wielokrotną**.
4.  Jeśli nie ma aktywnej Zawartości, a w dokumencie są dwie lub więcej Zawartości, otworzy się okno dialogowe **Wymagana jest aktywna zawartość** i poprosi o uaktywnienie jednej z nich. Jeśli istnieje jedna Zawartość, zostanie ona aktywowana automatycznie.
5.  Jeśli nie wybrano żadnych cech, zostanie wyświetlone okno dialogowe **Wybierz cechę** otworzy się [panel zadań](Task_panel/pl.md): wybierz jedną lub więcej *(przytrzymaj klawisz **Ctrl**)* z listy i naciśnij przycisk **OK**.
6.  Otworzy się [panel zadań](Task_panel/pl.md) **Parametry Transformacji wielokrotnej**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
7.  Naciśnij przycisk **OK**, aby zakończyć.



### Edycja

1.  Wykonaj jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt Transformacja wielokrotna w oknie [Widok drzewa](Tree_view/pl.md).
    -   Kliknij obiekt Transformacja wielokrotna prawym przyciskiem myszy w oknie [Widok drzewa](Tree_view/pl.md) i wybierz **Edycja funkcji transformacji wielokrotnej** z menu podręcznego.
2.  Otworzy się panel [Panel zadań](Task_panel/pl.md) **Parametry odbicia lustrzanego**. Więcej informacji można znaleźć w punkcie [Opcje](#Opcje.md).
3.  Naciśnij przycisk **OK**, aby zakończyć.



### Łączenie istniejących transformacji 

Możliwe jest utworzenie obiektu Transformacji wielokrotnej z istniejących przekształceń [Odbicia lustrzanego](PartDesign_Mirrored/pl.md), [Szyku linowego](PartDesign_LinearPattern/pl.md) i [Szyku kołowego](PartDesign_PolarPattern/pl.md).

1.  Sprawdź właściwość **Oryginały** istniejących przekształceń, aby upewnić się, że zostały one zastosowane do tych samych elementów.
2.  Wybierz te cechy w [Widoku Drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/PartDesign_MultiTransform.svg" width=16px> [Utwórz transformację wielokrotną](PartDesign_MultiTransform/pl.md)**.
    -   Wybierz z menu opcję **Projekt Części → Zastosuj przekształcenie → <img src="images/PartDesign_MultiTransform.svg" width=16px> Utwórz transformację wielokrotną**.
4.  Otworzy się [panel zadań](Task_panel/pl.md) **Parametry Transformacji wielokrotnej** .
5.  Naciśnij przycisk **OK** u góry.
6.  Edytuj właściwość **Transformacje** utworzonego obiektu Transformacji wielokrotnej:
    1.  Kliknij pole.
    2.  Naciśnij przycisk **…**, który się pojawi.
    3.  Otworzy się okno dialogowe **Łącze**.
    4.  Przytrzymaj klawisz **Ctrl** i wybierz istniejące transformacje.
    5.  Naciśnij przycisk **OK**.
7.  Opcjonalnie [edytuj](#Edycja.md) obiekt Transformacji wielokrotnej, patrz wyżej.



## Opcje

-   Aby dodać cechy:
    1.  Naciśnij przycisk **Dodaj element**.
    2.  Wybierz element w oknie [Widoku drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md).
    3.  Powtórz czynność, aby dodać więcej elementów.
-   Aby usunąć cechy:
    1.  Naciśnij przycisk **Usuń element**.
    2.  Wykonaj jedną z następujących czynności:
        -   Wybierz element w oknie [Widoku drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md).
        -   Zaznacz element na liście u góry i naciśnij klawisz **Del**.
        -   Kliknij prawym przyciskiem myszy element na liście u góry i wybierz **Usuń** z menu podręcznego.
    3.  Powtórz czynność, aby usunąć więcej funkcji.
-   Jeśli we wzorcu znajduje się kilka elementów, ich kolejność może być istotna. Zobacz stronę [Szyk kołowy](PartDesign_PolarPattern/pl#Oczekiwane_funkcje.md).
-   Aby dodać transformacje:
    1.  Jeśli już istnieją transformacje: wybierz jedną, po której ma zostać dodana nowa transformacja.
    2.  Kliknij prawym przyciskiem myszy listę **Przekształcenia**.
    3.  Wybierz jedną z następujących opcji z menu podręcznego:
        -   
            **Dodaj transformację odbicia lustrzanego**
            
            . Zobacz stronę [Odbicie lustrzane](PartDesign_Mirrored/pl.md).

        -   
            **Dodaj transformację szyku liniowego**
            
            . Zobacz stronę [Szyk liniowy](PartDesign_LinearPattern/pl.md).

        -   
            **Dodaj transformację szyku kołowego**
            
            . Zobacz stronę [Szyk kołowy](PartDesign_PolarPattern/pl.md).

        -   
            **Dodaj transformację zmiany skali**
            
            . Zobacz stronę [Skaluj](PartDesign_Scaled/pl.md).
    4.  Wybrana transformacja jest dodawana do listy, a ustawienia transformacji są wyświetlane poniżej listy.
    5.  Dostosuj ustawienia do własnych potrzeb.
    6.  Naciśnij przycisk **OK** na pasku u dołu.
    7.  Powtórz czynność, aby dodać więcej operacji przekształceń.
-   Aby edytować transformację:
    1.  Kliknij prawym przyciskiem myszy transformację na liście **Transformacje**.
    2.  Wybierz **Edytuj** z menu kontekstowego.
    3.  Dostosuj ustawienia.
    4.  Naciśnij **OK** na pasku u dołu.
-   Aby zmienić kolejność transformacji:
    1.  Kliknij prawym przyciskiem myszy transformację na liście **Transformacje**.
    2.  Wybierz **Przenieś wyżej** lub **Przenieś w dółj** z menu podręcznego.
-   Jeśli pole wyboru **Aktualizuj widok** jest zaznaczone, widok będzie aktualizowany w czasie rzeczywistym.



## Ograniczenia

Zobacz stronę o ograniczeniach [Szyku kołowego](PartDesign_PolarPattern/pl#Ograniczenia.md).



## Przykład

Za pomocą tego narzędzia można utworzyć ze szkicu w pełni parametryczną część, która jest symetryczna względem dwóch osi.

Może to być płyta montażowa o wymiarach 150x100x10 mm dla silnika z symetrycznymi otworami.

<img alt="" src=images/PartDesign_MultiTransform_Example2.png  style="width:400px;">

1.  Utwórz <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Zawartość](PartDesign_Body/pl.md) i dodaj <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [szkic](PartDesign_NewSketch/pl.md) na jednej z jego płaszczyzn bazowych.
2.  W szkicu utwórz geometrię dla jednej ćwiartki części *(tj. górnej prawej ćwiartki)*.
    -   Zwróć uwagę, że wiązania muszą również obejmować tylko jedną czwartą części, np. zamiast pełnego wymiaru {{Value|150mm}} wpisz {{Value|150/2mm}} lub {{Value|75mm}}.
    -   Upewnij się, że szkic jest zamknięty, dodając linie wzdłuż osi pionowej i poziomej.
3.  Wyciągnij część za pomocą fukcji <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [Projekt Części: Wyciągnij](PartDesign_Pad/pl.md).
4.  Wybierz narzędzie <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:16px;"> **Utwórz transformacje wielokrotną**.
5.  Zostanie otwarte okno dialogowe zadania.
6.  Ostatnia cecha Zawartości jest już wybrana. Ponieważ chcemy wykonać odbicie lustrzane tego elementu, możemy zignorować przyciski **Dodaj element** i **Usuń element**.
7.  Kliknij prawym przyciskiem myszki w polu **Transformacje** i wybierz **Dodaj transformację odbicia lustrzanego** z menu podręcznego.
8.  Jako **Płaszczyznę** wybierz **Pionowa oś szkicu**.
9.  Jeśli pole wyboru **Aktualizuj widok** jest zaznaczone, część powinna być teraz odbita symetrycznie względem jednej z osi.
10. Ponownie wybierz **Dodaj transformację odbicia lustrzanego** z menu podręcznego w polu **Transformacje**.
11. Teraz jako **Płaszczyznę** wybierz **Pozioma oś szkicu**.
12. Naciśnij przycisk **OK**, aby zakończyć operację.
13. Aby usunąć krawędzie wzdłuż osi symetrii w wyniku końcowym, ustaw właściwość **Ulepsz** nowego elementu na {{true/pl}} w [edytorze właściwości](Property_editor/pl.md).

Aby sprawdzić, czy część jest w pełni parametryczna, otwórz początkowy szkic z ćwiartką części i zmień jeden wymiar, na przykład średnicę otworu. Po zamknięciu szkicu trzy pozostałe otwory zostaną odpowiednio zmienione. Działa to również w przypadku wszystkich innych wymiarów. Szkic modelujący całą część z pojedynczym wyciągnięciem i bez odbicia lustrzanego byłby znacznie bardziej złożony, a wprowadzenie wszystkich późniejszych zmian byłoby bardziej skomplikowane.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MultiTransform/pl
