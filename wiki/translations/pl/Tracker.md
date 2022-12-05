# Tracker/pl
{{TOCright}}


**W lutym 2022 roku śledzenie błędów FreeCAD zostało przeniesione na GitHub Issues pod adresem https://github.com/FreeCAD/FreeCAD/issues. Opisany poniżej bug tracker Mantis jest obecnie w trybie tylko do odczytu.**

![](images/Mantis_logo_262x90.png )

[FreeCAD BugTracker](https://www.freecadweb.org/tracker) jest miejscem, na którym to możnaː zgłaszać błędy, przesyłać prośby o funkcje, poprawki lub prośby o połączenie oddziału, jeśli opracowałeś coś przy użyciu Gita. Tracker jest podzielony na Środowiska pracy, więc proszę być konkretnym i złożyć wniosek w odpowiedniej podsekcji. W razie wątpliwości należy pozostawić go w sekcji **FreeCAD**.

## Zalecany przepływ pracy 

![](images/Bugreport-workflow.png )

Jak pokazano na powyższym schemacie, przed utworzeniem zgłoszenia należy zawsze najpierw przeszukać forum i bugtracker, aby dowiedzieć się, czy Twój problem jest znany. Oszczędza to mnóstwo czasu/ pracy dla programistów i wolontariuszy, którzy mogliby poświęcić ten czas czyniąc FreeCAD jeszcze bardziej niesamowitym.

## Zgłaszanie błędów 

Jeśli uważasz, że mogłeś znaleźć błąd, możesz go zgłosić, pod warunkiem, że postępowałeś zgodnie z naszymi zasadami krok po krokuː

-   Upewnij się, że używasz najbardziej aktualnej wersji FreeCAD. **UWAGAː**. Twój błąd może zostać naprawiony w wersji rozwojowej *(niestabilnej)*. Zwykle użytkownicy korzystają z wersji stabilnej FC.
-   Upewnij się, że twój błąd jest naprawdę błędem, to znaczy czymś, co powinno działać, ale nie działa. **Upewnij się, że ten sam błąd nie został wcześniej zgłoszony, poprzez wstępne przeszukanie bugtrackera i forum**.
    -   Pamiętaj, żeː jeśli nie jesteś pewien, nie wahaj się wyjaśnić swojego problemu/błędu na [Forum Pomocy](http://forum.freecadweb.org/viewforum.php?f=3) i zapytaj co robić.
    -   **Uwaga**ː przed wysłaniem postu na forum proszę przeczytać [Przewodnik po forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=2264).
-   Opisuj jak najdokładniej problem, i jak można go odtworzyć. Jeśli nie możemy zweryfikować błędu, możemy nie być w stanie go naprawić.
    -   Oznacza to **zgłaszanie w sposób jasny, dobrze sformatowany, krok po kroku**, aby nawet użytkownik amator mógł go odtworzyć.
    -   Zalecamyː załączać **Zrzuty ekranu** błędu, są również bardzo pomocne. Użytkownicy Windows: proszę nie dołączać zrzutów ekranu w formacie Word lub PDF. Użyj narzędzia Windows Snipping do zapisania zrzutu jako obrazu PNG.
    -   Zalecamyː Jeszcze lepszym będzie, \"Animowany gif lub Screencast\" zwiększyłby prawdopodobieństwo udanego powielenia problemu.
-   **Dodaj przykładowy plik FreeCAD** *(.FCStd)*, aby programiści/testerzy mogli szybko odtworzyć błąd.
    -   Proszę nie pakować pliku \*.FCStd, jest już skompresowany.
    -   Załączniki są ograniczone rozmiarem. Jeśli Twój plik \*.FCStd jest zbyt duży, aby go załączyć, możesz skorzystać z usługi dysku online *(wiele z nich jest darmowych jak Google Drive, Microsoft OneDrive, Dropbox)*.
-   Dołącz wszystkie informacje zawarte w oknie dialogowym **Pomoc (menu) -\> O programie FreeCAD**, używając w przycisku **Kopiuj do schowka**. Upewnij się, że twoje dane zawierają używaną wersję OCC lub OCE.
-   Proszę złożyć jeden osobny raport dla każdego błędu.
-   Jeśli twój błąd powoduje awarię programu FreeCAD i jesteś w systemie, który go obsługuje, możesz spróbować uruchomić **debug backtrace** i dołączyć ten ślad do zgłoszenia. To może zaoszczędzić programistom dużo czasu przez wskazywanie źródła błędu. Zobacz [Debugging](Debugging.md) po więcej szczegółów.

## Oczekiwane funkcje 

Jeśli chcesz, aby w FreeCAD pojawiło się coś, co nie jest jeszcze zaimplementowane, to nie jest błędem, ale żądaniem funkcji.

1.  **WAŻNEː** Przed złożeniem zapytania o potencjalną funkcję **upewnij się, że jesteś pierwszy, przeszukując forum i bugtracker**. Jeśli doszedłeś do wniosku, że nie istnieją wcześniejsze zgłoszenia lub dyskusje, następnym krokiem jest toː
2.  Utwórz wątek na forum, aby przedyskutować swoją prośbę o funkcje ze społecznością poprzez [forum](http://forum.freecadweb.org/viewforum.php?f=8).
3.  Gdy społeczność zgodzi się, że jest to ważna funkcja, możesz otworzyć zgłoszenie na trackerze *(wpisz je pod **żądanie funkcji** zamiast **błąd**)*.

-   **UWAGA #1** Aby zachować porządek, należy pamiętać o umieszczeniu adresu URL zgłoszenia w wątku forum, oraz numeru zgłoszenia *(jako linku)*.
-   **UWAGA #2** Pamiętaj, że nie ma gwarancji, że twoje życzenie zostanie spełnione. ![Strona z raportem FreeCAD Bugtracker - użyj rozwijanego menu, aby poprawnie określić, czym jest zgłoszenie.](images/MantisBT-setting-Feature-Request.jpg )

## Przesyłanie łatek 

Jeśli zaprogramowałeś poprawkę dotyczącą błędu, rozszerzenie lub coś innego, co może być użyteczne publicznie w programie FreeCADe, prześlij swoją poprawkę jako \"Pull Request\" na [GitHub](https://github.com/FreeCAD/FreeCAD).

1.  Dla dużych, złożonych lub zmieniających zachowanie zgłoszeń, otwórz wątek na [forum dla programistów](https://forum.freecadweb.org/viewforum.php?f=10), aby ogłosić i omówić swoją poprawkę. Dla małych poprawek błędów nie jest to konieczne.
2.  Prześlij swój Pull Request *(PR)* do [FreeCAD GitHub repo](http://github.com/FreeCAD/FreeCAD). Wiadomość o wysłaniu PR będzie wstępnie wypełniona listą kontrolną, którą należy wykonać, aby upewnić się, że zgłoszenie ma jak największe szanse na szybką akceptację. Jeśli nie pracowałeś wcześniej z `git` lub nie jesteś zaznajomiony z przesyłaniem PR na github, przeczytaj nasze wprowadzenie do [github](Source_code_management/pl.md) na stronie wiki.
3.  Bądź obecny w dyskusji, zarówno na forum jak i w żądaniu podciągnięcia na GitHub, aby twój kod mógł być potencjalnie scalony bardziej efektywnie.

## Wnioskowanie o połączenie 

*(Te same wytyczne co [Przesyłanie łatek](https://www.freecadweb.org/wiki/Tracker#Submitting_patches))*.

Jeśli stworzyłeś gałąź gita zawierającą zmiany, które chciałbyś zobaczyć w kodzie FreeCAD, możesz tam poprosić o recenzję i połączenie swojej gałęzi, jeśli deweloperzy FreeCAD są wobec niej zgodni. Musisz najpierw opublikować swoją gałąź w publicznym repozytorium git *(github, gitlab, bitbucket, sourceforge itp\...)*, a następnie podać adres URL Twojej gałęzi w swoim wniosku o połączenie.

## Wskazówki i sztuczki MantisBT 

### Znacznik MantisBT 

MantisBT (Mantis Bug Tracker) ma swój własny unikalny znacznik.

-   **@** Wspomniany - działa tak jak na GitHubie, gdzie jeśli wyślesz **@** na czyjąś nazwę użytkownika, osoba ta otrzyma powiadomienie email, że została wymieniona w wątku zgłoszenia.

<img alt="" src=images/mantisbt-mention-example.jpg  style="width:600px;">

-   **\#**1234 - Poprzez dodanie znaku **#** przed numerem pojawi się skrót do połączenia z innym zgłoszeniem w MantisBT.

    :   **Uwaga**: jeśli najedziesz kursorem na zgłoszenie, wyświetli się podsumowanie + jeśli bilet jest zamknięty, zostanie przekreślony jak \# 1234.

<img alt="" src=images/mantisbt-ticket-shortcut-example.jpg  style="width:600px;">

-   **\~**5678 - skrót, który łączy się z notatką o błędzie w zgłoszeniu. Może być użyty do odniesienia się do czyjejś odpowiedzi w obrębie wątku. Każda osoba, która umieściła zgłoszenie, będzie miała przy swojej nazwie użytkownika wyświetlony unikalny numer \~#####. Jeśli spojrzysz na obrazek w przykładzie, zobaczysz, że skrót odnosi się do *numeru zgłoszenia:numeru komentarza* tego zgłoszenia.

<img alt="" src=images/mantisbt-comment-shortcut-example.jpg  style="width:600px;">

-   **\<del\> \</del\>** - Te tagi będą  przekreślać tekst.

<img alt="" src=images/mantisbt-strikeout-text-example.jpg  style="width:600px;">

-   **\<code\> \</code\>** - Aby przedstawić linię lub blok kodu, użyj tego znacznika, a on pokoloruje i elegancko go wyróżni.

<img alt="" src=images/mantisbt-colorized-code-example.jpg  style="width:600px;">

### MantisBT BBCode 

Oprócz powyższego [Znaczniki MantisBT](Tracker/pl#Znacznik_MantisBT.md) istnieje również możliwość korzystania z formatu BBCode. Pełna lista znajduje się na stronie [BBCode plus strona z pluginami](https://github.com/mantisbt-plugins/BBCodePlus#supported-bbcode-tags). Poniżej znajduje się lista obsługiwanych formatów BBCodeː 
[img][/img] - obrazek
[url][/url] - odnośnik internetowy
[email][/email] - adres Email
[color=red][/color] - kolorowy tekst
[highlight=yellow][/highlight] - Podświetlony tekst
[size][/size] - wielkość Fonta
[list][/list] - lista
[list=1][/list] - lista numerowana *(cyfra jest numerem początkowym)*
[*] - pozycje z listy
[b][/b] - pogrubiony
[u][/u] - podkreślony
[i][/i] - ukośny
[s][/s] - przekreślony
[left][/left] - wyrównany do lewej
[center][/center] - wyrównany do środka
[right][/right] - wyrównany do prawej
[justify][/justify] - wyjustowany
[hr] - reguła pozioma
[sub][/sub] - indeks dolny
[sup][/sup] - index górny
[table][/table] - tabela
[table=1][/table] - tabela z ramką o określonej szerokości
[tr][/tr] - wiersz tabeli
[td][/td] - kolumna tabeli
[code][/code] - blok z kodem
[code=sql][/code] - blok kodu z definicją języka
[code start=3][/code] - blok kodu z numerami linii zaczynającymi się od cyfry
[quote][/quote] - Cytat *ktoś* *(bez imienia)*
[quote=name][/quote] - Cytat według *nazwa*


===MantisBT \<=\> znaczniki GitHub=== Poniżej znajdują się specjalne słowa kluczowe pluginu MantisBT Source-Integration, który łączy się z repo FreeCAD GitHub. Zobacz [GitHub oraz MantisBT](Tracker/pl#GitHub_oraz_MantisBT.md).

-   **c:FreeCAD:git commit hash:** - **c** oznacza *commit*. FreeCAD oznacza GitHub FreeCAD repo. *git commit hash* to konkretny skrót git commit, do którego nastąpiło odwołanie. Uwaga: konieczne jest użycie dwukropka wskazującego. Przykładː cːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **d:FreeCAD:git commit hash:** - podobny do powyższego, **d** oznacza \"diff\", co zapewni odmienny pogląd na temat danego zobowiązania. Przykładː dːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **p:FreeCAD:pullrequest:** - podobny do powyższego, **p** oznacza Pull Request. Przykładː pːFreeCADː498ː

<img alt="" src=images/mantisbt-source-integration-markup.jpg  style="width:600px;"> 

## GitHub oraz MantisBT 

FreeCAD bugtracker posiada wtyczkę o nazwie [Source Integration](https://github.com/mantisbt-plugins/source-integration), która zasadniczo wiąże oba FreeCAD GitHub repo z naszym trackerem MantisBT. Ułatwia to śledzenie i kojarzenie zgłoszeń git z ich odpowiednimi zgłoszeniami do MantisBT. **Plugin Source Integration skanuje komunikaty git commit w poszukiwaniu konkretnych słów kluczowych w celu wykonania następujących działań:**.

**Uwaga** Poniższe słowa kluczowe muszą być dodane w git commit message, a nie w temacie PR.

### Zdalne odwoływanie się do zgłoszenia. 

Użycie tego wzorca automatycznie połączy git commit do zgłoszenia (**Uwaga:** to nie zamknie zgłoszenia). Format MantisBT rozpozna:

-   bug #1234
-   bugs #1234, #5678
-   issue #1234
-   issues #1234, #5678
-   report #1234
-   reports #1234, #5678

Dla dociekliwych tutaj jest wyrażenie regularne, którego używa MantisBT do tej operacji:


### Rozwiązywanie zdalnie zgłoszeń 

Interfejs MantisBT rozpoznaje format:

-   fix #1234
-   fixed #1234
-   fixes #1234
-   fixed #1234, #5678
-   fixes #1234, #5678
-   resolve #1234
-   resolved #1234
-   resolves #1234
-   resolved #1234, #5678
-   resolves #1234, #5678

Dla dociekliwych: mamy tu zastosowanie wyrażenia regularnego MantisBT do tej operacji:


## Powiązane

-   [Usuwanie błędów](Bug_Triage/pl.md)
-   [Zarządzanie kodem źródłowym](Source_code_management/pl.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Administration](Category_Administration.md) > Tracker/pl
