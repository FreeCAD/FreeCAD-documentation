# <img alt="" src=images/BIM_tutorial_screenshot.png  style="width:1024px;"> BIM ingame tutorial/pl


{{BIMTutorialAction/pl|descr=To jest samouczek dotyczący obsługi środowiska pracy [BIM](BIM_Workbench/pl.md). Nie należy go czytać tutaj na wiki, ale należy go uruchomić z poziomu programu FreeCAD, w środowisku pracy BIM, w menu '''Pomoc -> samouczek BIM'''. Zawiera serię kroków do wykonania przez użytkownika. Każdy krok kończy się wystąpieniem szablonu [<nowiki>{{BIMTutorialAction|descr|goal1|test1|goal2|test2}}</nowiki>](Template_BIMTutorialAction.md), który informuje o warunku, który musi być spełniony. Obrazy powinny mieć szerokość 300px. Na tej stronie nie powinny być używane żadne obrazy SVG, ponieważ nie są one obsługiwane przez widżet QTextBrowser.}}

### Witamy w środowisku pracy BIM! 

<img alt="" src=images/BIM_Tutorial_title.jpg  style="width:300px;">

Ten poradnik poprowadzi Cię przez różne funkcjonalności środowiska pracy [BIM](BIM_Workbench/pl.md) i pomoże Ci wejść na szlak, modelując bardzo prosty budynek pawilonu. Całkowite wykonanie powinno zająć od jednej do dwóch godzin, w zależności od wcześniejszych doświadczeń z aplikacjami 3D.

Można go przerwać w dowolnym momencie i wznowić później, wybierając z menu **Pomoc -\> Ekran powitalny**, a następnie klikając ponownie pozycję **Poradnik BIM**.

Niektóre kroki w tym poradniku wymagają podjęcia działań. Zostaną one wskazane poniżej tego pola tekstowego, z ikoną pokazującą, czy zadanie zostało wykonane, czy nie. Ale ponieważ jesteśmy dobrymi ludźmi, we FreeCAD, nie jest obowiązkowe wykonywanie czynności, aby przejść dalej przez te strony. Możesz po prostu przeglądać samouczek i pomijać zadania w dogodnym dla siebie czasie.

#### Informacje o wersjach FreeCAD 

Ten poradnik jest napisany dla [najnowszej dostępnej wersji rozwojowej FreeCAD](Download/pl.md) *(obecnie 0.19)*. Program BIM jest jednak tak skonstruowany, aby był kompatybilny z każdą wersją programu FreeCAD. Jeśli używasz wersji FreeCAD starszej niż podana tutaj, niektóre narzędzia BIM mogą wyglądać inaczej, działać inaczej lub nawet być niedostępne. W razie wątpliwości zapoznaj się z [dokumentacją](BIM_Workbench/pl.md), aby dowiedzieć się więcej.

#### Uwagi

