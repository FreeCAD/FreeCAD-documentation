# Manual:Creating FEM analyses/pl
{{Manual:TOC}}

[Metoda elementów skończonych](https://pl.wikipedia.org/wiki/Metoda_element%C3%B3w_sko%C5%84czonych) (MES) to potężna technika obliczeniowa stosowana do rozwiązywania złożonych problemów inżynieryjnych, fizycznych i matematycznych. Polega na rozbiciu dużego, skomplikowanego obiektu lub konstrukcji na mniejsze, prostsze części zwane elementami skończonymi. Te elementy są analizowane indywidualnie, a ich zachowanie jest łączone, aby przewidzieć, jak cała struktura zareaguje na wpływy zewnętrzne, takie jak siły, ciepło czy drgania.

MES jest szeroko stosowany w takich dziedzinach jak inżynieria budowlana, projektowanie mechaniczne, aerodynamika i elektromagnetyzm, aby symulować, jak obiekty odkształcają się pod wpływem naprężeń, jak ciepło przepływa przez materiały oraz jak pola elektromagnetyczne oddziałują z różnymi obiektami. Dzięki dostarczaniu szczegółowych informacji na temat tych interakcji, MES pozwala inżynierom i projektantom optymalizować produkty pod kątem wydajności, bezpieczeństwa i efektywności, eliminując potrzebę tworzenia fizycznych prototypów.

Uzyskiwanie takich symulacji w FreeCAD odbywa się za pomocą środowiska pracy <img alt="" src=images/Workbench_FEM.svg  style="width:16px;"> [MES](FEM_Workbench/pl.md), które zostało zaprojektowane specjalnie do przeprowadzania analiz metodą elementów skończonych (FEA). Oferuje ono kompleksowy zestaw narzędzi do przygotowania modelu, przypisywania właściwości materiałów, generowania siatki oraz przeprowadzania symulacji. Środowisko pracy MES jest wszechstronne, wspierając szeroki zakres symulacji, takich jak analizy strukturalne, termiczne i dynamiczne, z dostępnymi solverami, takimi jak [CalculiX](https://www.calculix.de/) i innymi.

To środowisko pracy umożliwia integrację z innymi środowiskami pracy FreeCAD, co pozwala na bezproblemowe przygotowanie modelu i przeprowadzenie analizy. Oferuje także potężne narzędzia do postprocessingu, umożliwiające wizualizację i interpretację wyników symulacji, takich jak naprężenia, odkształcenia i rozkłady temperatury. Praca w module MES obejmuje następujące kroki:

-   **Przygotowanie geometrii**: Model musi być uproszczony lub zoptymalizowany do analizy MES. Często obejmuje to usuwanie niepotrzebnych detali lub funkcji, które nie przyczyniają się do symulacji, ale mogą sprawić, że obliczenia staną się kosztowne obliczeniowo. Do przygotowania geometrii 3D można używać narzędzi z innych środowisk pracy, takich jak <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Projekt Części](PartDesign_Workbench/pl.md) lub <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md).

-   **Przypisywanie właściwości materiałów**: Definicje materiałów są kluczowe dla dokładnych symulacji. Właściwości takie jak moduł Younga, współczynnik Poissona i gęstość są przypisywane do analiz strukturalnych, natomiast przewodność cieplna i pojemność cieplna specyficzna do analiz termicznych. Materiały można wybrać z biblioteki materiałów FreeCAD lub dostosować według potrzeb.

-   **Generowanie siatki**: Siatka dzieli geometrię na elementy skończone, umożliwiając solverowi przeprowadzenie analizy obiektu. Jakość siatki jest kluczowa, ponieważ drobniejsze siatki prowadzą do dokładniejszych symulacji, ale wymagają większej mocy obliczeniowej. Dostępne są narzędzia do lokalnego ulepszania siatki, koncentrując się na obszarach, w których oczekuje się wyższych naprężeń lub odkształceń.

-   **Zadanie obciążeń i wiązań**: W tym kroku zadaje się na model warunki fizyczne, takie jak siły, ciśnienia, momenty lub obciążenia termiczne. Określane są także warunki brzegowe, takie jak utwierdzenie punktów, stosowanie warunków symetrii lub ograniczanie ruchu, w zależności od scenariusza, który jest symulowany.

-   **Uruchamianie solvera**: Po zakończeniu konfiguracji, solver oblicza reakcję modelu na zastosowane warunki. Solvery takie jak CalculiX obliczają przemieszczenia, naprężenia i inne wielkości, w zależności od rodzaju przeprowadzanej analizy. Proces ten może zająć różną ilość czasu, w zależności od gęstości siatki i złożoności modelu.

-   **Postprocessing (obróbka wyników)**: Po symulacji wyniki są wizualizowane za pomocą narzędzi w środowisku pracy MES. Pola naprężeń, odkształceń i przemieszczeń są przedstawiane jako mapy kolorów i można wygenerować wykresy deformacji. Te wizualizacje pozwalają na dokładną analizę pracy modelu, uwypuklając obszary o wysokich naprężeniach lub odkształceniach.

