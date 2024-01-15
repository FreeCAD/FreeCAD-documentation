---
 GuiCommand:
   Name: Draft ShapeString
   Name/pl: Rysunek Roboczy: Kształt z tekstu
   MenuLocation: Kreślenie , Kształt z tekstu ...
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: 
   Version: 0.14
   SeeAlso: Draft_Text/pl, Draft_Label/pl, Part_Extrude/pl
---

# Draft ShapeString/pl



## Opis

Polecenie <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Kształt z tekstu** tworzy złożony kształt reprezentujący ciąg tekstowy. Kształt ten może być użyty do tworzenia liter 3D za pomocą polecenia [Wyciągnij](Part_Extrude/pl.md) środowiska pracy Część.

Polecenie Kształt z tekstu nie jest przeznaczone do wykonywania standardowych adnotacji tekstowych. W tym celu należy użyć polecenia [Tekst](Draft_Text/pl.md) lub [Etykieta](Draft_Label/pl.md).

![](images/Draft_ShapeString_Example400.png ) 
*Pojedynczy punkt wymagany do pozycjonowania obiektu Kształt z tekstu*



## Użycie

Dla użytkowników Windows OS: przeczytaj najpierw akapit [Wybór pliku czcionki w systemie Windows](#Wybór_pliku_czcionki_w_systemie_Windows.md).

1.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_ShapeString.svg" width=16px> '''Kształt z tekstu'''**.
    -   Wybierz opcję z menu **Kreślenie → <img src="images/Draft_ShapeString.svg" width=16px> Kształt z tekstu**.
2.  Otworzy się panel zadań **Kształt z tekstu**.
3.  Kliknij punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne.
4.  Opcjonalnie naciśnij przycisk **Zresetuj współrzędne punktu**, aby zresetować punkt do położenia punktu początkowego.
5.  Wprowadź **Ciąg znaków**.
6.  Określ **Wysokość**.
7.  Aby wybrać czcionkę, wykonaj jedną z poniższych czynności:
    -   Wprowadź ścieżkę do pliku w polu wprowadzania **Plik czcionki**.
    -   Naciśnij przycisk **...** i wybierz plik.
8.  Naciśnij przycisk **OK**, aby zakończyć polecenie.
9.  Opcjonalnie można zmienić włąściwość **Wyrównanie** dla tekstu. Zobacz [Właściwości](#Właściwości.md).



## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.



## Uwagi

-   Szkic obiektu Kształt z tekstu może być edytowany poprzez dwukrotne kliknięcie go w [Widoku drzewa](Tree_view/pl.md). {{Version/pl|0.20}}
-   Obsługiwane czcionki to TrueType (**.ttf**), OpenType (**.otf**) i Type 1 (**.pfb**).
-   Polecenie jest ograniczone do tekstu od lewej do prawej. Teksty od prawej do lewej i od góry do dołu nie są obsługiwane.
-   Bardzo małe wysokości tekstu mogą skutkować zdeformowanymi kształtami znaków z powodu utraty szczegółów podczas skalowania.
-   Wiele czcionek wygeneruje problematyczną geometrię. Wynika to z faktu, że kontury czcionek mogą się nakładać, mieć małe odstępy i mieć różne kierunki w obrębie glifu. Warunki te są uważane za błędy w poliliniach używanych do definiowania ścian.
-   Kształt z tekstu można również utworzyć za pomocą makrodefinicji [Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP/pl.md).
-   Aby utworzyć Kształt tekstu ułożony w okrąg, należy użyć makrodefinicji [FCCircularText](Macro_FCCircularText/pl.md).



## Wybór pliku czcionki w systemie Windows 

W systemie Windows dostęp do domyślnego folderu czcionek jest chroniony. Ma to wpływ na wybór pliku czcionki dla obiektu Kształt z tekstu. W FreeCAD istnieją trzy przypadki, w których można określić plik czcionki dla tekstu: w panelu zadań Kształt z tekstu, podczas zmiany właściwości **Plik czcionki** tekstu oraz podczas określania domyślnego pliku czcionki w [Ustawieniach](Draft_Preferences/pl#Teksty_i_wymiary.md) środowiska pracy Rysunek Roboczy.

Naciśnięcie przycisku **...**, a następnie wybranie pliku z domyślnego folderu czcionek systemu Windows nie jest możliwe podczas korzystania z natywnego okna dialogowego plików. Istnieje kilka rozwiązań:

-   Upewnij się, że wartość opcji **DontUseNativeFontDialog** jest ustawiona na {{True/pl}}, co jest wartością domyślną dla tej preferencji. Spowoduje to wywołanie innego, nienatywnego okna dialogowego pliku tylko po naciśnięciu przycisku **...** na panelu zadań Kształt z tekstu. Za pomocą tego okna dialogowego plików można uzyskać dostęp do domyślnego folderu czcionek systemu Windows.
-   Zmień wartość opcji **DontUseNativeDialog** na {{True/pl}}. To instruuje FreeCAD, aby zawsze używał okna dialogowego innego niż systemowe.
-   Określ plik czcionki w polu wprowadzania. Możesz oczywiście wpisać pełną ścieżkę lub skopiować-wkleić ścieżkę z Eksploratora plików Windows. Istnieje jednak również inny sposób wprowadzenia ścieżki. Jeśli wpiszesz {{Value|C:\}}, pojawi się lista rozwijana. Wybierz {{Value|Windows}} z tej listy i dodaj {{Value|\F}}. Z nowej listy rozwijanej wybierz {{Value|Fonts}}. Na koniec dodaj {{Value|\}} i pierwszą literę *(lub kilka)* pliku czcionki, a następnie wybierz ją z rozwijanej listy.
-   Utwórz niestandardowy folder dla plików czcionek.

Zobacz akapit [Ustawienia](#Ustawienia.md) poniżej, aby sprawdzić lokalizację wspomnianych preferencji.



## Poradniki

-   [Poradnik: Rysunek Roboczy kształt z tekstu](Draft_ShapeString_tutorial/pl.md): wyciągnięcie Kształtu z tekstu, umieszczenie go w przestrzeni 3D i utworzenie grawerunku w innej bryle.
-   [Jak używać Kształtu z tekstu w środowisku pracy Projekt Części](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623).



## Ustawienia

Zobacz także: [Edytor ustawień](Preferences_Editor/pl.md), [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md) i [Edytor parametrów](Std_DlgParameter/pl.md).

-   Domyślny plik czcionki można zmienić w preferencjach: **Edycja → Preferencje ... → Rysunek Roboczy → Teksty i wymiary → Domyślny plik czcionki kształtu z tekstu**.
-   Dla użytkowników systemu Windows:
    -   Ustaw wartość parametru **Przybory → Edytor parametrów ... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog** na {{True/pl}}, aby użyć niesystemowego okna dialogowego wyboru pliku podczas wybierania pliku czcionki z panelu zadań Kształt z tekstu.
    -   Alternatywnie można ustawić parametr **Przybory → Edytor parametrów ... → BaseApp → Preferences → Dialog → DontUseNativeDialog** na {{True/pl}}, aby zawsze używać niesystemowego okna dialogowego wyboru pliku.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt *Kształt z tekstu* wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rysunek Roboczy}}

-    **Plik czcionki|File**: Nazwa pliku czcionki.

-    **Sczl|Bool**: Łączenie ścian, jeśli zachodzą na siebie, zwykle nie jest wymagane *(może być bardzo powolne)*. Ignorowane, jeśli parametr **Utwórz ścianę** ma wartość {{FALSE/pl}}. {{Version/pl|0.22}}

-    **Wyrównanie|Enumeration**: Wyrównanie poziome i pionowe. Opcje: {{value|Góra-lewo}}, {{value|Góra-środek}}, {{value|Góra-prawo}}, {{value|Środek-lewo}}, {{value|Środek}}, {{value|Środek-prawo}}, {{value|Dół-lewo}}, {{value|Dół-środek}}, {{value|Dół-prawo}}. {{Version/pl|0.22}}

-    **Odniesienie wyrównania|Enumeration**: Odniesienie do wysokości używane do wyrównania. Opcje: {{value|Wysokość nasadki}}, {{value|Wysokość kształtu}}. Wysokość kształtu zależy od znaków w **Ciągu znaków**. {{Version/pl|0.22}}

-    **Zachowaj lewy margines|Bool**: Zachowuje lewy margines i wiodącą spację, gdy justowanie jest w lewo. {{Version/pl|0.22}}.

-    **Utwórz ścianę|Bool**: Wypełnia litery licami.

-    **Kąt skośny|Angle**: Kąt ukośny. Musi mieścić się w zakresie od -80° do +80°. <small>(v0.22)</small> .

-    **Skaluj do rozmiaru|Bool**: Skalowanie w celu zapewnienia, że wysokość nakładki jest równa rozmiarowi. Jeśli ustawiono na {{FALSE/pl}}, w zależności od czcionki, wysokość nakładki nie będzie dokładnie odpowiadać wartości **Rozmiar**. {{Version/pl|0.22}}

-    **Rozmiar|Length**: Wysokość tekstu.

-    **Ciąg znaków|String**: Ciąg tekstowy. Obiekt Kształt z tekstu może wyświetlać tylko jedną linię tekstu.

-    **Kontrola|Distance**: Odstęp między znakami. Typ właściwości został zaktualizowany ({{Version/pl|0.22}}).

<img alt="" src=images/Draft_ShapeString_Justification.png  style="width:200px;"> 
*Wysokość czerwonego prostokąta ''(linia ciągła)'' jest równa wysokości nakładki.<br>
Wysokość zielonego prostokąta ''(linia przerywana)'' jest równa wysokości kształtu.<br>
Narożniki, środki krawędzi i środki prostokątów<br>
dopasuj 9 opcji wyrównania: od lewego górnego do prawego dolnego rogu.*



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć Kształt z tekstu użyj metody `make_shapestring` modułu Rysunek Roboczy *({{Version/pl|0.19}})*. Ta metoda zastępuje przestarzałą metodę `makeShapeString`.


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```

-   Tworzy złożony kształt `shapestring` przy użyciu określonego `String` i pełnej ścieżki obsługiwanego `FontFile`.

-    `Size`to wysokość wynikowego tekstu w milimetrach.

-    `Tracking`to odstęp między znakami w milimetrach.

Umiejscowienie obiektu Kształt z tekstu można zmienić nadpisując jego atrybut `Placement` lub indywidualnie nadpisując jego atrybuty `Placement.Base` i `Placement.Rotation`.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/pl
