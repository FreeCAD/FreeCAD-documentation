---
 GuiCommand:
   Name: WebTools BimServer
   Name/pl: WebTools: BimServer
   MenuLocation: Web Tools , BIM server
   Workbenches: WebTools_Workbench/pl
---

# WebTools BimServer/pl


**Począwszy od FreeCAD v0.17, narzędzie to zostało usunięte ze środowiska Architektura i jest teraz częścią zewnętrznego środowiska pracy [Narzędzia Web](WebTools_Workbench/pl.md), które można zainstalować poprzez menu Narzędzia → <img src="images/AddonManager.svg" width=24px> [Menadżer dodatków](Std_AddonMgr/pl.md).
**



## Opis

To polecenie umożliwia interakcję z instancją [BIMServer](http://www.bimserver.org), otwieranie plików przechowywanych na serwerze BIM i zapisywanie nowych wersji tych plików. BIMServer to darmowy system serwerowy o otwartym kodzie źródłowym przeznaczony do pracy z plikami IFC. W obecnym stanie pozwala na zarządzanie projektami z wieloma plikami IFC i zarządzanie wersjami. Jego wysoce rozszerzalny system baz danych i architektura wtyczek pozwala również na projektowanie zaawansowanych narzędzi zapytań / walidacji i inteligentnych przepływów pracy scalania.

Aby użyć tego polecenia, muszą być spełnione następujące warunki:

-   Moduły Python **json** i **requests** muszą być zainstalowane w systemie.
-   Musisz mieć dostęp do instancji BIMServer *(przeczytaj dokumentację [BIMServer](https://github.com/opensourceBIM/BIMserver/wiki), aby zainstalować BIMServer lokalnie)* i mieć poświadczenia *(login i hasło)* do tego serwera. W chwili pisania tego tekstu stabilna wersja BIMServer to 1.4, ale zalecamy zainstalowanie jednej z dostępnych wersji beta 1.5.X, która automatycznie instaluje wiele wtyczek *(w wersji 1.4 wtyczki należy instalować ręcznie)*.
-   Wszystkie transfery plików z BIMServer odbywają się za pomocą plików IFC. Dlatego musisz wiedzieć, jak pracować z plikami [IFC](Arch_IFC/pl.md).



## Użycie

1.  Upewnij się, że powyższe wymagania są spełnione i masz dostęp do działającej instancji BIMServer.
2.  Wybierz z menu **Web Tools → <img src="images/WebTools_BimServer.svg" width=16px> '''BIM Server''
**
3.  Naciśnij przycisk **Połącz** i wprowadź swoje dane uwierzytelniające
4.  Po nawiązaniu połączenia z BIMServer, wybierz projekt do pracy z rozwijanego okienka **Projekt**.



## Opcje

![](images/Arch_Bimserver_panel.jpg )

-   Jeśli po raz pierwszy łączysz się z serwerem BIMServer z FreeCAD, naciśnij przycisk **Połącz** i wprowadź adres URL serwera, swój login *(który zawsze jest adresem e-mail)* i hasło w oknie dialogowym, które się pojawi. Jeśli chcesz zalogować się automatycznie przy następnym użyciu polecenia BimServer, zaznacz opcję **zapisz dane uwierzytelniające** *(Twój login i hasło nie są zapisywane przez FreeCAD, tylko plik cookie sesji)*.
-   Gdy FreeCAD pomyślnie połączy się z instancją BIMServer, przycisk \"Połącz\" zmieni nazwę na \"\"Połączono\"\". Kliknij przycisk ponownie, aby się rozłączyć. Spowoduje to również usunięcie zapisanego pliku cookie sesji, więc następnym razem będziesz musiał ponownie wprowadzić swoje dane uwierzytelniające.
-   Aby ręcznie usunąć plik cookie sesji i zresetować wszystko, możesz po prostu usunąć adres URL BIMServer zapisany w **Edycja → Preferencje → Architektura → BimServer**.
-   Przycisk **Otwórz w przeglądarce** otworzy interfejs sieciowy BIMServera albo w wewnętrznej przeglądarce FreeCAD, albo, jeśli zaznaczyłeś tę opcję w **Edycja → Preferencje → Architektura → BimServer**, w zewnętrznej przeglądarce internetowej. Pozwala to na przykład tworzyć nowe projekty lub analizować zawartość przechowywaną na BIMServer.



### Pobieranie wersji 

-   Pole rozwijane **Projekt** pokaże dostępne projekty przechowywane na BIMServer. Wybierz jeden z nich, aby zobaczyć dostępne wersje dla tego projektu.
-   Wybierz jedną z wersji i kliknij **Otwórz**, aby pobrać i otworzyć plik IFC odpowiadający tej wersji w programie FreeCAD.
-   Po naciśnięciu przycisku **Otwórz** otworzy się okno dialogowe umożliwiające zapisanie pobranego pliku IFC w wybranej lokalizacji przed jego otwarciem. Jeśli naciśniesz przycisk **Anuluj**, plik zostanie zapisany pod tymczasową nazwą w katalogu tymczasowym systemu.



### Przesyłanie wersji 

-   Jeśli chcesz przesłać nową wersję, upewnij się, że właściwy projekt został wybrany w rozwijanym polu **Projekt**.
-   Wybierz **Obiekt główny**, który chcesz przesłać. Musi to być obiekt [teren](Arch_Site/pl.md) lub [budowla](Arch_Building.md). Tylko obiekty należące do tego głównego obiektu zostaną przesłane.
-   Wpisz **Komentarz**, który będzie opisem *(nazwą)* rewizji.
-   Naciśnij przycisk **Prześlij**. Otworzy się okno dialogowe umożliwiające zapisanie utworzonego pliku IFC w wybranej lokalizacji przed jego przesłaniem. Jeśli naciśniesz przycisk *Anuluj*, plik zostanie zapisany pod tymczasową nazwą w katalogu tymczasowym systemu.



---
⏵ [documentation index](../README.md) > WebTools BimServer/pl
