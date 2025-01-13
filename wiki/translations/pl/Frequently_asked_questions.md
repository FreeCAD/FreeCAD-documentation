# Frequently asked questions/pl
Ta strona jest próbą odpowiedzi na najczęściej powtarzające się pytania zadawane na forum FreeCAD. Jeśli masz problem lub pytanie dotyczące programu FreeCAD, sprawdź najpierw poniżej. Następnie, jeśli nie możesz znaleźć odpowiedzi na swoje konkretne pytanie, przejdź do [forum FreeCAD](http://forum.freecadweb.org/viewforum.php?f=3)!



## Instalacja



### Jaki jest najprostszy sposób instalacji FreeCAD w moim systemie? 

Jeśli pracujesz na systemie Windows lub macOS, najprostszym sposobem jest udanie się na stronę [pobierania](Download/pl.md), gdzie znajdziesz kilka gotowych do zainstalowania pakietów. Jeśli natomiast pracujesz na Debianie, Fedorze lub Ubuntu i kilku innych dystrybucjach, FreeCAD znajduje się już w standardowych repozytoriach oprogramowania i możesz go po prostu zainstalować za pomocą menedżera oprogramowania. Na Ubuntu, zespół FreeCAD utrzymuje również własne [repozytoria PPA](Installing_on_Linux/pl#Wersja_stabilna_PPA.md).



### Jakie są warunki wstępne do uruchomienia FreeCAD? 

W przeciwieństwie do większości oprogramowania 3D CAD, FreeCAD może działać bez problemów na najbardziej skromnych komputerach - jak wiadomo, działa na procesorach Pentium IV i Intel Core2 Solo. Jeśli Twój komputer jest wyposażony w aktualny system operacyjny, prawdopodobnie FreeCAD będzie działał. Jedynym warunkiem jest to, że karta graficzna lub chipset musi obsługiwać [OpenGL](http://en.wikipedia.org/wiki/OpenGL), najlepiej nie starsze niż v2.0. W razie problemów należy zapoznać się z sekcją [Rozwiązywanie problemów](Frequently_asked_questions/pl#Rozwiązywanie_problemów.md) z tego FAQ.



#### Wielowątkowość

Podstawą FreeCAD jest jądro modelowania geometrycznego, [OpenCASCADE Technology](http://en.wikipedia.org/wiki/Open_Cascade_Technology) *(OCCT)* zewnętrzna biblioteka, [ma obecnie tylko częściowe wsparcie wielowątkowości](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&p=173095&hilit=Multithread#p173095). Zobacz stronę [wielowątkowość](Multithreading/pl.md), aby uzyskać więcej informacji.



### Co jeśli sam chcę skompilować FreeCAD? 

Kod źródłowy FreeCAD jest zawsze dostępny w repozytorium kodu źródłowego projektu. Samodzielna kompilacja FreeCAD pozwala na korzystanie z najnowszych funkcji, które są opracowywane, ale wymaga odrobiny wiedzy komputerowej, chociaż procedura jest dość prosta. Dostęp do kodu źródłowego jest opisany na stronie [pobieranie kodu źródłowego](Compile_on_Linux/pl#Pobieranie_kodu_.C5.BAr.C3.B3d.C5.82owego.md), a my mamy szczegółowe instrukcje kompilacji dla środowisk [Linux](CompileOnUnix/pl.md), [Mac OSX](compileOnMac/pl.md) i [Windows](CompileOnWindows/pl.md).



### FreeCAD mówi mi, że brakuje jakiegoś modułu lub aplikacji 

FreeCAD zależy od wielu rzeczy, aby oferować całą swoją funkcjonalność. Wszystkie główne wymagane komponenty są zwykle dołączone do instalacji FreeCAD lub dostarczane przez menedżera pakietów, więc zwykle nie ma się czym martwić. Jeśli jednak zainstalowałeś FreeCAD z nieoficjalnych źródeł lub samodzielnie skompilowałeś FreeCAD, może brakować jakiegoś elementu, który nie jest krytyczny dla samego FreeCAD, ale może spowodować, że niektóre funkcje będą niedostępne. Niektóre specyficzne formaty plików, takie jak Collada lub DWG, również wymagają dodatkowych komponentów, które nie mogą być dołączone do FreeCAD i muszą być zainstalowane samodzielnie.

Wszystkie te komponenty i odpowiedni sposób ich instalacji są wymienione na stronie [Moduły Python](Extra_python_modules/pl.md).



## Rozwiązywanie problemów 



### Znane problemy specyficzne dla systemu operacyjnego 

Znane problemy związane z systemem operacyjnym można znaleźć w tym [wątku na forum](https://forum.freecad.org/viewtopic.php?t=30573).



### FreeCAD nie uruchamia się w ogóle 

Może być ku temu wiele powodów, najbardziej prawdopodobne jest to, że brakuje jakiejś biblioteki. Spróbuj uruchomić FreeCAD z terminala *(wpisz {{SystemInput|freecad}} przy pomocy terminala, lub {{SystemInput|FreeCAD}} w niektórych systemach)*, aby sprawdzić, czy nie pojawia się jakiś komunikat o błędzie. Przeczytaj również resztę tego FAQ, ponieważ możesz uzyskać więcej wskazówek do wykrycia przyczyny problemu. Jakby nic nie pomogło, powiedz o tym na [forum](http://forum.freecadweb.org/), na pewno znajdzie się ktoś, kto może pomóc.

W niektórych starszych systemach Windows XP może pojawić się następujący komunikat o błędzie: **Aplikacja nie może się uruchomić, ponieważ konfiguracja side-by-side jest nieprawidłowa. Ponowna instalacja aplikacji może rozwiązać problem**. Przyczyną tego problemu jest to, że w systemie brakuje bibliotek wykonawczych CRT lub zainstalowana wersja jest zbyt stara, ponieważ FreeCAD został połączony z nowszą wersją. W takim przypadku należy zainstalować **Microsoft Visual C++ Redistributable Package**, który można znaleźć na stronie Microsoft. Zobacz także odpowiednią wiadomość na forum [1](http://forum.freecadweb.org/viewtopic.php?f=3&t=1298&p=9961).



### FreeCAD uruchamia się normalnie, ale nie wszystkie ikony są wyświetlane, niektóre z nich są zastąpione czarnym \'X\' 

Niektóre części FreeCAD zależą od zewnętrznego modułu Python o nazwie Pivy. W systemie Windows pivy jest zawarty w instalacji FreeCAD. W systemach Debian/Ubuntu pakiet python-pivy jest częścią standardowych repozytoriów oprogramowania. W innych systemach, w chwili obecnej, może być konieczne samodzielne skompilowanie pivy. Należy pamiętać, że chociaż niektóre narzędzia nie są dostępne bez pivy, reszta FreeCAD działa normalnie.



### Mam problemy z wyświetlaniem, pogląd 3D nie wygląda prawidłowo, podczas przesuwania/obracania obrazu na ekranie pojawiają się jakieś śmieci, itp. 

FreeCAD zależy od OpenGL do wyświetlania zawartości 3D i dlatego wymaga działającego środowiska OpenGL. W niektórych systemach OpenGL nie jest domyślnie aktywowany i może być konieczne zainstalowanie lub uaktualnienie sterowników graficznych. Problem ten występuje najczęściej w systemach Linux lub systemach wirtualnych. Jeśli korzystasz z systemu Linux, spróbuj wykonać następujące czynności:

-   sprawdź, czy twój komputer ma kartę graficzną obsługującą 3D
-   wpisz {{SystemInput|glxinfo}} w oknie terminala i sprawdź na wyjściu, czy Direct Rendering jest ustawiony na \"tak\" i czy dostawca/renderer/wersja OpenGL pasuje do twojej karty graficznej.
-   zainstaluj inne oprogramowanie oparte na OpenGL *(na przykład [Blender](http://www.blender.org))* i sprawdź, czy działa i wyświetla się poprawnie.



### FreeCAD ulega awarii podczas uruchomienia 

Problem może wskazywać na poważniejszy błąd lub jakiś problem w konfiguracji. Większość awarii przy starcie występuje z jednego z dwóch następujących powodów:



#### Sterowniki OpenGL nie są zainstalowane lub nie działają prawidłowo 

Jest to bardzo powszechna przyczyna problemu. Objawy są po prostu takie, że FreeCAD ulega awarii podczas uruchamiania lub za każdym razem, gdy otwierasz widok 3D *(np. tworząc nowy dokument)*. Spróbuj dowiedzieć się, jaki jest twój układ graficzny, następnie sprawdź, czy obsługuje [OpenGL](http://en.wikipedia.org/wiki/OpenGL) *(najnowsze układy tak)*, następnie znajdź odpowiedni sterownik i zainstaluj go. Dobrym sposobem na sprawdzenie, czy OpenGL jest dostępny, jest próba uruchomienia innej aplikacji OpenGL, takiej jak [blender](http://www.blender.org).

A jako ogólną wskazówkę, aby uzyskać więcej informacji o awariach FreeCAD, możesz uruchomić go z parametrem programu {{SystemInput|--write-log}}. Spowoduje to utworzenie pliku **FreeCAD.log** w **$XDG_CONFIG_HOME/FreeCAD** *({{VersionPlus/pl|0.20}})* lub **$HOME/.FreeCAD** *({{VersionMinus/pl|0.19}})* w systemie Linux, lub **$HOME/Library/Preferences/FreeCAD** w systemie macOS, lub **%APPDATA%/FreeCAD** w systemach Windows.

W niektórych rzadkich przypadkach możesz mieć zainstalowany sterownik graficzny, który nie jest odpowiedni dla Twojej karty graficznej. Mieliśmy przypadek, w którym laptop użytkownika miał wbudowaną grafikę Intel, ale zainstalowano sterowniki ATI [opis problemu](http://forum.freecadweb.org/viewtopic.php?f=13&t=5160&start=10#p41042). Po usunięciu plików i ponownej instalacji właściwego sterownika FreeCAD zaczął działać.



#### Niektóre biblioteki, potrzebne przez FreeCAD, nie są obecne w twoim systemie, lub nie zostały znalezione przez FreeCAD 

Mogą istnieć dwie możliwości rozwiązania tego problemu:
albo brakuje jakiejś biblioteki, dlatego FreeCAD odmówi jej uruchomienia,
albo biblioteka tam jest, ale jest to starsza wersja niż oczekuje tego FreeCAD, więc awaria nastąpi, gdy FreeCAD spróbuje użyć brakującej funkcji z tej biblioteki. Częstym przykładem jest sytuacja, gdy masz zainstalowane Qt3 i Qt4 w swoim systemie, FreeCAD może wykryć Qt4, ale jeśli instalacja Qt nie jest właściwie skonfigurowana, niektóre elementy Qt3 mogą być nadal używane, powodując awarie.

Przejrzyj procedurę instalacji *(dla [Linux](Installing_on_Linux/pl.md), [Mac](Installing_on_Mac/pl.md) lub [Windows](Installing_on_Windows/pl.md))*, upewnij się, że zainstalowałeś wszystkie wymagane biblioteki *(w większości systemów linuksowych odbywa się to automatycznie)* i sprawdź jaki jest minimalny numer wersji dla każdego z komponentów.

Jeśli wszystko wydaje się prawidłowe, opisz problem na [forum](http://forum.freecadweb.org/) lub [zgłoś błąd](Tracker/pl.md). Jeśli korzystasz z systemu Linux, łatwo jest wykonać śledzenie debugowania, które zapewnia programistom bardzo przydatne informacje o awarii:

-   w terminalu wpisz: {{SystemInput|gdb freecad}} *(zakładając, że pakiet gdb jest zainstalowany)*,
-   wewnątrz gdb wpisz {{SystemInput|run}},
-   po awarii wpisz {{SystemInput|bt}}, aby uzyskać ślad, który możesz uwzględnić w swoim zgłoszeniu błędu.



### FreeCAD zawiesza się po uruchomieniu 

Po uruchomieniu FreeCAD GUI pojawia się prawie natychmiast, ale GUI jest zamrożony, a wskaźnik obciążenia CPU wynosi około 99%. Może się to zdarzyć na pulpicie KDE podczas korzystania z motywu Oxygen. Jest to błąd w motywie Oxygen i wybranie innego motywu powinno rozwiązać ten problem.



### FreeCAD ulega awarii przy tworzeniu nowego dokumentu lub otwieraniu pliku 

Jeśli FreeCAD ulega awarii podczas tworzenia nowego widoku 3D, spróbuj uruchomić FreeCAD z terminala. Jeśli podczas awarii pojawi się komunikat o błędzie, wspominający {{SystemOutput|Assertion Failed}} i nazwę komponentu zaczynającą się od \"So\" *({{SystemOutput|SoBase}}, {{SystemOutput|SoFieldContainer}} itp.)*, szanse są bardzo wysokie, zwłaszcza jeśli jesteś w systemie Linux, że FreeCAD próbuje użyć dwóch różnych wersji biblioteki Coin, co powoduje awarię. Aby sprawdzić, czy rzeczywiście jest to problem, spróbuj wykonać następujące czynności:

-   Zlokalizuj plik wykonywalny FreeCAD (zwykle w **/usr/lib/FreeCAD/bin**)
-   Uruchom polecenie {{SystemInput|ldd FreeCAD}} z terminala.
-   Zanotuj wersję biblioteki **libCoin.so**, której używa FreeCAD (na przykład **libCoin.so.60**).
-   Zlokalizuj bibliotekę **libSoQt.so** *(zwykle w **/usr/lib**)*
-   uruchom {{SystemInput|ldd libSoQt.so}} i sprawdź, czy łączy się z tą samą wersją Coin, co FreeCAD

Jeśli istnieje jakakolwiek różnica, FreeCAD lub SoQt muszą zostać ponownie skompilowane *(lepiej przekompilować ten, który używa najstarszej wersji Coin)*. Normalnym zachowaniem jest próba skontaktowania się z osobami odpowiedzialnymi za pakowanie SoQt lub FreeCAD i uprzejme poproszenie ich o rozważenie ponownej kompilacji. Jeśli chcesz podjąć ten krok samodzielnie, a ponowna kompilacja SoQt nie jest możliwa, ponieważ psuje inne aplikacje w systemie, możesz zmusić FreeCAD do kompilacji z wymaganą wersją Coin za pomocą {{SystemInput|<nowiki>./configure --with-coin=DIR</nowiki>}}. Musisz jednak upewnić się, że zainstalowany jest prawidłowy pakiet rozwojowy tej wersji Coin.\'\'\'



### FreeCAD ulega awarii po: Edycja → Wyrównanie 

Błąd segmentacji występuje przy {{SystemOutput|vbo_save_playback_vertex_list()}}. Oznacza to, że implementacja VBO w sterowniku graficznym jest zła. Aby uniknąć buforowania wywołań OpenGL możesz spróbować ustawić zmienną środowiskową {{SystemInput|<nowiki>IV_SEPARATOR_MAX_CACHES=0</nowiki>}} i zrestartować FreeCAD.



### Nie mogę zmienić wartości liczbowych w panelach właściwości FreeCAD 

<img alt="Wybór języka." src=images/Jj62l.png  style="width:480px;">

Najprawdopodobniej masz złe ustawienia regionalne Windows. Sprawdź, czy w ustawieniach regionalnych masz ten sam symbol separatora dziesiętnego i znak grupowania cyfr. Jeśli tak, [dostosuj ustawienia systemowe](http://forum.freecadweb.org/viewtopic.php?f=4&t=2655&p=20046#p20041), aby użyć różnych znaków dla symbolu grupowania cyfr i separatora miejsc po przecinku. Należy pamiętać, że nie jest obowiązkowe stosowanie kropki jako separatora dziesiętnego. W tych dwóch ustawieniach konieczne jest stosowanie różnych symboli. 



### FreeCAD funkcjonował normalnie, i nagle już się nie uruchamia 

Może się to również zdarzyć, jeśli zainstalowano starszą wersję FreeCAD i zaktualizowano ją do nowszej wersji. W tym procesie pliki konfiguracyjne FreeCAD mogły zostać z jakiegoś powodu uszkodzone, a teraz FreeCAD nie może ich już odczytać i nie uruchamia się. Rozwiązaniem jest po prostu usunięcie tych plików konfiguracyjnych, aby FreeCAD odtworzył je przy pierwszym uruchomieniu.

-   W Linuksie: Przejdź do **/home/USERNAME/.local/share/FreeCAD** *({{VersionPlus/pl|0.20}}) lub **/home/USERNAME/.FreeCAD** ({{VersionMinus/pl|0.19}})* i usuń pliki **user.cfg** oraz **system.cfg**
-   na komputerze Mac: Przejdź do **/Users/USERNAME/Library/Preferences/FreeCAD** i usuń pliki **user.cfg** oraz **system.cfg**.
-   W systemie Windows: Otwórz eksplorator plików i wpisz **%APPDATA%/FreeCAD** jako ścieżkę do pliku. Po tym usuń pliki **user.cfg** i **system.cfg**.

FreeCAD powinien teraz uruchomić się ponownie normalnie, resetując wszystkie ustawienia.

Istnieje [Makro findConfigFiles](Macro_findConfigFiles/pl.md), które pomoże Ci zlokalizować pliki konfiguracyjne. Można je zainstalować za pomocą Menedżera dodatków w menu Przybory. **Przybory → Menadżer dodatków → Makrodefinicje → findConfigFiles**. Makro odnajdzie folder z plikami konfiguracyjnymi, skopiuje go do schowka i *(spróbuje)* otworzy tę lokalizację za pomocą domyślnej przeglądarki plików. Nie wprowadza żadnych zmian w plikach ani ustawieniach.



## Używanie FreeCAD 



### Czy FreeCAD jest naprawdę bezpłatny? Nawet do użytku komercyjnego? 

FreeCAD jest [oprogramowaniem Open-Source](http://en.wikipedia.org/wiki/Open-source_software) i może być używany nie tylko dla siebie lub do wykonywania prac komercyjnych, ale także do dystrybucji, modyfikacji, a nawet wykorzystania w aplikacji z zamkniętym kodem źródłowym. Podsumowując, możesz robić *(prawie)* wszystko, co tylko zechcesz. Więcej informacji można znaleźć na stronie [Licencja](License/pl.md).



### Jak obracać widok w oknie 3D? 


<center>

Image:Style_of_navigation.png\|Za pomocą **prawego przycisku** myszki. Image:Style of navigation menu.png\|Z menu Edycja **Edycja → Preferencje ...→**


</center>




FreeCAD posiada kilka różnych [trybów nawigacji](Mouse_navigation/pl.md), które można ustawić w oknie dialogowym ustawień preferencji lub zmienić klikając prawym przyciskiem myszy w widoku 3D. Szczegółowe informacje na temat trybów można znaleźć na stronie [Profil nawigacji myszką](Mouse_navigation/pl.md).



### Co można robić z FreeCAD? Od czego zacząć? 

Przejdź do strony [Jak zacząć](Getting_started/pl.md), aby zapoznać się z krótkim opisem narzędzi, których możesz użyć. Istnieje również nowa strona [poradników](Tutorials/pl.md) zawierająca kilka zasobów. Strona [Centrum użytkownika](User_hub/pl.md) zawiera bardziej szczegółowe informacje na temat różnych środowisk pracy FreeCAD. Należy pamiętać, że ponieważ FreeCAD jest stosunkowo nowy, jego interfejs użytkownika jest nadal bardzo prosty i nie zawiera wielu narzędzi. Ale znacznie bardziej zaawansowana funkcjonalność jest już dostępna w [skryptach środowiska Python](Power_users_hub/pl.md).



### Czy istnieje dokumentacja dla początkujących? Jak mogę nauczyć się korzystać z FreeCAD? 

Istnieje wiele dokumentacji rozproszonej w różnych miejscach, zarówno na stronie FreeCAD, jak i poza nią. Możesz zacząć od strony [Jak zacząć](Getting_started/pl.md). Strona [z poradnikami](Tutorials/pl.md) zawiera wiele wyspecjalizowanych stron z przewodnikami, które pomogą ci rozpocząć pracę z różnymi środowiskami pracy. [Podręcznik:Słowo wstępne](Manual:Introduction/pl.md) jest ogólnym, kompletnym przewodnikiem użytkownika po FreeCAD. Strona [Centrum użytkownika](User_hub/pl.md) tej wiki zawiera listę wszystkich stron skierowanych do użytkowników końcowych. Na zewnętrznych stronach, takich jak [Youtube](https://www.youtube.com/results?search_query=freecad), można również znaleźć mnóstwo materiałów wideo stworzonych przez użytkowników. I wreszcie, co nie mniej ważne, forum [2](https://forum.freecadweb.org) zawiera wiele odpowiedzi na pytania zadane przez innych nowicjuszy.



### Chcę importować/eksportować dane w formacie XYZ do / z FreeCAD. Jak to zrobić? 

Proszę odnieść się do strony [FreeCAD Jak importować eksportować](FreeCAD_Howto_Import_Export.md). Być może Twoje pytania uzyskały już tam odpowiedź.



### Gdzie mogę znaleźć obejścia dla funkcji, których FreeCAD obecnie nie obsługuje? 

Więcej informacji można znaleźć na stronie [Obejścia](Workarounds/pl.md).



## Praca z geometrią detalu 



### Jak wyciągać bryły? Nie rozumiem właściwego wyniku 

Teoria jest prosta: Linie *(lub polilinie)* po wyciągnięciu tworzą powierzchnie. Wyciągnięte powierzchnie tworzą bryły.

Jeśli coś zostanie wyciągnięte, a wynikiem nie będzie bryła, oznacza to, że to coś nie było powierzchnią. Jeśli masz linie i chcesz wyciąć z nich bryłę, musisz najpierw wybrać linie, które tworzą zamknięty obwód *(zaznacz kilka obiektów, naciskając **Ctrl**)*, połączyć je w polilinię *(narzędzie [Ulepsz kształt](Draft_Upgrade/pl.md))*, a następnie utworzyć z niej ścianę *(narzędzie <img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> [Ulepsz kształt](Draft_Upgrade/pl.md))*. Jeśli wszystko poszło zgodnie z planem, możesz wyciąć bryłę.

Teraz, może być wiele małych zawirowań, które sprawiają, że otrzymujesz zły wynik. Najlepszym sposobem, aby się upewnić, jest sprawdzenie, co znajduje się wewnątrz przedmiotu, który wyciągasz. Zawartość obiektów można łatwo zbadać za pomocą środowiska Python. Zakładając na przykład, że masz obiekt o nazwie **Wire**, możesz napisać w konsoli Python:


{{code|code=
obj = FreeCAD.ActiveDocument.Wire
shp = obj.Shape
print shp.Faces
print shp.Wires
if shp.Wires:
    for w in shp.Wires:
        print w.isClosed()
}}

Powyższy kod pobiera kształt z obiektu, pokazuje ściany i polilinie obiektu *(jeśli takie istnieją)*, a jeśli istnieją polilinie, wyświetla, czy polilinie są zamknięte. Jeśli nie masz żadnej ściany, nie otrzymasz bryły. Jeśli nie ma zamkniętej polilinii, nie stanie się on powierzchnią. Jeśli jesteś zainteresowany, na stronie [Skrypty danych topologicznych](Topological_data_scripting/pl.md) znajduje się więcej informacji o tym, co można sprawdzić za pomocą języka Python. Jeśli nie możesz połączyć kilku linii w polilinię, najbardziej prawdopodobną przyczyną jest to, że ich punkty końcowe się nie spotykają, muszą istnieć małe przerwy między *(niektórymi)* z nich. Tam, obawiam się, moje doświadczenie mówi mi, że najszybszym sposobem byłoby przerysowanie linii na wierzchu.



### Moje operacje logiczne zawodzą, lub dają dziwne wyniki 

Jak każde jądro modelowania bryłowego, jądro modelowania geometrycznego [Open CASCADE](https://en.wikipedia.org/wiki/Open_CASCADE_Technology) używane w FreeCAD do geometrii części, choć prawdopodobnie najlepsze dostępne jądro geometrii typu open source, ma swoje wady i ograniczenia. Operacje logiczne *(łączenie, odejmowanie, przecinanie)* są skomplikowane i często dają dziwne wyniki. Jest to obecnie ograniczenie, którego nie jesteśmy w stanie rozwiązać od razu, więc najlepszą drogą jest próba uzyskania pożądanego rezultatu poprzez modelowanie w inny sposób. Na przykład, problemy z prymitywami takimi jak cylinder mogą być często rozwiązane poprzez użycie zamiast niego wyciągniętego okręgu. Powierzchnie współpłaszczyznowe między częściami mogą powodować problemy, podobnie jak styczność powierzchni. Zasadniczo, jeśli kształt nie działa, spróbuj przebudować go w inny sposób. W 99% przypadków na końcu uda ci się uzyskać pożądany rezultat.

Aby lepiej zrozumieć operacje logiczne, zobacz te artykuły:

-   <https://wiki.mcneel.com/rhino/booleanfaq>
-   <https://dev.opencascade.org/doc/overview/html/specification__boolean_operations.html#autotoc_md293>



### Kiedy eksportuję *(lub wyświetlam)* mój model, otwory zostają wypełnione 

Nie używaj **Ctrl** + **A** *(ZAZNACZ WSZYSTKO)*, aby wyeksportować wszystko z drzewa hierarchii. Jeśli model składa się z jednego elementu, spróbuj wybrać tylko najnowszy element *(zwykle ostatni)* w drzewie hierarchii.

Kiedy tworzymy model w środowisku pracy [Projekt części](PartDesign_Workbench/pl.md), każdy element przybiera kształt ostatniego i dodaje lub usuwa coś, tworząc liniowe zależności od elementu do elementu podczas tworzenia modelu. W związku z tym funkcja **Wytnij** to nie tylko sam wycięty otwór, ale cała część z wycięciem. Dlatego użytkownik zazwyczaj powinien mieć widoczny tylko najnowszy element *(cechę)* w drzewie modelu, ponieważ w przeciwnym razie poszczególne etapy modelu nakładają się na siebie, a otwory są wypełniane przez wcześniejsze obiekty modelu.

Aby włączyć lub wyłączyć widoczność obiektu, wybierz go w drzewku modelu i naciśnij klawisz **spacji** na klawiaturze. Zazwyczaj wszystko oprócz ostatniej pozycji w drzewie hierarchicznym powinno być wyszarzone a zatem niewidoczne w oknie [widoku 3D](3D_view/pl.md).



### Moje obiekty parametryczne psują się, gdy modyfikuję ich szkice bazowe 

Napotkałeś (nie)sławny problem z nazewnictwem topologicznym. Jest to obecnie główny problem w FreeCAD dla nowicjuszy. Występuje on w całym FreeCAD, ale jest bardziej widoczny podczas korzystania ze [szkicownika](Sketcher_Workbench/pl.md). Wyjaśnienie jest proste: Podczas ponownego obliczania szkicu, elementy geometryczne (krawędzie, ściany\...) są odbudowywane w innej kolejności, w zależności od pierwszeństwa wiązań. Następnie otrzymują one inną nazwę *(Edge1, Edge2, Face1, Face2\...)*. Większość kolejnych operacji zależy od tych nazw, aby zidentyfikować, na którym komponencie podrzędnym działają. Dlatego też, gdy szkic jest przebudowywany, funkcje oparte na takich elementach podrzędnych mogą nagle zmienić swoją geometrię bazową i dać nieprawidłowy wynik.

Jest to bardzo trudny do pokonania problem *([Projekt nazewnictwa topologicznego](Topological_Naming_Project.md) ma na celu jego rozwiązanie)*. Istnieje jednak wiele obejść tego problemu, a bardziej zaawansowanym użytkownikom udaje się go całkowicie uniknąć. Kilka strategii to:

-   Należy pamiętać, że szkice są bardzo wrażliwe na ten problem. Odwoływanie się do konkretnej krawędzi szkicu lub powierzchni obiektu zbudowanego na szkicu, takim jak [wyciągnięcie](PartDesign_Pad/pl.md), jest niebezpieczne, chyba że masz pewność, że te szkice nie zmienią się w czasie lub szkic jest bardzo prosty. Wyciągnięcie zbudowane na prostym prostokątnym szkicu, na przykład, będzie prawdopodobnie bezpieczne, ponieważ wygeneruje tylko jedną ścianę, więc nie ma problemu z kolejnością.
-   Jeśli to możliwe, preferuj inne rodzaje obiektów, takie jak [Część](Part_Workbench/pl.md) lub [Rysunek Roboczy](Draft_Workbench/pl.md). Obiekty te są zawsze budowane w ten sam sposób, a zatem ich komponenty geometryczne zazwyczaj zachowują tę samą kolejność za każdym razem, gdy są przebudowywane. Są one znacznie mniej podatne na problemy z nazewnictwem topologicznym.
-   Aby dołączyć kolejne obiekty do ścian geometrii opartej na szkicu, należy użyć [Geometrii układu odniesienia](PartDesign_Plane/pl.md). Te niewidoczne \"obiekty pomocnicze\" nie zależą od geometrii szkicu, a zatem pozostają stabilne w czasie.



## Wkład na rzecz FreeCAD 



### FreeCAD jest takim wspaniałym programem! Jak mogę pomóc? 

Istnieje wiele różnych sposobów, aby pomóc, nawet jeśli nie jesteś programistą. Oto kilka rzeczy, które możesz zrobić:

-   Przekaż kilka opinii programistom FreeCAD: Zawsze warto wiedzieć, co ludzie myślą, co uważają za dobre, czego im brakuje itp. Napisz notatkę na [forum](http://forum.freecadweb.org/), wyrażając swoją opinię lub złóż wniosek na naszym [trackerze błędów](https://tracker.freecadweb.org/main_page.php)!
-   Pomoc w pisaniu dokumentacji: Dokumentacja, którą posiadamy na tej stronie jest czasami bardzo ograniczona. Jeśli odkryłeś coś, co nie jest dobrze udokumentowane, dodaj tam swoją wiedzę!
-   Pomoc innym nowicjuszom: Kręć się po forum i pomagaj nowym osobom w rozwiązywaniu podstawowych pytań, takich jak jak zainstalować, jak dodać kostkę itp.
-   [Tłumacz dokumentację](Help_FreeCAD/pl#Tłumacz_dokumentację.md) na swój własny język.
-   [Tłumacz FreeCAD](Help_FreeCAD/pl#Tłumacz_interfejs_FreeCAD.md) na swój własny język.
-   Pisz [Poradniki](Tutorials/pl.md) lub nagrywaj samouczki wideo: Samouczki są bardzo łatwym sposobem dla nowicjuszy na naukę nowego oprogramowania. Jeśli zrobiłeś coś fajnego, dlaczego nie pokazać innym, jak to zrobić?
-   Wnieś swój wkład w postaci zasobów i przykładów: Wciąż brakuje nam dobrych plików przykładowych w FreeCAD. Jeśli stworzyłeś coś dobrego, podziel się tym z nami!
-   [Zgłoś błędy](Tracker/pl.md): Bardzo ważne jest, aby wszystkie możliwe błędy zostały naprawione. Jeśli go znajdziesz, zgłoś go tak jasno, jak to możliwe, abyśmy mogli dokładnie zrozumieć, co się dzieje.
-   Spróbuj zakodować coś w środowisku Python: Nigdy wcześniej nie programowałeś, ale chcesz spróbować? Python jest łatwy. Przeczytaj nasze [Wprowadzenie do środowiska Python](Introduction_to_Python/pl.md), ale uważaj, możesz szybko się uzależnić!
-   Zobacz stronę [Pomóż w rozwoju FreeCAD](Help_FreeCAD/pl.md), aby uzyskać więcej informacji na temat tego, jak wnieść swój wkład.



### W jaki sposób mogę uzyskać uprawnienia do edycji na Wiki? 

Zobacz akapit strony [Pracuj nad dokumentacją](Help_FreeCAD/pl#Pracuj_nad_dokumentacją.md), aby uzyskać więcej informacji na temat tego, jak wnieść swój wkład.



### Czy FreeCAD uczestniczy w Google Summer of Code? 

Tak, od 2016 roku FreeCAD uczestniczy w Google Summer of Code. Zobacz [Google Summer of Code](Google_Summer_of_Code.md), aby uzyskać informacje o poprzednich edycjach, oraz [Google Summer Of Code 2016](http://forum.freecadweb.org/viewtopic.php?f=8&t=13838) na forum, aby zapoznać się z oryginalnym ogłoszeniem.



### Chcę zacząć tłumaczyć Wiki w moim własnym języku. Co mam zrobić? 

Ta wiki zawiera wiele treści. Najbardziej aktualny i interesujący materiał zebrano w [podręczniku](Online_Help_Toc/pl.md).

Zobacz akapit strony [Tłumaczenie dokumentacji](Help_FreeCAD/pl#Tłumacz_dokumentację.md), aby uzyskać więcej informacji na temat tłumaczenia Wiki.



### Czy mogę kupić upominek? 

FreeCAD nie oferuje gadżetów, które można zamówić, aby wesprzeć projekt. Ale możesz stworzyć własne. Instrukcje można znaleźć na naszej stronie [o gadżetach](Swag/pl.md).



## Licencjonowanie, kopiowanie i ponowne wykorzystywanie 



### Czy muszę zapłacić, żeby używać FreeCAD? 

FreeCAD jest całkowicie bezpłatny w użytkowaniu, pobieraniu, redystrybucji lub modyfikacji. Jest to [oprogramowanie Open-Source](http://en.wikipedia.org/wiki/Open_source), opublikowane na warunkach [GNU Lesser General Public License 2.1](http://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), które gwarantuje wam te prawa i, co ważniejsze, gwarantuje, że prawa te nigdy nie zostaną wam odebrane.



### Czy mogę ponownie wykorzystać dowolną część grafiki FreeCAD lub części witryny? 

Jasne. Wszystkie prace graficzne *(ikony, banery, itp.)* FreeCAD są licencjonowane przez LGPL, tak samo jak kod FreeCAD. Pomóż sobie na stronie [Działanie artystyczne](Artwork/pl.md). Strona jest standardową stroną MediaWiki, wszystkie elementy graficzne mogą być swobodnie wykorzystywane ponownie, a jeśli jesteś ciekaw, jak dostosować oprogramowanie MediaWiki tak jak my, poszukaj specjalnych stron Common css i js.



### Czy mogę ponownie wykorzystać moduły FreeCAD w innej aplikacji? 

Tak, możesz używać podstawowych części FreeCAD w innych aplikacjach, o ile przestrzegasz warunków licencji LGPL. Biblioteki stron trzecich, [zewnętrzne środowiska pracy](External_workbenches/pl.md) i [makrodefinicje](Macros/pl.md) mogą podlegać ich własnym warunkom licencyjnym, więc należy skonsultować się z ich autorami. Więcej szczegółów można znaleźć na stronie [Licencja](License/pl.md).



---
⏵ [documentation index](../README.md) > [Documentation](Category_Documentation.md) > Frequently asked questions/pl
