---
 GuiCommand:
   Name: PartDesign Chamfer
   Name/pl: Projekt Części: Sfazowanie
   MenuLocation: Projekt Części , Zastosuj funkcję ulepszenia , Sfazowanie
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: PartDesign_Fillet/pl
---

# PartDesign Chamfer/pl



## Opis

Narzędzie <img alt="" src=images/PartDesign_Chamfer.svg  style="width:24px;"> **Sfazowanie** tworzy fazki na wybranych krawędziach obiektu. Dodaje ono obiekt **Sfazowanie** do dokumentu z odpowiadającą mu reprezentacją w oknie [Widoku drzewa](Tree_view/pl.md).



## Użycie



### Dodanie fazki 

1.  Opcjonalnie [zaznacz](PartDesign_Body/pl#Aktywny_status.md) bryłę do fazowania.
2.  Istnieje kilka sposobów wyboru krawędzi do fazowania:
    -   Wybierz jedną lub więcej krawędzi bryły indywidualnie.
    -   Wybierz jedną lub więcej ścian bryły, aby wybrać wszystkie ich krawędzie.
    -   Wybierz element *(zwykle ostatni)* bryły, aby wybrać wszystkie jej krawędzie. {{Version/pl|0.20}}
3.  W przypadku łańcucha stycznie połączonych krawędzi należy wybrać tylko jedną krawędź, a fazowanie będzie propagowane wzdłuż łańcucha.
4.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/PartDesign_Chamfer.svg" width=16px> Sfazowanie**.
    -   Wybierz z menu opcję **Projekt Części → Zastosuj funkcję ulepszenia → <img src="images/PartDesign_Chamfer.svg" width=16px> Sfazowanie**.
5.  Jeśli nie ma aktywnej Zawartości, a w dokumencie znajdują się dwie lub więcej, otworzy się okno dialogowe **Wymagana jest aktywna zawartość** z monitem o aktywację jednej z nich. Jeśli w dokumencie znajduje się tylko jedna Zawartość, zostanie ona aktywowana automatycznie.
6.  Otworzy się [Panel zadań](Task_panel/pl.md) **Parametry sfazowania**. Więcej informacji można znaleźć w akapicie [Opcje](#Opcje.md).
7.  Naciśnij przycisk **OK**, aby zakończyć.



### Edycja sfazowania 

1.  Wykonaj jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt Sfazowania w oknie [Widoku drzewa](Tree_view/pl.md).
    -   Kliknij obiekt Sfazowania prawym przyciskiem myszy w oknie [Widok drzewa](Tree_view/pl.md) i wybierz **Edycja funkcji sfazowania** z menu kontekstowego.
2.  Otworzy się panel [Panel zadań](Task_panel/pl.md) **Parametry sfazowania**. Więcej informacji można znaleźć w punkcie [Opcje](#Opcje.md).
3.  Naciśnij przycisk **OK**, aby zakończyć.



## Opcje

-   Aby dodać krawędzie, wykonaj jedną z poniższych czynności:
    -   Naciśnij przycisk **Dodaj**, aby rozpocząć zaznaczanie krawędzi i / lub ścian w oknie [Widoku 3D](3D_view/pl.md).
    -   Aby zaznaczyć wszystkie pozostałe krawędzie, wykonaj następujące czynności:
        1.  W razie potrzeby naciśnij przycisk **Dodaj**.
        2.  Użyj skrótu klawiaturowego **Ctrl** + **Shift** + **A** lub kliknij listę prawym przyciskiem myszy i wybierz **Dodaj wszystkie krawędzie** z menu podręcznego. {{Version/pl|0.20}}
-   Aby usunąć krawędzie, wykonaj jedną z następujących czynności:
    -   Naciśnij przycisk **Usuń**, aby rozpocząć odznaczanie krawędzi i / lub ścian w oknie [Widoku 3D](3D_view/pl.md). Wybrane elementy są podświetlone na fioletowo.
    -   Zaznacz jeden lub więcej elementów na liście i naciśnij klawisz **Del** lub kliknij listę prawym przyciskiem myszki i wybierz **Usuń** z menu podręcznego.
-   Określ **Typ** fazowania:
    -   
        **Wymiary równe**
        
        : Jedna odległość jest używana do umieszczenia obu krawędzi fazowania.

    -   
        **Dwa wymiary**
        
        : Do umieszczenia krawędzi fazowania używane są dwie odległości.

    -   
        **Wymiar i kąt**
        
        : Do umieszczenia jednej krawędzi fazowania używana jest odległość, a umieszczenie drugiej krawędzi fazowania jest definiowane przez kąt sfazowania.
-   Naciśnij przycisk **<img src="images/PartDesign_Flip_Direction.svg" width=16px> Odwróć kierunek**, aby odwrócić kierunek fazowania *(nieaktywne dla **Wymiary równe**)*.
-   Ustaw **Rozmiar** fazowania.
-   Ustaw **Rozmiar 2** fazowania *(dostępne tylko po wybraniu opcji **Dwa wymiary**)*.
-   Ustaw **Kąt** fazowania *(dostępne tylko po wybraniu opcji **Wymiar i kąt**)*.
-   Wyznacz **Promień** zaokrąglenia.
-   Zaznacz pole wyboru **Użyj wszystkich krawędzi**, aby wybrać wszystkie krawędzie poprzedniego elementu. Spowoduje to dezaktywację listy wyboru i powiązanych przycisków. {{Version/pl|0.20}}



## Uwagi

-   Sfazowanie środowiska pracy Projekt Części nie należy mylić z [Sfazowanie](Part_Fillet/pl.md) środowiska Część. Jeśli nie wiesz, co robisz [Część: Sfazowanie](Part_Chamfer/pl.md) nie powinno być używane na Zawartości środowiska Projekt Części. Zobacz stronę [Część i Projekt Części](Part_and_PartDesign/pl.md).
-   Sfazowania nie mogą całkowicie wchłonąć sąsiednich ścian.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Sfazowanie środowiska Projekt Części wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Baza|LinkSub**: Powiązanie z wybranymi krawędziami i ścianami elementu nadrzędnego. Może być linkiem tylko do elementu nadrzędnego, jeśli parametr **Użyj wszystkich krawędzi** ma wartość {{TRUE/pl}}.

-    **Wsparcie przekształcenia|Bool**: Jeśli wartość jest ustawiona na {{TRUE/pl}} zostanie użyty sfazowany kształt addytywnego / subtraktywnego elementu nadrzędnego, gdy sfazowany obiekt zostanie włączony do [szyku](PartDesign_Workbench/pl#Narzędzia_do_przekształcania.md), w przeciwnym razie zostanie użyty tylko kształt samej fazy. Domyślną wartością jest {{FALSE/pl}}.

-    **Dodaj kształt podrzędny|PartShape|ukryty**.

-    **Cecha podstawowa|Link|ukryty**: Odnośnik do elementu nadrzędnego.

-    **_ Body|LinkHidden|ukryty**: Link do elementu nadrzędnego.


{{Properties_Title|Sfazowanie}}

-    **Typ sfazowania|Enumeration**: Typ fazowania: {{value|Wymiary równe}} *(domyślnie)*, {{value|Dwa wymiary}} lub {{value|Wymiar i kąt}}.

-    **Rozmiar|QuantityConstraint**: Pierwsza odległość fazowania. Domyślnie {{value|1 mm}}.

-    **Rozmiar2|QuantityConstraint**: Druga odległość fazowania. Używane tylko jeśli **Typ sfazowania** to {{Value|Dwa wymiary}}. Wartość domyślna to {{value|1 mm}}.

-    **Kąt|Angle**: Kąt fazowania. Używany tylko jeśli **Typ sfazowania** to {{Value|Wymiar i kąt}}. Wartość domyślna to {{value|45 °}}.

-    **Odwróć kierunek|Bool**: Jeśli ustawiono wartość {{TRUE/pl}}, kierunek fazowania zostanie odwrócony. Nie używane, jeśli **Typ sfazowania** to {{Value|Wymiary równe}}. Domyślnia wartość to {{FALSE/pl}}.

-    **Użyj wszystkich krawędzi|Bool**: Jeśli wartość to {{TRUE/pl}} wszystkie krawędzie elementu są fazowane, a krawędzie określone przez **Bazę** są ignorowane. Domyślną wartością jest {{FALSE/pl}}.


{{Properties_Title|Projekt Części}}

-    **Ulepsz|Bool**: Jeśli ma wartość {{TRUE/pl}}, nadmiarowe krawędzie są usuwane z wyniku operacji. Wartość domyślna jest określona przez preferencję **Automatycznie udoskonal model po wykonaniu operacji opartej na szkicu**. Zobacz stronę [Projekt Części: Ustawienia](PartDesign_Preferences/pl#Ogólne.md).



## Znane problemy 

Zobacz stronę [Zaokrąglenie](PartDesign_Fillet/pl#Znane_problemy.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Chamfer/pl
