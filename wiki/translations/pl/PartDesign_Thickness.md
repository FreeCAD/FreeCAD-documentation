---
- GuiCommand:
   Name:PartDesign Thickness
   Name/pl:Projekt Części: Grubość
   MenuLocation:Projekt Części - Zastosuj funkcję ulepszenia - Grubość
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Część: Grubość](Part_Thickness/pl.md)
---

# PartDesign Thickness/pl



## Opis

Narzędzie <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> **Grubość** przekształca bryłę w pusty obiekt z przynajmniej jedną otwartą ścianą, nadając każdej z pozostałych ścian jednolitą grubość. Dodaje do dokumentu obiekt **Grubość** wraz z jego odpowiednią reprezentacją w [widoku drzewa](Tree_view/pl.md).

<img alt="" src=images/PartDesign_Thickness_example.svg  style="width:600px;"> 
*Bryła bazowa ''(A)'' → Bryła z wybraną ścianą do otwarcia ''(B)'' → Powstały pusty obiekt ''(C)''.*



## Użycie



### Dodanie funkcji grubość 

1.  Opcjonalnie [uaktywnij](PartDesign_Body/pl#Aktywny_status.md) bryłę, do której ma zostać zastosowana funkcja grubość.
2.  Wybierz jedną lub więcej ścian bryły.
3.  Istnieje kilka sposobów na wywołanie narzędzia:
    -   Naciśnij przycisk **<img src="images/PartDesign_Thickness.svg" width=16px> [Grubość](PartDesign_Thickness/pl.md)**.
    -   Wybierz z menu opcję **Projekt Części → Zastosuj funkcję ulepszenia → <img src="images/PartDesign_Thickness.svg" width=16px> Grubość**.
4.  Jeśli nie ma aktywnej Bryły, a w dokumencie występuje dwie lub więcej Brył, otworzy się okno dialogowe **Wymagana jest aktywna zawartość** i poprosi o uaktywnienie jednej z nich. Jeśli istnieje jedna bryła, zostanie ona aktywowana automatycznie.
5.  Otworzy się [panel zadań](Task_panel/pl.md) **Parametry funkcji grubość**. Więcej informacji znajdziesz w sekcji [Opcje](#Opcje.md).
6.  Naciśnij przycisk **OK**, aby zakończyć.

:   *Pamiętaj*:
    -   Ponieważ dla danej cechy musi istnieć przynajmniej jedna ściana, ostatnia pozostała na liście ściana nie może zostać usunięta.



### Edycja funkcji grubość 

1.  Wykonaj jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt Grubość w oknie [Widoku drzewa](Tree_view/pl.md).
    -   Kliknij obiekt Grubość prawym przyciskiem myszy w oknie [Widok drzewa](Tree_view/pl.md) i wybierz **Edytuj Grubość** z menu kontekstowego.
2.  Otworzy się panel [Panel zadań](Task_panel/pl.md) **Parametry funkcji Grubość**. Więcej informacji można znaleźć w punkcie [Opcje](#Opcje.md).
3.  Naciśnij przycisk **OK**, aby zakończyć.



## Opcje

-    **Dodaj ścianę**: Dodanie ścian do zaznaczenia poprzez naciśnięcie przycisku **Dodaj ścianę** i wybranie kolejnych ścian.

-    **Usuń ścianę**: Wybierz sposób usuwania ścian z zaznaczenia:

    -   Zaznacz jedną lub więcej ścian na liście i naciśnij klawisz **Del** lub kliknij prawym przyciskiem myszy listę i wybierz z menu kontekstowego opcję **Skasuj**.
    -   Naciśnij przycisk **Usuń ścianę**. Wszystkie wcześniej wybrane ściany są podświetlone na fioletowo. Wybierz każdą ścianę, która ma zostać usunięta.

-    **Grubość**: Ustaw grubość ścianki albo edytując wartość, albo klikając strzałki góra/dół.

-    **Tryb**:

    -   
        **Powłoka**
        
        : Można wybrać tylko tę opcję.

    -   
        **Rura**
        
        : Nie zaimplementowane. Zobacz [ten temat na forum](https://forum.freecadweb.org/viewtopic.php?p=484495#p484495)

    -   
        **Obie strony**
        
        : Nie zaimplementowane. Zobacz [ten temat na forum](https://forum.freecadweb.org/viewtopic.php?p=484495#p484495).

-    **Typ dołączenia**:

    -   
        **Łuk**
        
        : Gdy przesunięte są powierzchnie styczne, nowe ściany, które się nie przecinają, są łączone za pomocą zaokrąglenia o promieniu równym zdefiniowanej grubości.

    -   
        **Przecięcie**
        
        : Gdy niestyczne ściany są odsunięte, nowe ściany, które nie przecinają się, są przedłużane, aby spotkać się na ich wirtualnym przecięciu.

-    **Przecięcie**: Gdy opcja jest zaznaczona, unikane są samoczynne przecięcia w niektórych modelach. Ta opcja nie jest zalecana, ponieważ opiera się na niekompletnej [metodzie OpenCASCADE](https://dev.opencascade.org/doc/refman/html/class_b_rep_offset_a_p_i___make_thick_solid.html#af78f35025a31e2ce8bd96c82fb33a981).

-    **Stwórz grubość do wewnątrz**: Gdy opcja jest zaznaczona, ściany są przesunięte do wewnątrz.



## Uwagi

-   Jeśli grubość idzie do wewnątrz, wartość musi być mniejsza niż najmniejsza wysokość bryły.
-   Narzędzie może zawieść przy złożonych kształtach. [Wyciągnięcie po ścieżce](PartDesign_AdditivePipe/pl.md) lub [Wyciągnięcie przez profile](PartDesign_AdditiveLoft/pl.md) mogą działać lepiej przy tworzeniu złożonych kształtów.
-   Znane błędy:
    -   BRep_API: polecenie nie wykonane.
    -   BRep_Tool: brak parametru na krawędzi.
    -   Cichy błąd.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Grubość wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Base|LinkSub**: Link podrzędny do listy wybranych krawędzi i ścian cechy nadrzędnej.

-    **Support Transform|Bool**: \"Uwzględnij bazowy kształt addytywny/subtraktywny, gdy jest używany w cechach wzorcowych. Jeśli wyłączone, tylko ubrana część kształtu jest używana do wzorowania\". Domyślnie: `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link do cechy nadrzędnej.

-    **_ Body|LinkHidden|hidden**: Link do bryły nadrzędnej.


{{Properties_Title|Projekt Części}}

-    **Ulepsz|Bool**: \"Ulepsz kształt *(usuń zbędne krawędzie)* po operacji dodawania/odejmowania\". Wartość domyślna jest określana przez preferencję **Automatycznie udoskonal model po wykonaniu operacji opartej na szkicu**. Zobacz [Projekt Części: Ustawienia](PartDesign_Preferences/pl#Og.C3.B3lne.md).


{{Properties_Title|Grubość}}

-    **Value|Długość**: \"Wartość grubości\". Domyślnie: {{value|1 mm}}.

-    **Tryb|Enumeration**: \"Tryb\". {{value|Powłoka}} *(domyślnie)*, {{value|Rura}} lub {{Value|Obie strony}}. Tylko opcja {{value|Powłoka}} jest zaimplementowana.

-    **Dołącz|Enumeration**: \"Tryb dołączenia\". {{value|Łuk}} *(domyślnie)* lub {{Value|Przecięcie}}.

-    **Odwrócony|Bool**: \"Stwórz grubość do wewnątrz\". Domyślnie: {{FALSE/pl}}.

-    **Przecięcie|Bool**: \"Włącz obsługę przecięć\". Domyślnie: {{FALSE/pl}}.





{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Thickness/pl