Ten tutorial jest ciągle w trakcie opracowywania, dlatego jest **niekompletny**! Jeśli masz sugestie lub rzeczy, które uważasz za niejasne, dlaczego nie pomóc nam uczynić go lepszym na [forum FreeCAD](https://forum.freecadweb.org/viewforum.php?f=23)!


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Skonfiguruj FreeCAD 

FreeCAD posiada rozbudowany system preferencji z wieloma opcjami do ustawienia, znajdujący się w menu **Edycja → Preferencje**. Każde dodatkowe środowisko pracy może dodać więcej stron preferencji, co czyni go bardzo złożonym.

BIM udostępnia ekran [uproszczonej konfiguracji](BIM_Setup/pl.md), który pozwala na szybkie ustawienie kilku najbardziej przydatnych preferencji pracy w środowisku BIM. Ekran preferencji BIM znajduje się w menu **Zarządzanie -> Konfiguracja BIM** *(można również kliknąć odpowiedni przycisk na pasku narzędzi Zarządzaj)*:

<img alt="" src=images/BIM_Tutorial_01.jpg  style="width:300px;">

Otwórz teraz uproszczony ekran preferencji BIM i ustaw różne opcje zgodnie z własnymi upodobaniami.

W razie potrzeby ustaw kursor myszki na dowolnej opcji lub ustawieniu, aby zobaczyć wyjaśnienie, do czego służy:

<img alt="" src=images/BIM_Tutorial_02.jpg  style="width:300px;">

W tym poradniku będziemy pracować z zastosowaniem centymetrów. Proponujemy zatem ustawić preferowane jednostki jako **centymetry**, a domyślny rozmiar kwadratu siatki na **10 cm**. Ustawienia te można zmienić w dowolnym momencie za pomocą przycisku płaszczyzny roboczej znajdującego się na głównym pasku narzędzi oraz wskaźnika jednostek znajdującego się na pasku stanu *(na dole po prawej stronie)*:

<img alt="" src=images/BIM_tutorial_14.jpg  style="width:300px;">


{{BIMTutorialAction/pl|goal1=Otwórz ekran konfiguracji BIM|test1=True if hasattr(FreeCADGui, "BIMSetupDialog") else False|goal2=Ustaw jednostki na centymetry i rozmiar siatki na 10cm|test2=True if ((FreeCAD. ParamGet("User parameter:BaseApp/Preferences/Units").GetInt("UserSchema",0) == 4) and (FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft").GetFloat("gridSpacing",10) == 100)) else False}}

### Utwórz nowy dokument 

Jeśli właśnie zainstalowałeś FreeCAD, prawdopodobnie właśnie patrzysz na **Stronę startową FreeCAD**:

<img alt="" src=images/BIM_tutorial_13.jpg  style="width:300px;">

Strona startowa zawiera listę ostatnich dokumentów, z którymi pracowałeś, a także, w różnych zakładkach, wyjaśnia jak uzyskać pomoc. Jednak aby rozpocząć pracę, musimy stworzyć nowy, pusty **dokument**. Jeśli jeszcze tego nie zrobiłeś, utwórz nowy dokument używając opcji \"Utwórz nowy\...\" na stronie startowej, lub przechodząc do menu **Plik → Nowy**:

<img alt="" src=images/BIM_tutorial_09.jpg  style="width:300px;">

Znajdziesz się wtedy w przestrzeni 3D programu FreeCAD, gotowy do pracy:

<img alt="" src=images/BIM_tutorial_10.jpg  style="width:300px;">


{{BIMTutorialAction/pl|goal1=Utwórz nowy dokument|test1=True if FreeCAD.ActiveDocument else False}}

### Nawigacja w przestrzeni 3D 

Istnieje kilka sposobów używania myszki w programie FreeCAD. Nazywane są one [Profilami nawigacji myszką](Mouse_navigation/pl.md). Możesz zmienić bieżący styl nawigacji w dowolnym momencie, klikając przycisk stylu nawigacji na pasku stanu. Po umieszczeniu kursora myszki nad tym przyciskiem zobaczysz również, do czego służy każdy przycisk myszki. Kilka z nich zostało stworzonych tak, aby pasowały do innych znanych aplikacji. Wybierz taki, z którym czujesz się komfortowo.

<img alt="" src=images/BIM_Tutorial_03.jpg  style="width:300px;">

Kontrolowanie sposobu patrzenia na model w widoku 3D może być wykonane na wiele sposobów: Za pomocą **myszki** *(w zależności od wybranego stylu nawigacji)*, **klawiatury** *(zbadaj zawartość menu **Widok**, aby dowiedzieć się więcej)* lub [Kostki nawigacyjnej](Navigation_Cube/pl.md) *(kliknij różne strzałki i ściany sześcianu, aby wyrównać widok)*.

<img alt="" src=images/BIM_Tutorial_04.jpg  style="width:300px;">


{{BIMTutorialAction/pl|goal1=Wybierz styl nawigacji|test1=True|goal2=Set yourself in Top view|test2=True if FreeCADGui.ActiveDocument.ActiveView.getViewDirection().getAngle(FreeCAD.Vector(0,0,-1)) < 0.01 else False}}

### Reorganizacja interfejsu 

Wszystkie panele i paski narzędzi w programie FreeCAD można przesuwać i modyfikować. Większe panele można również łączyć, przeciągając je i upuszczając na inny. Jeśli Twój ekran jest zbyt mały, aby wyświetlić wszystkie paski narzędzi i ich zawartość *(okrojone paski narzędzi będą wyświetlane ze znakiem **>>**)*, dobrym pomysłem może być przeniesienie ich w lepsze miejsce.

<img alt="" src=images/BIM_Tutorial_05.jpg  style="width:300px;">

Paski narzędzi i panele można również włączać i wyłączać z menu **Widok**.

Środowisko pracy BIM posiada również przyciski przełączające na pasku statusu, które włączają i wyłączają dodatkowe panele, takie jak widok wyboru, widok raportu i konsolę Pythona. Panele te są często przydatne podczas pracy z programem FreeCAD, ale zajmują cenne miejsce na ekranie. Zazwyczaj można je wyłączyć, dopóki nie są potrzebne. Pamiętaj, że komunikaty o błędach są wyświetlane w oknie raportu, więc w razie gdyby coś poszło nie tak, zajrzyj tam.

<img alt="" src=images/BIM_tutorial_17.jpg  style="width:300px;">


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Narzędzia środowiska pracy BIM 

Środowisko [BIM](BIM_Workbench/pl.md) zawiera narzędzia zapożyczone z innych środowisk pracy, takich jak [Architektura](Arch_Workbench/pl.md), [Rysunek Roboczy](Draft_Workbench/pl.md) czy [Część](Part_Workbench/pl.md), jak również kilka własnych narzędzi. Są one zorganizowane w kilku kategoriach. Każda kategoria ma swoje menu i pasek narzędziowy. Poświęć chwilę na zapoznanie się z zawartością menu opisanych poniżej.

#### Rysunki 2D 

Narzędzia te pozwalają na rysowanie płaskich obiektów, takich jak linie, polilinie, prostokąty, łuki, itd\..., które staną się podstawą obiektów BIM. Na przykład, możesz użyć polilinii do zdefiniowania śladu bazowego dla ściany lub prostokąta jako profilu dla belki. Wszystkie obiekty 2D są tworzone w bieżącej [płaszczyźnie robocza](Draft_SelectPlane/pl.md).

<img alt="" src=images/BIM_Tutorial_35.jpg  style="width:300px;">

#### Modelowanie 3D oraz BIM 

Ta kategoria zawiera narzędzia do tworzenia obiektów BIM, takich jak [ściany](Arch_Wall/pl.md) lub [okna](Arch_Window/pl.md), oraz ogólnych, nie-BIM-owych obiektów 3D, takich jak [Prostopadłościan](BIM_Box/pl.md), które możesz później przekształcić w obiekty BIM. Końcowy efekt jest różny, jeśli używasz narzędzia z wybranym obiektem lub nie. Jeśli nie, zostanie wyświetlony interfejs tworzenia. Jeśli wybrałeś obiekt przed uruchomieniem narzędzia, zostanie utworzony obiekt odpowiedniego typu na podstawie wybranego obiektu jako bazy.

<img alt="" src=images/BIM_Tutorial_33.jpg  style="width:300px;">

Typowym przykładem jest wciśnięcie przycisku [ściana](Arch_Wall/pl.md) z wybraną [linią](Draft_Line/pl.md) lub [polilinią](Draft_Wire.md). Ściana zostanie utworzona automatycznie, używając tej linii lub polilinii jako linii bazowej.

Obiekty spoza BIM, w tym obiekty wykonane w innych środowiskach pracy, można w każdej chwili zamienić w obiekty BIM, zaznaczając je i naciskając dowolny przycisk narzędzia BIM.

#### Adnotacje

Narzędzia te tworzą obiekty opisu, takie jak wymiary, teksty, etykiety lub siatki, które nie są używane do modelowania, ale do dodawania adnotacji do modeli i tworzenia dobrze czytelnych rysunków.

<img alt="" src=images/BIM_Tutorial_34.jpg  style="width:300px;">

#### Przyciąganie

Te narzędzia włączają / wyłączają pozycje [przyciągania](Draft_Snap/pl.md). Podobnie jak w większości aplikacji BIM, każda dodatkowa pozycja przyciągania wydłuża czas obliczeń podczas rysowania, więc najlepiej jest mieć włączone tylko te, które są potrzebne.

#### Modyfikacja

Narzędzia te modyfikują istniejące obiekty. Zawierają one zwykłe narzędzia transformacji, takie jak Przesunięcie czy Obrót, a także szereg innych, które działają tylko dla określonych typów obiektów.

#### Zarządzanie

Kategoria ta zawiera narzędzia do ogólnego zarządzania. Większość z nich pozwala na edycję właściwości BIM dużej grupy obiektów jednocześnie, bez konieczności ich zaznaczania.

Każde narzędzie zawarte w tych menu ma swoją stronę z dokumentacją, która szczegółowo opisuje jak działa i jakie opcje są dostępne. Są one wymienione na stronie [Dokumentacja BIM](BIM_Workbench/pl.md), która jest również dostępna z menu **Pomoc**, lub poprzez użycie menu **Pomoc → Co to jest?** i kliknięcie na dowolny przycisk paska narzędzi.


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Przygotowanie przestrzeni roboczej 

Istnieje wiele sposobów tworzenia obiektów BIM w programie FreeCAD. Możesz użyć wbudowanych [Narzędzi BIM](BIM_Workbench/pl.md) z tego środowiska pracy, lub użyć jakiegokolwiek innego narzędzia FreeCAD z innych [środowisk pracy](Workbenches/pl.md). Zarówno narzędzia do rysowania 2D jak i narzędzia 3D BIM z tego środowiska pracy, w przeciwieństwie do innych środowisk takich jak Projekt Części, często używają **płaszczyzn roboczych** i **przyciągania**.

[Płaszczyzna robocza](Draft_SelectPlane/pl.md) jest miejscem, w którym będą tworzone kolejne obiekty. Możesz ją ustawić na jedną z podstawowych płaszczyzn ortogonalnych *(podłoże, przód, bok)*, lub użyć dowolnej wybranej ściany do zdefiniowania bieżącej płaszczyzny roboczej. Możesz również użyć [pośredniej płaszczyzny roboczej](Draft_WorkingPlaneProxy.md) z menu **Przybory** aby zapisać konkretną pozycję płaszczyzny roboczej wewnątrz modelu. [Części budowlane](Arch_BuildingPart/pl.md) również zawierają domyślną pozycję płaszczyzny roboczej. Zmiana aktualnej płaszczyzny roboczej odbywa się poprzez naciśnięcie przycisku płaszczyzny roboczej na pasku narzędzi BIM. *Siatka* zawsze odzwierciedla miejsce, w którym znajduje się płaszczyzna robocza.

Jak już zauważyliście, kąt widzenia i płaszczyzna robocza nie są ze sobą powiązane. Możesz pracować na swojej płaszczyźnie roboczej pod dowolnym kątem widzenia.

Płaszczyznę roboczą należy teraz ustawić w trybie *od góry*:

<img alt="" src=images/BIM_Tutorial_06.jpg  style="width:300px;">

Narzędzia [przyciągania](Draft_Snap/pl.md) pozwalają na precyzyjne umieszczanie nowych obiektów i punktów zgodnie z istniejącą geometrią. Jednakże, włączenie wielu miejsc przyciągania może spowolnić operacje rysowania, więc dobrze jest włączyć tylko te narzędzia przyciągania, których zamierzasz używać. Poświęć chwilę na sprawdzenie, co każde z nich robi, aby w razie potrzeby wiedzieć, które z nich można wyłączyć.

<img alt="" src=images/BIM_Tutorial_07.jpg  style="width:300px;">

Zwróć szczególną uwagę na ostatnie narzędzie, **przyciąganie do płaszczyzny roboczej**, ponieważ zmusi ono każdy przytrzaśnięty punkt do położenia na płaszczyźnie roboczej, zapobiegając w ten sposób przytrzaśnięciu powyżej lub poniżej płaszczyzny roboczej. Często trzeba będzie to włączyć lub wyłączyć, w zależności od wykonywanej operacji.


{{BIMTutorialAction/pl|goal1=Ustawienie płaszczyzny roboczej w trybie "od góry" ''(XY)''|test1=True if ((FreeCAD.DraftWorkingPlane.axis.getAngle(FreeCAD.Vector(0,0,1)) < 0.01) and (FreeCAD.DraftWorkingPlane.weak == False)) else False|goal2=Review the different snapping tools|test2=True}}

### Rysujemy pierwszą ścianę 

Zacznijmy budować nasz pawilon od stworzenia ścian. Ściany można rysować albo bezpośrednio za pomocą narzędzia [ściana](Arch_Wall/pl.md), albo najpierw rysując obiekty 2D, takie jak [linia](Draft_Line/pl.md), [linia łamana](Draft_Wire/pl.md) *(polilinie)* lub [szkice](Sketcher_NewSketch.md), które zdefiniują linię bazową naszych ścian. Gdy mamy zaznaczony taki obiekt bazowy, użycie narzędzia Ściana spowoduje automatyczne przekształcenie go w ściany.

Po pierwsze, powiększ obraz do momentu, gdy widoczna będzie odpowiednia część lub całość siatki. To znacznie ułatwi nam zorientowanie się w tym, co robimy:

<img alt="" src=images/BIM_tutorial_15.jpg  style="width:300px;">

Następnie wciśnij przycisk <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Ściana** z paska narzędzi *(lub wybierz pozycję menu **3D/BIM → Ściana**)*. Kliknij dwa punkty na siatce, wyrównane w pionie, oddalone od siebie o wartość {{Value|300 cm}}. Wciśnięcie klawisza **SHIFT** po kliknięciu pierwszego punktu pozwoli na utrzymanie ściany w poziomie lub pionie. Panel boczny będzie informował o długości ściany podczas rysowania.

<img alt="" src=images/BIM_tutorial_16.jpg  style="width:300px;">

Jeśli utworzyłeś nieprawidłową ścianę, nie martw się! Po prostu usuń ją lub cofnij *(menu **Edycja → Cofnij**)* i spróbuj ponownie.


{{BIMTutorialAction/pl|goal1=Utwórz ścianę|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 1)}}

### Rysujemy drugą ścianę 

Utwórz drugą, poziomą ścianę o długości {{Value|4}} metrów *(lub 400 centymetrów)*. Wybierz narzędzie <img alt="" src=images/Arch_Wall.png  style="width:16px;"> **Ściana**, przesuń i powiększ, aż zobaczysz odpowiedni obszar siatki i wybierz dwa punkty z siatki, aby zdefiniować punkt początkowy i końcowy nowej ściany:

<img alt="" src=images/BIM_tutorial_11.jpg  style="width:300px;">

Po ich utworzeniu wybierz obie ściany, naciskając klawisz **CTRL** i klikając je w widoku 3D lub w [widok drzewa](Document_structure/pl.md), i ustaw ich właściwość **wysokość** na {{Value|2,5 metra}}, a ich **szerokość** na {{Value|20 centymetrów}} *(lub jakąkolwiek inną miarę, jeśli pracujesz w innej jednostce)*, tak aby wyglądały jak poniżej *(użyj myszki, aby obrócić widok, zgodnie z wybranym stylem nawigacji)*:

<img alt="" src=images/BIM_tutorial_08.jpg  style="width:300px;">

Zawsze można skorygować lub zmienić właściwości po utworzeniu ściany lub innego obiektu BIM. Rozwijając obiekt ściany w widoku drzewa, a następnie dwukrotnie klikając linię bazową ściany, możesz również zmodyfikować jej bazowy obiekt 2D. Większość obiektów BIM w FreeCAD jest oparta na innym obiekcie, takim jak linia bazowa lub profil.

<img alt="" src=images/BIM_tutorial_12.jpg  style="width:300px;">

#### Istotne uwagi 

Zauważysz, że niektóre zmiany właściwości w FreeCAD nie są natychmiast odzwierciedlane na obiekcie w widoku 3D. Zamiast tego, obiekt jest oznaczony w drzewie niebieskim znakiem \"do ponownego obliczenia\":

Translations:BIM ingame tutorial/87/pl <img alt="" src=images/BIM_Tutorial_20.jpg  style="width:300px;">

Powodem tego jest fakt, że dokument FreeCAD może być bardzo złożonym łańcuchem współzależnych obiektów. Aktualizacja jednego z nich może wywołać aktualizację wielu innych, a przez to zająć dużo czasu. Aby tego uniknąć, niektóre operacje po prostu zaznaczają obiekt do ponownego obliczenia, a Ty sam wywołujesz ponowne obliczenie używając menu **Edycja → Odśwież** lub naciskając kombinacje klawiszy **Ctrl** + **R**.


{{BIMTutorialAction/pl|goal1=Utwórz dwa prostopadłe obiekty ścian|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList]) == 2)|goal2=Ustaw ich wysokość na wartość 2,50 metra, a szerokość na 20 centymetrów.|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "MakeBlocks" in o.PropertiesList and o.Height.Value == 2500 and o.Width.Value == 200]) == 2)}}

