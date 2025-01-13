# <img alt="Ikonka FreeCAD dla zewnętrznego środowiska pracy KicadStepUp" src=images/Kicad-StepUp-tools-WB.svg  style="width:64px;"> KicadStepUp Workbench/pl






## Wprowadzenie

Środowisko pracy KicadStepUp ma na celu pomóc zarówno użytkownikom KiCad, jak i FreeCAD we współpracy przy projektowaniu elektrycznym *(ECAD)* i mechanicznym *(MCAD)*.



## Kontekst

KiCad *([strona domowa](https://kicad.org/))* to otwarty pakiet do automatyzacji projektowania elektroniki. Umożliwia użytkownikowi zaprojektowanie schematu elektronicznego, a następnie jedno - lub wielowarstwowej płytki drukowanej *(PCB)* przy użyciu obszernej biblioteki części. Wspaniałą rzeczą jest to, że używanie FreeCAD z środowiskiem KicadStepUp jest oficjalnym sposobem KiCad na tworzenie części 3D dla komponentów elektronicznych dla KiCad. Biblioteki są hostowane [w serwisie GitHub](https://gitlab.com/kicad/libraries), więc każdy może tworzyć i sprawdzać części.

Filozofia GUI KiCad jest nieco inna niż FreeCAD, zwłaszcza jeśli chodzi o tworzenie elementów i przenoszenie ich. Jednak ponieważ KiCad jest używany w produkcji od lat, istnieje doskonała dokumentacja, np. bardzo dobry dokument \"Pierwsze kroki\". Dodatkowo, każde narzędzie posiada własną instrukcję.

Jeśli ktoś nie zna jeszcze programu [KiCad](https://kicad.org/), zaleca się wykonanie samodzielnej płytki PCB zgodnie z instrukcją [Wprowadzenie do obsługi](https://docs.kicad.org/8.0/en/getting_started_in_kicad/getting_started_in_kicad.html), aby zrozumieć związane z nią koncepcje. Chociaż niektóre tematy, takie jak dodawanie nowych schematów i footprintów do lokalnej biblioteki, wydają się mało interesujące dla początkujących, w praktyce są one często napotykane szybko po rozpoczęciu poważnego projektu.

Dla wszystkich tych koncepcji [KiCad](https://kicad.org/), można znaleźć jakąś funkcję w środowisku roboczym KicadStepUp. Znajomość tych pojęć znacznie ułatwia zrozumienie, jak korzystać z tego środowiska pracy.



## Funkcjonalność


{{emphasis|W trakcie opracowywania}}

-   Wczytaj płytkę i części programu KiCad do FreeCAD i wyeksportuj je do STEP *(lub IGES)* w celu pełnej współpracy ECAD MCAD.
-   Załaduj footprint programu KiCad do FreeCAD, aby łatwo i precyzyjnie dopasować model mechaniczny do footprintu KiCad.
-   Konwersja modelu STEP 3D części, płytki, obudowy do VRML z właściwościami materiałów dla najlepszego wykorzystania w KiCad.
-   Sprawdzanie wzajemnych zależności i kolizji przy projektowaniu obudów i footprintów.
-   Zaprojektuj nową krawędź PCB za pomocą [Szkicownika](Sketcher_Workbench/pl.md) FreeCAD i WSTAW ją do istniejącej płytki PCB KiCad.
-   WYCIĄGNIJ krawędź PCB z płytki PCB KiCad, edytuj ją w szkicowniku FreeCAD i WSTAW z powrotem do KiCad.
-   Zaprojektuj nowy footprint w FreeCAD, aby uzyskać moc szkicowania footprintów.
-   Generowanie plików VRML kompatybilnych z Blenderem.

<img alt="" src=images/ECAD-MCAD-collaboration.png  style="width:800px;">



## Instalacja

KicadStepUp jest częścią [zewnętrznych środowisk pracy](External_workbenches/pl.md) i może być automatycznie zainstalowany za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menedżera dodatków](Std_AddonMgr/pl.md), który jest dołączony do FreeCAD 0.17 i nowszych wersji, w menu **Przybory → Menedżer dodatków**.



## Użycie


{{emphasis|W trakcie opracowywania}}



### Ogólne podejście do tematu 

Podstawową ideą KicadStepUp jest synchronizacja danych między dwiema aplikacjami. Do użytku domowego możesz mieć FreeCAD i KiCad uruchomione w tym samym czasie. Profesjonalni użytkownicy mogą pracować na tych samych plikach (np. na centralnym serwerze) i mieć specjalistów od mechanicznego CAD *(MCAD)* pracujących w FreeCAD i ekspertów od elektroniki w elektrycznym CAD *(ECAD)*.

KicadStepUp konwertuje standardowe pliki FreeCAD na pliki KiCad i odwrotnie. W ten sposób każda aplikacja może pracować z natywnymi plikami danych. Projekty mogą być używane bez zainstalowanej innej aplikacji lub KicadStepUp. Jest to również powód, dla którego nie jest wymagana żadna wtyczka po stronie KiCad.

Należy zauważyć, że różnice między tymi dwoma programami stwarzają pewne trudności w pełnej wymianie danych.
Jednym z przykładów jest to, że szkicownik używany w KiCad do definiowania konturu płytki jest bardzo ograniczony w porównaniu do środowiska roboczego szkicownika FreeCAD. Tak więc, aby zsynchronizować tam i z powrotem, zawartość szkicownika nie może być bardziej złożona niż szkicownik KiCad może obsłużyć. Z punktu widzenia FreeCAD oznacza to, że możesz chcieć uniknąć korzystania z niektórych funkcji szkicowania FreeCAD. KicadStepUp oferuje obejścia, które mogą być trudniejsze do zrozumienia, jeśli nie masz takiego doświadczenia.



### Podstawowy przebieg pracy 

Współpracę można rozpocząć od nowego lub istniejącego projektu. Rozważamy tutaj nowy projekt, aby zachować prostotę:

1.  Utwórz nowy projekt KiCad w dowolnym miejscu. Nazwijmy go \"KsuTest\"
2.  Otwórz edytor PCB i utwórz zamknięty kontur na warstwie \"Edit.Cuts\". Kształt nie ma znaczenia, i tak go nadpiszemy.
3.  Utwórz nowy plik FreeCAD dla PCB, nazwa nie ma znaczenia. \*
4.  Utwórz szkic z zarysem pożądanej płytki PCB. Nazwijmy go \"pcb design\" *(ale może to być dowolna inna nazwa)* i umieśćmy w nim co najmniej jedno kółko na otwór.
5.  Możesz użyć dowolnych funkcji FreeCAD, aby dołączyć otwory, wycięcia i zewnętrzny kształt do innych komponentów, które możesz posiadać. Zakładamy, że użyjesz tutaj funkcji Szkicownika do wymiarowania, tworzenia wiązań i geometrii roboczej w swoim szkicu.

    :   Jeśli do tworzenia szkicu używasz środowiska pracy Projekt Części, nie ma potrzeby tworzenia Zawartości środowiska Projekt Części, ponieważ nie będziemy tworzyć tego szkicu.
6.  Przełącz się do środowiska pracy KicadStepUp.
7.  Wybierz szkic *pcb design*.
8.  Wybierz przycisk paska narzędzi *Push Sketch to PCB Edge* lub menu *ksu PushPull/ksu Push Sketch to PCB*.
    -   Najpierw otworzy się okno dialogowe z domyślnymi wartościami \"Edge.Cuts\" dla warstwy i {{value|0.16}} dla szerokości linii. Zachowaj te ustawienia domyślne.
    -   Następnie otworzy się okno dialogowe Plik. Kliknij na projekt KiCad *KsuTest*, gdzie powinieneś zobaczyć plik *KsuTest.kicad_pcb*. Jest to plik PCB z tymczasowym obrysem, który utworzyliśmy wcześniej. Wybierz go i potwierdź, aby zastąpić stary plik.

Teraz powinno pojawić się okno dialogowe *New Edge pushed to kicad board!*.

#: Jeśli zapomniałeś o drugim kroku, operacja przepchania może się nie powieść, ponieważ plik PCB musi istnieć i nie może być pusty.

1.  Zamknij i ponownie otwórz edytor PCB w KiCad. \*\*
2.  Kształt ze szkicu FreeCAD powinien się pojawić.
3.  Najedź myszą na okrąg i naciśnij **m** na klawiaturze, aby przesunąć okrąg. Kliknij, aby umieścić go w innej pozycji. Naciśnij przycisk **Zapisz** na pasku narzędzi w lewym górnym rogu.
4.  Przełącz się na FreeCAD i wybierz w środowisku pracy KicadStepUp przycisk narzędzia *Pull Sketch from PCB* lub menu *ksu PushPull/ksu Pull Sketch from PCB*.
    -   Otworzy się pierwsze okno dialogowe z domyślną warstwą *Edge.Cuts* i trzema opcjami do wyboru. Należy wybrać opcję *replace PCB and Sketch in current document* \*\*\*
    -   Następnie pojawi się okno dialogowe z plikiem *KsuTest.kucad_pcb*. Wybierz go i naciśnij **Otwórz**.

        :   Powinieneś zobaczyć swoją płytkę PCB jako model 3D. Zauważ, że otwór przesunął się w porównaniu do szkicu *pcb design*.
        :   Na drzewie pojawi się nowa struktura z żółtym \"Kontenerem środowiska Część\" z nazwą pliku KiCad i wewnątrz innego \"Kontenera\" z *Board_Geoms_e63b* *(część o numerze prawdopodobnie innym)*. W drugim kontenerze znajdują się kolejne trzy pliki. Nie należy zmieniać żadnych nazw w tej strukturze, ponieważ KicadStepUp używa ich do znalezienia części do aktualizacji.
5.  Nie zapomnij zapisać pliku.




    Local_CS_e63b      punkt odniesienia położenia PCB.
                         taki sam jak punkt odniesienia w szkicu "PCB design"
    Pcb_e63b           Obiekt 3D z płytką drukowaną.
                          Nie edytuj, zostanie nadpisany przez KicadStepUp.
    PCB_Sketch_e63b    szkic ze wszystkimi częściami szkicu "pcb design", które rozpoznał KiCad.
                          wszystkie inne zostały usunięte. Należy również pamiętać, że jeśli zmienisz ten szkic
                          i ponownie go przeliczysz, obiekt 3D nie ulegnie zmianie.

Spróbuj wykonać kolejną operację PushPull w obie strony: dostosuj szkic \"pcb design\" do zmian z KiCad, dodaj inną zmianę i zacznij od nowa. Zrób to kilka razy, aby docenić, jak szybko i naturalnie przebiega ta procedura w bardzo krótkim czasie.

Teraz możesz użyć nowego pliku 3D PCB do wyrównania komponentów 3D, takich jak złącza, przyciski, przełączniki, elementy złączne itp. lub dodać go do zespołu, jeśli masz większy projekt.

Pokazuje to tylko bardzo podstawowy sposób działania KicadStepUp. W tym momencie nadal brakuje wielu elementów, np. footprintów i części 3D, ale od tego momentu o wiele łatwiej jest rozpocząć samodzielną eksplorację KicadStepUp. Skorzystaj z pliku PDF z dokumentacją w menu *ksu Tools/Demo*.

Uwagi:

  - Dopóki nazwa utworzonej struktury (i jej części) pozostaje niezmieniona, wszelkie interakcje przepływu pracy będą po prostu aktualizować strukturę. Jeśli zmienisz jakiekolwiek nazwy, za każdym razem zostanie utworzona nowa struktura. Do aktualizacji plików projektu KiCad nie jest wymagane uruchomienie programu KiCad. W rzeczywistości KiCad nie musi być nawet zainstalowany na komputerze. Standardowym podejściem jest używanie tego samego szkicu po obu stronach, KiCad i Freecad. Wszelkie zmiany zostaną zsynchronizowane do drugiej aplikacji. Jest to najbardziej naturalny i czysty sposób pracy z KicadStepUp.
Powoduje to jednak problem, jeśli chcesz użyć dowolnej z następujących funkcji w szkicu do zdefiniowania kształtu PCB: wymiary, wiązania geometrii, geometria konstrukcyjna *(niebieskie linie)* lub zewnętrzna połączona geometria. Nie ma czystego sposobu, aby to zrobić, ponieważ KiCad nie zna żadnej z tych funkcji. Oznacza to, że podczas podróży w obie strony między aplikacjami, każda z tych cech zostanie usunięta. Nie ma prawdziwego rozwiązania tego problemu, a jedynie wybór jednego z kilku obejść. Jeśli więc chcesz użyć którejkolwiek z tych funkcji, oznacza to, że musisz zdefiniować kształt PCB tylko w FreeCAD i zsynchronizować go w jednym kierunku do KiCad. Wszelkie zmiany konturów wykonane w KiCad muszą być dodawane ręcznie po stronie FreeCAD. Może to mieć sens, np. jeśli przyszłe zmiany od strony mechanicznej są znacznie bardziej prawdopodobne niż od strony elektrycznej. Można to zrobić na kilka sposobów: Umieść szkic projektu w strukturze KicadStepUp i wybierz opcję \"replace PCB and keep Sketch in curr. doc\" za każdym razem, gdy importujesz z ponownie z Kicad. Zachowaj szkic projektu poza strukturą KicadStepUp. Zignoruj szkic zaimportowany z KiCad. Drugi wybór ma tę zaletę, że zmiany w KiCad można prześledzić do oryginalnego szkicu, a szkic FreeCAD jest chroniony przed przypadkowym błędnym wyborem importu. Opisany przepływ pracy wykorzystuje to podejście, aby upewnić się, że problem jest dobrze zrozumiany. Stamtąd łatwo jest przejść do modyfikowania dostarczonego szkicu KicadStepUp bez żadnych bardziej zaawansowanych funkcji FreeCAD. Aby użyć KicadStepUp ze Złożeniem FreeCAD *({{VersionPlus/pl|0.19}})*, można dodać nowy plik dla PCB. Po jednokrotnym uruchomieniu powyższego przepływu pracy dodaj obiekt 3D dla PCB do zespołu, tak jak każdą inną część mechaniczną. Upewnij się, że zapisałeś plik, gdy został zaktualizowany przez KicadStepUp *(Ważne: KicadStepUp zapisuje dane w pamięci FreeCAD, a nie w plikach FreeCAD).*

Pozostałe funkcje dostępne są na stronie [Ściągawka dla KicadStepUp](https://github.com/easyw/kicadStepUpMod/blob/master/demo/kicadStepUp-cheat-sheet.pdf).



## Bibliografia

-   Autor: w serwisie Github: [\@easyw](https://github.com/easyw) \| FreeCAD Forums: [kicad StepUp: Dwukierunkowa współpraca ECAD MCAD](https://forum.freecadweb.org/viewtopic.php?f=24&t=14276)
-   Kod źródłowy na GitHub: <https://github.com/easyw/kicadStepUpMod>



## Uwaga dodatkowa dotycząca zewnętrznych środowisk pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku programistycznym [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe \"przestrzenie robocze\" wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > KicadStepUp Workbench/pl
