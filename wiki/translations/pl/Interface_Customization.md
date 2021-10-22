# Interface Customization/pl
{{TOCright}}

## Wprowadzenie

Interfejs FreeCAD jest oparty na nowoczesnym zestawie narzędzi [Qt](http://en.wikipedia.org/wiki/Qt_(toolkit)) i posiada nowoczesną organizację. Niektóre aspekty interfejsu mogą być dostosowane do indywidualnych potrzeb. Możesz na przykład dodać niestandardowe paski narzędzi, z narzędziami z kilku Środowisk pracy lub narzędziami zdefiniowanymi w makrach, a także tworzyć własne skróty klawiaturowe. Ale menu i domyślne paski narzędzi, które są dostarczane z programem FreeCAD i jego warsztatami nie mogą być zmieniane.

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*Okno dialogowe Dostosowywanie interfejsu*

## Użycie

1.  Polecenia dostępne w oknie dialogowym Dostosowywania zależą od aktywnych programów roboczych, które zostały załadowane w bieżącej sesji programu FreeCAD. Należy więc najpierw załadować wszystkie programy, do których chcemy mieć dostęp.
2.  Istnieje kilka sposobów wywołania polecenia <img alt="" src=images/Std_DlgCustomize.svg  style="width:16px;"> [Std: Dostosuj](Std_DlgCustomize/pl.md):
    -   Wybierz polecenie z menu **Przybory → <img src="images/Std_DlgCustomize.svg" width=16px> Dostosuj...**.
    -   Kliknij prawym przyciskiem myszy na obszarze paska narzędzi i wybierz z menu kontekstowego **<img src="images/Std_DlgCustomize.svg" width=16px> Dostosuj...**.
3.  Otworzy się okno dialogowe Dostosuj\... Więcej informacji można znaleźć w rozdziale [Opcje](#Opcje.md).
4.  Przycisk **Pomocy** nie działa w tym momencie.
5.  Naciśnij przycisk **Zamknij**, aby zamknąć okno dialogowe.

## Opcje

W oknie dialogowym Dostosuj dostępne są następujące zakładki:

### Polecenia

![](images/Std_DlgCustomize_tab_Commands.png ) 
*Zakładka Polecenia*

Na tej zakładce można przeglądać dostępne polecenia.

#### Przegląd poleceń 

1.  Wybierz kategorię komend w panelu *\'Kategoria* po lewej stronie. Niektóre kategorie odpowiadają wpisom w menu.
2.  Narzędzia dostępne w wybranej kategorii są pokazane w panelu po prawej stronie.
3.  Najedź na polecenie: pojawi się podpowiedź.
4.  Wybierz polecenie: tekst paska stanu jest wyświetlany poniżej dwóch paneli.


{{Top}}

### Klawiatura

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*Zakładka Klawiatura*

Na tej karcie można zdefiniować własne skróty klawiaturowe. W zakładce [Makrodefinicje](#Makrodefinicje.md) można zdefiniować skróty dla poleceń makro.

#### Dodaj własny skrót 

1.  Wybierz kategorię poleceń z listy rozwijanej **Kategoria**.
2.  Wybierz polecenie z panelu **Komendy**.
3.  Pole **Aktualny skrót** wyświetla aktualny skrót, jeśli jest dostępny.
4.  Wprowadź nowy skrót w polu wprowadzania **Naciśnij nowy skrót**. Skróty mogą mieć długość do 4 wejść. Każde wejście jest albo pojedynczym znakiem, kombinacją jednego lub kilku klawiszy specjalnych, albo kombinacją jednego lub kilku klawiszy specjalnych i jednego znaku. Użyj klawisza **Backspace** do poprawiania błędów.
5.  Jeśli skrót jest już używany, w oknie dialogowym pojawi się pytanie, czy chcesz go zastąpić, a polecenie, do którego skrót jest przypisany, pojawi się w panelu **Aktualnie przypisany do**.
6.  Naciśnij przycisk **Przypisz**, aby przypisać nowy skrót.
7.  Naciśnij przycisk **Wyczyść** żeby usunąć wprowadzony skrót. Spowoduje to również usunięcie zawartości pola **Bieżący skrót**. Należy pamiętać, że domyślne skróty nie są usuwane na stałe. Zostaną one przywrócone po ponownym uruchomieniu FreeCAD.

#### Usuń własny skrót 

1.  Wybierz kategorię polecenia z listy rozwijanej **Kategoria**.
2.  Wybierz polecenie z panelu **Polecenia**.
3.  Naciśnij przycisk **Reset**.

#### Usuń wszystkie własne skróty 

1.  Naciśnij przycisk **Zresetuj wszystko**

#### Uwagi (Klawiatura) 

-   Skróty działają tylko wtedy, gdy ich polecenia pojawiają się w standardowym menu lub w menu Środowiska pracy, które zostało załadowane w bieżącej sesji programu FreeCAD. Oraz gdy ich polecenia pojawiają się na widocznym pasku narzędzi.

-   W wersji **0.19** jest problem z niektórymi poleceniami Środowiska Pracy Draft. Ich domyślne skróty nie działają i/lub nie można im przypisać własnych skrótów.
-   Aby ponownie przypisać domyślny skrót, należy najpierw przypisać nowy skrót do jego oryginalnego polecenia.


{{Top}}

### Środowiska pracy 

![](images/Std_DlgCustomize_tab_Workbenches.png ) 
*Zakładka Środowiska pracy*

Na tej zakładce można zmienić listę [Wybór środowiska pracy](Std_Workbench/pl.md). Lista **Aktywowane stanowiska pracy** pokazuje stanowiska pracy, które pojawią się w selektorze Środowisk pracy

#### Wyłączenie Środowiska pracy 

1.  Wybierz Środowisko pracy na liście **Włączone stanowiska pracy**.
2.  Naciśnij przycisk **<img src="images/Button_left.svg" width=16px>**.
3.  Środowisko pracy zostanie przeniesione na listę **Nieaktywne stanowiska pracy**.

#### Ponowne włączenie Środowiska pracy 

1.  Wybierz Środowisko pracy na liście **Wyłączone stanowiska pracy**.
2.  Naciśnij przycisk **<img src="images/Button_right.svg" width=16px>**.
3.  Środowisko pracy zostanie przeniesione na listę **Włączone Środowiska pracy**.

#### Ponowne włączenie wszystkich Środowisk pracy 

1.  Naciśnij przycisk **<img src="images/Button_add_all.svg" width=16px>**.

#### Zmiana pozycji Środowiska pracy 

1.  Wybierz Środowisko pracy na liście **Włączone Środowiska pracy**.
2.  Naciśnij przycisk **<img src="images/Button_up.svg" width=16px>** lub **<img src="images/Button_down.svg" width=16px>**.
3.  Opcjonalnie powtarzaj to do momentu, aż Środowisko pracy znajdzie się we właściwej pozycji.

#### Sortowanie Środowisk pracy w kolejności alfabetycznej 

1.  Naciśnij przycisk **<img src="images/Button_sort.svg" width=16px>**.


{{Top}}

### Paski narzędzi 

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*Zakładka Paski narzędzi*

Na tej karcie można tworzyć i modyfikować własne paski narzędzi.

#### Wybierz Środowisko pracy 

1.  Na liście rozwijanej po prawej stronie wybierz Środowisko pracy, którego własne paski narzędziowe chcesz zmodyfikować. Opcja {{Value|Global}} jest przeznaczona dla niestandardowych pasków narzędzi, które powinny być dostępne we wszystkich Środowiskach pracy.

#### Tworzenie paska narzędzi 

1.  Naciskaj przycisk **Nowy...**
2.  Wpisz nazwę w otwierającym się oknie dialogowym.
3.  Naciśnij przycisk **OK**.
4.  W panelu po prawej stronie pojawi się nowy pasek narzędzi.

#### Zmiana nazwy paska narzędzi 

1.  Wybierz pasek narzędzi w panelu po prawej stronie.
2.  Wciśnij przycisk **Zmień nazwę...**.
3.  Wprowadź nową nazwę w otwartym oknie dialogowym.
4.  Naciśnij przycisk **OK**.

#### Usuwanie paska narzędzi 

1.  Wybierz pasek narzędzi w panelu po prawej stronie.
2.  Wciśnij przycisk **Skasuj**.

#### Wyłączenie paska narzędzi 

1.  Usuń zaznaczenie pola wyboru z przodu nazwy paska narzędzi w panelu po prawej stronie.
2.  Wyłączony pasek narzędzi będzie niewidoczny w interfejsie FreeCAD.

#### Dodawanie polecenia 

1.  Wymagany jest co najmniej jeden niestandardowy pasek narzędzi. Zobacz [Tworzenie paska narzędzi](#Tworzenie_paska_narz.C4.99dzi.md).
2.  Wybierz odpowiedni pasek narzędzi w panelu po prawej stronie. Jeśli nie zostanie wybrany żaden pasek narzędzi, polecenie zostanie dodane do pierwszego paska narzędzi na liście.
3.  Wybierz kategorię z listy rozwijanej po lewej stronie. W kategorii \"Makra\" pojawiają się polecenia makrodefinicji, które zostały ustawione na karcie [Makrodefinicje](#Makrodefinicje.md).
4.  Wybierz polecenie z panelu po lewej stronie.
5.  Lub wybierz \'\', aby dodać separator *(linię pomiędzy dwoma przyciskami paska narzędzi)*.
6.  Naciśnij przycisk **<img src="images/Button_right.svg" width=16px>**.

#### Usuwanie polecenia 

1.  W razie potrzeby, rozwiń pasek narzędzi w panelu po prawej stronie.
2.  Wybierz polecenie.
3.  Naciśnij przycisk **<img src="images/Button_left.svg" width=16px>**.

#### Zmiana pozycji polecenia 

1.  W razie potrzeby, rozwiń pasek narzędzi w panelu po prawej stronie.
2.  Wybierz polecenie
3.  Naciśnij przycisk **<img src="images/Button_up.svg" width=16px>** lub **<img src="images/Button_down.svg" width=16px>**.
4.  Opcjonalnie powtarzaj to do momentu, aż polecenie znajdzie się we właściwej pozycji.

#### Uwagi (Paski narzędzi) 

-   Paski narzędzi należące do aktualnego stanowiska pracy są natychmiast aktualizowane, ale po wyłączeniu/ ponownym włączeniu paska narzędzi konieczna jest zmiana stanowiska pracy (przełączenie na inne stanowisko pracy, a następnie ponowne jego włączenie).
-   Do aktualizacji globalnych pasków narzędzi konieczna jest zmiana stanowiska pracy (jeżeli dodano lub usunięto polecenia) lub ponowny start (jeżeli zmieniono kolejność pasków narzędzi lub zmieniono nazwę paska narzędzi).

-   W V0.19 jest problem z niektórymi poleceniami draft. Po dodaniu ich do niestandardowego paska narzędzi i wyjściu z aplikacji FreeCAD plik {{FileName|user.cfg}} musi być ręcznie edytowany dla tych poleceń. Wyszukaj nazwę niestandardowego paska narzędzi i w tej sekcji zmień zawartość elementów `FCText`, które zaczynają się od `gui_` do `DraftTools`.


{{Top}}

### Makrodefinicje

![](images/Std_DlgCustomize_tab_Macros.png ) 
*Zakładka Makrodefinicje*

Na tej zakładce można skonfigurować polecenia makrodefinicji użytkownika. Po skonfigurowaniu można je dodawać do własnych pasków narzędzi. FreeCAD używa dedykowanego folderu dla makr użytkownika i tylko w nim można tworzyć makra. Użyj polecenia <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;"> [Std: DlgMacroExecute](Std_DlgMacroExecute.md), aby znaleźć ten folder w systemie.

Jeśli pobierasz makro z <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Menadżera dodatków](Std_AddonMgr/pl.md), upewnij się, że pobrałeś również jego plik ikonki. Większość makr ma link z obrazem na stronie informacyjnej, która pojawia się w menedżerze dodatków. Możesz na przykład umieścić ten plik ikonki w folderze makr użytkownika.

Jeśli chcesz korzystać z makrodefinicji pobranej z innego źródła, będziesz musiał zainstalować ją ręcznie. Zobacz temat [Jak zainstalować makrodefinicje](How_to_install_macros/pl.md) aby uzyskać więcej informacji.

#### Dodawanie makropolecenie 

1.  Na liście rozwijanej **Makro** wybierz makro.
2.  Wprowadź **Tekst menu**. Będzie to nazwa używana do identyfikacji polecenia makra i pojawi się również na pasku narzędzi, jeśli nie będzie ikony.
3.  Opcjonalnie wpisz **podpowiedź do narzędzia**. Tekst ten pojawi się w pobliżu miejsca, w którym znajduje się mysz po najechaniu na ikonę paska narzędzi.
4.  Opcjonalnie wprowadź tekst statusu. Ten tekst pojawi się na [pasku stanu](Status_bar.md) po najechaniu kursorem na ikonę paska narzędzi.
5.  Opcjonalnie w polu wejściowym „Co to jest" wprowadź stronę Wiki dla makra, jeśli powstała. Wpisz nazwę strony, a nie pełny adres URL.
6.  Opcjonalnie wprowadź skrót w polu edycji **skrót klawiaturowy**. Zobacz sekcję [Klawiatura](#Klawiatura.md), aby uzyskać więcej informacji.
7.  Aby dodać ikonę:
    1.  Naciśnij przycisk **Pixmap** **...**
    2.  Otworzy się okno dialogowe **Wybierz Ikonę**.
    3.  W razie potrzeby naciśnij przycisk **Folder ikonek...** aby dodać folder z ikonkami.
    4.  Wybierz ikonę z panelu. Okno dialogowe Wybierz ikonę zamknie się automatycznie.
8.  Wciśnij przycisk **dodaj**.
9.  Polecenie nowej makrodefinicji pojawi się w panelu po lewej stronie.
10. Polecenie utworzonej makrodefinicji można teraz wybrać na karcie [Paski narzędzi](#Paski_narzędzi.md).

#### Usuwanie makropolecenia 

1.  Wybierz makropolecenie w panelu po prawej stronie.
2.  Wciśnij przycisk **Skasuj**.

#### Modyfikacja makropolecenia 

1.  Dwukrotnie kliknij na polecenie makra w panelu po lewej stronie.
2.  Dokonaj wymaganych zmian. Zauważ, że nie można usunąć ikony, można ją tylko wymienić.
3.  Naciśnij przycisk **Replace**.


{{Top}}

### Spaceball ruchy 

Ta karta jest pusta, jeśli nie wykryto tego typu manipulatora. Patrz: [urządzenia wejściowe 3Dconnexion](3Dconnexion_input_devices.md). {{Top}}

### Spaceball przyciski 

Ta karta jest pusta, jeśli nie wykryto tego typu manipulatora. Patrz: [urządzenia wejściowe 3Dconnexion](3Dconnexion_input_devices.md). {{Top}}

## Motywy

FreeCAD obsługuje kompletną personalizację interfejsu, poprzez arkusze stylów .qss. Format _.

Możesz również stworzyć własny motyw, jeśli nie odpowiada Ci motyw dołączony do programu FreeCAD, na przykład poprzez edycję [istniejącego arkusza stylów](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Twój nowy styl musi być umieszczony w określonym folderze, aby został znaleziony przez FreeCAD:

-    {{FileName|$HOME/.FreeCAD/Gui/Stylesheets}}*(Linux)*.

-    {{FileName|$HOME/Library/Preferences/FreeCAD/Gui/Stylesheets}}*(MacOS)*.

-    {{FileName|%APPDATA%/FreeCAD/Gui/Stylesheets}}*(Windows)*. Lokalizację folderu {{FileName|%APPDATA%}} można uzyskać poprzez wpisanie {{Incode|App.getUserAppDataDir()}} w [konsoli Python](Python_console/pl.md).


{{Top}}

## Dodatki

Dodatki oferują jeszcze jeden sposób na dostosowanie interfejsu użytkownika. Poniżej znajduje się kilka dodatków stworzonych przez użytkowników w społeczności FreeCAD. Można je pobrać poprzez <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Menadżer dodatków](Std_AddonMgr/pl.md) *(uwaga: są one wymienione w zakładce Środowiska pracy)*.

### Menu kostki nawigacyjnej 

-   repozytorium Github: <https://github.com/triplus/CubeMenu>

### Przeźroczystość

-   repozytorium Github: <https://github.com/triplus/Glass>

### Zestawy ikon 

-   repozytorium Github: <https://github.com/triplus/IconThemes>

### Starter

-   repozytorium Github: <https://github.com/triplus/Launcher>

### PieMenu

-   repozytorium Github: <https://github.com/triplus/PieMenu>

### RemBench

-   repozytorium Github: <https://github.com/triplus/RemBench>

### Skróty

-   repozytorium Github: <https://github.com/triplus/ShortCuts>


{{Top}}





{{Std Base navi

}} {{Interface navi}}

---
[documentation index](../README.md) > Interface Customization/pl