### Nie zapomnij o regularnym zapisywaniu pliku! 

Jak każda inna aplikacja komputerowa, FreeCAD jest podatny na awarie i zawieszanie się, szczególnie gdy mamy z nim mało doświadczenia. Częste zapisywanie plików jest bardzo dobrym nawykiem w tych pierwszych chwilach. FreeCAD posiada również mechanizm automatycznego zapisywania, który można ustawić w menu **Edycja → Preferencje \... → Ogólne → Dokument**.

Zapisz teraz swój plik za pomocą opcji z menu **Plik → Zapisz**.


{{BIMTutorialAction/pl|goal1=Zapisz swój plik|test1=bool(FreeCAD.ActiveDocument.FileName)}}

### Narysuj płytę dachu 

Umieścimy teraz płytę dachową na szczycie naszych ścian. Zamiast rysować płytę bezpośrednio, jak to zrobiliśmy w przypadku ścian, narysujemy najpierw prostokąt, a następnie przekształcimy go w płytę. Obydwie metody są przydatne, więc sugerujemy, abyś najpierw wypróbował jedną z nich, następnie anulował ją *(lub ponownie załadował plik)* i wypróbował drugą.

#### Metoda 1: Narysuj płytę na podłożu, a następnie przenieś ją na miejsce 

