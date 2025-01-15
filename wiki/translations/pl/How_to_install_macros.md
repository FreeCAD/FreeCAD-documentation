---
 TutorialInfo:l
   Topic: Programowanie
   Level: programista średnio zaawansowany
   Time: 15 minut
   FCVersion: wszystkie
   Author: User:Mario52
---

# How to install macros/pl







## Opis

Od wersji v0.17 można łatwo dodać makrodefinicje za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md). Użytkownik nie musi robić nic więcej niż używać tego narzędzia. Czytaj dalej, aby uzyskać więcej informacji na temat instalacji [makrodefinicji](Macros/pl.md).

Makrodefinicje to sekwencje poleceń, które służą do wykonania złożonej operacji rysunkowej. Makra są skryptami środowiska [Python](Python/pl.md), co oznacza, że są to pliki tekstowe, które można pisać i edytować za pomocą edytora tekstu.

Podczas gdy skrypty Pythona zwykle mają rozszerzenie `.py`, makra FreeCAD powinny mieć rozszerzenie `.FCMacro`. Zbiór makr napisanych przez doświadczonych użytkowników znajduje się na stronie [przepisy na makra](macros_recipes.md).

Zobacz [Wprowadzenie do Pythona](Introduction_to_Python.md), aby zapoznać się z językiem programowania **Python**, a następnie [Poradnik do pisania skryptów Python](Python_scripting_tutorial.md) i [Podstawy skryptów FreeCAD](FreeCAD_Scripting_Basics.md), które pomogą Ci nauczyć się pisania makr.

