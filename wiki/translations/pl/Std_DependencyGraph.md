---
- GuiCommand:/pl
   Name:Std DependencyGraph
   Name/pl:Std: Graf zależności
   MenuLocation:Przybory → Graf zależności ...
   Workbenches:wszystkie
---

# Std DependencyGraph/pl



## Opis

Polecenie **Graf zależności** wyświetla zależności pomiędzy obiektami w aktywnym dokumencie w postaci *wykresu zależności*. W przeciwieństwie do [Widoku drzewa](Tree_view/pl.md), obiekty są wymienione w odwrotnym porządku chronologicznym, z obiektem utworzonym jako pierwszy na dole.

Może on być przydatny przy analizie dokumentu FreeCAD i lokalizowaniu rozwidleń w drzewie. Układ grafu zależności zależy od tego, w którym środowisku pracy zostały utworzone obiekty w dokumencie. Na przykład model wykonany wyłącznie w środowisku [Projekt Części](PartDesign_Workbench/pl.md) może wyświetlać liniowy wykres zależności z jedną pionową gałęzią. Model wykonany za pomocą działań w środowisku [Część](Part_Workbench/pl.md) będzie miał wiele gałęzi, ale dla pojedynczej części połączą się one u góry po przeprowadzonych operacjach [logicznych](Part_Boolean/pl.md). Jeśli tak się nie stanie, oznacza to, że są to osobne obiekty.

Graf zależności jest wyłącznie narzędziem wizualizacji, dlatego nie można go edytować. Podlega automatycznej aktualizacji w przypadku wprowadzenia zmian w modelu.

<img alt="" src=images/Std_DependencyGraph_example.svg  style="width:400px;"> 
*Przykład grafu zależności z korpusem Projekt Części po lewej stronie i obiektem utworzonym za pomocą operacji środowiska Część po prawej stronie.*



## Instalacja

Aby można było korzystać z poleceń, należy zainstalować oprogramowanie innej firmy o nazwie [Graphviz](http://graphviz.org/). Jeśli nie masz go wstępnie zainstalowanego lub jest on zainstalowany w niekonwencjonalnej lokalizacji, FreeCAD wyświetli następujące okno dialogowe:

![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )

### Windows

Pobierz instalator **graphviz-2.xx** ze [Graphviz strona do pobrania](https://graphviz.org/download/#windows) i uruchom go, aby wykonać instalację. Niektóre starsze wersje wydają się mieć problemy z wyświetlaniem wykresu; wersja 2.38 i nowsze są znane z niezawodności. Wszystkie wydania graphviz można znaleźć w [serwisie Gitlab](https://gitlab.com/graphviz/graphviz/-/releases).



### Mac OS 

Grafviz można zainstalować za pomocą [Homebrew](https://brew.sh/). *(Podczas instalacji Homebrew nie denerwuj się, jeśli MacOS poprosi Cię o zainstalowanie aktualizacji, np. dla narzędzi wiersza poleceń Xcode. Te aktualizacje są wykonywane później przez proces instalacji)*.


{{Code|lang=text|code=
brew install graphviz
}}

Wykona instalacje binarek graphviz pod /usr/local/bin dla macOS na Intelu, oraz /opt/homebrew dla macOS na Apple Silicon/ARM. FreeCAD sam będzie tam zaglądał. Jeśli program nie zostanie tam znaleziony zostaniemy poproszeni o podanie ścieżki. Niestety nie możemy nawigować tam bezpośrednio z okna dialogowego pliku, które pojawia się z poziomu **Przybory → Graf zależności ...**. Gdy pojawi się okno dialogowe wyboru pliku, masz dwie możliwości: Możesz użyć kombinacji klawiszy Cmd+Shift+. która pokaże Ci wszystkie ukryte elementy. Albo używasz klawiszy Cmd+Shift+G, aby uzyskać pole wejściowe dla ścieżki. Wpisz


{{Code|lang=text|code=
/usr/local/bin
}}

lub


{{Code|lang=text|code=
/opt/homebrew/bin
}}

i zatwierdzić pole wejściowe oraz okno dialogowe wyboru pliku.

W przypadku, gdy binaria Graphviz są zainstalowane w niestandardowej lokalizacji, spróbuj znaleźć program za pomocą polecenia


{{Code|lang=text|code=
type dot
}}

Wynikiem będzie coś takiego jak


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

I dlatego możesz powiedzieć programowi FreeCAD, aby szukał w tym katalogu.

### Linux

W większości dystrybucji Linuksa *(Debian / Ubuntu, Fedora, OpenSUSE)* wystarczy zainstalować pakiet graphviz z repozytoriów. Jednak podobnie jak w przypadku Mac / OSX, w przypadkach gdy binaria Graphviz są zainstalowane w niestandardowej lokalizacji, należy spróbować znaleźć program za pomocą polecenia:


{{Code|lang=text|code=
type dot
}}

Może to być coś w rodzaju


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

I dlatego możesz wskazać programowi FreeCAD, aby szukał w tym katalogu.



## Użycie

1.  Wybierz z menu opcję **Przybory → <img src="images/Std_DependencyGraph.svg" width=16px> Graf zależności ...**.
2.  W [Głównym obszarze widoku](Main_view_area/pl.md) otworzy się nowa zakładka zatytułowana **Graf zależności**.
3.  Użyj kółka przewijania myszy, aby przybliżyć lub oddalić widok.
4.  Użyj suwaków na dole i po prawej stronie ekranu, aby przesunąć widok. Alternatywnie ({{Version/pl|0.19}}) przytrzymaj lewy przycisk myszy i poruszaj kursorem.



## Zapis

Możesz zapisać wykres zależności:

1.  Upewnij się, że zakładka Graf zależności jest na pierwszym planie.
2.  Wybierz z menu opcję **Plik → [Zapisz](Std_Save/pl.md)** lub **Plik → [Zapisz jako](Std_SaveAs/pl.md)**.
3.  Wprowadź nazwę pliku i wybierz typ pliku (\*.png, \*.bmp, \*.gif, \*.jpg, \*.svg lub \*.pdf).
4.  Naciśnij przycisk **Zapisz**.



## Zasady ogólne 

-   Wykres przedstawia obiekty w odwrotnej kolejności chronologicznej.
-   Kierunek strzałek pokazujących zależności powinien być zawsze skierowany w dół, od obiektu dziecka do obiektu rodzica. Strzałka skierowana w górę wskazuje na zależność cykliczną, czyli problem, który należy rozwiązać.
-   Szkic zawierający odnośniki do [zewnętrznej geometrii](Sketcher_External/pl.md) będzie miał liczbę z przyrostkiem \"x\" obok strzałki łączącej go z jego rodzicem, pokazującą liczbę zewnętrznych geometrii powiązanych w szkicu.
-   Obiekty mogą mieć zależności z wieloma rodzicami. Na przykład, dla modelu zbudowanego w środowisku [Projekt Części](PartDesign_Workbench/pl.md), kieszeń może być powiązana ze swoim Szkicem i z elementem wyciągnięcia, który był przed nim.



## Ograniczenia

-   Graf zależności nie może pomóc w rozwiązaniu [problemu z nazewnictwem topologicznym](topological_naming_problem/pl.md). Jeśli szkic zmieni ściany elementu po edycji, nadal jest połączony z elementem. Nawet jeśli niektóre funkcje są zepsute, wykres zależności pozostanie niezmieniony.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [3rd Party](Category_3rd Party.md) > Std DependencyGraph/pl