Często wygodnie jest traktować górną płaszczyznę XY *(płaszczyznę podłoża)* jako swego rodzaju \"deskę kreślarską\", na której będziemy budować nasze obiekty, a następnie przesuwać je obok do ich właściwego położenia. Jest tu jeszcze jedna dodatkowa zaleta, nasza płaszczyzna robocza jest już w trybie \" Góra\", więc nie musimy jej zmieniać.

Ustaw się w widoku z góry, powiększ nieco widok, aż zobaczysz obie ściany, i narysuj prostokąt obejmujący je obie. Wciśnij przycisk <img alt="" src=images/Draft_Rectangle.png  style="width:16px;"> **Prostokąt**\' z paska narzędzi *(lub wybierz z menu **Kreślenie 2D → Prostokąt**)*:

<img alt="" src=images/BIM_Tutorial_18.jpg  style="width:300px;">

Obróć widok, aby sprawdzić wyniki. Domyślnie prostokąt jest zapełniony powierzchnią. Można to zmienić poprzez zmianę właściwości **Utwórz ścianę** naszego prostokąta na wartość {{False/pl}}. Dla płyty, którą zamierzamy zbudować, nie ma to żadnego znaczenia, jednak dla innych typów obiektów, obiekt bazowy będący polilinią lub ścianą może mieć znaczenie.

<img alt="" src=images/BIM_Tutorial_19.jpg  style="width:300px;">

Następnym krokiem jest zbudowanie płyty poprzez \"wyciągnięcie\" jej z naszym prostokątem jako jej bazowym *profilem*. W programie FreeCAD obiekty konstrukcyjne takie jak kolumny, belki czy płyty są tworzone za pomocą tego samego obiektu, zwanego **Konstrukcją**. Po utworzeniu obiektu konstrukcji, ustawienie właściwości **Typ IFC** na żądany typ *(kolumna, płyta, itd\...)* jest wszystkim, co jest potrzebne do zmiany jego typu.

Upewnij się, że nasz prostokąt jest zaznaczony, a następnie naciśnij przycisk <img alt="" src=images/BIM_Slab.png  style="width:16px;"> **Płyta** z paska narzędzi *(lub wybierz pozycję menu **3D/BIM -\> Płyta**)*. Jak wspomniano powyżej, można to również zrobić za pomocą narzędzi Słup lub Belka, gdyż wszystkie one tworzą ten sam typ obiektu. Po utworzeniu naszego obiektu musimy dokonać następujących zmian w jego właściwościach:

-   Ustaw jego **Wysokość** na wartość **20 cm**
-   Sprawdź, czy jego **Typ IFC** jest ustawiony na **Płyta**.

Teraz musimy przesunąć naszą nową płytę dachową do jej właściwej pozycji, czyli ponad ściany. Musimy więc przesunąć ją w górę, w kierunku Z, o odległość 250 cm, czyli wysokość naszych ścian. Możemy po prostu edytować właściwość **Umiejscowienie** naszej płyty, rozwinąć jej atrybut **Pozycja**\' i ustawić wartość **z** na {{Value|250 cm}}. Nasza płyta jest teraz dobrze osadzona:

<img alt="" src=images/BIM_Tutorial_21.jpg  style="width:300px;">

Innym sposobem na przesunięcie naszej płyty na właściwą pozycję, jest użycie <img alt="" src=images/Draft_Move.png  style="width:16px;"> narzędzia **Przesunięcie** z menu **Modyfikacja**. W tym celu musimy najpierw ustawić naszą płaszczyznę roboczą w płaszczyźnie pionowej, naciskając przycisk <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **płaszczyzna robocza** *(upewnij się, że nie masz wybranej żadnej ściany)*, i ustawiając ją na **XY \'\'(Od przodu)***. Ustawiając się w widoku z przodu*(wciśnij klawisz **1**)\'\', możemy teraz wybrać płytę, wcisnąć przycisk <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Przesuń**, **Shift**, aby ograniczyć ruch w pionie, kliknij na jeden z punktów na szczycie ścian:

<img alt="" src=images/BIM_Tutorial_23.jpg  style="width:300px;">

#### Metoda 2: Narysuj płytę bezpośrednio na właściwej płaszczyźnie 

Inną przydatną metodą jest bezpośrednia praca na płaszczyźnie docelowej. Możemy łatwo ustawić płaszczyznę roboczą na górną powierzchnię ścian, czyli tam, gdzie chcemy mieć naszą płytę. Zaznaczenie ściany i naciśnięcie przycisku <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **Płaszczyzna robocza** ustawia płaszczyznę roboczą tak, aby pokrywała się z wybraną powierzchnią. Wybierz górną powierzchnię ściany i ustaw ją jako bieżącą płaszczyznę roboczą. Położenie siatki przesuwa się, aby wskazać aktualną płaszczyznę roboczą.

<img alt="" src=images/BIM_Tutorial_22.jpg  style="width:300px;">

Wszystko, co od tej pory będziemy rysować, będzie się działo w tej płaszczyźnie. Jeśli chcesz, możesz teraz ustawić się w widoku z góry, ale nie jest to konieczne. Po ustawieniu płaszczyzny roboczej i włączeniu funkcji przyciągania do płaszczyzny roboczej, można rysować bezpośrednio w dowolnym widoku 3D.

Gdy nasz prostokątny *profil* jest już narysowany, możemy postępować tak samo jak w metodzie pierwszej, aby stworzyć płytę *(zaznaczyć ją, nacisnąć przycisk **Konstrukcja**, ustawić jej właściwości)*.


