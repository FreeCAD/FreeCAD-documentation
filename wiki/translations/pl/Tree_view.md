 {{TOCright}}

## Wprowadzenie

[Widok drzewa](Tree_view.md) pojawia się w zakładce {{MenuCommand|Model}} w [widoku połączonym](Combo_view.md), jest to jeden z najważniejszych paneli w [interfejsie użytkownika](Interface.md). Pokazuje wszystkie obiekty zdefiniowane przez użytkownika, które są częścią dokumentu FreeCAD. Widok drzewa jest reprezentacją [struktury dokumentu](document_structure.md) i wskazuje, jakie informacje są zapisane na dysku.

Obiekty te niekoniecznie muszą być kształtami geometrycznymi widocznymi w [oknie widoku 3D](3D_view.md), ale mogą również zawierać obiekty danych utworzone za pomocą dowolnego [Środowiska pracy](Workbenches.md).

![](images/FreeCAD_Tree_view.png )


*Widok drzewa pokazujący różne elementy w dokumencie.*

## Praca z widokiem drzewa {#praca_z_widokiem_drzewa}

Domyślnie, zawsze gdy tworzony jest nowy obiekt, jest on dodawany na końcu listy w widoku drzewa. Widok drzewa umożliwia zarządzanie obiektami w celu utrzymania ich w zorganizowanym szyku.
Pozwala na tworzenie [group](Std_Group.md), przesuwanie obiektów wewnątrz grup, przesuwanie grup wewnątrz innych grup, zmianę nazwy obiektów, kopiowanie obiektów, usuwanie obiektów i inne operacje w menu kontekstowym *(kliknięcie prawym przyciskiem myszki)*, które zależą od aktualnie wybranego obiektu i aktualnie aktywnego warsztatu.

Wiele operacji tworzy obiekty, które są zależne od wcześniej utworzonego obiektu. W tym przypadku widok drzewa pokazuje tę zależność poprzez pochłanianie starszego obiektu wewnątrz nowego obiektu. Rozwijanie i zwijanie obiektów w widoku drzewa pokazuje parametryczną historię tego obiektu. Obiekty głębiej położone wewnątrz innych są starsze, natomiast obiekty znajdujące się na zewnątrz są nowsze i pochodzą od obiektów starszych. Modyfikując obiekty wewnętrzne, operacje parametryczne rozprzestrzeniają się aż do góry, generując nowy wynik.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width:" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width:" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width:" height="304px;">


*Najwyższy z obiektów jest tworzony przez wykonywanie operacji parametrycznych na obiektach, które same zostały utworzone przez poprzednie operacje. Rozwinięcie drzewa na wielu poziomach ujawnia oryginalne elementy, które zostały użyte do utworzenia brył cząstkowych.*

## Działania


**Note:**

wyrażenia i akcje związane z linkami zostały dodane w wersji **0.19**.

Ponieważ widok drzewa zawiera listę obiektów, które mogą być widoczne w oknie [widoku 3D](3D_view.md), wiele z tych działań jest takich samych jak te, które mogą być wykonane bezpośrednio z okna [widoku 3D](3D_view.md).

Po uruchomieniu aplikacji domyślnym Środowiskiem pracy jest [Start](Start_Workbench.md) jest aktywny i nie stworzono żadnego dokumentu, a kliknięcie prawym przyciskiem myszy na [widoku drzewa](Tree_view.md) pokazuje tylko jedno polecenie:

-    {{MenuCommand|Expression actions}}: [Kopiuj wybrane](Std_Expressions.md), [Kopiuj aktywny element](Std_Expressions.md), [Kopiuj wszystkie dokumenty](Std_Expressions.md), Wklej. Umożliwiają one pracę z różnymi dokumentami, ale są wyłączone, jeśli nie ma dokumentu.

Po utworzeniu nowego dokumentu aktywne stają się następujące elementy:

-    {{MenuCommand|Expression actions}}: [Kopiuj aktywny dokument](Std_Expressions.md), [Kopiuj wszystkie dokumenty](Std_Expressions.md).

Ponadto dostępne są dodatkowe akcje [Link](Std_LinkMake.md).

-    {{MenuCommand|Link actions}}: [Utwórz link](Std_LinkMake.md).

    -   
        {{MenuCommand|Utwórz link grupy}}
        
        : [Grupa podstawowa](Std_LinkMakeGroup.md), [Grupa linków](Std_LinkMakeGroup.md), [Grupa linków umożliwiających modyfikację](Std_LinkMakeGroup.md).

### Wybór dokumentu {#wybór_dokumentu}

Jeśli wybierzesz aktywny dokument i klikniesz prawym przyciskiem myszy, oprócz pozycji {{MenuCommand|Akcje z wyrażeniami}} i {{MenuCommand|Akcje z linkami}}, pojawią się następujące polecenia:

