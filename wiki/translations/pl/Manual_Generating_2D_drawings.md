# Manual:Generating 2D drawings/pl
{{Manual:TOC/pl}}

Kiedy Twój model nie może być wydrukowany lub wyfrezowany bezpośrednio przez maszynę, na przykład *(budynek)* jest za duży lub wymaga ręcznego montażu po przygotowaniu elementów, zazwyczaj będziesz musiał wyjaśnić innej osobie, jak to zrobić. W dziedzinach technicznych *(inżynieria, architektura, itp.)*, zazwyczaj wykonuje się to za pomocą rysunków. Rysunki są przekazywane osobie odpowiedzialnej za montaż produktu końcowego i precyzują, jak to wykonać.

Typowymi przykładami mogą być instrukcje z marketu Ikea, oraz [rysunki architektoniczne](https://en.wikipedia.org/wiki/Architectural_drawing), i [projekty](https://en.wikipedia.org/wiki/Blueprint). Rysunki te zazwyczaj zawierają nie tylko sam szkic, ale również wiele adnotacji, takich jak tekst, wymiary, liczby i symbole, które pomogą innym ludziom zrozumieć, co i jak należy wykonać.

W programie FreeCAD środowiskiem pracy odpowiedzialnym za tworzenie takich rysunków jest <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md).

Środowisko pracy TechDraw pozwala na tworzenie arkuszy, które mogą być puste lub korzystać z gotowych [szablonów](TechDraw_Templates/pl.md), aby mieć już szereg elementów na arkuszu, takich jak ramki i tytuł. Na tych arkuszach możesz umieścić widoki wcześniej modelowanych obiektów 3D i skonfigurować, sposób w jaki te widoki będą się pojawiać na arkuszu. Możesz również umieścić na arkuszu wszelkiego rodzaju adnotacje, takie jak wymiary, teksty i inne symbole powszechnie używane w rysunkach technicznych.

Arkusze rysunków, po ukończeniu, można wydrukować lub wyeksportować jako pliki w formacie [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics), PDF lub [DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF).

