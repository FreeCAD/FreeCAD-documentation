# Manual:A gentle introduction/pl
{{Manual:TOC}}

[Python](https://pl.wikipedia.org/wiki/Python) to powszechnie używany, otwartoźródłowy język programowania, ceniony za swoją prostotę, wszechstronność i czytelność. Jest często osadzany w aplikacjach jako język skryptowy, a FreeCAD nie jest wyjątkiem. Ta integracja pozwala użytkownikom automatyzować zadania, dostosowywać przepływ pracy i rozszerzać funkcjonalność oprogramowania daleko poza jego interfejs graficzny.

Python oferuje kilka zalet, które sprawiają, że jest szczególnie odpowiedni dla użytkowników programu FreeCAD. Jest przyjazny dla początkujących, z klarowną i intuicyjną składnią, co ułatwia naukę, nawet dla osób bez wcześniejszego doświadczenia w programowaniu. Ta dostępność jest szczególnie cenna w społeczności programu FreeCAD, gdzie wielu użytkowników pochodzi z różnych dziedzin, takich jak inżynieria, architektura czy projektowanie, bez rozległej wiedzy z zakresu kodowania.

Dodatkowo, powszechne zastosowanie Pythona w innych aplikacjach, takich jak [Blender](https://www.blender.org) do modelowania 3D, [Inkscape](https://www.inkscape.org) do grafiki wektorowej i [GRASS GIS](https://grass.osgeo.org) do analizy geoprzestrzennej, czyni go niezbędną umiejętnością dla każdego, kto chce poszerzyć swoje możliwości skryptowe. Opanowanie Pythona w FreeCAD nie tylko zwiększa zdolność tworzenia niestandardowych narzędzi i makr, ale także zapewnia umiejętności, które można zastosować w różnych platformach programowych.

Tworzenie skryptów Pythona we FreeCAD umożliwia Ci:

-   Automatyzację powtarzalnych zadań, aby zaoszczędzić czas i zredukować błędy.
-   Tworzenie niestandardowych obiektów parametrycznych, które dynamicznie dostosowują się do zmian.
-   Rozwój spersonalizowanych makr i narzędzi dostosowanych do konkretnych przepływów pracy.
-   Interakcję z Interfejsem Programowania Aplikacji (API) FreeCAD, aby programowo uzyskać dostęp do geometrii, scen i elementów interfejsu użytkownika.

Dzięki wykorzystaniu Pythona, użytkownicy FreeCAD mogą odblokować pełny potencjał oprogramowania, przekształcając je w potężne i elastyczne narzędzie dostosowane do ich unikalnych potrzeb.

FreeCAD zawiera zaawansowaną konsolę Pythona, dostępną przez **Widok → Panele → Konsola Pythona**. To narzędzie pozwala użytkownikom na wykonywanie operacji wykraczających poza interfejs graficzny, takich jak dostęp do zaawansowanych funkcji, rozwiązywanie problemów z geometrią i automatyzowanie zadań. Zapisuje również polecenia Pythona dla działań w GUI, jeśli opcja *Pokaż polecenia skryptu w konsoli Pythona* jest włączona w **Edycja → Preferencje → Python → Makrodefinicje**). Trzymanie konsoli otwartej umożliwia obserwowanie kodu Pythona podczas pracy, oferując intuicyjny sposób nauki języka przy jednoczesnym eksplorowaniu możliwości FreeCAD. Na koniec, FreeCAD posiada także system [makr](Macros/pl.md), który pozwala na rejestrowanie działań do późniejszego odtworzenia. System ten także korzysta z konsoli Pythona, rejestrując wszystko, co jest w niej robione.

![](images/FreeCAD_Python_Console.png )

W tym rozdziale poznamy bardzo ogólnie język Python. Jeśli chcesz dowiedzieć się więcej, wiki dokumentacji FreeCAD zawiera obszerną sekcję związaną z [Programowaniem w języku Python](Power_users_hub/pl.md).



### Pisanie kodu Python 

We FreeCAD możesz pisać kod Pythona na dwa główne sposoby: przez konsolę Pythona (**Widok → Panele → Konsola Pythona**) lub za pomocą edytora makr (**Makrodefinicje → Makrodefinicje → Utwórz**). Konsola Pythona pozwala na wprowadzanie poleceń pojedynczo, które są natychmiastowo wykonywane po naciśnięciu klawisza Enter, co sprawia, że jest idealna do szybkiego testowania lub interaktywnego eksplorowania. Edytor Makr natomiast jest używany do pisania i zapisywania bardziej złożonych skryptów składających się z wielu linii kodu. Te makra można później wykonać jako całość z okna Makrodefinicji, co stanowi potężny sposób automatyzowania powtarzalnych zadań i rozszerzania funkcjonalności FreeCAD. W tym rozdziale będziesz używać obu metod, ale zaleca się korzystanie z Konsoli Pythona, ponieważ natychmiast informuje o wszelkich błędach popełnionych podczas pisania.

Jeśli używasz Python po raz pierwszy, rozważ przeczytanie tego krótkiego [Wprowadzenie do programowania w Pythonie](Introduction_to_Python/pl.md) przed przejściem dalej, dzięki czemu podstawowe pojęcia środowiska Python staną się bardziej zrozumiałe.



### Manipulowanie obiektami FreeCAD 

Zacznijmy od utworzenia nowego pustego dokumentu:


```python
doc = FreeCAD.newDocument()
```

W konsoli Pythona w FreeCAD, gdy tylko wpiszesz \"FreeCAD.\" (słowo \"FreeCAD\" po którym następuje kropka), pojawi się okno autouzupełniania. Ta funkcja nie tylko przyspiesza pracę, sugerując dostępne polecenia, ale także pomaga odkrywać nowe funkcje i możliwości w FreeCAD. Każdy wpis na liście zawiera podpowiedź wyjaśniającą jego przeznaczenie, co ułatwia zrozumienie i eksplorację dostępnych funkcji. Funkcja autouzupełniania jest szczególnie pomocna dla początkujących, którzy uczą się skryptowania w Pythonie, oraz dla zaawansowanych użytkowników poruszających się po rozległym API FreeCAD. Poświęć chwilę, aby zbadać opcje w oknie autouzupełniania - możesz odkryć polecenia, które uproszczą Twój sposób pracy lub otworzą nowe możliwości.

![](images/FreeCAD_python_newDocument.png )

Wpisanie **FreeCAD.newDocument()** tworzy nowy, pusty dokument w FreeCAD, tak jak kliknięcie przycisku **Nowy dokument** na pasku narzędzi. Gdy wykonasz **doc = FreeCAD.newDocument()**, nowy obiekt dokumentu zostaje przypisany do zmiennej **doc**, co umożliwia jego manipulację programistycznie. Korzystając z **doc**, możesz dodawać obiekty, zmieniać właściwości lub zapisywać dokument.

W Pythonie kropka (.) jest używana do wskazania, że jeden element jest zawarty w innym. Na przykład **newDocument** jest funkcją w ramach **modułu FreeCAD**, dlatego piszemy FreeCAD.newDocument. Okno autouzupełniania, które się pojawia, pokazuje wszystko, co jest dostępne w module FreeCAD. Jeśli wpiszesz kropkę po newDocument (nie dodając nawiasów), wyświetli się wszystko, co należy do funkcji newDocument. To pokazuje, jak Python organizuje i uzyskuje dostęp do obiektów i ich komponentów. Ważne jest, aby pamiętać, że nawiasy są obowiązkowe przy wywoływaniu funkcji Pythona, ponieważ sygnalizują wykonanie funkcji.

Wróćmy teraz do naszego dokumentu. Zobaczmy, co możemy z nim zrobić. Wpisz poniższe polecenie i sprawdź dostępne opcje:


```python
doc.
```

Konwencje nazewnictwa poleceń Pythona we FreeCAD mogą pomóc zrozumieć ich cel:

-   Nazwy zaczynające się od wielkiej litery to zazwyczaj atrybuty, które przechowują wartości lub dane, takie jak właściwości obiektu.
-   Nazwy zaczynające się od małej litery to zazwyczaj funkcje (zwane również metodami), które wykonują akcje lub operacje, takie jak tworzenie lub modyfikowanie obiektów.
-   Nazwy zaczynające się od podkreślenia (\_) są zazwyczaj przeznaczone do użytku wewnętrznego w module i zwykle można je zignorować.

Ta rozróżnienie pomaga w nawigacji po API programu FreeCAD i wyborze odpowiedniego polecenia do swoich potrzeb. Na przykład, możesz użyć metody, aby dodać nowy obiekt do dokumentu. Metoda wykonuje akcję tworzenia i dodawania obiektu, podczas gdy atrybuty przechowują właściwości obiektu. Zrozumienie tej struktury ułatwia odkrywanie dostępnej funkcjonalności, zwłaszcza gdy korzystasz z funkcji autouzupełniania lub czytasz podpowiedzi. Dodajmy teraz pudełko.


```python
box = doc.addObject("Part::Box", "myBox")
```

Polecenie **box = doc.addObject(\"Part::Box\", \"myBox\")** dodaje nowy obiekt 3D w kształcie prostopadłościanu do dokumentu. Oto proste wyjaśnienie:

-   **doc.addObject**: Informuje FreeCAD, aby dodał nowy obiekt do dokumentu.
-   **Part::Box**: Określa typ obiektu do utworzenia, w tym przypadku prostopadłościan.
-   **myBox**: Przypisuje nazwę nowemu obiektowi, co ułatwia jego identyfikację i późniejsze odwoływanie się do niego.

Wynikiem wykonania tego polecenia jest pojawienie się pudełka w aktywnym dokumencie, a zmienna box przechowuje odwołanie do niego, dzięki czemu można go modyfikować lub wchodzić z nim w interakcję później. Nasze pudełko zostało dodane do widoku drzewa, ale nic się nie dzieje w widoku 3D, ponieważ przy pracy z poziomu Pythona dokument nie jest automatycznie przeliczany. Musimy to zrobić ręcznie, kiedy zajdzie taka potrzeba:


```python
doc.recompute()
```

Teraz nasz prostopadłościan pojawił się w oknie widoku 3D. Wiele przycisków paska narzędzi, które dodają obiekty w FreeCAD, wykonuje w rzeczywistości dwie czynności: dodanie obiektu i ponowne obliczenie. Spróbuj teraz dodać kulę za pomocą odpowiedniego przycisku w środowisku pracy Część, a zobaczysz, że dwie linie kodu Python są wykonywane jedna po drugiej.

![](images/FreeCAD_python_Sphere.png )

Możesz uzyskać listę wszystkich możliwych typów obiektów, takich jak Part::Box:


```python
doc.supportedTypes()
```

Teraz przyjrzyjmy się zawartości naszego prostopadłościanu:


```python
box.
```

Od razu zobaczysz kilka bardzo interesujących rzeczy, takich jak:


```python
box.Height
```

Spowoduje to wyświetlenie bieżącej wysokości naszego prostopadłościanu. Teraz spróbujmy to zmienić:


```python
box.Height = 5
```

Jeśli wybierzesz swoje pudełko za pomocą myszy, zobaczysz, że w panelu właściwości, w zakładce **Dane**, nasza właściwość **Wysokość** pojawi się z nową wartością. Wszystkie właściwości obiektu FreeCAD, które pojawiają się w zakładkach **Dane** i **Widok**, są również bezpośrednio dostępne z poziomu Pythona, po ich nazwach, tak jak to zrobiliśmy z właściwością Wysokość. Właściwości danych są dostępne bezpośrednio z obiektu, na przykład:


```python
box.Length
```

Właściwości wizualne we FreeCAD są zarządzane przez **ViewObject**. Każdy obiekt FreeCAD ma przypisany ViewObject, który przechowuje informacje o tym, jak obiekt jest wyświetlany w interfejsie graficznym, takie jak kolor, przezroczystość czy widoczność. Jednakże, ViewObject jest dostępny tylko wtedy, gdy FreeCAD działa w trybie graficznym. Jeśli FreeCAD zostanie uruchomiony w trybie bez graficznego interfejsu --- na przykład z terminala z opcją wiersza poleceń -c lub używany jako biblioteka Pythona w zewnętrznym skrypcie --- ViewObject nie jest dostępny. Wynika to z faktu, że w tych trybach nie ma wizualnej reprezentacji obiektu, ponieważ interfejs graficzny nie jest załadowany.

Wypróbuj poniższy przykład, aby uzyskać dostęp do koloru linii naszego prostopadłościanu:


```python
box.ViewObject.LineColor
```



### Wektory i umiejscowienia 

Wektory są podstawowym pojęciem w każdej aplikacji 3D. Wektor to w zasadzie lista trzech liczb (x, y i z), które opisują punkt, pozycję lub kierunek w przestrzeni 3D. Wektory są kluczowe do definiowania geometrii, transformacji i interakcji w środowisku 3D. Stanowią one fundament dla operacji takich jak przesunięcia, obroty i skalowanie.

We FreeCAD wektory są szeroko wykorzystywane do tworzenia i manipulowania obiektami. Umożliwiają one szereg operacji matematycznych, takich jak dodawanie, odejmowanie, iloczyn wektorowy, iloczyn skalarny i projekcje. Operacje te pozwalają na obliczanie odległości, kątów i kierunków lub definiowanie relacji między obiektami w przestrzeni.

Zrozumienie wektorów i ich działania jest kluczowe dla efektywnego tworzenia skryptów i dostosowywania FreeCAD. Na przykład wektory są używane do ustawiania pozycji obiektów, definiowania ich orientacji, a nawet obliczania trajektorii dla bardziej złożonych operacji, takich jak przesunięcia czy formowanie.

We FreeCAD wektory są reprezentowane za pomocą klasy **Vector**, która oferuje różne metody i właściwości do wykonywania operacji oraz dostępu do ich składowych. Opanowanie tych możliwości znacząco zwiększy twoje zdolności do interakcji ze środowiskiem 3D programu FreeCAD za pomocą skryptów. We FreeCAD wektory działają w ten sposób:


```python
myvec = FreeCAD.Vector(2, 0, 0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Oto krótkie wyjaśnienie powyższych poleceń:

-   **myvec = FreeCAD.Vector(2,0,0)**: Tworzy wektor myvec z wartościami X = 2, Y = 0, Z = 0.
-   **print(myvec)**: Wypisuje wektor myvec z jego składowymi (X, Y, Z).
-   **print(myvec.x)**: Wypisuje składową X wektora myvec.
-   **print(myvec.y)**: Wypisuje składową Y wektora myvec.
-   **othervec = FreeCAD.Vector(0,3,0)**: Tworzy drugi wektor othervec z wartościami X = 0, Y = 3, Z = 0.
-   **sumvec = myvec.add(othervec)**: Dodaje wektory myvec i othervec, tworząc nowy wektor sumvec zawierający sumę ich składowych.

Inną powszechną cechą obiektów FreeCAD jest ich **Umiejscowienie**. Jak widzieliśmy w poprzednich rozdziałach, każdy obiekt ma właściwość Umiejscowienie, która zawiera pozycję (Baza) i orientację (Obrót) obiektu. Te właściwości są łatwe do manipulowania z poziomu Pythona, na przykład aby przesunąć nasz obiekt:


```python
print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5, 5, 0)
box.Placement = otherpla
```

Oto krótkie wyjaśnienie powyższych poleceń:

-   **print(box.Placement)**: Wypisuje położenie prostopadłościanu, które zawiera jego pozycję, rotację i orientację w przestrzeni 3D.
-   **print(box.Placement.Base)**: Wypisuje pozycję (Bazę) pudełka, która jest wektorem reprezentującym jego lokalizację w przestrzeni 3D.
-   **box.Placement.Base = sumvec**: Ustawia pozycję bazową (lokalizację) pudełka na wektor sumvec, co skutkuje przesunięciem pudełka na tę nową pozycję.
-   **otherpla = FreeCAD.Placement()**: Tworzy nowy obiekt umiejscowienia o nazwie otherpla.
-   **otherpla.Base = FreeCAD.Vector(5,5,0)**: Ustawia pozycję bazową obiektu otherpla na wektor o współrzędnych (5, 5, 0).
-   **box.Placement = otherpla**: Zastosowuje otherpla do pudełka, aktualizując jego umiejscowienie na nową pozycję i orientację zdefiniowaną przez otherpla.

**Więcej informacji:**

-   [Python](https://www.python.org)
-   [Makrodefinicje](Macros/pl.md)
-   [Wprowadzenie do środowiska Python](Introduction_to_Python/pl.md)
-   [Poradnik: Tworzenie skryptów Python](Python_scripting_tutorial/pl.md)
-   [Centrum Power użytkowników](Power_users_hub/pl.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:A gentle introduction/pl
