# Python scripting tutorial/pl
## Wprowadzenie

[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) to język programowania, który jest stosunkowo łatwy do nauczenia i zrozumienia. Jest open-source i wieloplatformowy i może być używany do wielu celów: od prostych skryptów powłoki do bardzo złożonych programów. Ale jego najbardziej rozpowszechnionym zastosowaniem jest język skryptowy osadzony w innych aplikacjach. W ten sposób jest on używany wewnątrz FreeCAD. Z poziomu [konsoli Python](Python_console/pl.md) lub niestandardowych skryptów można kontrolować FreeCAD i wykonywać bardzo złożone operacje.

Na przykład, ze skryptu Python można:

-   Tworzyć nowe obiekty.
-   Modyfikować istniejące obiekty.
-   Modyfikować reprezentację 3D tych obiektów.
-   Modyfikować interfejs FreeCAD.

Istnieje kilka sposobów korzystania ze środowiska Python w FreeCAD:

-   Z [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), gdzie można wydawać polecenia w interfejsie w stylu \"wiersza poleceń\".
-   Z [makrodefinicji](Macros/pl.md), które są wygodnym sposobem na szybkie dodanie brakującego narzędzia do interfejsu FreeCAD.
-   Z zewnętrznych skryptów, które mogą być używane do tworzenia dość złożonych rozwiązań, nawet całych [środowisk pracy](Workbenches/pl.md).

W tym samouczku będziemy pracować nad kilkoma podstawowymi przykładami, aby zacząć, ale jest o wiele więcej [dokumentacji na temat skryptów](Power_users_hub/pl.md) dostępnych na tej Wiki. Jeśli jesteś zupełnie nowy w środowisku Python i chcesz zrozumieć, jak ono działa, mamy również podstawowe [wprowadzenie do środowiska Python](Introduction_to_Python/pl.md).

Przed przystąpieniem do tworzenia skryptów w Pythonie, przejdź do **Edycja → Preferencje ... → Ogólne → Widok raportu** i zaznacz dwa pola:

-    **Przekieruj wiadomości wewnętrzne środowiska Python do Widoku raportu**.

-    **Przekieruj błędy wewnętrzne środowiska Python do Widoku raportu**.

Następnie przejdź do **Widok → Panele** i zaznacz:

-    **Widoku raportu**.



## Pisanie kodu Python 

Istnieją dwa sposoby pisania kodu Python w FreeCAD. W [konsoli Python](Python_console/pl.md) *(wybierz z menu **Widok → Panele → Konsola Python**)* lub w [Edytorze makrodefinicji](Std_DlgMacroExecute/pl.md) *(wybierz z menu **Makrodefinicje → Makrodefinicje ...**)*. W konsoli piszesz komendy Python jedna po drugiej, wykonując je poprzez naciśnięcie **Enter**, podczas gdy makra mogą zawierać bardziej złożony kod składający się z kilku linii, wykonywany tylko wtedy, gdy makro jest wykonywane.

![](images/Screenshot_pythoninterpreter.jpg ) 
*Konsola Python programu FreeCAD*

W tym samouczku możesz użyć obu metod. Możesz skopiować i wkleić każdą linię w konsoli Python, a następnie nacisnąć 

## Poznaj program FreeCAD od środka 

Zacznijmy od utworzenia nowego pustego dokumentu:


```python
doc = FreeCAD.newDocument()
```

Jeśli wpiszesz to w konsoli FreeCAD Python, zauważysz, że jak tylko wpiszesz `FreeCAD.`, pojawi się okno, pozwalające na szybkie autouzupełnianie reszty linii. Co więcej, każdy wpis na liście autouzupełniania ma etykietkę wyjaśniającą, co robi. Ułatwia to zapoznanie się z dostępnymi funkcjami. Zanim wybierzesz `newDocument`, zapoznaj się z innymi opcjami.

![](images/Screenshot_classbrowser.jpg ) 
*Mechanizm autouzupełniania dostępny w konsoli FreeCAD dla Python.*

Teraz nasz nowy dokument zostanie utworzony. Jest to podobne do naciśnięcia przycisku **<img src="images/Std_New.svg" width=16px> [Nowy](Std_New/pl.md)** na pasku narzędzi. W rzeczywistości większość przycisków w FreeCAD nie robi nic więcej niż wykonanie jednej lub więcej linii kodu Pythona. Co więcej, można ustawić opcję w **Edycja → Preferencje → Python → Makrodefinicje ** na **Pokaż polecenia skryptu w konsoli Python**. Spowoduje to wypisanie w konsoli całego kodu Python wykonanego po naciśnięciu przycisków. Bardzo przydatne do nauki odtwarzania akcji w Pythonie.

Wróćmy teraz do naszego dokumentu i zobaczmy, co możemy z nim zrobić:


```python
doc.
```