{{BIMTutorialAction/pl|goal1=Utwórz prostokąt|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Rectangle" in o.Name]) == 1)|goal2=Utwórz płytę o grubości 20cm|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "IfcType" in o.PropertiesList and o.IfcType == "Slab" and o.Height.Value == 200]) == 1)}}

### Tworzenie metalowej kolumny 

Dodajmy metalową kolumnę, aby zapewnić lepsze podparcie dla naszej płyty. Upewnijmy się, że płaszczyzna robocza jest w trybie widoku Od góry, zacznijmy od ustawienia się w widoku z góry *(naciśnij klawisz **2**)* i wyłączmy widoczność płyty, aby lepiej widzieć co jest pod spodem. Zaznacz płytę i wciśnij klawisz **Spacja** aby wyłączyć jej wyświetlanie.

W programie FreeCAD bardzo łatwo jest włączać i wyłączać obiekty lub grupy, a drzewo pokazuje wyraźnie, co jest pokazane, a co ukryte. Pamiętaj, aby często z tego korzystać!

Narzędzie **Kolumna** *(podobnie jak narzędzie **Belka**)* posiada kilka wbudowanych profili, z których będziemy teraz korzystać. Upewnij się, że nic nie jest wybrane, a następnie naciśnij przycisk Kolumna. W **Opcjach konstrukcji** wybierz **CTH**:

<img alt="" src=images/BIM_Tutorial_24.jpg  style="width:300px;">

Kliknij na punkt, aby umieścić kolumnę mniej więcej w tej pozycji. Upewnij się, że nowa kolumna ma typ IFC \"Kolumna\" i nadaj jej wysokość 250cm, aby była tej samej wysokości co nasze ściany.

<img alt="" src=images/BIM_Tutorial_25.jpg  style="width:300px;">

Niestety, wstępne ustawienia CTH mają tylko jedną opcję średnicy 42mm, która jest bardzo cienka, aby podeprzeć naszą betonową płytę dachową. Na szczęście, ponieważ wszystko jest parametryczne, można łatwo zmienić średnicę. Rozwiń nowy obiekt konstrukcyjny w widoku drzewa, a znajdziesz jego obiekt profilowy o nazwie CTH423. Zmień jego średnicę na 12cm, a grubość na 8mm. Teraz mamy wystarczająco mocny słup. Zauważ, że możesz określać jednostki w locie i przełączać się pomiędzy 0,8cm a 8mm bez problemu. FreeCAD zajmie się konwersją.

#### Dodaj płytę podporową 

Potrzebujemy sposobu, aby przymocować nasz metalowy słup do betonowej płyty. Dodajmy więc do jego górnej części płytę, którą można przykręcić do betonowej płyty. Zilustruje to, w jaki sposób można łatwo modyfikować obiekty BIM i tworzyć bardzo precyzyjne obiekty, których potrzebujemy.

Zacznijmy od zmiany wysokości naszej kolumny z 250cm na 249cm, aby zapewnić miejsce na płytę o grubości 1cm. Następnie narysujmy prostokąt o wymiarach 20cm x 20cm, albo na płaszczyźnie podłoża, albo ustawiając wierzchołek kolumny jako aktualną płaszczyznę roboczą, jak nauczyliśmy się w poprzednim kroku. Użyj narzędzia **Przesunięcie**, z aktywnym przyciąganiem do środka i punktu środkowego, aby wyśrodkować prostokąt względem środka kolumny.

Korzystając ponownie z narzędzia Płyta, utwórz z prostokąta obiekt konstrukcyjny, nadaj mu wysokość 1 cm i przenieś na wysokość 249 cm:

<img alt="" src=images/BIM_Tutorial_26.jpg  style="width:300px;">

Teraz dodajmy naszą płytę do kolumny. Obiekty BIM w FreeCAD posiadają dwie właściwości **Dodawanie** oraz **Odejmowanie**, które mogą przyjmować obiekty, które muszą być do nich dołączone lub od nich odjęte. Aby dodać płytę do naszego słupa, zaznaczamy płytę, następnie z wciśniętym **Ctrl** zaznaczamy kolumnę i używamy <img alt="" src=images/Arch_Add.png  style="width:16px;"> **Dodaj** z menu **Modyfikacja**. Nasza płyta jest teraz częścią kolumny:

<img alt="" src=images/BIM_Tutorial_27.jpg  style="width:300px;">

Zaczynając od prostych kształtów jak *profile* i dodając lub odejmując obiekty, możemy szybko stworzyć bardzo złożone obiekty BIM. Należy pamiętać, że dodawanie i odejmowanie danego obiektu BIM można łatwo zmienić poprzez dwukrotne kliknięcie na nim w widoku drzewa i użycie przycisków Dodaj i Usuń. Ponadto ten sam obiekt może być użyty jako dodatek lub odjęcie do wielu innych obiektów.

<img alt="" src=images/BIM_Tutorial_28.jpg  style="width:300px;">


{{BIMTutorialAction/pl|goal1=Utwórz słup rurowy CTH|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "CTH" in o.Label]) == 1)|goal2=Dodaj do kolumny płytkę o wymiarach 20cm x 20cm|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape" in o.PropertiesList and (abs(o.Shape.Volume - 7409000) < 10000)]) == 1)}}

### Dodanie drzwi 

Podobnie jak słupy i belki, drzwi i okna są tworzone za pomocą tego samego obiektu [Okno](Arch_Window/pl.md) w FreeCAD. Zmienia się tylko ich typ IFC. Mogą być niezależne lub, jeśli obiekt jest wybrany podczas uruchamiania narzędzia, wstawione w inny obiekt BIM, w którym to przypadku automatycznie utworzą w nim otwór.

Wstawmy w jedną z naszych ścian szklane drzwi o wymiarach 80cm x 210cm. Zacznijmy od umieszczenia płaszczyzny roboczej na licu ściany, co ułatwi nam precyzyjne umieszczenie naszego okna:

<img alt="" src=images/BIM_Tutorial_29.jpg  style="width:300px;">

Następnie, mając wybraną ścianę, wybierz **Drzwi** z menu **BIM**. Wybierz predefiniowane ustawienie **Drzwi szklane** i ustaw **Szerokość** na wartość {{Value|80cm}} oraz **Wysokość** na wartość {{Value|210cm}}. Pozostałe wartości można ustawić według własnego uznania:

<img alt="" src=images/BIM_Tutorial_30.jpg  style="width:300px;">

Kliknij punkt na podstawie ściany, w którym chcesz umieścić okno. Może to być trudne, ponieważ linie siatki nie zawsze pokrywają się z krawędziami ściany. Naciśnij klawisz **Q**, gdy masz aktywne przyciąganie na przecięciu siatki, i naciśnij go ponownie z aktywnym przyciąganiem na dole ściany. FreeCAD utworzy nowy punkt przyciągania w miejscu przecięcia się ich osi poziomej / pionowej. Użyj tej opcji, aby znaleźć odpowiedni punkt:

<img alt="" src=images/BIM_Tutorial_31.jpg  style="width:300px;">

Jeśli drzwi nie zostały umieszczone poprawnie, spróbuj użyć narzędzia **Przesuń**, aby przesunąć je na właściwą pozycję. W przeciwnym razie cofnij lub usuń je z drzewa modelu i spróbuj ponownie.

Kiedy wszystko jest gotowe, powinieneś otrzymać drzwi prawidłowo osadzone w ścianie:

<img alt="" src=images/BIM_Tutorial_32.jpg  style="width:300px;">


{{BIMTutorialAction/pl|goal1=Stwórz szklane drzwi|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Window" in o.Name]) == 1)}}

### Organizacja naszego modelu 

Mamy teraz w naszym modelu rosnącą kolekcję obiektów BIM. Nadszedł czas, aby wszystko uporządkować. Tworzenie dobrze zorganizowanych modeli, łatwych do zrozumienia przez innych, jest bardzo ważną częścią budowania wysokiej jakości modeli BIM.

Pierwszym bardzo prostym i bardzo dobrym nawykiem jest nadawanie obiektom właściwych i znaczących nazw, abyśmy mogli je później łatwo zidentyfikować w widoku drzewa. Aby zmienić nazwę obiektu, kliknij prawym przyciskiem myszy na nim w widoku drzewa i wybierz **Zmień nazwę**. Model, w którym komponenty są łatwo identyfikowalne przez inne osoby jest ogromną częścią tego, co czyni model BIM dobrym.

Inną ciekawą operacją jest **grupowanie**. Grupy pozwalają na organizowanie obiektów w widoku drzewa, jak pliki i foldery. Obiekt może należeć tylko do jednej grupy. Grupy są tworzone poprzez kliknięcie prawym przyciskiem myszy na korzeń dokumentu lub inną grupę w widoku drzewa i wybranie opcji **Utwórz grupę**. Następnie można przeciągać obiekty do i z grup w widoku drzewa.

Trzecim sposobem na uporządkowanie rzeczy jest użycie warstw. Warstwy są niezależne od grup, możesz używać obu systemów jednocześnie, jeśli chcesz. Podobnie jak grupy, warstwy pozwalają na łatwe włączanie i wyłączanie serii obiektów, ale w przeciwieństwie do grup, nie można ich układać jedna na drugiej. Pozwalają one także na zmianę ustawień wizualnych, takich jak kolor i szerokość linii obiektów potomnych. Warstwy są tworzone i zarządzane za pomocą narzędzia Menedżer warstw znajdującego się w menu **Zarządzanie -\> Menedżer warstw**. Obiekty są dodawane lub usuwane poprzez przeciąganie ich do i z warstw w widoku drzewa.

**Wybór warstwy** na głównym pasku narzędzi pozwala na ustawienie bieżącej warstwy. Po wykonaniu tej czynności każdy nowy obiekt 2D lub BIM zostanie automatycznie umieszczony w tej warstwie.

Wreszcie, aplikacje BIM zazwyczaj pozwalają na grupowanie obiektów w **poziomy** *(lub kondygnacje)* i **budynki**. FreeCAD oferuje również te narzędzia w menu **Modelowanie 3D/BIM**. Podobnie jak belki i słupy, poziomy i budynki używają tego samego typu obiektu o nazwie [Część budowli - piętro](Arch_BuildingPart/pl.md) z innym typem IFC. Działają one tak samo jak grupy, po utworzeniu możesz przeciągać i upuszczać dowolne obiekty do i z grupy. Części budynku są kompatybilne z grupami, więc możesz umieszczać grupy wewnątrz nich.

<img alt="" src=images/BIM_Tutorial_36.jpg  style="width:300px;">

Części budowlane mają wiele innych zastosowań, zapoznaj się z ich [dokumentacją](Arch_BuildingPart/pl.md) aby dowiedzieć się więcej.

Utwórz teraz Część budowlaną wybierając **Kondygnacja** z menu modelowania **3D / BIM**. Upewnij się, że typ IFC jest ustawiony na **Kondygnacja budynku** i przeciągnij do niego wszystkie nasze pozostałe obiekty BIM *(nie trzeba tego robić z obiektami dołączonymi, takimi jak drzwi czy płyta słupa)*, czyli nasze dwie ściany, płytę dachową i metalowy słup.

Zauważ, że ponieważ Części budowlane są ogólnymi komponentami budynku, nie jesteś zmuszony do organizowania swojego modelu według poziomów w programie FreeCAD. Możesz wybrać inne grupowanie swoich elementów. Ale format IFC oczekuje, że rzeczy będą pogrupowane według poziomów, więc jeżeli planujesz używać tego formatu, najlepiej jest traktować Części budowlane jako poziomy.


{{BIMTutorialAction/pl|goal1=Utwórz kondygnację|test1=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name]) == 1)|goal2=Dodaj do niego cztery pozostałe obiekty główne BIM|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "BuildingPart" in o.Name and (len(o.Group) == 4)]) == 1)}}

