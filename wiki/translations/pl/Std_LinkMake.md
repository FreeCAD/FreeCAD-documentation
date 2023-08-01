---
- GuiCommand:
   Name:Std LinkMake
   Name/pl:Std: Utwórz łącze
   MenuLocation:brak
   Workbenches:wszystkie
   Version:0.19
   SeeAlso:[Część](Std_Part/pl.md), [Grupa](Std_Group/pl.md), [Zawartość](PartDesign_Body/pl.md)
---

# Std LinkMake/pl



## Opis

Narzędzie **[<img src=images/Std_LinkMake.svg style="width:16px"> '''Utwórz łącze'''** tworzy obiekt [App: Łącze](App_Link/pl.md) *(klasa `App::Link`)*, typ obiektu, który odwołuje się lub łączy z innym obiektem, w tym samym dokumencie lub w innym dokumencie. Jest specjalnie zaprojektowany do wydajnego wielokrotnego powielania pojedynczego obiektu, co pomaga w tworzeniu skomplikowanych [złożeń](Assembly/pl.md) z mniejszych złożeń podrzędnych i wielu komponentów wielokrotnego użytku, takich jak śruby, nakrętki i podobne elementy złączne.

Obiekt [App: Łącze](App_Link/pl.md) został nowo wprowadzony w wersji 0.19. W przeszłości proste duplikowanie obiektów można było osiągnąć za pomocą **[<img src=images/Draft_Clone.svg style="width:16px"> [Klonu](Draft_Clone/pl.md)**, ale jest to mniej wydajne rozwiązanie ze względu na jego implementację, która zasadniczo tworzy kopię wewnętrznego [kształtu](Part_TopoShape/pl.md) obiektu źródłowego. Z drugiej strony, obiekt Łącze odwołuje się bezpośrednio do oryginalnego Kształtu, więc jest bardziej wydajny pamięciowo.

Sam obiekt [Łącze](App_Link/pl.md) może zachowywać się jak szyk, powielając swój obiekt bazowy wiele razy. Można to zrobić, ustawiając jego właściwość **Ilość elementów** na wartość {{Value|1}} lub większą. Ten obiekt \"[Szyk łączy](#Link_Array/pl.md)\" może być również tworzony za pomocą różnych narzędzi do tworzenia szyków w środowisku pracy <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md), na przykład **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Szyk ortogonalny](Draft_OrthoArray/pl.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Szyk biegunowy](Draft_PolarArray/pl.md)**, oraz **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Szyk kołowy](Draft_CircularArray/pl.md)**.

W przypadku korzystania ze środowiska <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), Łącza są przeznaczone do użycia z obiektem **[<img src=images/PartDesign_Body.svg style="width:16px"> [Zawartości](PartDesign_Body/pl.md)**, więc zaleca się ustawienie **Tryb wyświetlania Zawartości** na wrtość {{Value|Czubek}} w celu wybrania cech całej Zawartości, a nie indywidualnych cech. Aby utworzyć szyk wewnętrznych [cech](PartDesign_Feature/pl.md), użyj narzędzi **[<img src=images/PartDesign_LinearPattern.svg style="width:16px">. [Szyk liniowy](PartDesign_LinearPattern/pl.md)**, **[<img src=images/PartDesign_PolarPattern.svg style="width:16px"> [Szyk kołowy](PartDesign_PolarPattern/pl.md)**, oraz **[<img src=images/PartDesign_MultiTransform.svg style="width:16px"> [Transformacja wielokrotna](PartDesign_MultiTransform/pl.md)**.

Narzędzie **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz łącze](Std_LinkMake/pl.md)** nie jest definiowane przez konkretne środowisko pracy, ale przez system bazowy, dlatego znajduje się na pasku narzędzi **Konstrukcja**, który jest dostępny we wszystkich [środowiskach pracy](Workbenches/pl.md). Obiekt Łącze, używany w połączeniu z **[<img src=images/Std_Part.svg style="width:16px"> [Częścią](Std_Part/pl.md)** do grupowania różnych obiektów, stanowi podstawę środowiska pracy <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Złożenie 3](Assembly3_Workbench/pl.md) i <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Złożenie 4](Assembly4_Workbench/pl.md).



## Użycie

Przy użyciu zaznaczenia:

1.  Wybierz obiekt w oknie [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md), dla którego chcesz utworzyć Łącze.
2.  Naciśnij przycisk **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz Łącze](Std_LinkMake/pl.md)**. Utworzony obiekt ma taką samą ikonę jak oryginalny obiekt, ale posiada strzałkę wskazującą, że jest to Łącze.

Bez użycia zaznaczenia:

1.  Jeśli żaden obiekt nie jest zaznaczony, naciśnij przycisk **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz łącze](Std_LinkMake/pl.md)**, aby utworzyć puste <img alt="" src=images/Link.svg  style="width:24px;"> Łącze.
2.  Przejdź do [edytora właściwości](Property_editor/pl.md), następnie kliknij na właściwość **Powiązane obiekty**, aby otworzyć okienko dialogowe [Wybór obiektu](Selection_methods/pl.md) i wybrać obiekt, a następnie naciśnij **OK**.
3.  Zamiast wybierać cały obiekt w oknie [Widoku drzewa](Tree_view/pl.md), można również wybrać elementy podrzędne *(wierzchołki, krawędzie lub ściany)* pojedynczego obiektu w oknie [widoku 3D](3D_view/pl.md). W takim przypadku Łącze powieli tylko te elementy podrzędne, a ikonka strzałki będzie inna. Można to również zrobić za pomocą narzędzia **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Utwórz łącze względne](Std_LinkMakeRelative/pl.md)**.