Zapoznaj się z dostępnymi opcjami. Zazwyczaj nazwy rozpoczynające się wielką literą są atrybutami, zawierają wartość, podczas gdy nazwy rozpoczynające się małą literą są funkcjami (zwanymi również metodami), \"robią coś\". Nazwy zaczynające się od podkreślenia są zwykle przeznaczone do wewnętrznego działania modułu i nie należy się nimi przejmować. Użyjmy jednej z metod, aby dodać nowy obiekt do naszego dokumentu:


```python
box = doc.addObject("Part::Box", "myBox")
```

Nic się nie dzieje. Dlaczego? Ponieważ FreeCAD został stworzony z myślą o dużym obrazie. Pewnego dnia będzie pracował z setkami złożonych obiektów, z których wszystkie będą od siebie zależne. Dokonanie gdzieś małej zmiany może mieć duży wpływ. Może być konieczne ponowne obliczenie całego dokumentu, co może zająć dużo czasu. Z tego powodu prawie żadne polecenie nie aktualizuje sceny automatycznie. Trzeba to robić samodzielnie:


```python
doc.recompute()
```

Teraz pojawił się nasz prostopadłościan. Wiele przycisków dodających obiekty w FreeCAD wykonuje w rzeczywistości dwie czynności: dodanie obiektu i ponowne obliczenie. Jeśli włączyłeś opcję **Pokaż polecenia skryptu w konsoli Python** powyżej, spróbuj dodać kulę za pomocą przycisku GUI. Zobaczysz dwie linie kodu Python wykonywane jedna po drugiej.

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

Jeśli wybierzesz swój prostopadłościan za pomocą myszy, zobaczysz, że w [Edytorze właściwości](Property_editor/pl.md), na karcie 

## Wektory i umiejscowienia 

