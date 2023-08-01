# Crowdin Scripts/pl
{{TOCright}}

## Zarządzanie Tłumaczeniami w programie FreeCAD 

FreeCAD do zarządzania tłumaczeniami używa zewnętrznego serwisu nazywanego [Crowdin.](https://crowdin.com/project/freecad)

W FreeCAD/src/Tools znajdują się 3 skrypty, które służą do zarządzania plikami tłumaczeń:

1.  updatets.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatets.py)
2.  updatecrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatecrowdin.py)
3.  updatefromcrowdin.py [(github source)](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/updatefromcrowdin.py)

### Uwagi

-   Skrypty te uruchamiane są z głównego katalogu FreeCAD/.
-   By umożliwić działanie tych skryptów musisz mieć prawidłowy klucz FreeCAD Crowdin API umieszczony w swoim pliku key ~/.crowdin-freecad. (Z powodów bezpieczeństwa jest tylko dostępny dla ludzi z prawami administratora na stronie Crowdin FreeCAD)
-   Obecnie te narzędzia są kompatybilne z Pythonem 2.

### updatets.py

Skrypt updatets.py utworzy pliki .ts w twoim lokalnym katologu FreeCAD/. Generuje on pliki .ts (Plik Źródłowy Tłumaczenia Qt).

Jest wywoływany przez: python2 updatets.py

### updatecrowdin.py

Skrypt updatecrowdin.py ładuje zmiany do Crowdin (zewnętrznego serwisu tłumaczeń społecznościowych) z twojego lokalnego katalogu FreeCAD/. Obecnie skrypt obsługuje 4 argumenty:

-   updatecrowdin.py status wypisuje stan tłumaczeń
-   updatecrowdin.py update aktualizuje Crowdin aktualną wersją plików .ts znalezioną w kodzie źródłowym
-   updatecrowdin.py build buduje na Crowdin nową, możliwą do pobrania paczkę z wszystkimi przetłumaczonymi ciągami tekstowymi
-   updatecrowdin.py download pobiera najnowszą paczkę

### updatefromcrowdin.py

Skrypt updatefromcrowdin.py ściąga zmiany z Crowdin do twojego lokalnego katalogu FreeCAD/.

## By wysłać najnowsze zwroty do Crowdin 

-   Przetestowane tylko na Linuksie
-   Potrzebujesz pliku .credentials w twoim katalogu /home/TwójUżytkownik. Plik ten jest prostym plikiem tekstowym zawierającym tylko jedną linię, którą jest klucz API otrzymywany na <https://crowdin.com/project/freecad/settings#api> (tylko dla administratorów)
-   Upewnij się, że twoje repozytorium jest czyste (git pull, git stash jeśli to konieczne)
-   cd /path/to/freecad-source-code/src/Tools
-   python updatets.py (wypełni najnowszymi ciągami tekstowymi wszystkie pliki .ts znalezione w źródłach)
-   python updatecrowdin.py update (wyśle pliki .ts do Crowdin. Crowdin zaktualizuje tylko nowe ciągi tekstowe)
-   cd ../.. (idź z powrotem go głównego katalogu źródeł)
-   git checkout . (cofnij wszystkie zmiany w plikach .ts, nie ma powodu by wprowadzać je już teraz gdy są wciąż nieprzetłumaczone)

## By scalić najnowsze tłumaczenia z Crowdin 

-   Przetestowane tylko w systemie Linuks,
-   Potrzebujesz pliku .credentials w katalogu /home/TwójUżytkownik. Plik ten jest zwykłym plikiem tekstowym zawierającym tylko jeden wiersz, jest to klucz API otrzymywany na <https://crowdin.com/project/freecad/settings#api> *(tylko dla administratorów)*,
-   Upewnij się, że twoje repozytorium jest czyste *(git pull, git stash jeśli to konieczne)*,
-   cd /path/to/freecad-source-code/src/Tools,
-   python updatecrowdin.py build *(stworzy zip po stronie Crowdin z wszystkimi plikami, może potrwać chwilę\... Krok ten może zostać też wykonany na stronie internetowej Crowdin)*,
-   python updatecrowdin.py download *(pobierze plik freecad.zip do tego katalogu)*,
-   mv freecad.zip \~ przenieś plik zip do twojego katalogu domowego, *(by uniknąć przypadkowego wprowadzenia go później)*,
-   *(opcjonalnie)* zedytuj skrypt updatefromcrowdin.py i sprawdź czy default_languages zawiera wszystkie języki, których wymagasz *(co do zasady wszystkie, które maja ponad 50% zaawansowania)*,
-   python updatefromcrowdin.py -z /home/TwójUżytkownik/freecad.zip,
-   cd ../.. *(przejdź z powrotem go głównego katalogu źródeł)*.
-   jeśli coś pójdzie nie tak lub nie jesteś pewien, wyczyść wszytko używając git checkout,
-   jeśli wszystko wygląda w porządku *(git status)*, wprowadź zmiany używając git add . && git commit,
-   Utwórz prośbę o połączenie *(PR)* dla FreeCAD.

## By utworzyć plik tłumaczenia ze strony internetowej 

-   Sklonuj stronę domową
-   cd /path/to/FreeCAD-homepage
-   xgettext \--from-code=UTF-8 -o lang/homepage.pot \*.php
-   Zaktualizuj ręcznie \"homepage.po\" na stronie internetowej Crowdin, korzystając z pliku lang/homepage.pot

## By zaktualizować tłumaczenia na stronie internetowej 

-   Pozyskaj plik freecad.zip przez pobranie go ze strony internetowej Crowdin albo korzystając z instrukcji powyżej *(python updatecrowdin.py download)*,
-   cd /path/to/FreeCAD-homepage,
-   Upewnij się, że twoje repozytorium jest czyste *(git pull, git stash jeśli to konieczne)*,
-   python updatefromcrowdin.py -z /path/to/freecad.zip,
-   jeśli coś pójdzie nie tak lub nie jesteś pewien, wyczyść wszytko używając git checkout,
-   jeśli wszystko wygląda w porządku *(git status)*, wprowadź zmiany używając git add . && git commit,
-   Utwórz prośbę o połączenie *(PR)* dla FreeCAD-Homepage,
-   Po wykonaniu połączenia, jeden z administratorów załaduje ftp serwera Web,

## Powiązane

-   [Lokalizacja](Localisation/pl.md)
-   [Skrypty Crowdin](Crowdin_Scripts/pl.md)
-   [Proces wydania](Release_process.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Administration](Category_Administration.md) > Crowdin Scripts/pl
