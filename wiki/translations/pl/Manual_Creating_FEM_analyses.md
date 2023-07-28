# Manual:Creating FEM analyses/pl
{{Manual:TOC/pl}}

MES to skrót od [Metoda Elementów Skończonych](https://en.wikipedia.org/wiki/Finite_element_method). Jest to rozległy temat matematyczny, ale w FreeCAD możemy myśleć o nim jako o sposobie obliczania rozchodzenia się energii wewnątrz obiektu 3D, poprzez pocięcie go na małe kawałki i przeanalizowanie wpływu każdego małego kawałka na jego sąsiadów. Ma to wiele zastosowań w inżynierii i elektromagnetyzmie, ale my skupimy się na jednym z zastosowań, które jest już dobrze rozwinięte w programie FreeCAD, a mianowicie na symulacji deformacji obiektów poddawanych działaniu sił i ciężarów.

Uzyskanie takiej symulacji odbywa się w programie FreeCAD za pomocą środowiska [MES](FEM_Workbench/pl.md). Składa się na to kilka kroków: Przygotowanie geometrii, ustawienie jej materiału, wykonanie siatki, podział na mniejsze części, tak jak to robiliśmy w rozdziale [Przygotowanie obiektów do druku 3D](Manual:Preparing_models_for_3D_printing/pl.md), a na koniec obliczenie symulacji.

<img alt="" src=images/Exercise_fem_01.jpg  style="width:600px;">



### Przygotowanie programu FreeCAD 

Sama symulacja jest wykonywana przez inny program, który jest wykorzystywany przez FreeCAD do uzyskania wyników. Ponieważ jest dostępnych kilka interesujących aplikacji do symulacji MES o otwartym kodzie źródłowym, środowisko pracy [MES](FEM_Workbench/pl.md) pozwala na wybór pomiędzy nimi. Jednak obecnie tylko [CalculiX](http://www.calculix.de/) jest w pełni zaimplementowany. Wymagany jest również inny program, o nazwie [NetGen](https://sourceforge.net/projects/netgen-mesher/), który odpowiada za generowanie siatki podziału. Szczegółowe instrukcje dotyczące instalacji tych dwóch komponentów znajdują się [w dokumentacji FreeCAD](FEM_Install/pl.md).



### Przygotowanie geometrii 

Zaczniemy od domu, który wymodelowaliśmy w rozdziale [Modelowanie BIM](Manual:BIM_modeling/pl.md). Należy jednak dokonać pewnych zmian, aby model nadawał się do obliczeń metodą MES. Polega to w zasadzie na odrzuceniu obiektów, których nie chcemy uwzględniać w obliczeniach, takich jak drzwi i okna, oraz połączeniu wszystkich pozostałych obiektów w jeden.

-   Wczytaj [model domu](https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd), który wcześniej wymodelowaliśmy
-   Usuń lub ukryj obiekt strony, płaszczyzny przekroju i wymiary, pozostawiając tylko nasz model.
-   Ukryj okno, drzwi i płytę fundamentową
-   Ukryj również metalowe belki na dachu. Są to zupełnie inne obiekty niż reszta domu, więc uprościmy nasze obliczenia nie uwzględniając ich. Zamiast tego przyjmiemy, że płyta dachowa jest umieszczona bezpośrednio na ścianie.
-   Przesuń teraz płytę dachową w dół, tak aby spoczywała na ścianie: Edytuj obiekt **Prostokąt**, którego użyliśmy jako podstawy płyty dachowej, i zmień jego wartość **Umiejscowienie-\>Pozycja-\>X** z 3.18m na 3.00m
-   Nasz model jest teraz przejrzysty:

<img alt="" src=images/Exercise_fem_02.jpg  style="width:600px;">

-   Środowisko pracy MES może obecnie obliczać deformacje tylko jednego obiektu. Dlatego musimy połączyć nasze dwa obiekty *(ścianę i płytę)*. Przejdź do środowiska pracy [Część](Part_Workbench/pl.md), wybierz dwa obiekty i naciśnij przycisk **<img src="images/Part_Fuse.svg" width=16px> [Scalenie](Part_Fuse/pl.md)**. Otrzymaliśmy teraz połączony obiekt:

<img alt="" src=images/Exercise_fem_03.jpg  style="width:600px;">



### Tworzenie analizy 

-   Jesteśmy teraz gotowi do rozpoczęcia analizy MES. Przejdźmy do środowiska pracy [MES](FEM_Workbench/pl.md).
-   Wybierzmy obiekt o nazwie *scalony*.
-   Naciśnij przycisk **<img src="images/FEM_Analysis.svg" width=16px> [Nowa analiza](FEM_Analysis/pl.md)**.
-   Zostanie utworzona nowa analiza i otwarty panel ustawień. Tutaj można zdefiniować parametry siatki, które będą używane do produkcji siatki MES. Główną nastawą do edycji jest wartość **Maksymalny Rozmiar**, która definiuje maksymalny rozmiar *(w milimetrach)* każdego fragmentu siatki. Na razie możemy pozostawić domyślną wartość 1000:

<img alt="" src=images/Exercise_fem_04.jpg  style="width:600px;">

-   Po naciśnięciu przycisku **OK** i kilku sekundach obliczeń, nasza siatka MES jest gotowa:

<img alt="" src=images/Exercise_fem_05.jpg  style="width:600px;">

-   Możemy teraz zdefiniować materiał, który ma być zastosowany do naszej siatki. Jest to ważne, ponieważ w zależności od wytrzymałości materiału, nasz obiekt będzie różnie reagował na przyłożone do niego siły. Zaznacz obiekt analizy i naciśnij przycisk **<img src="images/FEM_MaterialSolid.svg" width=16px> [Nowy Materiał](FEM_MaterialSolid/pl.md)**.
-   Otworzy się panel zadań umożliwiający nam wybór materiału. Z listy rozwijanej Materiał wybieramy materiał **Beton-ogólnie** i wciskamy **OK**.

<img alt="" src=images/Exercise_fem_06.jpg  style="width:600px;">

-   Teraz jesteśmy gotowi do zastosowania sił. Zacznijmy od określenia, które ściany są przymocowane do podłoża i dlatego nie mogą się poruszać. Naciśnij przycisk **<img src="images/FEM_ConstraintFixed.svg" width=16px> [Wiązanie stałej geometrii](FEM_ConstraintFixed/pl.md)**.
-   Kliknij na dolną powierzchnię naszego budynku i naciśnij przycisk **OK**. Spód budynku jest oznaczony jako nieruchomy:

<img alt="" src=images/Exercise_fem_07.jpg  style="width:600px;">

-   Dodamy teraz obciążenie na górnej powierzchni, które może reprezentować, na przykład, ogromny ciężar umieszczony na dachu. W tym celu użyjemy wiązania nacisku. Naciśnij przycisk **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Wiązanie nacisku](FEM_ConstraintPressure/pl.md)**.
-   Kliknij górną powierzchnię dachu, ustaw wartość nacisku na **10MPa** *(nacisk jest wywierany na milimetr kwadratowy)* i kliknij przycisk **OK**. Nasza siła jest teraz przyłożona:

<img alt="" src=images/Exercise_fem_08.jpg  style="width:600px;">

-   Teraz jesteśmy gotowi do rozpoczęcia obliczeń. Zaznaczamy obiekt **CalculiX** w widoku drzewa i naciskamy przycisk **<img src="images/FEM_SolverControl.svg" width=16px> [Uruchom obliczenia](FEM_SolverControl/pl.md)**.
-   W panelu zadań, który się otworzy, kliknij najpierw przycisk **Zapisz plik .inp**, aby utworzyć plik wejściowy dla CalculiX, a następnie przycisk **Uruchom CalculiX**. Kilka chwil później obliczenia zostaną wykonane:

<img alt="" src=images/Exercise_fem_09.jpg  style="width:600px;">

-   Teraz możemy przyjrzeć się wynikom. Zamknij panel zadań i zobacz, że do naszej analizy został dodany nowy obiekt o nazwie **Wyniki**.
-   Kliknij dwukrotnie na obiekt *Wyniki*
-   Ustaw typ wyniku, który chcesz zobaczyć na siatce, na przykład \"przemieszczenie bezwzględne\", zaznacz pole wyboru **pokaż** w **Przemieszczenie** i przesuń suwak obok niego. Będziesz mógł zobaczyć jak deformacja rośnie wraz z przyłożeniem większej siły:

<img alt="" src=images/Exercise_fem_10.jpg  style="width:600px;">

Wyniki wyświetlane za pomocą programu MES nie są oczywiście obecnie wystarczające do podejmowania rzeczywistych decyzji dotyczących wymiarowania konstrukcji i materiałów. Mogą one jednak dostarczyć cennych informacji o tym, jak siły przepływają przez konstrukcję i które słabe obszary będą odczuwać największe naprężenia.

**Do pobrania**

-   Plik utworzony podczas tego ćwiczenia: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/fem.FCStd>

**Więcej informacji**

-   [Środowisko pracy MES](FEM_Workbench/pl.md)
-   [Instalacja środowiska MES](FEM_Install/pl.md)
-   [CalculiX](http://www.calculix.de)
-   [NetGen](https://sourceforge.net/projects/netgen-mesher)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Creating FEM analyses/pl