<img alt="" src=images/FreeCAD_FEMBeam.png  style="width:600px;">



### Przygotowanie programu FreeCAD 

W tej sekcji zaprezentujemy ogólną procedurę analizy MES na prostym przykładzie. Chociaż temat MES jest bardzo szeroki, skupimy się na prostej geometrii: belce wspornikowej. Naszym celem jest określenie maksymalnego przemieszczenia pionowego tej belki pod wpływem zastosowanego obciążenia, a następnie porównanie wyników numerycznych z rozwiązaniem analitycznym. W mechanice komputerowej weryfikacja wyników numerycznych w porównaniu do danych eksperymentalnych lub rozwiązań analitycznych jest kluczowa, aby zapewnić dokładność i wiarygodność symulacji. Dodatkowo będziemy korzystać z pakietów, które są już dołączone do instalacji FreeCAD, więc nie będą wymagane żadne dodatkowe instalacje do przeprowadzenia tej analizy.



### Przygotowanie geometrii 

Na początek stworzymy naszą prostą geometrię. W tym celu będziemy korzystać ze środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Projekt Części](PartDesign_Workbench/pl.md).

-   Utwórz nowy dokument i przejdź do środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [Projekt Części](PartDesign_Workbench/pl.md).
-   Kliknij <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Nowy szkic](Sketcher_NewSketch/pl.md), aby stworzyć nowy szkic na płaszczyźnie YZ.
-   Utwórz <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:16px;"> [prostokąt ze środka](Sketcher_CreateRectangle_Center/pl.md) wokół punktu początkowego.
    -   Używając <img alt="" src=images/Sketcher_Dimension.svg  style="width:16px;"> [wymiarowania szkicu](Sketcher_Dimension/pl.md), ustaw wymiar pionowy na **20 mm** oraz poziomy na **10 mm**.
-   Wyjdź z trybu szkicowania.
-   Mając wybrany nasz nowo stworzony szkic, zastosuj operację <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [wyciągnięcia](PartDesign_Pad/pl.md) o długości **1000 mm**.
-   Nasza geometria jest teraz gotowa. W tym przykładzie zrobiliśmy wysokość (h) i szerokość (b) belki znacznie mniejsze od długości (L), aby skupić się na tym, jak się ona wygina. Dzięki temu możemy upewnić się, że belka zachowuje się jak typowy długi, cienki obiekt, w którym gięcie jest głównym efektem, gdy zastosujemy siłę. Takie ustawienie ułatwia także porównanie wyników z prostymi wzorami, które możemy obliczyć ręcznie.

<img alt="" src=images/FreeCAD_FEM_BeamGeometry.png  style="width:600px;">



### Tworzenie analizy 

-   Jesteśmy teraz gotowi, aby rozpocząć analizę MES. Przełączmy się na środowisko pracy <img alt="" src=images/Workbench_FEM.svg  style="width:16px;"> [MES](FEM_Workbench/pl.md).
-   Kliknij <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [Nowa analiza](FEM_Analysis/pl.md).
-   Zostanie utworzona nowa analiza, a panel ustawień zostanie otwarty. Przycisk **Utwórz analizę** przygotowuje fundamenty do przeprowadzenia analizy metodą elementów skończonych. Tworzy kontener analizy, który organizuje kluczowe elementy, takie jak siatka, właściwości materiałowe, ograniczenia (np. punkty ustalone), zastosowane obciążenia i solver. Ten przycisk zasadniczo przygotowuje wszystko, co jest potrzebne do symulacji, umożliwiając dalsze kroki, takie jak tworzenie siatki i uruchamianie solvera w celu analizy zachowania obiektu w określonych warunkach.

-   Zaczniemy od stworzenia **Siatki**. W tym celu, mając wybrany nasz obiekt, wciśnij przycisk <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:16px;"> [Siatka MES z kształtu przy pomocy generatora Netgen](FEM_MeshNetgenFromShape/pl.md). Opcja ta korzysta z generatora Netgen, narzędzia open-source do tworzenia wysokiej jakości siatek czworościennych, szczególnie odpowiednich do skomplikowanych geometrii w analizie elementów skończonych.
-   W oknie parametrów generatora siatki pozostaniemy przy prostych ustawieniach i zmienimy tylko maksymalny rozmiar komórki. Opcja **Max Size** definiuje największy dopuszczalny rozmiar pojedynczych elementów siatki. Określa ona, jak gruba lub drobna będzie siatka. Większy rozmiar Max Size skutkuje grubsza siatką z mniejszą liczbą elementów, co może przyspieszyć obliczenia, ale może również zmniejszyć dokładność. Mniejszy rozmiar Max Size tworzy drobniejszą siatkę z większą liczbą elementów, zwiększając dokładność, ale również wymagając większych zasobów obliczeniowych. Ustaw tę wartość na **10** i kliknij **Zastosuj**.