-    {{MenuCommand|Pokaż ukryte obiekty}}: Jeśli opcja jest aktywna, widok drzewa pokaże ukryte elementy.

-    {{MenuCommand|Znajdź}}: Wyświetli pole do wprowadzania nazwy obiektu, do znalezienia wewnątrz wybranego dokumentu.

-    {{MenuCommand|Zamknij dokument}}: zamyka wybrany dokument, wywołując funkcję `closeDocument()`.

-    {{MenuCommand|Pomiń ponowne obliczenia}}: Jeśli opcja jest aktywna, obiekty dokumentu nie będą automatycznie [przeliczane](Std_Refresh.md).

    -   
        {{MenuCommand|Pozwól na ponowienie wybranych przeoliczeń}}
        
        : jeśli opcja jest aktywna, dokument pozwoli na [przeliczenie](Std_Refresh.md) tylko niektórych obiektów.

-    {{MenuCommand|Zaznacz do przeliczenia}}: zaznacza wszystkie obiekty dokumentu jako zmodyfikowane i gotowe do [przeliczenia](Std_Refresh.md).

-    {{MenuCommand|[Utwórz grupę](Std_Group.md)}}: Tworzy [grupę](Std_Group.md) w wybranym dokumencie, przy użyciu następujących funkcji `addObject()`.

### Zaznaczanie obiektów {#zaznaczanie_obiektów}

Gdy do dokumentu zostaną dodane nowe obiekty, kliknięcie prawym przyciskiem myszy na pustej części widoku drzewa spowoduje wyświetlenie dodatkowych poleceń na liście dostępnych działań.
Ich dostępność zależy od typu obiektu i aktywnego środowiska roboczego.

Na przykład, gdy aktywne jest Środowisko pracy [Draft](Draft_Workbench.md), najpierw wybierz obiekt, a następnie kliknij prawym przyciskiem myszy na puste miejsce w widoku drzewa:

-    {{MenuCommand|[Ukryj](Std_ToggleVisibility.md)}}: sprawia, że obiekt staje się widoczny lub niewidoczny w oknie [widoku 3D](3D_view/pl.md).

-    {{MenuCommand|[Pokaż zaznaczone](Std_ShowSelection.md)}}: sprawia, że wybrane obiekty są widoczne.

-    {{MenuCommand|[Ukryj zaznaczone](Std_HideSelection.md)}}:sprawia, że wybrane obiekty są niewidoczne.

-    {{MenuCommand|[Przełącznik wyboru](Std_ToggleSelectability.md)}}: sprawia, że obiekt nie może być dłużej zaznaczany w oknie [widoku 3D](3D_view/pl.md). Ponowne użycie tego polecenia, anuluje jego efekt działania. Ustawia atrybuty obiektu `Selectable` na wartość `True` lub `False`. Zmień właściwości przez przełączanie wartości obiektu {{PropertyView/pl|Selectable}} w [edytorze właściwości](Property_editor/pl.md).

-    {{MenuCommand|[Wybierz wszystkie wystąpienia](Std_TreeSelectAllInstances.md)}}: zaznacza wszystkie wystąpienia tego obiektu w widoku drzewa.

-    {{MenuCommand|[Wygląd](Std_SetAppearance.md)}}: uruchamia okno dialogowe w celu zmiany koloru i rozmiaru linii i wierzchołków oraz koloru ścian.

-    {{MenuCommand|[Kolor losowy](Std_RandomColor.md)}}: przypisuje obiektowi przypadkowy kolor. Pozwala na określenie koloru obiektu `ShapeColor` atrybutami cząstkowymi `(r,g,b)` w sposób losowy, z pośród zakresu wartości 0 i 1. Zmień właściwość modyfikując {{PropertyView/pl|Kolor kształtu}} w [edytorze właściwości](Property_editor/pl.md).

-    {{MenuCommand|[Wytnij](Std_Cut.md)}}: Opcja jest niedostępna, jeśli kliknięcie prawym przyciskiem myszy nie następuje na obiekcie.

-    {{MenuCommand|[Kopiuj](Std_Copy.md)}}: Kopiuje obiekt do pamięci komputera.

-    {{MenuCommand|[Wklej](Std_Paste.md)}}: Wkleja skopiowany obiekt do dokumentu; kopia jest dodawana do widoku drzewa na ostatniej pozycji.

-    {{MenuCommand|[Usuń](Std_Delete.md)}}: usuwa obiekt z dokumentu, a także z widoku drzewa, wywołując obiekt `removeObject()`.

-    {{MenuCommand|Utilities}}: **(optional)** Dodatkowe polecenia kontekstowe dostarczane przez Środowisko pracy [Draft](Draft_Workbench/pl.md).

