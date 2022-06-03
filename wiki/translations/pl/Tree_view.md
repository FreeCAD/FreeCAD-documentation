# Tree view/pl
{{TOCright}}

## Wprowadzenie

[Widok drzewa](Tree_view.md) pojawia się w zakładce **Model** w [widoku połączonym](Combo_view.md), jest to jeden z najważniejszych paneli w [interfejsie użytkownika](Interface.md). Pokazuje wszystkie obiekty zdefiniowane przez użytkownika, które są częścią dokumentu FreeCAD. Widok drzewa jest reprezentacją [struktury dokumentu](document_structure.md) i wskazuje, jakie informacje są zapisane na dysku.

Obiekty te niekoniecznie muszą być kształtami geometrycznymi widocznymi w [oknie widoku 3D](3D_view.md), ale mogą również zawierać obiekty danych utworzone za pomocą dowolnego [Środowiska pracy](Workbenches.md).

![](images/FreeCAD_Tree_view.png )



*Widok drzewa pokazujący różne elementy w dokumencie.*

## Praca z widokiem drzewa 

Domyślnie, zawsze gdy tworzony jest nowy obiekt, jest on dodawany na końcu listy w widoku drzewa. Widok drzewa umożliwia zarządzanie obiektami w celu utrzymania ich w zorganizowanym szyku.
Pozwala na tworzenie [grup](Std_Group/pl.md), przesuwanie obiektów wewnątrz grup, przesuwanie grup wewnątrz innych grup, zmianę nazwy obiektów, kopiowanie obiektów, usuwanie obiektów i inne operacje w menu kontekstowym *(kliknięcie prawym przyciskiem myszki)*, które zależą od aktualnie wybranego obiektu i aktualnie aktywnego warsztatu.

Wiele operacji tworzy obiekty, które są zależne od wcześniej utworzonego obiektu. W tym przypadku widok drzewa pokazuje tę zależność poprzez pochłanianie starszego obiektu wewnątrz nowego obiektu. Rozwijanie i zwijanie obiektów w widoku drzewa pokazuje parametryczną historię tego obiektu. Obiekty głębiej położone wewnątrz innych są starsze, natomiast obiekty znajdujące się na zewnątrz są nowsze i pochodzą od obiektów starszych. Modyfikując obiekty wewnętrzne, operacje parametryczne rozprzestrzeniają się aż do góry, generując nowy wynik.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width   *" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width   *" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width   *" height="304px;">



*Najwyższy z obiektów jest tworzony przez wykonywanie operacji parametrycznych na obiektach, które same zostały utworzone przez poprzednie operacje. Rozwinięcie drzewa na wielu poziomach ujawnia oryginalne elementy, które zostały użyte do utworzenia brył cząstkowych.*

## Działania

Ponieważ widok drzewa zawiera listę obiektów, które mogą być widoczne w oknie [widoku 3D](3D_view/pl.md), wiele z tych działań jest takich samych jak te, które mogą być wykonane bezpośrednio z okna [widoku 3D](3D_view/pl.md).

Po uruchomieniu aplikacji domyślnym Środowiskiem pracy jest [Start](Start_Workbench/pl.md) jest aktywny i nie stworzono żadnego dokumentu, a kliknięcie prawym przyciskiem myszy na [widoku drzewa](Tree_view/pl.md) pokazuje jedno podmenu z czterema poleceniami   *   *

-    **Akcje z wyrażeniami**   *

    -   [Kopiuj wybrane](Expressions/pl.md),
    -   [Kopiuj aktywny element](Expressions/pl.md),
    -   [Kopiuj wszystkie dokumenty](Expressions/pl.md),
    -   [Wklej](Std_Paste/pl.md).

Umożliwiają one pracę z różnymi dokumentami, ale są wyłączone, jeśli nie ma dokumentu.

Po utworzeniu nowego dokumentu aktywne stają się następujące elementy   *

-    **Akcje z wyrażeniami**   *

    -   [Kopiuj aktywny dokument](Expressions/pl.md),
    -   [Kopiuj wszystkie dokumenty](Expressions/pl.md).

Ponadto dostępne są dodatkowe akcje [Link](Std_LinkMake.md).

-    **Akcje z łączami**   *

    -   
        **Utwórz link grupy**
        
           *

        -   [Grupa podstawowa](Std_LinkMakeGroup/pl.md),
        -   [Grupa linków](Std_LinkMakeGroup/pl.md),
        -   [Grupa linków umożliwiających modyfikację](Std_LinkMakeGroup/pl.md),

    -   [Utwórz link](Std_LinkMake/pl.md)

### Wybór dokumentu 