### Dodawanie płaszczyzn przekroju 

Jedną z najczęściej wykonywanych operacji na modelu BIM jest wyodrębnienie z niego rysunków 2D, takich jak plany czy elewacje. Istnieje kilka sposobów, aby to zrobić w programie FreeCAD, w zależności od wyniku, jaki chcesz uzyskać. Zasadniczo możesz wybrać pomiędzy produkcją rezultatu 2D wewnątrz przestrzeni 3D, co jest przydatne jeśli chcesz go tam przerobić, rozbudować lub lepiej kontrolować jak jest eksportowany do formatów takich jak [DXF](Draft_DXF/pl.md) lub [DWG](FreeCAD_and_DWG_Import/pl.md), lub na arkuszu [Rysunku Technicznego](TechDraw_Workbench/pl.md), który lepiej nadaje się do tworzenia widoków lub eksportu do PDF. W obu przypadkach zaczyna się to od umieszczenia [płaszczyzny przekroju](Arch_SectionPlane/pl.md) w modelu:

<img alt="" src=images/BIM_Tutorial_37.jpg  style="width:300px;">

1.  Wybierz obiekt Poziom, który zawiera Twoje obiekty, stworzone w ostatnim kroku,
2.  Dodaj płaszczyznę przekroju z menu **Adnotacje-\>Płaszczyzna przekroju**.

Płaszczyzny przekroju nie przecinają całego modelu, lecz tylko obiekty znajdujące się w ich właściwości **Obiekty**. Można wybrać płaszczyznę przekroju, aby sprawdzić i zmienić zawartość tej właściwości w dowolnym momencie.

Domyślnie nowa płaszczyzna przekroju zostanie umieszczona w środku wybranego obiektu lub jego zawartości i będzie patrzeć w dół, tak aby utworzyć widok planu piętra. Płaszczyzna przekroju jest jednak obiektem jak każdy inny i można ją przesuwać i obracać w zależności od potrzeb. Umieść ją poziomo, aby utworzyć widok planu, pionowo wewnątrz modelu, aby utworzyć przekrój, lub na zewnątrz modelu, aby utworzyć elewację.


{{BIMTutorialAction/pl|goal1=Wybierz główną część Budowli|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "BuildingPart" in o.Name]) == 1)|goal2=Utwórz płaszczyznę przekroju|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Section" in o.Name and (len(o.Objects) == 1) and ("BuildingPart" in o.Objects[0].Name)]) == 1)}}

### Wyodrębnianie widoków 2D jako geometrii 

Gdy płaszczyzna przekroju jest już na miejscu, możemy teraz stworzyć geometrię 2D na podstawie tego, co widzi, używając narzędzia [Widok 2D kształtu](Draft_Shape2DView/pl.md):

<img alt="" src=images/BIM_Tutorial_38.jpg  style="width:300px;">

1.  Wybierz płaszczyznę przekroju.
2.  Utwórz widok kształtu 2D używając **Modyfikacja → Widok kształtu 2D**
3.  Nasz obiekt widoku jest ukryty pod ścianami. Wyłącz wyświetlanie poziomu i płaszczyzny przekroju wybierając te obiekty w widoku drzewa i naciskając klawisz **Spacja**, abyśmy mogli lepiej zobaczyć nasz rezultat.

<img alt="" src=images/BIM_Tutorial_39.jpg  style="width:300px;">

Stworzony przez nas widok 2D jest obiektem typu wszystko w jednym i będzie znajdował się na płaszczyźnie (0,0) w modelu. Można go przemieszczać i będzie on przeliczany, gdy model ulegnie zmianie.

Aby utworzyć grubsze linie dla obszarów cięcia, możesz utworzyć kolejny widok Kształtu 2D i ustawić jego właściwość **Tryb rzutowania** na \"Linie cięcia\" lub \"Powierzchnie cięcia\", a jego właściwość **W miejscu** na \"Fałsz\". Będziesz miał wtedy dwa obiekty, jeden dla linii widocznych i jeden dla linii ciętych, dla których możesz nadać różne grubości linii.


{{BIMTutorialAction/pl|goal1=Wybierz płaszczyznę przekroju|test1=bool(len([o for o in FreeCADGui.Selection.getSelection() if "Section" in o.Name]) == 1)|goal2=Utwórz widok kształtu 2D|test2=bool(len([o for o in FreeCAD.ActiveDocument.Objects if "Shape2DView" in o.Name]) == 1)}}

