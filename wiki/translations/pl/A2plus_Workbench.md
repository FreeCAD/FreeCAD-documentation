# <img alt="Ikonka FreeCAD dla środowiska pracy A2plus" src=images/A2p_workbench.svg  style="width:64px;"> A2plus Workbench/pl



## Wprowadzenie




Środowisko pracy A2plus to [zewnętrzne środowisko](External_workbenches/pl.md) do wykonywania [złożeń](Assembly/pl.md) różnych części w programie FreeCAD.

Niniejsza dokumentacja opisuje wersję A2plus **0.4.56 lub nowszą**.



## Instalacja

Środowisko pracy A2plus jest dodatkiem do programu FreeCAD. Można je łatwo zainstalować za pomocą <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) z menu **Przybory → Menadżer dodatków**. A2plus jest w trakcie aktywnego rozwoju i będzie często wzbogacany o nowe funkcje. Dlatego warto go regularnie aktualizować, również za pomocą narzędzia w menu **Przybory → Menadżer dodatków**. Kod A2plus jest przechowywany i rozwijany [na GitHub](https://github.com/kbwbe/A2plus) i może być również zainstalowany ręcznie poprzez skopiowanie go do katalogu **Mod** programu FreeCAD.



## Rozpoczęcie pracy 

Na początku przejdź do paska narzędzi A2plus w programie FreeCAD. Aby utworzyć złożenie, utwórz nowy plik w programie FreeCAD. Na początku plik ten musi zostać zapisany. Zaleca się *(ale nie jest to konieczne)*, aby zapisać go w tym samym folderze, w którym znajdują się części, z których ma zostać wykonany montaż.

Teraz części można dodawać do złożenia za pomocą przycisku na pasku narzędzi <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> lub <img alt="" src=images/A2p_ShapeReference.svg  style="width:24px;">. Przycisk <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> dodaje wszystkie bryły w wybranym pliku jako jedną część. Używając przycisku <img alt="" src=images/A2p_ShapeReference.svg  style="width:24px;"> możesz wybrać, jaki element z pliku ma zostać zaimportowany jako część. W ten sposób można na przykład zaimportować tylko szkic, a następnie złożyć kolejne części, używając szkicu do określenia pozycji części.

Pierwsza dodana część otrzymuje domyślnie stałą pozycję. *(Można to zmienić później za pomocą właściwości części **fixed Position**)*.

Części, które już znajdują się w złożeniu, można klonować za pomocą przycisku z paska narzędzi <img alt="" src=images/A2p_DuplicatePart.svg  style="width:24px;">.

Aby edytować część ze złożenia, zaznacz ją w drzewie modelu i użyj przycisku na pasku narzędzi <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. Spowoduje to otwarcie części w nowej zakładce w programie FreeCAD lub przełączenie do jej zakładki, jeśli plik jest już otwarty.

Aby zaktualizować części zmodyfikowane w złożeniach kliknij na przycisk na pasku narzędzi <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;">. Przycisk paska narzędzi <img alt="" src=images/A2p_RecursiveUpdate.svg  style="width:24px;"> również importuje części, ale rekurencyjnie przez możliwe [montaż podzespołów](#Monta.C5.BC_podzespo.C5.82.C3.B3w.md). Jeśli zaznaczysz jedną lub kilka części w widoku drzewa programu FreeCAD, A2plus poprosi Cię o aktualizację tylko wybranych części.

Zaimportowane części zachowują swoje zewnętrzne zależności i można je edytować. W przypadku ściśle zdefiniowanych części, takich jak śruby, warto jednak, aby ich kształt nie mógł być edytowany. Można to osiągnąć za pomocą przycisku na pasku narzędzi <img alt="" src=images/A2p_ConvertPart.svg  style="width:24px;">, który przekształca wybraną część w statyczną kopię części oryginalnej.

Aby zapisać złożenie i zamknąć je po zakończeniu, można użyć przycisku paska narzędzi <img alt="" src=images/A2p_Save_and_exit.svg  style="width:24px;">.

Przełączanie przycisku paska narzędzi <img alt="" src=images/A2p_CD_OneButton.svg  style="width:24px;"> ustawia sposób, zaznaczenia kilku krawędzi, ścian itp.: albo za pomocą pojedynczego kliknięcia, albo używając **Ctrl** + kliknięcie.



## Montaż

Montaż części odbywa się poprzez dodawanie więzów pomiędzy częściami. Po wprowadzeniu wiązania środowisko pracy A2plus przesuwa części zgodnie z wiązaniem, jeśli jest to możliwe.

Aby utworzyć wiązanie między częściami, przytrzymaj wciśnięty klawisz **Ctrl** i zaznacz każdą krawędź lub powierzchnię dwóch części. Następnie kliknij przycisk na pasku narzędziowym żądanego wiązania. Pojawi się okno dialogowe opisane w rozdziale [wiązania](#Wiązania.md). Wiązanie zostanie dodane do drzewa modelu dołączonego do części, których dotyczy.

W przypadku złożonych wiązań między częściami środowisko pracy A2plus może nie wykonać rozwiązania wiązań. W związku z tym zapoznaj się również z punktem [Rozwiązywanie problemów](#Rozwi.C4.85zywanie_problem.C3.B3w.md), aby poznać strategie rozwiązywania takich przypadków.



### Bieżące monitorowanie 

Im więcej części dodajesz, tym ważniejsze jest, aby je śledzić. Dlatego A2plus oferuje narzędzia do przenoszenia i przeglądania części:

-   Aby przesunąć część w złożeniu, zaznacz ją w drzewie modelu i użyj przycisku na pasku narzędzi <img alt="" src=images/A2p_MovePart.svg  style="width:24px;">. Gdy umieścisz część tam, gdzie chcesz, kliknij lewym przyciskiem myszy. Jeśli przeniesiona część ma już wiązania, zostanie ona odpowiednio umieszczona po naciśnięciu przycisku paska narzędzi <img alt="" src=images/A2p_solver.svg  style="width:24px;">, ponieważ powoduje to rozwiązanie wszystkich więzów złożenia.
-   Aby pokazać wiązanie, wybierz je w drzewie modelu i użyj przycisku na pasku narzędzi <img alt="" src=images/A2p_ViewConnection.svg  style="width:24px;">. Spowoduje to, że cały zespół stanie się przezroczysty i zostaną podświetlone dwa obiekty, które są połączone wiązaniem. Aby powrócić do normalnego widoku, kliknij lewym przyciskiem myszki na złożeniu.
-   Aby pokazać tylko niektóre części złożenia, wybierz te części w drzewie modelu i użyj przycisku paska narzędzi <img alt="" src=images/A2p_Isolate_Element.svg  style="width:24px;">. Alternatywnie możesz ukryć określoną część, zaznaczając ją w drzewie modelu i naciskając klawisz **Spacja**, aby przełączyć jej widoczność.
-   Aby przełączyć widok przezroczystości całego złożenia, możesz użyć przycisku na pasku narzędzi <img alt="" src=images/A2p_ToggleTransparency.svg  style="width:24px;">.
-   Każdą część można uczynić przezroczystą za pomocą normalnej edycji w programie FreeCAD. Jednak czasami ustawienie przezroczystości dla części jest tracone przy ponownym otwieraniu złożenia z powodu błędu w programie FreeCAD. Jako obejście tego problemu możesz użyć przycisku paska narzędzi <img alt="" src=images/A2p_Restore_Transparency.svg  style="width:24px;">, aby przywrócić ustawienia przezroczystości.



### Wiązania

Podczas tworzenia wiązania takie okno dialogowe zostanie wyświetlone po naciśnięciu przycisku paska narzędziowego wiązania:

![](images/A2p_ConstraintPropertiesDialog.png ) 
*Powyżej: Okno dialogowe właściwości wiązań A2plus*

W przypadku niektórych wiązań można modyfikować kierunek wiązania. Za pomocą przycisku **<img src="images/A2p_solver.svg" width=24px> Rozwiąż** można wcześniej sprawdzić, czy to nowe wiązanie może być rozwiązane przez A2plus. Jeśli nie, zajrzyj do rozdziału [Rozwiązywanie problemów](#Rozwi.C4.85zywanie_problem.C3.B3w.md).

Wiązania można wyłączyć, zmieniając ich [widzialność](Std_ToggleVisibility/pl.md). Robi się to przez wybranie wiązania w widoku drzewa i naciśnięcie klawisza **Spacja**. Powoduje to włączenie właściwości **Stłumione**. Wyciszone wiązanie nie jest brane pod uwagę podczas rozwiązywania zespołu.

A2plus zapewnia następujące wiązania:



#### Punkt w punkcie 

Wybierz [wierzchołek](Glossary#Vertex.md) *(punkt)*, okrąg lub sferę na każdej części. Jeśli wybrano okrąg lub sferę, to jej punkt środkowy zostanie użyty w Wiązaniu. Przycisk na pasku narzędzi <img alt="" src=images/A2p_PointIdentity.svg  style="width:24px;"> dodaje wiązanie {{Variable|PunktIdentyfikacja}}, które sprawia, że wierzchołki są zbieżne.



#### Punkt na linii 

Wybierz [wierzchołek](Glossary#Vertex.md) *(punkt)*, lub okrągłą [krawędź](Glossary#Edge.md) *(wybierze jej punkt środkowy)*, lub kulistą [ścinę](Glossary#Face.md) *(również wybierze jej punkt środkowy)* na jednej części i [krawędź](Glossary#Edge.md) na drugiej. Przycisk paska narzędzi <img alt="" src=images/A2p_PointOnLineConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|PunktNaLinii}}. Spowoduje ono umieszczenie wierzchołka na krawędzi.



#### Punkt na płaszczyźnie 

Wybierz [wierzchołek](Glossary#Vertex.md) *(punkt)*, okrągłą [krawędź](Glossary#Edge.md) *(zostanie wybrany jej punkt środkowy)* lub kulistą [ścianę](Glossary#Face.md) *(również zostanie wybrany jej punkt środkowy)* na jednej części i płaszczyznę na drugiej części. Przycisk paska narzędzi <img alt="" src=images/A2p_PointOnPlaneConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|Punkt na płaszczyźnie}}. W oknie dialogowym wiązania można określić przesunięcie między punktem a płaszczyzną. Przesunięcie to można również przerzucić między obiema stronami płaszczyzny. Jeśli przesunięcie wynosi zero, ograniczenie spowoduje umieszczenie wierzchołka na płaszczyźnie.



#### Sfera w sferze 

Wybierz sferyczną [powierzchnię](Glossary#Powierzchnia.md) lub [wierzchołek](Glossary#Wertex.md) *(punkt)* na obu częściach. Przycisk na pasku narzędzi <img alt="" src=images/A2p_SphericalSurfaceConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|sphereCenterIdent}} *(sfera o wspólnym środku)*. Sprawi ono, że środki sfer, środki sfery i wierzchołka lub wierzchołki będą się pokrywać.



#### Okrągła krawędź na okrągłej krawędzi 

Wybierz okrągłą krawędź [krawędź](Glossary#Edge.md) na obu częściach. Przycisk na pasku narzędzi <img alt="" src=images/A2p_CircularEdgeConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|circularEdge}}. W oknie dialogowym wiązania można określić przesunięcie między krawędziami. To przesunięcie może być również odwrócone. Ponadto można ustawić kierunek wiązania i zablokować obrót części. Jeśli przesunięcie wynosi zero, wiązanie spowoduje, że krawędzie będą koncentrycznie leżeć w tej samej płaszczyźnie.



#### Zbieżność osi 

Wybierz cylindryczną [Powierzchnię](Glossary#Face.md) lub liniową [Krawędź](Glossary#Edge.md) na obu częściach. Przycisk na pasku narzędzi <img alt="" src=images/A2p_AxialConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|Zbieżność osi}}. W oknie dialogowym wiązania można określić kierunek osi. W oknie tym można również zablokować obrót części. Wiązanie spowoduje, że osie lub linie będą zbieżne.



#### Równoległość osi 

Wybierz cylindryczną [powierzchnię](Glossary#Face.md) lub liniową [krawędź](Glossary#Edge.md) na obu częściach. Przycisk na pasku narzędzi <img alt="" src=images/A2p_AxisParallelConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|równoległości osi}}. W oknie dialogowym ograniczenia można określić kierunek osi. Ograniczenie sprawi, że osie lub linie będą równoległe.



#### Oś na płaszczyźnie równoległej 

Wybierz cylindryczną [powierzchnię](Glossary#Face.md) lub liniową [krawędź](Glossary#Edge.md) na jednej części i płaszczyznę na drugiej części. Przycisk paska narzędzi <img alt="" src=images/A2p_AxisPlaneParallelConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|Oś na płaszczyźnie równoległej}}. Dzięki temu wiązaniu oś lub prosta będzie równoległa do płaszczyzny.



#### Oś na płaszczyźnie normalnej 

Wybierz cylindryczną [powierzchnię](Glossary#Face.md) lub liniową [krawędź](Glossary#Edge.md) na jednej części i płaszczyznę na drugiej części. Przycisk paska narzędzi <img alt="" src=images/A2p_AxisPlaneNormalConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|Oś na płaszczyźnie normalnej}}. Wiązanie spowoduje, że oś lub linia będzie normalna do płaszczyzny.



#### Kąt osi na płaszczyźnie 

Wybierz cylindryczną [powierzchnię](Glossary#Face.md) lub liniową [krawędź](Glossary#Edge.md) na jednej części i płaszczyznę na drugiej części. Przycisk paska narzędzi <img alt="" src=images/A2p_AxisPlaneAngleConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|axisPlaneAngleAngle}}. Początkowo wiązanie sprawi, że oś będzie równoległa do płaszczyzny. Następnie można dostosować kąt dla osi w pojawiającym się oknie dialogowym ustawień wiązania.



#### Równoległe płaszczyzny 

Zaznacz płaszczyznę na obu częściach. Przycisk na pasku narzędzi <img alt="" src=images/A2p_PlanesParallelConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|RównoległePłaszczyzny}}. W oknie dialogowym wiązania można określić kierunek wiązania. Użycie tego wiązania spowoduje, że płaszczyzny będą równoległe.



#### Płaszczyzna na płaszczyźnie 

Wybierz płaszczyznę na obu częściach. Przycisk na pasku narzędzi <img alt="" src=images/A2p_PlaneCoincidentConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|Zbieżność płaszczyzn}}. Okno dialogowe wiązania pozwala określić kierunek wiązania i przesunięcie między płaszczyznami. Przesunięcie to może być również odwrócone. Jeśli przesunięcie wynosi zero, wiązanie spowoduje, że płaszczyzny będą się pokrywać.



#### Płaszczyzna kątowa 

Wybierz płaszczyznę na obu częściach. Przycisk paska narzędzi <img alt="" src=images/A2p_AngleConstraint.svg  style="width:24px;"> dodaje wiązanie {{Variable|angledPlanes}}. Okno dialogowe wiązania pozwala określić kąt między płaszczyznami. Wiązanie sprawi, że płaszczyzny będą najpierw równoległe, a następnie ustawi określony kąt.



#### Zbieżność w środku masy 

Wybierz zamkniętą [krawędź](Glossary#Edge.md) lub płaszczyznę na obu częściach. Przycisk paska narzędzi <img alt="" src=images/A2p_CenterOfMassConstraint.svg  style="width:24px;"> dodaje ograniczenie {{Variable|centerOfMass}}. Okno dialogowe wiązania pozwala określić przesunięcie między krawędziami lub płaszczyznami. Przesunięcie to można również odwrócić. Ponadto można ustawić kierunek wiązania i zablokować obrót części. Jeśli przesunięcie wynosi zero, wiązanie umieści krawędzie lub płaszczyzny w tej samej płaszczyźnie.



### Montaż podzespołów 

Złożenie może zawierać inne złożenia. Dodaje się je jak części, naciskając przycisk paska narzędzi <img alt="" src=images/A2p_ImportPart.svg  style="width:24px;"> i wybierając plik ***.FCStd** zawierający zespół. Takie podzespoły mogą być również edytowane jak części za pomocą przycisku paska narzędzi <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. W przypadku wyższych etapów montażu należy upewnić się, że zespół został zaktualizowany rekursywnie za pomocą przycisku paska narzędzi <img alt="" src=images/A2p_RecursiveUpdate.svg  style="width:24px;"> po wprowadzeniu zmian.



## Operowanie wiązaniami 

Możliwe wiązania dla zaznaczenia są wyświetlane na pasku narzędzi i w oknie dialogowym *Narzędzia wiązań* poprzez włączenie odpowiednich przycisków. Okno dialogowe *Narzędzia wiązań* jest otwierane za pomocą przycisku na pasku narzędzi <img alt="" src=images/A2p_DefineConstraints.svg  style="width:24px;">. Powinno ono pozostać otwarte, aby móc szybko dodać kilka wiązań do zespołu.

Istniejące wiązania mogą być edytowane poprzez zaznaczenie ich w drzewie modelu, a następnie dwukrotne kliknięcie na nie lub użycie przycisku na pasku narzędzi <img alt="" src=images/A2p_EditConstraint.svg  style="width:24px;">. Umożliwi to otwarcie okna dialogowego *Właściwości wiązania*.

Wiązania można tymczasowo wyciszyć, zaznaczając je w drzewie modelu i zmieniając właściwość elementu drzewa **Stłumione**.

Wiązania mogą zostać usunięte poprzez zaznaczenie ich w drzewie modelu i naciśnięcie przycisku **Del** lub poprzez zaznaczenie części z wiązaniami w drzewie modelu i użycie przycisku paska narzędzi <img alt="" src=images/A2p_DeleteConnections.svg  style="width:24px;">.

Wszystkie wiązania mogą być rozwiązane w dowolnym momencie za pomocą przycisku paska narzędzi <img alt="" src=images/A2p_solver.svg  style="width:24px;">. Jeśli przycisk paska narzędzi <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width:24px;"> jest włączony, rozwiązanie jest wykonywane automatycznie po każdej edycji wiązania.

Przycisk paska narzędzi <img alt="" src=images/A2p_FlipConstraint.svg  style="width:24px;"> wpływa na ostatnio dodane wiązanie. Odwraca on kierunek wiązania.

Za pomocą narzędzia <img alt="" src=images/A2p_CD_ConstraintViewer.svg  style="width:24px;"> można wyświetlać i sprawdzać istniejące wiązania. Po kliknięciu pojawi się okno dialogowe. Następnie należy wybrać część w drzewie i kliknąć przycisk **Importuj z drzewa**, aby uzyskać wszystkie wiązania tej części, lub wybrać jedno lub więcej wiązań w drzewie i kliknąć przycisk **Importuj z drzewa**. W rezultacie otrzymasz wszystkie informacje o ograniczeniach. Klikając w kolumnie \"Pomiń\" można wyłączyć pojedyncze wiązanie. Więcej informacji można znaleźć w podpowiedziach innych przycisków okna dialogowego.



## Lista części 

Aby stworzyć listę części dla złożenia, poszczególne części złożenia muszą otrzymać informacje, które mogą być odczytane przez A2plus. Robi się to poprzez edycję części za pomocą przycisku na pasku narzędzi <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">. W otwartej części naciśnij przycisk paska narzędzi <img alt="" src=images/A2p_PartsInfo.svg  style="width:24px;"> i zostanie utworzony [arkusz kalkulacyjny](Spreadsheet_Workbench/pl.md) nazwany *#PARTINFO#*.

Struktura arkusza kalkulacyjnego wygląda następująco:

![](images/A2p_PartinfoTable.png )

Wypełnij szare pola informacjami, które chcesz mieć na docelowej liście części.

W złożeniu lub podzespole użyj przycisku paska narzędzi <img alt="" src=images/A2p_PartsList.svg  style="width:24px;">. Pojawi się pytanie, czy chcesz iterować rekurencyjnie po wszystkich podzespołach. Kliknij na *Yes*. Spowoduje to utworzenie nowego arkusza kalkulacyjnego o nazwie *#PARTSLIST#*. Zawiera on informacje z różnych arkuszy kalkulacyjnych *#PARTSINFO#* części na liście takiej jak ta:

![](images/A2p_PartslistTable.png )

Pozycja *(POS)* jest automatycznie ustawiana zgodnie z wyglądem części w drzewie modelu. Część najwyższego poziomu otrzyma POS 1.

Ilość *(QTY)* jest automatycznie obliczana na podstawie złożenia. Jeśli część występuje dwukrotnie w zespole, otrzyma QTY 2.

Jeśli zaktualizowałeś informacje o części, możesz odświeżyć listę części, naciskając ponownie przycisk paska narzędzi <img alt="" src=images/A2p_PartsList.svg  style="width:24px;">.

Dla złożeń podrzędnych można również utworzyć arkusz informacyjny za pomocą przycisku paska narzędzi <img alt="" src=images/A2p_PartsInfo.svg  style="width:24px;">. Podczas tworzenia lub aktualizowania listy części głównego złożenia informacje te będą używane, jeśli klikniesz *Nie* na pytanie, czy chcesz iterować rekurencyjnie po wszystkich podzespołach. Wówczas różne części nie znajdują się na liście części, a jedynie w złożeniach podrzędnych.



## Funkcje specjalne 



### Struktura złożenia 

Przycisk paska narzędzi <img alt="" src=images/A2p_Treeview.svg  style="width:24px;"> tworzy plik HTML ze strukturą złożenia. Plik zostanie domyślnie utworzony w folderze pliku złożenia. Struktura wygląda następująco:

:   ![](images/A2p_Dependency-Tree.jpg )



### Stopnie swobody 

Przycisk <img alt="" src=images/A2p_DOFs.svg  style="width:24px;"> oznacza każdą część złożenia z jej stopniami swobody. Ponadto wyświetla listę wszystkich części i ich zależności. Lista jest wyprowadzana do widżetu FreeCAD *Widok raportu*. Jeśli widżet ten nie jest obecnie widoczny, można go wyświetlić, klikając prawym przyciskiem myszy pustą część obszaru paska narzędzi FreeCAD, a następnie wybierając go w wyskakującym menu podręcznym lub za pomocą menu **Widok → Panele → [Widok raportu](Report_view/pl.md)**.

Etykiety stopni swobody można usunąć, klikając ponownie przycisk <img alt="" src=images/A2p_DOFs.svg  style="width:24px;">.



### Etykiety części 

Przycisk <img alt="" src=images/A2p_PartLabel.svg  style="width:24px;"> oznacza każdą część złożenia w widoku 3D jej nazwą. Etykiety części można usunąć, klikając ponownie przycisk <img alt="" src=images/A2p_PartLabel.svg  style="width:24px;">.



### Kształt całego złożenia 

Czasami konieczne jest połączenie całego złożenia w jeden kształt. Kształt ten może być następnie użyty do drukowania 3D w środowisku [Siatka](Mesh_Workbench/pl.md) lub do rysowania w środowisku [Rysunek Techniczny](TechDraw_Workbench/pl.md). Jest on tworzony za pomocą przycisku paska narzędzi <img alt="" src=images/A2p_SimpleAssemblyShape.svg  style="width:24px;">. Kształt nie jest domyślnie widoczny. Użyj tego samego przycisku paska narzędzi, aby zaktualizować kształt w przypadku zmian w złożeniu.



### Konwersja ścieżek bezwzględnych na względne 

Za pomocą opcji menu **A2plus → Misc → [<img src=images/A2p_SetRelativePathes.svg style="width:24px"> Konwertuj bezwzględne ścieżki importowanych części na względne** można konwertować ścieżki importowanych części.



## Ustawienia

Dostęp do konfiguracji środowiska pracy A2plus można uzyskać poprzez menu FreeCAD **Edycja → [Preferencje ...](Preferences_Editor/pl.md)** i tam w sekcji *A2plus*. Można ustawić następujące opcje:



### Domyślna metoda rozwiązywania 

Użycie rozwiązywania układów cząstkowych: Rozwiązywanie rozpoczyna się od części, która ma właściwość **Pozycja ustalona** ustawioną na {{true/pl}} i części do niej związanej. Wszystkie pozostałe części nie podlegają obliczeniom. Jeśli uda się znaleźć rozwiązanie, do obliczeń dodawana jest następna związana część i tak dalej. Użyj \"magnetycznego\" solwera, rozwiązującego wszystkie części naraz: Solwer próbuje przesunąć wszystkie części naraz w kierunku części, która ma właściwość **Pozycja ustalona** ustawioną na \"true\". Należy pamiętać, że w większości przypadków obliczenie rozwiązania zajmie więcej czasu. Wymuś stałą pozycję: Ustawia właściwość **Pozycja ustalona** na wartość {{true/pl}} dla wszystkich części w złożeniu. Wówczas nie są wykonywane żadne obliczenia, ponieważ wszystkie części będą zawsze ustawione w pozycjach, w których zostały utworzone.



### Domyślne działanie solvera 

Rozwiąż automatycznie, jeśli właściwość wiązania zostanie zmieniona : Rozwiązywanie zostanie uruchomione automatycznie. Tak samo, jak użycie przycisku paska narzędzi <img alt="" src=images/A2p_ToggleAutoSolve.svg  style="width:24px;">.



### Działanie podczas aktualizacji zaimportowanych części 

Oblicz ponownie zaimportowane części przed ich aktualizacją: Wszystkie części złożenia, w tym złożenia podrzędne, zostaną otwarte we FreeCAD w celu zrekonstruowania przy użyciu wartości z arkuszy kalkulacyjnych.
Ta funkcja jest przeznaczona do konstruowania w pełni parametrycznego.

**Uwaga:** Ta funkcja jest bardzo eksperymentalna i nie jest zalecana w przypadku ważnych projektów.
Znane problemy:

-   Złożenie może zostać zniszczone z powodu błędnych odniesień do nazw topologicznych w częściach.
-   Główne arkusze kalkulacyjne mogą ulec uszkodzeniu podczas edycji, gdy plik części, do którego następuje odniesienie, jest już zamknięty. Może to spowodować awarię programu FreeCAD.

Włącz rekurencyjną aktualizację importowanych części: Otwiera rekurencyjnie wszystkie zespoły podrzędne w celu ich aktualizacji.

Używanie eksperymentalnego nazewnictwa topologicznego: Podczas importowania części do złożenia algorytm generuje nazwy topologiczne dla każdego elementu podrzędnego importowanego kształtu. Nadawane nazwy topologiczne są zapisywane we własciwości **mux Info**. Kiedy zaimportowana część wymaga aktualizacji, te nazwy topologiczne są używane do aktualizacji elementów podrzędnych wiązań. Dzięki temu zespoły stają się bardziej odporne na zmienne numery elementów podrzędnych FreeCAD.
**Uwaga:** Zwiększa to rozmiary plików i czas obliczeń podczas importowania części. Jeśli ma być używane nazewnictwo topologiczne, należy je aktywować przed utworzeniem złożenia.





Dziedziczenie przezroczystości na powierzchnię z części i podzespołów: Użyj ustawień kolorów i przezroczystości z importowanych części.
**Uwaga:** Ta funkcja jest bardzo eksperymentalna i nie jest zalecana dla ważnych projektów.





Nie importuj niewidocznych kształtów: Spowoduje to ukrycie niewidocznych kształtów odniesienia / konstrukcji. **Uwaga:** Żadne wiązania nie mogą być połączone z kształtami odniesienia / konstrukcji w wyższych lub innych złożeniach podrzędnych. W przeciwnym razie może dojść do uszkodzenia złożenia.





Używaj łączenia brył do importowania części i złożeń: Wszystkie importowane części zostaną bezpośrednio połączone w całość.
Ta funkcja jest przydatna w przypadku [MES](FEM_Workbench/pl.md) lub symulacji [drukowania 3D](Manual:Preparing_models_for_3D_printing/pl.md), jeśli dozwolona jest tylko jedna bryła. Alternatywą jest utworzenie [kształtu całego zespołu](#Kształt_całego_złożenia.md) później.



### Ustawienia interfejsu użytkownika 

Pokaż wiązania na pasku narzędzi: Jeśli ta opcja nie jest używana, przyciski paska narzędzi dla różnych wiązań nie są widoczne, aby zaoszczędzić miejsce na pasku narzędzi. Nowe wiązania można nadal ustawiać za pomocą okna dialogowego **Narzędzia wiązań** *(przycisk paska narzędzi <img alt="" src=images/A2p_DefineConstraints.svg  style="width:24px;">)*. Użyj natywnego menedżera plików systemu operacyjnego: Jeśli ta opcja jest używana, podczas wybierania plików dla złożeń wyświetlane jest okno dialogowe plików systemu operacyjnego.



### Zapisywanie plików 

Użyj ścieżek względnych dla importowanych części : Używa względnych ścieżek do plików części.
Użyj bezwzględnych ścieżek dla importowanych części: Używa bezwzględnych ścieżek do plików części.
Wszystkie pliki znajdują się w tym folderze projektu: Wszystkie pliki projektu umieszczone są w określonym folderze. Nie ma znaczenia, czy znajdują się w podfolderach podrzędnych. Uwaga: Żaden plik nie może być w folderze kilka razy *(np. w różnych podfolderach)*.
Ta opcja jest przydatna do pracy na różnych komputerach, ponieważ wystarczy skopiować folder projektu.



## Rozwiązywanie problemów 

Prędzej czy później pojawi się problem, że środowisko A2plus nie może rozwiązać ustalonych wiązań. Aby temu zaradzić, istnieją różne strategie:



### Korzystanie z narzędzia do wyszukiwania konfliktów 

Jest to najbezpieczniejsza metoda, gdy masz kilka ograniczeń, ponieważ narzędzie to próbuje rozwiązać jedno wiązanie po drugim, dopóki nie znajdzie konfliktowego wiązania. Następnie można przejść do innych strategii, aby rozwiązać zidentyfikowane wiązanie. Narzędzie jest wywoływane za pomocą przycisku na pasku narzędzi <img alt="" src=images/A2p_SearchConstraintConflicts.svg  style="width:24px;">.



### Sprawdzanie kierunku wiązania 

Czasami wiązania wydają się być spójnie zdefiniowane, ale mimo to nie można ich rozwiązać. Przykład: Załóżmy, że masz wiązanie {{Variable|[Równoległe płaszczyzny](#Równoległe_płaszczyzny.md)}} ustawione dla dwóch płaszczyzn. Teraz chcesz ustawić dla tych samych płaszczyzn wiązanie {{Variable|[Płaszczyzna na płaszczyźnie](#Płaszczyzna_na_płaszczyźnie.md)}} i A2plus nie może tego rozwiązać. Wtedy kierunki wiązań {{Variable|Równoległe płaszczyzny}} i {{Variable|Płaszczyzna na płaszczyźnie}} są różne. Użyj tego samego kierunku dla obu wiązań, aby to naprawić.

Środowisko pracy A2plus oferuje automatyczne sprawdzanie właściwego kierunku dla **wszystkich** wiązań złożenia za pomocą przycisku paska narzędzi <img alt="" src=images/A2p_ReAdjustConstraints.svg  style="width:24px;">.



### Usuwanie wiązań 

Większość przypadków nierozwiązywalnych wiązań występuje bezpośrednio podczas dodawania nowego wiązania. Rozwiązaniem jest usunięcie ostatnio dodanego wiązania. A2plus również to zaproponuje.

Czasami strategia usuwania jest jedyną, na przykład podczas edycji części w programie FreeCAD, tak że brakuje ścian lub krawędzi połączonych z wiązaniami. Powinieneś wtedy usunąć jedno wiązanie, które jest połączone ze zmienioną częścią na raz. Użyj przycisku paska narzędzi <img alt="" src=images/A2p_solver.svg  style="width:24px;"> po każdym usunięciu, aby sprawdzić, czy osiągnąłeś stan rozwiązywalny.

Gdy masz złożenie, które można rozwiązać, dodaj krok po kroku potrzebne wiązania.



### Przesuwanie Części 

W niektórych przypadkach solver potrzebuje tylko lepszych wartości początkowych, aby rozwiązać powiązania. Weźmy na przykład przypadek, w którym masz część osi i część koła. Dodajesz wiązanie {{Variable|zbieżność Osi}} i nie otrzymujesz informacji, że solver zawiódł, ale części nie są odpowiednio przesuwane, a w widżecie \"Widok raportu\" FreeCAD widzisz \"*REACHED POS-ACCURACY :0.0*\". Rozwiązaniem jest przesunięcie części bliżej pozycji, którą chcesz uzyskać za pomocą wiązania.

**Uwaga:** Upewnij się, że przynajmniej jedna część wiązania ma właściwość **Pozycja ustalona** ustawioną na {{false/pl}}.



### Ustawienie właściwości Czubka 

Jeśli po zaimportowaniu do złożenia A2plus brakuje niektórych funkcji części, należy sprawdzić właściwość **[Czubek](PartDesign_MoveTip/pl.md)**.

Środowisko pracy A2plus importuje bryły części ze wszystkimi ich cechami aż do cechy Czukek. Jest to rozsądne, ponieważ ustawienie właściwości Czubek na określoną cechę oznacza, że wszystkie cechy za nim nie powinny pojawić się w gotowej części. Jeśli więc przegapisz cechę części w A2plus, otwórz część za pomocą przycisku paska narzędzi <img alt="" src=images/A2p_EditPart.svg  style="width:24px;">, a następnie wybierz bryłę i spójrz na jej właściwość **Czubek**. Jeśli końcówka nie znajduje się w wybranym miejscu, kliknij prawym przyciskiem myszy w miejscu, w którym powinna się znajdować i wybierz **[<img src=images/PartDesign_MoveTip.svg style="width:24px"> Ustaw czubek**. Na koniec zapisz część i przeładuj złożenie za pomocą przycisku na pasku narzędzi <img alt="" src=images/A2p_ImportPart_Update.svg  style="width:24px;">.



### Naprawa drzewa montażu 

Jeśli nie widzisz wyraźnego powodu, dla którego niektóre ograniczenia nie mogą zostać rozwiązane, możesz spróbować użyć przycisku paska narzędzi <img alt="" src=images/A2p_RepairTree.svg  style="width:24px;">. Spowoduje to rozwiązanie wszystkich wiązań i ponowne pogrupowanie ich pod różnymi częściami.



### Migracja starych złożeń A2plus 

Zespoły utworzone za pomocą środowiska A2plus starszego niż marzec 2019 r. nie wyświetlają prawidłowych ikon dla importowanych części i mają przestarzałe właściwości. Złożenia te można zmigrować do A2plus w wersji 0.4.35 i nowszej za pomocą opcji menu **A2plus → Misc → [<img src=images/A2p_Upgrade.svg style="width:24px">. Migruj proxy zaimportowanych części**. Po wykonaniu tej czynności należy zapisać i ponownie otworzyć plik złożenia.



### Unikanie znaków akcentowanych 

**Ta strategia nie jest konieczna dla systemu Windows.**

W niektórych systemach operacyjnych mogą wystąpić problemy, jeśli nazwy plików lub ścieżki plików części lub zespołu zawierają znaki akcentowane. Dlatego należy unikać takich znaków, a także generalnie znaków specjalnych.



### Pozycja ustalająca 

**Ta strategia nie jest już konieczna w przypadku złożeń utworzonych za pomocą A2plus 0.3.11 lub nowszej wersji, ponieważ A2plus wydaje teraz ostrzeżenie o braku ustalonych pozycji**.

Po ustawieniu wiązania między dwiema częściami, gdy żadna część nie ma właściwości **ustalona pozycja** ustawionej na {{true/pl}} lub jest połączona wiązaniem z częścią z **ustalona pozycja** ustawioną na {{true/pl}}, wiązanie nie może zostać rozwiązane. To samo dzieje się, jeśli obie części wiązania mają **fixed Position** ustawione na {{true/pl}}.

Następnie A2plus wyświetla informacje o nieudanym rozwiązaniu, ale czasami widać tylko, że części nie zostały odpowiednio przesunięte, a w widżecie \"Widok raportu\" FreeCAD widać \"*REACHED POS-ACCURACY :0.0*\". Oznacza to, że solver zakończył pracę bez błędów, ale w rzeczywistości nie mógł rozwiązać wiązań.

Dlatego sprawdź, czy przynajmniej jedna z części w złożeniu ma właściwość **ustalona pozycja** ustawioną na \"true\". Następnie upewnij się, że ustawiłeś ograniczenia tylko dla części, która jest w jakiś sposób połączona z częścią stałą. Aby zwizualizować te zależności, zobacz sekcję [Struktura złożenia](#Assembly_Structure/pl.md).



### Obracanie części 

**Ta strategia nie jest już konieczna w przypadku złożeń utworzonych za pomocą środowiska pracy A2plus 0.4.0 lub nowszego, ponieważ A2plus automatycznie obraca części w tle, aby uzyskać wystarczający kąt początkowy dla solwera**.

Solver często kończy się niepowodzeniem dla wiązania {{Variable|kątowePłaszczyzny}}, jeśli dwie wybrane płaszczyzny mają obecnie kąt 0° lub 180°. *(Części nie są odpowiednio przesuwane, a w widżecie \"Widok raportu\" programu FreeCAD wyświetlany jest komunikat \"REACHED POS-ACCURACY :0.0\")*. Rozwiązaniem tego problemu jest obrócenie jednej części o kilka stopni za pomocą funkcji transformacji FreeCAD *(kliknij prawym przyciskiem myszy część w drzewie modelu i wybierz z menu kontekstowego **Przemieszczenie**)*.

**Uwaga:** Upewnij się, że przynajmniej jedna część wiązania ma właściwość **Pozycja ustalona** ustawioną na {{false/pl}}.



## Animacja

A2plus oferuje animacje za pomocą przeciągania oraz skryptów Pythona.



### Przeciąganie

Animacje przeciągania są interaktywne, ponieważ uruchamia się je poprzez przeciągnięcie części złożenia. Aby uzyskać tego rodzaju animacje:

1.  W pełni zwiąż część, której ruch lub obrót ma być animowany
2.  Kliknij przycisk na pasku narzędzi <img alt="" src=images/A2p_MovePartUnderConstraints.svg  style="width:24px;">. Spowoduje to włączenie trybu przeciągania.
3.  Kliknij wybraną część w zespole.
4.  Teraz możesz poruszać myszą, a część będzie podążać za ruchem myszy w ramach zdefiniowanych ograniczeń.
5.  Aby zakończyć tryb przeciągania, kliknij lewym przyciskiem myszy w złożeniu lub naciśnij ESC.

Oto przykładowy zestaw do wypróbowania animacji przeciągania: [A2p_example-for-dragging-animation.FCStd](https://forum.freecadweb.org/download/file.php?id=99204).

![](images/A2p_dragging-animation-result.gif )



*Powyżej: Animacja przeciągania przy użyciu przykładowego złożenia.*



### Tworzenie skryptów 

Pomimo tego, że tryb przeciągania oferuje ładne interaktywne animacje, czasami nie są one wystarczająco precyzyjne dla screencastów lub filmów. Animacje skryptowe mają tę zaletę, że animują ruchy i obroty w określony sposób. Można na przykład obrócić część o dokładnie 10° w przód i w tył. Poniższe przykłady wykorzystują złożenie, w którym część powinna zostać obrócona. Jeśli spróbujesz animować to za pomocą trybu przeciągania, zobaczysz, jak trudno jest uzyskać obrót w przód iw tył, który można np. pokazać szefowi w prezentacji. Dzięki interaktywnemu skryptowi przykładowemu jest to jednak łatwe zadanie.

Animacja skryptowa działa zazwyczaj w ten sposób:

1.  Zespół jest w pełni ograniczony
2.  Skrypt zmienia parametr, na przykład pozycję lub kąt obrotu części.
3.  Po zmianie parametru wiązania zespołu są rozwiązywane.
4.  Kroki 2. i 3. są powtarzane w celu uzyskania animacji.

Zamiast parametru rozmieszczenia można również zmienić ograniczenie, na przykład odległość między 2 płaszczyznami.



#### Przykład prostego skryptu 

Najprostszym sposobem tworzenia skryptów animacji jest animacja nieinteraktywna, która podąża za zdefiniowanym ruchem. Oto przykład: Najpierw pobierz ten plik złożenia: [A2p_animated-example.FCStd](https://forum.freecadweb.org/download/file.php?id=97554), a także ten skrypt Python: [A2p_animation-example-script.py](https://forum.freecadweb.org/download/file.php?id=97981).


<div class="mw-collapsible mw-collapsed toccolours">

Jest to zawartość skryptu, a linie zaczynające się od \"#\" opisują, co robią poszczególne linie skryptu:


<div class="mw-collapsible-content">


```python
# import bibliotek
import time, math, PySide
import A2plus.a2p_solversystem as a2p_solver

# używamy kroków co 1 stopień
step = 1
# odczekaj 1 ms między każdym krokiem
timeout = 0.001
# początkowy kąt wynosi 0 stopni
angle = 0
# bierzemy aktualnie otwarty dokument
document = FreeCAD.activeDocument()
# chcemy później zmienić kąt obrotu części "star_wheel_001"
starWheel = document.getObject("star_wheel_001")
# zdefiniuj okno dialogowe postępu działające od 0 do 360
progressDialog = PySide.QtGui.QProgressDialog(u " Animation progress", u " Stop", 0, 360)

# blok while jest główną pętlą zmieniającą kąt i rozwiązującą
# ograniczenia montażowe następnie
while angle < 360: # wykonuj tę pętlę, aż uzyskamy jeden pełny obrót (360 stopni)
    # zwiększyć kąt obrotu
    angle += step
    # ustaw nowy kąt w oknie dialogowym postępu
    progressDialog.setValue(angle)
    # zmień kąt obrotu części "star_wheel_001"
    starWheel.Placement.Rotation.Angle = math.radians(angle)
    # rozwiąż ograniczenia 
    a2p_solver.solveConstraints(document, useTransaction=True)
    # zaktualizuj widok po rozwiązaniu ("Gui" oznacza "graficzny interfejs użytkownika")
    FreeCADGui.updateGui()
    # przenieś okno dialogowe postępu na przód
    PySide.QtGui.QWidget.raise_(progressDialog)
    # jeśli w oknie dialogowym naciśnięto "Stop", wyjdź z pętli
    if progressDialog.wasCanceled():
        angle = 360
    # odczekaj jakiś czas przed wykonaniem następnego kroku
    time.sleep(timeout)
```


</div>


</div>

Aby użyć skryptu do wykonania animacji, musimy

1.  Otworzyć plik złożenia w programie FreeCAD.
2.  Otworzyć plik skryptu w programie FreeCAD.
3.  Kliknąć przycisk paska narzędzi <img alt="" src=images/Menu_Std_DlgMacroExecute_fr_02.png  style="width:24px;">, aby wykonać skrypt *(zwany również makrem)*.
4.  Przejdź do zakładki zespołu, aby zobaczyć obrót.

Aby poćwiczyć, po prostu zmień coś w skrypcie i wykonaj go później. Na przykład zwiększyć \"krok\" do \"5\".

Oto wynik przykładowej animacji:

![](images/A2p_animated-example-result.gif )



#### Przykład interaktywnego skryptu 

Pierwszy przykład skryptu pokazał, jak utworzyć animację bez żadnej informacji zwrotnej od użytkownika. W przypadku większości aplikacji konieczna jest interakcja z animacją. Na przykład interesującą kwestią w tym przykładzie jest zobaczenie, jak szpilki napędowe przecinają środkowy rowek koła. Aby przyjrzeć się temu bliżej, można zaprezentować ten szczegół współpracownikom lub szefowi. Dlatego potrzebne jest interaktywne rozwiązanie.

Można to zrobić za pomocą niestandardowego okna dialogowego animacji z suwakiem. Przesuwając suwak można ustawić kąt obrotu, a tym samym obracać się tam i z powrotem w interesującej pozycji.

Używamy tego samego pliku asemblera: [A2p_animated-example.FCStd](https://forum.freecadweb.org/download/file.php?id=97554) i tego skryptu Pythona: [A2p_animation-example-script.py](https://forum.freecadweb.org/download/file.php?id=97982).


<div class="mw-collapsible mw-collapsed toccolours">

Jest to treść skryptu, który wyświetla interaktywne okno dialogowe animacji:


<div class="mw-collapsible-content">


```python
# import bibliotek
import time, math, PySide, sys
import FreeCAD.A2plus.a2p_solversystem as a2p_solver
from FreeCAD import Units
from PySide import QtCore, QtGui

# odczekać 1 ms po każdym obliczeniu
timeout = 0.001
# pobieramy aktualnie otwarty dokument
document = FreeCAD.activeDocument()
# chcemy później zmienić kąt obrotu części "star_wheel_001"
starWheel = document.getObject("star_wheel_001")

class AnimationDlg(QtGui.QWidget): # okno dialogowe animacji

    def __init__(self): # to initialize the dialog
        super(AnimationDlg, self).__init__()
        self.initUI()

    def initUI(self): # definicja komponentów okna dialogowego
        self.setMinimumSize(self.minimumSizeHint()) # set the minimal dialog size to minimum
        self.setWindowTitle('Animation Dialog')
        # używać układu siatki dla całego formularza
        self.mainLayout = QtGui.QGridLayout()
        self.lineNo = 0 # first dialog grid line
        # Dodaj etykietę opisu
        DescriptionLabel = QtGui.QLabel(self)
        DescriptionLabel.setText("Change slider to change rotation angle")
        self.mainLayout.addWidget(DescriptionLabel,self.lineNo,0,1,4)
         # następny wiersz okna dialogowego
        self.lineNo += 1
        # dodaje etykietę; nie ma potrzeby stosowania przedrostka "self.", ponieważ nie chcemy później zmieniać etykiety.
        LabelMin = QtGui.QLabel(self)
        LabelMin.setText("Min")
        LabelMin.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMin,self.lineNo,0)
        # dodać edycję obrotową, aby zdefiniować minimum suwaka
        self.MinEdit = QtGui.QSpinBox(self)
        # pobiera jednostkę kąta jako ciąg znaków
        self.MinEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2:])
        self.MinEdit.setMaximum(999)
        self.MinEdit.setMinimum(0)
        self.MinEdit.setSingleStep(10)
        self.MinEdit.setValue(0)
        self.MinEdit.setFixedHeight(32)
        self.MinEdit.setToolTip("Minimal angle for the slider")
        QtCore.QObject.connect(self.MinEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMinEdit)
        self.mainLayout.addWidget(self.MinEdit,self.lineNo,1)
        # dodaj suwak
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setRange(0, 360)
        self.slider.setValue(0)
        self.slider.setFixedHeight(32)
        self.slider.setToolTip("Move the slider to change the rotation angle")
        QtCore.QObject.connect(self.slider, QtCore.SIGNAL("sliderMoved(int)"), self.handleSliderValue)
        self.mainLayout.addWidget(self.slider,self.lineNo,2)
        # dodaj etykietę
        LabelMax = QtGui.QLabel(self)
        LabelMax.setText("Max")
        LabelMax.setFixedHeight(32)
        self.mainLayout.addWidget(LabelMax,self.lineNo,3)
        # dodaje edycję obrotową, aby zdefiniować maksimum suwaka
        self.MaxEdit = QtGui.QSpinBox(self)
        # pobiera jednostkę kąta jako ciąg znaków
        self.MaxEdit.setSuffix(" " + str(FreeCAD.Units.Quantity(1, FreeCAD.Units.Angle))[2:])
        self.MaxEdit.setMaximum(999)
        self.MaxEdit.setMinimum(1)
        self.MaxEdit.setSingleStep(10)
        self.MaxEdit.setValue(360)
        self.MaxEdit.setFixedHeight(32)
        self.MaxEdit.setToolTip("Maximal angle for the slider")
        QtCore.QObject.connect(self.MaxEdit, QtCore.SIGNAL("valueChanged(int)"), self.setMaxEdit)
        self.mainLayout.addWidget(self.MaxEdit,self.lineNo,4)
         # następny wiersz okna dialogowego
        self.lineNo += 1
        # dodaje element dystansowy
        self.mainLayout.addItem(QtGui.QSpacerItem(10,10), 0, 0)
        # dodaje etykietę
        LabelCurrent = QtGui.QLabel(self)
        LabelCurrent.setText("Current angle:")
        LabelCurrent.setFixedHeight(32)
        self.mainLayout.addWidget(LabelCurrent,self.lineNo,1)
        # wyświetla bieżący kąt
        self.CurrentAngle = QtGui.QLineEdit(self)
        self.CurrentAngle.setText(str(0))
        self.CurrentAngle.setFixedHeight(32)
        self.CurrentAngle.setToolTip("Current rotation angle")
        self.CurrentAngle.isReadOnly()
        self.mainLayout.addWidget(self.CurrentAngle,self.lineNo,2)
        # dodaje etykietę dla urządzenia
        LabelUnit = QtGui.QLabel(self)
        LabelUnit.setText("deg")
        LabelUnit.setFixedHeight(32)
        self.mainLayout.addWidget(LabelUnit,self.lineNo,3)
        # aby zamknąć okno dialogowe
        self.Close = QtGui.QPushButton(self)
        self.Close.setText("Close")
        self.Close.setFixedHeight(32)
        self.Close.setToolTip("Closes the dialog")
        QtCore.QObject.connect(self.Close, QtCore.SIGNAL("clicked()"), self.CloseClicked)
        self.mainLayout.addWidget(self.Close,self.lineNo,4)
        # place the defined grid layout to the dialog
        self.setLayout(self.mainLayout)
        self.update()

    def handleSliderValue(self):
        # ustawia wartość suwaka jako kąt
        starWheel.Placement.Rotation.Angle = math.radians(self.slider.value())
        # kąt prądu wyjściowego
        self.CurrentAngle.setText(str(self.slider.value()))
        # rozwiązywanie wiązań
        a2p_solver.solveConstraints(document)
        # aktualizacja widoku po rozwiązaniu ''("Gui" oznacza "graficzny interfejs użytkownika")''
        FreeCADGui.updateGui()
        # odczekaj trochę czasu, ważne jest, aby dać czas na wykonanie obliczeń.
        time.sleep(timeout)

    def setMinEdit(self):
        # upewnij się, że minimum jest mniejsze niż maksimum
        if self.MinEdit.value() >=  self.MaxEdit.value():
            self.MaxEdit.setValue(self.MinEdit.value() + 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def setMaxEdit(self):
        # upewnić się, że minimum jest mniejsze niż maksimum
        if self.MinEdit.value() >=  self.MaxEdit.value():
            self.MinEdit.setValue(self.MaxEdit.value() - 1)
        self.slider.setRange(self.MinEdit.value(), self.MaxEdit.value())

    def CloseClicked(self):
        AnimationDialog.close()

# utwórz i wyświetl zdefiniowane okno dialogowe
AnimationDialog = AnimationDlg()
AnimationDialog.show()

# uruchom tę pętlę, gdy okno dialogowe jest widoczne
while AnimationDialog.isVisible():
    # aktualizacja widoku; ważne, aby system operacyjny otrzymał informację zwrotną, że okno dialogowe jest aktywne
    FreeCADGui.updateGui()
    # przeniesienie okna dialogowego na przód, tak aby było ono zawsze widoczne
    QtGui.QWidget.raise_(AnimationDialog)
    # wartość wyjściowa suwaka również tutaj, ponieważ podczas obliczeń suwak mógł zostać przesunięty
    AnimationDialog.CurrentAngle.setText(str(AnimationDialog.slider.value()))
```


</div>


</div>

Okno dialogowe zdefiniowane w skrypcie wygląda następująco:

![](images/A2p_AnimationDialog.png )



### Polecenia skryptu 

Aby lepiej zrozumieć składnię skryptu, oto kilka informacji o poleceniach: 
```python starWheel.Placement.Rotation.Angle = math.radians(angle)```

Tutaj zmieniamy właściwość umieszczania `Rotation.Angle` części otrzymanej wcześniej jako `starWheel`. Ta właściwość pobiera kąt jako [radian](https://en.wikipedia.org/wiki/Radian). Funkcja `radians()` z biblioteki `math` konwertuje kąt ze stopni na radiany.

Właściwość `Rotation.Angle` wykorzystuje bieżącą oś umieszczenia części *(w naszym przykładzie oś X)*. Aby obrócić część np. wokół osi Z, można ustawić oś obrotu *(przed wywołaniem polecenia obrotu)* za pomocą polecenia: 
```python starWheel.Placement.Rotation.Axis = FreeCAD.Vector(0,0,1)``` Zamiast obracać, części można również przesuwać. Aby zmienić na przykład położenie koła w kierunku Y, polecenie brzmiałoby: 
```python starWheel.Placement.Base.y = PositionShift``` W tym przypadku nie definiowalibyśmy zmiennej `angle`, ale `PositionShift`, którą zmieniamy przy każdym przebiegu pętli.

Istnieją różne sposoby ustawiania położenia części. Niektóre z nich są udokumentowane na stronie [Umiejscowienie](Placement/pl.md). Niestety nie ma *(jeszcze)* listy wszystkich możliwych poleceń umiejscowienia. 
```pythona2p_solver.solveConstraints(document, useTransaction=False/True)```

Jest to polecenie specyficzne dla środowiska pracy A2plus. Rozwiązuje ono wiązania złożenia, które wcześniej otrzymaliśmy jako `document`. Opcja `useTransaction` określa, czy FreeCAD powinien przechowywać każdą zmianę w stosie cofania / ponawiania. W przypadku dużych animacji można więc ustawić ją na `False`.



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > A2plus Workbench/pl
