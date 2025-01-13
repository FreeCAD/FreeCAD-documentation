# Manual:Preparing models for 3D printing/pl
{{Manual:TOC}}

Jednym z głównych celów programu FreeCAD jest projektowanie obiektów, które można przekształcić w rzeczywiste, fizyczne produkty. Te projekty mogą być udostępniane innym do produkcji lub, coraz częściej, eksportowane bezpośrednio do [drukarek 3D](https://pl.wikipedia.org/wiki/Druk_przestrzenny) lub do [obrabiarek CNC](https://pl.wikipedia.org/wiki/Obrabiarka_sterowana_numerycznie) w celu zautomatyzowanej produkcji. Dzięki programowi FreeCAD, możesz tworzyć precyzyjne, szczegółowe modele, które są gotowe do różnych metod produkcji. Ten rozdział przeprowadzi Cię przez proces przygotowywania modeli do tych obrabiarek, zapewniając, że spełniają one niezbędne specyfikacje do udanej produkcji, niezależnie od tego, czy pracujesz w zespole, czy zajmujesz się całym procesem samodzielnie.

Jeśli zachowałeś ostrożność podczas modelowania, większość wyzwań związanych z drukowaniem 3D twojego modelu powinna już zostać zminimalizowana. Kluczowe aspekty, na które warto zwrócić uwagę, to:

-   **Zapewnienie, że obiekty są bryłami**: Tak jak w przypadku rzeczywistych obiektów, twoje modele 3D muszą być bryłami. FreeCAD, szczególnie w środowisku pracy Projekt Części, pomaga zapewnić, że twoje modele pozostaną bryłami przez cały proces projektowania. Oprogramowanie powiadomi cię, jeśli jakakolwiek operacja zagrozi bryłowej naturze obiektu. Dodatkowo, środowisko pracy Część oferuje narzędzie <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Sprawdź geometrię](Part_CheckGeometry/pl.md), które pozwala zidentyfikować potencjalne wady lub problemy, które mogą zakłócać proces druku 3D.

-   **Potwierdzenie dokładności wymiarów**: Precyzja jest kluczowa - to, co zaprojektujesz we FreeCAD, będzie miało bezpośrednie odzwierciedlenie w rzeczywistych wymiarach. Milimetr we FreeCAD to milimetr w fizycznym obiekcie, dlatego każdy wymiar musi być starannie przemyślany i zweryfikowany, aby zapewnić dokładność.

-   **Zarządzanie degradacją**: Ważne jest, aby pamiętać, że żadna drukarka 3D ani frez CNC nie może bezpośrednio przetwarzać plików FreeCAD. Maszyny te używają G-Code, języka maszynowego z różnymi dialektami w zależności od maszyny lub producenta. Proces konwertowania modelu na G-Code można zwykle wykonać automatycznie za pomocą oprogramowania slicera, ale masz również możliwość zrobienia tego ręcznie, aby uzyskać większą kontrolę. Podczas tej konwersji nieunikniona jest pewna utrata szczegółów lub jakości, szczególnie podczas konwersji modelu do formatu siatki do druku. Musisz upewnić się, że ta degradacja pozostaje w akceptowalnych granicach i nie wpływa na funkcjonalność ani wygląd twojego końcowego obiektu.

-   **Kompatybilność formatu eksportu**: Dla druku 3D najczęściej używanym formatem jest STL, ale z natury konwertuje on model na siatkę trójkątów, co może prowadzić do utraty szczegółów. Ważne jest, aby wybrać odpowiednią rozdzielczość podczas eksportu do STL, balansując między zachowaniem szczegółów a rozmiarem pliku. Podobnie, w przypadku obróbki CNC, formaty takie jak STEP lub IGES są preferowane, ponieważ lepiej zachowują pierwotną integralność geometryczną projektu niż STL. Wybór odpowiedniego formatu zapewnia dokładność konwersji do G-Code.

-   **Analiza siatki i kalibracja**: Przed eksportem modelu do programu slicera lub generatora ścieżki narzędzia CNC, warto przeprowadzić analizę siatki za pomocą środowiska pracy [Siatka](Mesh_Workbench/pl.md) we FreeCAD, aby wykryć nieregularności, krawędzie nienałożone lub inne problemy z siatką, które mogą skomplikować proces produkcji. Dodatkowo, nawet przy idealnym modelu, upewnij się, że twoja drukarka 3D lub obrabiarka CNC jest odpowiednio skalibrowana (np. poziomowanie stołu, ustawienia silników krokowych lub konfiguracja ekstrudera), aby uniknąć problemów z jakością końcowego produktu.