### Sporządzanie adnotacji i eksport do formatów CAD 2D 

Możesz umieścić [adnotacje wieloliniowe](Draft_Text/pl.md), [etykiety](Draft_Label/pl.md) *(tekst z linią i strzałką)*, [wymiary](Draft_Dimension/pl.md) na czymkolwiek w przestrzeni modelu: Albo bezpośrednio na modelu 3D, albo też w widoku 2D, który utworzyliśmy w kroku powyżej. Wybór należy do Ciebie, w zależności od tego, co chcesz osiągnąć. Jeśli pozostawisz widok 2D dokładnie pod modelem 3D, możesz również chcieć wykonać obie czynności za jednym razem.

![](images/BIM_Tutorial_34.jpg )

Adnotacje *(teksty, etykiety, wymiary)* zostaną umieszczone na bieżącej **płaszczyźnie roboczej**. Pamiętaj, aby umieścić płaszczyznę roboczą tam, gdzie chcesz umieścić adnotacje. Dzięki temu możesz umieszczać adnotacje w dowolnej płaszczyźnie przestrzeni 3D: Poziomo lub pionowo. Możesz je również przesuwać lub obracać po utworzeniu.

Umieśćmy wymiar poziomy pomiędzy krańcami naszych dwóch ścian:

![](images/BIM_Tutorial_40.jpg )

1.  Ustaw **płaszczyznę roboczą** w pozycji **góra**,
2.  Skieruj swój widok tak, by móc zobaczyć podstawę obu ścian,
3.  Wybierz menu **Adnotacje →** <img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Wymiarowanie](Draft_Dimension/pl.md),
4.  Kliknij na pierwszy punkt na krańcu lewej ściany,
5.  Naciśnij klawisz **Shift** aby przyciąć wymiar pionowo lub poziomo,
6.  Kliknij na drugi punkt na krańcu prawej ściany,
7.  Kliknij w trzeci punkt, aby wskazać, gdzie umieścić linię wymiarową.

[Wymiar](Draft_Dimension/pl.md) posiada wiele ustawień, aby dostosować format, rozmiar i typ tekstu oraz strzałki. Możesz ustawić swoje preferowane wartości domyślne w menu **Edycja → Preferencje → Rysunek Roboczy → Teksty i wymiary**.

Teraz dodajmy tekst:

![](images/BIM_Tutorial_41.jpg )

1.  Wybierz menu **Opisy →** <img alt="" src=images/Draft_Text.png  style="width:24px;"> [Adnotacja wieloliniowa](Draft_Text/pl.md),
2.  Kliknij na wybrane miejsce w oknie widoku 3D, aby umieścić tekst,
3.  Napisz tekst, na przykład **Pawilon**, a następnie kliknij przycisk **Utwórz tekst** lub naciśnij klawisz **Enter** dwa razy.

Dobrym pomysłem jest stworzenie **Grup** dla różnych zestawów adnotacji (plan, przekrój, różne skale, itd\...):

1.  Utwórz grupę klikając prawym przyciskiem myszy na korzeń dokumentu i wybierz **Utwórz grupę**, zmień jej nazwę na \"Adnotacje\".
2.  Wybierz adnotacje, które utworzyliśmy powyżej w drzewie i przeciągnij je do grupy.

#### Eksport do formatu DXF 

Obiekty 2D takie jak linie lub okręgi lub widoki 2D jak te stworzone powyżej, lub adnotacje, są bardzo odpowiednie do eksportu do tradycyjnych formatów 2D CAD takich jak [DXF lub DWG](Draft_DXF/pl.md). Format DWG wymaga zainstalowania w systemie dodatkowego oprogramowania, sprawdź [instrukcje](Draft_DXF/pl.md), aby to zrobić, jeżeli zachodzi taka potrzeba.

Spróbujmy wyeksportować naszą pracę 2D do formatu DXF:

1.  Wybierz widok 2D, wymiar i tekst
2.  Wybierz z menu **Plik → Eksportuj \...**, wybierz format **Autodesk DXF 2D**, wprowadź nazwę pliku i naciśnij **Zachowaj**.

Jeśli nie używasz żadnego programu CAD 2D, istnieje kilka darmowych i otwartych aplikacji, które mogą otwierać pliki DXF *(oprócz oczywiście samego programu FreeCAD!)*, takich jak [LibreCAD](https://librecad.org/) i [QCAD CE](https://qcad.org/).

![](images/BIM_Tutorial_42.jpg )


{{BIMTutorialAction/pl|goal1=Utwórz wymiar|test1=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Dimension" in obj.Name]))|goal2=Utwórz opis|test2=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Text" in obj.Name]))}}

### Tworzenie geometrii 2D na stronie do wydruku 

Arkusze do druku tworzy się i zarządza nimi za pomocą środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md). Utwórzmy nowy arkusz i umieśćmy na nim widok naszego modelu:

1.  Przełącz się do środowiska pracy **Rysunek Techniczny**
2.  Stwórz nowy pusty arkusz używając domyślnego szablonu z menu **Rysunek Techniczny → Wstaw nową domyślną stronę rysunku**
3.  Wybierz płaszczyznę przekroju i utwórz widok na stronie używając **Rysunek Techniczny → Wstaw obiekt środowiska pracy Architektura**
4.  Zmień właściwość **Skala** w widoku architektonicznym i przelicz model naciskając klawisz *(F5)* aby zobaczyć zmiany.

\... Ciąg dalszy nastąpi


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Eksport do formatu IFC 

[IFC, czyli Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes), jest protokołem i formatem plików służącym do wymiany modeli BIM pomiędzy aplikacjami. Zapisując swój model jako plik IFC, będziesz mógł go otworzyć w większości lub wszystkich innych aplikacjach BIM, zarówno open-source jak i prawnie zastrzeżonych.