![](images/Std_Link_tree_example.png ) ![](images/Std_Link_example.png )



*''(1)'' obiekt, ''(2)'' puste łącze, ''(3)'' pełne łącze do pierwszego obiektu ''(z nadrzędnym materiałem)'' i ''(4)'' łącze tylko do niektórych elementów podrzędnych obiektu. Puste łącze nie jest powiązane z rzeczywistym obiektem, więc nie jest wyświetlane w oknie [widoku 3D](3D_view/pl.md).*



## Użycie: dokumenty zewnętrzne 

1.  Zacznij od dokumentu, który ma co najmniej jeden obiekt, który będzie źródłem łącza.
2.  Otwórz nowy lub istniejący dokument. Dla łatwiejszej obsługi, użyj opcji **[<img src=images/Std_TreeMultiDocument.svg style="width:16px"> [Wiele dokumentów](Std_TreeMultiDocument/pl.md)**, aby wyświetlić oba dokumenty w oknie [Widoku drzewa](tree_view/pl.md). Zanim przejdziesz dalej, [zapisz](Std_Save/pl.md) oba dokumenty. Łącze nie będzie w stanie znaleźć swojego źródła i celu, jeśli oba dokumenty nie zostaną zapisane na dysku.
3.  W pierwszym dokumencie wybierz obiekt, który chcesz powiązać. Następnie przełącz zakładki w [głównego obszaru widoku](Main_view_area/pl.md), aby przejść do drugiego dokumentu.
4.  Naciśnij przycisk **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz link](Std_LinkMake/pl.md)**. Utworzony obiekt ma taką samą ikonę jak oryginalny obiekt, ale ma dodatkową nakładkę ze strzałką wskazującą, że jest to łącze pochodzące z zewnętrznego dokumentu.


**Uwaga:**

