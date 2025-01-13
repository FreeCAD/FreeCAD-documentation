---
 GuiCommand:
   Name: WebTools Git
   Name/pl: WebTools: Git‏‎
   MenuLocation: Web Tools , Git
   Workbenches: WebTools_Workbench/pl
   Version: 0.17
---

# WebTools Git/pl


**Począwszy od FreeCAD v0.17, narzędzie to zostało usunięte ze środowiska Architektura i jest teraz częścią zewnętrznego środowiska pracy [Narzędzia Web](WebTools_Workbench/pl.md), które można zainstalować poprzez menu Narzędzia → <img src="images/AddonManager.svg" width=24px> [Menadżer dodatków](Std_AddonMgr/pl.md).
**



## Opis

To polecenie umożliwia zarządzanie bieżącym dokumentem za pomocą [GIT](https://en.wikipedia.org/wiki/Git_%28software%29). GIT to potężny system kontroli wersji plików, który może zarządzać różnymi wersjami plików i śledzić zmiany.

Git jest złożonym narzędziem, przed jego użyciem warto zapoznać się z jego podstawami, aby uniknąć błędnych operacji, które mogą spowodować utratę danych. Obfita literatura na temat GIT jest dostępna i łatwa do znalezienia w Internecie.

**Wymagania wstępne:** Aby móc korzystać z tego polecenia, w systemie musi być zainstalowany pakiet [gitpython](https://github.com/gitpython-developers/GitPython). W większości dystrybucji Linuksa gitpython jest dostępny w standardowych repozytoriach oprogramowania jako {{Incode|gitpython}} lub {{Incode|python-git}}.



## Użycie

1.  Upewnij się, że okno [Widok raportów](Report_view/pl.md) jest otwarte, ponieważ będą tam wyświetlane komunikaty Git.
2.  Zapisz bieżący aktywny dokument, upewniając się, że zapisany plik znajduje się w istniejącym repozytorium git. Może on znajdować się w podkatalogu.
3.  Wybierz z menu **Web Tools → <img src="images/WebTools_Git.svg" width=16px> '''Git'''
**
4.  Otworzy się [Panel zadań](Task_panel/pl.md) w [widok połączonym](Combo_view/pl.md).



## Opcje

![Zakładka Zadania pokazująca interfejs Git.](images/Arch_Git_panel.jpg )

-   Przycisk **Log** spowoduje wyświetlenie okna dialogowego zawierającego najnowsze wpisy dziennika. Dane wyjściowe odpowiadają git log.
-   Przycisk **Odśwież** spowoduje ponowne przeskanowanie repozytorium w poszukiwaniu zmienionych plików. Po zapisaniu pracy należy wykonać ręczne odświeżenie.
-   Przycisk **Porównaj** pokaże różnice pomiędzy aktualną wersją wybranego pliku, a najnowszą wersją przechowywaną w repozytorium. Dane wyjściowe odpowiadają git diff.
    -   Domyślnie wykonywana jest różnica binarna, musisz skonfigurować narzędzie fcinfo do porównywania tekstowego.
-   Przycisk **Wybierz wszystko** spowoduje wybranie wszystkich plików do zatwierdzenia.
-   Przycisk **Zatwierdź** zatwierdzi wybrane pliki. Pamiętaj, aby napisać wiadomość zatwierdzenia opisującą wprowadzane zmiany.
-   Przycisk **Pull** spowoduje **pobranie** wszelkich nowych zmian w repozytorium z wybranego pilota. Jeśli plik aktualnie otwarty we FreeCAD jest modyfikowany przez ściągnięcie, pojawi się komunikat ostrzegawczy, abyś mógł albo zapisać plik ponownie, albo zapisać go gdzie indziej.
-   Przycisk **Push** spowoduje **przesłanie** najnowszych zatwierdzeń do wybranego pilota.



## Ograniczenia

-   Narzędzie nie może jeszcze tworzyć nowych repozytoriów. Musisz mieć już utworzone istniejące lokalne repozytorium. (FreeCAD sprawdzi, czy bieżący plik dokumentu znajduje się w repozytorium Git).
-   Narzędzie nie może zmieniać ani tworzyć gałęzi. Należy to zrobić ręcznie za pomocą standardowych narzędzi Git.



## Włączenie czytelnych dla człowieka różnic dla plików FCStd za pomocą narzędzia fcinfo 

Format pliku FreeCAD [FCStd](File_Format_FCStd/pl.md) jest formatem binarnym opartym na zip, dla którego Git nie może generować poprawnych różnic. Oznacza to, że nie można zobaczyć, co zmieniło się między jedną wersją a drugą, a także, że każda nowa wersja przechowywana w repozytorium Git jest pełną kopią pliku.

Chociaż drugi problem nie ma obecnie rozwiązania, pierwszy można rozwiązać za pomocą małego narzędzia dostępnego w kodzie źródłowym FreeCAD, o nazwie [fcinfo](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/fcinfo). Git może zostać poproszony o użycie narzędzia fcinfo do wydrukowania przyjaznego dla człowieka raportu pliku FCStd, a gdy zostanie poproszony o porównanie dwóch plików FCStd, zamiast tego wygeneruje porównanie dwóch raportów fcinfo. Należy pamiętać, że jest to tylko wizualna informacja zwrotna, pełna kopia pliku będzie nadal przechowywana wewnętrznie.

Przykładowe porównanie uzyskane za pomocą fcinfo:


```python
diff --git a/testhouse.FcStd b/testhouse.FcStd
index 08077b6..985b1d8 100644
--- a/testhouse.FcStd
+++ b/testhouse.FcStd
@@ -1,26 +1,25 @@
-Document: /tmp/43un09_testhouse.FcStd (442K)
-   SHA1: 67c1985a45d93cba57d5bf44490897aba460100d
+Document: /tmp/zfXoDd_testhouse.FcStd (370K)
+   SHA1: db1cb5fca18af7bfdca849028f40550df4d845cb
    Comment : This is a test house to showcase FreeCAD's BIM worflow and IFC export capabilities
    Company : uncreated.net
    CreatedBy : Yorik van Havre
    CreationDate : Fri May  9 12:05:54 2014 
    FileVersion : 1
    Id : 
-   Label : testhouse
-   LastModifiedBy : Yorik van Havre
-   LastModifiedDate : 2016-06-28T17:05:57-03:00
+   Label : testhouse2
+   LastModifiedBy : Yorik van Havre
+   LastModifiedDate : Sat Sep 13 20:46:36 2014
+
    License : CC-BY 3.0
    LicenseURL : http://creativecommons.org/licenses/by/3.0/
-   ProgramVersion : 0.17R7800 (Git)
-   TipName : 
+   ProgramVersion : 0.15R3989 (Git)
    Uid : 67e62d8a-6674-4358-92fe-615443be887a
-   Objects: (231)
+   Objects: (221)
        Annotation : Drawing::FeatureViewAnnotation
        Annotation001 : Drawing::FeatureViewAnnotation
        Annotation002 : Drawing::FeatureViewAnnotation
        Annotation003 : Drawing::FeatureViewAnnotation
-       Annotation004 : Drawing::FeatureViewAnnotation
-       Annotation005 : Drawing::FeatureViewAnnotation
        Array : Part::FeaturePython (9K)
        Box : Part::Box (2K)
        Building : App::DocumentObjectGroupPython
@@ -110,7 +109,7 @@ Document: /tmp/43un09_testhouse.FcStd (442K)
        Floor : App::DocumentObjectGroupPython
        Floor001 : App::DocumentObjectGroupPython
        Floor002 : App::DocumentObjectGroupPython
-       Frame : Part::FeaturePython (89K)
```

Każdy plik FreeCAD zawiera numer sumy kontrolnej SHA1, który zmienia się za każdym razem, gdy plik jest zapisywany, nawet jeśli żadna zawartość nie została zmieniona. Tak więc fcinfo zawsze coś wydrukuje, bez względu na zmiany zawartości.

Aby umożliwić korzystanie z fcinfo *(tylko Linux i Mac)*.



### Korzystanie z fcinfo w jednym repozytorium Git 

Oto kroki, aby umożliwić korzystanie z narzędzia fcinfo na podstawie repozytorium.

-   Zapisz plik fcinfo gdzieś w ścieżce systemowej.

:   Uwaga: Od 2023-12-09 w systemach Arch Linux skrypt {{Incode|fcinfo}} jest dołączony do pakietu {{Incode|freecad}}, [łatka tutaj](https://gitlab.archlinux.org/archlinux/packaging/packages/freecad/-/commit/4419bfbfdb670abebd7f2e6ed93194e819781f7d).

-   Uczyń go wykonywalnym.

:   Uwaga: Od 2023-12-09 na systemach Arch Linux skrypt {{Incode|fcinfo}} jest dostępny pod adresem {{Incode|/usr/bin/fcinfo}}.

-   Utwórz plik {{Incode|.gitattributes}} w swoim repozytorium Git i dodaj do niego następujący wiersz:

:   
    {{Code|lang=text|code=
    *.FCStd diff=fcinfo
    }}
    

-   Dodaj następujące linie do pliku {{Incode|.gitconfig}} w swoim katalogu domowym:

:   
    {{Code|lang=text|code=
    [diff "fcinfo"]
    textconv = /path/to/fcinfo
    }}
    

-   Alternatywnie, jeśli chcesz wywołać fcinfo z argumentami (np. {{Incode|--gui}}) użyj [this approach](https://stackoverflow.com/questions/55601430/how-to-pass-a-filename-argument-gitconfig-diff-textconv):

:   
    {{Code|lang=text|code=
    [diff "fcinfo"]
    textconv = sh -c '/path/to/fcinfo --gui "$0"'XD
    }}
    

Zauważ, że jeśli pracujesz we wspólnym projekcie, możesz chcieć dołączyć narzędzie fcinfo do swojego repozytorium, w takim przypadku ścieżka jest względna do katalogu głównego repozytorium Git.



### Włączenie fcinfo globalnie 

Jeśli pracujesz nad wieloma projektami, które wymagają narzędzia fcinfo, możesz włączyć je globalnie dla swojego użytkownika.

-   Utwórz plik {{Incode|$HOME/.config/git/attributes}} i dodaj do niego następującą linijkę:

:   
    {{Code|lang=text|code=
    *.FCStd diff=fcinfo
    }}
    

-   Dodaj następujące linie do pliku {{Incode|$HOME/.config/git/config}}:
    -   Odpowiednik tego polecenia to {{Incode|git config --global diff.fcinfo.textconv "/path/to/fcinfo"}}.
    -   Użytkownicy systemu Arch Linux korzystający z pakietu {{Incode|freecad}} mogą używać {{Incode|textconv = fcinfo}}, ponieważ jest on już zainstalowany w ich systemie.

:   
    {{Code|lang=text|code=
    [diff "fcinfo"]
    textconv = /path/to/fcinfo
    }}
    

Zauważ, że wszelkie konfiguracje dokonane na poziomie repozytorium zastępują konfiguracje globalne.



---
⏵ [documentation index](../README.md) > WebTools Git/pl
