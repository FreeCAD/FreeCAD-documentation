# Object name/pl
## Wprowadzenie




Wszystkie obiekty w programie mają [nazwę obiektu](Object_name/pl.md), która jednoznacznie identyfikuje je w obrębie danego dokumentu.

Informacje te dotyczą wszystkich obiektów pochodnych od [App: Obiektu dokumentu](App_DocumentObject/pl.md) *(klasa `App::DocumentObject`)*, która zasadniczo obejmuje wszystkie obiekty, które można utworzyć w dokumencie.



## Nazwy

Nazwy mają różne właściwości:

-    {{Incode|Nazwa}}może zawierać tylko proste znaki alfanumeryczne i znak podkreślenia, {{Incode|[_0-9a-zA-Z]}}.

-    {{Incode|Nazwa}}nie może zaczynać się od cyfry, musi zaczynać się od litery lub podkreślenia, {{Incode|[_a-zA-Z]}}.

-    {{Incode|Nazwa}}jest przypisywana w czasie tworzenia obiektu, później nie można jej już edytować. Nigdy nie można zmienić nazwy obiektu.

-    {{Incode|Nazwa}}musi być unikalna w całym dokumencie. Nie ma znaczenia, czy dwa obiekty są zupełnie różnych typów, na przykład jeden to [kieszeń](PartDesign_Pocket/pl.md) środowiska Projekt Części, a drugi to [ściana](Arch_Wall/pl.md) środowiska Architektura. Muszą one mieć różne nazwy.

-   Podczas tworzenia obiektu tego samego typu, zwykle nazwa jest zwiększana o kolejny numer, a więc `Sześcian`, `Sześcian001`, `Sześcian002` itd. Zapobiega to kolizji nazw.

-   Po usunięciu obiektu, jego `Nazwa` staje się dostępna do użycia przez nowo utworzony obiekt. Oznacza to, że jeśli istnieją obiekty `Sześcian`, `Sześcian001` i `Sześcian002`, a my usuniemy pierwszy z nich, to następnym obiektem utworzonym za pomocą [Part Box](Part_Box.md) nie będzie `Sześcian003`, lecz `Sześcian`, ponieważ ciąg ten jest dostępny do ponownego użycia. Zauważ, że nie jest możliwa zmiana nazwy obiektu `Sześcian001` lub `Sześcian002` na `Sześcian`, ponieważ ich nazwy są niezmienne.

Podsumowując, `Nazwa` zasadniczo działa jak unikalny identyfikator (UID) dla obiektu. Ponieważ unikalna `Nazwa` jest bardzo restrykcyjna, wszystkie obiekty mają również właściwość `Etykieta`, która umożliwia \"zmianę nazwy\" obiektu na coś bardziej opisowego. Wewnętrzna {{Incode|Nazwa}} faktycznie pozostaje stała, ale edytowalna przez użytkownika {{Incode|Etykieta}} może być używana w większości sytuacji, w których użyto by {{Incode|Nazwy}}. W powszechnym użyciu w programie i dokumentacji \"zmiana nazwy\" oznacza zmianę `Etykiety`, a nie rzeczywistej `Nazwy` obiektu.



## Etykiety

Istnieją różne właściwości etykiet:

-    {{Incode|Etykieta}}może akceptować dowolny ciąg UTF8, w tym znaki akcentu i spacji.

-   W oknie [widoku drzewa](Tree_view/pl.md) wyświetlana jest `Etykieta` obiektu, a nie jego `Nazwa`. Dlatego za każdym razem, gdy tworzony jest nowy obiekt, dobrą praktyką jest zmiana `Etykiety` na bardziej opisowy ciąg znaków. Aby zmienić nazwę *(etykietę)* obiektu, wybierz ją w widoku drzewa i naciśnij **F2** *(lub raczej **Return** na macOS)* lub otwórz menu podręczne *(kliknij prawym przyciskiem myszy)* i wybierz **Zmień nazę**.

-   Nawet po zmianie nazwy obiektu, wewnętrzny {{Incode|NamNazwae}} będzie nadal wyświetlana w wielu miejscach, na przykład na pasku [pasek stanu](Status_bar.md) lub w oknie [widok wyboru](Selection_view/pl.md), gdy obiekt jest zaznaczony.

-   Ponieważ wewnętrzne funkcje programu odnoszą się do obiektów za pomocą {{Incode|Nazwy}}, wiele okien dialogowych wyświetli najpierw {{Incode|Nazwę}}, a następnie edytowalną przez użytkownika {{Incode|Etykietę}} w nawiasach, na przykład {{Incode|Sześcian ''(Element wyciągany)''}}.

-   Domyślnie {{Incode|Etykieta}} jest unikalna, podobnie jak {{Incode|Nazwa}}. Zachowanie to można jednak zmienić w [edytorze preferencji](Preferences_Editor/pl.md), **Edycja → Preferencje ... → Ogólne → Dokument → Zezwalaj na umieszczanie duplikatów etykiet obiektów w obrębie jednego dokumentu**. Oznacza to, że generalnie {{Incode|Etykieta}} nie jest unikalna w dokumencie i może się powtarzać. Zaleca się jednak zachowanie unikalności `Etykiet`, ponieważ jest to prawdopodobnie najbardziej przydatne do identyfikacji różnych obiektów. Podczas pisania niestandardowych funkcji, które manipulują obiektami, metody powinny używać `Nazwy` obiektu, a nie jego `Etykiety`, aby zagwarantować, że używany jest właściwy obiekt.