Tutaj jest filmik o [instalowaniu makrodefinicji FreeCAD w Ubuntu](https://wiki.opensourceecology.org/wiki/Installing_Macros_in_FreeCAD).



## Menu i pasek narzędziowy Makrodefinicji 



### Pasek narzędzi 

-   <img alt="" src=images/Std_DlgMacroRecord.svg  style="width:32px;"> [Rejestrowanie makr\...](Std_DlgMacroRecord/pl.md)
-   <img alt="" src=images/Std_MacroStopRecord.svg  style="width:32px;"> [Zatrzymaj nagrywanie makra](Std_MacroStopRecord/pl.md)
-   <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:32px;"> [Wykonaj makro\...](Std_DlgMacroExecute/pl.md)
-   <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:32px;"> [Wykonaj makro bezpośrednio](Std_DlgMacroExecuteDirect/pl.md)

### Menu

Oprócz narzędzi na pasku dostępne są następujące funkcje w menu **Makrodefinicje**.

-   [Przełącz na debugger zewnętrzny\...](Std_MacroAttachDebugger.md)
-   <img alt="" src=images/Std_MacroStartDebug.svg  style="width:32px;"> [Debudowanie makrodefinicji](Std_MacroStartDebug/pl.md)
-   <img alt="" src=images/Std_MacroStopDebug.svg  style="width:32px;"> [Zatrzymaj debugowanie](Std_MacroStopDebug/pl.md)
-   [Krok dalej](Std_MacroStepOver/pl.md)
-   [Wejdź do](Std_MacroStepInto/pl.md)
-   [Przełącz punkt przerwania](Std_ToggleBreakpoint/pl.md)



## Katalog z makrodefinicjami 


<div class="toccolours mw-collapsible mw-collapsed">

Makra są tworzone w określonym folderze w katalogu FreeCAD użytkownika. Katalog ten można skonfigurować w oknie dialogowym [Wykonaj makrodefinicję](Std_DlgMacroExecute/pl.md) lub w [Edytorze preferencji](Preferences_Editor/pl.md), poprzez menu **Edycja → Preferencje → Python → Makropolecenia → Ustawienia ogólne dla makrodefinicji**.

Pobrane makra również powinny zostać umieszczone w tym katalogu.


<div class="mw-collapsible-content">



### Katalog domyślny 

Makra można po prostu skopiować do


```python
$ROOT_DIR/
```

gdzie `$ROOT_DIR` to ścieżka najwyższego poziomu sprawdzana przez FreeCAD przy uruchamianiu.

Katalog `$ROOT_DIR` może być katalogiem dostępnym systemowo, w takim przypadku makro będzie zainstalowane dla wszystkich użytkowników.

-   W systemie Linux zazwyczaj jest to `/usr/share/freecad/`
-   W systemie Windows zazwyczaj jest to `C:\Program Files\FreeCAD\`
-   W systemie macOS zazwyczaj jest to `/Applications/FreeCAD/`

Katalog `$ROOT_DIR` może być katalogiem przypisanym do konkretnego użytkownika.

-   W systemie Linux zazwyczaj jest to `/home/username/.local/share/FreeCAD/` (<small>(v0.20)</small> ) lub `/home/username/.FreeCAD/` ({{VersionMinus|0.19}}).
-   W systemie Windows zazwyczaj jest to `C:\Users\username\AppData\FreeCAD\`
-   W systemie macOS zazwyczaj jest to `/Users/username/Library/Preferences/FreeCAD/`



### Konfiguracja katalogu użytkownika 

1\. Otwórz menu **Makrodefinicje → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makra...](Std_DlgMacroExecute/pl.md)**, aby otworzyć [okno wykonania makra](Std_DlgMacroExecute/pl.md).

![](images/Dxf_Importer_Install_01.png ) 
*align=center|Otwieranie okna uruchamiania makra*

2\. Ustaw odpowiednią `Lokalizację makr użytkownika`.

-   Linux: zazwyczaj `/home/username/.local/share/FreeCAD/` (<small>(v0.20)</small> ) lub `/home/username/.FreeCAD/` ({{VersionMinus|0.19}})
-   Windows: zazwyczaj `C:\Users\username\AppData\Roaming\FreeCAD\`
-   MacOS: zazwyczaj `/Users/username/Library/Preferences/FreeCAD/`

![](images/Dxf_Importer_Install_02.png ) 
*align=center|Ustawianie lokalizacji makr*

3\. Przejdź do tego katalogu na swoim komputerze.

-   Linux: wklej adres do menedżera plików, takiego jak \"Nautilus\" lub inny. Możesz potrzebować nacisnąć **Ctrl**+**H**, aby wyświetlić ukryty katalog `.FreeCAD/`.
-   Windows: wklej adres do \"Eksploratora plików\" i potwierdź.
-   MacOS: zlokalizuj folder w \"Finderze\" lub wklej adres do \"Eksploratora plików\"; pamiętaj o prefiksie `file:///` dla pliku na dysku.

![](images/Dxf_Importer_Install_03.png ) 
*align=center|Otwieraie ścieżki makr w systemie operacyjnym*

4\. Dodaj pliki makr do tego katalogu.

-   Linux: pozostaw menedżera plików otwartego i dodaj lokalizację do zakładek dla szybszego dostępu.
-   Windows: pozostaw otwarty \"Eksplorator plików\".
-   MacOS: możesz pozostawić otwarte okno \"Findera\", dodać lokalizację do zakładek w \"Eksploratorze plików\", utworzyć \"Alias\", który będzie wskazywał na ten katalog, lub przeciągnąć folder do \"Pasek boczny\" w \"Finderze\", aby mieć do niego dostęp z innych programów, takich jak edytory tekstu.

![](images/Dxf_Importer_Install_04.png ) 
*align=center|Ścieżka makr*





</div>


</div>



## Instalacja makropoleceń 


<div class="toccolours mw-collapsible mw-collapsed">



### Metoda automatyczna 

Poczynając od FreeCAD 0.17, użyj [Menadżera dodatków](Std_AddonMgr/pl.md) w menu głównym **Narzędzia → Menadżer dodatków** aby zainstalować makrodefinicje, która została dołączone do repozytorium [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros).


<div class="mw-collapsible-content">

W poprzednich wersjach FreeCAD można było korzystać z dwóch automatycznych sposobów instalacji makr i innych dodatków:

-   [addons_installer.FCMacro](https://github.com/FreeCAD/FreeCAD-addons): to makro, które było poprzednikiem Menedżera dodatków i jest hostowane w repozytorium [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons). W nowych instalacjach FreeCAD nie trzeba już korzystać z tego narzędzia.
-   [freecad-pluginloader](https://github.com/microelly2/freecad-pluginloader): także makro, które można było używać do instalowania nowych komponentów w FreeCAD. Obecnie nie jest już rozwijane.

Zalecaną metodą instalacji dodatków, czyli [zewnętrznych środowisk pracy](External_workbenches/pl.md) i makr, jest [Menedżer dodatków](Std_AddonMgr/pl.md). Można jednak nadal dodawać makra do systemu za pomocą metod ręcznych opisanych w poniższych sekcjach; jest to przydatne, jeśli rozwijasz i testujesz własny kod.


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Metoda manualna 1. Skopiuj kod do edytora makrodefinicji 

W przypadku makr, które są stosunkowo małe, 300 linii lub mniej, kod można skopiować i wkleić bezpośrednio do edytora makr FreeCAD.


<div class="mw-collapsible-content">

Użyjemy <img alt="" src=images/Part_Prism_Apothem.svg  style="width:24px;"> [Macro Apothem Based Prism GUI](Macro_Apothem_Based_Prism_GUI/pl.md) jako przykładu.

1\. Przejdź do strony wiki makra, która powinna być wymieniona w [Przepisy na makra](Macro_recipes/pl.md).

Jeśli masz niestandardową ikonę, pobierz ją; kliknij na nią prawym przyciskiem myszy i wybierz `Zapisz obraz jako...`; umieść ikonę w katalogu makr. Ta ikona może być używana jako skrót do makra w [niestandardowym pasku narzędzi](Customize_Toolbars.md). Domyślną ikoną jest <img alt="" src=images/Text-x-python.png  style="width:24px;">.

![](images/Macro_Install_HowTo_28.png ) 
*align=center|Pobieranie ikony ze strony makra*

2\. Na stronie makra wybierz kod znajdujący się w sekcjach **Skrypt** lub **Makro**, a następnie skopiuj go.

3\. We FreeCAD otwórz menu **Makrodefinicje → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makrodefinicje...](Std_DlgMacroExecute/pl.md)**, aby otworzyć [okno wykonania makra](Std_DlgMacroExecute/pl.md).

![](images/Dxf_Importer_Install_01.png ) 
*align=center|Otwieranie okna uruchamiania makra*

4\. Kliknij **Utwórz**.

![](images/Macro_Install_HowTo_17.png ) 
*align=center|Tworzenie nowego makra*

5\. Wprowadź nazwę makra, tutaj `Macro_Apothem_Based_Prism_GUI` i kliknij **OK**.

![](images/Macro_Install_HowTo_18.png ) 
*align=center|Wprowadzanie nazwy makra*

6\. Zostanie otwarty edytor makra, pokazując pełną ścieżkę nowego makra.

![](images/Macro_Install_HowTo_19.png ) 
*align=center|Edytor makra*

7\. Wklej kod w oknie edytora, a następnie kliknij krzyżyk na karcie, aby zamknąć okno.

![](images/Macro_Install_HowTo_20.png ) 
*align=center|Zamykanie edytora makr*

8\. Pojawi się okno z prośbą o potwierdzenie zapisania kodu; kliknij **Tak**. Możesz również użyć **Ctrl**+**S**, aby zapisać plik.

Zrestartuj program FreeCAD aby poprawnie zarejestrować nowe makro.

![](images/Macro_Install_HowTo_27.png ) 
*align=center|Pytanie o potwierdzenie zapisania kodu*

9\. Otwórz ponownie menu **Makrodefinicje → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makrodefinicje...](Std_DlgMacroExecute.md)**, wybierz nowo dodane makro i naciśnij **Wykonaj**.

![](images/Macro_Install_HowTo_21.png ) 
*align=center|Wybieranie makra aby je uruchomić*

10\. Makro zostanie teraz uruchomione. Wypełnij pola swoimi wartościami i kliknij przycisk **OK**.

![](images/Macro_Install_HowTo_22.png ) 
*align=center|Makro w działaniu; wypełnij informacje i naciśnij OK, gdy będziesz gotowy*

11\. To makro powinno zwrócić błąd, jeśli żaden dokument nie jest aktywny; inne makra otwierają nowy dokument, jeśli żaden nie istnieje.

Utwórz nowy dokument za pomocą **Plik → <img src="images/Std_New.svg" width=16px> [Nowy](Std_New/pl.md)**, a następnie powtórz poprzednie kroki, aby uruchomić makro.

![](images/Macro_Install_HowTo_23.png) 
*align=center|Makro zwracające błąd gdy żaden dokument nie jest aktywny*

12\. Gdy aktywny dokument jest dostępny, makro uruchomi się i utworzy obiekt.

![](images/Macro_Install_HowTo_24.png ) 
*align=center|Obiekt utworzony przez makro*

13\. Możesz ponownie otworzyć makro w edytorze, aby je uruchomić lub zmodyfikować. Przejdź do **Makrodefinicje → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makrodefinicje...](Std_DlgMacroExecute/pl.md)**, wybierz makro i naciśnij **Edycja**.