Jeśli wybierzesz aktywny dokument i klikniesz prawym przyciskiem myszy, oprócz pozycji **Akcje z wyrażeniami** i **Akcje z linkami**, pojawią się następujące polecenia   *

-    **Pokaż ukryte obiekty**   * Jeśli opcja jest aktywna, widok drzewa pokaże ukryte elementy.

-    **Znajdź**   * Wyświetli pole do wprowadzania nazwy obiektu, do znalezienia wewnątrz wybranego dokumentu.

-    **Zamknij dokument**   * zamyka wybrany dokument.

-    **Pomiń ponowne obliczenia**   * Jeśli opcja jest aktywna, obiekty dokumentu nie będą automatycznie [przeliczane](Std_Refresh.md).

    -   
        **Pozwól na ponowienie wybranych przeoliczeń**
        
           * jeśli opcja jest aktywna, dokument pozwoli na [przeliczenie](Std_Refresh.md) tylko niektórych obiektów.

-    **Zaznacz do przeliczenia**   * zaznacza wszystkie obiekty dokumentu jako zmodyfikowane i gotowe do [przeliczenia](Std_Refresh.md).

-    **[Utwórz grupę](Std_Group.md)**   * Tworzy [grupę](Std_Group.md) w wybranym dokumencie.

### Zaznaczanie obiektów 

Po dodaniu obiektów do dokumentu kliknięcie na nich prawym przyciskiem myszki powoduje wyświetlenie dodatkowych poleceń. Zależą one od liczby wybranych obiektów, ich typu, a także od aktywnego obszaru roboczego. W większości przypadków i w większości środowisk pracy *(z wyjątkiem [Start](Start_Workbench/pl.md))* dostępne są wtedy następujące polecenia   *

-    **[Wygląd zewnętrzny](Std_SetAppearance/pl.md)**   * uruchamia okno dialogowe do zmiany właściwości wizualnych całego obiektu.

-    **[Nadaj kolor losowo](Std_RandomColor/pl.md)**   * przypisuje kolor losowo do obiektu.

-    **[Wytnij](Std_Cut/pl.md)**   * wyłączone.

-    **[Kopiuj](Std_Copy/pl.md)**   * kopiuje obiekt do pamięci.

-    **[Wklej](Std_Paste/pl.md)**   * wkleja skopiowany obiekt do dokumentu; kopia jest dodawana na ostatniej pozycji widoku drzewa.

-    **[Usuń](Std_Delete/pl.md)**   * usuwa obiekt z dokumentu.

-    **Ukryj element**   * jeżeli jest aktywny, wybrany obiekt zostanie ustawiony jako ukryty.

-    **Dodaj do wyboru obiekty zależne**   * wszystkie obiekty zależne zostaną dodane do zaznaczenia. W ten sposób można zobaczyć zależności i np. usunąć wszystkie obiekty zależne za jednym razem. Opcja ta jest dostępna tylko wtedy, gdy jeden z wybranych obiektów posiada powiązania. {{Version/pl|0.20}}

-    **Zaznacz do przeliczenia**   * zaznacza wybrany obiekt jako \"dotknięty\" i gotowy do [przeliczenia](Std_Refresh/pl.md).

-    **Przelicz obiekt**   * oblicza ponownie wybrany obiekt.

-    **Zmień nazwę**   * rozpoczyna edycję etykiety wybranego obiektu, a nie nazwy, która jest tylko do odczytu. Opcja ta jest dostępna tylko wtedy, gdy wybrany jest pojedynczy obiekt.

Jako przykład rozszerzenia menu kontekstowego, jeśli [sześcian](Part_Box/pl.md) jest kliknięty prawym przyciskiem myszy, gdy aktywne jest środowisko pracy [Część](Part_Workbench/pl.md), dostępne są następujące dodatkowe polecenia   *

-    **[Edytuj](Std_Edit/pl.md)**   * uruchamia tryb edycji obiektu.

-    **[Transform](Std_TransformManip/pl.md)**   * uruchamia widżet transformacji, aby przesunąć lub obrócić obiekt.

-    **[Edytor dołączenia](Part_EditAttachment/pl.md)**   * uruchamia okno dialogowe dołączenia obiektu do jednego lub więcej innych obiektów.

-    **[Ustaw kolory ...](Part_FaceColors/pl.md)**   * ustawia kolor wybranych powierzchni obiektu.

-    **[Przełącz widoczność](Std_ToggleVisibility/pl.md)**   * sprawia, że obiekt jest widoczny lub niewidoczny w oknie [widoku 3D](3D_view/pl.md).

-    **[Pokaż zaznaczone](Std_ShowSelection/pl.md)**   * czyni zaznaczony obiekt widocznym.