W poniższym ćwiczeniu zobaczymy, jak stworzyć prosty rysunek modelu krzesła znajdującego się w bibliotece [FreeCAD](https://github.com/FreeCAD/FreeCAD-library) *(Furniture → Chairs → IkeaLikeChair)*. Biblioteka FreeCAD, może być łatwo dodana do Twojej instalacji programu *(patrz rozdział [instalacja](Manual:Installing/pl.md) tego podręcznika)*, lub możesz po prostu pobrać model ze strony internetowej biblioteki, lub za pośrednictwem bezpośredniego łącza podanyego na dole tego rozdziału.

![](images/Exercise_TechDraw_01.svg )

-   Wczytaj plik IkeaLikeChair z biblioteki. Możesz wybrać wersję pliku [FCStd](File_Format_FCStd.md), która załaduje pełną historię modelowania, lub [step](STEP.md), która utworzy tylko jeden obiekt, bez historii. Ponieważ nie będziemy już musieli dalej modelować, najlepiej wybrać wersję step, ponieważ będzie ona łatwiejsza do manipulowania.

![](images/Parts_library.jpg )

-   Przełącz się do środowiska pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek techniczny](TechDraw_Workbench/pl.md)
-   Naciśnij przycisk <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:24px;"> [Wstaw nową stronę przy użyciu szablonu](TechDraw_PageTemplate/pl.md)
-   Wybierz szablon **A4\_Portret\_ISO7200TD**. W oknie FreeCAD zostanie otwarta kolejna zakładka, pokazująca nową stronę.
-   W oknie [widoku drzewa](Tree_view/pl.md) *(lub w zakładce model)*, wybierz model krzesła. Najprawdopodobniej zostanie on nazwany czymś w rodzaju *\"Otwórz importer CASCADE STEP\"*.
-   Naciśnij przycisk <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [Wstaw widok](TechDraw_View/pl.md).
-   Obiekt Widoku zostanie utworzony na naszej stronie. Wybierz obiekt widoku w widoku drzewa, a następnie nadaj widokowi następujące cechy [właściwości](TechDraw_View/pl#Właściwosci.md) w zakładce danych widoku połączonego:
    -   Pod kategorią Baza:
        -   X: 70mm,
        -   Y: 120mm,
        -   Obrót: 0,
        -   Skala: 0.1.
    -   Pod kategorią Rzutowanie *(naciśnij strzałkę w dół, aby indywidualnie zmodyfikować składowe x, y i z, tych właściwości)*:
        -   Kierunek: \[0 0 1\]
        -   Kierunek X: \[0 -1 0\] *(Zmień najpierw pole y, potem pole x)*.
-   Mamy teraz ładny widok z góry na nasze krzesło. Naciśnij przycisk <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:24px;"> [Włącz / wyłącz wyświetlanie ramek](TechDraw_ToggleFrame/pl.md) służy on do wyświetlania widoku ramek, etykiet i wierzchołków widoku.

![](images/Exercise_drawing_02.jpg )

-   Powtórzmy operację dwa razy, żeby stworzyć jeszcze dwa widoki. Ustawimy dla nich wartości X i Y, które wskazują położenie widoku na stronie, w celu pokazania ich niezależnie od widoku z góry, oraz ich kierunku, aby utworzyć różne orientacje widoków. Nadaj każdemu z nowych widoków następujące właściwości:
    -   View001 *(widok z przodu)*: X: 70, Y: 220, Skala: 0.1, Obrót: 0, Kierunek: *(-1,0,0)*, XDirection: *(0,-1,0)*
    -   View002 *(widok z boku)*: X: 150, Y: 220, Skala: 0.1, Obrót: 0, Kierunek: *(0,-1,0)*, Kierunek: XDirection: *(1,0,0)*
-   Otrzymujemy następujący dokument:

![](images/Exercise_TechDraw_04.png )

-   Zwróć uwagę, że mogą być łatwiejsze sposoby na uzyskanie widoku, którego potrzebujesz. Możesz po prostu [obrócić](Manual_Navigating_in_the_3D_view.md) swój model w widoku 3D, a gdy już będziesz miał odpowiedni widok, wybierz model w widoku drzewa i naciśnij przycisk <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> Nowy widok. Spowoduje to automatyczne wstawienie widoku z żądanymi właściwościami obrotu i kierunku. Możesz również użyć narzędzia <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:16px;"> [Grupa rzutów](TechDraw_ProjectionGroup/pl.md)

-   Możemy dopasować ustawienia naszych widoków jeśli chcemy, na przykład możemy zmienić ich właściwość **Szerokość linii** *(pod zakładką Widok w okienku widoku połączonego)* na 0.5.

Teraz umieścimy wymiary i oznaczenia na naszym rysunku. Istnieją dwa sposoby dodawania wymiarów do modelu:
pierwszy polega na umieszczeniu wymiarów w modelu 3D za pomocą narzędzia <img alt="" src=images/_Draft_Dimension.svg  style="width:16px;"> [Dimension](Draft_Dimension/pl.md) z Środowiska pracy [Draft](Draft_Workbench/pl.md), a następnie umieszczenie widoku tych wymiarów na naszym arkuszu za pomocą narzędzia <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [Nowy rysunek roboczy](TechDraw_DraftView/pl.md).
Drugi to wykonywanie czynności bezpośrednio na arkuszu Rysunku Technicznego. Użyjemy tej drugiej metody.

-   Wciśnij przycisk <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> Przełącznik do włączania widoku wierzchołków.
-   Użyj klawiszy **Ctrl** + Lewy klawisz myszki, by zaznaczyć dwa wierzchołki, między którymi chcesz zmierzyć odległość.
-   Naciśnij przycisk <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md).

![](images/Exercise_TechDraw_05.png )