-   Podczas zapisywania dokumentu z łączem, program poprosi również o [zapisanie](Std_Save/pl.md) dokumentu źródłowego zawierającego oryginalny obiekt.
-   Aby dołączyć oryginalny obiekt do dokumentu z łączem, należy użyć przycisku **[<img src=images/Std_LinkImport.svg style="width:16px"> [Importuj łącza](Std_LinkImport/pl.md)** lub **[<img src=images/Std_LinkImportAll.svg style="width:16px"> [Importuj wszystkie łącza](Std_LinkImportAll/pl.md)**.
-   Narzędzie **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz łącze](Std_LinkMake/pl.md)** może być użyte na istniejącym obiekcie łącza, w celu utworzenia łącza do łącza, które ostatecznie prowadzi do oryginalnego obiektu w dokumencie źródłowym. Można tego użyć z **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> [Utwórz łącze względne](Std_LinkMakeRelative/pl.md)**, aby wybrać tylko określone elementy podrzędne.

![](images/Std_Link_tree_documents_example.png ) ![](images/Std_Link_documents_example.png )



*''(1, 2)'' dwa obiekty z dokumentu źródłowego połączone z dokumentem docelowym, ''(3)'' łącze do drugiego łącza ''(z nadrzędnym materiałem)'' oraz ''(4)'' łącze do elementów podrzędnych drugiego łącza.*



## Przeciąganie i upuszczanie 

Zamiast przełączać zakładki dokumentów, można tworzyć Łącza wykonując operację przeciągnij i upuść w oknie [Widoku drzewa](Tree_view/pl.md): wybierz obiekt źródłowy z pierwszego dokumentu, przeciągnij go, a następnie upuść na nazwę drugiego dokumentu przytrzymując klawisz **Alt** na klawiaturze.

Przeciąganie i upuszczanie powoduje różne działania w zależności od trzymanego klawisza modyfikatora.

-   Bez klawisza modyfikatora po prostu przenosi obiekt z jednego dokumentu do drugiego. Na kursorze wyświetlana jest pochylona strzałka.
-   Przytrzymanie klawisza **Ctrl** kopiuje obiekt. Na kursorze wyświetlany jest znak plus.
-   Przytrzymanie klawisza **Alt** tworzy łącze. Na kursorze wyświetlana jest para ogniw łańcucha.

W przypadku modyfikatorów **Ctrl** i **Alt**, przeciąganie i upuszczanie może być również wykonywane w pojedynczym dokumencie. Oznacza to, że przeciągnięcie obiektu i upuszczenie go na nazwę tego samego dokumentu może być użyte do utworzenia wielu kopii lub wielu linków do niego.



## Grupy


**[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz łącze](Std_LinkMake/pl.md)**

można użyć na obiekcie **[<img src=images/Std_Part.svg style="width:16px"> [Część](Std_Part/pl.md)** w celu szybkiego duplikowania grup obiektów umieszczonych w przestrzeni, czyli [złożeniach](Assembly/pl.md).

![](images/Std_Link_tree_Std_Part_example.png )



*Łącze utworzone z obiektu [Część](Std_Part.md). Obiekty nie są duplikowane, ale są przedstawione pod oryginalną zawartością i pod zawartością Łącze.*

Zwykła **[<img src=images/Std_Group.svg style="width:16px"> [Grupa](Std_Group/pl.md)** nie posiada właściwości **Umiejscowienie**, więc nie może kontrolować pozycji obiektów wewnątrz niego. Jednakże, gdy narzędzie **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz link](Std_LinkMake/pl.md)** zostanie użyte z **[<img src=images/Std_Group.svg style="width:16px"> [Grupą](Std_Group/pl.md)**, wynikowe łącze zachowuje się zasadniczo jak obiekt **[<img src=images/Std_Part.svg style="width:16px"> [Część](Std_Part/pl.md)**, a także może być przemieszczane w przestrzeni.

![](images/Std_Link_tree_Std_Group_example.png ) ![](images/Std_Link_Std_Group_example.png )



*Łącze utworzone z [Grupy](Std_Group/pl.md). Obiekty nie są duplikowane, ale są wymienione pod oryginalną zawartością i pod zawartością Łącza. Łącze ''(z nadrzędnym materiałem)'' może być przesuwane w przestrzeni, tak jak obiekt [Część](Std_Part/pl.md).*

Łącze do **[<img src=images/Std_Part.svg style="width:16px"> [Części](Std_Part/pl.md)** utrzyma widoczność obiektów zsynchronizowaną z oryginalnym obiektem Część, więc jeśli ukryjesz jeden obiekt w Łączu, będzie on ukryty we wszystkich Łączach i w oryginalnym obiekcie. Z drugiej strony, łącze do **[<img src=images/Std_Group.svg style="width:16px"> [Grupy](Std_Group/pl.md)** pozwoli na niezależną kontrolę widoczności.

![](images/Std_Link_tree_Std_Part_visibility.png ) ![](images/Std_Link_tree_Std_Group_visibility.png )



*Po lewej: [Część](Std_Part/pl.md) z dwoma obiektami i dwoma linkami do Części, gdzie widoczność obiektów jest zsynchronizowana. Po prawej: [Grupa](Std_Group/pl.md) z dwoma obiektami i dwoma linkami do Grupy, gdzie widoczność obiektów jest kontrolowana niezależnie w każdej grupie.*



## Kontrola wyglądu 

Gdy tworzone jest łącze, domyślnie właściwość **Zastępuj materiał** ma wartość {{FALSE/pl}}, więc obiekt łącza będzie miał taki sam wygląd jak oryginalny **Połączony obiekt**.

Gdy właściwość **Zastępuj materiał** jest ustawione na {{TRUE/pl}}, właściwość **Materiał kształtu** będzie teraz kontrolować wygląd obiektu Łącza.

Niezależnie od stanu właściwości **Zastępuj materiał**, możliwe jest indywidualne ustawienie wyglądu elementów podrzędnych (wierzchołków, krawędzi, ścian) dla obiektu Łącza.

1.  Wybierz obiekt Łącza w oknie [Widoku drzewa](Tree_view/pl.md). Otwórz menu kontekstowe *(kliknij prawym przyciskiem myszy)* i wybierz **Zastąp kolory ...**.
2.  Teraz wybierz w oknie [widoku 3D](3D_view/pl.md) poszczególne elementy podrzędne, których chcesz użyć, naciśnij **Edycja** i zmień właściwości, w tym przezroczystość.
3.  Aby usunąć niestandardowe atrybuty, zaznacz elementy na liście i naciśnij **Usuń**.
4.  Gdy wynik będzie zadowalający, naciśnij **OK**, aby zamknąć okno dialogowe.


**Uwaga:**

od wersji 0.19 kolorowanie elementów podrzędnych podlega regułom [problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md), więc powinno być wykonywane jako ostatni krok modelowania, gdy model nie podlega już zmianom.

<img alt="" src=images/Std_Link_override_color_example.png  style="width:500px;">



*(1) Oryginalny obiekt, (2) obiekt Łącza z nadrzędnym materiałem i (3) drugi obiekt Łącza ze zmodyfikowanymi poszczególnymi elementami podrzędnymi.*



## Szyk łączy 


**Zobacz również:**

[Szyk ortogonalny](Draft_OrthoArray/pl.md).

Gdy tworzone jest Łącze, domyślnie jego **Liczba elementów** wynosi {{Value|0}}, więc tylko pojedynczy obiekt Łącze będzie widoczny w [Widoku drzewa](Tree_view/pl.md).

Biorąc pod uwagę, że wartość **Wyświetl element** jest domyślnie ustawiona na `True`, gdy **Liczba elementów** jest ustawiona na {{Value|1}} lub więcej, automatycznie więcej obiektów Łącze zostanie utworzonych poniżej pierwszego. Każdy nowy obiekt Łącze może zostać umieszczony w żądanej pozycji poprzez zmianę jego własnej właściwości **Umiejscowienie**.

W podobny sposób każdy element szyku może mieć zmieniony wygląd, albo przez właściwości **Zastępuj materiał** i **Materiał kształtu**, albo przez użycie menu **Zastąp kolory ...** na całym szyku, a następnie wybranie poszczególnych ścian. Zostało to opisane w akapicie [Kontrola wyglądu](#Kontrola_wyglądu.md).

<img alt="" src=images/Std_Link_tree_array_example.png ) ![](images/Std_Link_array_example.png  style="width:500px;">



*(1) Oryginalny obiekt i (2, 3, 4) szyk Łączy z trzema elementami, każdy w innej pozycji. Pierwszy obiekt Łącza ma nadpisany materiał i przezroczyste ściany, a dwa pozostałe mają niestandardowe kolory ścian.*

Gdy jesteś zadowolony z rozmieszczenia i właściwości elementów Łącza w szyku, możesz zmienić wartość właściwości **Wyświetl element** na {{FALSE/pl}}, aby ukryć poszczególne Łącza w oknie [Widoku drzewa](Tree_view/pl.md). Ma to tę zaletę, że system jest bardziej dynamiczny, zwłaszcza jeśli w dokumencie znajduje się wiele obiektów.

Tworząc tego typu szyk Łączy, musisz umieścić każdy z elementów samodzielnie. Jeśli jednak chcesz użyć określonych wzorców do umieszczenia kopii, możesz użyć narzędzi szyku w środowisku pracy <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md), takich jak **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Szyk ortogonalny](Draft_OrthoArray/pl.md)**, **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Szyk biegunowy](Draft_PolarArray/pl.md)**, oraz **[<img src=images/Draft_CircularArray.svg style="width:16px"> [Szyk kołowy](Draft_CircularArray/pl.md)**. Polecenia te mogą tworzyć normalne kopie lub kopie Łącz w zależności od opcji w czasie tworzenia.



## Widoczność

Gdy właściwość **Wyświetl element** ma wartość `True`, a poszczególne elementy są wyświetlane w [Widoku drzewa](Tree_view/pl.md) w [szyku łączy](#Szyk_łączy.md), każde Łącze można wyświetlić lub ukryć, naciskając klawisz **Spacja** na klawiaturze.

Innym sposobem na ukrycie poszczególnych elementów jest użycie menu **Zastąp kolory ...**.

1.  Wybierz szyk, otwórz z menu podręcznego **Zastąp kolory ...** *(kliknij prawym przyciskiem myszy)*.
2.  W oknie [widoku 3D](3D_view/pl.md) wybierz dowolny element podrzędny z dowolnego Łącza w szyku.
3.  Naciśnij **Ukryj**. Powinna pojawić się ikona oka <img alt="" src=images/Invisible.svg  style="width:24px;"> wskazująca, że ten element został ukryty w [widoku 3D](3D_view/pl.md). Obiekt tymczasowo pokaże się, gdy kursor najedzie na ikonę <img alt="" src=images/Invisible.svg  style="width:24px;">.
4.  Możesz kliknąć **OK**, aby potwierdzić operację i zamknąć okno dialogowe. Łącze pozostanie ukryte, nawet jeśli jest wyświetlane jako widoczne w [widoku drzewa](Tree_view/pl.md).

![](images/Std_Link_array_visibility_example.png )



*Okno dialogowe koloru elementu dostępne po otwarciu menu kontekstowego obiektu Łącze w Widoku drzewa.*

Jeśli chcesz przywrócić widoczność tego elementu szyku, wejdź ponownie do okna dialogowego, wybierz ikonę oka, a następnie kliknij **Usuń**, aby usunąć status ukrycia, i kliknij **OK**, aby potwierdzić i zamknąć okno dialogowe. Element będzie ponownie widoczny w oknie [widoku 3D](3D_view/pl.md).

Gdy Łącze odnosi się do obiektu **[<img src=images/Std_Part.svg style="width:16px"> [Część](Std_Part/pl.md)** lub **[<img src=images/Std_Group.svg style="width:16px"> [Grupa](Std_Part/pl.md)**, narzędzie z menu **Zastąp kolory ...** działa podobnie jak w przypadku szyków. Pozwala kontrolować kolor ściany, kolor całego obiektu i widoczność obiektów w grupie.

![](images/Std_Link_Std_Part_visibility_example.png ) ![](images/Std_Link_Std_Part_visibility_example_3D.png )



*Obiekt [Część](Std_Part.md) zawierający trzy obiekty i Łącze do tej części. W Łączu (1) pierwszy obiekt jest niewidoczny, (2) drugi obiekt ma kilka elementów podrzędnych o różnych kolorach, (3) cały trzeci obiekt ma inny kolor i poziom przezroczystości.*



## Właściwości

Obiekt [App: Łącze](App_Link/pl.md) *(klasa `App::Link`)* wywodzi się z podstawowej klasy [App: DocumentObject](App_DocumentObject/pl.md) *(`App::DocumentObject`)*, dlatego posiada podstawowe właściwości tej ostatniej, takie jak **Etykieta** i **Etykieta2**.

Są to właściwości dostępne w [edytorze właściwości](Property_editor/pl.md). Ukryte właściwości można wyświetlić za pomocą polecenia **Wyświetl wszystko** w menu podręcznym [edytora właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty| Link}}

-    **Powiązane Obiekty|XLink**: wskazuje obiekt źródłowy [App: Łącze](App_Link/pl.md). Może to być cały obiekt lub jego element *(wierzchołek, krawędź lub ściana)*.

-    **Przekształcanie łączy|Bool**: domyślnie ustawiona na wartość {{FALSE/pl}}, w którym to przypadku Łącze zastąpi własne położenie **Powiązaniem Obiektu**. Jeśli właściwość jest ustawiona na {{TRUE/pl}}, Łącze zostanie umieszczone w tej samej pozycji co **Powiązane Obiekty**, a jego położenie będzie względne w stosunku do położenia **Powiązanych Obiektów**. Można to również osiągnąć za pomocą narzędzia **[<img src=images/Std_LinkMakeRelative.svg style="width:16px">. [Utwórz łącze względne](Std_LinkMakeRelative/pl.md)**.

-    **Umiejscowienie|Placement**: umiejscowienie odnośnika we współrzędnych bezwzględnych.

-    **Umiejscowienie łącza|Placement|Ukryte**: jest to przesunięcie nałożone na **Umiejscowienie** **Powiązanego obiektu**. Ta właściwość jest normalnie ukryta, ale pojawia się, jeśli właściwość **Przekształcanie łączy** jest ustawiona na wartość {{TRUE/pl}}. W tym przypadku właściwość **Umiejscowienie** staje się teraz ukryta.

-    **Wyświetl element|Bool**: właściwość domyślnie ustawiona na wartość {{TRUE/pl}}, w którym to przypadku [widok drzewa](Tree_view/pl.md) pokaże poszczególne kopie Łącza, tak długo jak właściwość **Liczba elementów** jest równa {{Value|1}} lub większa.

-    **Liczba elementów|IntegerConstraint**: domyślnie {{Value|0}}. Jeśli wartość wynosi {{Value|1}} lub jest większa, obiekt [App: Łącze](App_Link.md) będzie zachowywać się jak szyk i powieli ten sam **Powiązany obiekt** wiele razy. Jeśli właściwość**Wyświetl element** ma wartość {{TRUE/pl}}, każdy element w tablicy będzie wyświetlany w [Widoku drzewa](Tree_view/pl.md), a każdy z nich może mieć zmodyfikowane własne **Umiejscowienie**. Każda kopia Łącza będzie miała nazwę opartą na właściwości [Nazwa](Object_name.md) Łącza, powiększoną o `_iN`, gdzie `N` jest liczbą zaczynającą się od `0`. Na przykład, z pojedynczym obiektem `Łącze`, kopie będą miały nazwy `Link_i0`, `Link_i1`, `Link_i2` itd.

-    **Link Execute|String**: nazwa funkcji execute, która zostanie uruchomiona dla tego konkretnego obiektu Łącza. Domyślnie jest to {{Value|'appLinkExecute'}}. Ustaw ją na {{Value|'None'}}, aby ją wyłączyć.

-    **Colored Elements|LinkSubHidden|Ukryte**: lista elementów Łącza, których kolor został nadpisany.

-    **Skala|Float**: domyślnie przyjmuje wartość {{Value|1.0}}. Jest to współczynnik równomiernego skalowania w każdym kierunku `X`, `Y` i `Z`. Na przykład, sześcian o wymiarach {{Value|2 mm}} x {{Value|2 mm}} x {{Value|2 mm}}, który jest skalowany przez {{Value|2.0}}, da w wyniku kształt o wymiarach {{Value|4 mm}} x {{Value|4 mm}} x {{Value|4 mm}}.

-    **Wektor skali|Vector|Ukryte**: współczynnik skali dla każdego elementu `(X, Y, Z)` dla wszystkich elementów Łącza, gdy właściwość **Liczba elementów** ma wartość {{Value|1}} lub większą. Jeśli **Skala** ma wartość inną niż {{Value|1.0}}, ta sama wartość zostanie użyta w trzech komponentach.

-    **Lista skali|VectorList**: współczynnik skali dla każdego elementu Łącza.

-    **Lista wyświetlania|BoolList|Ukryte**: {{emphasis|(tylko do odczytu)}} stan widoczności każdego elementu Łącza, każdy element przyjmuje wartości albo {{TRUE/pl}} albo {{FALSE/pl}}.

-    **Lista umiejscowienia|PlacementList|Ukryte**: {{emphasis|(tylko do odczytu)}} the placement for each Link element.

-    **Lista elementów|LinkList|Ukryte**: lista elementów Łącza.

-    **_LinkTouched|Bool|Ukryte**:

-    **_ChildCache|LinkList|Ukryte**:


{{TitleProperty|Podstawa}}

-    **Proxy|PythonObject|Ukryte**: klasa własna związana z tym obiektem. Istnieje wyłącznie dla wersji środowiska [Python](Python/pl.md). Zobacz sekcję [tworzenie skryptów](#Tworzenie_skrypt.C3.B3w.md).

Obiekt [App: Łącze](App_Link/pl.md) będzie dodatkowo pokazywał właściwości oryginalnego **Powiązanego obiektu**, więc [edytor właściwości](Property_editor/pl.md) może mieć grupy właściwości takie jak {{TitleProperty|Dołączenie}}, {{TitleProperty|Sześcian}}, {{TitleProperty|Draft}}, itd.



### Widok


{{TitleProperty| Link}}

-    **Styl kreślenia|Enumeration**: domyślnie {{Value|Brak}}. Może przyjąć wartości {{value|Pełna}}, {{value|Kreskowana}}, {{value|Kropkowana}}, {{value|Kreska Kropka}}. Definiuje styl krawędzi w oknie [widoku 3D](3D_view/pl.md).

-    **Szerokość linii|FloatConstraint**: wartość zmiennoprzecinkowa określająca szerokość w pikselach krawędzi w oknie [widoku 3D](3D_view/pl.md). Domyślnie {{value|2.0}}.

-    **Zastępuj materiał|Bool**: wartość domyślna to {{FALSE/pl}}. Jeśli zostanie ustawiona na {{TRUE/pl}}, zastąpi materiał **Połączonego Obiektu** i wyświetli kolory zdefiniowane w właściwości **Materiał kształtu**.

-    **Rozmiar punktu|FloatConstraint**: podobnie jak **Szerokość linii**, definiuje rozmiar wierzchołków.

-    **Wybieralność|Bool**: jeśli przyjmie wartość {{TRUE/pl}}, obiekt może zostać wybrany w oknie [widoku 3D](3D_view/pl.md) za pomocą kursora. W przeciwnym razie obiekt nie może zostać wybrany, dopóki wartość tej opcji nie zostanie ustawiona na {{TRUE/pl}}.

-    **Materiał kształtu|Material**: Ta właściwość zawiera właściwości podrzędne, które opisują wygląd obiektu.

    -   
        **Barwa rozproszenia**
        
        , domyślnie  light blue .

    -   
        **Barwa otoczenia**
        
        , wartość domyślna to  dark gray .

    -   
        **Barwa odbicia**
        
        , wartość domyślna to  black .

    -   
        **Kolor emisji**
        
        , wartość domyślna to  black .

    -   
        **Stopień połysku**
        
        , wartość domyślna to {{Value|0.2}}

    -   
        **Przezroczystość**
        
        , wartość domyślna to {{Value|0.0}}.


{{TitleProperty|Podstawa}}

-    **Child View Provider|PersistentObject|Ukryte**:

-    **Material List|MaterialList|Ukryte**: **(tylko do odczytu)** jeśli poszczególne materiały zostały dodane, będą one wymienione tutaj.

-    **Override Color List|ColorList|Ukryte**: **(tylko do odczytu)** jeśli poszczególne ściany lub krawędzie łącza zostały nadpisane, zostaną one wymienione tutaj.

-    **Override Material List|BoolList|Ukryte**: **(tylko do odczytu)** jeśli poszczególne materiały Łącza zostały nadpisane, zostaną one wymienione tutaj.


{{TitleProperty|Opcje wyświetlania}}

-    **Tryb wyświetlania|Enumeration**: przyjmuję wartości {{Value|'Link'}} lub {{Value|'ChildView'}}.

-    **Wyświetl w Drzewie|Bool**: zobacz informacje na stronie [Właściwości Python](App_FeaturePython/pl.md).

-    **Widoczność|Bool**: zobacz informacje na stronie [Właściwości Python](App_FeaturePython/pl.md).


{{TitleProperty|Wybieranie}}

-    **Na wierzchu po zaznaczeniu|Enumeration**: zobacz informacje na stronie [Właściwości Python](App_FeaturePython/pl.md).

-    **Styl zaznaczenia|Enumeration**: zobacz informacje na stronie [Właściwości Python](App_FeaturePython/pl.md).

Dodatkowo wyświetli właściwości widoku oryginalnego **Powiązanego obiektu**.



## Dziedziczenie

Obiekt [App: Łącze](App_Link/pl.md) jest formalnie instancją klasy `App::Link`, której rodzicem jest podstawowy [App: DocumentObject](App_DocumentObject/pl.md) *(klasa `App::DocumentObject`)*. Jest to obiekt bardzo niskiego poziomu, który może być używany z większością innych obiektów dokumentów.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony schemat zależności pomiędzy głównymi obiektami w programie. Obiekt `App::Link* jest głównym składnikiem systemu, nie zależy on od żadnego środowiska pracy, a może być użyty z większością obiektów stworzonych we wszystkich środowiskach pracy.`



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Zapoznaj się z artykułem [Część: Cecha](Part_Feature/pl.md), aby uzyskać ogólne informacje.

Obiekt App Łącze jest tworzony za pomocą metody `addObject()` dokumentu. Może on zdefiniować swój **Połączony obiekt** poprzez nadpisanie atrybutu `LinkedObject` lub poprzez użycie metody `setLink`. 
```python
import FreeCAD as App

doc = App.newDocument()
bod1 = App.ActiveDocument.addObject("Part::Box", "Box")
bod2 = App.ActiveDocument.addObject("Part::Cylinder", "Cylinder")
bod1.Placement.Base = App.Vector(10, 0, 0)
bod2.Placement.Base = App.Vector(0, 10, 0)

obj1 = App.ActiveDocument.addObject("App::Link", "Link")
obj2 = App.ActiveDocument.addObject("App::Link", "Link")

obj1.LinkedObject = bod1
obj2.setLink(bod2)
obj1.Placement.Base = App.Vector(-10, -10, 0)
obj2.Placement.Base = App.Vector(10, -10, 0)
obj1.ViewObject.OverrideMaterial = True
App.ActiveDocument.recompute()
```

Podstawowy `App::Link` nie ma obiektu Proxy, więc nie może być w pełni wykorzystany do tworzenia klas podrzędnych.

Dlatego też, dla klasy podrzędnej [Python](Python/pl.md), powinieneś stworzyć obiekt `App::LinkPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::LinkPython", "Link")
obj.Label = "Custom label"
```



## Dodatkowe informacje 

Obiekt [App Łącze](App_Link/pl.md) został wprowadzony po 2 latach rozwoju i prototypowania. Komponent ten został wymyślony i opracowany niemal samodzielnie przez użytkownika **realthunder**. Motywacje i implementacje stojące za tym projektem zostały opisane na jego stronie GitHub, [Link](https://github.com/realthunder/FreeCAD_assembly3/wiki/Link). Aby wdrożyć tę funkcję, wprowadzono kilka podstawowych zmian w programie FreeCAD. Zostały one również obszernie udokumentowane w artykule [Core-Changes](https://github.com/realthunder/FreeCAD_assembly3/wiki/Core-Changes).

Projekt związany z App Łącze rozpoczął się po tym, jak przeprojektowanie środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md) zostało ukończone w wersji 0.17. Historię App Łącze można prześledzić w kilku istotnych wątkach na forum:

-   [Dlaczego obiekt może znajdować się tylko w jednym App::Part?](https://forum.freecadweb.org/viewtopic.php?f=19&t=21505) *(marzec 2017)*
-   [Wprowadzenie App::Link/XLink](https://forum.freecadweb.org/viewtopic.php?f=10&t=21586) *(marzec 2017)*
-   [Linki](https://forum.freecadweb.org/viewtopic.php?f=20&t=22216) *(maj 2017)*
-   [Implementacja Realthunder Link: Dyskusja o architekturze](https://forum.freecadweb.org/viewtopic.php?f=20&t=23015) *(czerwiec 2017)*
-   [PR #876: Link, etap pierwszy, wybór świadomy kontekstu](https://forum.freecadweb.org/viewtopic.php?f=17&t=23419) *(lipiec 2017)*
-   [Preview: Link, etap drugi, podstawy API](https://forum.freecadweb.org/viewtopic.php?f=17&t=23626) *(lipiec 2017)*
-   [Podgląd Assembly3](https://forum.freecadweb.org/viewtopic.php?f=20&t=25712) *(grudzień 2017)*
-   [Scalanie mojej gałęzi Link](https://forum.freecadweb.org/viewtopic.php?f=10&t=29542) *(czerwiec 2018)*

W końcu nastąpiło zgłoszenie pull request i scalenie:

-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=27&t=38621), stary wątek (lipiec 2019), [pull request #2350](https://github.com/FreeCAD/FreeCAD/pull/2350) (the BIG merge), [LinkMerge branch](https://github.com/realthunder/FreeCAD/tree/LinkMerge).
-   [App::Link: the big merge](https://forum.freecadweb.org/viewtopic.php?f=8&t=37757), główny wątek (lipiec 2019)
-   [Prosty opis ścieżki Link, 019, Link stage, Asm3, merge?](https://forum.freecadweb.org/viewtopic.php?p=329054#p329054) (sierpień 2019)
-   [PR#2559: ujawnienie linków i akcji nawigacyjnych](https://forum.freecadweb.org/viewtopic.php?f=17&t=39672), wprowadzenie do funkcji Link w wersji 0.19 (wrzesień 2019).

Inne różne \"odnośniki internetowe\" dotyczące Łącza obejmują:

-   [Obiekty łączone dynamicznie](Dynamic_linked_object.md) - Wzorzec z Łączem i złożeniami, który ma na celu zmniejszenie duplikacji logiki związanej ze złożeniem, takiej jak orientacja, pozycjonowanie lub liczba instancji.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std LinkMake/pl
