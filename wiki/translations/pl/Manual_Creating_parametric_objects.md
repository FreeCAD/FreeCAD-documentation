# Manual:Creating parametric objects/pl
{{Manual:TOC}}

W [poprzednim rozdziale](Manual:Creating_and_manipulating_geometry/pl.md) badaliśmy, jak tworzyć geometrię **Część** i wyświetlać ją na ekranie, przypisując ją do \"głupiego\" (nie-parametrycznego) obiektu dokumentu. Choć ta metoda jest skuteczna, staje się uciążliwa, gdy trzeba zmienić kształt. Każda zmiana wymaga stworzenia nowego kształtu i przypisania go do obiektu, co prowadzi do powtarzalnych i nieefektywnych procesów roboczych.

W całym tym podręczniku widzieliśmy, jak obiekty parametryczne rozwiązują ten problem, umożliwiając dynamiczne aktualizacje. Poprzez modyfikację jednej właściwości, kształt jest automatycznie przeliczany, eliminując konieczność ręcznych aktualizacji. Ten proces przeliczania umożliwia bardziej efektywne modelowanie i wprowadza elastyczność do projektów. Wewnątrz obiekty parametryczne działają podobnie do tego, co już robiliśmy: przeliczają zawartość swojej właściwości **Kształt** za każdym razem, gdy jedna z ich właściwości się zmienia. Ten iteracyjny proces jest płynny i zapewnia, że obiekt pozostaje zgodny z określonymi parametrami.

FreeCAD oferuje przyjazny system do tworzenia obiektów parametrycznych w całości w Pythonie. Obiekty te są definiowane za pomocą klasy Pythona, która:

-   Deklaruje niezbędne właściwości dla obiektu.
-   Definiuje zachowanie, gdy któraś z tych właściwości zostanie zmodyfikowana.

Struktura takiego obiektu parametrycznego jest tak prosta, jak ta:


```python
class myParametricObject:

    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "MyLength")
        ...

    def execute(self,obj):
        print ("Recalculating the shape...")
        print ("The value of MyLength is:")
        print (obj.MyLength)
        ...
```

Wszystkie klasy Pythona zazwyczaj mają metodę **\_\_init\_\_**. Ta metoda jest wykonywana, gdy klasa jest instantiowana --- czyli gdy obiekt Pythona jest tworzony z klasy. Można traktować klasę jako \"szablon\" lub plan, który służy do tworzenia żywych instancji samej siebie. Każda instancja klasy staje się niezależnym obiektem ze swoimi własnymi atrybutami i metodami. W naszej metodzie **\_\_init\_\_** wykonujemy dwie kluczowe czynności:

-   Zapisz samą klasę w atrybucie **Proxy** obiektu dokumentu FreeCAD:

Przypisując **self** do atrybutu **Proxy** obiektu dokumentu FreeCAD, łączymy logikę naszej klasy Pythona z obiektem FreeCAD. Oznacza to, że obiekt dokumentu \"przechowa\" kod klasy Pythona wewnątrz siebie, co pozwala mu zachowywać się zgodnie z logiką zdefiniowaną w klasie. To połączenie umożliwia FreeCAD interakcję z obiektem parametrycznym i jego ponowne przeliczenie.

-   Tworzenie wszystkich właściwości, których obiekt potrzebuje:

Za pomocą metody **addProperty** definiujemy niestandardowe właściwości wymagane przez obiekt. Właściwości działają jako parametry lub zmienne dla obiektu i mogą być dostępne, modyfikowane oraz wyświetlane w edytorze właściwości FreeCAD. W tym przykładzie dodajemy właściwość typu zmiennoprzecinkowego o nazwie **MyLength**. Ta właściwość będzie później wpływać na kształt lub zachowanie obiektu.

