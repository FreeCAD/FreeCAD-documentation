---
 TutorialInfo:l
   Topic:  Analiza metodą elementów skończonych
   Level:  Początkujący/średnio zaawansowany
   Time:  30 minut
   Author: http://www.freecadweb.org/wiki/index.php?title=User: HarryvL
   FCVersion: 0.17.12960 lub nowszy
---

# FEM Shear of a Composite Block/pl







## Wprowadzenie

W tym przykładzie przeanalizujemy deformację postaciową kompozytowego bloku składającego się ze sztywnego rdzenia osadzonego w miękkiej matrycy. Zademonstrowane będzie użycie narzędzi BooleanFragments i CompoundFilter do utworzenia brył dla bloku i matrycy z dwóch współśrodkowych sześcianów. To podejście zapewnia możliwość przypisania obszarów siatki, materiałów i warunków brzegowych osobno dla bloku i otaczającej go matrycy. Do wybrania wewnętrznych obszarów wykorzystamy makrodefinicję autorstwa Markusa Hovorki *(https://github.com/drhooves/SelectionTools)* lub alternatywne podejście. Wyniki z solvera CalculiX wyraźnie pokazują wpływ sztywnego rdzenia na odpowiedź bloku kompozytowego.



## Geometria

Najpierw utworzymy dwie współśrodkowe kostki, jedną o rozmiarze 10mm a drugą o rozmiarze 5mm. Robimy to w środowisku pracy [Część](Part_Module/pl.md). Domyślnie sześcian jest umieszczony w środku układu współrzędnych \[0,0,0\]. więc mniejszy sześcian należy przeskalować i przesunąć poprzez zmianę ustawień w zakładce Dane panelu właściwości. Aby uczynić rdzeń widocznym, przezroczystość zewnętrznego bloku jest ustawiana na 50 w zakładce Widok panelu właściwości. Wynik jest pokazany poniżej.

<img alt="" src=images/Pic1.png  style="width:700px;">

Następnie zaznaczmy dwa bloki w drzewie i utwórzmy obiekt BooleanFragments *(**Część → Rozdziel → Fragmentacja funkcją logiczną**)*. W zakładce Dane panuelu właściwości zmień tryb na BryłaZłożona *(CompSolid)*. Teraz zaznacz obiekt BooleanFragments w drzewie modelu i utwórz Filtr złożeń *(**Część → Złożenie → Filtr złożeń**)*.

<img alt="" src=images/Pic2.png  style="width:700px;">



## Siatka i obszary siatki 

W środowisku pracy MES tworzymy kontener Analiza. Będzie on zawierał wszystkie definicje wymagane do analizy w solverze CalculiX i jej wyniki. Zauważ, że ten kontener Analiza musi być aktywowany *(kliknij prawym przyciskiem myszy i wybierz \"Aktywuj analizę\")* przy każdym ponownym wczytaniu pliku lub po przełączeniu się z innej analizy. Aby rozpocząć proces generowania siatki, zaznacz obiekt CompoundFilter w drzewie modelu i aktywuj okno dialogowe **Siatka → Siatka MES z kształtu przy pomocy generatora Gmsh**. Opuść okno dialogowe klikając OK.

Obiekt siatki jest tworzony w drzewie modelu. Zaznacz go i utwórz Obszar siatki poprzez **Siatka → Obszar siatki MES**. Otwórz okno dialogowe dla tego obszaru siatki klikając na nim dwukrotnie i zaznacz przycisk dla Solid. Następnie wciśnij przycisk \"Dodaj odniesienie\" i wybierz obiekt CompoundFilter w oknie graficznym. Powinno to dodać odniesienie do \"CompoundFilter:Solid1\" na liście obiektów obszaru siatki. Wreszcie, podaj maksymalny rozmiar elementów dla tego obszaru (tutaj 5mm). Opuść okno dialogowe klikając OK.

<img alt="" src=images/Pic3.png  style="width:700px;">

Następnie utwórz nowy obiekt siatki jak powyżej i użyj makra do wskazywania *(skrót S, E)* aby wybrać obiekt Cube_Core w oknie graficznym. Tym razem lista odniesień powinna pokazać \"CompoundFilter:Solid2\", jak poniżej. Alternatywnie można ukryć obiekt Compound i pokazać obiekt Cube_Core *(rozwijając Compound w drzewie, wybierając każdy z nich i naciskając spację)*. Wybieramy maksymalny rozmiar elementów 1mm.

Uwaga1: Wybór obiektu \"CompoundFilter:Solid2\" wymaga wskazania jednej z jego ścian.

Uwaga2: Jeśli masz problem z wyborem obiektu \"CompoundFilter:Solid2\", może to wynikać z pominięcia ustawienia trybu BryłaZłożona (CompSolid) w obiekcie BooleanFragments.

<img alt="" src=images/Pic4.png  style="width:700px;">



## Przypisanie materiału 

Materiał jest przypisywany do obszaru siatki poprzez obiekt SolidMaterial. W tym przykładzie przypisujemy dwa materiały, jeden dla matrycy i jeden dla rdzenia.

Zacznij od zaznaczenia obiektu CompoundFilter w drzewie modelu. Następnie utwórz obiekt SolidMaterial poprzez opcję **Model → Materiał MES dla bryły**. Otwórz okno dialogowe i zaznacz przycisk dla Solid, wciśnij \"Dodaj odniesienie\" i wybierz obiekt CompoundFilter z okna graficznego. Lista odniesień powinna teraz pokazywać \"CompoundFilter:Solid1\", jak poprzednio. Przypisujemy materiał ABS do matrycy, z modułem Younga około 1% wartości dla stali.

<img alt="" src=images/Pic5.png  style="width:700px;">

Potwórz powyższą procedurę dla rdzenia *(\"CompoundFilter:Solid2\")* z pomocą makra do zaznaczania lub alternatywnego podejścia, opisanego wcześniej. Tym razem przypisujemy materiał CalculiX-Steel, który jest znacznie sztywniejszy od materiału ABS matrycy.



## Podpora przesuwna 

Aby uzyskać stan prostego ścinania dla bloku kompozytowego, należy pozostawić nie zablokowane deformacje na brzegach. Żeby to uzyskać, blok jest umieszczany na podporze przesuwnej. Pozostawia to trzy stopnie swobody w płaszczyźnie podpory (2 translacje i 1 obrót) i te stopnie swobody będą związane później. *(Uwaga: ponieważ płaszczyzna zapobiega deplanacji ściany, nadal wprowadza ona drobne wiązanie, który można by wyeliminować poprzez inny wybór warunków brzegowych)*. Aby utworzyć podporę przesuwną, dodaj obiekt FemConstraintDisplacement *(**Model → Warunki brzegowe i obciążenia mechaniczne → Warunek brzegowy przemieszczenia**)*. W otwartym oknie dialogowym najpierw wskaż ścianę, do której warunek będzie przyłożony a następnie kliknij przycisk Dodaj. Ponieważ blok będzie mógł się przesuwać po płaszczyźnie x-y, wybierany jest tylko przycisk \"Nieruchomy\" dla \"Przemieszczenie z\" a pozostałe przyciski są pozostawione jako wolne.

<img alt="" src=images/Pic6.png  style="width:700px;">



## Utwierdzone węzły 

Aby zapobiec ruchowi sztywnemu w płaszczyźnie przesuwu, trzy niezależne stopnie swobody muszą zostać wyeliminowane. Żeby to osiągnąć, jeden wierzchołek w płaszczyźnie przesuwu jest blokowany w kierunkach x i y (eliminacja 2 stopni swobody) a inny jest blokowany w kierunku x (eliminacja ostatniego stopnia swobody). Do tego celu tworzone są dwa dodatkowe obiekty FemConstraintDisplacement a efekt jest pokazany poniżej.

<img alt="" src=images/Pic7.png  style="width:700px;">



## Siły styczne 

Ostatni etap definicji analizy to zadanie obciążeń. Aby utworzyć stan prostego ścinania, przykładany jest zestaw sił stycznych, jak pokazano poniżej. Każde obciążenie ma wartość 1000 N i biorąc pod uwagę kierunki przyłożenia, równowaga sił i momentów jest osiągnięta dla wszystkich translacyjnych i obrotowych stopni swobody. W programie FreeCAD wymaga to dodania czterech obiektów FemConstraintForce *(**Model → Warunki brzegowe i obciążenia mechaniczne → Obciążenie siłą**)* - jeden dla każdej ściany. W otwartym oknie dialogowym najpierw wciśnij przycisk Dodaj odniesienie a następnie wskaż ścianę, do której ma być przyłożony warunek brzegowy *(Uwaga: to inna sekwencja niż dla FemConstraintDisplacement)*. Domyślnie, tworzy to zestaw sił prostopadłych do ściany *(siły normalne)*. Aby zmienić je na styczne, wciśnij przycisk kierunku i wybierz krawędź sześcianu, która przebiega w odpowiednim kierunku. Jeśli uzyskany zwrot siły jest nieodpowiedni, można go zmienić zaznaczając opcję \"Odwróć kierunek\".

<img alt="" src=images/Pic8.png  style="width:700px;">



## Analiza w CalculiX 

Teraz wszystkie obszary siatki, materiały i warunki brzegowe są zdefiniowane i jesteśmy gotowi do przeanalizowania deformacji bloku przy pomocy solvera CalculiX. Aktywuj kontener Analiza klikając \"Aktywuj analizę\", otwórz okno dialogowe CalciliX klikając dwukrotnie na obiekcie CalculiXccxTools i wybierz lokalizację dla plików tymczasowych tworzonych przez FreeCAD i CalculiX. Zapisz plik wejściowy CalculiX\'a i sprawdź czy występują ostrzeżenia lub błędy.

<img alt="" src=images/PIC9.png  style="width:700px;">

Po tym można uruchomić analizę wciskając przycisk Uruchom analizę. Jeśli wszystko pójdzie prawidłowo, okno CalculiX\'a powinno pokazać następujące wiadomości.

<img alt="" src=images/Pic10.png  style="width:700px;">



## Wyniki CalculiX 

Po ukończeniu analizy kliknij dwukrotnie na obiekcie \"CalculiX_static_results\" i wybierz opcję \"Przemieszczenie bezwzględne\". Maksymalna wartość przemieszczenia \~ 0.08mm zostanie wyświetlona w odpowiednim polu. Ponieważ maksymalne przemieszczenia jest stosunkowo małe w porównaniu z wymiarami bloku (\<1% rozmiaru bloku), przemieszczenia należy przeskalować. Można to zrobić pod napisem \"Przemieszczenie\", zaznaczając przycisk \"Pokaż\" i skalując przemieszczenie np. współczynnikiem 20. Maksymalne przemieszczenie będzie teraz przesadzone do ok. 20% rozmiaru bloku. Po zamknięciu okna dialogowego, zdeformowana siatka może być ponownie wyświetlona poprzez zaznaczenie obiektu Result_mesh i wciśnięcie klawisza Spacja.

<img alt="" src=images/Figure_11_Deformed_Mesh.png  style="width:700px;">

Aby sprawdzić deformację rdzenia, musimy przeciąć blok. Można tego dokonać tworząc filtr przycinania. Aby aktywować tą funkcjonalność, najpierw musimy utworzyć \"obiekt prezentacji graficznej wyników\" poprzez zaznaczenie obiektu \"CalculiX_static_results\" i wybranie opcji **Wyniki → Prezentacja graficzna wyników** z menu. Następnie, z zaznaczonym obiektem prezentacji graficznej wyników, utwórz filtr wizualizacji deformacji (Wyniki → Filtr wizualizacji deformacji), ustaw Wektor=Displacement i Wartość=20 aby przeskalować przemieszczenie oraz Tryb = \"Surface with Edges\", Pole = \"Displacement\", Wektor = \"Magnitude\" aby pokazać kontury przemieszczenia. Wcisnij Zastosuj i OK. Jako ostatni krok, dodaj Filtr przycięcia obszaru (Wyniki → Filtr przycięcie obszaru) i utwórz płaszczyznę z początkiem \[5.0,2.5,5.0\] i kierunkiem normalnym \[0,1,0\], tj. na ścianie rdzenia z kierunkiem normalnym w osi y. Zaznacz przycisk \"Wytnij komórki\" aby uzyskać gładką powierzchnię. Jak poprzednio, ustaw Tryb = \"Surface with Edges\", Pole = \"Displacement\", Wektor = \"Magnitude\" aby pokazać kontury przemieszczenia. Wciśnij Zastosuj i OK. Wreszcie, wyłącz widoczność Filtra przycięcia obszaru aby pokazać tylko blok przecięcia.

<img alt="" src=images/Figure12_Deformed_Mesh_Clipped_View_(2).png  style="width:700px;">

Na podstawie wyników można łatwo wywnioskować, że rdzeń pozostaje w większości niezdeformowany i pomaga oprzeć się deformacji miękkiej matrycy (porównaj kąt ścięcia niebieskiej części z kątem ścięcia zielonej części). Widać też jednak, że w warunkach prostego ścinania, ściany kompozytowego bloku ulegają wypaczeniu, co sugeruje, że podpora przesuwna na podstawie sześcianu to nieodpowiedni warunek brzegowy.



## Dalsza praca 

Następujące wyzwania mogą być ciekawe jako dalsze ćwiczenia:

1\) Poprawa warunku brzegowego z podpory przesuwnej

2\) Spróbuj utworzyć warunki kontaktu między rdzeniem i matrycą aby zobaczyć czy występuje separacja

Plik programu FreeCAD dla tego przykładu jest załączony poniżej jako punkt wyjścia.

<https://forum.freecadweb.org/viewtopic.php?f=18&t=26517&start=20>

Baw się dobrze !


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Shear of a Composite Block/pl
