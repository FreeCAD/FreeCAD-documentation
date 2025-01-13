# CAM Tools/pl
}









## Opis

Ta strona opisuje architekturę narzędzi *(ToolBit)* używaną w środowisku pracy [CAM](CAM_Workbench/pl.md), które stało się domyślne dla FreeCAD v0.19. Narzędzia w środowisku pracy CAM są obsługiwane inaczej niż w innych pakietach [CAM](https://en.wikipedia.org/wiki/Computer-aided_manufacturing).

Istnieje kilka pojęć, które użytkownik musi zrozumieć:

-   [CAM: Profil narzędzia](CAM_ToolShape/pl.md): to szablony do tworzenia końcówek narzędzi. Są to dokumenty FreeCAD, które modelują narzędzie za pomocą nazwanych wiązań. Profil narzędzia jest *abstrakcyjnym* szablonem narzędzia, z którego tworzone są instancje narzędzi (nazywane końcówkami narzędzi - *toolbits*). Na przykład wszystkie frezy końcowe będą korzystać z tego samego pliku profilu narzędzia (*toolshape*).

-   [CAM: Końcówki narzędzi](CAM_ToolBit/pl.md): to instancje profili narzędzi. Końcówka narzędzia będzie miała określone wartości dla każdego z nazwanych wiązań w profilu narzędzia. Końcówki narzędzia są używane w zadaniach CAM za pośrednictwem kontrolera narzędzi (TC). Ta sama końcówka narzędzia może istnieć w wielu bibliotekach.

-   [CAM: Biblioteka narzędzi](CAM_ToolBit_Library/pl.md): zawiera dowolny zestaw (końcówek) narzędzi. Konkretne narzędzia w bibliotece zależą całkowicie od użytkownika. Przykłady użycia bibliotek:
    -   Użytkownik hobbysta może mieć tylko jedną bibliotekę zawierającą wszystkie posiadane narzędzia.
    -   Biblioteka może zawierać wszystkie narzędzia używane do pracy z konkretnym materiałem, takim jak aluminium czy drewno.
    -   Biblioteka może zawierać narzędzia przeznaczone do pracy z określonym materiałem.
    -   Biblioteka może zawierać narzędzia od konkretnego dostawcy.
    -   Biblioteka może odpowiadać układowi automatycznej wymiany narzędzi.

[CAM: Kontroler narzędzi](CAM_ToolController/pl.md) kontroluje, w jaki sposób narzędzie jest używane w zadaniu CAM. Kontroler łączy narzędzie z właściwościami takimi jak prędkość wrzeciona, kierunek oraz prędkości posuwu w poziomie i pionie.

 ===Okno dialogowe==

Użytkownik będzie wchodził w interakcję z systemem zarządzania narzędziami za pośrednictwem menu CAM w dwóch różnych przepływach pracy. Każdy przepływ pracy ma dedykowane elementy GUI.

-    **<img src="images/CAM_ToolBitLibraryOpen.svg" width=24px> [Tabela narzędzi](CAM_ToolBitDock/pl.md)**\- widok oznaczony na górze jako *Tabela narzędzi*, służący do korzystania z narzędzi w zadaniu CAM poprzez tworzenie kontrolerów narzędzi.

-    **<img src="images/CAM_ToolBitDock.svg" width=24px> [Edytor biblioteki narzędzi](CAM_ToolBitLibraryOpen/pl.md)**do zarządzania kolekcją narzędzi użytkownika za pomocą przycisków *Utwórz narzędzie*, *Dodaj istniejące* i *Usuń*.



## Organizowanie

Po zainstalowaniu FreeCAD przykładowa hierarchia bibliotek narzędzi i zestawów narzędzi jest tworzona w katalogu instalacyjnym pod adresem:

-   W systemie Linux jest to zazwyczaj **/usr/lib64/FreeCAD/Mod/CAM/Tools**.
-   Na macOS jest to zazwyczaj **/Applications/FreeCAD.app/Contents/Resources/Mod/CAM/Tools**.
-   W systemie Windows jest to zazwyczaj **C:\Program Files\FreeCAD\Mod\CAM\Tools**.




    Tools
      + Bit
      + Library
      + Shape

Zawsze zaleca się przechowywanie nowo utworzonych zestawów narzędzi i bibliotek w bezpiecznej lokalizacji, aby uniknąć ich nadpisania podczas aktualizacji programu. Nawet niestandardowe kształty narzędzi mogą być przechowywane w dowolnych lokalizacjach, w których można tworzyć ich kopie zapasowe. Zachęcamy jednak użytkownika do korzystania z porównywalnej struktury logicznej, jak pokazano powyżej, aby zachować dobrą organizację zestawów narzędzi i bibliotek.

Po otwarciu Menedżer biblioteki narzędzi CAM sprawdza lokalizację katalogu roboczego. Jeśli lokalizacja nie jest zapisywalna lub jest taka sama jak przykładowa/domyślna lokalizacja, środowisko CAM poprosi użytkownika o wybranie lub utworzenie nowego katalogu roboczego, który zwykle domyślnie jest katalogiem makrodefinicji użytkownika.

Kopie domyślnych narzędzi i bibliotek są kopiowane do tego katalogu. Możesz teraz zarządzać swoimi narzędziami, na przykład kopiować, edytować i tworzyć kształty narzędzi, narzędzia i biblioteki, a zmiany zostaną zachowane. Zauważ, że kształty narzędzi nie są kopiowane, ponieważ obecność duplikatów może powodować błędy. Zobacz raport GitHub [CAM: Tool shapes not copied by \"Setup ToolBit working directory\" #15275](https://github.com/FreeCAD/FreeCAD/issues/15275).



## Opcje

Odwołania do narzędzi i ich kształtów mogą być przechowywane za pomocą ścieżki bezwzględnej lub ścieżki względnej do ścieżki wyszukiwania. Ogólnie zaleca się stosowanie ścieżek względnych ze względu na ich elastyczność i odporność na zmiany układu. Jeśli w różnych katalogach istnieje wiele narzędzi lub kształtów narzędzi o tej samej nazwie, może być konieczne użycie ścieżek bezwzględnych.

Zobacz [CAM: Ustawienia](CAM_Preferences/pl.md) aby wybrać czy używane będą ścieżki bezwzględne czy względne.



## Migracja ze starszych narzędzi 

Jeśli korzystasz z modułu CAM we FreeCAD od jakiegoś czasu, może być konieczne dostosowanie ustawień przed rozpoczęciem korzystania z systemu narzędzi. Jeśli po naciśnięciu przycisku Biblioteki narzędzi na pasku narzędzi pojawia się starsze okno dialogowe, przejdź do strony w [CAM: Ustawienia](CAM_Preferences/pl.md) i wyłącz starsze narzędzia.
Aby zmiana była skuteczna, musisz ponownie uruchomić FreeCAD.

![Wyłączanie starszych narzędzi](images/Preferences.png )



## Początki pracy z narzędziami we FreeCAD 0.19 

Przeczytaj sekcję [Migracja ze starszych narzędzi](#Migracja_ze_starszych_narzędzi.md) powyżej. Poniższe kroki przeprowadzą Cię przez proces dodania narzędzia do danego **<img src="images/CAM_Job.svg" width=16px> [zadania CAM](CAM_Job/pl.md)**.

W skrócie, proces rozpoczyna się od pliku kształtu narzędzia (profilu), który zawiera jedynie szkic we FreeCAD połowy fizycznego kształtu narzędzia (profilu). Ten plik kształtu narzędzia jest następnie wykorzystywany jako podstawa do stworzenia pliku narzędzia zawierającego trójwymiarową reprezentację narzędzia lub frezu. Jedno lub więcej narzędzi może być przypisanych do dowolnej liczby bibliotek narzędzi, zgodnie z potrzebami użytkownika. Taka struktura i przepływ pracy umożliwiają dzielenie się kształtami narzędzi, narzędziami i całymi bibliotekami narzędzi, co stanowi ogromny krok naprzód w porównaniu z poprzednim systemem zarządzania narzędziami, który istniał przed wersją 0.19.



### Zweryfikuj lub utwórz kształt narzędzia 

Dodawanie frezu lub narzędzia do zadania CAM w celu użycia go w operacjach rozpoczyna się od [kształtu narzędzia](CAM_ToolShape/pl.md). Ten krok weryfikacji lub tworzenia kształtu narzędzia nie jest konieczny, jeśli masz już dostępne istniejące narzędzie.



#### Upewnij się, że Twój kształt narzędzia istnieje 

-   FreeCAD zawiera zestaw powszechnych kształtów narzędzi z każdą dystrybucją. Odwiedź stronę [CAM: Profil narzędzia](CAM_ToolShape/pl.md), aby zobaczyć listę dołączonych, powszechnych kształtów narzędzi.
-   Możesz mieć dodatkowe pliki kształtów narzędzi dostępne w swoich osobistych plikach.
-   Zwróć uwagę na większą [organizację](CAM_Tools/pl#Organizowanie.md) systemu narzędzi, jak wspomniano powyżej.



#### Utwórz nowy kształt narzędzia 

:   Podążaj za instrukcjami przedstawionymi w sekcji [Użycie](CAM_ToolShape/pl#Usage.md) strony [CAM: Profil narzędzia](CAM_ToolShape/pl.md) aby utworzyć własny kształt narzędzia.



### Załaduj lub utwórz narzędzie 

Po utworzeniu żądanego kształtu narzędzia (profilu), musisz stworzyć [narzędzie](CAM_ToolBit/pl.md) używając tego kształtu narzędzia (profilu).

1.  W menu <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [środowiska pracy CAM](CAM_Workbench/pl.md), przejdź do **CAM → Utwórz narzędzie**.
2.  W panelu zadań tworzenia [narzędzia](CAM_ToolBit/pl.md) który się pojawi, nadaj nowemu narzędziu nazwę i wybierz odpowiedni plik kształtu narzędzia jako bazę dla tego nowego narzędzia.
3.  Powinna pojawić się miniatura wybranego kształtu narzędzia wraz z listą parametrów.
4.  Ustaw parametry narzędzia według potrzeb.
5.  Kliknij **OK**, aby zapisać nowe narzędzie.
6.  Nowe narzędzie pojawi się w drzewie obiektów FreeCAD.



### Zapisz nowe narzędzie 

1.  Zlokalizuj i wybierz nowe narzędzie w drzewie obiektów w głównym oknie FreeCAD.
2.  W menu <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [środowiska pracy CAM](CAM_Workbench/pl.md), przejdź do **CAM → Zapisz narzędzie jako...**.
3.  Wyskoczy okno dialogowe.
4.  Przejdź do folderu, w którym chcesz zapisać nowy plik narzędzia.
5.  Wprowadź nazwę pliku dla narzędzia.
6.  Kliknij przycisk **Zapisz**.



### Zarejestruj narzędzie w bibliotece narzędzi 

1.  W menu <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [środowiska pracy CAM](CAM_Workbench/pl.md), przejdź do **CAM → Otwórz edytor biblioteki narzędzi**.
2.  Otworzy się okno [Menadżera bibliotek narzędzi](CAM_ToolBitLibraryOpen/pl.md).
3.  Na górze tego okna, zweryfikuj lub ustaw ścieżkę do folderu zawierającego istniejące biblioteki narzędzi lub lokalizację, w której chcesz przechowywać swoje biblioteki narzędzi.
4.  Pod polem ścieżki, po lewej stronie znajduje się obszar listy bibliotek narzędzi. Kliknij istniejącą bibliotekę narzędzi, którą chcesz użyć jako miejsce docelowe dla nowego narzędzia, lub kliknij zielony symbol plus, aby utworzyć nową bibliotekę narzędzi w wyżej określonym folderze.
5.  Po prawej stronie okna edytora bibliotek narzędzi znajduje się lista narzędzi i przyciski akcji dla aktualnie wybranej biblioteki narzędzi. Kliknij ikonę **Dodaj narzędzie**.
6.  W oknie nawigacji plików, które się otworzy, przejdź do nowego narzędzia, wybierz je i kliknij przycisk **Otwórz**. Nowe narzędzie zostanie dodane do aktywnej biblioteki narzędzi.
7.  Upewnij się, że klikniesz przycisk **Zapisz tabelę** na dole okna Biblioteki narzędzi, aby zapisać zmiany.
8.  Pozostaw to okno Biblioteki narzędzi otwarte na następny krok.
9.  Gdy Twoje narzędzia są już utworzone i zapisane w Bibliotece narzędzi, możesz je ponownie wykorzystać.



### Dodaj kontroler narzędzia do zadania 

1.  W otwartym oknie Biblioteki narzędzi, zlokalizuj i aktywuj pożądaną bibliotekę narzędzi.
2.  Wybierz pożądane narzędzia, które mają zostać dodane do zadania. Aby wybrać wiele narzędzi, przytrzymaj klawisz CTRL podczas wybierania.
3.  Kliknij przycisk **Dodaj kontroler narzędzia do zadania**.
4.  Zamknij Bibliotekę narzędzi.



## Powiązane

-   [CAM: Końcówki narzędzi](CAM_ToolBit/pl.md)
-   [CAM: Edytor biblioteki narzędzi](CAM_ToolBitLibraryOpen/pl.md)





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Tools/pl
