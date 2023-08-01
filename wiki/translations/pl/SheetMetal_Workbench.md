# SheetMetal Workbench/pl
}

<img alt="Ikonka FreeCAD dla zewnętrznego środowiska pracy Arkusz blachy" src=images/Sheetmetal_workbench_icon.svg  style="width:128px;">






## Wprowadzenie

Środowisko pracy <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:32px;"> [Arkusz blachy](SheetMetal_Workbench/pl.md) jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md) i nie należy do standardowej instalacji programu FreeCAD. Zostało ono opracowane w celu dostarczenia narzędzi do tworzenia i rozwinięć obiektów blaszanych.

Cechami charakterystycznymi przedmiotów wykonanych z blachy są:

-   Mają stałą grubość,
-   Mogą być rozkładane, jeśli są wykonane tylko z płaskich ścian i połączeń cylindrycznych.

Narzędzie do rozkładania w obu wersjach nie jest ograniczone do części wykonanych narzędziami z tego środowiska pracy, ale może obsługiwać również obiekty należące do środowisk pracy [Część](Part_Workbench/pl.md) i [Projekt Części](PartDesign_Workbench/pl.md), o ile spełniają one powyższe wymagania.

<img alt="" src=images/SheetMetal_Example.png  style="width:600px;"> 
*Model z blachy zbudowany za pomocą dodatku '''Arkusz blachy''' ''(z tyłu)'', <br>przed nim rozwinięta bryła, <br>na pierwszym planie rozwinięty szkic z liniami gięcia do eksportu do formatu DXF.*

Jeśli eksport do formatu DXF jest używany do sterowania maszynami *(na przykład cięcie laserowe)*, należy zmodyfikować DXF, aby usunąć linie pokazujące zagięcia, ponieważ linie te mogą być używane przez maszynę do cięcia.



## Instalacja

To środowisko pracy może być zainstalowane z <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md). Aby zainstalować je samodzielnie zobacz stronę [Instalacja zewnętrznych środowisk pracy](Installing_more_workbenches/pl.md).



## Przybory

Szczegółowy opis narzędzi można znaleźć [na blogu autora](http://theseger.com/projects/2015/06/sheet-metal-addon-for-freecad/). Jednak jest on już trochę przestarzały, ponieważ dodano kilka nowych narzędzi.

-   <img alt="" src=images/SheetMetal_AddBase.svg  style="width:32px;"> [Dodaj element bazowy](SheetMetal_AddBase/pl.md): Tworzy obiekt bazowy z blachy na podstawie szkicu, profilu lub płyty.

-   <img alt="" src=images/SheetMetal_AddWall.svg  style="width:32px;"> [Dodaj ścianę](SheetMetal_AddWall/pl.md): Dodaje kołnierz na każdej wybranej krawędzi płyty bazowej *(Kołnierz można przekształcić w obszycie, modyfikując jego kąt)*.

-   <img alt="" src=images/SheetMetal_Extrude.svg  style="width:32px;"> [Wyciągnij](SheetMetal_Extrude/pl.md): Rozciąga blachę na wybranej krawędzi wzdłuż jej wektora normalnego *(Po dodaniu szkicu konturu można go użyć do utworzenia geometrii blokującej)*.

-   <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:32px;"> [Zagnij blachę](SheetMetal_AddFoldWall/pl.md): Składa ścianę na wybranej linii z zadanym promieniem gięcia.

-   <img alt="" src=images/SheetMetal_Unfold.svg  style="width:32px;"> [Rozwiń](SheetMetal_Unfold/pl.md): Prostuje zgięty obiekt blaszany i generuje rozwiniętą bryłę oraz szkic konturowy z liniami gięcia *(udostępnia okno dialogowe do ustawiania parametrów)*.

-   <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:32px;"> [Rozwiń bezobsługowo](SheetMetal_UnattendedUnfold/pl.md): Prostuje zgięty obiekt blaszany i generuje rozwinięcie oraz szkic konturowy z liniami gięcia *(jeżeli parametry zostały już ustawione)*.

-   <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:32px;"> [Dodaj podcięcie w narożniku](SheetMetal_AddCornerRelief/pl.md): Dodaje relief narożny do narożnika.

-   <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:32px;"> [Dodaj podcięcie](SheetMetal_AddRelief/pl.md): Pierwszy krok do przekształcenia obiektu powłoki w rozkładany obiekt z blachy, dodaje zagłębienie *(wycięcie)* do narożnika.

-   <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:32px;"> [Dodaj otwarte połączenie](SheetMetal_AddJunction/pl.md): Drugi krok, aby przekształcić obiekt powłoki w obiekt z rozkładanej blachy, tworzy otwarte połączenie na krawędzi dwóch ścian.

-   <img alt="" src=images/SheetMetal_AddBend.svg  style="width:32px;"> [Dodaj zaokrąglone zgięcie](SheetMetal_AddBend/pl.md): Trzeci krok do przekształcenia obiektu powłoki w obiekt z rozkładanej blachy, zastępuje ostre krawędzie okrągłymi zagięciami.

-   <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:32px;"> [Szkic na arkuszu](SheetMetal_SketchOnSheet/pl.md): Na podstawie szkicu wycina wzór otworów wzdłuż zagiętych ścian obiektu z blachy.

-   <img alt="" src=images/SheetMetal_Forming.svg  style="width:32px;"> [Formowanie blach](SheetMetal_Forming/pl.md): Wytłacza kształty z otworami lub bez otworów w arkuszu blachy.



## Krótki opis 

To środowisko pracy dostarcza narzędzi do dwóch głównych zadań:

-   Tworzenie obiektów blaszanych,
-   Rozkładanie obiektów z blachy.

Ta sekcja ma na celu dać ogólne pojęcie o tym, jak używać dostarczonych narzędzi. Bardziej szczegółowe informacje można znaleźć na stronie każdego narzędzia *(patrz wyżej)* lub w połączonych z nim poradnikach *(patrz niżej)*.



### Utwórz obiekt z blachy 



#### Rozpoczęcie od profilu 

1.  Utwórz otwartą polilinię *(najlepiej za pomocą szkicownika)*,
2.  Użyj polecenia <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Dodaj ścianę bazową](SheetMetal_AddBase/pl.md), aby utworzyć profil arkusza blachy.



