# Tree view/pl
## Wprowadzenie

**Widok drzewa** pojawia się w górnej części panelu **Model** (jeśli [widok połączony](Combo_view/pl.md) jest aktywny) lub jako niezależny panel. Pokazuje wszystkie obiekty zdefiniowane przez użytkownika, które są częścią dokumentu FreeCAD. Widok drzewa jest reprezentacją [struktury dokumentu](Document_structure/pl.md) i wskazuje, jakie informacje są zapisywane na dysku.

Obiekty te niekoniecznie muszą być kształtami geometrycznymi widocznymi w [oknie widoku 3D](3D_view.md), ale mogą również zawierać obiekty danych utworzone za pomocą dowolnego [Środowiska pracy](Workbenches.md).

![](images/FreeCAD_Tree_view.png )



*Widok drzewa pokazujący różne elementy w dokumencie.*



## Praca z widokiem drzewa 

Domyślnie, zawsze gdy tworzony jest nowy obiekt, jest on dodawany na końcu listy w widoku drzewa. Widok drzewa umożliwia zarządzanie obiektami w celu utrzymania ich w zorganizowanym szyku.
Pozwala na tworzenie [grup](Std_Group/pl.md), przesuwanie obiektów wewnątrz grup, przesuwanie grup wewnątrz innych grup, zmianę nazwy obiektów, kopiowanie obiektów, usuwanie obiektów i używając opcji z [menu podręcznego](#Menu_podręczne.md).

Wiele operacji tworzy obiekty, które są zależne od wcześniej utworzonego obiektu. W tym przypadku widok drzewa pokazuje tę zależność poprzez pochłanianie starszego obiektu wewnątrz nowego obiektu. Rozwijanie i zwijanie obiektów w widoku drzewa pokazuje parametryczną historię tego obiektu. Obiekty głębiej położone wewnątrz innych są starsze, natomiast obiekty znajdujące się na zewnątrz są nowsze i pochodzą od obiektów starszych. Modyfikując obiekty wewnętrzne, operacje parametryczne rozprzestrzeniają się aż do góry, generując nowy wynik.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history.png  style="width:" height="300px;">



*Najwyższy z obiektów jest tworzony przez wykonywanie operacji parametrycznych na obiektach, które same zostały utworzone przez poprzednie operacje. <br>
Pełne rozwinięcie drzewa na wielu poziomach ujawnia oryginalne elementy, które zostały użyte do utworzenia brył cząstkowych.*



### Kolumny widoku drzewa 

Widok drzewa zawsze wyświetla kolumnę z ikonami i etykietami obiektów. Opcjonalnie mogą być również wyświetlane dwie dodatkowe kolumny. Aby włączyć te kolumny, kliknij prawym przyciskiem myszy widok drzewa i w menu podręcznym wybierz **Ustawienia Widoku drzewa**, a następnie **Pokaż kolumnę opisu** *({{Version/pl|0.21}})* i / lub **Pokaż nazwę wewnętrzną** *(<small>(v1.0)</small> )*. Nagłówki kolumn są dodawane, jeśli wyświetlana jest więcej niż jedna kolumna. Należy pamiętać, że wewnętrzne nazwy obiektów nie mogą zostać zmienione.



### Edycja etykiety obiektu 

Zaznacz obiekt w pierwszej kolumnie i naciśnij przycisku **F2** *(w systemach Linux i Windows)* lub **Enter** *(na macOS)*, pozwala na edycję właściwości **Etykieta** obiektu. Tę właściwość można również edytować za pomocą opcji menu kontekstowego **Zmień nazwę** lub w sekcji [Edytora właściwości](Property_editor/pl.md).



### Edytuj opis obiektu 

Obiekt może opcjonalnie posiadać opis. Informacje te są przechowywane w jego właściwości **Etykieta2**. Jeśli wyświetlana jest kolumna opisu, można edytować tę właściwość, wybierając obiekt w tej kolumnie i naciskając przycisk **F2** *(w systemach Linux i Windows)* lub **Enter** *(na macOS)*. Właściwość tę można również zmienić w [Edytorze właściwości](Property_editor/pl.md).



### Menu podręczne 

Opcje w menu kontekstowym widoku drzewa zależą od wybranych obiektów i aktualnie aktywnego środowiska pracy. Aby wyświetlić to menu, kliknij prawym przyciskiem myszy tło listy, kliknij prawym przyciskiem myszy obiekt na liście lub zaznacz wiele obiektów na liście, a następnie kliknij prawym przyciskiem myszy jeden z nich.



### Klawisze modyfikujące 

W widoku drzewa można używać zwykłych klawiszy modyfikujących. Modyfikatory można również łączyć.

-    **Ctrl**: przytrzymaj ten klawisz, aby zaznaczyć wiele obiektów.

-    **Shift**: przytrzymanie tego klawisza powoduje zaznaczenie wszystkich obiektów pomiędzy poprzednio zaznaczonym obiektem a następnym zaznaczonym obiektem.



### Skróty klawiaturowe 

Następujące skróty klawiaturowe są dostępne, gdy aktywny jest widok drzewa:

-    **Ctrl**\+**F**: otwiera okno wyszukiwania na dole drzewa, umożliwiając wyszukiwanie i docieranie do obiektów za pomocą ich nazw wewnętrznych lub etykiet.

-   Rozwijanie i zwijanie za pomocą kombinacji klawiszy **Alt**+**Arrow**: {{Version/pl|0.20}}
    -   
        **Alt**
        
        \+**Lewy**: zwija zaznaczony element *(lub elementy)*.

    -   
        **Alt**
        
        \+**Prawo**: rozwija zaznaczony element *(elementy)*.

    -   
        **Alt**
        
        \+**Up**: rozwija zaznaczony element*(y)*, zwijając wszystkie jego elementy podrzędne z poziomu pierwszego *(głębsze elementy podrzędne pozostają bez zmian)*.

    -   
        **Alt**
        
        \+**Down**: rozwija zaznaczony element *(elementy)* wraz z rozwijając elementy podrzędne z pierwszego poziomu *(głębsze elementy podrzędne pozostają bez zmian)*.



## Ikonki dodatków 

Na domyślnej ikonie obiektu w widoku drzewa może być wyświetlana jedna lub więcej mniejszych ikonek dodatków. Dostępne ikony dodatków i ich znaczenie są wymienione poniżej.



### ![](images/FreeCAD_Tree_view_recompute.png ) Biały znak kontrolny na niebieskim tle 

Oznacza to, że obiekt musi zostać [przeliczony](Std_Refresh/pl.md), z powodu zmian dokonanych w modelu lub dlatego, że użytkownik zaznaczył obiekt w menu kontekstowym widoku drzewa do ponownego przeliczenia. W większości przypadków ponowne obliczenia są wywoływane automatycznie, ale czasami są opóźniane z powodów wydajnościowych.



### ![](images/FreeCAD_Tree_view_error.png ) Biały wykrzyknik na czerwonym tle 

Wskazuje to, że w obiekcie wystąpił błąd, który należy naprawić. Po przeliczeniu całego dokumentu po najechaniu myszką na obiekt w widoku drzewa zostanie wyświetlona etykietka z opisem błędu. **Uwaga**: Wszystkie inne obiekty zależne od obiektu w stanie błędu, nie zostaną poprawnie przeliczone, mogą więc nadal prezentować nieaktualny stan.



### ![](images/FreeCAD_Tree_view_unattached.png ) Fioletowe ogniwo łańcucha na białym tle 

Jest to typowe dla [szkiców](Sketch/pl.md), prymitywów [środowiska Projekt Części](PartDesign_Workbench/pl.md), takich jak sześcian, walec, itp. oraz geometrii [konstrukcyjnej](Datum/pl.md). Wskazuje, że obiekt nie jest do niczego przymocowany. Nie ma on przesunięcia dołączenia i pobiera swoją pozycję i wyrównanie wyłącznie z właściwości [umiejscowienie](Placement/pl.md).

Dostępny jest [Poradnik: Podstawy przyłączania](Basic_Attachment_Tutorial.md) wyjaśniający jak radzić sobie z takimi obiektami.



### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Żółty znak X 

Jest on używany tylko w odniesieniu do [szkiców](Sketch/pl.md) i wskazuje, że szkic nie jest w pełni związany. Jeśli szkic jest w trybie [edycji](Sketcher_EditSketch/pl.md), liczba pozostałych stopni swobody jest wyświetlana w [komunikatach solvera](Sketcher_Dialog/pl#Komunikaty_solvera.md).



### ![](images/FreeCAD_Tree_view_tip.png ) Biała strzałka na zielonym tle 

Oznacza to tak zwany [czubek](PartDesign_Body/pl#Czubek.md) korpusu. Jest to zazwyczaj ostatnia cecha obiektu [zawartość](PartDesign_Body/pl.md) i reprezentuje całą bryłę dla świata zewnętrznego, np. gdy bryła jest eksportowana lub używana w operacjach [logicznych](Part_Boolean/pl.md) środowiska Część. Czubek może być zmieniany przez użytkownika.



### ![](images/FreeCAD_Tree_view_suppressed.png ) Czerwony backslash 


{{Version/pl|1.0}}

Wskazuje to na wyłączoną funkcję środowiska [Projekt Części](PartDesign_Workbench/pl.md).



### ![](images/FreeCAD_Tree_view_link.png ) Zakrzywiona biała strzałka w górę 

To oznacza [zlinkowany](Std_LinkMake/pl.md) obiekt.



### ![](images/FreeCAD_Tree_view_link_external.png ) Dwie zakrzywione białe strzałki w górę 

To oznacza [zlinkowany](Std_LinkMake/pl.md) obiekt załadowany z zewnętrznego dokumentu.



### ![](images/FreeCAD_Tree_view_hidden.png ) Symbol oka 

Oznacza to, że obiekt będzie ukryty w Widoku drzewa, jeśli opcja menu podręcznego **Pokaż elementy ukryte w Widoku drzewa** zostanie odznaczona.



### ![](images/FreeCAD_Tree_view_frozen.png ) Cyjanowy kryształ lodu 


{{Version/pl|1.0}}

Wskazuje to na [zamrożony](Std_ToggleFreeze/pl.md) obiekt, który nie jest ponownie przeliczany, gdy zmieniają się jego obiekty nadrzędne.



## Ustawienia

Zobacz [Widok połączony](Combo_view/pl#Ustawienia.md).


{{Interface_navi

}} {{Std_Base_navi}}



---
⏵ [documentation index](../README.md) > Tree view/pl
