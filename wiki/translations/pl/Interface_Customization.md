# Interface Customization/pl
{{TOCright}}



## Wprowadzenie

Interfejs FreeCAD jest oparty na nowoczesnym zestawie narzędzi [Qt](http://en.wikipedia.org/wiki/Qt_(toolkit)) i posiada nowoczesną organizację. Niektóre aspekty interfejsu mogą być dostosowane do indywidualnych potrzeb. Możesz na przykład dodać niestandardowe paski narzędzi, z narzędziami z kilku Środowisk pracy lub narzędziami zdefiniowanymi w makrach, a także tworzyć własne skróty klawiaturowe. Ale menu i domyślne paski narzędzi, które są dostarczane z programem FreeCAD i jego warsztatami nie mogą być zmieniane.


{{Version/pl|0.21}}

: Zakładka ta nie jest już dostępna. Jej funkcjonalność została przeniesiona do zakładki [dostępne środowiska pracy](#Środowiska_pracy.md) w sekcji środowiska pracy [Edytora Preferencji](Preferences_Editor/pl.md).

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*Okno dialogowe Dostosowywanie interfejsu*



## Użycie

1.  Polecenia dostępne w oknie dialogowym Dostosowywania zależą od aktywnych programów roboczych, które zostały załadowane w bieżącej sesji programu FreeCAD. Należy więc najpierw załadować wszystkie programy, do których chcemy mieć dostęp.
2.  Istnieje kilka sposobów wywołania polecenia <img alt="" src=images/Std_DlgCustomize.svg  style="width:16px;"> [Std: Dostosuj](Std_DlgCustomize/pl.md):
    -   Wybierz polecenie z menu **Przybory → <img src="images/Std_DlgCustomize.svg" width=16px> Dostosuj...**.
    -   Kliknij prawym przyciskiem myszy na obszarze paska narzędzi i wybierz z menu kontekstowego **<img src="images/Std_DlgCustomize.svg" width=16px> Dostosuj...**.
3.  Otworzy się okno dialogowe Dostosuj\... Więcej informacji można znaleźć w rozdziale [Opcje](#Opcje.md).
4.  Przycisk **Pomocy** uruchamia polecenie <img alt="" src=images/Std_WhatsThis.svg  style="width:16px;"> [Co to jest](Std_WhatsThis/pl.md).
5.  Naciśnij przycisk **Zamknij**, aby zamknąć okno dialogowe.



## Opcje

W oknie dialogowym Dostosuj dostępne są następujące zakładki:



### Klawiatura

![](images/Std_DlgCustomize_tab_Keyboard.png ) 
*Zakładka Klawiatura*

Na tej karcie można zdefiniować własne skróty klawiaturowe. W zakładce [Makrodefinicje](#Makrodefinicje.md) można zdefiniować skróty dla poleceń makro.



#### Wyszukiwanie

Polecenia można wyszukiwać, wprowadzając co najmniej 3 znaki tekstu dla menu lub nazwy w polu wyszukiwania. Wielkość liter nie ma znaczenia.

Możliwe jest również wyszukiwanie skrótów:

-   W polu wyszukiwania klawisze specjalne w skrótach muszą być wprowadzane jako ciągi znaków. Na przykład, aby wyszukać polecenia, które używają **Ctrl** w swoim skrócie, wpisz {{Value|ctrl}} *(4 litery)*.
-   Dodaj nawiasy, aby wyszukać skróty składające się z pojedynczych znaków, na przykład: {{Value|(c)}}.
-   Dodaj przecinek i spację między znakami skrótów wieloznakowych, na przykład: {{Value|g, b, b}}.



#### Dodaj skrót 

1.  Wybierz kategorię poleceń z listy rozwijanej **Kategoria**.
2.  Wybierz polecenie z panelu **Komendy**.
    -   Opcjonalnie kliknij nagłówki kolumn {{Value|Polecenie}}, {{Value|Skrót}} lub {{Value|Domyślnie}}, aby zmienić kolejność listy.
    -   Opcjonalnie przeciągnij element rozdzielający na prawo od panelu, aby zmienić jego rozmiar.
3.  Pole *Bieżący skrót* wyświetla bieżący skrót, jeśli jest dostępny.
4.  Wprowadź nowy skrót w polu *Nowy skrót*. Skróty mogą mieć długość do 4 znaków. Każde wejście jest pojedynczym znakiem, kombinacją jednego lub więcej klawiszy specjalnych lub kombinacją jednego lub więcej klawiszy specjalnych i znaku. Użyj klawisza **Backspace**, aby poprawić błędy.
5.  Inne aktywne polecenia (patrz [Notatki](#Notatki.md)), które już używają skrótu, będą wymienione na **Liście priorytetów skrótów**.
6.  Naciśnij przycisk **Przypisz**, aby przypisać nowy skrót.
7.  Jeśli *Lista priorytetów skrótów* zawiera więcej niż jedno polecenie: opcjonalnie można zmienić kolejność, wybierając poszczególne polecenia i naciskając przycisk **W górę** lub **W dół**. Jeśli aktywne polecenia mają ten sam skrót, uruchomiony zostanie skrót znajdujący się najwyżej na liście.



#### Usuwanie skrótu 

1.  Wybierz kategorię poleceń z listy rozwijanej \"Kategoria\".
2.  Wybierz polecenie z panelu **Polecenia**.
3.  Naciśnij przycisk **Wyczyść**.



#### Przywracanie domyślnego skrótu 

1.  Wybierz kategorię polecenia z listy rozwijanej **Kategoria**.
2.  Wybierz polecenie z panelu **Polecenia**.
3.  Naciśnij przycisk **Reset**.



#### Przywrócenie wszystkich domyślnych skrótów 

1.  Naciśnij przycisk **Zresetuj wszystko**



#### Uwagi

-   Skróty działają tylko dla aktywnych poleceń. Aktywne polecenia to polecenia, które pojawiają się w standardowym menu lub w menu środowiska pracy, które zostało załadowane w bieżącej sesji FreeCAD, lub polecenia, które pojawiają się na *widocznym* pasku narzędzi.


{{Top}}



### Paski narzędzi 

![](images/Std_DlgCustomize_tab_Toolbars.png ) 
*Zakładka Paski narzędzi*

Na tej karcie można tworzyć i modyfikować własne paski narzędzi.



#### Wyszukiwanie 

Zobacz sekcję [Klawiatura](#Wyszukiwanie.md).



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
3.  Wybierz kategorię z listy rozwijanej po lewej stronie. W kategorii {{Value|Makra}} pojawiają się polecenia makrodefinicji, które zostały ustawione na karcie [Makrodefinicje](#Makrodefinicje.md).
4.  Wybierz opcję z panelu **Polecenia** lub wybierz {{Value|<Separator>}}, aby dodać separator *(linię między dwoma przyciskami paska narzędzi)*.
    -   Opcjonalnie przeciągnij element rozdzielający na prawą stronę panelu, aby zmienić jego rozmiar.
5.  Naciśnij przycisk **<img src="images/Button_right.svg" width=16px>**.



#### Usuwanie polecenia 

1.  W razie potrzeby, rozwiń pasek narzędzi w panelu po prawej stronie.
2.  Wybierz polecenie.
3.  Naciśnij przycisk **<img src="images/Button_left.svg" width=16px>**.



#### Zmiana pozycji polecenia 

1.  W razie potrzeby, rozwiń pasek narzędzi w panelu po prawej stronie.
2.  Wybierz polecenie
3.  Naciśnij przycisk **<img src="images/Button_up.svg" width=16px>** lub **<img src="images/Button_down.svg" width=16px>**.
4.  Opcjonalnie powtarzaj to do momentu, aż polecenie znajdzie się we właściwej pozycji.



#### Uwagi 

-   Paski narzędzi należące do aktualnego stanowiska pracy są natychmiast aktualizowane, ale po wyłączeniu / ponownym włączeniu paska narzędzi konieczna jest zmiana stanowiska pracy *(przełączenie na inne stanowisko pracy, a następnie ponowne jego włączenie)*.
-   Do aktualizacji globalnych pasków narzędzi konieczna jest zmiana stanowiska pracy *(jeżeli dodano lub usunięto polecenia)* lub ponowny start *(jeżeli zmieniono kolejność pasków narzędzi lub zmieniono nazwę paska narzędzi)*.


{{Top}}



### Makrodefinicje

![](images/Std_DlgCustomize_tab_Macros.png ) 
*Zakładka Makrodefinicje*

Na tej karcie można skonfigurować makropolecenia. Po skonfigurowaniu można je dodać do niestandardowych pasków narzędzi. Makrodefinicje instalowane za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) są konfigurowane automatycznie i dodawane do {{Value|Głownego}}paska narzędzi *(zobacz sekcję [Paski narzędzi](#Paski_narzędzi.md))*, jeśli potwierdzisz wyskakujące okienko **Dodaj przycisk** podczas procesu instalacji.

Jeśli chcesz użyć makra pobranego z innego źródła, będziesz musiał zainstalować je ręcznie. Zobacz stronę [Jak zainstalować makrodefinicje](How_to_install_macros.md), aby uzyskać więcej informacji. Należy pamiętać, że FreeCAD używa dedykowanego folderu dla makrodefinicji i tylko makrodefinicje zawarte w tym folderze mogą być skonfigurowane. Użyj opcji <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:16px;">. [Okno dialogowe Makrodefinicje](Std_DlgMacroExecute/pl.md), aby znaleźć ten folder w systemie.



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

Ta karta jest pusta, jeśli nie wykryto tego typu manipulatora. Patrz: [urządzenia wejściowe 3Dconnexion](3Dconnexion_input_devices/pl.md). 

### Spaceball przyciski 

Ta karta jest pusta, jeśli nie wykryto tego typu manipulatora. Patrz: [urządzenia wejściowe 3Dconnexion](3Dconnexion_input_devices/pl.md). 

## Motywy

FreeCAD obsługuje kompletną personalizację interfejsu, poprzez arkusze stylów .qss. Format [qss](https://doc.qt.io/qt-5/stylesheet-syntax.html) jest bardzo podobny do formatu [css](https://en.wikipedia.org/wiki/CSS) używanego na stronach internetowych, w zasadzie dodaje więcej metod, aby odnieść się do różnych widżetów i elementów interfejsu Qt. Możesz zmienić obecny domyślny motyw *(który po prostu bierze styl zdefiniowany przez system pulpitu)* poprzez wybranie **arkusza stylów** w [Edytorze ustawień](Preferences_Editor/pl#Informacje_og.C3.B3lne.md).

Możesz również stworzyć własny motyw, jeśli nie odpowiada Ci motyw dołączony do programu FreeCAD, na przykład poprzez edycję [istniejącego arkusza stylów](https://github.com/FreeCAD/FreeCAD/tree/master/src/Gui/Stylesheets). Twój nowy styl musi być umieszczony w określonym folderze, aby został znaleziony przez FreeCAD:

-    **$HOME/.FreeCAD/Gui/Stylesheets***(Linux)*.

-    **$HOME/Library/Application Support/FreeCAD/Gui/Stylesheets***(MacOS)*.

-    **%APPDATA%/FreeCAD/Gui/Stylesheets***(Windows)*. Lokalizację folderu **%APPDATA%** można uzyskać poprzez wpisanie {{Incode|App.getUserAppDataDir()}} w [konsoli Python](Python_console/pl.md).


{{Top}}



## Dodatki

Dodatki z <img alt="" src=images/Std_AddonMgr.svg  style="width:16px;"> [Menedżera dodatków](Std_AddonMgr/pl.md) oferują kolejny sposób na dostosowanie interfejsu użytkownika. Dostępnych jest kilka [Pakietów preferencji](Preference_Packs/pl.md) do zmiany [motywu](#Motywy.md).

W kategorii Środowiska pracy Menedżera dodatków można znaleźć niektóre dodatki użytkownika triplus:

-   <https://github.com/triplus/CubeMenu> *({{VersionMinus|0.20}})*
-   <https://github.com/triplus/Glass>
-   <https://github.com/triplus/IconThemes>
-   <https://github.com/triplus/Launcher>
-   <https://github.com/triplus/PieMenu>
-   <https://github.com/triplus/RemBench>
-   <https://github.com/triplus/ShortCuts>


{{Top}}





{{Std Base navi

}} {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Interface Customization/pl
