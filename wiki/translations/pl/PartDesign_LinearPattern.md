---
- GuiCommand:/pl
   Name:PartDesign LinearPattern
   Name/pl:Projekt Części: Szyk liniowy
   MenuLocation:Projekt Części → Zastosuj szyk → Szyk liniowy
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[Transformacja wielokrotna](PartDesign_MultiTransform/pl.md)
---

# PartDesign LinearPattern/pl

## Opis

Narzędzie <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:24px;"> **Szyk liniowy** tworzy liniowy wzór jednej lub kilku cech.

![](images/PartDesign_LinearPattern_example.svg ) 
*Powyżej: wyciągnięcie w kształcie litery L ''(B)'' wykonane na bazie bryły ''(A, zwanej również podstawą)'' jest używane do tworzenia liniowego wzoru. Wynik ''(C)'' jest pokazany po prawej stronie*.

## Użycie

### Tworzenie

1.  Opcjonalnie [aktywuj](PartDesign_Body/pl#Aktywny_status.md) właściwą bryłę.
2.  Opcjonalnie wybierz jedną lub więcej cech w oknie [widoku](Tree_view/pl.md) lub w [widoku 3D](3D_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/PartDesign_LinearPattern.svg" width=16px> [Szyk liniowy](PartDesign_LinearPattern/pl.md)**.
    -   Wybierz z menu **Projekt Części → Zastosuj wzór → <img src="images/PartDesign_LinearPattern.svg" width=16px> Szyk liniowy**.
4.  Jeśli nie ma aktywnej Zawartości, a w dokumencie są dwie lub więcej Zawartości, otworzy się okno dialogowe **Wymagana jest aktywna Zawartość** i poprosi o uaktywnienie jednej z nich. Jeśli istnieje jedna Zawartość, zostanie ona aktywowana automatycznie.
5.  Jeśli nie wybrano żadnych cech, zostanie wyświetlone okno dialogowe **Wybierz cechę** otworzy się [panel zadań](Task_panel/pl.md): wybierz jedną lub więcej *(przytrzymaj klawisz **Ctrl**)* z listy i naciśnij przycisk **OK**.
6.  Otwórz [panel zadań](Task_panel/pl.md) Parametry **Szyku liniowego**. Więcej informacji na ten temat można znaleźć w sekcji [Opcje](#Opcje.md).
7.  Naciśnij przycisk **OK**, aby zakończyć.

### Edycja

1.  Wykonaj jedną z następujących czynności:
    -   Kliknij dwukrotnie obiekt Szyk Liniowy w oknie [widoku drzewa](Tree_view/pl.md).
    -   Kliknij prawym przyciskiem myszy obiekt Szyk Liniowy w oknie [widoku drzewa](Tree_view/pl.md) i wybierz opcję **Edytuj Szyk Liniowy** z menu kontekstowego.
2.  Otworzy się [panel zadań](Task_panel/pl.md) **Parametry Szyku liniowego**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  Naciśnij przycisk **OK**, aby zakończyć.

## Opcje

-   Aby dodać cechy:
    1.  Naciśnij przycisk **Dodaj cechę**.
    2.  Wybierz cechę w oknie [Widoku drzewa](Tree_view/pl.md) lub w oknie [Widoku 3D](3D_view/pl.md).
    3.  Powtórz, aby dodać więcej cech.
-   Aby usunąć cechy:
    1.  Naciśnij przycisk **Usuń cechę**.
    2.  Wykonaj jedną z następujących czynności:
        -   Wybierz cechę w oknie [Widoku drzewa](Tree_view/pl.md) lub w oknie [Widoku 3D](3D_view/pl.md).
        -   Zaznacz cechę na liście i naciśnij klawisz **Del**.
        -   Kliknij prawym przyciskiem myszy cechę na liście i wybierz z menu podrzędnego opcję **Usuń**.
    3.  Powtórz czynność, aby usunąć więcej cech.
-   Jeśli we wzorcu znajduje się kilka cech, ich kolejność może być ważna. Zobacz stronę [Projekt Części: Szyk kołowy](PartDesign_PolarPattern/pl#Oczekiwane_funkcje.md).
-   Określenie **Kierunku** wzorca:
    -   
        **Normalna oś szkicu**
        
        : Oś Z szkicu *(dostępna tylko dla cech opartych na szkicu)*.

    -   
        **Pionowa oś szkicu**
        
        : Oś Y szkicu *(analogicznie)*.

    -   
        **Pozioma oś szkicu**
        
        : Oś X szkicu *(analogicznie)*.

    -   
        **Linia konstrukcyjna #**
        
        : Osobny wpis dla każdej linii konstrukcyjnej w szkicu *(analogicznie)*.

    -   
        **Podstawowa oś X**
        
        : Oś X Zawartości.

    -   
        **Podstawowa oś Y**
        
        : Oś Y Zawartości.

    -   
        **Podstawowa oś Z**
        
        : Oś Z Zawartości.

    -   
        **Wybór odniesienia...**
        
        : Wybierz [Linię odniesienia](PartDesign_Line/pl.md) w oknie [Widok drzewa](Tree_view/pl.md) lub [Linię odniesienia](PartDesign_Line/pl.md) lub krawędź w oknie [Widok 3D](3D_view/pl.md).
-   Zaznacz pole wyboru **Odwróć kierunek**, aby odwrócić wzór.
-   Określ **Długość**, która ma zostać objęta wzorcem.
-   Określ liczbę **Wystąpień** *(łącznie z cechą oryginalną)*.
-   Jeśli zaznaczone jest pole wyboru **Aktualizuj widok**, widok będzie aktualizowany w czasie rzeczywistym.

## Ograniczenia

Zobacz stronę o ograniczeniach [Szyku kołowego](PartDesign_PolarPattern/pl#Ograniczenia.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign LinearPattern/pl