<img alt="" src=images/FreeCAD_FEM_MesherParameters.png  style="width:600px;">

-   Nasza siatka jest gotowa.

<img alt="" src=images/FreeCAD_FEM_Mesh.png  style="width:600px;">

-   Teraz możemy zdefiniować materiał, który zostanie zastosowany do naszej siatki klikając opcję <img alt="" src=images/FEM_MaterialSolid.svg  style="width:16px;"> [Nowy materiał](FEM_MaterialSolid/pl.md). Wybór materiału jest kluczowy w każdej analizie, ponieważ różne materiały o różnych właściwościach będą zachowywać się inaczej w tych samych warunkach. Czynniki takie jak wytrzymałość, elastyczność i gęstość odgrywają istotną rolę w tym, jak materiał reaguje na siły, ciśnienia lub temperatury. Wybór odpowiedniego materiału zapewnia dokładne wyniki symulacji, odzwierciedlające, jak obiekt zachowywałby się w rzeczywistych warunkach.
-   Otworzy się panel z zadaniami, który umożliwi nam wybór materiału. Z listy rozwijanej Materiał wybierz materiał **Steel-1C22** i kliknij **OK**.

<img alt="" src=images/FreeCAD_FEM_material.png  style="width:600px;">

-   Ostatnim krokiem jest zastosowanie sił i wiązań, które przekształcają warunki fizyczne na potrzeby analizy FEM. W tym prostym przypadku mamy belkę, która jest zamocowana z jednej strony (co reprezentuje przymocowanie do ściany), podczas gdy druga strona jest swobodna do ruchu. Rozłożona siła jest przykładana wzdłuż całej długości belki, symulując obciążenie, które doświadcza w warunkach rzeczywistych. Zaczniemy od określenia powierzchni zamocowanej do ściany, która nie może się poruszać. Kliknij przycisk <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:16px;"> [Warunek brzegowy utwierdzenia](FEM_ConstraintFixed/pl.md).
-   Naciśnij przycisk **dodaj** i wybierz lewą ścianę naszej belki (tę na początku). Kliknij **Zastosuj**. Ta powierzchnia została teraz oznaczona jako nieruchoma.

<img alt="" src=images/FreeCAD_FEM_Beam_FC.png  style="width:600px;">

-   Teraz dodamy obciążenie rozłożone na górnej powierzchni, które może na przykład reprezentować ciężki ładunek umieszczony na belce. Aby to zrobić, kliknij opcję <img alt="" src=images/FEM_ConstraintForce.svg  style="width:16px;"> [Obciążenie siłą](FEM_ConstraintForce/pl.md).
-   Kliknij górną powierzchnię belki, ustaw siłę na **1000 N** i wybierz opcję **odwróć kierunek**. Następnie kliknij **OK**. Nasza siła została teraz zastosowana.

<img alt="" src=images/_FreeCAD_FEM_Beam_force.png  style="width:600px;">

-   Teraz jesteśmy gotowi do rozpoczęcia obliczeń. Wybierz <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> [solver CalculiX](FEM_SolverCalculixCxxtools/pl.md).
-   Wybierz analizę **Statyczną** i kliknij przycisk **Zapisz plik .inp**, aby utworzyć plik wejściowy dla CalculiX. Następnie kliknij przycisk **Uruchom CalculiX**. Symulacja rozpocznie się teraz.

<img alt="" src=images/FreeCAD_FEM_Calculix.png  style="width:600px;">

-   Teraz możemy zobaczyć wyniki. Kliknij opcję <img alt="" src=images/FEM_ResultShow.svg  style="width:16px;"> [Pokaż wyniki](FEM_ResultShow/pl.md).
-   Zaznacz opcję **Przemieszczenie Z**, które odpowiada za współrzędną pionową w naszym przypadku.
-   Zobaczysz minimalne i maksymalne wartości dla przemieszczenia pionowego. Na podstawie analizy maksymalne przemieszczenie pionowe wynosi **-356,30 mm**. To dobrze odpowiada naszej wyznaczonej analitycznie wartości **-357,14 mm**.
-   Możesz przesunąć suwak obok. Będziesz w stanie zobaczyć jak odkształcenie rośnie w miarę stosowania większej siły.

<img alt="" src=images/FreeCAD_FEM_Results.png  style="width:600px;">

Wyniki wyświetlane za pomocą programu MES nie są oczywiście obecnie wystarczające do podejmowania rzeczywistych decyzji dotyczących wymiarowania konstrukcji i materiałów. Mogą one jednak dostarczyć cennych informacji o tym, jak siły przepływają przez konstrukcję i które słabe obszary będą odczuwać największe naprężenia.

**Więcej informacji:**

-   [Środowisko pracy MES](FEM_Workbench/pl.md)
-   [Instalacja środowiska MES](FEM_Install/pl.md)
-   [CalculiX](http://www.calculix.de)
-   [NetGen](https://sourceforge.net/projects/netgen-mesher)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Creating FEM analyses/pl
