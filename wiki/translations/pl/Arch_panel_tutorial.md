---
 TutorialInfo:l
   Topic:  Modelowanie panelami architektonicznymi
   Level:  początkujący
   Time:  60 minut
   Author:  Yorik
   FCVersion:  dowolna
   Files: nie dołączono
---

# Arch panel tutorial/pl





To jest kopia postu [poradnika](http://opensourceecology.org/wiki/FreeCAD_Architecture_Tutorial) oryginalnie napisanego dla [Open-Source Ecology](http://opensourceecology.org).



## Prezentacja FreeCAD 

<img alt="" src=images/Arch_panel_tutorial_01.jpg  style="width:800px;">

FreeCAD to parametryczny modeler 3D. Modelowanie parametryczne pozwala na łatwą modyfikację projektu poprzez powrót do historii modelu i zmianę jego parametrów. FreeCAD jest programem typu open source *(licencja LGPL)* i bardzo modułowym, pozwalającym na bardzo zaawansowane rozszerzenia i dostosowywanie, szczególnie dzięki intensywnemu wykorzystaniu języka Python.

-   Strona internetowa FreeCAD: <http://www.freecad.org/>
-   Wiki dokumentacji FreeCAD: <http://www.freecad.org/wiki/index.php?title=Main_Page>
-   Środowiska pracy FreeCAD: <http://www.freecad.org/wiki/index.php?title=Workbench_Concept>
-   Forum FreeCAD: <http://forum.freecad.org/>
-   Rozpoczęcie pracy z FreeCAD: <http://www.freecad.org/wiki/index.php?title=Getting_started>
-   Przewodnik po architekturze: <http://www.freecad.org/wiki/index.php?title=Arch_tutorial>



## Instalacja FreeCAD 

Masz możliwość zainstalowania najnowszej stabilnej wersji *(na dzień dzisiejszy, maj 2015: wersja 0.15)* lub wersji rozwojowej *(obecnie 0.16)*. W rzeczywistości wersje rozwojowe FreeCAD są zazwyczaj dość stabilne i zdecydowanie zachęcamy do wypróbowania wersji rozwojowej, chyba że masz konkretny powód, aby tego nie robić. Ponieważ rozwój FreeCAD jest dość szybki, upewnij się, że jeśli pobierasz ręcznie, sprawdzaj od czasu do czasu i ponownie zainstaluj / zaktualizuj, aby skorzystać z najnowszych ulepszeń.

-   W systemie Windows: Pobierz najnowszą wersję dla swojej wersji systemu Windows *(32- lub 64-bitowej)* ze strony <https://github.com/FreeCAD/FreeCAD/releases>. Kliknij dwukrotnie plik, aby zainstalować.
-   W systemie Mac OS: Pobierz najnowszą wersję ze strony <https://github.com/FreeCAD/FreeCAD/releases>. Kliknij dwukrotnie plik, aby zainstalować.
-   Na Ubuntu: Wersja FreeCAD dostarczana przez Ubuntu jest zwykle nieaktualna, więc zamiast tego zaleca się korzystanie z PPA utrzymywanego przez społeczność FreeCAD. Aby zainstalować, otwórz aplikację \"Źródła oprogramowania\" Ubuntu i dodaj ppa:freecad-maintainers/freecad-stable dla wersji stabilnej lub ppa:freecad-maintainers/freecad-daily dla wersji rozwojowej do źródeł oprogramowania.
-   Na innych platformach: Na większości głównych dystrybucji Linuksa *(Debian, Fedora itp.)* FreeCAD znajduje się w oficjalnych repozytoriach oprogramowania. Nie zawsze jest to jednak najbardziej aktualna wersja. Jeśli potrzebna wersja nie jest dostępna, jedyną opcją jest samodzielna kompilacja FreeCAD *(instrukcje na stronie FreeCAD)*.



## Dodatkowa opcjonalna zawartość 

-   Włączenie importu/eksportu IFC: Aby importować i eksportować projekty do/z formatu pliku IFC, FreeCAD opiera się na importerze IfcOpenShell, który należy zainstalować oddzielnie od <http://ifcopenshell.org/python.html>. Upewnij się, że wybrałeś wersję opartą na Python2.7, która jest tą samą wersją Pythona, z której korzysta FreeCAD.
-   Środowisko pracy do wymiarowania rysunków: Dodatkowe środowisko pracy dla FreeCAD, które oferuje wiele wygodnych narzędzi do dodawania wymiarów i adnotacji do arkuszy rysunkowych 2D FreeCAD: <https://github.com/hamish2014/FreeCAD_drawing_dimensioning> (instrukcje instalacji na stronie internetowej)
-   Środowisko pracy Złożenie 2: Dodatkowe środowisko pracy dla FreeCAD, które oferuje szereg podstawowych narzędzi montażowych: <https://github.com/hamish2014/FreeCAD_assembly2> *(Instrukcje instalacji na stronie internetowej)*.



## Wskazówki dotyczące szybkiego uruchamiania 

Kolekcja poradników dostępnych na wiki FreeCAD jest wciąż bardzo skąpa. Jednak wielu członków społeczności FreeCAD korzysta z youtube do publikowania filmów instruktażowych. Pamiętaj, aby szukać treści związanych z FreeCAD na youtube, to z pewnością najlepsze źródło materiałów do nauki.

FreeCAD jest aplikacją bardzo techniczną, a jego krzywa uczenia się może być stroma. Pamiętaj, aby polegać na samouczkach, wiki dokumentacji i nie wahaj się zadawać pytań na forum, jeśli napotkasz konkretny problem. Pytania, które są jasno sformułowane, zazwyczaj otrzymują bardzo szybkie i wyczerpujące odpowiedzi.



### Bardzo zgrubna lista rzeczy, które musisz wiedzieć 

-   Interfejs FreeCAD jest podzielony na środowiska pracy. Środowiska pracy to po prostu zbiory narzędzi *(przycisków paska narzędzi i menu)*, które są zgrupowane razem, zwykle dla określonego zadania. Po przełączeniu na inne środowisko pracy, interfejs pokazuje narzędzia z tego środowiska. Zawartość dokumentu 3D nie ulega jednak zmianie. Nadal pracujesz na tym samym dokumencie i na tych samych obiektach.

-   FreeCAD jest wciąż w fazie rozwoju, nadal istnieje wiele błędów, a aplikacja może się czasem zawiesić. Zapisuj często i włącz tworzenie kopii zapasowych plików w **Edycja → Preferencje ... → Ogólne → Dokument**

-   Większość obiektów w FreeCAD jest parametryczna. Oznacza to, że ich geometria jest tworzona automatycznie na podstawie szeregu parametrów. Parametry te są zawsze edytowalne w widoku właściwości. Są one zawsze podzielone na parametry, które wpływają na samą geometrię *(zakładka Dane)* i parametry, które wpływają tylko na wyświetlanie obiektu *(zakładka Widok)*. Jednak obiekty utworzone w innych aplikacjach i zaimportowane do FreeCAD zwykle nie są definiowane przez parametry, a zatem nie można ich edytować.

-   Niektóre środowiska pracy *(takie jak Projekt Części, Architektura)* są przeznaczone do pracy tylko z obiektami bryłowymi i odmawiają pracy z obiektami, które nie są bryłowe. Dobrą zasadą jest zawsze praca z obiektami bryłowymi.

-   Chociaż FreeCAD może importować i pracować z obiektami siatkowymi *(środowisko pracy Siatka)*, jest on przeznaczony przede wszystkim do pracy z bardziej zaawansowanym typem obiektu o nazwie brep, który jest używany przez większość jego środowisk pracy *(Część, Projekt Części, Rysunek Roboczy, Szkicownik, Architektura)*. Podczas importowania plików opartych na siatce *(.dae, .orb, .stl \...)* zwykle trzeba przekonwertować te obiekty na brep, zanim będzie można zrobić z nimi coś interesującego. Jednak formaty plików bryłowych *(.step, .iges)*, po zaimportowaniu do FreeCAD, bezpośrednio tworzą obiekty brep. Formaty 2D *(.dxf, .svg)* również tworzą zawartość brep.

-   FreeCAD ma różne sposoby lub tryby korzystania z przycisków myszki. Tryby te można ustawić w preferencjach lub zmienić w locie, klikając prawym przyciskiem myszki na tle okna widoku 3D. Są one opisane na stronie [Profil nawigacji myszką](Mouse_navigation/pl.md). Tryby najlepiej nadające się do pracy CAD to CAD lub Gestures.



## Ćwiczenie: modelowanie panelu dachowego 

Aby zaprezentować typowy przepływ pracy w programie FreeCAD, zamodelujmy panel dachowy zgodnie z opisem na stronie <http://opensourceecology.org/wiki/MicroHouse_4_Roof_-_Module_-_Build_Instructions>. Aby to zrobić, zaczniemy od narysowania różnych elementów w szkicu 2D z wiązaniami, a następnie skorzystamy ze specjalnego obiektu Okno ze środowiska Architektura, który jest w stanie budować złożone obiekty 3D ze szkicu 2D zawierającego kontury kilku elementów. Wreszcie, ponieważ nie potrzebujemy okna, ale panelu dachowego, po prostu przekonwertujemy nasz obiekt okna na inny typ obiektu środowiska Architektura.



### 1. Otwórz FreeCAD, a następnie ustaw preferowane jednostki na \"calowe\" 

W menu **Edycja → Preferencje ... → Ogólne → Jednostki**



### 2. Przełącz się na środowisko pracy szkicownika i utwórz nowy szkic w płaszczyźnie XY 

![](images/Arch_panel_tutorial_02.jpg )

Zwykle, o ile nie ma konkretnego powodu, aby tego nie robić, zawsze będziesz chciał rozpocząć rysowanie szkiców 2D na płaszczyźnie podłoża, wokół punktu odniesienie położenia (0,0). Następnie wygenerowany na tej podstawie obiekt 3D zostanie przesunięty / obrócony do odpowiedniej pozycji.



### 3. Narysuj dwa prostokąty. Na każdym z nich umieść pionowe wiązanie 16 stóp i poziome wiązanie 2 cale 

![](images/Arch_panel_tutorial_03.jpg )

Nie martw się o wymiary elementów podczas ich rysowania, wiązania odpowiednio zmienią ich rozmiar. Aby dodać wiązanie wymiarowe *(pionowe lub poziome)*, możesz wybrać linię lub dwa punkty *(z wciśniętym klawiszem **CTRL**)*.



### 4. Gdy dwa prostokąty będą miały prawidłowy rozmiar, umieść pionowe wiązanie o wartości 0 między ich punktami narożnymi i poziome wiązanie o wartości 4 stóp 

![](images/Arch_panel_tutorial_04.jpg )

Dzięki temu nasze dwa prostokąty są prawidłowo ustawione względem siebie.



### 5. Dodaj dwa dodatkowe elementy 2 cale x 6 cali 

![](images/Arch_panel_tutorial_05.jpg )

Dodaj dwa kolejne prostokąty i powtórz proces. Zauważ, że w powyższym przykładzie nie określiliśmy długości tych elementów, ale raczej umieściliśmy wiązanie odległości między ich końcami a długimi pionowymi elementami i pozostawiliśmy między nimi niewielką przerwę 0,05 cala. Dzieje się tak, ponieważ jeśli sprawimy, że prostokąty zetkną się ze sobą, FreeCAD może błędnie wydedukować pętle i możemy uzyskać dziwne wyniki za pomocą narzędzia Okno środowiska Architektura. Ta mała sztuczka gwarantuje, że każdy prostokąt zostanie rozpoznany jako niezależna pętla przez narzędzie okna środowiska Architektura.



### 6. Dodaj narożne elementy wzmacniające 

![](images/Arch_panel_tutorial_06.jpg )

To samo. Ustaw je na szerokość 6 cali i oddziel je od innych prostokątów o 0,05 cala.



### 7. Narysuj 7 pomocnicznych elementów wzmacniających, ustaw ich szerokość na 2 cale i zwiąż ich lewy i prawy punkt końcowy w odległości 0,05 cala od pionowych prostokątów *(lub w odległości 0 cala od punktów końcowych innych poziomych prostokątów)* 

![](images/Arch_panel_tutorial_07.jpg )

W zależności od systemu, FreeCAD może zacząć wolno przetwarzać nowe wiązania. Jest to wada korzystania z obiektów z wiązaniami, które szybko pochłaniają wiele zasobów systemowych. Należy zawsze rozważyć, czy są one absolutnie potrzebne. Można również usunąć wiązania, gdy spełnią one swoje zadanie. Wymiary te nie będą już stałe, ale jeśli nie będziesz przesuwać elementów, nie ulegną one zmianie. W razie potrzeby zawsze można też dodać wiązania później.



### 8. Oblicz odstępy między 7 elementami wzmacniającymi i ustaw pionowe ograniczenia między nimi 

W naszym przypadku całkowita długość wynosi {{Value|192 cale}}, minus dwa elementy końcowe *(2 x 2 cale)* i dwa wzmocnienia narożne *(2 x 6 cali)*, = 192 - (4 + 12) = 176. Po odjęciu 7 elementów wzmacniających (7 x 2) = 162. Dzieląc to przez 8, otrzymujemy odstęp między każdym wzmocnieniem: {{Value|20,25}}.

![](images/Arch_panel_tutorial_08.jpg )



### 9. Uzyskanie w pełni związanego szkicu 

W prawym panelu *(zakładka Zadania w widoku Połączonym -\> Komunikaty Solvera)* widoczny jest komunikat \"\... 2 stopnie swobody\". Oznacza to, że nasz szkic nie jest w pełni związany *(nadal ma dwa \"sposoby\" deformacji)*. Dzieje się tak dlatego, że chociaż żaden jego element nie może teraz poruszać się względem innych, cały szkic może nadal poruszać się w pionie i poziomie. Aby temu zapobiec, możemy po prostu wziąć jeden z jego punktów narożnych, wybrać punkt początkowy siatki (gdzie przecinają się osie zielona i czerwona) i nacisnąć przycisk **Wiązanie zbieżności**. Spowoduje to zmianę koloru naszego szkicu na zielony, co oznacza, że jest on w pełni związany i żadna jego część nie może się już poruszać.

![](images/Arch_panel_tutorial_09.jpg )

W rzeczywistości nie jest to absolutnie konieczne. Ale zawsze lepiej jest śledzić dokładną pozycję obiektów *(jesteśmy teraz pewni, że nasz narożnik znajduje się w punkcie (0,0))*. Informacja ta przyda się na wypadek, gdyby później coś poszło nie tak lub gdybyśmy musieli ustalić położenie obiektu zbudowanego na podstawie tego szkicu.

Możemy teraz nacisnąć przycisk \"zamknij\" i nasz szkic bazowy został utworzony:

![](images/Arch_panel_tutorial_10.jpg )



### 10. Przełącz się na środowisko pracy Architektury i po wybraniu szkicu naciśnij przycisk **Okno** 

Nasz szkic zniknął, a jeden z jego prostokątów został lekko wyciągnięty w bryłę:

![](images/Arch_panel_tutorial_11.jpg )

Chociaż wydaje się to błędne, jest tak po prostu dlatego, że narzędzie Okno Architektury utworzyło domyślny element z największej pętli, jaką mogło znaleźć w szkicu bazowym. Wkrótce to naprawimy. Zwróć też uwagę, że szkic nie zniknął, został po prostu wyłączony i \"połknięty\" przez nowy obiekt nadrzędny. Nadal można go znaleźć w widoku drzewa, rozwijając obiekt okna i włączając/wyłączając jego wyświetlanie, naciskając klawisz **Spacja**.



### 11. Edytuj komponenty okna, klikając je dwukrotnie w widoku drzewa 

![](images/Arch_panel_tutorial_12.jpg )

Po dwukrotnym kliknięciu okna jego szkic bazowy staje się ponownie widoczny, a my otrzymujemy jego interfejs edycji: Po lewej lista pętli znalezionych w szkicu bazowym, po prawej elementy bryłowe zbudowane na jego podstawie.

Zacznij od usunięcia elementu \"Domyślny\".

Następnie wybierz pierwszą pętlę (Wire0). Zostanie ona podświetlona w oknie widoku 3D. Naciśnij przycisk \"Dodaj\", aby utworzyć z niej nowy element. Nadaj mu nazwę, upewnij się, że ustawiony jest prawidłowa polilinia i nadaj wiciągnięciu długość 6 cali. Przesunięcie powinno pozostać równe 0, ponieważ chcemy umieścić go \"na ziemi\".

Wartość \"Typ\" będzie używana do przypisywania materiałów do okna *(nie została jeszcze zaimplementowana)*, więc obecnie można pozostawić wartość \"Rama\".

![](images/Arch_panel_tutorial_13.jpg )

Następnie naciśnij przycisk \"Utwórz komponent\". Czasami FreeCAD nie odgaduje poprawnie kierunku wytłaczania, dlatego należy edytować komponent i zmienić wartość {{Value|6 cali}} na {{Value|-6 cali}}.

Powtórz tę czynność dla wszystkich potrzebnych elementów:

![](images/Arch_panel_tutorial_14.jpg )

Po zamknięciu panelu edycji otrzymujemy powyższy obiekt. Zauważ, że domyślnie obiekty okien są reprezentowane jako półprzezroczyste. Ponieważ w rzeczywistości nie będzie to okno, możemy to po prostu wyłączyć, ustawiając wartość przezroczystości na 0 we właściwościach widoku.



### 12. Dodaj panel pokrywy 

Mamy teraz ramkę panelu, ale nie sam panel bazowy. Aby to zrobić, najlepiej jest otworzyć nasz szkic bazowy i dodać nowy prostokąt. Pamiętaj jednak, aby żaden z rogów tego prostokąta nie pokrywał się z rogami innych prostokątów, aby nie pomylić naszego obiektu okna, co może wymagać od nas ponownego wykonania całej serii komponentów, jeśli zmieni się kolejność pętli.

Możemy zatem związać ten nowy prostokąt 0,05 cala wewnątrz obwodu. Będzie to wymagało umieszczenia 4 nowych wiązań.

Następnie możemy ponownie edytować nasze okno i dodać nowe komponenty. Widzimy, że znaleziono nowy przewód. Tym razem użyjemy go do dodania panelu z poliwęglanu o grubości {{Value|8 mm}} *(należy pamiętać, że we FreeCAD można bez problemu mieszać jednostki i zapisywać {{Value|8 mm}} jako grubość, nawet jeśli pracujemy w calach)*. Nadamy mu również przesunięcie o 0,05 cala, aby był nieco przesunięty względem ramy, tylko dla zachowania spójności, ponieważ wszystkie części naszego obiektu mają takie przesunięcie między sobą.

![](images/Arch_panel_tutorial_15.jpg )

Możemy teraz utworzyć kolejny komponent w oparciu o tę samą polilinię, aby umieścić kolejny panel na górze naszej ramy. Tym razem nadamy mu odsunięcie 6,05 cala. Nasz panel jest wreszcie gotowy:

![](images/Arch_panel_tutorial_16.jpg )



### 13. Przekształć okno w inny typ komponentu środowiska Architektura 

W tej chwili nie jest to naprawdę konieczne, ale może stać się ważne później, gdy będziemy eksportować lub pracować w innych aplikacjach zorientowanych na konstrukcję, na przykład za pośrednictwem IFC, nie chcemy, aby nasz panel był identyfikowany jako okno.

Środowisko pracy Architektura FreeCAD zapewnia łatwy sposób radzenia sobie z tym, polegający na tym, że każdy typ obiektu może zawsze stać się innym, będąc podstawą innego typu. W tym przypadku zmieńmy nasze okno w obiekt Panel, po prostu wybierając okno i naciskając narzędzie **Panel**.

![](images/Arch_panel_tutorial_17.jpg )

Zauważ, że kolor wynikowego panelu zmienił się, ponieważ obsługa materiałów w FreeCAD i module Architektura jest nadal niekompletna. Kiedy zostanie ukończony, będzie to poprawnie obsługiwane.



### 14. Powielanie panelu 

Nasz panel można następnie powielić i skopiować na kilka sposobów, na przykład za pomocą funkcji kopiuj / wklej. Ale bardziej interesującym sposobem jest użycie narzędzia Klon środowiska Rysunek roboczy *(obecnego również w środowisku pracy Architektury, podobnie jak wszystkie inne narzędzia Rysunku Roboczego)*. Narzędzie Klon zachowuje relację między obiektem bazowym a jego klonem, więc każda modyfikacja obiektu bazowego zostanie odzwierciedlona we wszystkich jego klonach.

![](images/Arch_panel_tutorial_18.jpg )

W obecnej wersji rozwojowej FreeCAD klony obiektów Architektury są teraz również obiektami Architektury.



### 15. Obracanie i pozycjonowanie paneli 

Podczas gdy środowisko pracy Złożenie FreeCAD nie jest jeszcze gotowe, musimy ręcznie pozycjonować nasze elementy, manipulując ich właściwością Umiejscowienie lub używając narzędzi Przesuń i Obróć środowiska Rysunek Roboczy, które są w rzeczywistości tylko wizualnymi sposobami modyfikowania umiejscowienia obiektów.

Zarówno narzędzia Obróć, jak i Przesuń korzystają z systemu przyciągania środowiska Rysunek Roboczy. Dostępne są różne pozycje przyciągania *(punkty końcowe, środkowe itp.)*, które można włączać i wyłączać, co pozwala na bardzo precyzyjne pozycjonowanie i obracanie.

![](images/Arch_panel_tutorial_19.jpg )

![](images/Arch_panel_tutorial_20.jpg )


 {{Draft_Tools_navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Category_Sketcher.md) > Arch panel tutorial/pl
