---
- GuiCommand:/pl
   Name:PartDesign PolarPattern
   Name/pl:Projekt Części: Szyk kołowy
   MenuLocation:Projekt Części → Zastosuj szyk → Szyk kołowy
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso:[Transformacja wielokrotna](PartDesign_MultiTransform/pl.md)
---

# PartDesign PolarPattern/pl

## Opis

Narzędzie <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:24px;"> **wzorca kołowego** tworzy wzorzec typu kołowego jednej lub wielu cech.

![](images/PartDesign_PolarPattern_example.png ) 
*Powyżej: kieszeń w kształcie szczeliny ''(B)'' wykonana na bazie bryły ''(A, zwana również podstawą)'' jest używana do tworzenia wzoru biegunowego. Wynik ''(C)'' jest pokazany po prawej stronie.*

## Użycie

### Tworzenie

1.  Opcjonalnie [aktywuj](PartDesign_Body/pl#Aktywny_status.md) właściwą bryłę.
2.  Opcjonalnie wybierz jedną lub więcej cech w oknie [widoku drzewa](Tree_view/pl.md) lub w oknie [widoku 3D](3D_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/PartDesign_PolarPattern.svg" width=16px> [Szyk kołowy](PartDesign_PolarPattern/pl.md)**,
    -   Wybierz opcję z menu **Projekt Części → Zastosuj wzór → <img src="images/PartDesign_PolarPattern.svg" width=16px> Szyk kołowy**.
4.  Jeśli nie ma aktywnej Zawartości, a w dokumencie są dwie lub więcej Zawartości, otworzy się okno dialogowe **Wymagana jest aktywna zawartość** i poprosi o uaktywnienie jednej z nich. Jeśli istnieje jedna Zawartość, zostanie ona aktywowana automatycznie.
5.  Jeśli nie wybrano żadnych cech, zostanie wyświetlone okno dialogowe **Wybierz cechę** otworzy się [panel zadań](Task_panel/pl.md): wybierz jedną lub więcej *(przytrzymaj klawisz **Ctrl**)* z listy i naciśnij przycisk **OK**.
6.  Otwórz [panel zadań](Task_panel/pl.md) Parametry **Szyku kołowego**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
7.  Naciśnij przycisk **OK**, aby zakończyć.

### Edycja

1.  Wykonaj jedną z następujących czynności:
    -   Kliknij dwukrotnie obiekt SzykKołowy w oknie [widoku drzewa](Tree_view/pl.md).
    -   Kliknij prawym przyciskiem myszy obiekt SzykKołowy w oknie [widoku drzewa](Tree_view/pl.md) i wybierz opcję **Edytuj SzykKołowy** z menu kontekstowego.
2.  Otworzy się [panel zadań](Task_panel/pl.md) **Parametry Szyku kołowego**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
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
-   Jeśli we wzorcu znajduje się kilka cech, ich kolejność może być ważna. Zobacz sekcję [Oczekiwane funkcje](PartDesign_PolarPattern/pl#Oczekiwane_funkcje.md).
-   Określenie **Osi** wzorca:
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
-   Określ **Kąt**, który ma być objęty wzorcem. Jeśli kąt jest mniejszy niż 360°, elementy są równomiernie rozmieszczone od 0° *(pierwszy element)* do danego kąta *(ostatni element)*. Jeśli kąt jest pełnym kołem 360°, elementy są równomiernie rozmieszczone wokół koła. Oznacza to, że dla n wystąpień kąt 360° jest równoważny kątowi 360°\*(1-1/n).
-   Określ liczbę **Wystąpień** *(łącznie z cechą oryginalną)*.
-   Jeśli zaznaczone jest pole wyboru **Aktualizuj widok**, widok będzie aktualizowany w czasie rzeczywistym.

## Oczekiwane funkcje 

Jeśli niektóre z wybranych cech są addytywne, a inne subtraktywne, ich kolejność może mieć wpływ na efekt końcowy. Kolejność można zmienić, przeciągając poszczególne cechy na liście. {{Version/pl|0.19}}

![](images/PartDesign_feature-order.gif ) 
*Efekty kolejności występowania elementów*

## Ograniczenia

-   Każdy kształt we wzorcu, który nie pokrywa się z elementem nadrzędnym, zostanie wykluczony. Zapewnia to, że bryła środowiska Projekt Części zawsze składa się z jednej, ciągłej bryły.
-   Wzorce Projektu Części nie są jeszcze tak zoptymalizowane jak ich odpowiedniki Rysunku Roboczego. Dlatego dla dużej liczby instancji powinieneś rozważyć użycie [Szyku biegunowego](Draft_PolarArray/pl.md) zamiast tego, w połączeniu z operacją logiczną środowiska Część. Może to wymagać poważnych zmian w twoim modelu, ponieważ opuszczasz środowisko Projekt Części i dlatego nie możesz po prostu kontynuować dalszych funkcji Projektu Części w tej samej Zawartości. Przykład pokazano na [Forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192).
-   Nie można zastosować wzorca bezpośrednio do innego wzorca, czy to kołowego, liniowego czy odbicia lustrzanego. Do tego potrzebna jest funkcja [Transformacji wielokrotnej](PartDesign_MultiTransform/pl.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/pl