Operacje importu / eksportu IFC w FreeCAD są wykonywane przez zewnętrzny program o nazwie [IfcOpenShell](http://www.ifcopenshell.org/). Przeczytaj stronę [Architektura: IFC](Arch_IFC/pl.md) aby dowiedzieć się więcej o tym jak go zainstalować.

Po zainstalowaniu IfcOpenShell, eksportowanie modelu jako pliku IFC jest tak proste, jak wybranie obiektów, które chcemy eksportować, lub tylko górnego kontenera *(grupy lub części budynku)*, który zawiera wszystkie inne obiekty, które chcemy eksportować, a potem należy użyć menu **Plik-\>Eksportuj \...** i wybrać format pliku IFC.

Na koniec, po wyeksportowaniu pliku IFC, zawsze warto go sprawdzić przed wysłaniem do innych osób, aby upewnić się, że model wygląda dobrze i nie brakuje w nim żadnego obiektu. W Internecie dostępnych jest wiele darmowych aplikacji do przeglądania formatu IFC dla wielu platform. Dobrą przeglądarką open-source, która działa na wszystkich platformach jest [IFC++](http://ifcquery.com/). Jeśli chcesz użyć pliku IFC do dalszej edycji może być przydatny [dodatek Blender BIM](https://blenderbim.org/).

Aby sprawdzić strukturę i poprawność modelu do eksportu IFC należy uruchomić narzędzie **Zarządzanie → Kontrola wstępna \...**. Zostanie to omówione w następnym rozdziale.


{{BIMTutorialAction|goal1=Otwórz narzędzie BIM Kontrola wstępna i przeprowadź wszystkie testy|test1=True if (hasattr(FreeCADGui,"BIMPreflightDone") and (FreeCADGui.BIMPreflightDone == True)) else False}}

### Zarządzanie własnościami BIM 

Ogromną częścią tego, co czyni dobrym model BIM są właściwości niegeometryczne, które możesz nadać swoim obiektom, takie jak typ, materiał lub właściwości specyficzne dla danego typu. Na przykład, ściana może być oznaczona jako nośna lub nie. Albo jako zewnętrzną lub wewnętrzną. Format [IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) jest bardzo bogaty pod tym względem. Ilość specyfikacji i właściwości, które chcesz nadać swoim obiektom, zależy głównie od twoich potrzeb oraz od tego, jak pracujesz z innymi i czego oczekują od twojego modelu BIM.

Należy pamiętać o jednej ważnej rzeczy: wszystkie obiekty BIM / Arch w FreeCAD obsługują pełny zestaw właściwości IFC. Inne obiekty FreeCAD, takie jak te modelowane za pomocą innych grup roboczych, również zostaną wyeksportowane do IFC, ale nie można zmienić żadnych ich właściwości IFC. Można jednak przekonwertować dowolny obiekt FreeCAD na obiekt BIM poprzez wybranie obiektu i użycie **3D / BIM → Utwórz komponent**.

Najważniejsze dane, które możesz przekazać swoim obiektom, to:

#### Nazwa i opis 

Wydaje się to oczywiste, ale najprostszym sposobem, aby Twój model był bardziej zrozumiały dla innych, jest właściwe nazwanie każdego z obiektów i, jeśli to istotne, dodanie opisu. Można to zrobić po prostu wybierając obiekt i naciskając klawisz **F2** lub zmieniając jego właściwość **Etykieta** aby zmienić jego nazwę. Opis będzie można znaleźć wśród właściwości obiektu.

#### Typ BIM / IFC 

Jest to najbardziej podstawowa informacja. W programie FreeCAD, obiekt utworzony za pomocą narzędzia Ściana będzie miał domyślnie ustawiony typ IFC na \"Ściana\". Możesz to jednak zmienić w każdej chwili. Możesz więc użyć narzędzia Ściana do modelowania np. belki. Wystarczy zmienić jej typ IFC po jej utworzeniu. Aby zmienić typ IFC obiektu, wybierz go, znajdź jego **Typ IFC** w jego właściwościach i zmień typ na inny z rozwijanej listy.

Można również zarządzać zbiorczo nazwami, typami i materiałami kilku obiektów jednocześnie używając menadżera elementów IFC znajdującego się w menu **Zarządzanie → Zarządzaj elementami IFC**.

#### Materiał

Każdy obiekt w konstrukcji ma swój materiał. Sensowne jest więc nadanie każdemu obiektowi w Twoim modelu odpowiedniego materiału, takiego jak beton czy drewno. Aby przypisać materiał do obiektu, wybierz go i użyj [menadzera materiału](Arch_SetMaterial/pl.md) z menu **Zarządzanie → Materiał**.

#### Właściwości

Każdy obiekt BIM może również otrzymać dodatkowe właściwości, na przykład w celu wskazania, czy ściana jest nośną czy nie. IFC pozwala na dodawanie własnych właściwości do wszystkiego, ale większość typów takich jak Ściana czy Belka posiada również specjalne, predefiniowane zestawy właściwości, zwykle nazwane Pset_WallCommon lub Pset_BeamCommon. Możesz dodać te zestawy do swoich obiektów, zmodyfikować wartości właściwości zawartych w zestawie lub dodać swoje własne właściwości. Zarządzanie właściwościami IFC dla wybranego obiektu lub masowa edycja właściwości kilku obiektów na raz odbywa się za pomocą menedżera właściwości w menu **Zarządzanie → Edytuj właściwości IFC**.

#### Ilości

Wielkości takie jak długość, szerokość czy wysokość ściany mogą być również specjalnie zapisane w pliku IFC. Nie są one powiązane z geometrią obiektu, więc gdy spotykamy takie wielkości w pliku IFC, nie ma gwarancji, że odzwierciedlają one rzeczywistą geometrię obiektu. Jednakże wielkości te pozwalają aplikacjom, które nie są w stanie przetwarzać geometrii, takim jak arkusze kalkulacyjne, poznać główne wymiary obiektów. Można sprawdzić, które wielkości zostaną wyeksportowane do IFC za pomocą menedżera wielkości znajdującego się w menu **Zarządzanie → Edytuj ilości IFC**.

Format IFC ma wiele cech szczególnych i czasami aplikacja, w której otwierasz swój plik IFC lub osoba, która otrzyma plik IFC, ma dodatkowe wymagania. Stanie się biegłym modelarzem BIM często oznacza zapoznanie się z tymi wszystkimi szczegółami i tym, co musi być dodane lub określone w modelu BIM. Narzędzie [BIM: Kontrola wstępna](BIM_Preflight/pl.md) pozwala na sprawdzenie Twojego modelu pod kątem kilku z tych szczegółów i najczęstszych wymagań, a także pomaga zdecydować, co należy uwzględnić w modelu, a czego nie.


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Poznaj pozostałe narzędzia BIM i inne środowiska pracy 

Poświęć chwilę na poznanie innych dostępnych narzędzi BIM. Pamiętaj, że niektóre z nich nie są jeszcze ukończone i mogą nie robić wszystkiego, czego od nich oczekujesz. Użyj przycisku \"Co to jest?\" znajdującego się w menu **Pomoc**, aby otworzyć stronę pomocy każdego narzędzia. Forum [FreeCAD](https://forum.freecadweb.org) jest również zawsze dobrym miejscem do szukania lub zadawania pytań, gdy napotkasz specyficzny problem, którego nie możesz rozwiązać.

FreeCAD jest wielką rodziną środowisk pracy, a narzędzia z innych środowisk pracy często się przydają. Jak widzieliśmy powyżej, prawie każdy obiekt utworzony w innych środowiskach może zostać przekształcony w poprawny obiekt BIM, wystarczy użyć narzędzia **3D / BIM → Utwórz komponent** i nadać mu odpowiedni typ IFC.

Więcej samouczków na temat BIM i innych grup roboczych można znaleźć w sekcji [Poradniki](Tutorials/pl.md) w [dokumentacji FreeCAD](https://wiki.freecadweb.org), a także w kompletnej serii wideo [Poradniki BIM](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU) na YouTube.


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Pomóż programowi FreeCAD stać się lepszym narzędziem! 

FreeCAD jest wolnym oprogramowaniem, rozwijanym przez entuzjastyczną społeczność użytkowników, niektórzy z nich rozwijają kod, a wielu innych przyczynia się w takiej czy innej formie do ulepszania oprogramowania, pisząc dokumentację, znajdując i zgłaszając błędy, zgłaszając pomysły, pisząc poradniki i wiele innych rzeczy. Im więcej i bardziej jesteśmy aktywni, tym szybciej oprogramowanie będzie się dalej rozwijać. Dlaczego nie przyłączyć się do nas? Dobrym miejscem do rozpoczęcia jest dział [BIM na forum FreeCAD](https://forum.freecadweb.org/viewforum.php?f=23). Do zobaczenia tam!


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Tutorials](Category_Tutorials.md) > BIM ingame tutorial/pl
