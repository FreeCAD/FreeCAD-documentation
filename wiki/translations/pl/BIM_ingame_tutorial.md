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

Innym sposobem na przesunięcie naszej płyty na właściwą pozycję, jest użycie <img alt="" src=images/Draft_Move.png  style="width:16px;"> narzędzia **Przesunięcie** z menu **Modyfikacja**. W tym celu musimy najpierw ustawić naszą płaszczyznę roboczą w płaszczyźnie pionowej, naciskając przycisk <img alt="" src=images/Draft_SelectPlane.png  style="width:16px;"> **płaszczyzna robocza** *(upewnij się, że nie masz wybranej żadnej ściany)*, i ustawiając ją na **XY *(Od przodu)***. Ustawiając się w widoku z przodu *(wciśnij klawisz **1**)*, możemy teraz wybrać płytę, wcisnąć przycisk <img alt="" src=images/Draft_Move.png  style="width:16px;"> **Przesuń**, **Shift**, aby ograniczyć ruch w pionie, kliknij na jeden z punktów na szczycie ścian:

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

You can place [Texts](Draft_Text.md), [Labels](Draft_Label.md) (text with line and arrow), [Dimensions](Draft_Dimension.md) on anything in the model space: Either directly on the 3D model, or on the 2D view that we created in the step above. The choice is yours, depending on what you wish to achieve. If you leave the 2D view exactly under the 3D model, you might also want to do both in one go.

![](images/BIM_Tutorial_34.jpg )

Annotations (texts, labels, dimensions) will be placed on the current **Working Plane**. Be sure to place your working plane where you want your annotations. You can this way place annotations in any plane of the 3D space: Horizontally or vertically. You can also move or rotate them after creation.

Let\'s place a horizontal dimension between the extremities of our two walls:

![](images/BIM_Tutorial_40.jpg )

1.  Set the **working plane** to **Top** position
2.  Orient your view to be able to view the base of both walls
3.  Choose menu **Annotations -\>** <img alt="" src=images/Draft_Dimension.png  style="width:16px;"> [Dimension](Draft_Dimension.md)
4.  Click a first point at the extremity of the left wall
5.  Press **SHIFT** to constrain the dimension vertically or horizontally
6.  Click a second point at the extremity of the right wall
7.  Click a third point to indicate where to place the dimension line

[Dimensions](Draft_Dimension.md) have a lot of settings to tweak their aspect and the size and type of the text and arrow. You can set your preferred defaults under menu **Edit-\>Preferences-\>Draft-\>Text and Dimensions**.

Now let\'s add a text:

![](images/BIM_Tutorial_41.jpg )

1.  Choose menu **Annotations -\>** <img alt="" src=images/Draft_Text.png  style="width:16px;"> [Text](Draft_Text.md)
2.  Click a location in the 3D view to place the text
3.  Write the text you wish, for example **Pavilion**, then click the **Create Text** button or press Enter twice.

A good idea is to create **Groups** for the different sets of annotations (plan, section, different scales, etc\...):

1.  Create a group by right-clicking the document root and select **Create group**, rename it to \"Annotations\"
2.  Select the annotations we created above in the tree and drag and drop them into the group

#### Exporting to DXF 

2D objects such as lines or circles or 2D views as we created above or annotations are very suited to export to traditional 2D CAD formats such as [DXF or DWG](Draft_DXF.md). The DWG format requires an additional piece of software to be installed on your system, check the [instructions](Draft_DXF.md) to do that if needed.

Spróbujmy wyeksportować naszą pracę 2D do formatu DXF:

1.  Select the 2D view, the dimension and the text
2.  Select menu **File-\>Export**, choose the **Autodesk DXF**format, a file name, and press **Export**

If you don\'t use any 2D CAD program, there are several free and open-source applications that can open DXF files (apart from FreeCAD itself, of course!) such as [LibreCAD](https://librecad.org/) and [QCAD CE](https://qcad.org/).