#### Rozpoczęcie od pustego 

1.  Utwórz zamkniętą polilinię *(najlepiej za pomocą szkicownika)*,
2.  Użyj polecenia <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Dodaj ścianę bazową](SheetMetal_AddBase/pl.md), aby utworzyć nowy arkusz blachy.



#### Rozpoczęcie od wyciągnięcia w środowisku Projekt Części 

1.  Utwórz zamkniętą polilinię *(najlepiej za pomocą szkicownika)*,
2.  Użyj polecenia <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md) aby stworzyć bryłę prostopadłościanu,
3.  Narzędzie <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [Grubość](PartDesign_Thickness.md) środowiska Projekt Części sprawi, że będzie to obiekt o stałej grubości,
4.  Aby można było go rozłożyć, potrzebne są przerwy lub połączenia między ścianami:
    1.  Za pomocą narzędzia <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:24px;"> [Dodaj podcięcie](SheetMetal_AddRelief/pl.md) zetniemy wybrane narożniki,
    2.  Polecenie <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> [Dodaj otwarte połączenie](SheetMetal_AddJunction/pl.md) utworzy szczeliny między sąsiednimi ścianami, które trzeba rozdzielić,
    3.  Polecenie <img alt="" src=images/SheetMetal_AddBend.svg  style="width:24px;"> [Dodaj zaokrąglone zgięcie](SheetMetal_AddBend/pl.md) utworzy cylindryczne połączenia dla pozostałych ścian, które muszą pozostać połączone.

Niektóre parametry będą dziedziczone z obiektu*(ów)* nadrzędnego, ale lepiej jest sprawdzić odpowiednie parametry na każdym etapie.

