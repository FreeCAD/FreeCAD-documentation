# NativeIFC/pl
-   -   Uwaga\*\*: Funkcjonalność Natywne IFC jest wciąż w trakcie opracowywania i nie została jeszcze ukończona. Pamiętaj o tym podczas korzystania z niej i nie polegaj na niej, dopóki nie będziesz pewny, że spełnia Twoje oczekiwania. Więcej informacji na temat rozwoju, tego co działa i co jest planowane, można znaleźć w [planie rozwoju](https://github.com/yorikvanhavre/FreeCAD-NativeIFC/blob/main/doc/roadmap2024.md).



## Wprowadzenie

Od wersji 1.0 FreeCAD wykorzystuje [koncepcję Natywne IFC](https://github.com/brunopostle/ifcmerge/blob/main/docs/whitepaper.rst). Umożliwia ona użytkownikom FreeCAD otwieranie, manipulowanie i tworzenie plików IFC bezpośrednio w programie FreeCAD.

Chociaż FreeCAD od dawna wspierał otwieranie i zapisywanie plików IFC za pomocą środowiska pracy Arch, robił to, jak większość innych aplikacji BIM, konwertując w jedną i drugą stronę między formatem pliku IFC a wewnętrznym modelem danych FreeCAD. Oznacza to dwie konwersje: jedna podczas otwierania a druga podczas zapisywania, co powoduje utratę danych oraz całkowite przepisywanie pliku za każdym razem. W związku z tym, jest to nieodpowiednie dla [systemów kontroli wersji](https://en.wikipedia.org/wiki/Version_control), takich jak [Git](https://en.wikipedia.org/wiki/Git) oraz bardzo trudne do zlokalizowania zmian.

Natywne IFC oznacza, że sam plik IFC jest strukturą danych w programie FreeCAD. Podczas otwierania pliku IFC we FreeCAD, to co widzisz na ekranie, jest bezpośrednim renderowaniem zawartości pliku IFC. Wszystko, co zmodyfikujesz, bezpośrednio zmieni plik IFC. Jeśli otworzysz plik, zmodyfikujesz jeden element i zapiszesz plik, jedyną rzeczą, która zmieni się w pliku, będzie linia dotycząca tego elementu. Reszta pliku pozostanie w 100% identyczna jak przed zapisaniem. Brak utraty danych i bardzo łatwe do zidentyfikowania zmiany.

Koncepcja Natywnego IFC pochodzi z [tego artykułu autorstwa Bruno Postle](https://github.com/brunopostle/ifcmerge/blob/main/docs/whitepaper.rst). Jest mocno inspirowana oprogramowaniem [BlenderBIM](https://blenderbim.org/) i stara się w jak największym stopniu używać tych samych koncepcji i ponownie wykorzystywać kod. Ostatecznym celem jest zaoferowanie we FreeCAD takiego samego poziomu funkcjonalności i wydajności, jakie można znaleźć w BlenderBIM oraz przekazywanie jak najwięcej do [IfcOpenShell](https://ifcopenshell.org/), wspólnego silnika IFC używanego przez obie aplikacje. Projekt rozpoczął się jako [odrębny projekt Yorika](https://github.com/yorikvanhavre/FreeCAD-NativeIFC).

Praca z natywnymi plikami IFC we FreeCAD jest prosta: Otwórz istniejący plik IFC lub stwórz nowy projekt używając narzędzia [Projekt](BIM_Project/pl.md) ze [środowiska pracy BIM](BIM_Workbench/pl.md). Twórz nowe obiekty za pomocą dowolnych środowisk pracy lub narzędzi FreeCAD. Dodaj te obiekty do swojego projektu IFC, przeciągając je do struktury projektu. Zapisz plik i gotowe.

Poniżej znajdziesz więcej szczegółów.



## Tryb zablokowany i odblokowany 

[Środowisko pracy BIM](BIM_Workbench/pl.md) oferuje dwa tryby pracy z plikami IFC. Przełączanie między tymi trybami odbywa się poprzez kliknięcie **przycisku blokady** na pasku statusu FreeCAD:

![](images/BIM-statusbar-lock.jpg )

-   **Tryb odblokowany** (domyślny): Możesz mieć zarówno projekty Natywne IFC, jak i elementy inne niż IFC w tym samym dokumencie FreeCAD. Możesz również pracować nad modelami BIM bez tworzenia projektu Natywne IFC i nadal eksportować swój model jako IFC.
-   **Tryb zablokowany**: Twój dokument FreeCAD jest plikiem IFC. Wszystko, co robisz, spowoduje zmiany w pliku IFC. Każdy nowo dodany obiekt jest natychmiast konwertowany na IFC.

W trybie zablokowanym wszystkie obiekty, które tworzysz, są natychmiast konwertowane na IFC, co może spowodować utratę niektórych ich pierwotnych właściwości i parametrycznego zachowania, jeśli nie są one obsługiwane przez format IFC. Ten tryb jest bardziej restrykcyjny, co może być wadą w pewnych momentach rozwoju projektu, ale staje się zaletą, gdy integralność danych i niezawodność są kluczowe.

Możliwe jest również tworzenie projektów Natywnych IFC wewnątrz dokumentu w trybie odblokowanym. W takim przypadku ścisłe elementy IFC współistnieją z elementami innymi niż IFC w Twoim dokumencie FreeCAD. Obiekty w ramach projektu IFC są powiązane z załączonym plikiem IFC. Praca z projektami IFC często nie jest potrzebna na wczesnych etapach projektu, ale jeśli współpracujesz z innymi i używasz plików IFC jako głównego medium komunikacji, korzystanie z projektów Natywnych IFC może stać się korzystne, ponieważ zmiany w każdej wersji pliku są znacznie mniejsze.

Zawsze możesz wyeksportować swój model do pliku IFC w razie potrzeby, niezależnie od tego, czy korzystasz z projektu IFC, czy nie. Różnica polega na tym, że gdy używasz projektu IFC, do pliku IFC zapisywane są minimalne zmiany. Gdy nie korzystasz z projektu IFC, cały plik jest przepisywany przy każdym eksporcie. Może to być lub nie być problemem, w zależności od Twoich potrzeb.

Ogólna zasada to praca w trybie odblokowanym, gdy pracujesz nad własnymi projektami, aby mieć zarówno elementy IFC, jak i inne niż IFC w swoich dokumentach, oraz korzystanie z trybu zablokowanego, gdy pracujesz nad plikami IFC innych osób, aby mieć ścisłą kontrolę nad tym, co zmieniasz w tych plikach.



## Koncepcje plików 

Podczas pracy z natywnymi plikami IFC w FreeCAD, projekt IFC (czy to zablokowany, czy odblokowany) zawsze ma przypisany plik IFC. Ten plik IFC zawiera wszystkie dane Twojego projektu IFC wewnątrz FreeCAD i odpowiada również za dostarczanie geometrii jego obiektów do FreeCAD.

Podczas tworzenia nowego projektu IFC, plik IFC jeszcze nie istnieje. Przy pierwszym zapisie pliku FreeCAD zapyta Cię, gdzie chcesz zapisać plik IFC.

W trybie zablokowanym pracujesz bezpośrednio w pliku IFC. Nie ma już pliku FreeCAD.

W trybie odblokowanym masz obiekty projektu IFC przypisane do plików IFC, a dokument FreeCAD jest uzależniony od tych plików IFC. Jeśli chcesz przekazać swój plik FreeCAD komuś innemu, musisz również dostarczyć pliki IFC. Alternatywnie, możesz ustawić tryb kształtu wszystkich obiektów na „Shape" (patrz poniżej). Sprawi to, że plik FreeCAD zachowa kształt wszystkich obiektów IFC i poprawnie je wyświetli nawet bez załączonego pliku IFC. Jednak obiekty IFC wewnątrz nie będą już edytowalne.



## Obiekty IFC vs obiekty BIM 

Gdy obiekt BIM lub jakikolwiek inny obiekt FreeCAD jest powiązany z [projektem](BIM_Project.md) Natywne IFC, staje się obiektem IFC. Powiązanie obiektu z projektem Natywne IFC odbywa się po prostu przez przeciągnięcie, w widoku drzewa, obiektu na projekt lub na jakikolwiek obiekt, który już jest częścią tego projektu, na przykład budynek lub piętro.

Gdy obiekt stanie się obiektem IFC, jest całkowicie kontrolowany przez dane IFC. Traci swoje wcześniejsze właściwości parametryczne FreeCAD i może utracić wszelkie właściwości i cechy parametryczne, które nie są obsługiwane przez format IFC. Celem na przyszłość jest płynne renderowanie wszystkich tych właściwości i zachowanie tych samych możliwości edycyjnych zarówno dla obiektów IFC, jak i innych niż IFC.

## Otwieranie i importowanie plików IFC 

Masz dwie opcje: otwieranie lub import.

-   Jeśli otwierasz, nowy dokument zostanie utworzony, a ty automatycznie znajdziesz się w **trybie zablokowanym**.
-   Jeśli importujesz, obiekt [projektu](BIM_Project/pl.md) natywne IFC zostanie dodany do bieżącego dokumentu, ale nadal możesz tworzyć obiekty inne niż IFC poza tym projektem. Będziesz nadal w **trybie odblokowanym**.

Aby otworzyć plik IFC, użyj menu Plik -\> Otwórz i wybierz plik IFC. Aby zaimportować plik IFC, użyj menu Plik -\> Importuj i wybierz plik IFC.

Aby maksymalnie przyspieszyć początkowy czas importu, otwieranie lub importowanie plików IFC domyślnie renderuje tylko obiekt najwyższego poziomu (zwykle Teren) we FreeCAD. Aby rozszerzyć zawartość tego obiektu, należy dwukrotnie kliknąć go w widoku drzewa (zobacz poniżej).

Importowanie lub otwieranie pliku IFC nie wymaga ustawiania żadnych opcji. Jednak niektóre domyślne ustawienia można dostosować w menu Edycja -\> Preferencje -\> BIM -\> Natywne IFC.



## Tworzenie nowego dokumentu IFC 

Możesz wybrać pracę w trybie zablokowanym lub odblokowanym, w zależności głównie od tego, czy potrzebujesz mieć w dokumencie FreeCAD obiekty inne niż IFC (tryb odblokowany), czy też chcesz, aby wszystko, co robisz w dokumencie, odbywało się w pliku IFC (tryb zablokowany).

Podczas tworzenia nowego projektu IFC, nie ma jeszcze przypisanego pliku IFC. Przy pierwszym zapisywaniu FreeCAD poprosi cię o wybranie lokalizacji, w której chcesz zapisać plik IFC.

**W trybie zablokowanym:**

1.  Utwórz nowy dokument FreeCAD, wybierając z menu Plik -\> Nowy
2.  Naciśnij przycisk <img alt="" src=images/IFC.svg  style="width:24px;"> [Blokada IFC](BIM_ToggleNativeIFC.md) na pasku statusu, aby zablokować dokument

**W trybie odblokowanym:**

1.  Naciśnij przycisk <img alt="" src=images/BIM_Project.svg  style="width:24px;"> [Projekt](BIM_Project/pl.md), aby utworzyć natywny projekt IFC w bieżącym dokumencie FreeCAD. Możesz mieć więcej niż jeden projekt w tym samym dokumencie FreeCAD



## Zapisywanie i eksportowanie plików IFC 

Zawsze możesz wyeksportować dowolny model FreeCAD do formatu IFC, nawet jeśli nie został zbudowany za pomocą narzędzi BIM lub zawiera elementy inne niż BIM. Obiekty inne niż BIM zostaną po prostu wyeksportowane jako ogólne obiekty IfcBuildingElementProxy, podczas gdy obiekty BIM mogą mieć określoną swoją klasę (IfcWall, IfcDoor, itp.).

Projekty Natywne IFC, zarówno w trybie zablokowanym, jak i odblokowanym, zawsze mają dołączony plik IFC. Nie trzeba już niczego eksportować, wystarczy zapisać plik IFC. Sposób zapisywania zawartości IFC różni się w zależności od trybu:

-   Pracując w **trybie zablokowanym**, wszystko, co dzieje się w dokumentach FreeCAD, jest zapisywane w pliku IFC. Nie ma już potrzeby zapisywania pliku FreeCAD, a pozycje w menu *Plik -\> Zapisz* i *Plik -\> Zapisz jako* są zastąpione przez *Plik -\> Zapisz IFC* i *Plik -\> Zapisz IFC jako*. Wystarczy zapisać plik IFC, nie ma już pliku .FCStd.

-   Pracując w **trybie odblokowanym**, każdy obiekt [projektu](BIM_Project/pl.md) IFC w twoim dokumencie będzie powiązany z oddzielnym plikiem IFC. Obiekt projektu śledzi zmiany, a jego ikona pokaże czerwoną kropkę, gdy zawiera niezapisane zmiany. Zapisanie dokumentu FreeCAD spowoduje również zapisanie wszystkich plików IFC powiązanych z projektami IFC znajdującymi się w dokumencie.

W trybie odblokowanym można również zapisywać załączone pliki ręcznie, klikając prawym przyciskiem myszy na projekcie i wybierając IFC -\> Zapisz



## Rozszerzanie zawartości plików 

Podczas otwierania pliku IFC tylko obiekty najwyższego poziomu (zazwyczaj Teren i Budynek) są domyślnie renderowane we FreeCAD (można to zmienić w menu Edycja -\> Preferencje -\> BIM -\> Natywne IFC), a dodatkowe dane, takie jak materiały, właściwości geometryczne, kształt, warstwy i obiekty podrzędne nie są renderowane.

Aby załadować wszystkie dodatkowe dane i wyświetlić bezpośrednie dzieci obiektu, kliknij go dwukrotnie w widoku drzewa.

Możesz także zwinąć rozwinięte obiekty, klikając je prawym przyciskiem myszy w drzewie i wybierając IFC -\> zwiń dzieci.



## Ładowanie i wyładowywanie kształtów 

Domyślnie, aby zwiększyć wydajność, obiekty IFC nie ładują swoich pełnych kształtów. W widoku 3D wyświetlana jest jedynie lekka reprezentacja 3D. Dzięki temu operacje importu i rozwijania są szybkie. Jednak złożone operacje geometryczne, takie jak operacje logiczne czy przekroje wykonywane za pomocą [płaszczyzn przekroju](Arch_SectionPlane/pl.md), wymagają obecności pełnego kształtu. W takich przypadkach może być konieczne załadowanie kształtu obiektów, na których chcesz wykonać te operacje.

Aby wczytać kształt wybranych obiektów, wystarczy ustawić ich właściwość *Shape Mode* na *Shape*.

Aby wyładować kształt i powrócić do trybu lekkiej reprezentacji 3D, należy ustawić właściwość \"Shape Mode\" na \"Coin\" (Coin to nazwa biblioteki renderowania 3D używanej we FreeCAD).

Istnieje trzeci tryb kształtu, *None*, który całkowicie wyłącza wizualną reprezentację obiektów IFC. Są one wtedy kontrolowane wyłącznie za pomocą widoku drzewa.



## Klasy, atrybuty i właściwości 

Wszystkie obiekty IFC zawsze mają co najmniej dwie właściwości: **Class** i **Step ID**. Klasa to klasa IFC (IfcWall, IfcWindow itd.), a Step ID to identyfikator elementu w pliku IFC. Step ID to właściwie jedyne dane potrzebne do zlokalizowania obiektu w pliku IFC. Możesz zmienić klasę obiektu w dowolnym momencie; nie wpłynie to na geometrię ani na zestawy właściwości, ale może zmienić dostępne atrybuty (patrz poniżej). Możesz zmienić klasę tylko na klasę rodzeństwa, klasę nadrzędną lub klasę potomną. Jeśli chcesz zmienić na klasę, która jest bardzo odległa od bieżącej klasy, będziesz musiał znać strukturę klas IFC i powtarzać operację kilka razy.

**Atrybuty** to dodatkowe zakodowane właściwości obiektów IFC, takie jak Nazwa, Opis lub ID. Atrybuty zależą od klasy. Na przykład, IfcWindows ma również długość i szerokość, IfcSites ma długość i szerokość geograficzną itp. Atrybuty są zawsze zgrupowane w grupie **IFC** i są zawsze ładowane razem z obiektem.

Podczas zmiany klasy obiektu atrybuty mogą ulec zmianie. Można edytować wartości atrybutów, ale nie można dodawać ani usuwać atrybutów, ponieważ są one obowiązkowe i zdefiniowane przez standard IFC.

**Właściwości** IFC, które są zgrupowane w zestawach właściwości, to niestandardowe właściwości, które można przypisać do dowolnego obiektu IFC. Nie są one ładowane domyślnie, ale są ładowane po dwukrotnym kliknięciu obiektu. Zestawy właściwości, które są pakietami właściwości dołączanymi do obiektów, są renderowane jako grupy właściwości wewnątrz drzewa właściwości FreeCAD.



## Warstwy i materiały 

**Warstwy** są ładowane po dwukrotnym kliknięciu obiektu. Warstwy są reprezentowane jako [normalne warstwy programu FreeCAD](Draft_Layer.md), ale są przechowywane wewnątrz projektu IFC. Podczas korzystania z narzędzia [Warstwy BIM](BIM_Layers.md) dodatkowa ikona wskazuje, czy warstwa jest częścią projektu IFC, czy nie.

**Materiały** działają według tej samej logiki. Są one ładowane tylko po dwukrotnym kliknięciu obiektu, są reprezentowane jako zwykłe [materiały](Arch_Material/pl.md), ale są przechowywane wewnątrz projektu IFC.



## Struktura budynku 

Zgodnie ze standardami IFC, wszystkie pliki IFC muszą zawierać jeden i tylko jeden obiekt IfcProject (lub IfcProjectLibrary), który stanowi korzeń modelu IFC. Wszystkie inne obiekty IFC mogą być dowolnie agregowane pod tym głównym obiektem (pomysł, który nazywamy \"płaskim plikiem\"), ale standardy IFC wymagają posiadania co najmniej jednego obiektu kontenera budynku (IfcSite, IfcBuilding lub IfcBuildingStorey) pod głównym obiektem IfcProject. W FreeCAD, przy ustawionych opcjach domyślnych, eksportowane pliki IFC zawsze będą zawierać IfcProject i co najmniej jeden kontener budynku (domyślne zostaną utworzone, jeśli ich nie masz).

Chociaż nie jest to obowiązkowe, powszechną praktyką w plikach IFC jest posiadanie zawsze tej samej podstawowej struktury:

IfcProject
  -> IfcSite
     -> IfcBuilding
        -> IfcBuildingStorey

Można również użyć [grup](Std_Group/pl.md) wewnątrz projektów IFC. Standard IFC nie pozwala jednak na zagnieżdżanie grup wewnątrz struktury budynku. Tak więc grupy te zostaną przekonwertowane na IfcAssemblies. Ponieważ jednak większość aplikacji BIM z powodzeniem współpracuje z zagnieżdżonymi grupami, można wyłączyć tę konwersję w preferencjach eksportu IFC.



## Sprawdzanie zmian w projekcie IFC 

Jedną z głównych zalet natywnego systemu IFC jest to, że tylko rzeczy zmienione w FreeCAD są odzwierciedlane w pliku IFC dołączonym do projektu. W rezultacie plik IFC zawiera bardzo niewiele zmian, w przeciwieństwie do tradycyjnych aplikacji BIM, w których plik IFC jest całkowicie przepisywany przy każdym eksporcie.

Pozwala to na precyzyjne zlokalizowanie zmian w pliku. Na przykład przeniesienie ściany zmienia tylko jedną linię: położenie tej ściany. To z kolei pozwala systemom kontroli wersji, takim jak Git, precyzyjnie identyfikować te zmiany i zapisywać tylko przyrosty każdej nowej wersji.

Wizualną reprezentację (diff) zmian w wybranym projekcie IFC można uzyskać za pomocą menu Utils -\> IFC Diff lub, w trybie odblokowanym, klikając projekt IFC prawym przyciskiem myszy i wybierając IFC -\> Diff.



## Dodawanie, usuwanie i modyfikowanie obiektów 

W trybie zablokowanym każdy nowo dodany obiekt (BIM lub nie) jest natychmiast konwertowany do IFC. Nie ma nic więcej do zrobienia.

W trybie odblokowanym każdy nowy obiekt (BIM lub nie) dodany do dokumentu musi zostać dodany do projektu IFC. Odbywa się to poprzez przeciągnięcie obiektu w widoku drzewa i upuszczenie go w dowolnym miejscu w strukturze projektu IFC.

Usunięcie obiektów znajdujących się wewnątrz projektu IFC spowoduje również usunięcie ich z pliku IFC.

Gdy obiekt staje się obiektem IFC, traci swoje poprzednie możliwości parametryczne FreeCAD i dziedziczy całe swoje zachowanie z pliku IFC. W wersji FreeCAD 1.0 możliwości edycji obiektów IFC są nadal ograniczone i odbywają się całkowicie za pomocą właściwości (nie jest jeszcze dostępna edycja graficzna). Aby edytować obiekt, należy załadować jego właściwości geometrii. Odbywa się to poprzez dwukrotne kliknięcie lub kliknięcie prawym przyciskiem myszy i wybranie opcji \"IFC -\> dodaj właściwości geometryczne\" w widoku drzewa.

Edytowalne właściwości geometryczne, takie jak \"Wysokość\" lub \"Szerokość\" są następnie dodawane do obiektu. Są to prace w toku, nie wszystkie właściwości są jeszcze obsługiwane. Zmiana wartości tych właściwości spowoduje zmianę kształtu obiektu.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > NativeIFC/pl
