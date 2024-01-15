---
 GuiCommand:
   Name: Draft CircularArray
   Name/pl: Rysunek Roboczy: kołowy
   MenuLocation: Modyfikacja , Narzędzia szyku , Szyk kołowy
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Version: 0.19
   SeeAlso: Draft_OrthoArray/pl, Draft_PolarArray/pl, Draft_PathArray/pl, Draft_PathLinkArray/pl, Draft_PointArray/pl, Draft_PointLinkArray/pl
---

# Draft CircularArray/pl



## Opis

Polecenie <img alt="" src=images/Draft_CircularArray.svg  style="width:24px;"> **Szyk kołowy** tworzy tablicę z wybranego obiektu poprzez umieszczenie kopii wzdłuż współśrodkowych okręgów. Polecenie może opcjonalnie utworzyć szyk [łączy](App_Link.md), który jest bardziej wydajny niż zwykły szyk.

Narzędzie Przesuń może być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może być również używane dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md).

<img alt="" src=images/Draft_CircularArray_example.png  style="width:400px;"> 
*Szyk kołowy*



## Użycie

Zapoznaj się również z informacjami na stronie [Przyciąganie](Draft_Snap/pl.md).

1.  Opcjonalnie wybierz jeden obiekt.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_CircularArray.svg" width=16px> '''Szyk kołowy'''**.
    -   Wybierz opcję z manu **Modyfikacja → Narzędzia szyku → <img src="images/Draft_CircularArray.svg" width=16px> Szyk kołowy**.
3.  Otworzy się panel zadań **Szyk kołowy**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
4.  Jeśli nie wybrano jeszcze żadnego obiektu: wybierz jeden obiekt.
5.  Wprowadź wymagane parametry w panelu zadań.
6.  Aby zakończyć polecenie, wykonaj jedną z następujących czynności:
    -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md) dla **Środek obrotu**.
    -   Naciśnij **Enter**.
    -   Naciśnij przycisk **OK**.



## Opcje

-   Wprowadź **Odległość promieniowa**, aby określić odległość między okrągłymi warstwami oraz między środkiem a pierwszą okrągłą warstwą.
-   Wprowadź **Odległość styczna**, aby określić odległość między elementami na tej samej warstwie kołowej. Musi być ona większa od zera.
-   Wprowadź **Liczba warstw kołowych**. Element w środku liczy się jako jedna warstwa. Liczba ta musi wynosić co najmniej {{Value|2}}. Maksymalna wartość, jaką można wprowadzić w panelu zadań to {{Value|99}}, ale wyższe wartości są możliwe poprzez zmianę właściwości **Liczba okręgów** szyku.
-   Wprowadź wartość **Odbicie lustrzane**. Liczba ta określa sposób rozmieszczenia elementów. Wartość {{Value|3}}, na przykład, skutkuje wzorem z trzema równymi segmentami kołowymi 120°. Większe wartości **Odbicia lustrzanego** i **Odległość styczna** skutkują mniejszą liczbą lub nawet brakiem elementów na wewnętrznych warstwach.
-   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md), zauważ, że zakończy to również polecenie, lub wpisz współrzędne dla **Środka obrotu**. Oś obrotu tablicy będzie przechodzić przez ten punkt. Zaleca się przesunięcie wskaźnika poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Naciśnij przycisk **Zresetuj współrzędne punktu**, aby zresetować **Środek obrotu** do punktu odniesienia położenia.
-   Jeśli pole wyboru **Scal** jest zaznaczone, nakładające się elementy w tablicy są łączone. Nie działa to w przypadku szyków łączy.
-   Jeśli pole wyboru **Szyk łączy** jest zaznaczone, tworzony jest szyk łączy zamiast zwykłego szyku. Szyk łączy jest bardziej wydajny, ponieważ jego elementami są obiekty [App: Łącze](App_Link/pl.md).
-   Naciśnij **Esc** lub przycisk **Cancel**, aby przerwać wykonywanie polecenia.



## Uwagi

-   Domyślną osią obrotu dla szyku jest dodatnia oś Z. Można to zmienić edytując właściwość **Oś**.
-   Szyk kołowy może zostać przekształcony w [Szyk ortogonalny](Draft_OrthoArray/pl.md) lub [Szyk biegunowy](Draft_PolarArray/pl.md) poprzez zmianę jego właściwości **Typ szyku**.
-   Szyk łączy nie może zostać przekształcony w zwykły szyk lub odwrotnie. Typ szyku musi być określony w czasie tworzenia.



## Właściwości

Zapoznaj się z informacjami zawartymi na stronie [Szyk ortogonalny](Draft_OrthoArray/pl#Właściwości.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć parametryczny szyk kołowy, należy użyć metody `make_array` *({{Version/pl|0.19}})* modułu Rysunek Roboczy. Metoda ta zastępuje przestarzałą metodę `makeArray`. Metoda `make_array` może tworzyć obiekty [Szyk ortogonalny](Draft_OrthoArray/pl.md), [Szyk biegunowy](Draft_PolarArray/pl.md) i Szyk kołowy środowiska Rysunek Roboczy. Dla każdego typu szyku dostępny jest jeden lub więcej elementów opakowujących.

Metoda podstawowa:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Opakowaniem dla szyków kołowych jest:


```python
array = make_circular_array(base_object,
                            r_distance=100, tan_distance=50,
                            number=3, symmetry=1,
                            axis=App.Vector(0, 0, 1), center=App.Vector(0, 0, 0),
                            use_link=True)
```

-    `base_object`jest obiektem, który ma zostać użyty w szyku. Może to być również `Etykieta` (ciąg znaków) obiektu w bieżącym dokumencie.

-    `r_distance`i `tan_distance` są odległościami radialnymi i stycznymi między elementami.

-    `Liczba`to liczba okrągłych warstw we wzorze, oryginalny obiekt liczy się jako pierwsza warstwa.

-    `symetria`to liczba całkowita używana w niektórych obliczeniach, które wpływają na sposób rozmieszczenia elementów na obwodzie. Zwykle przyjmuje się wartości od 1 do 6. Wyższe wartości nie są zalecane i spowodują zniknięcie elementów w wewnętrznych warstwach.

-    `Oś`i `Środek` to wektory opisujące kierunek osi obrotu i punkt, przez który ta oś przechodzi.

-   Jeśli `use_link` ma wartość {{True/pl}}, utworzone elementy są [App: Łącze](App_Link/pl.md) zamiast zwykłych kopii.

-    `szyk`jest zwracany wraz z utworzonym obiektem szyku.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)

array = Draft.make_circular_array(tri, 1800, 1200, 4, 1)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CircularArray/pl