-   Podczas korzystania z [wyrażeń](Expressions/pl.md), na przykład w [edytorze właściwości](Property_editor/pl.md) lub w [arkuszu kalkulacyjnym](Spreadsheet/pl.md), Etykieta może być przywoływana za pomocą podwójnych nawiasów utworzonych z symboli \"mniej niż\" i \"więcej niż\".


```python
<<Custom Label With Spaces>>.Height
<<Label may use UTF8 characters>>.Width
```



### Etykieta2

Jest to prosty ciąg znaków, który może zawierać dowolny tekst, a zatem może być używany do dokumentowania *(opisywania z większą ilością szczegółów)* utworzonego obiektu.

-   W oknie [widoku drzewa](Tree_view/pl.md) edytuj pole obok ikony, w kolumnie \"Opis\", klikając je i naciskając **F2** *(lub raczej **Entern** na macOS)*.
-   Można również zmienić tę właściwość, modyfikując atrybut `Etykieta2` z poziomu [Konsoli Python](Python_console/pl.md).
-   Atrybut **Etykieta2** jest normalnie ukryty w [edytorze właściwości](Property_editor/pl.md), ale może być uwidoczniony poprzez otwarcie menu podręcznego *(kliknięcie prawym przyciskiem myszy)* i wybranie **Wyświetl wszystko**.



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Każdy obiekt w oprogramowaniu jest tworzony wewnętrznie za pomocą metody `addObject()` dokumentu. Większość obiektów 2D i 3D, które użytkownik zobaczy w oknie [widoku 3D](3D_view/pl.md) pochodzi z [Część: Cecha](Part_Feature/pl.md). W poniższym przykładzie utworzony obiekt to [Sześcian](Part_Box/pl.md) środowiska pracy Część.


```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Box", "Name")
obj.Label = "Custom label"
```



### Nazwa

Funkcja `addObject` posiada dwa podstawowe argumenty typu string.

-   Pierwszy argument wskazuje typ obiektu, w tym przypadku `"Part::Box"`.
-   Drugi argument to ciąg znaków definiujący atrybut `Name`. Jeśli nie zostanie on podany, domyślnie przyjmuje taką samą nazwę jak klasa obiektu, czyli `"Part__Box"`, gdzie dwa nieprawidłowe symbole, dwukropki `::`, są zastąpione dwoma podkreśleniami `__`.
    -   
        `Name`
        
        może zawierać tylko podstawowe znaki alfanumeryczne i znak podkreślenia, `[_0-9a-zA-Z]`. Jeśli podane zostaną inne symbole, zostaną one przekonwertowane na znak podkreślenia. Na przykład `"A+B:C*"` zostanie przekonwertowane na `"A_B_C_"`.

    -   
        {{Incode|Name}}
        
        nie może zaczynać się od liczby, musi zaczynać się od litery lub podkreślenia, {{Incode|[_a-zA-Z]}}. Na przykład `"123ABC"` jest konwertowany na `"_23ABC"`.

    -   Obiekt `Name` jest ustalany w momencie utworzenia, nie można go później zmodyfikować.

    -   Obiekt `Name` musi być unikalny w całym dokumencie. Jeśli użyty zostanie ten sam obiekt {{Incode|"Name"}}, automatycznie dołączony zostanie kolejny numer, tak aby wynikowe nazwy były unikalne; na przykład, jeśli {{Incode|"Name"}} już istnieje, nowe obiekty zostaną nazwane {{Incode|"Name001"}}, {{Incode|"Name002"}}, {{Incode|"Name003"}} itd.



### Etykieta

Obiekt `Label` jest właściwością utworzonego obiektu i może zostać zmieniony na bardziej znaczący tekst.

-   Podczas tworzenia obiektu, `Label` ma taką samą wartość jak `Name`.
-   Jednak w przeciwieństwie do `Name`, `Label` może akceptować dowolny ciąg UTF8, łącznie ze znakami akcentówi i spacji.
-   Obiekt `Label` można zmienić w dowolnym momencie, po prostu przypisując żądany ciąg znaków, obj.Label = "New label".



### Pobieranie obiektu przez nazwę lub etykietę 

Wszystkie obiekty w dokumencie są atrybutami danych odpowiedniego obiektu [Dokument](App_DocumentObject/pl.md). Nazwa atrybutu odpowiada wewnętrznej `Nazwie` obiektu.


```python
import FreeCAD as App

obj1 = App.ActiveDocument.Box
obj2 = App.ActiveDocument.Box001
obj3 = App.ActiveDocument.Box002
```

Jest to równoważne użyciu metody `getObject` dokumentu. 
```python
import FreeCAD as App

obj1 = App.ActiveDocument.getObject('Box')
obj2 = App.ActiveDocument.getObject('Box001')
obj3 = App.ActiveDocument.getObject('Box002')
```

Możliwe jest jednak również pobranie obiektu za pomocą bardziej opisowego identyfikatora `Label`. 
```python
import FreeCAD as App

obj1 = App.ActiveDocument.getObjectsByLabel("Concrete wall")[0]
obj2 = App.ActiveDocument.getObjectsByLabel("Custom parallelepiped")[0]
obj3 = App.ActiveDocument.getObjectsByLabel("Some special name for this cube__002")[0]
```

Biorąc pod uwagę, że obiekt `Label` nie jest unikalny, metoda `getObjectsByLabel` zwraca listę wszystkich obiektów znalezionych z tym obiektem `Label`. Jeśli jednak `Label` jest unikalny w dokumencie, to pierwszym elementem tej listy powinien być żądany obiekt.



---
⏵ [documentation index](../README.md) > Object name/pl
