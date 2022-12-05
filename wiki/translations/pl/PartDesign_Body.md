---
- GuiCommand:/pl
   Name:PartDesign Body
   Name/pl:Projekt części: Zawartość
   MenuLocation:Projekt części → Stwórz zawartość
   Workbenches:[Projekt części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Std: Część](Std_Part/pl.md), [edycja funkcji](Feature_editing/pl.md)
---

# PartDesign Body/pl

## Opis

Obiekt [zawartość](PartDesign_Body/pl.md) jest podstawowym elementem do tworzenia brył w środowisku [Projekt części](PartDesign_Workbench/pl.md). Może on zawierać [szkice](Sketch/pl.md), [obiekty odniesienia](Datum/pl.md) i [cechy](PartDesign_Feature/pl.md), które pomagają w tworzeniu [pojedynczej, ciągłej bryły](PartDesign_Body/pl#Pojedyncza_ci.C4.85g.C5.82a_bry.C5.82a.md).

Element Zawartość dostarcza obiekt **odniesienia położenia**, który zawiera zarówno lokalne osie X, Y i Z, jak i płaszczyzny standardowe. Te elementy mogą być użyte jako referencje do dołączenia [szkiców](Sketch/pl.md) i [brył pierwotnych](PartDesign_CompPrimitiveAdditive/pl.md).

Nie pomyl obiektu <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [zawartość](PartDesign_Body/pl.md) środowiska pracy Projekt części z obiektem <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std: Część](Std_Part.md). Pierwszy z nich jest specyficznym obiektem używanym w środowisku <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt części](PartDesign_Workbench/pl.md), przeznaczonym do modelowania [pojedynczej ciągłej bryły](PartDesign_Body/pl#Pojedyncza_ci.C4.85g.C5.82a_bry.C5.82a.md) za pomocą [cech](PartDesign_Feature/pl.md) środowiska Projekt części. [Std: Część](Std_Part/pl.md) jest obiektem grupującym przeznaczonym do tworzenia [złożeń](Assembly/pl.md), nie jest on używany do modelowania, tylko do rozmieszczania różnych obiektów w przestrzeni. Wiele ciał i innych [Std: Części](Std_Part/pl.md), może być umieszczonych wewnątrz pojedynczej [Std: Części](Std_Part.md), aby stworzyć złożony zespół.

![](images/PartDesign_Body_tree.png ) ![](images/PartDesign_Body_example.png ) 
*Po lewej: widok drzewa przedstawiający cechy, które kolejno tworzą ostateczny kształt obiektu. </br>Po prawej: zakończony obiekt prezentowany w oknie [widoku 3D](3D_view/pl.md).*

## Użycie

Jeśli nie jest wybrana żadna istniejąca bryła:

1.  Naciśnij przycisk **<img src="images/PartDesign_Body.svg" width=16px> [Body](PartDesign_Body.md)**. Zostanie utworzona pusta zawartość, która automatycznie stanie się **[ aktywna ](PartDesign_Body/pl#Aktywny_status.md)**.
2.  Teraz możesz nacisnąć **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Nowy szkic](PartDesign_NewSketch/pl.md)**, aby utworzyć [szkic](Sketch/pl.md) w zawartości, który może być użyty z **[<img src=images/PartDesign_Pad.svg style="width:16px"> [wyciągnięciem](PartDesign_Pad/pl.md)**.
3.  Alternatywnie, dodaj prymitywną [własciwość](PartDesign_Feature.md), na przykład, **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [addtywny sześcian](PartDesign_AdditiveBox/pl.md)**.

Jeśli wybrano obiekt bryły:

1.  Naciśnij przycisk **<img src="images/PartDesign_Body.svg" width=16px> [zawartość](PartDesign_Body/pl.md)**. Tworzone jest nowa zawartość z pojedynczym elementem **właściwości podstawowej**. Ten element Właściwości podstawowej jest prostym odwołaniem do innego obiektu utworzonego wcześniej lub zaimportowanego do dokumentu. Zobacz akapit [właściwość podstawowa](PartDesign_Body/pl#W.C5.82a.C5.9Bciwo.C5.9B.C4.87_podstawowa.md), aby uzyskać więcej informacji. Istniejąca bryła lub [właściwość](PartDesign_Feature/pl.md) nie może być wybrana po naciśnięciu przycisku **<img src="images/PartDesign_Body.svg" width=16px> [zawartość](PartDesign_Body/pl.md)**.

### Uwagi

-   Jeśli nie ma obecnie żadnej zawartości, gdy przycisk **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Nowy szkic](PartDesign_NewSketch/pl.md)** zostanie wciśnięty, automatycznie zostanie utworzona nowa zawartość. Jeśli zawartość już istnieje, musi zostać uaktywniona przed użyciem funkcji **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Nowy szkic](PartDesign_NewSketch/pl.md)**.
-   Kliknij dwukrotnie zawartość w widoku [widoku drzewa](Tree_view/pl.md) lub otwórz menu kontekstowe *(kliknij prawym przyciskiem myszy)* i wybierz **Przełącz aktywną zawartość**, aby aktywować lub dezaktywować zawartość. Jeśli inna zawartość jest aktywna, zostanie ona wyłączona. Zobacz [stan aktywny](PartDesign_Body/pl#Aktywny_status.md), aby uzyskać więcej informacji.

## Właściwości

[Projekt części: zawartość](PartDesign_Body/pl.md) *(klasa `PartDesign::Body`)* wywodzi się z [Część: Cecha](Part_Feature/pl.md) *(klasy `Part::Feature`)*, dlatego posiada wszystkie właściwości tej ostatniej.

Oprócz właściwości opisanych na stronie [Cecha części](Part_Feature/pl.md), bryła pochodząca ze środowiska Projekt części posiada następujące właściwości w [edytorze właściwości](Property_editor/pl.md).

### Dane


{{TitleProperty|Podstawowe}}

-    **Czubek|Link**: [Cecha](PartDesign_Feature.md) zdefiniowana jako \"Końcówka\", która jest zazwyczaj ostatnią cechą utworzoną w bryle. Końcówka wskazuje ostateczny kształt bryły, który jest wyświetlany w oknie [widoku 3D](3D_view.md), gdy **Tryb wyświetlania zawartości** jest ustawiony na `Czubek`. Zobacz stronę [czubek](PartDesign_Body/pl#Czubek.md), aby uzyskać więcej informacji.

-    **Cecha Podstawa|Link**: zewnętrzny kształt używany jako pierwsza [właściwość](PartDesign_Feature/pl.md) w bryle. Zazwyczaj ustawia się go podczas przeciągania obiektu bryłowego do pustej bryły. Jeśli żadna bryła nie zostanie zaimportowana w ten sposób, ta właściwość będzie pusta. Zobacz stronę [Cecha Podstawa](PartDesign_Feature/pl.md), aby uzyskać więcej informacji.

-    **Umiejscowienie|Placement**: pozycja obiektu w oknie [3D view](3D_view/pl.md). Położenie jest określone przez punkt `Bazowy` *(wektor)* i punkt `Obrotu` *(oś i kąt)*. Zobacz stronę [Umiejscowienie](Placement/pl.md)

-    **Grupa|LinkList**: lista [Cech projektu części](PartDesign_Feature/pl.md) w treści.

#### Ukryte Dane właściwości 

-    **Odniesienie położenia|Link**: obiekt [odniesienia położenia](App_OriginGroupExtension/pl.md), który jest pozycyjnym odniesieniem dla wszystkich elementów wymienionych w **Grupie**.

-    **_ Grupa Dotknięta|Bool**: czy grupa jest wzruszona czy nie.

Również ukryte właściwości opisane na stronie [Cecha części](Part_Feature/pl.md).

### Widok


{{TitleProperty|Podstawowe}}

-    **Tryb wyświetlania zawartości|Enumeration**: ustawia tryb wyświetlania specyficzny dla zawartości za pomocą jednego z dwóch typów.

    -   
        `Na wskroś`
        
        *(domyślnie)* wyświetla wszystkie obiekty wewnątrz bryły, czyli [szkice](Sketch/pl.md), [cechy](PartDesign_Feature/pl.md), obiekty punktów odniesienia itp. Tryb ten pozwala na wizualizację częściowych operacji wykonywanych wewnątrz Bryły, dlatego jest zalecanym trybem podczas dodawania i edycji cech. Wybierz konkretny element, a następnie ustaw **Widoczność** na `True` lub wciśnij klawisz **Spacja** na klawiaturze.

    -   
        `Czubek`
        
        ujawnia tylko ostateczny kształt bryły, który jest zdefiniowany przez właściwość **Czubek**. Cała reszta, w tym [szkice](Sketch/pl.md), [częściowe cechy](PartDesign_Feature/pl.md), punkty odniesienia itp. nie są wyświetlane, nawet jeśli są widoczne w [widoku drzewa](Tree_view/pl.md). Ten tryb jest zalecany, gdy bryła nie musi być dalej modyfikowana, więc wyświetlany jest ustalony kształt. Ten tryb jest również zalecany, gdy chcemy wybrać podelementy *(wierzchołki, krawędzie i ściany)* ostatecznego kształtu, aby użyć ich do pracy z w innymi narzędziami.

## Koncepcja zawartości 

### Pojedyncza ciągła bryła 

Zawartość Projektu części jest przeznaczona do modelowania pojedynczej, ciągłej bryły. Znaczenie słowa \"ciągła\" to element wykonany w jednym kawałku, bez części ruchomych lub brył rozłącznych. Przykłady brył ciągłych to takie, które są wytwarzane z jednego kawałka surowca w procesie odlewania, cięcia lub frezowania. Na przykład nakrętka, podkładka i śruba składają się z pojedynczego stałego kawałka stali bez ruchomych części, więc każda z nich może być modelowana przez Zawartość Projektu części. Obiekty, które są tworzone przez spawanie dwóch elementów, mogą być również modelowane przez pojedynczą Zawartość, o ile spoina nie jest przeznaczona do rozerwania.

Gdy te sąsiadujące bryły są umieszczone razem w jakimś układzie, wtedy stają się \"złożeniem\". W złożeniu, obiekty nie są połączone razem, ale są po prostu \"ułożone w stos\" lub umieszczone obok siebie, i pozostają indywidualnymi częściami.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*Po lewej: trzy pojedyncze, przylegające do siebie bryły, z których każda jest modelowana przez zawartość Projektu części. </br> Po prawej: poszczególne Zawartości połączone w złożenie.*

### Edycja cech 

Zawartość Projektu części jest przeznaczona do pracy poprzez tworzenie początkowej bryły, albo ze [szkicami](Sketch/pl.md), lub z [bryłami pierwotnymi](PartDesign_CompPrimitiveAdditive.md), a następnie modyfikowanie jej poprzez [\"cechy\"](PartDesign_Feature/pl.md) aby dodać lub usunąć materiał z poprzedniego kształtu. Pełne wyjaśnienie znajdziesz na stronie [Edycja cech](Feature_editing/pl.md).

Zawartość Projektu części wykona automatyczne funkcją [suma](Part_Fuse/pl.md) *(zjednoczenie)* elementów bryłowych wewnątrz niej. Oznacza to, że *(1)* częściowe bryły powinny się stykać podczas tworzenia i *(2)* rozłączone bryły nie są dozwolone.

<img alt="" src=images/PartDesign_Body_two_intersection.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_two_fusion.png  style="width:" height="200px;"> 
*Po lewej: dwie pojedyncze bryły, które przecinają się wzajemnie. </br>Po prawej: pojedyncze złożenie projektu części z dwoma [cechami dodatkowymi](PartDesign_Feature/pl.md). Są one automatycznie łączone razem, więc zamiast przecinać się, tworzą jedną ciągłą bryłę.*

![](images/PartDesign_Body_non-contiguous.png ) 
*Po lewej: dwie nieciągłe bryły. to nie jest prawidłowa zawartość Projektu części. </br> Po prawej: dwie przylegające do siebie bryły, co skutkuje poprawną bryłą Projektu części. Nowsza [cecha](PartDesign_Feature/pl.md) powinna zawsze stykać się lub przecinać poprzednią, tak, że jest z nią zespolona i staje się jedną ciągłą bryłą.*


**Uwaga:**

Inne programy CAD, takie jak Catia pozwalają na tworzenie nieciągłych brył w tej samej \"zawartości\". Od wersji v0.19, FreeCAD nie pozwala na to. Na forum [FreeCAD](https://forum.freecadweb.org/index.php) toczyły się dyskusje na temat zniesienia tego ograniczenia, ale nie podjęto jeszcze żadnej konkretnej decyzji. Jeśli chciałbyś dowiedzieć się więcej lub przedstawić różne punkty widzenia, proszę dyskutuj na [forum](https://forum.freecadweb.org/index.php).

## Szczegółowe objaśnienie właściwości 

### Aktywny status 

Otwarty dokument może zawierać wiele Zawartości. Aby dodać nową cechę do określonej zawartości, należy nadać jej status **aktywna**. Aktywna zawartość będzie wyświetlana w [widoku drzewa](Tree_view/pl.md) kolorem tła określonym przez wartość **Aktywna zawartość** w [Edytor ustawień](Preferences_Editor/pl#Kolory.md) *(domyślnie jasnoniebieski)*. Aktywna bryła będzie również wyświetlana w postaci pogrubionego tekstu.

Aby uaktywnić lub dezaktywować Zawartość:

-   Kliknij dwukrotnie na jej pozycję w [widoku drzewa](Tree_view/pl.md), lub
-   Otwórz menu kontekstowe *(klikając prawym przyciskiem myszki)* i wybierz **Przełącz aktywną zawartość**.

Aktywowanie Zawartości powoduje automatyczne przełączenie do środowiska [Projekt części](PartDesign_Workbench/pl.md). W tym samym czasie może być aktywna tylko jedna Zawartość.

![](images/PartDesign_Body_active.png )



*Dokument z dwiema Zawartościami Projektu części, wśród których aktywna jest druga.*

### Odniesienie położenia 

Odniesienie położenia obejmuje trzy standardowe osie *(X, Y, Z)* i trzy standardowe płaszczyzny *(XY, XZ i YZ)*. [Szkice](Sketch/pl.md) i inne obiekty mogą być dołączane do tych elementów podczas ich tworzenia.

1.  Tworzenie bryły.
2.  Jeśli zawartość jest wybrana w [widoku drzewa](Tree_view/pl.md), naciśnij przycisk **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Utwórz nowy szkic](PartDesign_NewSketch/pl.md)**, otworzy się [panel zadań](Task_panel/pl.md) umożliwiający wybranie jednej z płaszczyzn.
3.  Jeśli zawartość nie jest wybrana, wybierz Odniesienie położenia i uczyń go widocznym w oknie widoku [widoku 3D](3D_view.md) naciskając klawisz **Spacja** na klawiaturze. Rozwiń także obiekt Odniesienie położenia, aby zobaczyć osie i płaszczyzny.
4.  Wybierz jedną z płaszczyzn, albo w [widoku drzewa](Tree_view/pl.md) albo w oknie [widok 3D](3D_view/pl.md), a następnie naciśnij **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Utwórz nowy szkic](PartDesign_NewSketch/pl.md)**. Szkic zostanie utworzony na wybranej płaszczyźnie.

Ten sam proces może być zastosowany przy tworzeniu pomocniczej geometrii układu odniesienia jak [Linia](PartDesign_Line/pl.md), [Płaszczyzna](PartDesign_Plane/pl.md) i [Układ współrzędnych](PartDesign_CoordinateSystem/pl.md).


**Uwaga:**

Początek układu współrzędnych jest obiektem [App: Odniesienie położenia](App_OriginGroupExtension.md) *(klasa `App::Origin`)*, podczas gdy osie i płaszczyzny są obiektami odpowiednio typu `App::Line` oraz `App::Plane`. Każdy z tych elementów może być ukryty i nieujawniany indywidualnie przy użyciu klawisza **spacja**. Jest to przydatne przy tworzeniu innych obiektów, aby wybrać właściwe odniesienie.


**Uwaga 2:**

Wszystkie elementy składowe Zawartości są powiązane z jej odniesieniem położenia, co oznacza, że Zawartość może być przesuwana i obracana w odniesieniu do globalnego układu współrzędnych, bez wpływu na rozmieszczenie jej elementów składowych.

<img alt="" src=images/PartDesign_Body_Origin_tree.png ) ![](images/PartDesign_Body_Origin_view.png  style="width:" height="400px;">



*Z lewej: Odniesienie położenia Projekt części w [widoku drzewa](Tree_view/pl.md). <br>Z prawej: reprezentacja Odniesienia położenia w oknie [widoku 3D](3D_view/pl.md).*

### Właściwość podstawowa 

Element cechy bazowej jest pierwszym elementem [cecha projektu części](PartDesign_Feature/pl.md) w Zawartości, gdy Zawartość jest oparta na innym kształcie bryły. Bryła ta może być utworzona przez dowolne środowisko pracy lub zaimportowana z pliku zewnętrznego, na przykład z pliku STEP.

![](images/PartDesign_Body_BaseFeature_tree.png ) 
*Zawartość Projekt części, każda z nich z jedną cechą bazową, która jest pobierana z wcześniej utworzonych brył.*

Aby utworzyć Cechę Bazową:

1.  wybierz kształt bryły zewnętrzny w stosunku do dowolnej bryły, i
2.  naciśnij **[<img src=images/PartDesign_Body.svg style="width:16px"> [Zawartość](PartDesign_Body/pl.md)**, spowoduje to utworzenie nowej bryły z pojedynczą cechą bazową.


**Uwaga:**

nie możesz wybrać istniejącej zawartości ani żadnej z jej [cechy](PartDesign_Feature/pl.md), po naciśnięciu przycisku **[<img src=images/PartDesign_Body.svg style="width:16px"> [Zawartość](PartDesign_Body/pl.md)**.

Jeśli masz już zawartość, możesz utworzyć cechę bazową w ten sposób:

-   w [widoku drzewa](Tree_view/pl.md) wybierz obiekt, przeciągnij go i upuść wewnątrz zawartości, lub
-   w [edytorze właściwości](Property_editor/pl.md), edytuj wartość {{PropertyData/pl|cecha bazowa}} naciskając ikonkę wielokropka **...** i wybierając obiekt z listy. W tym przypadku możesz wybrać istniejącą zawartość jako cechę bazową.


**Uwaga:**

Przeciąganie i upuszczanie działa tylko dla zawartości, które nie mają jeszcze cechy bazowej.


**Uwaga 2:**

jeśli zawartość posiada już kilka cech, to po przeciągnięciu i upuszczeniu bryły zewnętrznej, Cecha bazowa zostanie utworzona na początku listy cech, czyli zostanie dodana na początku właściwości **Grupy**.

Cecha Podstawa jest całkowicie opcjonalna; jest ona obecna tylko wtedy, gdy dołączamy obiekt spoza zawartości. Jeśli żadna zewnętrzna bryła nie jest dołączona, możesz nadal budować swój kształt używając [szkiców](Sketch/pl.md), [wyciągnięć](PartDesign_Pad/pl.md), [brył pierwotnych](PartDesign_CompPrimitiveAdditive/pl.md) i innych [Cech Projektu części](PartDesign_Feature/pl.md). W tym przypadku właściwość **cechy podstawowej** pozostaje pusta.

![](images/PartDesign_Body_BaseFeature_Tip.svg )



*Po lewej: Zawartość Projektu części z cechą bazową, która jest pobierana z zewnętrznego obiektu bryły, i wiele kolejnych [Cechy Projektu części](PartDesign_Feature/pl.md) na wierzchu.. </br> Po prawej: Zawartość, która nie posiada określonej cechy bazowej.*


**Note:**

Jeżeli inna bryła środowiska Projekt Części jest wybrana jako Cecha bazowa, musi zawierać kształt. Jeśli jest pusta *(brak elementów, brak Cechy bazowej, \...)*, spowoduje to błąd.

### Czubek

Czubek jest [cechą Projektu części](PartDesign_Feature/pl.md), który jest wystawiony poza Zawartość. To znaczy, jeśli inne narzędzie z dowolnego środowiska pracy *(na przykład **[<img src=images/Part_SimpleCopy.svg style="width:16px"> [Część: Szybka kopia](Part_SimpleCopy/pl.md)** lub **[<img src=images/Part_Cut.svg style="width:16px"> [Część: Wytnij](Part_Cut/pl.md)**)* musi używać kształtu zawartości, użyje kształtu Czubka. Mówiąc inaczej, Czubek jest ostateczną reprezentacją bryły, tak jakby historia parametryczna nie istniała.

![](images/PartDesign_Body_Tip_final.svg )



*Po lewej: Zawartość Projektu części z pełną historią parametryczną włącznie z cechami pośrednimi. </br>Po prawej: Czubek jest ostatecznym kształtem, który może być wyeksportowany z Zawartości, z pominięciem historii modelu.*

Czubek jest automatycznie ustawiany na ostatnią cechę utworzoną w zawartości. Niemniej jednak, może być również ustawiony na dowolną cechę pośrednią poprzez otwarcie menu kontekstowego w [widoku drzewa](Tree_view/pl.md) *(prawy przycisk myszy)* i wybranie opcji **[<img src=images/PartDesign_MoveTip.svg style="width:16px"> [Ustaw czubek](PartDesign_MoveTip.md)**, lub zmieniając wartość zawartości **Czubka** w [Edytorze właściwości](Property_editor/pl.md).

Zmiana czubka w efekcie cofa jego historię, umożliwiając dodanie cech, które powinny być dodane wcześniej. Pozwala także na udostępnienie innego kształtu narzędziom zewnętrznym.

W [widoku drzewa](tree_view.md), Czubek Zawartości jest rozpoznawany przez [cechę Projektu części](PartDesign_Feature/pl.md), który ma ikonę składającą się z białej strzałki wewnątrz zielonego koła.

![](images/PartDesign_Body_Tip_tree.png ) 
*Dwie zawartości Projektu części, każda z nich posiada [Cechy Projektu części](PartDesign_Feature/pl.md). Czubek jest ostatnią cechą w nich, i jest oznaczony symbolem nakładki.*

### Współpraca z innymi środowiskami pracy 

Domyślnie, [cechy Projektu Części](PartDesign_Feature/pl.md) wewnątrz bryły są zaznaczone, ponieważ jest to wymagane do edycji i dodawania kolejnych cech za pomocą narzędzi środowiska [Projekt części](PartDesign_Workbench/pl.md). Nie zaleca się jednak wybierania poszczególnych cech, aby używać ich z narzędziami z innych środowisk, takich jak [Część](Part_Workbench/pl.md) i [Rysunek Roboczy](Draft_Workbench/pl.md), ponieważ wyniki mogą być nieoczekiwane. Jeśli to zrobimy, w widoku [raportu](Report_view/pl.md) może pojawić się komunikat o błędzie, **Powiązania wykraczają poza dozwolony zakres**.

Dlatego też na potrzeby pracy z innymi środowiskami, w [widoku drzewa](Tree_view/pl.md) należy wybrać tylko samą Zawartość. W przypadkach, gdy konieczne jest wybranie konkretnych elementów podrzędnych zawartości *(wierzchołków, krawędzi i powierzchni)*, właściwość **Tryb wyświetlania zawartości** bryły powinna być przełączona na `Czubek`. Gdy ten tryb jest włączony, dostęp do obiektów pod zawartością *([cechy](PartDesign_Feature/pl.md), punkty bazowe, [szkice](Sketch/pl.md))* jest wyłączony, a wszystko poza [Czubkiem](PartDesign_Body#Tip.md) w oknie [widoku 3D](3D_view/pl.md) będzie ukryte .

Po zastosowaniu elementów podrzędnych w innych środowiskach pracy, **Tryb wyświetlania zawartości** może być ustawiony z powrotem na wartość `Na wskroś`.

![](images/PartDesign_Body_Tip_Display_mode.svg )



*Po lewej: gdy "Tryb wyświetlania zawartości" jest ustawiony na wartość `Na wskroś* możliwe jest wybranie i wykonanie operacji z poszczególnymi [cechami Projektu części](PartDesign_Feature/pl.md); generalnie nie jest to zalecane. </br> Po prawej: gdy "Tryb wyświetlania zawartości" jest ustawiony na {{incode|Czubek`, wszystkie zaznaczenia i operacje wykonywane na zawartości będą wykonywane w odniesieniu do Czubka, dzięki czemu widoczny będzie tylko ostateczny kształt bryły.}}

### Zarządzanie wyświetlaniem 

Widoczność zawartości jest nadrzędna w stosunku do widoczności wszystkich obiektów, które zawiera. Jeśli zawartość jest ukryta, obiekty, które zawiera, również zostaną ukryte, nawet jeśli ich właściwości **Widoczność** są ustawione na wartość `True`.

Wiele [Szkiców](Sketch/pl.md) może być widocznych w tym samym czasie, ale tylko jedna [Cecha](PartDesign_Feature/pl.md) *(wynik bryły)* może być widoczna w tym samym czasie. Wybranie ukrytej cechy i naciśnięcie klawisza **Spacja** na klawiaturze spowoduje, że stanie się ona widoczna i automatycznie ukryje wcześniej prezentowaną cechę.

![](images/PartDesign_Body_Visibility.png ) 
*Zawartość Projektu części: wiele [Szkiców](Sketch/pl.md) może być widocznych jednocześnie, ale tylko jedna [cecha](PartDesign_Feature/pl.md) bryły może być widoczna w tym samym czasie, niezależnie od tego, czy jest to Czubek, czy nie.*

### Przyłączanie

[Cecha Projektu części](PartDesign_Feature/pl.md), tak jak [obiekty planarne](Part_Part2DObject/pl.md), mogą być dołączone do różnych płaszczyzn, zazwyczaj standardowych płaszczyzn zdefiniowanych przez [Odniesienie położenia](PartDesign_Body/pl#Odniesienie_po.C5.82o.C5.BCenia.md), lub do niestandardowych [płaszczyzn Projektu części](PartDesign_Plane/pl.md).

[Szkice](Sketch/pl.md) są zazwyczaj dołączane do płaszczyzny podczas ich tworzenia. W podobny sposób mogą być dołączane [bryły pierwotne](PartDesign_CompPrimitiveAdditive/pl.md). Przymocowanie tych obiektów do płaszczyzny pozwala na ich przemieszczanie w zawartości poprzez zmianę ich właściwości **Przesunięcie umocowania**. Więcej informacji na temat trybów dołączania można znaleźć na stronie [Część: Edytuj mocowanie](Part_EditAttachment/pl.md).

Element [cecha Projektu części](PartDesign_Feature/pl.md), który nie jest dołączony będzie pokazany z czerwonym symbolem nakładki obok jego ikony w [widoku drzewa](Tree_view/pl.md).

![](images/PartDesign_Body_Feature_attachment.png ) 
*Zawartość Projektu części: [Cechy projektu części](PartDesign_Feature/pl.md), które nie są dołączone do płaszczyzny lub układu współrzędnych będą pokazane z symbolem nakładki obok ich ikony w [widok drzewa](Tree_view/pl.md).*

### Dziedziczenie

[Zawartość Projektu części](PartDesign_Body/pl.md) jest formalnie instancją klasy `PartDesign::Body`, której rodzicem jest [cecha części](Part_Feature/pl.md) *(klasa `Part::Feature`)* poprzez pośrednią klasę `Part::BodyBase`, i jest uzupełniona o rozszerzenie Odniesienie położenia.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony schemat zależności pomiędzy podstawowymi obiektami programu. Obiekt `PartDesign::Body* jest przeznaczony do budowania parametrycznych brył 3D, a więc wywodzi się z podstawowego obiektu {{incode|Part::Feature` i posiada Odniesienie położenia do kontroli rozmieszczenia cech użytych wewnątrz siebie.}}

## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Zobacz stronę [Cecha części](Part_Feature/pl.md), aby uzyskać ogólne informacje na temat dodawania obiektów do dokumentu.

Zawartość środowiska Projekt części jest tworzona w dokumencie za pomocą metody `addObject()`. Gdy Zawartość już istnieje, [cecha Projekt części](PartDesign_Feature/pl.md) może być do niego dodana za pomocą metod `addObject()` lub `addObjects()` tej zawartości.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj.Label = "Custom label"

feat1 = App.ActiveDocument.addObject("PartDesign::AdditiveBox", "Box")
feat2 = App.ActiveDocument.addObject("PartDesign::AdditiveCylinder", "Cylinder")

obj.addObjects([feat1, feat2])
App.ActiveDocument.recompute()
```

W dokumencie, który ma wiele obiektów Zawartości, można ustawić [aktywny obiekt](PartDesign_Body/pl#Aktywny_status.md) za pomocą `setActiveObject` i metody `ActiveView`. Pierwszym argumentem jest stały ciąg znaków `"pdbody"`, a drugim argumentem jest obiekt Zawartość, który ma zostać uaktywniony. 
```python
import FreeCAD as App
import FreeCADGui as Gui

doc = App.newDocument()
obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("PartDesign::Body", "Body")

Gui.ActiveDocument.ActiveView.setActiveObject("pdbody", obj1)
App.ActiveDocument.recompute()
```





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Body/pl