W kolejnych sekcjach zakładać będziemy, że już zadbałeś o stworzenie modeli bryłowych o poprawnych wymiarach. Skupimy się teraz na zarządzaniu procesem konwersji do G-Code, zapewniając, że twój model zachowa niezbędną jakość do druku 3D lub obróbki CNC. Zajmując się tymi kwestiami, będziesz lepiej przygotowany do produkcji udanych obiektów fizycznych bezpośrednio z twoich modeli FreeCAD.



### Eksport do krajalnicy 

Najczęściej stosowaną techniką przygotowywania modelu 3D do druku jest eksportowanie obiektu 3D z FreeCAD do specjalistycznego oprogramowania nazywanego slicerem. Slicer generuje G-code, dzieląc model na cienkie warstwy, które drukarka 3D będzie śledzić, budując obiekt warstwa po warstwie. Ponieważ wiele drukarek 3D - szczególnie tych zbudowanych samodzielnie lub modeli hobbystycznych - ma unikalne konfiguracje, slicery oferują szeroki zakres zaawansowanych ustawień. Te ustawienia pozwalają dostosować kluczowe parametry, takie jak wysokość warstwy, prędkość druku, gęstość wypełnienia oraz struktury wsporcze, zapewniając, że G-code będzie dopasowany do specyficznych cech i możliwości twojej drukarki.

Wiele slicerów oferuje również funkcje symulacji i walidacji druku, które są niezwykle przydatne do podglądu procesu druku. Możesz wizualizować ścieżkę narzędzia dla każdej warstwy, co pomaga wykryć potencjalne problemy, takie jak wystające elementy, które mogą wymagać wsparcia, lub obszary, gdzie chłodzenie może być niewystarczające. Ta walidacja przed drukiem zapewnia, że twój model jest odpowiednio przygotowany przed rozpoczęciem druku, co pozwala uniknąć nieudanych wydruków lub zmarnowanego materiału.

Slicery często oferują dodatkowe informacje, takie jak szacowany czas druku, zużycie materiału i koszty w zależności od używanego filamentu lub żywicy. Pozwala to podejmować świadome decyzje dotyczące procesu druku i dostosowywać ustawienia w celu zwiększenia efektywności lub oszczędności materiału. Chociaż głębsze aspekty druku 3D, takie jak kalibracja maszyny, dobór materiału i postprocessing, wykraczają poza zakres tego przewodnika, skupimy się na tym, jak prawidłowo eksportować model z programu FreeCAD i używać oprogramowania slicer, aby upewnić się, że wynik jest poprawny i zoptymalizowany pod kątem twojej konkretnej drukarki.



### Konwersja obiektów do siatek 