[Wektory](https://en.wikipedia.org/wiki/Euclidean_vector) to bardzo podstawowe pojęcie w każdej aplikacji 3D. Wektor to lista 3 liczb (x, y i z) opisujących punkt lub pozycję w przestrzeni 3D. Z wektorami można zrobić wiele rzeczy, takich jak dodawanie, odejmowanie, rzutowanie i [wiele więcej](https://en.wikipedia.org/wiki/Vector_space). W FreeCAD wektory działają w następujący sposób:


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Inną wspólną cechą obiektów FreeCAD jest ich [umiejscowienie](Placement/pl.md). Każdy obiekt posiada właściwość **Umiejscowienie**, która zawiera **Baze** *(położenie)* i **Obrót** *(orientacja)* obiektu. Jest to łatwe do manipulowania, na przykład w celu przesunięcia naszego obiektu:


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

Zanim przejdziemy dalej, musisz zrozumieć kilka ważnych pojęć. 

## Aplikacja i interfejs graficzny 

FreeCAD został zaprojektowany tak, aby mógł być również używany bez interfejsu użytkownika, jako aplikacja wiersza poleceń. Prawie każdy obiekt w FreeCAD składa się z dwóch części: `Object`, jego komponentu \"geometrii\" oraz `ViewObject`, jego komponentu \"wizualnego\". Podczas pracy w trybie wiersza poleceń część geometryczna jest obecna, ale część wizualna jest wyłączona.

Aby zilustrować tę koncepcję, spójrzmy na nasz obiekt sześcianu. Właściwości geometryczne sześcianu, takie jak jego wymiary, położenie itp. są przechowywane w `Object`. Podczas gdy jego właściwości wizualne, takie jak kolor, grubość linii itp. są przechowywane w `ViewObject`. Odpowiada to zakładkom **Dane** i **Widok** w [Edytorze właściwości](Property_editor/pl.md). Dostęp do obiektu widoku obiektu można uzyskać w następujący sposób:


```python
vo = box.ViewObject
```

Teraz możesz także zmienić właściwości w zakładce **Widok**:


```python
vo.Transparency = 80
vo.hide()
vo.show()
```

Po uruchomieniu FreeCAD konsola Python ładuje już dwa moduły bazowe: 

## Moduły

Prawdziwa moc FreeCAD leży w jego wiernych modułach, z ich odpowiednimi środowiskami pracy. Podstawowa aplikacja FreeCAD jest mniej więcej pustym kontenerem. Bez swoich modułów może zrobić niewiele więcej niż tworzyć nowe, puste dokumenty. Każdy moduł nie tylko dodaje nowe środowiska pracy do interfejsu, ale także nowe polecenia Pythona i nowe typy obiektów. W rezultacie kilka różnych, a nawet całkowicie niekompatybilnych typów obiektów może współistnieć w tym samym dokumencie. Najważniejsze moduły FreeCAD, którym przyjrzymy się w tym samouczku to: [Część](Part_Workbench/pl.md), [Siatka](Mesh_Workbench/pl.md), [Szkicownik](Sketcher_Workbench/pl.md) i [Rysunek Roboczy](Draft_Workbench/pl.md).

[Szkicownik](Sketcher_Workbench/pl.md) i [Rysunek Roboczy](Draft_Workbench/pl.md) używają modułu [Część](Part_Workbench/pl.md) do tworzenia i obsługi swojej geometrii. Natomiast [Siatka](Mesh_Workbench/pl.md) jest całkowicie niezależny i obsługuje własne obiekty. Więcej na ten temat poniżej.

W ten sposób można sprawdzić wszystkie dostępne typy obiektów bazowych dla bieżącego dokumentu:


```python
doc.supportedTypes()
```

Różne moduły FreeCAD nie są automatycznie ładowane w konsoli Python. Ma to na celu uniknięcie bardzo powolnego uruchamiania. Moduły są ładowane tylko wtedy, gdy są potrzebne. Na przykład, aby zbadać, co znajduje się w module Part:


```python
import Part
Part.
```

Ale więcej o module Part powiemy poniżej. 

## Moduł Siatka 

[Siatki](https://en.wikipedia.org/wiki/Polygon_mesh) są bardzo prostym rodzajem obiektów 3D, używanym na przykład przez [Sketchup](https://en.wikipedia.org/wiki/SketchUp), [Blender](https://en.wikipedia.org/wiki/Blender_(software)) i [3D Studio Max](https://en.wikipedia.org/wiki/Autodesk_3ds_Max). Składają się one z 3 elementów: punktów *(zwanych również wierzchołkami)*, linii *(zwanych również krawędziami)* i powierzchni. W wielu aplikacjach, w tym FreeCAD, ściany mogą mieć tylko 3 wierzchołki. Oczywiście nic nie stoi na przeszkodzie, aby mieć większą ścianę składającą się z kilku współpłaszczyznowych trójkątów.

Siatki są proste, ale dlatego, że są proste, można łatwo mieć ich miliony w jednym dokumencie. Jednak w FreeCAD mają one mniejsze zastosowanie i są głównie po to, aby można było importować obiekty w formatach siatki (**.stl**, **.obj**) z innych aplikacji. Moduł Siatka był również intensywnie wykorzystywany jako główny moduł testowy w pierwszym miesiącu życia FreeCAD.

Obiekty Siatki i obiekty FreeCAD to różne rzeczy. Możesz zobaczyć obiekt FreeCAD jako kontener dla obiektu Siatka *(i jak zobaczymy poniżej, również dla obiektów Części)*. Aby dodać obiekt siatkowy do FreeCAD, musimy najpierw utworzyć obiekt FreeCAD i obiekt Siatki, a następnie dodać obiekt Siatki do obiektu FreeCAD:


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```

Jest to standardowy przykład wykorzystujący metodę `createSphere()` do utworzenia sfery, ale można również tworzyć niestandardowe siatki od podstaw, definiując ich wierzchołki i ściany.

[Więcej informacji o skryptach siatek \...](Mesh_Scripting/pl.md) 

## Moduł Część 

Moduł [Część](Part_Workbench/pl.md) jest najpotężniejszym modułem w całym FreeCAD. Pozwala on na tworzenie i manipulowanie obiektami [BRep](https://en.wikipedia.org/wiki/Boundary_representation). BREP to skrót od \"Boundary Representation\". Obiekt BREP jest definiowany przez powierzchnie, które otaczają i definiują wewnętrzną objętość. W przeciwieństwie do siatek, obiekty BREP mogą mieć wiele różnych komponentów, od płaskich powierzchni po bardzo złożone powierzchnie NURBS.

Moduł Część oparty jest na potężnej bibliotece [OpenCasCade](https://en.wikipedia.org/wiki/Open_CASCADE_Technology), która umożliwia wykonywanie szerokiej gamy złożonych operacji na tych obiektach, takich jak operacje logiczne, zaokrąglanie, przeciąganie itp.

Moduł Część działa w taki sam sposób jak moduł Siatka: Tworzysz obiekt FreeCAD, obiekt Część, a następnie dodajesz obiekt Część do obiektu FreeCAD:


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```

Moduł części (podobnie jak moduł siatki) ma również skrót, który automatycznie tworzy obiekt FreeCAD i dodaje do niego kształt, dzięki czemu można skrócić ostatnie trzy linie do:


```python
Part.show(myshape)
```

Eksplorując zawartość myshape, można zauważyć wiele interesujących komponentów podrzędnych, takich jak `Faces`, `Edges`, `Vertexes`, `Solids` i `Shells`, a także szeroki zakres operacji geometrii, takich jak `cut` *(odejmowanie)*, `common` *(przecinanie)* lub `fuse` *(łączenie)*. Strona [Skrypty danych topologicznych](Topological_data_scripting/pl.md) wyjaśnia to wszystko w szczegółach.

[Więcej informacji na temat skryptów części \...](Topological_data_scripting/pl.md) 

## Moduł rysunku Roboczego 

FreeCAD posiada wiele innych modułów, takich jak [Szkicownik](Sketcher_Workbench/pl.md) i [Rysunek Roboczy](Draft_Workbench/pl.md), które również tworzą obiekty Części. Moduły te dodają dodatkowe parametry do tworzonych obiektów, a nawet implementują zupełnie nowy sposób obsługi geometrii części. Nasz powyższy przykład prostopadłościanu jest doskonałym przykładem obiektu parametrycznego. Aby zdefiniować prostopadłościan, wystarczy określić parametry wysokości, szerokości i długości. Na ich podstawie obiekt automatycznie obliczy kształt części. FreeCAD pozwala na [tworzenie takich obiektów w środowisku Python](Scripted_objects/pl.md).

Moduł [Rysunek Roboczy](Draft_Workbench/pl.md) dodaje parametryczne typy obiektów 2D *(które są obiektami Części)*, takie jak linie i okręgi, a także zapewnia pewne ogólne funkcje, które działają nie tylko na obiektach Rysunek Roboczy, ale na każdym obiekcie Części. Aby zapoznać się z dostępnymi funkcjami, wystarczy wykonać następujące czynności:


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```


{{Top}}



## Interfejs

Interfejs użytkownika FreeCAD jest wykonany przy użyciu [Qt](https://en.wikipedia.org/wiki/Qt_(software)), potężnego systemu interfejsu graficznego, odpowiedzialnego za rysowanie i obsługę wszystkich elementów sterujących, menu, pasków narzędzi i przycisków wokół [widoku 3D](3D_view/pl.md). Qt udostępnia moduł [PySide](PySide/pl.md), który pozwala środowisku Pyton na dostęp i modyfikację interfejsów Qt, takich jak FreeCAD. Spróbujmy pobawić się interfejsem Qt i stworzyć proste okno dialogowe:


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```

Zauważ, że pojawiające się okno dialogowe ma ikonę FreeCAD na pasku narzędzi, co oznacza, że Qt wie, że polecenie zostało wydane z poziomu aplikacji FreeCAD. Możliwe jest manipulowanie dowolną częścią interfejsu FreeCAD.

Qt to bardzo potężny system interfejsu, który pozwala robić bardzo złożone rzeczy. Posiada również kilka łatwych w użyciu narzędzi, takich jak Qt Designer, za pomocą którego można projektować okna dialogowe graficznie, a następnie dodawać je do interfejsu FreeCAD za pomocą kilku linii kodu Python.

[Przeczytaj więcej o PySide tutaj \...](PySide/pl.md) 

## Makrodefinicje

Teraz, gdy dobrze zrozumiałeś podstawy, gdzie będziemy przechowywać nasze skrypty Python i jak będziemy je uruchamiać wewnątrz FreeCAD? Istnieje do tego prosty mechanizm o nazwie [Makrodefinicje](Macros/pl.md). Makro to skrypt Pythona, który można dodać do paska narzędzi i uruchomić za pomocą kliknięcia myszą. FreeCAD zapewnia prosty edytor tekstu (**Makrodefinicje → Makrodefinicje ... → Utwórz**), w którym można pisać lub wklejać skrypty. Gdy skrypt jest gotowy, użyj **Przybory → Dostosuj ... → Makrodefinicje**, aby zdefiniować dla niego przycisk, który można dodać do pasków narzędzi.



## Skrypty zewnętrzne 

Alternatywną metodą tworzenia, zapisywania i uruchamiania własnych skryptów Python jest tworzenie ich poza FreeCAD, przy użyciu wybranego edytora (na przykład Vim). Aby uruchomić skrypt Python wewnątrz FreeCAD, należy zapisać go z rozszerzeniem **.py**.

Następnie użyj polecenia **Plik → Otwórz**, aby otworzyć skrypt. Zostanie on załadowany do nowej karty w [Głównyn obszarze widoku](Main_view_area/pl.md). Skrypt można uruchomić, klikając przycisk **<img src="images/Std_DlgMacroExecuteDirect.svg" width=16px> [Wykonaj makro](Std_DlgMacroExecuteDirect/pl.md)**. Wszelkie błędy lub dane wyjściowe skryptu zostaną wyświetlone w oknie [Widoku raportu](Report_view.md).

Po wprowadzeniu i zapisaniu jakichkolwiek modyfikacji w już załadowanym skrypcie, pojawi się okno dialogowe z pytaniem, czy chcesz ponownie załadować zmodyfikowany skrypt do FreeCAD.

Możesz przejść do strony [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md) lub uzyskać dostęp do tej strony i innych odpowiednich stron na [Centrum Power użytkowników](Power_users_hub/pl.md). {{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Python scripting tutorial/pl