-    **[Ukryj zaznaczone](Std_HideSelection/pl.md)**   * czyni zaznaczony obiekt niewidocznym.

-    **[Przełącznik wyboru](Std_ToggleSelectability/pl.md)**   * przełącza możliwość wyboru obiektu w oknie [widoku 3D](3D_view/pl.md).

-    **[Wybierz wszystkie wystąpienia](Std_TreeSelectAllInstances.md)**   * zaznacza wszystkie wystąpienia tego obiektu w widoku drzewa.

-    **[Wyślij do konsoli Python](Std_SendToPythonConsole/pl.md)**   * tworzy zmienną w [Konsoli Python](Python_console/pl.md) odwołującą się do obiektu.

### Operacje na klawiaturze 

Gdy użytkownik jest skupiony na widoku drzewa, dostępne są następujące operacje klawiaturowe   *

-    **Ctrl**\+**F**   * otwiera okno wyszukiwania na dole drzewa, umożliwiając wyszukiwanie i docieranie do obiektów za pomocą ich nazw lub etykiet.

-   Rozwijanie i zwijanie za pomocą kombinacji klawiszy **Alt**+**Arrow**   * {{Version/pl|0.20}}
    -   
        **Alt**
        
        \+**Lewy**   * zwija zaznaczony element *(lub elementy)*.

    -   
        **Alt**
        
        \+**Prawo**   * rozwija zaznaczony element *(elementy)*.

    -   
        **Alt**
        
        \+**Up**   * rozwija zaznaczony element*(y)*, zwijając wszystkie jego elementy podrzędne z poziomu pierwszego *(głębsze elementy podrzędne pozostają bez zmian)*.

    -   
        **Alt**
        
        \+**Down**   * rozwija zaznaczony element *(elementy)* wraz z rozwijając elementy podrzędne z pierwszego poziomu *(głębsze elementy podrzędne pozostają bez zmian)*.

## Ikonki dodatków 

Na domyślnej ikonie obiektu w widoku drzewa może być wyświetlana jedna lub więcej mniejszych ikonek dodatków. Dostępne ikony dodatków i ich znaczenie są wymienione poniżej. {{Version/pl|0.19}}

### ![](images/FreeCAD_Tree_view_recompute.png ) Biały znak kontrolny na niebieskim tle 

Oznacza to, że obiekt musi zostać [przeliczony](Std_Refresh/pl.md), z powodu zmian dokonanych w modelu lub dlatego, że użytkownik zaznaczył obiekt w menu kontekstowym widoku drzewa do ponownego przeliczenia. W większości przypadków ponowne obliczenia są wywoływane automatycznie, ale czasami są opóźniane z powodów wydajnościowych.

### ![](images/FreeCAD_Tree_view_tip.png ) Biała strzałka na zielonym tle 

Oznacza to tak zwany [czubek](PartDesign_Body/pl#Czubek.md) korpusu. Jest to zazwyczaj ostatnia cecha obiektu [zawartość](PartDesign_Body/pl.md) i reprezentuje całą bryłę dla świata zewnętrznego, np. gdy bryła jest eksportowana lub używana w operacjach [logicznych](Part_Boolean/pl.md) środowiska Część. Czubek może być zmieniany przez użytkownika.

### ![](images/FreeCAD_Tree_view_unattached.png ) Fioletowe ogniwo łańcucha na białym tle 

Jest to typowe dla [szkiców](Sketch/pl.md), pierwotnych brył geometrycznych, takich jak sześcian, walec, itp. oraz geometrii [punktu odniesienia](Datum.md). Wskazuje, że obiekt nie jest do niczego przymocowany. Nie ma on przesunięcia dołączenia i pobiera swoją pozycję i wyrównanie wyłącznie z właściwości [umiejscowienie](Placement.md).

Dostępny jest [Poradnik   * Podstawy przyłączania](Basic_Attachment_Tutorial.md) wyjaśniający jak radzić sobie z takimi obiektami.

### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Żółty znak X 

Jest to używane tylko dla [szkiców](Sketch/pl.md) i wskazuje, że szkic nie jest w pełni związany. Wewnątrz środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md) liczba pozostałych stopni swobody jest wyświetlana w komunikatach solvera.

### ![](images/FreeCAD_Tree_view_error.png ) Biały wykrzyknik na czerwonym tle 

Wskazuje to, że w obiekcie wystąpił błąd, który należy naprawić. Po przeliczeniu całego dokumentu po najechaniu myszką na obiekt w widoku drzewa zostanie wyświetlona etykietka z opisem błędu. **Uwaga**   * Wszystkie inne obiekty zależne od obiektu w stanie błędu, nie zostaną poprawnie przeliczone, mogą więc nadal prezentować nieaktualny stan.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tree view/pl
