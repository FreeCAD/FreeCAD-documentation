---
 GuiCommand:
   Name: Arch Window
   Name/pl: BIM: Okno
   MenuLocation: 3D / BIM , Okno
   Workbenches: BIM_Workbench/pl
   Shortcut: **W** **I**
   SeeAlso: 
---

# Arch Window/pl



## Opis

Narzędzie **Okno** tworzy obiekt bazowy dla wszelkiego rodzaju \"osadzalnych\" obiektów, takich jak okna i drzwi. Okno środowiska Architektura może być niezależne lub \"umieszczone\" wewnątrz innego elementu, takiego jak [Ściana](Arch_Wall/pl.md), [Konstrukcja](Arch_Structure/pl.md) lub [Dach](Arch_Roof/pl.md). Ma własną geometrię, która może być wykonana z kilku stałych elementów *(zwykle rama i panele wewnętrzne)*, a także definiuje objętość, która ma zostać odjęta od obiektów nadrzędnych w celu utworzenia otworu.

Obiekty okien są oparte na zamkniętych obiektach 2D, takich jak [prostokąt](Draft_Rectangle/pl.md) środowiska Rysunek Roboczy lub [szkicach](Sketcher_Workbench/pl.md) środowiska Szkicownik, które są używane do definiowania ich wewnętrznych komponentów. Podstawowy obiekt 2D musi zatem zawierać kilka zamkniętych polilinii, które można łączyć w celu utworzenia wypełnionych paneli *(jedna polilinia)* lub ramek *(kilka polilinii)*.