![](images/Macro_Install_HowTo_25.png ) 
*align=center|Otwieranie makra w edytorze*

14\. Makro można teraz uruchomić za pomocą **Makrodefinicje → <img src="images/Std_DlgMacroExecuteDirect.svg" width=16px> [Wykonaj makrodefinicję](Std_DlgMacroExecuteDirect/pl.md)**, lub klikając przycisk **<img src="images/Std_DlgMacroExecuteDirect.svg" width=16px> [Wykonaj makrodefinicję](Std_DlgMacroExecuteDirect/pl.md)** na pasku narzędzi.

![](images/Macro_Install_HowTo_26.png ) 
*align=center|Uruchamianie makra załadowanego w edytorze*


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Metoda manualna 2. Dodanie pliku zawierającego makroinstrukcje ze skompresowanego pliku .zip 

Niektóre makra są zbyt duże, aby wygodnie kopiować je i wklejać do edytora makr, lub nie mogą być hostowane na wiki. W takim przypadku kod może być hostowany gdzie indziej, na przykład w repozytorium Github lub na [forum FreeCAD](https://forum.freecadweb.org/). Kod może być również skompresowany w pliku `.zip`, archiwum tarball `.tar.xz` lub innym typie archiwum, jeśli zawiera kilka plików. Jeśli kod jest dystrybuowany w ten sposób, archiwum należy wyodrębnić, a pliki umieścić w katalogu makr.


<div class="mw-collapsible-content">

Skorzystamy z <img alt="" src=images/Text-x-python.png  style="width:24px;"> [Macro screw maker](Macro_screw_maker1_2/pl.md) jako przykładu.

1\. Pobierz skompresowany kod z forum, [Screw Maker](http://forum.freecadweb.org/viewtopic.php?f=22&t=6558#p52887).

Aby uzyskać pliki wewnętrzne, musisz użyć narzędzia do dekompresji.

-   Dla Windows możesz użyć aplikacji takich jak [7-zip](http://www.7-zip.org/), [L-Zarc](http://www.kanmandet.dk/?p=37) lub [quickzip](http://www.quickzip.org/quickzip51.html).
-   Dla Linux możesz użyć polecenia z terminala:


```python
unzip your_file.zip -d your_directory
```

2\. Pobierz skompresowane archiwum z kodem makra do lokalnego folderu.

![](images/Macro_Install_HowTo_01.png ) 
*align=center|Pobieranie skompresowanego archiwum do ścieżki lokalnej*

3\. Zdekompresuj plik w folderze.

![](images/Macro_Install_HowTo_02.png ) 
*align=center|Dekompresowanie pliku w folderze*

4\. Dekompresor tworzy nową ścieżkę z rozpakowanymi plikami.

![](images/Macro_Install_HowTo_03.png ) 
*align=center|Nowa ścieżka utworzona po rozpakowaniu archiwum*

5\. Przejdź do nowej ścieżki i skopiuj lub wytnij plik makra.

![](images/Macro_Install_HowTo_04.png ) 
*align=center|Wprowadzanie nowo utworzonej ścieżki ze zdekompresowanym plikiem makra*

6\. Przejdź do ścieżki makr i wklej tam plik.

![](images/Macro_Install_HowTo_05.png ) 
*align=center|Umieszczanie pliku makra w ścieżce makr*

7\. We FreeCAD, otwórz menu **Makrodefinicje → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Makrodefinicje...](Std_DlgMacroExecute/pl.md)** aby otworzyć [okno uruchamiania makra](Std_DlgMacroExecute/pl.md).

![](images/Macro_Install_HowTo_06.png ) 
*align=center|Otwieranie okna uruchamiania makra*

8\. Wybierz nowe makro i wciśnij **Wykonaj**.

![](images/Macro_Install_HowTo_07.png ) 
*align=center|Wybieranie makra do uruchomienia go*

9\. Makro jest teraz uruchomione. Wybierz odpowiednie opcje i wciśnij przycisk **Utwórz**.

<img alt="" src=images/Macro_Install_HowTo_08.png  style="width:640px;"> 
*align=center|Makro w działaniu: wybierz odpowiednie opcje i wciśnij Utwórz gdy gotowe*

![](images/Macro_Install_HowTo_30.png ) 
*align=center|Obiekt utworzony przez makro*


</div>


</div>



## Wykonanie makrodefinicji w wierszu poleceń 


<div class="toccolours mw-collapsible mw-collapsed">

Uruchamianie makra z linii poleceń (.FCMacro lub .py)


<div class="mw-collapsible-content">

na Windows


```python
"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"
```

na Linux


```python
todo
```


</div>


</div>



## Błędy w makrodefinicjach 


<div class="mw-collapsible mw-collapsed">



### Błędy wcięć 

W języku programowania [Python](Python/pl.md) biała spacja na początku linii (wcięcie) jest bardzo ważna i stanowi integralną część kodu. Nieodpowiednie wcięcia mogą spowodować, że kod nie będzie działał lub wywoła błędy.

Ta sekcja opisuje niektóre błędy, które mogą wystąpić podczas kopiowania i wklejania oraz pisania kodu makr.


<div class="mw-collapsible-content">

Typowy błąd wcięcia wygląda następująco:


```python
<unknown exception traceback><type 'exceptions.IndentationError'>: ('expected an indented block', ('C:/Users/d/AppData/Roaming/FreeCAD/Macro_Apothem_Based_Prism_GUI.FCMacro', 21, 3, 'def priSm(self):\n'))
```



#### Przykład 1 

Jeśli kod nie zawiera wcięć, nie będzie działał. Definicje klas (`class`) i funkcji (`def()`), a także struktury kontrolne (`if`, `while`, `for`) powinny być następnie śledzone przez blok kodu z wcięciem.

Ten błąd może wystąpić, jeśli użytkownik nie skopiuje kodu poprawnie i wszystkie spacje zostaną przypadkowo usunięte.

![](images/Macro_Install_HowTo_09.png ) 
*align=center|Kod Pythona, któremu brakuje wcięcia; wywoła to błąd przy uruchamianiu kodu*

Problem wcięcia rozwiązany.

![](images/Macro_Install_HowTo_10.png ) 
*align=center|Kod Pythona z odpowiednim wcięciem*

Jeśli kod jest zaznaczony, wszystkie linie powinny być wyróżnione aż do lewej krawędzi, co wskazuje, że linie są wyrównane.

![](images/Macro_Install_HowTo_11.png ) 
*align=center|Podświetlenie kodu Pythona pokazujące, że wszystkie linie zaczynają się od lewej krawędzi*



#### Przykład 2 

Jeśli na początku wszystkich linii zostanie dodana dodatkowa spacja, interpreter Pythona zgłosi błąd i narzeka na niepotrzebne wcięcia. W takim przypadku należy usunąć początkową spację ze wszystkich linii.

![](images/Macro_Install_HowTo_12.png ) 
*align=center|Kod Pythona z dodatkową spacją w każdej linii*



#### Przykład 3 

Oto kod skopiowany z wątku na forum przy użyciu przycisku **Wybierz wszystko**. Wygląda na to, że zaznaczenie jest poprawne.

![](images/Macro_Install_HowTo_14.png ) 
*align=center|Kod Pythona skopiowany z forum*

Jednakże, po wklejeniu zaznaczenia do edytora makr, wydaje się, że pojawia się niepożądane wcięcie.

![](images/Macro_Install_HowTo_15.png ) 
*align=center|Kod Pythona skopiowany z forum do edytora makr; zbędne wcięcie jest dodane*

W takim przypadku należy usunąć początkowe wcięcia. Można to zrobić za pomocą specjalistycznego edytora tekstu, aby szybko zmniejszyć wcięcia w liniach.

W systemie Windows, [Notepad++](http://notepad-plus-plus.org/) umożliwia zaznaczenie tekstu przy użyciu **Alt** + przeciąganie myszą, a następnie użycie opcji **Edycja → Wcięcie → Zmniejsz wcięcie**.

![](images/Macro_Install_HowTo_16.png ) 
*align=center|Kod Pythona z odpowiednim wcięciem*



#### Przykład 4 

Tutaj zaznaczenie obejmuje także numery linii w przykładzie kodu. Jeśli to zaznaczenie zostanie wklejone do edytora makr, kod nie będzie działał. Wszystkie numery linii muszą zostać usunięte, a spacje dostosowane, aby kod Pythona miał odpowiednie wcięcia.

![](images/Macro_Install_HowTo_29.png ) 
*align=center|Zaznaczenie, które obejmuje także numery linii; jeśli ten kod zostanie wklejony do edytora makr, nie będzie działał*



#### Dobry kod 

![](images/Macro_Install_HowTo_13.png ) 
*align=center|Kod Pythona z odpowiednim wcięciem*


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">



### Brak wyjścia tekstu z makrodefinicji 

Makra mogą wyświetlać informacje w widoku raportu, aby szczegółowo opisać, co kod robi podczas jego wykonywania.

Jeśli żadna informacja nie jest wyświetlana, upewnij się, że widok raportu i konsola [Pythona](Python/pl.md) są widoczne, a wyjście jest kierowane do widoku raportu.


<div class="mw-collapsible-content">



#### Informacje dotyczące drukowania 

Makra FreeCAD mają dwa sposoby drukowania informacji w widoku raportu:

Funkcje FreeCAD


```python
FreeCAD.Console.PrintMessage("Hello World! \n")
FreeCAD.Console.PrintError("Hello World! \n")
FreeCAD.Console.PrintWarning("Hello World! \n")
```

Prosta funkcja Pythona


```python
print("Hello World!")
```



#### Uaktywnienie widoku raportu 

Aby zobaczyć informacje wyświetlane w konsoli powinieneś:

1\. Przejść do menu **Widok → Panele**.

![](images/Macro_Install_HowTo_31.png )

![](images/Macro_Install_HowTo_32.png ) 
*align=center|Uwidacznianie paneli w menu Widok → Panel*

2\. Włącz `Widok raportu` i `konsolę Pythona`.

![](images/Macro_Install_HowTo_33.png ) 
*align=center|Włączanie widoku raportu i konsoli Pythona*

3\. Panele są teraz widoczne i polecenia takie jak `FreeCAD.Console.PrintMessage()` pokazują informacje, które pojawiają się w `widoku raportu`.

![](images/Macro_Install_HowTo_34.png ) 
*align=center|Główne okno programu FreeCAD z widokiem raportu i konsolą Pythona*



#### Włączenie polecenia print() 

FreeCAD może wymagać konfiguracji, aby funkcja `print()` w [Pythonie](Python/pl.md) poprawnie przekierowywała swoje wyjście do widoku raportu.

1\. Przejdź do [Edytora preferencji](Preferences_Editor/pl.md) z menu **Edycja → Preferencje**.

![](images/Macro_Install_HowTo_35.png ) 
*align=center|Przechodzenie do edytora preferencji*

2\. Przejdź do sekcji **Python** a następnie **Okno wyników → Interpreter Pythona**.

![](images/Macro_Install_HowTo_36.png ) 
*align=center|Preferencje okna wyników*

3\. Zaznacz oba pola:

-   <img alt="" src=images/Case_a_cocher_O.png  style="width:16px;"> Przekieruj wewnętrzne wyniki Pythona do widoku raportu

-   <img alt="" src=images/Case_a_cocher_O.png  style="width:16px;"> Przekieruj wewnętrzne błędy Pythona do widoku raportu

a następnie wciśnij przycisk **OK**.

![](images/Macro_Install_HowTo_37.png ) 
*align=center|Przekierowywanie wyników Pythona do widoku raportu*

![](images/Macro_Install_HowTo_38.png ) 
*align=center|Polecenia Pythona wyświetlające informacje do widoku raportu*


</div>


</div>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > How to install macros/pl