Żaden z dostępnych obecnie slicerów nie może bezpośrednio obsługiwać geometrii bryłowej stworzonej w FreeCAD. Slicery takie jak Cura czy PrusaSlicer działają z formatami opartymi na [siatkach wielokątów](https://pl.wikipedia.org/wiki/Siatka_(grafika_3D)), takimi jak STL, OBJ lub 3MF, które przedstawiają geometrię obiektu za pomocą sieci trójkątów. W związku z tym, aby użyć modelu stworzonego we FreeCAD, musi on najpierw zostać przekonwertowany do formatu siatki, który slicery te potrafią zinterpretować.

Najczęściej używanym formatem do druku 3D jest STL. Jednym z powodów, dla których STL jest preferowany, jest jego prostota - reprezentuje geometrię 3D jako siatkę trójkątów, nie zawierając skomplikowanych szczegółów, takich jak kolory, materiały czy tekstury. To minimalistyczne podejście zapewnia, że pliki STL są lekkie i kompatybilne praktycznie ze wszystkimi slicerami i drukarkami 3D, co czyni go standardem branżowym. Choć formaty OBJ i 3MF są również obsługiwane, mogą zawierać dodatkowe informacje, takie jak tekstury i materiały, co jest niepotrzebne w większości zadań związanych z drukowaniem 3D i może skomplikować proces cięcia.

Na szczęście konwersja obiektu bryłowego na siatkę we FreeCAD jest prosta, choć konwersja siatki z powrotem na bryłę jest bardziej skomplikowaną operacją. Podczas procesu konwersji ważne jest, aby pamiętać, że może dojść do pewnej degradacji jakości modelu, szczególnie przy redukcji skomplikowanej geometrii do prostej siatki trójkątnej. Należy upewnić się, że ta degradacja mieści się w dopuszczalnych granicach, aby zachować dokładność wydrukowanego obiektu.

[Środowisko pracy Siatka](Mesh_Workbench/pl.md) we FreeCAD obsługuje wszystkie zadania związane z siatkami. To środowisko zawiera narzędzia nie tylko do konwersji między obiektami bryłowymi a siatkowymi, ale także do analizowania i naprawiania siatek. Choć manipulacja siatkami nie jest głównym celem FreeCAD, staje się kluczowa podczas przygotowywania modeli do druku 3D. Obiekty siatkowe są szeroko wykorzystywane w innych aplikacjach, a Środowisko Siatki umożliwia pełne zarządzanie i dostosowywanie tych obiektów, zapewniając, że są gotowe na kolejny krok w procesie druku.

-   Teraz skonwertujemy stworzony klocek Lego na siatkę STL. Geometrię można pobrać na końcu wspomnianego rozdziału.
-   Otwórz plik FreeCAD zawierający klocek Lego.
-   Przełącz się na [środowisko pracy Siatka](Mesh_Workbench/pl.md).
-   Wybierz klocek Lego.
-   Wybierz menu **Siatka → Utwórz siatkę z kształtu**.
-   Pojawi się panel z kilkoma opcjami. Niektóre dodatkowe algorytmy siatki (Mefisto lub Netgen) mogą być niedostępne, w zależności od tego, jak została skompilowana Twoja wersja FreeCAD. Algorytm siatki Standardowy będzie zawsze dostępny. Oferuje on mniej opcji niż dwa pozostałe, ale jest w pełni wystarczający dla małych obiektów, które mieszczą się w maksymalnym rozmiarze druku drukarki 3D.

![](images/FreeCAD_MeshLego.png )

-   Wybierz generator siatki **Standardowy**, i pozostaw wartość odchylenia na wartości domyślnej **0.10**. Naciśnij przycisk **Ok**.
-   Zostanie utworzony obiekt siatki, dokładnie na naszym obiekcie bryły. Albo ukryj bryłę, albo odsuń jeden z obiektów na bok, aby móc porównać oba.
-   Zmień właściwość **Widok → Tryb wyświetlania** nowego obiektu siatki na **Linie płaskie**, aby zobaczyć jak przebiegała triangulacja.
-   Jeśli nie jesteś zadowolony i uważasz, że wynik jest zbyt gruby, możesz powtórzyć operację, obniżając wartość odchylenia. W przykładzie poniżej, dla siatki lewej użyto domyślnej wartości **0.10**, natomiast dla prawej **0.01**:

![](images/Exercise_meshing_02.jpg )

Niemniej jednak w większości przypadków wartości domyślne dadzą zadowalający rezultat.

-   Możemy teraz wyeksportować naszą siatkę do formatu siatek, takiego jak [STL](https://en.wikipedia.org/wiki/STL_%28file_format%29), który jest obecnie najczęściej używanym formatem w druku 3D, poprzez użycie menu **Plik → Eksportuj** i wybranie formatu pliku STL.

Środowisko pracy Siatka we FreeCAD oferuje kilka algorytmów do konwersji modelu bryłowego na siatkę, w tym Standardowy, Mefisto, Netgen i Gmsh. Algorytm Standardowy jest powszechnie używany do małych i średniej wielkości obiektów, ponieważ zapewnia równowagę między szybkością a jakością siatki. Podczas tworzenia siatki, dwa kluczowe parametry to odchylenie powierzchniowe i odchylenie kątowe. Odchylenie powierzchniowe kontroluje, jak ściśle siatka odwzorowuje pierwotną geometrię, przy czym mniejsze wartości zapewniają dokładniejszą i drobniejszą siatkę, ale mogą prowadzić do większych rozmiarów pliku. Odchylenie kątowe określa, jak dużo odchylenia jest dozwolone na podstawie zmian w kątach modelu, szczególnie dla krzywizn i ostrych krawędzi. Inne opcje, takie jak względne odchylenie powierzchniowe, pozwalają dynamicznie dostosować precyzję w zależności od skali modelu, a takie funkcje jak stosowanie kolorów na powierzchniach lub definiowanie segmentów siatki według koloru są przydatne do zaawansowanego renderowania lub grupowania różnych regionów modelu. Po wygenerowaniu siatki, można ją eksportować w formatach takich jak STL, OBJ lub 3MF, które są niezbędne do przygotowania modeli do druku 3D. Jakość siatki jest kluczowa dla zapewnienia, że drukarki 3D poprawnie zinterpretują model, dlatego wybór odpowiedniego algorytmu siatki i ustawień odchylenia może znacząco wpłynąć na ostateczny wynik druku.



### Użycie PrusaSlicer 

[PrusaSlicer](https://github.com/prusa3d/prusaslicer/release) to aplikacja, która konwertuje obiekty STL, OBJ i 3MF na G-code, który może być wysłany bezpośrednio do drukarek 3D. Podobnie jak FreeCAD, jest to oprogramowanie wolne i open-source, dostępne na systemy Windows, Mac OS i Linux. Chociaż jest opracowany przez Prusa Research i zoptymalizowany pod kątem drukarek 3D Prusa, PrusaSlicer może być używany z niemal każdą drukarką 3D, co czyni go wszechstronnym narzędziem do różnych maszyn. PrusaSlicer opiera się na Slic3r, oryginalnym oprogramowaniu slicera, ale z licznymi ulepszeniami i częstszymi aktualizacjami. Slic3r nie jest już aktywnie rozwijany, podczas gdy PrusaSlicer wciąż ewoluuje, dodając nowe funkcje, takie jak adaptacyjne wysokości warstw, podpory typu drzewo i ulepszone strategie druku.

Poprawna konfiguracja slicera do druku 3D jest skomplikowanym procesem, który wymaga dobrej znajomości możliwości Twojej drukarki 3D. Generowanie G-code bez tej wiedzy może skutkować plikiem, który nie będzie dobrze działał na innych drukarkach, jednak PrusaSlicer nadal oferuje doskonały sposób, aby zweryfikować, czy plik STL jest poprawnie sformatowany i gotowy do druku. Funkcje symulacji slicera pozwalają na podgląd ścieżek G-code i sprawdzenie ewentualnych problemów z drukowaniem, zanim rozpoczniesz rzeczywisty proces druku. Pomaga to zapewnić, że wydruk przebiegnie sprawnie i zaoszczędzi materiał, identyfikując potencjalne problemy na wczesnym etapie.

To jest nasz wyeksportowany plik STL otwarty w PrusaSlicer. Po naciśnięciu przycisku **slice** oprogramowanie dzieli model na warstwy, generuje ścieżki narzędziowe dla drukarki 3D i stosuje odpowiednie ustawienia prędkości oraz temperatury. Oblicza wypełnienie, struktury wsporcze i obwody, a następnie tworzy G-code, który zawiera szczegółowe instrukcje dla drukarki. Możesz podglądać pokrojony model warstwa po warstwie, sprawdzić szacowany czas druku i zużycie filamentu, a następnie zapisać lub wysłać G-code do drukarki, aby rozpocząć rzeczywisty proces druku.

![](images/FreeCAD_PrusaSlicer.png )

Oprócz PrusaSlicer, istnieje kilka innych opcji oprogramowania slicera dostępnych do druku 3D. [Cura](https://ultimaker.com/fr/software/ultimaker-cura/) opracowana przez Ultimaker to jeden z najpopularniejszych slicerów open-source, który obsługuje szeroką gamę drukarek z rozbudowaną możliwością dostosowywania ustawień. [Simplify3D](https://www.simplify3d.com/) to płatny slicer, znany ze swoich zaawansowanych funkcji i efektywnego generowania ścieżek narzędziowych. [MatterControl](https://www.matterhackers.com/store/l/mattercontrol/sk/MKZGTDW6) to slicer open-source, który zawiera również podstawowe narzędzia CAD, podczas gdy [IdeaMaker](https://www.raise3d.com/fr/ideamaker/) oferuje przyjazny interfejs użytkownika z adaptacyjnymi wysokościami warstw, opracowany przez Raise3D. Wreszcie, [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer), nowsza opcja open-source oparta na PrusaSlicer i Bambu Studio, oferuje dodatkowe funkcje dla różnych drukarek. Każdy slicer ma swoje unikalne mocne strony, a najlepszy wybór zależy od specyficznych modeli drukarek i wymagań dotyczących druku.



### Generowanie G-code 

<img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [Środowisko pracy CAM](CAM_Workbench/pl.md) we FreeCAD oferuje zaawansowane opcje generowania G-code bezpośrednio dla maszyn CNC, zapewniając większą elastyczność i kontrolę w porównaniu do automatycznych narzędzi slicerów, takich jak te używane do druku 3D. Podczas gdy slicery do druku 3D mogą automatycznie konwertować model na G-code przy minimalnym udziale użytkownika, frezowanie CNC wymaga znacznie większego zaangażowania, aby zapewnić precyzyjną kontrolę nad ścieżkami narzędzi, prędkościami, głębokościami i innymi parametrami obróbczo-maszynowymi. Dzięki temu środowisko pracy CAM jest niezbędne do zadań, które wymagają precyzyjnego G-code, szczególnie w przypadku frezowania CNC, gdzie złożoność maszyn i różnorodność operacji (takich jak cięcie, wiercenie i konturowanie) wymagają starannego planowania.

Generowanie ścieżek G-code w środowisku pracy CAM jest w pełni konfigurowalne. Oferuje narzędzia do generowania kompletnych ścieżek narzędzi dla różnych operacji lub, alternatywnie, możesz tworzyć częściowe segmenty G-code i łączyć je w pełną operację frezowania. To modułowe podejście pozwala dostosować każdy etap procesu obróbki, optymalizując ścieżki narzędzi pod kątem efektywności, typu materiału oraz specyficznych możliwości maszyny.

Proces CAM jest rzeczywiście znacznie bardziej skomplikowany niż drukowanie 3D, ponieważ maszyny CNC używają różnych narzędzi i muszą uwzględniać usuwanie materiału, geometrię narzędzi oraz marginesy bezpieczeństwa, które są konfigurowane ręcznie. We FreeCAD, stworzenie prostego projektu CAM wymaga zdefiniowania ścieżek narzędzi, dostosowania głębokości cięcia, wyboru odpowiednich narzędzi oraz skonfigurowania offsetów roboczych, prędkości posuwu i prędkości obrotowej. W przeciwieństwie do oprogramowania slicera, które automatycznie obsługuje większość z tych ustawień, CAM Workbench daje pełną kontrolę w twoich rękach, co sprawia, że jest wysoce konfigurowalny, ale także bardziej skomplikowany.

Chociaż generowanie ścieżek frezowania CNC to temat zbyt szeroki, aby omówić go szczegółowo w tym miejscu, pokażemy, jak stworzyć prosty projekt CAM we FreeCAD. Chociaż nie będziemy koncentrować się na wszystkich szczegółach rzeczywistego obróbki CNC, ten przewodnik wprowadzi cię w kluczowe kroki, podkreślając poziom zaangażowania wymagany do zapewnienia dokładnych i wydajnych wyników. Ta dodatkowa złożoność jest niezbędna w projektach CNC, gdzie precyzja i możliwość dostosowywania są kluczowe dla uzyskania pożądanych rezultatów obróbki.

-   Załaduj plik zawierający naszą część Lego i przełącz się na <img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [Środowisko pracy CAM](CAM_Workbench/pl.md).
-   Kliknij przycisk <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Zadanie](CAM_Job/pl.md) i wybierz naszą część Lego.
-   Ponieważ ten rozdział nie ma na celu szczegółowego przedstawienia środowiska pracy CAM, będziemy korzystać z wartości domyślnych. Jeśli chcesz zapoznać się z bardziej szczegółowym samouczkiem, zajrzyj do [przewodnika po CAM](CAM_Walkthrough_for_the_Impatient/pl.md). Pamiętaj, że w środowisku pracy CAM automatycznie tworzony jest materiał magazynowy, który otacza twój obiekt, reprezentując surowiec, który będzie obrabiany. Obecnie ten materiał rozciąga się o 1 mm we wszystkich kierunkach od obiektu.

![](images/FreeCAD_CAM1.png )

-   Pierwszym krokiem jest usunięcie niepotrzebnego materiału wokół naszego obiektu. Na tym etapie zaczynamy od bryłowego bloku surowca, z którego musimy wyciąć klocek Lego. Proces ten polega na zdefiniowaniu ścieżek narzędzi, które stopniowo usuną nadmiar materiału, pozostawiając pożądany kształt klocka Lego.

-   Poniższy obrazek pokazuje konfigurację środowiska pracy CAM we FreeCAD dla obróbki klocka Lego. Drzewo modelu zawiera operacje modelowania, takie jak Wyciągnięcie, Kieszeń i Szyk liniowy, które zostały użyte do ukształtowania części. Tworzone jest Zadanie, zawierające ścieżki narzędzi w sekcji Operacje, które definiują sposób usuwania materiału z materiału magazynowego. Wybierane jest domyślne narzędzie do obróbki, a bryła modelu reprezentuje 3D część, nad którą pracujemy. Ta konfiguracja przygotowuje obiekt do generowania G-code, który kontroluje maszynę CNC.

![](images/FreeCAD_CAMtree.png )

-   Zanim zaczniemy usuwać nadmiar materiału, dokonajmy kilku poprawek w narzędziu, które będzie używane. Chociaż środowisko pracy CAM pozwala na definiowanie niestandardowych narzędzi, dla uproszczenia zmodyfikujemy narzędzie domyślne. Dzięki temu ustawienia będą zoptymalizowane pod nasz projekt, bez konieczności tworzenia nowego narzędzia od podstaw.

-   Kliknij na tekst **TC:Default Tool**. Otworzy to **Edytor Sterownika Narzędzia**. Zmień prędkości posuwu i obroty wrzeciona zgodnie z obrazkiem. Prędkości posuwu dla cięcia poziomego i pionowego ustawione są na 2000 mm/min, a prędkość wrzeciona wynosi 2000 RPM z obrotem w kierunku zgodnym z ruchem wskazówek zegara. Te ustawienia kontrolują ruch i prędkość cięcia narzędzia podczas procesu obróbki.

![](images/FreeCAD_toolController.png )

-   Kliknij dwukrotnie na narzędziu i zmień jego średnicę na 1 mm.
-   Teraz jesteśmy gotowi, aby rozpocząć usuwanie nadmiaru materiału z bloku, stopniowo wycinając geometrię Lego. Proces ten obejmuje ścieżki narzędziowe, które ustawiliśmy, aby zapewnić, że końcowy kształt będzie odpowiadał zamierzonemu projektowi.
-   Kliknij na <img alt="" src=images/CAM_Profile.svg  style="width:16px;"> [Profilowanie](CAM_Profile/pl.md). Ta opcja służy do wycięcia nadmiaru materiału wokół obwodu części, skutecznie formując zewnętrzne granice, aby uzyskać ogólne wymiary elementu Lego.
-   Zwykle nie będziesz musiał zmieniać żadnych domyślnych wartości, z wyjątkiem opcji **Dodatkowe odsunięcie** znajdującej się w zakładce Operacja. Ustaw tę opcję na 1 mm, aby zapewnić, że pozostała część będzie zgodna z granicami klocka Lego.
-   Po naciśnięciu **Zastosuj** powinieneś zobaczyć zielone linie wokół obiektu. Te linie wizualizują ścieżkę, którą narzędzie skrawające podąży podczas cięcia początkowego bloku.

![](images/FreeCAD_CAMProfile.png )

-   Naszym kolejnym krokiem jest stworzenie 6 walców na górze klocka Lego.
-   Wybierz górną powierzchnię i wciśnij przycisk <img alt="" src=images/CAM_Pocket_Shape.svg  style="width:16px;"> [Obróbka kieszeni](CAM_Pocket_Shape/pl.md). W zakładce **Rozszerzenia** włącz opcję Rozszerzenia i kliknij na krawędź górnej powierzchni (powinna być automatycznie dodana do domyślnego pola długości).
-   W zakładce **Operacja** wprowadź -1,5 mm w polu **Rozszerzenie przejścia** i zmień opcję wzorca na ZigZagOffset.
-   Naciśnij **Zastosuj**, a następnie zamknij zakładkę.
-   W podobny sposób możemy stworzyć trzy walce na spodzie klocka Lego.
-   Łatwo możemy zwizualizować kroki wykonane podczas frezowania obiektu, korzystając z opcji <img alt="" src=images/CAM_SimulatorGL.svg  style="width:16px;"> [Symulator](CAM_SimulatorGL/pl.md).

**Do pobrania**

-   Plik STL generowany w tym ćwiczeniu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   Plik generowany podczas tego ćwiczenia: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   Plik G-code generowany w tym ćwiczeniu: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Więcej informacji:**

-   Środowisko pracy [Siatka](Mesh_Workbench/pl.md)
-   [format plików STL](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   Środowisko pracy [Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   Środowisko pracy [CAM](CAM_Workbench/pl.md)
-   [Camotics](http://camotics.org/)



### Filmy

-   [How To Use FreeCAD For 3D Printing - Używanie gałęzi Realthunder](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) Lista odtwarzania wideo przygotowana przez Maker Tales o tym jak używać programu FreeCAD do druku 3D.



---
⏵ [documentation index](../README.md) > [CAM](Category_CAM.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/pl