Narzędzie Okno zawiera kilka [nastaw wstępnych](#Nastawy_wstępne.md). Pozwalają one użytkownikowi na tworzenie popularnych typów okien i drzwi z pewnymi edytowalnymi parametrami, bez konieczności ręcznego tworzenia podstawowych obiektów 2D i komponentów.

Wszystkie informacje dotyczące okna mają również zastosowanie do [drzwi](Arch_Door/pl.md), ponieważ jest to ten sam obiekt.

<img alt="" src=images/Arch_Window_example2.jpg  style="width:600px;"> 
*Złożone okno konstruowane na [Szkicu](Sketcher_Workbench/pl.md). Wchodząc w tryb edycji okna możesz tworzyć różne komponenty, ustawiać ich grubość, a także wybierać i przypisywać do nich polilinie ze szkicu.*



## Użycie



### Korzystanie z ustawień wstępnych 

Jest kilka sposobów na wywołanie tego polecenia:

#\* Wciśnij przycisk **<img src="images/Arch_Window.svg" width=16px> [Okno](Arch_Window/pl.md)**.

#\* Wybierz opcję **3D/BIM → <img src="images/Arch_Window.svg" width=16px> Okno** z menu.

#\* Użyj skrótu klawiszowego: **W** a następnie **I**.

1.  Wybierz jeden z predefiniowanych szablonów z listy.
2.  Wypełnij wymagane parametry.
3.  W [widoku 3D](3D_view/pl.md), przesuń obiekt okna w miejsce, gdzie chcesz je umieścić. Jeśli najedziesz kursorem na [ścianę](Arch_Wall/pl.md), zarys okna powinien dostosować się do tej ściany.
4.  Kliknij w oknie [widoku 3D](3D_view/pl.md) myszką, lub naciśnij klawisz **Enter** trzy razy, aby potwierdzić współrzędne X, Y, Z umieszczenia.



#### Nastawy dodatkowe 

Jeśli zainstalujesz [Parts Library](Parts_Library_Workbench/pl.md) z [Menadżera dodatków](Std_AddonMgr/pl.md), narzędzie okna przeszuka tę bibliotekę w poszukiwaniu dodatkowych ustawień wstępnych. Te ustawienia wstępne to pliki FreeCAD zawierające pojedyncze okno oparte na szkicu parametrycznym z nazwanymi ograniczeniami. Możesz umieścić dodatkowe ustawienia wstępne w katalogu **parts_library**, aby zostały znalezione przez narzędzie do okien.


**$ROOT_DIR/Mod/parts_library/Architectural Parts/Doors/Custom/**

**$ROOT_DIR/Mod/parts_library/Architectural Parts/Windows/Custom/**

-   Zmienna **$ROOT_DIR** to katalog użytkownika, w którym przechowywane są pliki konfiguracyjne FreeCAD, makra oraz zewnętrzne środowiska pracy. Można go znaleźć, wpisując `FreeCAD.getUserAppDataDir()` w [konsoli Python](Python_console/pl.md).

  ** Na systemach Linux zazwyczaj znajduje się w **/home/username/.local/share/FreeCAD/** ({{VersionPlus/pl|0.20}}) lub **/home/username/.FreeCAD/** ({{VersionMinus/pl|0.19}})
  ** Na systemach Windows zazwyczaj znajduje się w **C:\Users\username\Application Data\FreeCAD/**
  ** Na systemach Mac OSX zazwyczaj znajduje się w **/Users/username/Library/Preferences/FreeCAD/**

-   Nazwa podkatalogu **Custom** to jedynie sugestia, można użyć dowolnej nazwy. Jednak pliki muszą być umieszczone w jednym lub więcej podkatalogach wewnątrz katalogów **Doors** lub **Windows**.



### Tworzenie okna użytkownika 

1.  Opcjonalnie, wybierz powierzchnię na obiekcie Architektury, gdzie chcesz umieścić okno.
2.  Przełącz się do środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).
3.  Utwórz nowy szkic.
4.  Narysuj jedną lub więcej zamkniętych polilinii *(pętli)*. Zwróć szczególną uwagę na kolejność tworzenia tych pętli, od tego zależy numeracja polilinii w [panelu zadań](Task_panel/pl.md) *(\"Elementy okna\")*.
5.  Zamknij szkic.
6.  Wróć do środowiska pracy [BIM](BIM_Workbench/pl.md).
7.  Kliknij przycisk **<img src="images/Arch_Window.svg" width=16px> [Okno](Arch_Window/pl.md)**, lub wciśnij klawisze **W** a następnie **I**.
8.  Aby dostosować składniki okna oraz różne właściwości, przejdź do panelu zadań dla okna, klikając dwukrotnie na utworzony obiekt w [widoku drzewa](Tree_view/pl.md).
9.  Należy pamiętać, że ponieważ komponenty następujące po komponencie zawiasowym również będą miały zawiasy, wszystkie komponenty stałe, takie jak ramy zewnętrzne i nieruchome panele szklane, muszą zostać zdefiniowane przed komponentami zawiasowymi. Panel szklany w ramie zawiasowej należy zdefiniować za tą ramą i przed innymi elementami zawiasowymi.



## Nastawy wstępne 

Dostępne są następujące ustawienia wstępne:

Image:ParametersWindowFixed.svg\|Stałe Image:ParametersWindowSimple.svg\|Otwarta 1 szyba Image:ParametersWindowDouble.svg\|Otwarta 2 szyby Image:ParametersWindowStash.svg\|Skrzydło 2-szybowe Image:ParametersWindowDouble.svg\|Przesuwne 2-szybowe Image:ParametersDoorSimple.svg\|Proste drzwi Image:ParametersDoorGlass.svg\|Drzwi szklane Image:ParametersWindowDouble.svg\|Przesuwne 4-szybowe Image:ParametersWindowSimple.svg\|Markiza Image:ParametersOpening.svg\|Tylko otwieranie {{Version/pl|1.0}}



## Komponenty budynku 

Okna mogą składać się z 4 rodzajów elementów: ram, paneli pełnych, paneli szklanych i żaluzji. Panele i żaluzje są wykonane z jednej zamkniętej polilinii, która jest wytłaczana, podczas gdy ramy są wykonane z 2 lub więcej zamkniętych żył, z których każda jest wytłaczana, a następnie mniejsze są odejmowane od największej. Komponenty okna można tworzyć, modyfikować i usuwać w trybie edycji *(klikając dwukrotnie okno w widoku drzewa)*. Komponenty mają następujące właściwości:

-   **Nazwa**: Nazwa komponentu.
-   **Typ**: Typ komponentu. Może być \"Rama\", \"Panel szklany\", \"Panel stały\" lub \"Żaluzje\".
-   **Polilinie**: Lista drutów, na których opiera się komponent, oddzielona przecinkami.
-   **Grubość**: Grubość wyciągnięcia komponentu.
-   **Przesunięcie Z**: Odległość między komponentem a jego bazowymi poliliniami 2D.
-   **Zawias**: Pozwala na wybór krawędzi z podstawowego obiektu 2D, a następnie ustawienie tej krawędzi jako zawiasu dla tego komponentu i kolejnych na liście.
-   **Tryb otwierania**: Jeśli zdefiniowano zawias w tym komponencie lub którymkolwiek wcześniej na liście, ustawienie trybu otwierania spowoduje, że okno będzie wyglądać na otwarte lub będzie wyświetlać symbole otwarcia w planie lub elewacji.

<img alt="" src=images/Arch_Window_options.jpg  style="width:600px;">



## Opcje

-   Okna dzielą wspólne właściwości i zachowania wszystkich [komponentów](Arch_Component/pl.md).
-   Jeśli pole wyboru **Automatyczne dołączanie do obiektu nadrzędnego** na panelu tworzenia okna jest odznaczone, okno nie zostanie wstawione do żadnego obiektu nadrzędnego podczas tworzenia.
-   Dodaj wybrane okno do [ściany](Arch_Wall/pl.md) przez zaznaczenie obu, a następnie naciśnięcie przycisku **<img src="images/Arch_Add.svg" width=16px> [Połącz obiekty](Arch_Add/pl.md)**.
-   Usuń wybrane okno ze [ściany](Arch_Wall/pl.md) poprzez zaznaczenie okna, a następnie naciśnięcie przycisku **<img src="images/Arch_Remove.svg" width=16px> [Usuń komponent](Arch_Remove/pl.md)**.
-   Podczas korzystania z predefiniowanych ustawień często wygodnie jest włączyć [przyciąganie](Draft_Snap/pl.md) \"Do najbliższego\" , aby można było przyciągnąć okno do istniejącej powierzchni.
-   Otwór stworzony przez okno w jego obiekcie hosta jest określany przez dwie właściwości: **Głębokość otworu** i **Polilinia otworu** *({{Version/pl|0.17}})*. Numer Polilinii otworu można wybrać w widoku 3D z panelu zadań okna dostępnego po podwójnym kliknięciu okna w widoku drzewa.
-   Okna mogą korzystać z [Multi-materiałów](Arch_MultiMaterial/pl.md). Okno będzie wyszukiwać w załączonym Multi-materiałze warstwy materiałów o tej samej nazwie dla każdego z jego komponentów okna i używać jej, jeśli taka zostanie znaleziona. Na przykład komponent o nazwie \"OuterFrame\" będzie szukał w załączonym Multi-materiale warstwy materiałów o nazwie \"OuterFrame\". Jeśli taka warstwa materiałów zostanie znaleziona, jej materiał zostanie przypisany do komponentu OuterFrame. Wartość grubości warstwy materiałowej jest ignorowana.



## Otwieranie


**See also:**

[Poradnik dla otwartych okien](Tutorial_for_open_windows/pl.md)

Drzwi i okna mogą być częściowo lub całkowicie otwarte w modelu 3D lub mogą wyświetlać symbole otwarcia zarówno na planie, jak i / lub elewacji. W rezultacie będą one również widoczne w wyodrębnionych widokach 2D generowanych przez narzędzie [Widok 2D kształtu](Draft_Shape2DView/pl.md) środowiska Rysunek roboczy lub środowisko [Rysunek Techniczny](TechDraw_Workbench/pl.md). Aby to uzyskać, przynajmniej jeden komponent drzwi musi mieć zawias i zdefiniowany tryb otwarcia *(patrz [Komponenty budynku](#Komponenty_budynku.md) powyżej)*. Następnie, korzystając z właściwości **Otwieranie**, **Symbol planu** lub **Symbol Elewacji**, można skonfigurować wygląd okna:

<img alt="" src=images/Arch_window_openings.png  style="width:600px;"> 
*Drzwi pokazujące plan symbolu, elewację symbolu i właściwości otwierania podczas pracy.*



## Definiowanie typów okien 

Okna mogą również wykorzystywać inne narzędzia, w szczególności przepływy pracy środowiska [Projekt Części](PartDesign_Workbench/pl.md), do definiowania typu. Typ jest obiektem, który definiuje kształt okna. Jest to szczególnie przydatne do pracy z [App: Część](App_Part/pl.md):

<img alt="" src=images/Arch_window_type_example.png  style="width:800px;">

[Pobierz przykładowy plik pokazany powyżej](https://github.com/FreeCAD/Examples/raw/master/Arch_Example_Files/Window_Type.FCStd)



### Przykład przepływu pracy 

-   Stwórz obiekt ramy okiennej, panel szklany i inne elementy okna, korzystając z narzędzi środowisk [Część](Part/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md).
-   Na przykład, stwórz prostokątny szkic podstawowy dla okna, następnie szkic profilu dla ramy i utwórz [Wyciągnięcie po ścieżce](Part_Sweep/pl.md), aby wyprofilować profil wokół szkicu podstawowego. Utwórz [Odsunięcie 2D](Part_Offset2D/pl.md) z szkicu podstawowego, a następnie [Wyciągnij](Part_Extrude/pl.md), aby utworzyć panel szklany.
-   Upewnij się, że wszystkie te elementy mają unikalną, znaczącą nazwę *(na przykład \"Rama\" lub \"Panel szklany\")*.
-   Stwórz obiekt [App: Część](App_Part/pl.md) i umieść w nim wszystkie swoje komponenty podrzędne.
-   Utwórz wolumin do odjęcia od ściany, na przykład poprzez wyciągnięcie szkicu podstawowego. Dodaj tę objętość do App Part. Upewnij się, że objętość jest wyłączona.
-   Jeśli korzystasz z wersji FreeCAD 0.19 lub nowszej, możesz dodać 3 właściwości do swojego obiektu App: Część, klikając prawym przyciskiem myszki w widoku właściwości i zaznaczając \"Pokaż wszystkie\". Dodaj następujące właściwości *(wszystkie są opcjonalne, grupa nie ma znaczenia)*:

 - **Wysokość** jako PropertyLength i połącz ją, na przykład, z pionowym wiązaniem szkicu podstawowego.
 - **Szerokość** jako PropertyLength i połącz ją, na przykład, z poziomym wiązaniem szkicu podstawowego.
 - **Objętość podrzędna** jako PropertyLink i połącz go z objętością do odjęcia, którą utworzyliśmy powyżej.
 - **Tag** jako StringWłaściwości.

Nasz typ okna jest już gotowy. Możemy tworzyć z niego obiekty okien, po prostu wybierając App: Część i naciskając przycisk okna. Właściwości \"Wysokość\", \"Szerokość\", \"Objętość\" i \"Znacznik\" okna zostaną powiązane z odpowiednimi właściwościami App Part, jeśli takie istnieją.



### Materiały

Aby utworzyć materiał dla okien opartych na typach:

-   Utwórz [materiał złożony](Arch_MultiMaterial/pl.md)
-   Utwórz jeden wpis w materiał złożony dla każdego komponentu App Część. Na przykład, jeden \"Frame\", jeden \"Glass panel\", jak użyliśmy powyżej. Upewnij się, że używasz dokładnie tej samej nazwy.
-   Przypisz ten materiał złożony do każdego okna pochodzącego z tego samego typu.

Możesz użyć dowolnego innego rodzaju przepływu pracy niż ten opisany powyżej, ważne punkty do zapamiętania to:

-   Obiekt typu musi być jednym obiektem, bez względu na typ *(App: Część, Zawartość środowiska Projektu Części, Złożenie środowiska Część, a nawet inne okno środowiska Architektura)*
-   Obiekt typu musi mieć właściwość \"Objętość podrzędna\" *(powiązaną z właściwością Objętość podrzędna okna)*, aby otwory w obiektach nadrzędnych działały.
-   Obiekt typu musi mieć właściwość \"Grupa\" z różnymi elementami podrzędnymi o takich samych nazwach jak elementy wielomateriałowe, aby działały elementy wielomateriałowe.



## Właściwości



### Dane


{{TitleProperty|Okno}}

-    **Powierzchnia|Area**: Powierzchnia tego okna.

-    **Rama|Length**: Rozmiar ramy (grubość/głębokość) tego okna.

-    **Wysokość|Length**: Wysokość tego okna.

-    **Głębokość otworu|Length**: Głębokość otworu utworzonego przez to okno w jego obiekcie gospodarzu.

-    **Polilinia otworu|Integer**: Numer polilinii z obiektu bazowego używanego do stworzenia otworu w obiekcie gospodarzu tego okna. Wartość można ustawić graficznie, klikając dwukrotnie okno w widoku drzewa. Ustawienie wartości 0 spowoduje, że okno automatycznie wybierze największą polilinię dla otworu.

-    **Gospodarze|LinkList**: Obiekty (np. ściana), które są gospodarzami tego okna.

-    **Odległość między okiennicami|Length**: Jeśli którykolwiek z komponentów jest ustawiony jako \"Okiennice\", ta właściwość definiuje rozstaw między elementami okiennic.

-    **Szerokość okiennic|Length**: Jeśli którykolwiek z komponentów jest ustawiony jako \"Okiennice\", ta właściwość definiuje rozmiar elementów okiennic.

-    **Normalny|Vector**: Kierunek normalny tego okna, ustawiony (na stałe) przez narzędzie Okno w trybie interaktywnym. Uwaga: Ustawienie na (0,0,0) sprawia, że okno automatycznie dedukuje kierunek normalny, co jest przydatne, gdy użytkownik obraca bazowy szkic okna, np. gdy jego gospodarzem jest obrócona ściana.

-    **Odsunięcie|Length**: Rozmiar odsunięcia (od bazowego szkicu) tego okna.

-    **Otwarcie|Percent**: Wszystkie komponenty, które mają ustawiony tryb otwierania, a w których zdefiniowano zawias (lub w wcześniejszym komponencie na liście), będą otwierane procentowo zgodnie z tą wartością.

-    **Preset|Integer|Hidden**: Numer presetu, na którym bazuje to okno.

-    **Podobjętość|Link**: Opcjonalny obiekt definiujący objętość odejmowaną od gospodarzy tego okna.

-    **Symbol wysokości|Bool**: Wyświetla symbol otwarcia 2D na elewacji.

-    **Symbol planu|Bool**: Wyświetla symbol otwarcia 2D na planie.

-    **Szerokość|Length**: Szerokość tego okna.

-    **Części okna|StringList|Hidden**: Komponenty tego okna (5 ciągów na komponent).



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Okno** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
Window = makeWindow(baseobj=None, width=None, height=None, parts=None, name="Window")
```

-   Tworzy obiekt `Okno` na podstawie `baseobj`, który powinien być dobrze uformowaną, zamkniętą [polilinią](Draft_Wire/pl.md) lub [Szkicem](Sketcher_Workbench/pl.md).
-   Jeśli dostępne, ustawia `szerokość`, `wysokość`, i `nazwa` *(etykietę)* dla Okna.
-   Jeśli `baseobj` nie jest zamkniętym kształtem, narzędzie może nie utworzyć prawidłowej bryły.

Przykład:


```python
import FreeCAD, Draft, Arch

Rect1 = Draft.makeRectangle(length=900, height=3000)
Window = Arch.makeWindow(Rect1)
FreeCAD.ActiveDocument.recompute()
```

Okno można również utworzyć z ustawienia wstępnego.


```python
Window = makeWindowPreset(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)
```

-   Tworzy obiekt `Window` na podstawie `windowtype`, który powinien być jedną z nazw zdefiniowanych w `Arch.WindowPresets`.
-   Parametry `width` i `height` definiują całkowity rozmiar obiektu, z jednostkami w milimetrach.
-   Parametry `h1`, `h2`, `h3` *(przesunięcia pionowe)*, `w1`, `w2` *(szerokości)*, `o1` i `o2` *(przesunięcia poziome)* określają różne odległości w milimetrach i zależą od typu tworzonego ustawienia wstępnego.
-   Jeśli podano `placement`, jest on używany.

Przykład:


```python
import FreeCAD, Arch

base = FreeCAD.Vector(2000, 0, 0)
Axis = FreeCAD.Vector(1, 0, 0)
place=FreeCAD.Placement(base, FreeCAD.Rotation(Axis, 90))

Door = Arch.makeWindowPreset("Simple door",
                             width=900, height=2000,
                             h1=100, h2=100, h3=100, w1=200, w2=100, o1=0, o2=100,
                             placement=place)
```



---
⏵ [documentation index](../README.md) > Arch Window/pl