We FreeCAD dostępnych jest wiele typów właściwości, począwszy od liczb zmiennoprzecinkowych po łańcuchy znaków, a nawet specjalistyczne typy dla geometrii i materiałów. Aby zapoznać się z pełną listą dostępnych typów właściwości, można wpisać poniższy kod w konsoli Pythona:


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```

Drugą kluczową częścią naszej klasy jest metoda **execute**. Ta metoda jest automatycznie wywoływana, gdy obiekt zostaje oznaczony do ponownego obliczenia, co ma miejsce, gdy jedna z jego właściwości zostanie zmodyfikowana. Metoda **execute** to miejsce, w którym odbywają się wszystkie przeliczenia obiektu, zapewniając, że jego kształt i zachowanie są zaktualizowane, aby odzwierciedlić wszelkie zmiany. Wewnątrz metody **execute** wykonujesz wszystkie niezbędne operacje do wygenerowania nowej geometrii dla swojego obiektu. Zwykle polega to na przeliczeniu kształtu na podstawie bieżących wartości jego właściwości, a następnie przypisaniu zaktualizowanego kształtu do atrybutu **Shape** obiektu za pomocą polecenia takiego jak **obj.Shape = myNewShape**. Metoda **execute** przyjmuje jeden argument, **obj**, który reprezentuje obiekt dokumentu FreeCAD powiązany z twoim obiektem parametrycznym. Dzięki temu możesz bezpośrednio manipulować obiektem wewnątrz tej metody, np. uzyskiwać dostęp do jego właściwości, aktualizować jego geometrię lub wykonywać inne operacje.

Podsumowując:

-   Metoda **execute** jest wywoływana za każdym razem, gdy obiekt wymaga aktualizacji.
-   Odpowiada za przeliczenie kształtu i przypisanie go do atrybutu **Shape** obiektu.
-   Argument **obj** umożliwia dostęp do obiektu dokumentu FreeCAD, co pozwala na dokonywanie zmian programowo.

Dzięki temu systemowi, FreeCAD zajmuje się resztą - zapewniając, że obiekt zostanie prawidłowo zaktualizowany w dokumencie i poprawnie wyświetlony w interfejsie graficznym.

Jedną z ważnych rzeczy, o których należy pamiętać, jest to, że gdy tworzysz obiekty parametryczne w dokumencie programu FreeCAD, używany kod Pythona do ich definiowania nie jest zapisywany w pliku. Jest to celowy środek bezpieczeństwa. Gdyby pliki programu FreeCAD mogły przechowywać kod Pythona, mogłoby to otworzyć drogę dla osób złośliwych do rozpowszechniania plików zawierających szkodliwe skrypty, które mogłyby uszkodzić komputer użytkownika. W związku z tym, gdy udostępniasz plik programu FreeCAD zawierający obiekty parametryczne stworzone za pomocą niestandardowego kodu Pythona, odbiorca musi mieć dostęp do kodu, który zdefiniował te obiekty. Bez tego, FreeCAD nie będzie wiedział, jak prawidłowo przeliczyć ani wchodzić w interakcję z obiektami.

Najprostszym sposobem zapewnienia tego jest zapisanie kodu Pythona w pliku makra. Przy udostępnianiu pliku FreeCAD możesz dołączyć makro obok niego. Alternatywnie, możesz udostępnić makro w [repozytorium makr FreeCAD](Macros_recipes.md), umożliwiając innym łatwe pobranie i użycie go. Takie podejście zapewnia, że twoje niestandardowe obiekty parametryczne pozostaną funkcjonalne na innych systemach, zachowując jednocześnie zasady najlepszych praktyk bezpieczeństwa.

Poniżej wykonamy małe ćwiczenie, budując obiekt parametryczny, który jest prostą parametryczną prostokątną powierzchnią. Bardziej złożone przykłady są dostępne na stronie [Obiekty tworzone skryptami](Scripted_objects/pl.md) oraz w samym kodzie źródłowym [FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py).

Nadamy naszemu obiektowi dwie właściwości: Długość i Szerokość, które wykorzystamy do skonstruowania prostokąta. Następnie, ponieważ nasz obiekt będzie już miał wstępnie zbudowaną właściwość Umiejscowienie (wszystkie obiekty geometryczne mają ją domyślnie, nie trzeba jej dodawać samodzielnie), przesuniemy nasz prostokąt do lokalizacji / obrotu ustawionego w Placement, dzięki czemu użytkownik będzie mógł przenieść prostokąt w dowolne miejsce, edytując właściwość Umiejscowienie.


```python
class ParametricRectangle:

    def __init__(self,obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "Length")
        obj.addProperty("App::PropertyFloat", "Width")

    def execute(self, obj):
        # We need to import the FreeCAD module here too, because we might be running out of the Console
        # (in a macro, for example) where the FreeCAD module has not been imported automatically:
        import FreeCAD
        import Part

        # First we need to make sure the values of Length and Width are not 0
        # otherwise Part.LineSegment will complain that both points are equal:
        if (obj.Length == 0) or (obj.Width == 0):
            # If yes, exit this method without doing anything:
            return

        # We create 4 points for the 4 corners:
        v1 = FreeCAD.Vector(0, 0, 0)
        v2 = FreeCAD.Vector(obj.Length, 0, 0)
        v3 = FreeCAD.Vector(obj.Length,obj.Width, 0)
        v4 = FreeCAD.Vector(0, obj.Width, 0)

        # We create 4 edges:
        e1 = Part.LineSegment(v1, v2).toShape()
        e2 = Part.LineSegment(v2, v3).toShape()
        e3 = Part.LineSegment(v3, v4).toShape()
        e4 = Part.LineSegment(v4, v1).toShape()

        # We create a wire:
        w = Part.Wire([e1, e2, e3, e4])

        # We create a face:
        f = Part.Face(w)

        # All shapes have a Placement too. We give our shape the value of the placement
        # set by the user. This will move/rotate the face automatically.
        f.Placement = obj.Placement

        # All done, we can attribute our shape to the object!
        obj.Shape = f
