---
- GuiCommand:/pl
   Name:Draft Text
   Name/pl:Rysunek roboczy: Tekst
   MenuLocation:Adnotacja → Tekst
   Workbenches:[Rysunek roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut:**T** **E**
   Version:0.7
   SeeAlso:[Etykieta](Draft_Label/pl.md), [Kształt z tekstu](Draft_ShapeString/pl.md)
---

# Draft Text/pl

## Opis

Narzędzie <img alt="" src=images/Draft_Text.svg  style="width:24px;"> **Adnotacja wieloliniowa** wstawia wielowierszowe pole tekstowe w wybranym miejscu.

Aby wstawić element tekstowy ze strzałką, użyj przycisku [Rysunek roboczy: Etykieta](Draft_Label/pl.md) zamiast tego polecenia.

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Pojedynczy punkt wymagany przy ustawianiu tekstu*

## Użycie

Zobacz również: [Rysunek roboczy: Tacka narzędziowa](Draft_Tray/pl.md) oraz [Rysunek roboczy: Przyciąganie](Draft_Snap/pl.md).

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Text.svg" width=16px> [Adnotacja wieloliniowa](Draft_Text/pl.md)**,
    -   Wybierz opcję z menu **Adnotacje → <img src="images/Draft_Text.svg" width=16px> Tekst**,
    -   Użyj skrótu klawiaturowego: **T** a następnie **E**.
2.  Otwiera się panel zadań **Tekst**. Zobacz sekcję [Opcje](#Opcje.md), aby uzyskać więcej informacji.
3.  Kliknij punkt w oknie [widoku 3D](3D_view/pl.md), lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Dodaj punkt**.
4.  Wprowadź żądany tekst, naciskając **Enter** między każdą linijką.
5.  Naciśnij **Enter** dwukrotnie, lub naciśnij przycisk **<img src="images/Button_valid.svg" width=16px>. Utwórz tekst** aby zakończyć operację.

## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne, po prostu wprowadź liczby, a następnie naciśnij klawisz **Enter** pomiędzy każdą składową X, Y i Z. Możesz wcisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> dodaj punkt**, gdy już wprowadzisz żądane wartości. Zaleca się wysunięcie kursora poza okno [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne są względne w stosunku do globalnego układu współrzędnych, w przeciwnym razie są względne w stosunku do układu współrzędnych [płaszczyznay roboczej](Draft_SelectPlane/pl.md). {{Version/pl|0.20}}
-   Naciśnij klawisz **T** lub zaznacz pole wyboru **Kontynuuj** aby przełączyć tryb kontynuacji. Jeśli tryb kontynuacji jest włączony, polecenie zostanie uruchomione ponownie po zakończeniu pracy, umożliwiając kontynuowanie tworzenia tekstów. Skrót ten nie działa w drugim panelu zadań. Opcja ta nie jest dostępna w pierwszym panelu zadań w programie FreeCAD w wersji 0.19 i wcześniejszych.
-   Naciśnij **S**, aby włączyć lub wyłączyć [przyciąganie](Draft_Snap/pl.md).
-   Naciśnij klawisz **Esc** lub przycisk **Zamknij**, aby przerwać bieżące polecenie.

## Uwagi

-   Tekst może być edytowany poprzez dwukrotne kliknięcie na nim w [Widoku drzewa](Tree_view.md). <small>(v0.20)</small> 
-   Teksty utworzone za pomocą funkcji [z wydania 0.18](Release_notes_0.18/pl.md) nie są wstecznie kompatybilne.

## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Adnotacja wieloliniowa wywodzi się z obiektu [App: FeaturePython](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Poniższe właściwości są dodatkowe, chyba że zaznaczono inaczej.

### Dane


{{TitleProperty|Podstawowe}}

-    **Umieszczenie|Placement**: określa położenie tekstu w oknie [widoku 3D](3D_view/pl.md). Zobacz [Umiejscowienie](Placement/pl.md).

-    **Tekst|StringList**: określa zawartość tekstu. Każda pozycja na liście reprezentuje nowy wiersz tekstu.

### Widok


{{TitleProperty|Adnotacja}}

-    **Styl adnotacji|Enumeration**: określa styl adnotacji zastosowany do tekstu. Zobacz stronę [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md).

-    **Mnożnik skali|Float**: określa ogólny współczynnik skalowania zastosowany do tekstu.


{{TitleProperty|Opcje wyświetlania}}

-    **Tryb wyświetlania|Enumeration**: określa sposób wyświetlania tekstu. Jeśli wartością jest {{value|tekst 3D}}, tekst będzie wyświetlany w płaszczyźnie zdefiniowanej przez jego **Uniejscowienie**. Jeśli jest to {{value|tekst 2D}}, tekst będzie zawsze skierowany w stronę patrzącego. Jest to właściwość dziedziczona.


{{TitleProperty|Grafika}}

-    **Kolor linii|Color**: nie wykorzystano.

-    **Szerokość linii|Float**: nie wykorzystano.


{{TitleProperty|Tekst}}

-    **Nazwa czcionki**: określa czcionkę, której należy używać do rysowania tekstu. Może to być nazwa czcionki, np. {{value|Arial}}, styl domyślny, np. {{value|sans}}, {{value|serif}} lub {{value|mono}}, rodzina {{value|Arial, Helvetica, sans}} lub nazwa w stylu {{value|Arial:Bold}}. Jeśli dana czcionka nie znajduje się w systemie, stosuje się zamiast niej czcionkę standardową.

-    **Wielkość czcionki**: określa rozmiar liter. Jeżeli obiekt tekstowy jest tworzony w widoku drzewa, lecz nie jest widoczny żaden tekst, to należy zwiększyć rozmiar tekstu, aż będzie on widoczny.

-    **Wyrównanie**: określa, czy tekst wyrównuje się do lewej, prawej czy do środka punktu bazowego.

-    **Rozstaw linii**: określa odstęp między liniami tekstu.

-    **Kolor tekstu|Color**: definiuje barwę tekstu.

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Adnotacja wieloliniowa** używa metody `make_text` *(<small>(v0.19)</small> )* środowiska Rysunek roboczy. Ta metoda zastępuje przestarzałą metodę `makeText`.


```python
text = make_text(string, placement=None, screen=False)
```

-   Tworzy obiekt `text`, w miejscu `placement`, który może być `FreeCAD.Placement`, ale także zdefiniowanym przez `FreeCAD.Rotation` lub `FreeCAD.Vector`.

-    `string`to łańcuch, lub lista łańcuchów. Jeżeli jest to lista, to każdy element jest wyświetlany w swoim wierszu.

-   Jeżeli wartość `screen` ma wartość `True`, to tekst jest zawsze zwrócony w kierunku obserwacji z kamery, w przeciwnym razie jest wyświetlana w płaszczyźnie zdefiniowanej przez jej {{PropertyData/pl|Umiejscowienie}}.

Właściwości widoku `text` można zmienić poprzez nadpisanie jego właściwości, np. nadpisać `ViewObject.FontSize` wartością nowego rozmiaru w milimetrach.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

t1 = "This is a sample text"
p1 = App.Vector(0, 0, 0)

t2 = ["First line", "second line"]
p2 = App.Vector(1000, 1000, 0)

text1 = Draft.make_text(t1, p1)
text2 = Draft.make_text(t2, p2)
text1.ViewObject.FontSize = 200
text2.ViewObject.FontSize = 200

zaxis = App.Vector(0, 0, 1)

t3 = ["Upside", "down"]
p3 = App.Vector(-1000, -500, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 180))
text3 = Draft.make_text(t3, place3)
text3.ViewObject.FontSize = 200

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text/pl