Należy teraz sprawdzić, czy powstały obiekt blaszany może zostać rozłożony *(zobacz rozdział [Rozłóż blaszany element](#Roz.C5.82.C3.B3.C5.BC_blaszany_element.md) poniżej)*.



#### Dodawanie kolejnych cech 

Standardowe rozkładane blaszane elementy mogą być rozbudowywane:

1.  Użyj polecenia <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> [Wyciągnij](SheetMetal_Extrude/pl.md), aby powiększyć ściany.
2.  Polecenie <img alt="" src=images/SheetMetal_AddWall.svg  style="width:16px;"> [Dodaj ścianę](SheetMetal_AddWall/pl.md) doda nowe kołnierze lub obszycia w istniejącym obiekcie.
3.  Użyj polecenia <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:24px;"> [Dodaj podcięcie w narożniku](SheetMetal_AddCornerRelief/pl.md), aby dodać lub zmienić kształt podcięć narożnych.
4.  Polecenie <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> [Zagnij blachę](SheetMetal_AddFoldWall/pl.md) złoży ścianę na wybranej linii, tzn. przytnie ścianę na tej linii, przeniesie odciętą stronę i połączy je cylindrycznym połączeniem.
5.  Użyj narzędzia <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:24px;"> [Szkic na arkuszu](SheetMetal_SketchOnSheet/pl.md) wytnij otwory w obiekcie zaczynając od wybranej ściany, a następnie podążając za sąsiednimi ścianami i połączeniami.
6.  Polecenie <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;"> [Formowanie blach](SheetMetal_Forming/pl.md) wytłoczy w płycie *(ścianie)* kształt.

:   

    :   Po utworzeniu cechy *Formowanie blach* obiekt *Arkusz blachy* **już nie da się rozłożyć**!

Kilka narzędzi z innych środowisk pracy może być używanych do dodawania otworów lub zmiany kształtu krawędzi.



### Rozłóż blaszany element 

Aby rozłożyć obiekt z blachy aktywuj narzędzie <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> [Rozłóż](SheetMetal_Unfold/pl.md) lub <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;">[Rozłóż bezobsługowo](SheetMetal_UnattendedUnfold/pl.md).

Wynikiem będzie obiekt 3D z opcjonalnym szkicem konturowym zawierającym linie zgięcia.



### Przykłady

Dopóki strony poradników nie są dostępne na tej wiki, istnieje strona z [przykładami](SheetMetal_Examples/pl.md).

<img alt="" src=images/SheetMetal_Example-01.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-02.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:100px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:100px;">

Zawiera również kilka wskazówek dotyczących [własności](SheetMetal_Examples/pl#W.C5.82a.C5.9Bciwo.C5.9Bci_.C5.9Brodowiska_pracy_Arkusz_Blachy.md).



## Ograniczenia

-   Na środowisko robocze ma wpływ [problem nazewnictwa topologicznego](Topological_naming_problem/pl.md), który jest nieodłączny dla FreeCAD. Jeśli edycja zagięcia wcześniej w historii części zmieni numerację powierzchni, wówczas kolejne zagięcia mogą zostać naruszone i zmienić powierzchnię. Jeżeli właściwości gięcia nie zostaną uszkodzone, możesz kliknąć na nim dwukrotnie, aby uzyskać okno dialogowe, w którym możesz wybrać odpowiednią powierzchnię w oknie [widoku 3D](3D_view/pl.md) i zaktualizować gięcie.
-   Narzędzie Rozwiń ma pewne ograniczenia i może zawieść w pewnych skomplikowanych sytuacjach. Jeśli zawiedzie, spróbuj wybrać inną ścianę.
-   Częsty przypadek awarii: należy podjąć wszelkie środki ostrożności, aby nie ciąć w zawiasach *(zagięciach)* ani wzdłuż powierzchni ścian, ani w kątach, ani nie robić otworów lub nacięć w kątach.



## Poradniki


<div class="mw-collapsible mw-collapsed toccolours" style="width:800px">

### Arkusz blachy poradnik według meme2704 

Poniższy poradnik został zaczerpnięty z poradnika PDF wspomnianego w sekcji [Odnośniki internetowe](#Odno.C5.9Bniki_internetowe.md).


<div class="mw-collapsible-content">



#### Prezentacja środowiska pracy 

Po pobraniu i zainstalowaniu rozszerzenia, uruchom je. ![](images/sm1.png ) 

#### Operacja pierwsza 

-   Wykonaj element początkowy: użyj środowisk pracy Część lub Rysunek Roboczy, wykonaj pierwszy szkic, który będzie zawierał wszystkie otwory i cięcia, następnie wytłocz ten element do grubości arkusza.
-   Pamiętaj, że krawędzie będą zawsze w dodatku, tak samo jak promienie składania.

![](images/sm2.png ) 

#### Operacja druga 

-   Otwórz środowisko pracy Arkusz blachy.
-   Wybierz 1 grubość krawędzi *(brzegu)* płyty bazowej i kliknij na narzędzie \"Dodaj zaokrąglone gięcie\" 90° domyślny kąt gięcia może być zmieniany w zakresie od {{Value|0}} do {{Value|90}}°.
-   Wysokość krawędzi wynosi domyślnie 10mm, można ją edytować w zakresie od {{Value|0.1}} do {{Value|xxx}} mm.
-   Promień gięcia jest domyślnie równy grubości, można go edytować w zakresie od {{Value|0.1}} do {{Value|xx}} mm *(nigdy nie należy wstawiać wartości 0)*.
-   Odstęp1, odstęp2 to odległość zagiętej krawędzi od rogu podstawy *(0 akceptwalne)*.
-   Invert domyślnie: przyjmuje wartość {{false/pl}} składa się do Z +, {{true/pl}} do ZReliefd przecina róg między fałdą a podstawą *(nieaktywne, jeśli szczelina ma wartość = 0)*.
-   Reliefw dodaje 1 szczelina między zagięciem a krawędzią *(nieaktywne, jeśli reliefd ma wartość = 0)*.

![](images/sm3.png ) Powtórz tyle razy, ile jest boków do zgięcia.
Składanie 1 powrót z wykorzystaniem wyciągnięcia.
![](images/sm4a.png ) Aby dodać 1 powrót powtórz tę samą operację wybierając grubość danej krawędzi.
Aby zmniejszyć odstęp między 2 krawędziami użyj funkcji wyciągnięcia.
Wybierz grubość i określ długość do dodania.
Zwróć uwagę, że jeśli wyciągnięcie pierwszej krawędzi zostanie wykonane przed powrotem zagięcia, nie będzie brane pod uwagę, jeśli 1 identyczne zagięcie zostanie dodane do wyciągnięcia, będzie wyglądało poprawnie, ale rozkładanie nie zostanie wykonane.
Złożenie pierwsze drugiej krawędzi:
Teraz musimy rozdzielić te 2 krawędzie, w przeciwnym razie połączą się i rozkładanie nie będzie możliwe.
\* Metoda pierwsza: zrobić 1 wycofanie 1 krawędzi.

-   -   Podaj 1 wartość nieco większa niż szczelina1 *(lub szczelina2)*, przy zerze jest jeszcze połączenie.

-   Metoda druga: zrobić 1 cięcie pod kątem 45 ° patrz dalej, użyj tego narzędzia.

![](images/sm5a.png ) 

#### Rozkładanie

Wybierz jedną ścianę odniesienia *(tutaj pomarańczowa)* i kliknij przycisk na pasku narzędzi.
Otrzymujemy niebieską część, której wystarczy zmodyfikować wartości X, Y lub Z, aby zobaczyć ją w całości.
![](images/sm6.png ) 

#### Przycięcie brzegów pod kątem 45° 

Po złożeniu brzegów bez wycofania powstaje kształt. ![](images/sm7a.png ) Aby to zrobić należy dokonać podziału pod kątem 45° *(lub po dwusiecznej boki są nierównej szerokości)*.
\* Utwórz jeden nowy skit związany z częściami wspólnymi dwóch brzegów.

-   Utwórz jeden powiązany ogranicznik, wybierając zewnętrzną krawędź \"zawiasu\".
-   Narysuj jeden trójkąt, którego wierzchołek jest związany na końcu, zorientowany na jeden bok pod kątem 45°, nadaj małemu bokowi minimalną szerokość *(wystarczy 0,1 mm)* i wykonaj kieszeń.

Be careful not to scratch the \"hinge\" where the nakedness of bound the tip of the triangle at the edge of the fold line. ![](images/sm8a.png ) Rozkładanie ![](images/sm9.png ) 

#### Przebijanie krawędzi i brzegów 

Wykonaj odpowiednie otwory i nacięcia po zakończeniu etapu gięcia, a przed rozłożeniem.
Zawsze uważaj, aby nie \"zarysować\" linii zagięcia.
![](images/sm10.png ) 

#### Wykonanie brzegów załamanych 

Wykonaj jedno zagięcie na krawędzi strony, pod kątem 

#### Szczególny przypadek tej samej krawędzi z przebiciami 

W tym konkretnym przypadku, rozwijanie działa tylko poprzez wybranie żółtej ściany jako odniesienia.
![](images/sm12.png ) 

#### Szczególny przypadek otworu położonego w poprzek zagięcia 

Wcześniej kilkakrotnie stwierdzono, że nie jest konieczne cięcie linii składania.
Jak to zrobić?
![](images/sm13.png )

-   Wykonaj podstawę z półokrągłym otworem i wykonaj dwie połówki boków i dwie połówki zagięcia oddzielnie.
-   Następnie wykonaj przedłużenie na jednym z boków o szerokości otworu minus {{Value|0,1}}mm, w ten sposób dwie krawędzie pozostaną rozdzielone.
-   Następnie na tym przedłużeniu *(w kolorze zielonym)* narysuj kontur cięcia i wykonaj kieszeń.
-   W rezultacie otrzymujemy czerwony element powyżej, a rozkładanie działa, pozostaje linia, która wcześniej oddzielała dwie krawędzie.

![](images/sm14.png )


</div>


</div>



## Filmy

-   [Eleganckie środowisko pracy obróbki blachy](https://www.youtube.com/watch?v=xidvQYkC4so) autorstwa Joko Engineering



## Odnośniki internetowe 

-   [Rozwinięcie blachy](Macro_Sheet_Metal_Unfolder/pl.md), oryginalna makrodefinicja, na której bazuje narzędzie Rozkładanie.
-   [Angielski i francuski poradnik w formacie PDF](https://forum.freecadweb.org/viewtopic.php?f=3&t=25002) na forum FreeCAD.
-   Zgłaszanie błędów/żądanie funkcji: <https://github.com/shaise/FreeCAD_SheetMetal/issues>.



## Bibliografia

-   Autor:
    -   Narzędzia do składania: Copyright 2015-2018 by Shai Seger
    -   Narzędzie do rozkładania: Copyright 2014 by Ulrich Brammer
-   Licencja: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
-   Kod źródłowy na githubie: <https://github.com/shaise/FreeCAD_SheetMetal>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Workbench/pl