-   Powtarzaj tą operację, aż wszystkie wymiary, które chcesz określić, zostaną umieszczone. Użyj narzędzia <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Wstaw wymiar pionowy](TechDraw_VerticalDimension/pl.md) i <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Wstaw wymiar poziomy](TechDraw_HorizontalDimension.md) w razie potrzeby.
-   Poświęć chwilę, aby spojrzeć na [właściwości](TechDraw_LengthDimension/pl#Właściwości.md) obiektu **Wymiar długości** w okienku widoku połączonego.
-   Zwróć uwagę, że jeśli wymiarujesz widok [aksonometryczny](https://en.wikipedia.org/wiki/Axonometric_projection) *(np. izometryczny)* zamiast [wieloekranowego](https://en.wikipedia.org/wiki/Multiview_projection) *(np. widok z przodu)*, tak jak zrobiliśmy to tutaj, będziesz musiał użyć <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:16px;"> [powiązania wymiaru](TechDraw_LinkDimension/pl.md), aby uzyskać dokładny wymiar.

![](images/Exercise_TechDraw_07.png )

-   Teraz umieścimy dwa objaśnienia pokazane na powyższym obrazku, używając narzędzia <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [Dymek](TechDraw_Balloon/pl.md).

![](images/_Exercise_TechDraw_06.png )

1.  Patrząc na stronę w oknie [Widok 3D](3D_view/pl.md), wybierz widok, do którego zostanie dołączony dymek, jak pokazano na powyższym obrazku.
2.  Naciśnij przycisk dymka <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;">.
3.  Kursor jest teraz wyświetlany jako ikona dymka. Kliknij na stronie, aby umieścić początek dymka w żądanej pozycji.
4.  Pęcherzyk dymka może być przeciągnięty w żądane miejsce.
5.  Zmień właściwości dymka, klikając dwukrotnie etykietę dymka lub obiekt dymka w [widoku drzewa](Tree_view/pl.md). Spowoduje to otwarcie okna dialogowego **Zadanie dymka**. Ustaw pole **Wartość** na żądany tekst i zmień wybór z menu rozwijanego Symbol na **None**.
6.  Naciśnij przycisk **OK**
7.  Kontynuuj operację dla drugiego wywołania.

-   Wypełnimy teraz blok tytułowy arkusza.
    -   Upewnij się, że ramki, etykiety i wierzchołki Widoku są widoczne. Jeśli nie, kliknij na przycisk przełączania <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;">.
    -   Edytuj tekst w każdej części bloku tytułowego arkusza, klikając na mały zielony kwadrat po lewej stronie tekstu.

Nasza strona może być teraz eksportowana do formatu SVG w celu dalszej pracy w aplikacjach graficznych, takich jak [Inkscape](http://www.inkscape.org) lub DXF. W [widoku drzewa](tree_view/pl.md) wybierz stronę, a następnie opcję z menu **Plik → Eksport**. Format DXF jest importowalny w prawie wszystkich istniejących aplikacjach 2D CAD. Strony TechDraw mogą być również bezpośrednio drukowane lub eksportowane do formatu PDF.

**Do pobrania**

-   Plik utworzony podczas tego ćwiczenia: [1](https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.FCStd)
-   Arkusz SVG sporządzony z tego pliku: [2](https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.svg)

**Więcej informacji**

-   [Środowisko pracy Rysunek Techniczny](TechDraw_Workbench/pl.md)
-   [Tech Draw: Jak wykonać nowy szablon ramki](TechDraw_TemplateHowTo/pl.md)
-   [Poradnik: Podstawy dla środowiska pracy Rysunek Techniczny](Basic_TechDraw_Tutorial/pl.md)
-   [Biblioteki FreeCAD](https://github.com/FreeCAD/FreeCAD-library)
-   [Inkscape](http://www.inkscape.org)

**Obejrzyj poradniki**

-   [Lista odtwarzania Sliptonic dla TechDraw](https://www.youtube.com/watch?v=7LbOmSGW9F0&list=PLEuOia-QxyFKQnmM1U9yVo7eNrK_Mcln8)
-   [Symbole i widoki](https://www.youtube.com/watch?v=cggBR1Ghq7k)




[<img src="images/Property.png" style="width:16px"> Tutorials](Category_Tutorials.md)

---
[documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/pl