Gdy obiekt zostanie wybrany, na przykład, [Draft Linia](Draft_Line/pl.md), i kolejnie wykonamy na nim kliknięcie prawym przyciskiem myszy, mogą być dostępne dodatkowe polecenia:

-    {{MenuCommand|Transform}}: uruchamia widżet transformacji, aby przesunąć lub obrócić obiekt.

-    {{MenuCommand|Ustaw kolor}}: określa kolory obiektu.

-    {{MenuCommand|Spłaszcz ścieżkę}}: **(Draft)** polecenie specjalne dla [Draft Linia](Draft_Line/pl.md).

-    {{MenuCommand|ukryj}}: jeśli opcja jest aktywna, wybrany obiekt zostanie ustawiony jako ukryty.

-    {{MenuCommand|Zaznacz do przeliczenia}}: zaznacza wszystkie obiekty dokumentu jako zmodyfikowane i gotowe do [przeliczenia](Std_Refresh.md).

-    {{MenuCommand|Przelicz}}: Przelicza aktywny obiekt.

-    {{MenuCommand|Zmień nazwę}}: rozpoczyna edycję nazwy zaznaczonego obiektu. Pozwala to na zmianę nazwy atrybutu `Etykieta`, ale nie w odniesieniu do atrybutu `Name`, jako że ten ostatni jest tylko do odczytu.

## Ikonki dodatków {#ikonki_dodatków}

Na domyślnej ikonie obiektu w widoku drzewa może być wyświetlana jedna lub więcej mniejszych ikonek dodatków. Dostępne ikony dodatków i ich znaczenie są wymienione poniżej. {{Version/pl|0.19}}

### ![](images/FreeCAD_Tree_view_recompute.png ) Biały znak kontrolny na niebieskim tle {#freecad_tree_view_recompute.png_biały_znak_kontrolny_na_niebieskim_tle}

Oznacza to, że obiekt musi zostać [przeliczony](Std_Refresh/pl.md), z powodu zmian dokonanych w modelu lub dlatego, że użytkownik zaznaczył obiekt w menu kontekstowym widoku drzewa do ponownego przeliczenia. W większości przypadków ponowne obliczenia są wywoływane automatycznie, ale czasami są opóźniane z powodów wydajnościowych.

### ![](images/FreeCAD_Tree_view_tip.png ) Biała strzałka na zielonym tle {#freecad_tree_view_tip.png_biała_strzałka_na_zielonym_tle}

Oznacza to tak zwany [czubek](PartDesign_Body/pl#Czubek.md) korpusu. Jest to zazwyczaj ostatnia cecha obiektu [zawartość](PartDesign_Body/pl.md) i reprezentuje całą bryłę dla świata zewnętrznego, np. gdy bryła jest eksportowana lub używana w operacjach [logicznych](Part_Boolean/pl.md) środowiska Część. Czubek może być zmieniany przez użytkownika.

### ![](images/FreeCAD_Tree_view_unattached.png ) Fioletowe ogniwo łańcucha na białym tle {#freecad_tree_view_unattached.png_fioletowe_ogniwo_łańcucha_na_białym_tle}

Jest to typowe dla [szkiców](Sketch/pl.md), pierwotnych brył geometrycznych, takich jak sześcian, walec, itp. oraz geometrii [punktu odniesienia](Datum.md). Wskazuje, że obiekt nie jest do niczego przymocowany. Nie ma on przesunięcia dołączenia i pobiera swoją pozycję i wyrównanie wyłącznie z właściwości [umiejscowienie](Placement.md).

Dostępny jest [Poradnik: Podstawy przyłączania](Basic_Attachment_Tutorial.md) wyjaśniający jak radzić sobie z takimi obiektami.

### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Żółty znak X {#freecad_tree_view_notfullyconstrained.png_żółty_znak_x}

Jest to używane tylko dla [szkiców](Sketch/pl.md) i wskazuje, że szkic nie jest w pełni związany. Wewnątrz środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md) liczba pozostałych stopni swobody jest wyświetlana w komunikatach solvera.

### ![](images/FreeCAD_Tree_view_error.png ) Biały wykrzyknik na czerwonym tle {#freecad_tree_view_error.png_biały_wykrzyknik_na_czerwonym_tle}

Wskazuje to, że w obiekcie wystąpił błąd, który należy naprawić. Po przeliczeniu całego dokumentu po najechaniu myszką na obiekt w widoku drzewa zostanie wyświetlona etykietka z opisem błędu. **Uwaga**: Wszystkie inne obiekty zależne od obiektu w stanie błędu, nie zostaną poprawnie przeliczone, mogą więc nadal prezentować nieaktualny stan.


{{Interface navi

}} {{Std Base navi}} 
