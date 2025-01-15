# The FreeCAD source code/pl
Kod źródłowy [FreeCAD](https://github.com/FreeCAD/FreeCAD) jest zarządzany za pomocą git i jest publiczny, otwarty i dostępny na licencji [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License). Może być kopiowany, pobierany, czytany, analizowany, redystrybuowany i modyfikowany przez każdego. Jeśli planujesz wprowadzić modyfikacje, które chcesz zobaczyć w oficjalnym kodzie, pamiętaj, że Twoje zmiany będą musiały zostać zatwierdzone przez programistów FreeCAD, więc dobrze jest najpierw omówić swoje zamiary i pomysły na [forum](http://forum.freecadweb.org), aby uniknąć ryzyka odrzucenia zmian z jakiegoś powodu, którego nie przewidziałeś.

Poniżej znajduje się kilka wskazówek i przydatnych informacji, które naprowadzą Cię na właściwe tory, jeśli jesteś zainteresowany eksploracją kodu FreeCAD.

-   Kod FreeCAD jest zaprogramowany głównie w **C++**, ale w dużej mierze opiera się na **Pythonie**. Bardzo duża część jego funkcjonalności zapewnia powiązane wiązania Pythona, a częścią podstawowej filozofii rozwoju FreeCAD jest zawsze oferowanie dostępu Pythona do każdej nowej funkcji zaimplementowanej w C++. Aby to osiągnąć, CPython (narzędzia interfejsu C dostarczane przez samego Pythona) i specjalnie [PyCXX](http://cxx.sourceforge.net/) są intensywnie wykorzystywane w całym FreeCAD. Wiele szablonów i niestandardowych narzędzi jest również dostarczanych w samym kodzie FreeCAD, aby bardzo ułatwić tworzenie powiązanych wiązań Pythona. Niektóre bardziej wysokopoziomowe części kodu FreeCAD są w pełni zakodowane w Pythonie.

-   Kod źródłowy FreeCAD jest w pełni *wieloplatformowy* i dołożono wszelkich starań, aby umożliwić korzystanie z aplikacji na jak największej liczbie platform i konfiguracji oraz nie stawiać obecnych użytkowników w trudnych sytuacjach. Dlatego, o ile to możliwe, unika się nowych wersji potrzebnych komponentów, które nie są powszechnie i łatwo dostępne na wszystkich platformach, a kompatybilność wsteczna *(możliwość otwarcia pliku wyprodukowanego w starej wersji FreeCAD na nowszej wersji)* jest ważnym priorytetem.

-   Prawie cała funkcjonalność FreeCAD jest podzielona na dwie różne części, nazwane **APP** i **GUI**. Ta separacja jest odzwierciedlona wszędzie w strukturze plików kodu źródłowego. Aplikacja zawiera wszystkie funkcje, które muszą działać w trybie czysto konsolowym (bez GUI). Ponieważ FreeCAD może być kompilowany i uruchamiany bez graficznego interfejsu użytkownika, kod w aplikacji jest niezależny od jakiejkolwiek biblioteki związanej z GUI. GUI zawiera cały kod potrzebny do działania w trybie GUI i jest zbudowany wokół funkcjonalności aplikacji.

-   Większość funkcjonalności FreeCAD jest zaimplementowana w *modułach*. FreeCAD bez modułu jest prostym oknem kontenera, które może po prostu otworzyć i zapisać plik. Wszystkie narzędzia geometrii i środowiska pracy są zaimplementowane w modułach. Moduły mogą być napisane w C++, Pythonie lub łącząc to, co najlepsze z tych dwóch światów. Mogą to być moduły hybrydowe C++/Python, w których solidna podstawowa funkcjonalność jest zaprogramowana w C++, a narzędzia użytkownika końcowego są napisane w Pythonie, co ułatwia ich rozszerzanie i dostosowywanie przez użytkowników FreeCAD. Każdy moduł zazwyczaj definiuje i tworzy **środowisko pracy** w interfejsie FreeCAD, gdy jest używany w trybie GUI, zwykle o tej samej nazwie, ale nie jest obowiązkowe, aby moduły zawierały środowisko pracy.

-   Moduły FreeCAD często **zależą od innych modułów**. Większość modułów wykorzystujących geometrię bryłową zależy od modułu **Część**, który jest najbardziej podstawowym modułem FreeCAD i implementuje większość interfejsów z OpenCascade. Chociaż inne moduły mogą bezpośrednio korzystać z funkcjonalności OpenCascade, często polegają na funkcjach wyższego poziomu dostarczanych przez Część.

-   Moduły są zawsze **inicjowane** z Pythona. Nawet jeśli są napisane w całości w C++, zawsze zawierają minimalną strukturę Pythona/CPythona.

-   FreeCAD jest gorliwym zwolennikiem **innych bibliotek open-source**. Oprócz Pythona i Qt, używanych przez rdzeń i prawie wszystkie moduły, dwie ciężkie biblioteki używane w większości modułów to [OpenCascade Technology](https://en.wikipedia.org/wiki/Open_Cascade_Technology) *(OCCT)* i [Coin3D](http://www.coin3d.org/). OpenCascade służy do tworzenia i zarządzania całą geometrią bryłową FreeCAD, podczas gdy coin3D służy do zarządzania widokiem 3D. OpenCascade jest używany głównie w świecie aplikacji, a coin3D wyłącznie w świecie GUI. Podstawowe zrozumienie OpenCascade jest niezbędne do wykonywania wszelkich prac związanych z geometrią za pomocą FreeCAD. Bardziej specyficzne moduły wykorzystują bardziej specyficzne biblioteki, a ponieważ zwykle nie ma żadnych ograniczeń w tym zakresie, poza tym, że biblioteki te muszą być łatwo dostępne na wszystkich platformach, lista zależności pełnej instalacji FreeCAD ze wszystkimi jego modułami może być dość duża.

-   Obiekty dokumentu FreeCAD, które są wszystkimi obiektami zawartymi w dokumencie FreeCAD, są tym, co pojawia się w widoku drzewa w GUI i w FreeCAD.ActiveDocument.Objects() w Pythonie. Mogą one mieć lub nie mieć żadnych danych geometrycznych i mogą lub nie mogą pokazywać niczego w widoku 3D. Są one zawsze podzielone na części APP i GUI. Część Gui nie jest ładowana podczas działania w trybie konsoli. Standardowe obiekty geometryczne, takie jak te znajdujące się w Part lub PartDesign, mają swoją geometrię opartą na OpenCascade zdefiniowaną w ich odpowiedniku App, podczas gdy odpowiednik GUI *(zwykle nazywany również \"Dostawcą widoku\")* jest odpowiedzialny za tworzenie reprezentacji coin3D tej geometrii, która zostanie wstawiona do głównego wykresu sceny coin3D widoku 3D.

-   Podstawowa struktura katalogów kodu źródłowego jest zorganizowana w następujący sposób:
    -   **App**: zawiera aplikację trybu konsoli FreeCAD, definiuje podstawowe struktury i klasy bazowe dla obiektów dokumentów, które są używane przez moduły do budowania własnych.
    -   **Base**: zawiera podstawową funkcjonalność powszechnie używaną w FreeCAD: wektory 3D, jednostki, macierze, rozmieszczenia itp.
    -   **Gui**: zawiera aplikację FreeCAD w trybie GUI, definiuje widok 3D, zawiera wiele narzędzi i funkcji do wykorzystania przez środowiska robocze do interakcji z interfejsem i widokiem 3D, definiuje klasy bazowe dla dostawców widoków.
    -   **Doc**: zawiera głównie uniwersalny plik pomocy Qt wygenerowany z tej wiki.
    -   **Mod**: zawiera wszystkie moduły, podzielone na App i Gui *(z wyjątkiem modułów Pythona, które nie zawsze przestrzegają tej zasady)*.

## Powiązane

-   [Zarządzanie kodem źródłowym](Source_code_management/pl.md)
-   [Centrum Power użytkowników](Power_users_hub/pl.md) zawiera wiele dokumentacji na temat modułów, OpenCascade i Coin3D, głównie dla programistów Pythona. Jednakże, ponieważ funkcjonalność jest podobna, strony te będą również interesujące dla programistów C++.
-   [FCStd](File_Format_FCStd/pl.md) - format pliku FreeCAD.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > The FreeCAD source code/pl
