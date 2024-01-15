---
 GuiCommand:
   Name: PartDesign Fillet
   Name/pl: Projekt Części: Zaokrąglenie
   MenuLocation: Projekt Części , Zastosuj funkcję ulepszenia , Zaokrąglenie
   Workbenches: PartDesign_Workbench/pl
   SeeAlso: PartDesign_Chamfer/pl
---

# PartDesign Fillet/pl



## Opis

Narzędzie <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> **Zaokrąglenie** tworzy zaokrąglenia na wybranych krawędziach obiektu. Dodaje on do dokumentu obiekt **Zaokrąglenie** wraz z jego reprezentacją w oknie [Widoku drzewa](Tree_view/pl.md).



## Użycie



### Dodanie zaokrąglenia 

1.  Opcjonalnie [zaznacz](PartDesign_Body/pl#Aktywny_status.md) bryłę do zaokrąglenia.
2.  Istnieje kilka sposobów wyboru krawędzi do zaokrąglenia:
    -   Wybierz jedną lub więcej krawędzi bryły indywidualnie.
    -   Wybierz jedną lub więcej ścian bryły, aby wybrać wszystkie ich krawędzie.
    -   Wybierz element (zwykle ostatni) bryły, aby wybrać wszystkie jej krawędzie. {{Version/pl|0.20}}
3.  W przypadku łańcucha stycznie połączonych krawędzi należy wybrać tylko jedną krawędź, zaokrąglenie będzie rozchodzić się wzdłuż łańcucha.
4.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/PartDesign_Fillet.svg" width=16px> '''Zaokrąglenie'''**.
    -   Wybierz z nemu opcję **Projekt Części → Zastosuj funkcję ulepszenia → <img src="images/PartDesign_Fillet.svg" width=16px> Zaokrąglenie**.
5.  Jeśli nie ma aktywnej Zawartości, a w dokumencie znajdują się dwie lub więcej, otworzy się okno dialogowe **Wymagana jest aktywna zawartość** z monitem o aktywację jednej z nich. Jeśli w dokumencie znajduje się tylko jedna Zawartość, zostanie ona aktywowana automatycznie.
6.  Otworzy się [Panel zadań](Task_panel/pl.md) **Parametry zaokrąglenia**. Więcej informacji można znaleźć w akapicie [Opcje](#Opcje.md).
7.  Naciśnij przycisk **OK**, aby zakończyć.



### Edycja zaokrąglenia 

1.  Wykonaj jedną z poniższych czynności:
    -   Kliknij dwukrotnie obiekt Szkic w oknie [Widoku drzewa](Tree_view/pl.md).
    -   Kliknij obiekt Szkic prawym przyciskiem myszy w oknie [Widoku drzewa](Tree_view/pl.md) i wybierz **Edycja funkcji zaokrąglenia** z menu podręcznego.
2.  Otworzy się [Panel zadań](Task_panel/pl.md) **Parametry zaokrąglenia**. Więcej informacji można znaleźć w punkcie [Opcje](#Opcje.md).
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
-   Wyznacz **Promień** zaokrąglenia.
-   Zaznacz pole wyboru **Użyj wszystkich krawędzi**, aby wybrać wszystkie krawędzie poprzedniego elementu. Spowoduje to dezaktywację listy wyboru i powiązanych przycisków. {{Version/pl|0.20}}



## Uwagi

-   Zaokrąglenia środowiska pracy Projekt Części nie należy mylić z [Zaokrągleniem](Part_Fillet/pl.md) środowiska Część. Jeśli nie wiesz, co robisz [Część: Zaokrąglenie](Part_Fillet/pl.md) nie powinno być używane na Zawartości środowiska Projekt Części. Zobacz stronę [Część i Projekt Części](Part_and_PartDesign/pl.md).
-   Zaokrąglenia nie mogą całkowicie wchłonąć sąsiednich ścian.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt Zaokrąglenie środowiska Projekt Części wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Baza|LinkSub**: Powiązanie z wybranymi krawędziami i ścianami elementu nadrzędnego. Może być linkiem tylko do elementu nadrzędnego, jeśli parametr **Użyj wszystkich krawędzi** ma wartość {{TRUE/pl}}.

-    **Wsparcie przekształcenia|Bool**: Jeśli wartość jest ustawiona na {{TRUE/pl}} zostanie użyty zaokrąglony kształt addytywnego / subtraktywnego elementu nadrzędnego, gdy obiekt zaokrąglenia zostanie włączony do [szyku](PartDesign_Workbench/pl#Narzędzia_do_przekształcania.md), w przeciwnym razie zostanie użyty tylko kształt samego zaokrąglenia. Domyślną wartością jest {{FALSE/pl}}.

-    **Dodaj kształt podrzędny|PartShape|ukryty**.

-    **Cecha podstawowa|Link|ukryty**: Odnośnik do elementu nadrzędnego.

-    **_ Body|LinkHidden|ukryty**: Link do elementu nadrzędnego.


{{Properties_Title|Zaokrąglenie}}

-    **Promień|QuantityConstraint**: Promień zaokrąglenia. Domyślnie {{value|1 mm}}.

-    **Użyj wszystkich krawędzi|Bool**: Jeśli wartość to {{TRUE/pl}} wszystkie krawędzie elementu są zaokrąglane, a krawędzie określone przez **Bazę** są ignorowane. Domyślną wartością jest {{FALSE/pl}}.


{{Properties_Title|Projekt Części}}

-    **Ulepsz|Bool**: Jeśli ma wartość {{TRUE/pl}}, nadmiarowe krawędzie są usuwane z wyniku operacji. Wartość domyślna jest określona przez preferencję **Automatycznie udoskonal model po wykonaniu operacji opartej na szkicu**. Zobacz stronę [Projekt Części: Ustawienia](PartDesign_Preferences/pl#Ogólne.md).



## Znane problemy 

Zaokrąglenia, fazowania i inne funkcje działające na bryłach zależą od jądra Technologii [OpenCASCADE](OpenCASCADE/pl.md) *(OCCT)*, z której korzysta FreeCAD. Jądro OCCT czasami ma trudności z obsługą zbieżnych ostrych krawędzi, gdzie spotykają się dwie ściany. W takim przypadku FreeCAD może ulec awarii bez wyjaśnienia.

W przypadku uruchomienia z terminala, FreeCAD może wyświetlić taki dziennik po awarii:


{{code|lang=text|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}

Dane wyjściowe odwołują się do funkcji z bibliotek OCCT. Jeśli wystąpi tego typu awaria, problem może wymagać zgłoszenia i rozwiązania w OCCT, a nie w FreeCAD.

Więcej informacji można znaleźć w wątkach na forum:

-   [Błąd Fazowanie większe niż 2 mm rozbija FreeCAD](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Błąd podczas korzystania z zaokrąglenia środowiska Projekt Części](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827).



### Nazewnictwo topologiczne 

Numery krawędzi nie są całkowicie stabilne, dlatego zaleca się zakończenie głównych prac projektowych bryły przed zastosowaniem funkcji takich jak zaokrąglenia i fazowania, w przeciwnym razie krawędzie mogą zmienić nazwy, a zaokrąglone krawędzie prawdopodobnie staną się nieprawidłowe. Gdy właściwość **Użyj wszystkich krawędzi** ({{Version/pl|0.20}}) ma wartość {{TRUE/pl}}, istnieje pewna ochrona przed taką sytuacją. Ponieważ w takich przypadkach używane są wszystkie krawędzie obiektu bazowego i nie ma zależności od indywidualnych nazw krawędzi.

Przeczytaj więcej na stronie [problem nazewnictwa topologicznego](Topological_naming_problem/pl.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/pl