![](images/BIM_Tutorial_42.jpg )


{{BIMTutorialAction|goal1=Create a dimension|test1=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Dimension" in obj.Name]))|goal2=Create a text|test2=bool(len([obj for obj in FreeCAD.ActiveDocument.Objects if "Text" in obj.Name]))}}

### Creating 2D geometry on a printable sheet 

Printable sheets are created and managed with the [TechDraw Workbench](TechDraw_Workbench.md). Let\'s create a new sheet and place a view of our model on it:

1.  Switch to the **TechDraw Workbench**
2.  Create a new empty sheet using the default template from menu **TechDraw -\> Insert default page**
3.  Select the section plane and create a view on the page using **TechDraw -\> Insert Arch Workbench Object**
4.  Change the **Scale** property of your Arch View and recalculate the model (F5) to see your changes.

\... To be continued


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Eksport do formatu IFC 

The [IFC, or Industry Foundation Classes](https://en.wikipedia.org/wiki/Industry_Foundation_Classes), is a protocol and file format aimed at interchanging BIM model between applications. By saving your model as an IFC file, you will be able to open it in most or all other open-source or proprietary BIM applications out there.

IFC import/export operations in FreeCAD are performed by an external piece of software called [IfcOpenShell](http://www.ifcopenshell.org/). Read the [Arch IFC](Arch_IFC.md) page to learn further about how to install it.

Once IfcOpenShell is installed, exporting your model as an IFC file is as simple as selecting the objects you wish to export, or just the top container (group or Building Part) that contains all other objects you wish to export, and use menu **File-\>Export** and choose the IFC file format.

Finally, once you have exported an IFC file, it is always a good idea to inspect it before sending it to other people, to make sure the model looks good and no object is missing. There are many free IFC viewer applications available on the internet for many platforms. A good, open-source viewer that works on all platforms is [IFC++](http://ifcquery.com/). If you want to use the IFC file for further editing [Blender BIM Add-on](https://blenderbim.org/) might be useful.

To test the structure and validity of your model for IFC export run the **Manage-\>IFC Preflight** tool. This will be discussed in the next section.


{{BIMTutorialAction|goal1=Open the BIM preflight tool and run all the tests|test1=True if (hasattr(FreeCADGui,"BIMPreflightDone") and (FreeCADGui.BIMPreflightDone == True)) else False}}

### Managing BIM properties 

A huge part of what makes a good BIM model are the non-geometry properties that you can give to your objects, such as type, material, or properties specific to a certain type. For example, a wall can be marked as load-bearing or not. Or as exterior or interior. The [IFC format](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) is very rich in that regard. The amount of specifications and properties you want to give your objects depends mostly on your needs and how you work with others and what they expect your BIM model to contain.

One thing is important to keep in mind: all BIM/Arch objects in FreeCAD support the full set of IFC properties. Other FreeCAD objects, such as those modeled with other workbenches, will also be exported to IFC but you cannot change any of their IFC properties. You can however convert any FreeCAD object to a BIM object by selecting the object and using **3D/BIM -\> Create Component**.

Najważniejsze dane, które możesz przekazać swoim obiektom, to:

#### Name and description 

This seems obvious, but the simplest way to make your model more understandable to others is to properly name each of your objects, and, if relevant, add a description. This is done simply by selecting an object, and pressing **F2**, or change its **Label** property to rename it. The Description will be found among the object properties.

#### The BIM/IFC type 

This is the most fundamental piece of information. In FreeCAD, an object created with the wall tool will have its IFC type set to \"Wall\" by default. But you can change this anytime. So you can use the wall tool to model a beam for example. You only need to change its IFC type after creating it. To change the IFC type of an object, select it, find its **IFC Type** in its properties, and change to another type from the drop-down list.

You can also bulk-manage names, types and materials of several objects at a time using the IFC elements manager found under menu **Manage-\>IFC elements**.

#### Materials

Each object of a construction has a material. So it makes sense to give each object of your model a proper material, such as concrete or wood. To attribute a material to an object, select the object, and use the [materials manager](Arch_SetMaterial.md) from menu **Manage-\>Materials**.

#### Właściwości

Each BIM object can also receive additional properties, for example to indicate that a wall is load-bearing or not. IFC allows you to add custom properties to just anything, but most types such as Wall or Beam also have special, predefined sets of properties, usually named Pset\_WallCommon or Pset\_BeamCommon. You can choose to add these sets to your objects, modify the value of the properties contained in the set, or add your custom properties. Managing the IFC properties for a selected object or bulk edit the properties of several objects at a time is done using the properties manager under menu **Manage-\>IFC properties**.

#### Ilości

Quantities such as length or width or height of a wall can also be specifically written to an IFC file. They are not linked to the geometry of the object, so when meeting such quantities in an IFC file there is no guarantee that they reflect the actual object geometry. However, these quantities allow applications that are not able to process the geometry, such as spreadsheet applications, to know the principal dimensions of objects. You can check which quantities will be exported to IFC using the quantities manager found under menu **Manage-\>IFC quantities**.

The IFC format has many particularities and sometimes the application you will be opening your IFC file with or the person who will receive your IFC file will have further requirements. Becoming a fluent BIM modeller often means to get familiar with all these particularities and what needs to be added or specified to your BIM model. The BIM workbench of FreeCAD provides a [BIM Preflight](BIM_Preflight.md) tool that allows you to check your model for several of these particularities and most common requirements, and help you decide what to include in your model or not.


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Poznaj pozostałe narzędzia BIM i inne środowiska pracy 

Poświęć chwilę na poznanie innych dostępnych narzędzi BIM. Pamiętaj, że niektóre z nich nie są jeszcze ukończone i mogą nie robić wszystkiego, czego od nich oczekujesz. Użyj przycisku \"Co to jest?\" znajdującego się w menu **Pomoc**, aby otworzyć stronę pomocy każdego narzędzia. Forum [FreeCAD](https://forum.freecadweb.org) jest również zawsze dobrym miejscem do szukania lub zadawania pytań, gdy napotkasz specyficzny problem, którego nie możesz rozwiązać.

FreeCAD jest wielką rodziną środowisk pracy, a narzędzia z innych środowisk pracy często się przydają. Jak widzieliśmy powyżej, prawie każdy obiekt utworzony w innych środowiskach może zostać przekształcony w poprawny obiekt BIM, wystarczy użyć narzędzia **3D / BIM → Utwórz komponent** i nadać mu odpowiedni typ IFC.

There are more tutorials about BIM and other workbenches in the [Tutorials](Tutorials.md) section of the [FreeCAD documentation](https://wiki.freecadweb.org), and a complete video series of [BIM tutorials](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU) on youtube.


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}

### Pomóż programowi FreeCAD stać się lepszym narzędziem! 

FreeCAD jest wolnym oprogramowaniem, rozwijanym przez entuzjastyczną społeczność użytkowników, niektórzy z nich rozwijają kod, a wielu innych przyczynia się w takiej czy innej formie do ulepszania oprogramowania, pisząc dokumentację, znajdując i zgłaszając błędy, zgłaszając pomysły, pisząc poradniki i wiele innych rzeczy. Im więcej i bardziej jesteśmy aktywni, tym szybciej oprogramowanie będzie się dalej rozwijać. Dlaczego nie przyłączyć się do nas? Dobrym miejscem do rozpoczęcia jest dział [BIM na forum FreeCAD](https://forum.freecadweb.org/viewforum.php?f=23). Do zobaczenia tam!


{{BIMTutorialAction/pl|descr=Brak działań do wykonania dla tego etapu}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [Tutorials](Category_Tutorials.md) > BIM ingame tutorial/pl
