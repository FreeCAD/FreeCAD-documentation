---
 GuiCommand:
   Name: PartDesign Mirrored
   Name/pl: Projekt Części: Odbicie lustrzane
   MenuLocation: Projekt Części , Zastosuj przekształcenie , Odbicie lustrzane
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: PartDesign_MultiTransform/pl
---

# PartDesign Mirrored/pl



## Opis

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> Narzędzie **Odbicie lustrzane** odzwierciedla jedną lub więcej cech.

![](images/PartDesign_Mirrored_example.svg ) 
*Element Kieszeń utworzony ze szkicu zawierającego okrąg ''(A)'' jest używany do utworzenia elementu odbicia lustrzanego. Pionowa oś szkicu ''(B)'' jest używana do zdefiniowania płaszczyzny lustrzanej. Wynik ''(C)'' pokazany jest po prawej stronie.*



## Użycie



### Tworzenie

1.  Opcjonalnie [wybierz](PartDesign_Body/pl#Aktywny_status.md) odpowiednią Zawartość.
2.  Opcjonalnie wybierz jedną lub więcej cech.
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/PartDesign_Mirrored.svg" width=16px> '''Odbicie lustrzane'''**.
    -   Wybierz opcję z menu **Projekt Części → Zastosuj przekształcenie → <img src="images/PartDesign_Mirrored.svg" width=16px> Odbicie lustrzane**.
4.  Jeśli nie wybrano aktywnej Zawartości, a w dokumencie istnieją dwie lub więcej Zawartości, otworzy się okno dialogowe **Wymagana jest aktywna zawartość** z monitem o wybranie jednej z nich. Jeśli istnieje jedna struktura, zostanie ona aktywowana automatycznie.
5.  Jeśli nie wybrano żadnych cech, zostanie otworzony [panel zadań](Task_panel/pl.md) **Wybierz cechę** : należy wybrać jedną lub więcej cech *(przytrzymując klawisz **Ctrl**)* z listy i nacisnąć przycisk **OK**.
6.  Otworzy się [Panel zadań](Task_panel/pl.md) **Parametry odbicia lustrzanego**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
7.  Naciśnij przycisk **OK**, aby zakończyć.



### Edycja

1.  Wykonaj jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt Odbicie lustrzane w oknie [Widok drzewa](Tree_view/pl.md).
    -   Kliknij obiekt Odbicie lustrzane prawym przyciskiem myszy w oknie [Widok drzewa](Tree_view/pl.md) i wybierz **Edycja funkcji odbicia lustrzanego** z menu podręcznego.
2.  Otworzy się panel [Panel zadań](Task_panel/pl.md) **Parametry odbicia lustrzanego**. Więcej informacji można znaleźć w punkcie [Opcje](#Opcje.md).
3.  Naciśnij przycisk **OK**, aby zakończyć.



## Opcje

-   Aby dodać cechy:
    1.  Naciśnij przycisk **Dodaj element**.
    2.  Wybierz element w oknie [Widoku drzewa](Tree_view/pl.md) lub [Widok 3D](3D_view/pl.md).
    3.  Powtórz czynność, aby dodać więcej cech.
-   Aby usunąć funkcje:
    1.  Naciśnij przycisk **Usuń element**.
    2.  Wykonaj jedną z następujących czynności:
        -   Wybierz element w [Widoku drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md).
        -   Zaznacz element na liście i naciśnij klawisz **Del**.
        -   Kliknij prawym przyciskiem myszki element na liście i wybierz **Usuń** z menu podręcznego.
    3.  Powtórz czynność, aby usunąć więcej elementów.
-   Jeśli we wzorcu znajduje się kilka elementów, ich kolejność może być istotna. Zobacz stronę [Szyk kołowy](PartDesign_PolarPattern/pl#Oczekiwane_funkcje.md).
-   Określ **płaszczyznę**:
    -   
        **Pionowa oś szkicu**
        
        : Oś Y szkicu *(płaszczyzna przechodzi przez to odniesienie i oś Z szkicu, dostępne tylko dla elementów opartych na szkicu)*.

    -   
        **Pozioma oś szkicu**
        
        : Oś X szkicu (analogicznie).

    -   
        **Linia konstrukcyjna #**
        
        : Oddzielny wpis dla każdej linii konstrukcyjnej na szkicu (idem).

    -   
        **Bazowa płaszczyzna XY**
        
        : Płaszczyzna XY Zawartości.

    -   
        **Bazowa płaszczyzna YZ**
        
        : Płaszczyzna YZ Zawartości.

    -   
        **Bazowa płaszczyzna XZ**
        
        : Płaszczyzna XZ Zawartości.

    -   
        **Wybierz odniesienie ...**
        
        : Wybór płaskiej ściany w oknie [Widoku 3D](3D_view.md).
-   Jeśli pole wyboru **Aktualizuj widok** jest zaznaczone, widok będzie aktualizowany w czasie rzeczywistym.



## Ograniczenia

Zobacz stronę o ograniczeniach [Szyku kołowego](PartDesign_PolarPattern/pl#Ograniczenia.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Mirrored/pl