```

Zamiast wklejać powyższy kod w konsoli Python, lepiej zapiszmy go gdzieś, abyśmy mogli go później ponownie wykorzystać i zmodyfikować. Na przykład w postaci nowej makrodefinicji *(menu **Makrodefinicje → Makrodefinicje → Utwórz**)*. Nazwij je na przykład \"ParamRectangle\". Jednak makra FreeCAD są zapisywane z rozszerzeniem .FCMacro, którego Python nie rozpoznaje podczas importowania. Tak więc, przed użyciem powyższego kodu, będziemy musieli zmienić nazwę pliku ParamRectangle.FCMacro na ParamRectangle.py. Można to zrobić z poziomu eksploratora plików, przechodząc do folderu Macros wskazanego w menu Przybory → Makrodefinicje.

Gdy to zrobimy, możemy teraz zrobić to w konsoli Python:


```python
import ParamRectangle
```

Badając zawartość ParamRectangle, możemy sprawdzić, czy zawiera ona naszą klasę ParametricRectangle.

Aby utworzyć nowy obiekt parametryczny przy użyciu naszej klasy ParametricRectangle, użyjemy następującego kodu. Zauważ, że używamy **Part::FeaturePython** zamiast **Part::Feature**, którego używaliśmy w poprzednich rozdziałach *(wersja Python pozwala na zdefiniowanie własnego zachowania parametrycznego)*:


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

Oto szybkie wyjaśnienie poprzednich poleceń:

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\", \"Rectangle\")**: Tworzy nowy obiekt **Part::FeaturePython** o nazwie **Rectangle** w aktywnym dokumencie FreeCAD. Ten obiekt jest specjalnie zaprojektowany do niestandardowego zachowania parametrycznego, pozwalając na zarządzanie jego właściwościami i zachowaniem za pomocą logiki zdefiniowanej w Pythonie.

-   **ParamRectangle.ParametricRectangle(myObj)**: Inicjalizuje obiekt, łącząc go z klasą **ParametricRectangle** z modułu lub skryptu **ParamRectangle**. To połączenie pozwala na powiązanie niestandardowej logiki zdefiniowanej w Pythonie z obiektem, umożliwiając mu działanie jako obiekt parametryczny.

-   **myObj.ViewObject.Proxy = 0**: Resetuje atrybut **ViewObject.Proxy** do 0, co zapewnia, że obiekt używa domyślnego zarządzania widokiem w FreeCAD. Ten krok jest wymagany, chyba że zdefiniujesz niestandardowy **ViewProvider**, który zarządza wizualną reprezentacją obiektu.

-   **FreeCAD.ActiveDocument.recompute()**: Ponownie przelicza dokument, aby zaktualizować geometrię i odzwierciedlić zmiany w interfejsie graficznym FreeCAD, czyniąc nowy obiekt w pełni widocznym i funkcjonalnym.

Nic nie pojawi się jeszcze na ekranie, ponieważ właściwości **Długość** i **Szerokość** mają wartość 0, co spowoduje uruchomienie naszego warunku \"do-nothing\" wewnątrz execute. Musimy tylko zmienić wartości Długość i Szerokość, a nasz obiekt w magiczny sposób pojawi się i zostanie ponownie przeliczony w locie.

Oczywiście uciążliwe byłoby wpisywanie tych 4 linijek kodu Python za każdym razem, gdy chcemy utworzyć nowy parametryczny prostokąt. Bardzo prostym sposobem na rozwiązanie tego problemu jest umieszczenie powyższych 4 linijek wewnątrz naszego pliku **ParamRectangle.py**, na końcu, po zakończeniu klasy **ParametricRectange** *(możemy to zrobić z poziomu edytora makrodefinicji)*.

Teraz, gdy wpiszemy import ParamRectangle, automatycznie zostanie utworzony nowy prostokąt parametryczny. Co więcej, możemy dodać przycisk na pasku narzędzi, który właśnie to zrobi:

-   Otwórz menu **Przybory → Dostosuj**
-   W zakładce \"Makra\" wybierz nasze makro ParamRectangle.py, wypełnij szczegóły według własnego uznania i naciśnij \"Dodaj\":

![](images/FreeCAD_python_macroRec.png )

-   W zakładce Paski narzędzi utwórz nowy niestandardowy pasek narzędzi w wybranym środowisku pracy *(lub globalnie)*, wybierz makrodefinicję i dodaj je do paska narzędzi:

![](images/FreeCAD_python_toolbarCus.png )

-   To wszystko, mamy teraz nowy przycisk paska narzędzi, który po kliknięciu utworzy parametryczny prostokąt.

Pamiętaj, że jeśli chcesz rozpowszechniać pliki utworzone za pomocą tego nowego narzędzia innym osobom, muszą one również mieć zainstalowaną makrodefinicję **ParamRectangle.py** na swoich komputerach.

**Więcej informacji:**

-   [Przepisy na makropolecenia](Macros_recipes/pl.md)
-   [Obiekty tworzone skryptami](Scripted_objects/pl.md)
-   [Więcej przykładów kodu FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating parametric objects/pl
