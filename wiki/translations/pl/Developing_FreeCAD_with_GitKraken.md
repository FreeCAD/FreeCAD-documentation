# Developing FreeCAD with GitKraken/pl
## Przedmowa




FreeCAD używa [Git](https://git-scm.com/) do zarządzania swoim kodem źródłowym. Niniejszy dokument stanowi pobieżne wprowadzenie do [GitKraken](https://www.gitkraken.com/), graficznego interfejsu użytkownika Git. GitKraken jest zastrzeżonym oprogramowaniem, które jest bezpłatne do użytku niekomercyjnego. Nie potrzebujesz GitKrakena do tworzenia kodu dla FreeCAD, ale wielu programistów lubi go i uważa za przydatny do zarządzania ich rozwojem. FreeCAD nie popiera GitKraken, ale mamy nadzieję, że przewodnik taki jak ten pokaże użytkownikom, jak łatwo jest skonfigurować środowisko programistyczne i zachęci więcej osób do wniesienia wkładu.

Więcej informacji na temat ogólnego korzystania z Git z linii poleceń można znaleźć na stronie [Zarządzanie kodem źródłowym](Source_code_management/pl.md) oraz w książce online [Pro Git](https://git-scm.com/book/en/v2). Aby skompilować FreeCAD zobacz stronę [Kompilacja](Compiling/pl.md).



## Wprowadzenie

Git to potężny system kontroli wersji powszechnie używany do śledzenia rozwoju kodu komputerowego. Mimo że jest to złożony system, zwykle potrzebne są tylko podstawowe informacje na temat jego działania i znajomość kilku poleceń terminala. Graficzny interfejs użytkownika (GUI) ułatwia naukę. [GitKraken](https://www.gitkraken.com/) to zastrzeżony program, który jest darmowy do użytku niekomercyjnego i działa na platformie [Electron](https://electronjs.org), co oznacza, że jest wieloplatformowy i może być używany tak samo w systemach Linux, MacOS i Windows.



## Konfiguracja Git development 

Istnieją różne sposoby pobrania GitKraken w zależności od systemu operacyjnego. W dystrybucjach Linuksa czasami można go pobrać z menedżera pakietów.

1.  Pobierz GitKraken.
2.  W przeglądarce internetowej przejdź do strony: {{URL|https://github.com/FreeCAD/FreeCAD}}.
    ![](images/Github-Fork-button.png )
3.  Kiknij na **Fork**. Spowoduje to sklonowanie repozytorium `FreeCAD/FreeCAD` do własnego konta. Innymi słowy, adres URL dostępu do forka będzie następujący:
        https://github.com/GITHUBUSERNAME/FreeCAD.git
4.  Otwórz GitKraken, przejdź do menu **File → Clone Repo**, kolejnie wprowadź adres.
    ![](images/GitKraken-Clone-Repo-dialogue.png )
5.  GitKraken wykona teraz operację `git clone` na twoim osobistym repozytorium.
    Zapoznaj się z różnicą między zdalnym repozytorium [origin vs. upstream](https://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-on-github#9257901). Essentially, Twój fork FreeCAD jest repozytorium `origin`, podczas gdy oficjalne repozytorium FreeCAD jest `upstream`. Teraz musisz odpowiednio ustawić upstream.
6.  Znajdź pasek boczny w Gitkraken. Znajduje się tam sekcja **Lokalna** i **Zdalna**. Sekcja Local odnosi się do lokalnych oddziałów. Sekcja Remote odnosi się do zdalnych repozytoriów i ich gałęzi. Dodajmy repozytorium FreeCAD jako zdalne. W sekcji **Remote** kliknij przycisk **+**. *( jak pokazano na poniższym obrazku)*
    ![](images/Gitkraken-remote-sidebar.png )
7.  Otworzy się okno dialogowe *Add Remote*. Kliknij symbol Github (1). W polu **Github repo** (2) znajdź `FreeCAD/FreeCAD` i kliknij na niego. W polu **Name** wpisz `upstream`. Następnie kliknij przycisk **Add Button**.
    <img alt="" src=images/Gitkraken-add-remote-dark.png  style="width:400px;">
8.  Okno dialogowe zostanie zamknięte i nastąpi powrót do głównego interfejsu GitKrakena. Tym razem znajdź sekcję **Local** na pasku bocznym. Kliknij dwukrotnie gałąź `master`, aby się do niej przełączyć. W wierszu poleceń jest to równoważne
        git checkout master
9.  Kliknij ikonę \"Push\" w prawym górnym rogu interfejsu. Spowoduje to wypchnięcie **Local master** do **Remote origin master**



## Interfejs GitKraken 

Więcej informacji można znaleźć w podręczniku GitKraken [Przewodnik dla początkujących](https://support.gitkraken.com/start-here/guide/).

+++
| Local master                 | Lokalna gałąź głównej gałęzi FreeCAD, oznaczona *niebieską* linią na zrzucie ekranu.                                                                                         |
|                              |                                                                                                                                                                              |
|                              | Element jest podświetlony na **zielono**, co oznacza, że gałąź jest obecnie aktywna (`git checkout`).                                                 |
+++
| Local  | Wszelkie inne gałęzie na lokalnym komputerze. Na zrzucie ekranu widać gałęzie o nazwach `editor_fixes` i `editor_fixes_typos`. |
+++

: *Local* wskazuje komputer lokalny

   
  Remote upstream   Oficjalne repozytorium FreeCAD {{URL|https://github.com/FreeCAD/FreeCAD}}, oznaczone **zieloną** linią na zrzucie ekranu.
  Remote origin     Twój osobisty fork FreeCAD, {{URLn|https://github.com/YourGitHubUsername/FreeCAD}}, oznaczony **czerwoną** linią na zrzucie ekranu.
   

  : *Remote* wskazuje zdalne repozytorium, na przykład w serwisie GitHub

![](images/GitKraken-Main-Screen-sm.jpg )



*Interfejs GitKraken pokazujący trzy lokalne gałęzie, w tym lokalną **master*, oraz zdalne repozytoria `origin** i {{incode|upstream`, z których każde ma gałęzie master i release.}}

Na obrazku zdalne gałęzie **Local master** i **Remote origin master** są trzy commity za **Remote upstream master**, czyli oficjalnym kodem źródłowym FreeCAD. Wskazują na to ikony znajdujące się trzy kroki za łańcuchem, który reprezentuje historię zatwierdzeń gałęzi głównej. Zobacz [Zmiana bazy](Developing_FreeCAD_with_GitKraken/pl#Rebasing.md), aby zaktualizować gałęzie, które są w tyle.



## Rebasing

-   Sprawdź gałąź **Local master**, klikając na nią dwukrotnie (`git checkout master`).
-   Przesuń kursor myszy do ostatniego zatwierdzenia upstream, kliknij prawym przyciskiem myszy i wybierz **Rebase master onto upstream/master** (`git pull upstream master`).
-   Teraz naciśnij przycisk **Push** (`git push origin master`). Spowoduje to wypchnięcie z **Local master** do **Remote origin master**.

![](images/GitKraken-Rebasing.gif )



*Rebasing local master aktualizuje go tak, aby pasował do zawartości upstream master.*



## Gałęzie

Gałęzie są cechą, która sprawia, że Git jest potężny w porównaniu do innych systemów rewizji. Gałęzie nie są kompletnymi forkami, ale raczej definiują migawki, w których wersja kodu zaczyna odbiegać od gałęzi głównej. Za każdym razem, gdy chcesz zmodyfikować kod FreeCAD, najpierw utwórz gałąź, następnie wprowadź zmiany, a następnie scal swoje zatwierdzenia z powrotem do gałęzi głównej. Dzięki Git łatwo jest tworzyć, scalać i usuwać gałęzie, gdy nie są już potrzebne. Przeczytaj [Branching and Merging](https://support.gitkraken.com/working-with-repositories/branching-and-merging), aby dowiedzieć się więcej o tym procesie w GitKraken.

1.  Upewnij się, że aktualnie masz aktywną gałąź master *(kliknij ją dwukrotnie, `git checkout master`)*. W GitKraken gałąź *Local master* powinna być podświetlona na *zielono*.
2.  Kliknij przycisk **Branch**, aby utworzyć nową gałąź i wprowadź jej nową nazwę (`git checkout -b new-name-of-your-branch`).



## Tworzenie pull requests 

[Żądania ściągnięcia](https://help.github.com/articles/about-pull-requests/) (PR) są niezbędne do połączenia kodu w gałęzi w lokalnym repozytorium z kodem w repozytorium `upstream`. Podsumowując proces, po zmodyfikowaniu gałęzi należy przesłać ją do widelca GitHub (`origin`, {{URLn|https://github.com/GITHUBUSERNAME/FreeCAD.git}}), a stamtąd wykonać żądanie ściągnięcia do `upstream`. GitKraken pozwala zaoszczędzić kilka kliknięć w celu łatwego tworzenia pull requestów zamiast korzystania z interfejsu GitHub.

Kroki w GitKraken:

-   Znajdź lokalną gałąź w interfejsie i upewnij się, że jest aktywna *(kliknij ją dwukrotnie)*.
-   Kliknij prawym przyciskiem myszy nazwę gałęzi i znajdź opcję **Push  i rozpocznij żądanie ściągnięcia**.

GitKraken otworzy okno dialogowe z prośbą o potwierdzenie repozytorium, którego gałąź będzie używać do pobierania i wypychania. Następnie wypchnie lokalną gałąź do tego zdalnego repozytorium. ![](images/Gitkraken-How_to_PR.png )

-   GitKraken zapyta, jak chcesz nazwać zdalną gałąź. Domyślną nazwą jest ta sama nazwa, którą gałąź ma lokalnie na komputerze.

<img alt="" src=images/Gitkraken-How-to-PR-Prompt-for-Branch-name.png  style="width:1200px;">

-   Następnie GitKraken otwiera kolejne okno dialogowe z pytaniem o repozytoria i gałęzie do scalenia oraz kierunek (od i do).

Zwykle chcesz scalić ze zdalnej gałęzi **origin ** (`GITHUBUSERNAME/FreeCAD`) do zdalnej gałęzi **upstream master** (`FreeCAD/FreeCAD`). Pamiętaj, aby wprowadzić dobry tytuł żądania ściągnięcia i napisać bardziej opisowy akapit, jeśli zmiany są znaczące. Więcej informacji można znaleźć w oficjalnej dokumentacji [GitKraken](https://support.gitkraken.com/working-with-repositories/pull-requests). ![](images/Gitkraken-How-to-PR-Github-Dialog-breakdown.png )



## Rozwiązywanie konfliktów scalania 

GitKraken ma specjalne narzędzie do konfliktów scalania, które jest dostępne tylko w wersji GitKraken Pro. Istnieją jednak obejścia umożliwiające korzystanie z zewnętrznych narzędzi do scalania.

-   [Zewnętrzne narzędzia do scalania kompatybilne z GitKraken](https://support.gitkraken.com/working-with-repositories/branching-and-merging/): Beyond Compare, FileMerge, Kaleidoscope, KDiff, Araxis, P4Merge
-   Jeśli żadna z powyższych opcji nie działa, można określić [Zewnętrzne narzędzia scalania i porównywania](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_external_merge_tools) w pliku konfiguracyjnym `~/.gitconfig` w katalogu domowym użytkownika.



## Squashing commits 

Jako system kontroli wersji Git zachęca do wykonywania wielu zatwierdzeń, aby śledzić zmiany. Jeśli jednak masz zbyt wiele małych zmian, historia zatwierdzeń może wyglądać nieco niechlujnie. Squashing to kondensacja różnych commitów w tylko jeden commit. Z [podręcznika GitKraken](https://support.gitkraken.com/working-with-commits/squash/), squashing jest dostępny dla commitów, które spełniają następujące wymagania:

-   Należy wybrać co najmniej dwa zatwierdzenia do zgniecenia.
-   Najmłodsze zatwierdzenie, według daty zatwierdzenia, jest również bieżącym zatwierdzeniem HEAD.
-   Genealogicznie następujące po sobie.
-   Chronologicznie następujące po sobie.
-   Najstarsze zatwierdzenie na liście ma rodzica.

Jeśli wszystkie te warunki są spełnione, opcja *Squash* pojawia się po kliknięciu prawym przyciskiem myszy węzła zatwierdzenia. Zobacz [Squash.gif](https://support.gitkraken.com/img/documentation/working-with-files/commits/squash.gif).



## Podążanie za innymi repozytoriami FreeCAD 

Możesz użyć GitKraken do śledzenia osobistych forków FreeCAD innych programistów; w ten sposób możesz zobaczyć, jak piszą kod i zatwierdzają zmiany we własnych gałęziach, zanim prześlą pull requesty do repozytorium upstream `FreeCAD/FreeCAD`.

1.  W lewym panelu obok kategorii *Remote* naciśnij znak *+*.
2.  Pojawi się okno dialogowe do wprowadzenia nazwy repozytorium, które chcesz dodać. Zalecane piloty pochodzą od głównych programistów FreeCAD i znanych współpracowników: wmayer, yorikvanhavre, ickby, sliptonic, kkremitzki, itp.
3.  Naciśnij **Add Remote**.

Teraz za każdym razem, gdy autorzy tych repozytoriów wykonają nowe zatwierdzenia lub gałęzie zostaną ponownie zbudowane, zobaczysz ich historię zatwierdzeń w sposób graficzny. ![](images/Gitkraken-add-remote.gif )



## Powiązane

-   [Zarządzanie kodem źródłowym](Source_code_management/pl.md)
-   [Rozwój FreeCAD z KDevelop](Developing_FreeCAD_with_KDevelop/pl.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Developer](Category_Developer.md) > [3rd Party](Category_3rd Party.md) > Developing FreeCAD with GitKraken/pl
