# Source code management/pl
{{TOCright}}

## Wprowadzenie

Głównym narzędziem do zarządzania kodem źródłowym projektu FreeCAD jest [Git](http://en.wikipedia.org/wiki/Git_%28software%29), który może być łatwo zainstalowany w większości systemów operacyjnych z menedżera pakietów lub bezpośrednio z [strony internetowej Git](https://git-scm.com/). Zaleca się zapoznanie się ze środowiskiem Git przed bezpośrednią pracą z kodem źródłowym FreeCAD. Odwiedź stronę [dokumentacja Git](https://git-scm.com/doc), aby zapoznać się z podręcznikiem źródłowym, a także [Pro Git book](https://git-scm.com/book/en/v2), aby nauczyć się korzystać z systemu w sposób ogólny. Niniejszy dokument koncentruje się na wykorzystaniu Git do rozwoju FreeCAD. Kompilacja programu FreeCAD jest opisana na stronie [Kompilacja](Compiling/pl.md).

Chociaż Git jest przede wszystkim aplikacją terminalową, istnieje wiele klientów graficznych, które ułatwiają pracę z gałęziami, nanoszenie poprawek i wysyłanie żądań ściągnięcia do gałęzi głównej. Przykłady obejmują [gitk](https://git-scm.com/docs/gitk) *(pierwszy opracowany interfejs graficzny)*, [gitg](https://wiki.gnome.org/Apps/Gitg/) *(Gnome)*, [qgit](https://github.com/tibirna/qgit) *(Qt)*, [tig](https://jonas.github.io/tig/) *(Ncurses)*, [git-cola](http://github.com/git-cola/git-cola) i [GitKraken](https://www.gitkraken.com/) *(własnościowy)*. Krótkie wprowadzenie do tego narzędzia można znaleźć w [Rozwój FreeCAD z GitKraken](Developing_FreeCAD_with_GitKraken/pl.md).

Uwaga: jeśli to wszystko zaczyna przyprawiać cię o zawrót głowy, istnieje bardzo dobra nietechniczna seria o tym, jak używać Gita i Githuba, zatytułowana \"[Git i Github dla poetów](https://youtu.be/BCQHnlnPusY)\".

## Dostęp do kodu źródłowego 

Każdy może uzyskać dostęp i kopię kodu źródłowego FreeCAD, ale tylko menedżerowie projektu FreeCAD mają do niego dostęp do zapisu. Możesz uzyskać kopię kodu, studiować go i modyfikować, ale jeśli chcesz, aby Twoje zmiany zostały włączone do oficjalnego kodu źródłowego, musisz wykonać \"pull request\" w stosunku do głównego repozytorium, aby Twoje modyfikacje mogły zostać sprawdzone przez menedżerów. Ten styl rozwoju jest znany jako [Dyktator i porucznicy](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows), ponieważ główni programiści *(dyktatorzy)* i zaufani programiści *(porucznicy)* filtrują kod nadsyłany przez niezależnych programistów i użytkowników.

Jeśli zmiany w kodzie źródłowym są znaczące, zaleca się wyjaśnienie ich w sekcji pull request na forum [FreeCAD](http://forum.freecadweb.org/viewforum.php?f=17).

<img alt="" src=images/FreeCAD_git_workflow.svg  style="width:600px;"> 
*Ogólny przepływ pracy do rozwijania kodu dla FreeCAD. Każdy może uzyskać kod z głównego repozytorium, ale główni deweloperzy mają wyłączne prawo do przeglądania i łączenia zgłoszeń innych deweloperów.*

### Oficjalne repozytorium GitHub 

Kod źródłowy programu FreeCAD jest dostępny w serwisie Github, {{URL|https://github.com/FreeCAD/FreeCAD}}

Aby móc wnieść swój kod, należy posiadać konto [GitHub account](https://github.com/join).

W przeszłości kod źródłowy był przechowywany w repozytorium SVN, {{URL|https://free-cad.svn.sourceforge.net/svnroot/free-cad}}. Przeniesiono je na GitHub, 10 października 2011 r. za pomocą [commit 120ca87015](https://github.com/FreeCAD/FreeCAD/commit/120ca87015).

:   W związku z tym istnieje wiele zmian, które zostały wprowadzone przed tym czasem, a które nie są zapisane we współczesnej historii commitów Git. Więcej na ten temat można przeczytać na stronie [Historia](History/pl.md).

## Ustawianie nazwy użytkownika Git 

= Programiści powinni wysyłać kod do swojego osobistego repozytorium używając swojej nazwy użytkownika GitHub. Jeśli nie jest ona jeszcze ustawiona globalnie, można ją ustawić lokalnie dla bieżącego repozytorium Git w następujący sposób:


{{Code|lang=text|code=
git config user.name "YOUR_NAME"
git config user.email GITHUB_USERNAME@users.noreply.github.com
}}

Gdzie `"YOUR_NAME"` reprezentuje twoje pełne imię i nazwisko lub pseudonim, używane do identyfikacji autora danego commitu, a `GITHUB_USERNAME` oznacza nazwę twojego konta na GitHubie.

## Repozytoria zdalne 

Proszę przeczytać [Jaka jest różnica między origin a upstream na GitHubie?](https://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-on-github#9257901) *(Stackoverflow)*, aby pomóc w zrozumieniu różnicy między `origin` a `upstream` w kontekście Git. Ta sekcja wyjaśnia, jak ustawić właściwe repozytoria dla rozwoju. Zasadniczo:

-    `origin`to Twój osobisty fork oficjalnego repozytorium FreeCAD, czyli {{URL|https://github.com/GITHUB_USERNAME/FreeCAD}}

-    `upstream`to oficjalne repozytorium FreeCAD, czyli {{URL|https://github.com/FreeCAD/FreeCAD}}.

To rozróżnienie jest ważne, ponieważ najpierw należy napisać kod we własnej kopii repozytorium, a dopiero potem przesłać zmiany do oficjalnego repozytorium.

W oparciu o powyższe informacje można skonfigurować środowisko programistyczne Git na dwa sposoby:

-   Pierwsza metoda: rozwidlenie na GitHubie i sklonowanie go lokalnie.
-   Druga metoda: sklonuj FreeCAD bezpośrednio na lokalnym komputerze i dostosuj zdalne serwery.

Zalecamy pierwszą metodę, ponieważ jest ona o jeden krok krótsza.


<div class="mw-collapsible mw-collapsed toccolours">

#### Metoda pierwsza: Rozwidlenie na GitHub i sklonowanie swojego widelca lokalnie 


<div class="mw-collapsible-content">

Najpierw rozwidlisz repozytorium FreeCAD na GitHubie, następnie sklonujesz to osobiste rozwidlenie na swój komputer, a na koniec ustawisz repozytorium `upstream`.

-   [Zaloguj się](https://github.com/join) na swoje konto GitHub.
-   Przejdź do oficjalnego repozytorium FreeCAD: {{URL|https://github.com/FreeCAD/FreeCAD}}
-   W prawym górnym rogu strony naciśnij przycisk \"Fork\". Spowoduje to utworzenie osobistej kopii repozytorium FreeCAD pod Twoją nazwą użytkownika GitHub: {{URLn|https://github.com/GITHUB_USERNAME/FreeCAD}}
-   Na swoim komputerze sklonuj nowo utworzony fork programu FreeCAD. Zostanie on utworzony wewnątrz katalogu `freecad-source`.


{{Code|lang=text|code=
git clone https://github.com/GITHUB_USERNAME/FreeCAD.git freecad-source
}}

-   Po zakończeniu pobierania wprowadź nowy katalog źródłowy i ustaw repozytorium `upstream`.


{{Code|lang=text|code=
cd  freecad-source
git remote add upstream https://github.com/FreeCAD/FreeCAD.git
}}

-   Potwierdź swoje zdalne repozytoria za pomocą `git remote -v`; rezultat powinien być podobny do tego


{{Code|lang=text|code=
origin  https://github.com/GITHUB_USERNAME/FreeCAD.git (fetch)
origin  https://github.com/GITHUB_USERNAME/FreeCAD.git (push)
upstream    https://github.com/FreeCAD/FreeCAD.git (fetch)
upstream    https://github.com/FreeCAD/FreeCAD.git (push)
}}

-   Teraz można rozpocząć prace rozwojowe.


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">

#### Metoda druga: Sklonuj FreeCAD bezpośrednio na swój komputer lokalny 


<div class="mw-collapsible-content">

Najpierw rozwidlisz repozytorium FreeCAD w serwisie GitHub, jednak oryginalne repozytorium FreeCAD sklonujesz na swój komputer lokalny, a następnie zmienisz swoje zdalne adresy za pomocą terminala.

-   [Zaloguj się](https://github.com/join) na swoje konto GitHub.
-   Przejdź do oficjalnego repozytorium FreeCAD: {{URL|https://github.com/FreeCAD/FreeCAD}}
-   W prawym górnym rogu strony naciśnij przycisk \"Fork\". Spowoduje to utworzenie osobistej kopii repozytorium FreeCAD pod Twoją nazwą użytkownika GitHub: {{URLn|https://github.com/GITHUB_USERNAME/FreeCAD}}
-   Sklonuj oryginalne repozytorium FreeCAD. Zostanie ono utworzone wewnątrz katalogu `freecad-source`.


{{Code|lang=text|code=
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
}}

-   Po zakończeniu pobierania należy wejść do nowego katalogu źródłowego i ustawić `origin` repozytorium.


{{Code|lang=text|code=
cd freecad-source
git remote add origin https://github.com/GITHUB_USERNAME/FreeCAD.git
}}

-   Następnie należy skonfigurować repozytorium `upstream`.


{{Code|lang=text|code=
git remote add upstream https://github.com/FreeCAD/FreeCAD.git
}}

-   Potwierdź swoje zdalne repozytoria za pomocą `git remote -v`; rezultat powinien być podobny do tego


{{Code|lang=text|code=
origin  https://github.com/GITHUB_USERNAME/FreeCAD.git (fetch)
origin  https://github.com/GITHUB_USERNAME/FreeCAD.git (push)
upstream    https://github.com/FreeCAD/FreeCAD.git (fetch)
upstream    https://github.com/FreeCAD/FreeCAD.git (push)
}}

-   Teraz można rozpocząć prace rozwojowe.


</div>


</div>

Jeśli z jakiegoś powodu zdalne repozytoria istnieją, ale wskazują na niewłaściwy adres, możesz naprawić sytuację, zmieniając nazwę zdalnego repozytorium. Na przykład `origin` powinno wskazywać na Twój osobisty fork. Jeśli wskazuje na oryginalne repozytorium FreeCAD, zmień nazwę tego zdalnego na `upstream` i ręcznie dodaj repozytorium `origin`.


{{Code|lang=text|code=
git remote rename origin upstream
git remote add origin https://github.com/GITHUB_USERNAME/FreeCAD.git
git remote -v
}}

Można również wyświetlić więcej informacji za pomocą słowa kluczowego `show`.


{{Code|lang=text|code=
git remote show origin
git remote show upstream
}}

## Proces rozwoju w Git 


**Nigdy nie rozwijaj swojej lokalnej gałęzi ''master''. Zamiast tego należy utworzyć lokalną gałąź do rozwoju, a następnie scalić tę lokalną gałąź z gałęzią główną poprzez pull request. Aby dowiedzieć się więcej, przeczytaj [https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell Git Branching], [https://book.git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging Basic Branching and Merging] oraz [https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project GitHub - Contributing to a project].**

<img alt="" src=images/FreeCAD_git_branches_workflow.svg  style="width:800px;"> 
*Ogólny tok pracy nad kodem programu FreeCAD przy użyciu `git*. Główne repozytorium jest rozwidlane online i klonowane na komputer offline ''(0)''; nowe gałęzie ''(1)'' są używane do wprowadzania lokalnych zmian i uzupełnień do kodu ''(2)''. Gałęzie są przebudowywane do najnowszego kodu online ''(3)'', a następnie są wypychane do zdalnego repozytorium ''(4)''. Następnie tworzone jest żądanie ściągnięcia w celu połączenia kodu z głównym repozytorium (5). Następnie klon osobisty jest aktualizowany nowym kodem głównym ''(a)''. Ten zaktualizowany kod główny jest również przesyłany do zdalnego repozytorium ''(b)'', aby mieć ten sam kod zarówno w trybie online, jak i offline.`

### Odgałęzienia

Zamiast pracować na głównej wersji kodu, najlepsze praktyki Git zalecają tworzenie nowej gałęzi za każdym razem, gdy chcesz pracować nad nową funkcjonalnością. Gałęzie są niedrogie, nie kopiują całego drzewa źródłowego, a jedynie tworzą punkt w czasie, na którym będziesz pisał kod. W ten sposób gałęzie pomagają oddzielić prace w toku od głównego kodu.

Korzystanie z nowej gałęzi odbywa się w dwóch etapach: najpierw należy utworzyć gałąź, a następnie przejść do niej:


{{Code|lang=text|code=
git branch myNewBranch
git checkout myNewBranch
}}

Alternatywnie można wykonać obie czynności za pomocą jednej instrukcji:


{{Code|lang=text|code=
git checkout -b myNewBranch
}}

Teraz możesz zmieniać gałęzie za pomocą `checkout`, kiedy tylko chcesz nad nimi pracować. Aby zobaczyć gałęzie w projekcie i bieżącą gałąź, użyj samej operacji `branch` lub dodaj `-v` lub `-vv`, aby uzyskać więcej informacji:


{{Code|lang=text|code=
git branch
git branch -vv
}}

Po wprowadzeniu zmian i ich zatwierdzeniu użyj operacji `log` z następującymi opcjami, aby wyświetlić gałęzie


{{Code|lang=text|code=
git log --oneline --decorate --graph --all
}}

### Committing

Gdy już znajdziesz się w nowej gałęzi, edytuj wybrane pliki źródłowe za pomocą edytora tekstu. Aby sprawdzić, które pliki zostały zmodyfikowane, użyj operacji `status` i `diff`. Kiedy będziesz zadowolony z wprowadzonych zmian, zapisz je za pomocą operacji `commit`:


{{Code|lang=text|code=
git status
git diff
git commit -a
}}

W przeciwieństwie do SVN, musisz wskazać, które pliki mają być commitowane. Użyj opcji `-a`, aby zapisać zmiany we wszystkich plikach, które zostały zmienione. Otworzy się edytor tekstu, na przykład `nano` lub `vim`, aby umożliwić napisanie wiadomości do zgłoszenia commit.

Ewentualnie dodaj wiadomość w samym zgłoszeniu commit:


{{Code|lang=text|code=
git commit -a -m "Fix the bug in the clone function."
}}

Jeśli tworzysz nowe pliki lub katalogi, musisz najpierw użyć operacji `add`, aby dodać je do lokalnego repozytorium przed zatwierdzeniem zmian.


{{Code|lang=text|code=
git add path
git commit -a
}}

Gdzie `path` może być dowolnym katalogiem lub plikiem.

### Pisanie dobrych komunikatów zgłoszeń commit 

Powinieneś starać się pracować małymi krokami, czyli często zatwierdzać zmiany po wprowadzeniu niewielkiego dodatku do swojego kodu. Jeśli nie potrafisz streścić swoich zmian w jednym zdaniu, to prawdopodobnie minęło zbyt dużo czasu od wykonania zgłoszenia commit.

W przypadku dużych zmian ważne jest, abyś miał pomocne i przydatne opisy swojej pracy. FreeCAD przyjął format wspomniany w książce [Pro Git](https://git-scm.com/book/en/v2), który składa się z krótkiej wiadomości, a następnie większego akapitu opisowego.


{{Code|lang=text|code=
Krótkie (nie więcej niż 50 znaków) podsumowanie zmian
 
 W razie potrzeby bardziej szczegółowy tekst objaśniający. Należy go zawinąć do około 72
 znaków lub więcej. W niektórych kontekstach pierwszy wiersz jest traktowany jako
 temat wiadomości e-mail, a pozostały tekst jako treść.  Pusta
 pusta linia oddzielająca podsumowanie od treści ma kluczowe znaczenie (chyba że pominiesz
 ciała); narzędzia takie jak rebase mogą się pomylić, jeśli uruchomisz
 te dwa elementy razem.
 
 Kolejne akapity znajdują się po pustych liniach. 
 
  - Punkty kuliste też są w porządku
 
  - Zazwyczaj w wypunktowaniu stosuje się myślnik lub gwiazdkę, poprzedzone
    pojedynczą spacją, a pomiędzy nimi znajdują się puste linie, ale konwencje są tu różne

}}

Jeśli wykonujesz wiele powiązanych prac w gałęzi, powinieneś wykonać wiele małych commitów *(zobacz post na forum [1](https://forum.freecadweb.org/viewtopic.php?f=10&t=2062&p=14887#p14886))*. Gdy chcesz scalić te zmiany w gałęzi głównej, powinieneś wydać polecenie:


{{Code|lang=text|code=
git log master..myNewBranch
}}

aby zobaczyć poszczególne komunikaty zgłoszeń commit. Dzięki temu można napisać wysokiej jakości komunikat podczas wykonywania scalania.

Kiedy łączysz się z wersją master, użyj opcji `--squash` i wykonaj commit z wysokiej jakości komunikatem commit. To pozwoli ci być bardzo liberalnym w swoich zgłoszeniach commit i pomoże zapewnić dobry poziom szczegółowości w komunikatach commit bez tak wielu odrębnych opisów.

### Squashing commits 

Squashing odnosi się do procesu łączenia różnych kolejnych commitów w jeden. Może to być pożądane, jeśli wykonałeś wiele małych commitów, które chcesz przedstawić jako jeden commit, na przykład przy zmianie pojedynczej zmiennej, poprawianiu błędów ortograficznych i poprawianiu odstępów w kodzie. Powinieneś zgnieść tylko małe commit\'y do pojedynczego pliku. Duże zmiany w kodzie w wielu plikach powinny zawierać pełną historię commit\'ów.

Dzięki `git log --oneline` możesz zobaczyć wiele commitów po kolei, z najnowszym na górze. W tym przykładzie, zaczynając od \"cechy A\", powstało wiele commitów implementujących \"cechę B\"; chcielibyśmy zebrać wszystkie commity należące do \"cechy B\" w jeden.


{{Code|lang=text|code=
871adb OK, feature B is fully implemented
1c3317 Whoops, it is not ready yet...
87871a I'm almost ready!
643d0e Code cleanup
af2581 Fix this and that
4e9baa Good implementation
d94e78 Prepare the module for feature B
6394da Feature A
}}

Użyj operacji `rebase` z opcją `--interactive` lub `-i`, aby wybrać różne commity i je usunąć. Użyj hash commitu znajdującego się tuż przed pierwszym, który chcesz usunąć, w tym przypadku tego odpowiadającego \"cechom A\".


{{Code|lang=text|code=
git rebase -i 6394da
}}

*(WSKAZÓWKA: Jeśli wiesz, ile commitów chcesz edytować, możesz użyć `git rebase -i HEAD~n`, aby pracować na ostatnich `n` commitach)*.

Edytor wiersza poleceń, taki jak `nano` lub `vim`, otworzy się, aby ponownie wyświetlić listę commitów, teraz ze starszym commitem na górze. Przed każdym commitem pojawi się słowo `pick`. Usuń słowo `pick` i wpisz w jego miejsce słowo `squash` lub po prostu literę `s`, z wyjątkiem pierwszego wpisu; ten commit jest najstarszy, więc wszystkie następne zostaną w nim zebrane.


{{Code|lang=text|code=
pick d94e78 Prepare the module for feature B
s 4e9baa Good implementation
s af2581 Fix this and that
s 643d0e Code cleanup
s 87871a I'm almost ready!
s 1c3317 Whoops, it is not ready yet...
s 871adb OK, feature B is fully implemented
}}

Zapisz plik i zamknij edytor.

Edytor zostanie ponownie otwarty. Teraz możesz dodać dłuższy komunikat opisujący wszystkie zmiany, tak jakby były pojedynczym commitem. Zapisz plik i ponownie zamknij edytor. W ten sposób zakończysz łączenie tych commitów w jeden, z nowym komunikatem commit, który napisałeś.

Możesz użyć `git log --oneline` ponownie, aby zaobserwować historię nowych zgłoszeń commit. W tym przypadku pojawi się tylko pojedynczy commit dla \"cechy B\", na wierzchu niezmodyfikowanego commitu dla \"cechy A\".


{{Code|lang=text|code=
c83d67 OK, feature B is fully implemented now, with proper module setup, and clean code.
6394da Feature A
}}

Podczas kodowania dla FreeCAD prosimy, abyś rozpoczynał każdą wiadomość commit od modułu, którego dotyczy. Na przykład wiadomość commit dla zmiany w Szkicowniku może wyglądać następująco:

    Sketcher: make straight lines curve a bit

    Straight lines are sort of ugly, so this commit adds a little bit of curvature to them, so
    they are more visually pleasing. They also sparkle some, and change colors over time.

    Fixes bug #1234.

Twój PR będzie ułatwiał przeglądanie i szybciej zostanie scalony, jeśli będziesz uważał, aby używać rebase do strukturyzacji i opisywania swoich zgłoszeń commit przed wysłaniem.

### Przesłanie pracy do repozytorium GitHub 

Gałęzie lokalne na Twoim komputerze nie są automatycznie synchronizowane ze zdalnymi serwerami, które określiłeś jako `origin` lub `upstream` ( patrz [Remote repositories](#Remote_repositories.md)). Musisz jawnie wysłać gałęzie na zdalne serwery, do których wymagany jest dostęp z prawem zapisu. Gdy to zrobisz, gałęzie staną się publiczne i dostępne do wglądu dla innych programistów.

W przypadku programu FreeCAD powinieneś przesłać swoją lokalną gałąź do zdalnego repozytorium `origin`, czyli do {{URLn|https://github.com/GITHUB_USERNAME/FreeCAD}}. Musisz podać swoją nazwę użytkownika i hasło za każdym razem, gdy wykonujesz push, chyba że ustawiłeś [Buforowanie poświadczeń](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage#_credential_caching). Przeczytaj [Pushing commit do zdalnego repozytorium](https://help.github.com/articles/pushing-to-a-remote/), aby uzyskać więcej informacji.


{{Code|lang=text|code=
git push origin myNewBranch
}}

Podczas pracy z pojedynczą gałęzią może zajść potrzeba wielokrotnego, interaktywnego przekształcania, usuwania i poprawiania zgłoszeń commit. W takim przypadku historia oddziału *(branch)* nie będzie prosta i nie będzie można jej przesłać do zdalnego repozytorium. Może pojawić się komunikat taki jak poniżej, mówiący, że nie jest możliwe wykonanie pchnięcia \"fast-forward\".


{{Code|lang=text|code=
error: failed to push some refs to 'https://github.com/USER/FreeCAD.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
}}

Aby ostatecznie przepchnąć swoją gałąź do zdalnego repozytorium, musisz wykonać \"force push\". Spowoduje to całkowite nadpisanie zdalnej gałęzi aktualną gałęzią, którą mamy w trybie offline.


{{Code|lang=text|code=
git push -f origin myNewBranch
}}

Zwykły programista nie ma dostępu do zapisu w repozytorium `upstream` {{URL|https://github.com/FreeCAD/FreeCAD}}, dlatego nigdy nie należy umieszczać kodu na tym zdalnym serwerze.

### Rebasing from upstream 

Podczas gdy Ty pracujesz nad swoją własną gałęzią, oficjalny kod programu FreeCAD \"idzie do przodu\" dzięki zgłoszeniom commit innych deweloperów i w ten sposób zaczyna odbiegać od kodu, który masz w swoim osobistym forku.

          .A origin/myNewBranch
         / 
    oZ FreeCAD upstream/master

Dlatego, gdy jesteś gotowy do połączenia swojego oddziału z głównym repozytorium FreeCAD, musisz \"przebudować\" swoją kopię repozytorium, tak aby była jak najbardziej zbliżona do oficjalnego repozytorium. Zapoznaj się z treścią [Git Branching - Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing), aby uzyskać więcej informacji.


{{Code|lang=text|code=
git checkout myNewBranch
git pull --rebase upstream master
}}

Spowoduje to pobranie kodu z gałęzi `master` repozytorium `upstream` (oficjalne źródło programu FreeCAD) i scalenie go z Twoją bieżącą gałęzią (`myNewBranch`), tak aby Twoje zmiany znalazły się na wierzchu najnowszego oficjalnego kodu. Jeśli nikt nie zmodyfikował tych samych plików, co Ty, to scalenie przebiegnie bez problemów. Jeśli niektóre pliki zostały zmienione w tym samym czasie przez różne osoby, może istnieć konflikt, który należy rozwiązać.

                      .A' origin/myNewBranch
                     /
    oZ FreeCAD upstream/master

Podsumowując, trzeba być w odpowiedniej gałęzi, przebudować kod do wykonania upstreamu, a następnie wykonać push.


{{Code|lang=text|code=
git checkout myNewBranch
git pull --rebase upstream master
git push origin myNewBranch
}}

Operacja `pull` jest równoważna operacji `fetch`, po której następuje `merge`. Gdy użyta jest opcja `--rebase`, zamiast prostego `merge` wykonywana jest operacja `rebase`.


{{Code|lang=text|code=
git pull upstream

git fetch upstream
git merge FETCH_HEAD
}}


{{Code|lang=text|code=
git pull --rebase upstream master

git fetch upstream
git rebase master
}}

### Scalanie gałęzi (pull request) 

Po lokalnym wprowadzeniu zmian, przebudowaniu swojej gałęzi z repozytorium upstream i umieszczeniu swojej gałęzi online, możesz zainicjować \"pull request\". Prośba [pull request](https://help.github.com/articles/about-pull-requests/) mówi administratorom oficjalnego repozytorium FreeCADa, że chcesz połączyć nowy kod w swojej gałęzi z oficjalnym kodem.

Podsumowując, proces rozwoju wygląda następująco:

1.  Utwórz fork programu FreeCAD i uzyskaj lokalną kopię tego forka.
2.  Utwórz gałąź na swoim rozwidleniu i zmień na tę gałąź.
3.  Koduj! Udostępniaj tyle lub tak mało, jak chcesz, pisząc dobre komunikaty commit, aby śledzić, co robisz.
4.  Gdy będziesz zadowolony ze swojej pracy, użyj `git rebase -i HEAD~n` *(gdzie n jest całkowitą liczbą zgłoszeń commit, które wykonałeś)*, aby zebrać swoje commity w logiczny zestaw z dobrymi komunikatami do zgłoszeń commit *(każdy komunikat powinien zaczynać się od nazwy modułu, którego dotyczy, np. \"Sketcher: make straight lines curve bit\")*.
5.  Użyj GitHuba, aby przesłać swój kod jako \"Pull Request (PR)\", jak opisano poniżej.

Gdy tylko umieścisz kod w swoim repozytorium `origin` {{URLn|https://github.com/GITHUB_USERNAME/FreeCAD}}, GitHub da Ci możliwość porównania i utworzenia pull requestu do repozytorium `upstream`. Po naciśnięciu przycisku **Compare & pull request** otworzysz interfejs, który pozwoli Ci wybrać, które repozytorium jest \"bazą\", czyli celem scalania, a które \"głową\", czyli Twoim dodatkowym kodem. System szybko sprawdzi, czy nie ma konfliktów z plikami, które zmodyfikowałeś. Jeśli pracowałeś nad plikami, których nikt nie dotykał, twoja gałąź będzie mogła zostać scalona bez problemów.

GitHub wyświetli edytor tekstu, w którym można napisać wiadomość dokumentującą zmiany: edytor ten będzie wstępnie wypełniony wiadomością powitalną (którą można usunąć), listą kontrolną (którą należy przejrzeć) oraz przypomnieniem o konieczności udokumentowania zmiany na wiki, gdy zostanie zaakceptowana. Aby skorzystać z listy kontrolnej, przejdź przez każdy element po kolei i zmień `[ ]` na `[X]`, aby zaznaczyć, że wykonałeś dany krok. GitHub wyświetli także liczbę commitów w Twojej gałęzi, liczbę plików, które zostały zmodyfikowane, oraz widok pokazujący różnice między \"bazą\" a \"głową\", aby każdy mógł natychmiast zobaczyć, jakie są Twoje zamierzone modyfikacje. Sprawdź dwukrotnie, czy nie ma tam takich rzeczy, jak zabłąkane puste linie, których nie chciałeś dodać, lub ogromne zmiany formatowania, które IDE postanowiło wprowadzić za Twoimi plecami.


{{Code|lang=text|code=
base repository: FreeCAD/FreeCAD    base: master  <  head repository: GITHUB_USERNAME/FreeCAD    compare: myNewBranch

Able to merge. These branches can be automatically merged.
}}

Kliknij **Create pull request**, aby kontynuować. Pojawi się komunikat informujący, że kod musi zostać sprawdzony. Jest to system, który automatycznie kompiluje program FreeCAD i uruchamia testy jednostkowe. Jeśli testy przejdą pomyślnie, pull request będzie miał większe szanse na połączenie z głównym kodem, w przeciwnym razie zostanie sporządzony raport wskazujący napotkane błędy. Zobacz [FreeCAD pull requests](https://travis-ci.org/FreeCAD/FreeCAD/pull_requests).

    Some checks haven’t completed yet

    * continuous-integration/travis-ci/pr Pending — The Travis CI build is in progress  |Required|

Jeśli testy zakończą się powodzeniem, pojawi się komunikat taki jak poniżej:

All checks have passed

    * continuous-integration/travis-ci/pr — The Travis CI build passed  |Required|

Ta gałąź nie ma konfliktów z gałęzią podstawową Tylko osoby z prawem zapisu do tego repozytorium mogą łączyć zgłoszenia pull request.

Teraz musisz poczekać, aż administratorzy połączą Twoją gałąź. Zostaniesz o tym poinformowany.


{{Code|lang=text|code=
Pull request successfully merged and closed

You’re all set — the GITHUB_USERNAME:myNewBranch branch can be safely deleted.
If you wish, you can also delete your fork of FreeCAD/FreeCAD.
}}

Jeśli chcesz, możesz usunąć gałąź, która została właśnie scalona, a nawet cały swój fork programu FreeCAD, ponieważ Twój własny kod jest już dołączony na końcu gałęzi głównej.


{{Code|lang=text|code=
oZA' FreeCAD upstream/master
}}


**Uwaga:**

możesz kontynuować pracę (`git commit -a`) na tej samej gałęzi, czekając na zatwierdzenie scalenia. Jeśli ponownie wykonasz `git push`, drugi commit scalenia zostanie umieszczony w kolejce w tym samym żądaniu ściągnięcia, a kolejny automatyczny test zostanie wykonany. Oznacza to, że podczas gdy twoje scalenia nie są jeszcze zatwierdzone przez administratorów, możesz nadal wysyłać zmiany do swojego repozytorium `origin`, a to spowoduje umieszczenie tych zgłoszeń commit w kolejce tego samego żądania wyciągnięcia do repozytorium `upstream`. Używanie pojedynczego żądania pull do kolejkowania wielu pojedynczych zgłoszeń commit jest często pożądane w przypadku małych zmian. W przypadku dużych zmian w kodzie źródłowym, należy utworzyć inną gałąź, rozwijać w niej swoje funkcje, a następnie wysłać osobne żądanie pull request dla tej gałęzi.

Przetłumaczono z www.DeepL.com/Translator (wersja darmowa)

Interfejs pull request może być używany za każdym razem, gdy chcesz przesłać kod z własnego repozytorium do innego repozytorium w GitHubie. Można go również używać do scalania kodu w odwrotnym kierunku, z gałęzi innych osób do własnej, a nawet pomiędzy własnymi gałęziami. W tym ostatnim przypadku, ponieważ jesteś właścicielem gałęzi, możesz od razu zatwierdzić scalanie.


{{Code|lang=text|code=
base repository: SomeProject/Some_Software  base: master       <  head repository: GITHUB_USERNAME/Some_Software  compare: add_new_functions
base repository: GITHUB_USERNAME/FreeCAD    base: myNewBranch  <  head repository: FreeCAD/FreeCAD                compare: master
base repository: GITHUB_USERNAME/FreeCAD    base: myNewBranch  <  head repository: GITHUB_USERNAME/FreeCAD        compare: fix-many-bugs-branch
}}

### Utrzymywanie aktualnego repozytorium GitHub 

Po rozwidleniu FreeCAD, Twoje osobiste repozytorium istnieje niezależnie od oryginalnego. Kiedy oryginalne repozytorium będzie miało nowe zgłoszenia commit, GitHub poinformuje Cię, że Twoje osobiste repozytorium jest opóźnione pod względem liczby zgłoszeń commit:


{{Code|lang=text|code=
This branch is 5 commits behind FreeCAD:master.
}}

W podobny sposób, jeśli utworzyłeś gałąź rozwojową z nowym kodem, GitHub poinformuje Cię, że ta gałąź wyprzedza Cię w liczbie zgłoszeń commit. To znaczy, że ta gałąź zawiera zmiany, które nie zostały jeszcze scalone z oficjalnym repozytorium FreeCAD:


{{Code|lang=text|code=
This branch is 3 commits ahead of FreeCAD:master.
}}

Podczas rozwijania możliwe są oba przypadki, ponieważ Twoja własna gałąź może nie zawierać zgłoszeń commit innych deweloperów, ale zawierać nowe, napisane przez Ciebie:


{{Code|lang=text|code=
This branch is 2 commits ahead, 14 commits behind FreeCAD:master. 
}}

Podczas tworzenia kodu zaleca się, abyś zmienił bazę gałęzi, w której aktualnie pracujesz, ponieważ dzięki temu Twoja gałąź będzie zawsze wyprzedzać kod główny FreeCAD.

Jeśli chodzi o twoją oryginalną gałąź `master`, to nigdy nie będzie ona automatycznie aktualizowana przez GitHub. Musisz o to zadbać samodzielnie. Przełącz się na gałąź `master`, a następnie `pull` z `upstream` *(co spowoduje pobranie `fetch` i `merge`)*, a następnie przepchnij zaktualizowaną gałąź `master` do swojego zdalnego repozytorium `origin`.


{{Code|lang=text|code=
git checkout master
git pull upstream master
git push origin master
}}

Po wykonaniu tych czynności GitHub poinformuje Cię, że jesteś zsynchronizowany z repozytorium `upstream`.


{{Code|lang=text|code=
This branch is even with FreeCAD:master. 
}}

Teraz, gdy twój `master` jest aktualny, możesz zdecydować się na przejście do niego i usunąć inną gałąź, której używałeś wcześniej do rozwijania funkcji.


{{Code|lang=text|code=
git checkout master
git branch -d myNewBranch
}}

Aby usunąć gałąź w zdalnym repozytorium `origin`, można użyć operacji `push`. Zwykle pcha się lokalną gałąź. Spowoduje to utworzenie zdalnej gałęzi o tej samej nazwie co lokalna.


{{Code|lang=text|code=
git push origin myNewBranch
}}

Jeśli jednak użyjesz zapisu `local_name:remote_name`, lokalna gałąź zostanie utworzona w zdalnym repozytorium pod inną nazwą:


{{Code|lang=text|code=
git push origin myNewBranch:someRemoteBranch
}}

Dlatego można usunąć zdalną gałąź, przesuwając pustą gałąź lokalną:


{{Code|lang=text|code=
git push origin :myNewBranch
git push origin :someRemoteBranch
}}

Teraz, gdy masz już tylko aktualny `master`, możesz utworzyć nową gałąź i powtórzyć kroki zmiany plików, zgłoszenia commit, push, wysłania pull request, scalenia i aktualizacji.


{{Code|lang=text|code=
git checkout master
git checkout -b anotherBranch
}}

Jeśli nie chcesz usuwać swojej już niestandardowej gałęzi, możesz wymusić jej aktualizację tak, aby była równa zaktualizowanej gałęzi `master`; następnie możesz zrobić z nią, co tylko chcesz, włączając w to dodawanie kolejnych zgłoszeń commit i wypychanie jej do zdalnego repozytorium `origin`.


{{Code|lang=text|code=
git checkout myNewBranch
git reset --hard master
git push -f origin myNewBranch
}}

Takie twarde resetowanie gałęzi zwykle nie jest potrzebne. W większości przypadków należy wykonać następujące czynności: utworzenie nowej gałęzi, wprowadzenie zmian, przepchnięcie tych zmian, scalenie gałęzi, a następnie usunięcie gałęzi.

## Zaawansowane operacje Git 

### Wyszukiwanie

Oto kilka przydatnych narzędzi, które pomogą Ci znaleźć to, czego szukasz:

#### Wyszukiwanie plików według nazw 

Użyj `git ls-files`, aby przeszukać repozytorium w poszukiwaniu plików, które zawierają w nazwie określony ciąg znaków. Poniższy przykład zwróci wszystkie przypadki plików, które zawierają w nazwie ciąg \'dxf\'.


{{Code|lang=text|code=
git ls-files *dxf*
}}

#### Wyszukiwanie ciągu znaków 

Użyj `git grep`, aby przeszukać repozytorium w poszukiwaniu plików, które zawierają określony ciąg znaków w samych plikach. Poniższy przykład zwróci wszystkie wystąpienia plików, które zawierają \"dxf\" w każdym z nich.


{{Code|lang=text|code=
git grep dxf
}}

### Rozwiązywanie konfliktów scalania 

Łączenie gałęzi za pomocą `git merge`, lub zmiana lokalizacji gałęzi za pomocą `git rebase`, może czasami powodować konflikty, ponieważ pliki mogły być modyfikowane przez innego autora w tym samym czasie. Jeśli tak się stanie, powinieneś zobaczyć zmiany obu stron, autora i swoje własne, a następnie podjąć decyzję, jak uwzględnić oba zestawy zmian w najlepszy możliwy sposób. Jest to zwykle proces ręczny, którego nie da się zautomatyzować; programista musi zrozumieć kod i zdecydować, jaki kod przenieść, przerobić lub usunąć, aby rozwiązać konflikt.

Po wystąpieniu konfliktu może zostać wyświetlony komunikat podobny do tego.


{{Code|lang=text|code=
CONFLICT (content): Merge conflict in src/Mod/source_code.py
error: Failed to merge in the changes.
Patch failed at 1234 Some commit message when editing source_code.py
}}

Jeśli dla projektu Git jest zainstalowane i skonfigurowane specjalistyczne narzędzie diff, na przykład program [Meld](https://wiki.gnome.org/Apps/Meld) firmy Gnome, konflikt można zbadać i rozwiązać za pomocą operacji `mergetool`.


{{Code|lang=text|code=
git mergetool
}}

Narzędzie Scalanie zwykle wyświetla trzy kolumny; dwie kolumny po bokach wyświetlają dwa sprzeczne pliki, natomiast kolumna pośrodku wyświetla nowy kod, który zostanie zapisany i ostatecznie zatwierdzony. Dlatego też środkowa kolumna powinna być edytowana w taki sposób, aby scalała kod z obu kolumn bocznych. Po rozwiązaniu konfliktu i zapisaniu nowego kodu źródłowego (kolumna środkowa) można zamknąć narzędzie Meld. Następnie można kontynuować operację `merge` lub `rebase`.


{{Code|lang=text|code=
git merge --continue
git rebase --continue
}}

Więcej informacji o scalaniu i rozwiązywaniu konfliktów można znaleźć na stronach:

-   [Jak są przedstawiane konflikty scalania](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented) z `git merge`.
-   [Podstawowe konflikty scalania](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts) i [Narzędzia Git - Zaawansowane scalanie](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging).
-   [Rozwiązywanie konfliktu scalania za pomocą wiersza poleceń](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/).
-   [Zewnętrzne narzędzia do scalania i dyfuzji](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_external_merge_tools), których można użyć po napotkaniu konfliktu w programie Git.

### Sprawdzanie zmian 

Sprawdź historię pojedynczego pliku dla różnych zgłoszeń commit za pomocą operacji `log`:


{{Code|lang=text|code=
git log --patch path
}}

Gdzie `path` może być dowolnym katalogiem lub plikiem. Zamiast `--patch` można również użyć skrótów `-p` lub `-u`.

### Sprawdzanie zmian między dwoma gałęziami 

Sprawdź zmiany między dwiema gałęziami za pomocą operacji `log` i `diff` z podaniem nazw gałęzi:


{{Code|lang=text|code=
git log master..myBranch
git diff master..myBranch
}}

Operacja `log` pokazuje zgłoszenia commit, natomiast `diff` pokazuje rzeczywiste zmiany w plikach.

### Resetowanie plików i katalogów 

Jeśli przypadkowo wprowadzono modyfikacje w pliku lub katalogu, może być konieczne całkowite odwrócenie tych zmian, aby uzyskać poprzedni stan kodu źródłowego.

Można to szybko wykonać za pomocą operacji `checkout`:


{{Code|lang=text|code=
git checkout path
git checkout .
}}

Spowoduje to przywrócenie `path` *(plików lub katalogów)* do stanu z początku gałęzi, odrzucając zmiany, które nie zostały zatwierdzone. Jeśli `path` jest pojedynczą kropką `.`, to przywróci wszystkie pliki w bieżącym katalogu.

Jeśli przez przypadek dodano pliki i katalogi, można użyć operacji `clean`:


{{Code|lang=text|code=
git clean -df
}}

Spowoduje to wymuszone usunięcie wszystkich plików i katalogów (`-df`), które nie są śledzone przez repozytorium, czyli takich, które nie zostały wcześniej dołączone za pomocą operacji `add`.

Aby całkowicie zresetować repozytorium, tracąc wszystkie niezaangażowane modyfikacje, należy użyć operacji `reset`:


{{Code|lang=text|code=
git fetch
git reset --hard FETCH_HEAD
}}

Gdzie `FETCH_HEAD` jest wierzchołkiem repozytorium `upstream`. Można też użyć innego zgłoszenia commit.

Operacja `revert` również odwraca zmiany. Jednak to polecenie robi to przez dodanie kolejnego zgłoszenia commit do historii. W wielu przypadkach nie jest to pożądane.

### Obcinanie starych gałęzi 

Jeśli wysłałeś wiele gałęzi do repozytorium `upstream`, możesz chcieć usunąć te gałęzie ze swojego lokalnego systemu, ponieważ zostały już scalone. Gałąź w repozytorium `origin` online może zostać usunięta natychmiast po scaleniu. Następnie można usunąć lokalne odwołania do tej gałęzi, używając opcji `--prune` lub `prune` w operacjach `fetch` i `remote`.


{{Code|lang=text|code=
git fetch --prune origin
git remote prune origin
}}

Na koniec można usunąć gałęzie lokalnie:


{{Code|lang=text|code=
git branch -D myBranch
}}

Dobrą praktyką jest również odśmiecanie repozytorium po pewnym czasie za pomocą operacji `gc`. Spowoduje to wyczyszczenie niepotrzebnych plików i skompresowanie lokalnych rewizji plików, aby zoptymalizować wykorzystanie lokalnego dysku w repozytorium.


{{Code|lang=text|code=
git gc
}}

### Praca z łatkami 

Chociaż Git pozwala na łączenie różnych gałęzi kodu za pomocą `git merge` *(na swoim komputerze)* lub pull request *(w zdalnym repozytorium)*, to jednak zdarzają się sytuacje, w których pożądane może być utworzenie tradycyjnej \"łatki\" *(patch)*, którą można wysłać jako załącznik przez e-mail. Poniższy przepływ pracy wyjaśnia, jak to zrobić.

#### Tworzenie łatek 

-   Nowy kod powinien być rozwijany w gałęzi dodatkowej repozytorium, a nie w gałęzi głównej. Dlatego pierwszym krokiem jest upewnienie się, że znajdujesz się we właściwej gałęzi.


{{Code|lang=text|code=
git branch -v
git checkout myBranch
}}

-   Teraz użyj `git format-patch` względem gałęzi master i użyj opcji `--stdout`, aby przekierować wynik na standardowe wyjście. Następnie przekieruj standardowe wyjście do pliku, który dla wygody jest tworzony powyżej katalogu z kodem źródłowym.


{{Code|lang=text|code=
git format-patch master --stdout > ../myCode.patch
}}

-   Inną metodą jest


{{Code|lang=text|code=
git format-patch HEAD^
git format-patch HEAD~1
}}

Liczba znaków nawigacyjnych `^` lub liczba `1` wskazują liczbę zgłoszeń commit, które należy wziąć pod uwagę, czyli `^^` lub `~3` utworzą trzy poprawki dla trzech zgłoszeń commit.


{{Code|lang=text|code=
git format-patch HEAD^
}}

Spowoduje to utworzenie łaty lub serii łat zgodnie z następującą konwencją nazewniczą


{{Code|lang=text|code=
XXXX-commit-message.patch
}}

gdzie `XXXX` jest liczbą od `0000` do `9999`, a komunikat commit stanowi większą część nazwy pliku, np,


{{Code|lang=text|code=
0001-fix-ViewProjMatrix-getProjectionMatrix.patch
}}

#### Stosowanie łatek 

Git może scalać poprawki lub różnice. Aby dowiedzieć się więcej o tym procesie, przeczytaj stronę [Stosowanie poprawek za pomocą Git](https://www.drupal.org/node/1399218).

Jeśli plik z poprawką znajduje się już w systemie, wystarczy go zastosować.


{{Code|lang=text|code=
git apply myCode.patch
}}

Można użyć `curl`, aby pobrać łatę z witryny internetowej, a następnie zastosować ją za pomocą `git`.


{{Code|lang=text|code=
curl -O https://some.website.org/code/myCode.patch
git apply myCode.patch
}}

Dodaj `.diff` lub `.patch` na końcu adresu URL zgłoszenia commit, pull requestu lub widoku porównania na GitHubie, aby na stronie był wyświetlany zwykły widok tekstowy.

-   Zwykła strona zgłoszenia commit: {{URL|https://github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621}}
-   Strona porównania: {{URL|https://github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.diff}}
-   Strona poprawki: {{URL|https://github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.patch}}

Możesz wskazać `curl` na konkretne zgłoszenie commit poprawki w repozytorium i przesłać go bezpośrednio do `git`, aby zastosować poprawkę.

    curl https://github.com/FreeCAD/FreeCAD/commit/c476589652a0f67b544735740e20ff702e8d0621.patch | git apply -

#### Cofanie poprawki 

Podczas stosowania poprawki modyfikuje się niektóre pliki. Modyfikacje te nie są jednak trwałe, dopóki nie zatwierdzisz zmian. Dlatego jeśli chcesz cofnąć poprawkę, skorzystaj z poniższych instrukcji.

Spowoduje to cofnięcie wprowadzonych zmian, jeśli nadal masz dostęp do oryginalnego pliku poprawki.


{{Code|lang=text|code=
git apply -R myCode.patch
}}

Alternatywnie, spowoduje to usunięcie niezaakceptowanych zmian w gałęzi.


{{Code|lang=text|code=
git checkout -f
}}

### Przechowywanie zgłoszeń commit git 

Powiedzmy, że pracujesz nad gałęzią i okazuje się, że dokonujesz pewnych modyfikacji w źródle, które wykraczają poza zakres bieżącej gałęzi. Innymi słowy, te zmiany byłyby lepsze w innej gałęzi, a nie w bieżącej. Polecenie `git stash` może być użyte do tymczasowego przechowywania tych niezaangażowanych zmian lokalnych.


{{Code|lang=text|code=
git stash
}}

Jeśli w przyszłości będziesz chciał użyć tych zgłoszeń commit, możesz je \"wyciągnąć\" ze schowka i umieścić w swojej gałęzi roboczej.


{{Code|lang=text|code=
git stash pop
}}

Jeśli zdecydujesz, że nie lubisz już tych zapisanych zgłoszeń commit, możesz całkowicie usunąć je ze schowka.


{{Code|lang=text|code=
git stash drop
}}

Można wyświetlić listę wielu schowków dla zgłoszeń commit za pomocą:


{{Code|lang=text|code=
git stash list
}}

Aby dowiedzieć się więcej, przeczytaj [Przydatne sztuczki, których możesz nie wiedzieć o schowkach Git](https://medium.freecodecamp.org/useful-tricks-you-might-not-know-about-git-stash-e8a9490f0a1a).

### Sprawdź lokalnie żądania z GitHub 

[Checkout GitHub pull requests locally](https://gist.github.com/piscisaureus/3342247)

### Obciążanie winą 


**Sekcja do ustalenia**

Dodaj zawartość z witryny <https://forum.freecadweb.org/viewtopic.php?f=23&t=55943&p=481483#p481287>

### Bisect


`Git bisect`

Jest to metoda umożliwiająca znalezienie konkretnego zgłoszenia commit, które wprowadziło błąd.

Musisz znaleźć dwa zgłoszenia commit:

-   Prawidłowy commit *(na przykład `abcd`)* przed uszkodzeniem systemu.
-   Nieprawidłowy commit *(na przykład `efgh`)* po uszkodzeniu systemu.

Potem w terminalu wprowadź następujące dane:


{{Code|lang=text|code=
git bisect start
git bisect good abcd
git bisect bad efgh
}}

Wynik: Polecenie `git` sprawdzi spójność między dwoma zgłoszeniami commit.

Następnym krokiem jest zbudowanie i przetestowanie kodu. Jeśli system działa, kontynuuj proces, wpisując:


{{Code|lang=text|code=
git bisect good
}}

Powtórz poprzedni etap budowania kodu i jego testowania.

Jeśli system jest uszkodzony, wpisz:


{{Code|lang=text|code=
git bisect bad
}}

Powtórz poprzednie kroki, stosując `good` lub `bad` w zależności od wyników testów.

W końcu `git` powie ci, że `wxyz` jest pierwszym błędnym commitem.

Na koniec, aby zakończyć proces bisect, wpisz:


{{Code|lang=text|code=
git bisect reset
}}

Uwaga: `git bisect` zajmuje dużo czasu, jeśli obszary poprawne i błędne są odległe od siebie.

## Numer rewizji FreeCAD 

W przeciwieństwie do subversion, które używa kolejnych numerów dla swoich rewizji, Git tworzy [SHA-1 hash values](https://en.wikipedia.org/wiki/SHA-1) z każdym zgłoszeniem commit. Wartość skrótu to długi alfanumeryczny ciąg znaków, który wygląda następująco


{{Code|lang=text|code=
9b3ffef570596e184006287434fba54a4b03ccc3
}}

### Numer ostatniej wersji 

Aby znaleźć numer ostatniej rewizji w konkretnym oddziale, należy użyć operacji `rev-list` z opcją `--count`. Podaj nazwę gałęzi, zdalnego repozytorium, znacznika lub specjalny wskaźnik, taki jak `HEAD`, aby wskazać ostatni commit w tym konkretnym obiekcie.


{{Code|lang=text|code=
git rev-list --count master
git rev-list --count HEAD
git rev-list --count origin
}}

Można też przejrzeć [repozytorium na GitHubie](https://github.com/FreeCAD/FreeCAD) i zapoznać się z liczbą zgłoszeń commit zgłoszonych w danej gałęzi.

### Numer wersji określonego hasha zatwierdzenia commit 

Ponieważ hash jest łańcuchem alfanumerycznym, nie jest zbyt użyteczne określanie, czy dany commit jest starszy czy nowszy od innego hasha. Aby znaleźć numer rewizji określonego hasha, ponownie użyj operacji `rev-list`; dane wejściowe mogą być pełnym hashem lub częściowym hashem, który jest unikalny, zwykle wystarczy pierwsze 7 cyfr.


{{Code|lang=text|code=
git rev-list --count ab1520b872821414c6ce4a15fb85d471ac2a2b03
git rev-list --count 9948ee4
}}

### Hash wersji określonego numeru zatwierdzenia commit 

Jeśli mamy numer commit, powiedzmy 15000, i chcemy znaleźć odpowiadający mu hash, musimy obliczyć liczbę zgłoszdeń commit od tego momentu do ostatniego commitu (`HEAD`). Najpierw należy uzyskać numer ostatniego zgłoszenia commit.


{{Code|lang=text|code=
git rev-list --count HEAD
17465
}}

Następnie należy odjąć numer zgłoszenia commit


{{Code|lang=text|code=
17465 - 15000 = 2465
}}

Następnie użyj operacji `log`, aby wyświetlić wszystkie zatwierdzenia i hashes. Opcja `--skip` przeskakuje różnicę w zatwierdzeniach, które obliczyliśmy, dzięki czemu przechodzimy bezpośrednio do hasza, którego szukamy.


{{Code|lang=text|code=
git log --skip=2465
commit 44c2f19e380e76b567d114a6360519d66f7a9e24
}}

Ponieważ log może pokazywać dwa zbliżone do siebie żądania commit, sprawdź, czy numer jest właściwy. Jeśli jest on przesunięty o jeden, wybierz kolejne żądanie w sekwencji *(przed lub po)* i sprawdź ponownie.


{{Code|lang=text|code=
git rev-list --count 44c2f19e38
15000
}}

-   [Pokaż żądania commits](https://forum.freecadweb.org/viewtopic.php?f=10&t=26673) bezpośrednio przed konkretnym żądaniem w GitHubie: w pasku adresu przeglądarki zmień słowo `commit` na `commits`, aby wyświetlić listę,
-   [Znajdowanie numeru żądania commit](https://forum.freecadweb.org/viewtopic.php?t=5308),
-   [Znajdowanie numeru rewizji żądania commit](https://forum.freecadweb.org/viewtopic.php?f=18&t=12883&p=103207#p103203),
-   [Znajdowanie wartości hash odpowiadającej danemu numerowi żądania commit](https://forum.freecadweb.org/viewtopic.php?f=10&t=31118).

### Numer wydania w interfejsie programu FreeCAD 

Numer wersji, który pojawia się w okienku dialogowym [Informacje o FreeCAD](Std_About/pl.md) jest zdefiniowany w pliku `src/Build/Version.h`, który jest tworzony w czasie kompilacji, gdy uruchamiane jest narzędzie `cmake`. Przeczytaj stronę [Wyodrębnij numer wersji ze źródła git](https://forum.freecadweb.org/viewtopic.php?f=4&t=3025), aby uzyskać więcej informacji.

## Dodawanie innych repozytoriów *(zdalnych)* 

Kilku współpracowników projektu FreeCAD ma swoje własne repozytoria Git, gdzie gromadzą swoją pracę lub gdzie eksperymentują z nowymi pomysłami, zanim będą one gotowe do włączenia do oficjalnego kodu źródłowego. Być może będziesz chciał uzyskać ich źródła, aby przetestować ich kod, gdy złożą pull request.

Użyj polecenia `git remote`, aby dodać te inne repozytoria, dzięki czemu będziesz mógł wykonywać operacje `fetch` i `pull` z ich kodem.


{{Code|lang=text|code=
git checkout master
git remote add OTHER_USER OTHER_URL
git fetch OTHER_USER
git checkout -b OTHER_BRANCH OTHER_USER/OTHER_BRANCH
}}

Na przykład dodajmy zdalne repozytorium Bernd-a:


{{Code|lang=text|code=
git remote add bernd http://github.com/berndhahnebach/FreeCAD_bhb
}}

Polecenie `git fetch` pobiera referencje z tego zdalnego repozytorium.


{{Code|lang=text|code=
git fetch bernd
}}

Wyświetla wszystkie gałęzie w Twoim repozytorium oraz te z dodanych przez Ciebie repozytoriów zdalnych. Gałęzie Bernd=a będą wyświetlane jako `remotes/bernd/<branchname>`.


{{Code|lang=text|code=
git branch -a
}}

Teraz przejrzyjmy listę ostatnich 10 żądań commit w gałęzi `femdev` Bernd=a.


{{Code|lang=text|code=
git log -10 --oneline remotes/bernd/femdev
}}

Teraz możemy sprawdzić wybraną gałąź.


{{Code|lang=text|code=
git checkout remotes/bernd/femdev
}}

Następnie możemy utworzyć lokalną gałąź, która będzie bazować na gałęzi zdalnej. Tę lokalną gałąź możemy modyfikować i dodawać do niej własny kod.


{{Code|lang=text|code=
git checkout -b local_branch_name /remotes/bernd/femdev
}}

Możesz też chcieć wykonać operację `git rebase` przeniesienia nowo utworzonej gałęzi na gałąź `upstream/master`, aby upewnić się, że używa ona najnowszego kodu. Jeśli istnieją konflikty, będą musiały być rozwiązane w tym momencie.


{{Code|lang=text|code=
git pull --rebase upstream master
}}

Nowa gałąź jest gotowa do modyfikacji i kompilacji, jak opisano na stronie [Kompilacja](Compiling/pl.md).

Przejdź do sekcji rozwoju na [forum FreeCAD](https://forum.freecadweb.org/viewforum.php?f=6), aby porozmawiać o rozwoju.

## Dodatkowe informacje 

-   [Rozwój FreeCAD z GitKraken](Developing_FreeCAD_with_GitKraken/pl.md), przewodnik używania interfejsu graficznego z Gitem.
-   [Git dla leniwych](https://wiki.spheredev.org/index.php/Git_for_the_lazy), bardzo zwięzły przewodnik po głównych poleceniach `git`.
-   [Pro Git book](https://git-scm.com/book), książka open source ucząca o środowisku Git; jest dostępna w wersji elektronicznej i drukowanej.
-   [Visual Git guide](https://marklodato.github.io/visual-git-guide), podręcznik z diagramami objaśniającymi najczęściej wykonywane operacje w środowisku Git.
-   [Git Tutorial for Beginners: Command-Line Fundamentals](https://www.youtube.com/watch?v=HVsySz-h9r4), film wideo autorstwa Coreya Schafera.
-   [Wprowadzenie do Git - podstawowe pojęcia](https://www.youtube.com/watch?v=uR6G2v_WsRA), wideo autorstwa Davida Mahlera.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Source code management/pl
