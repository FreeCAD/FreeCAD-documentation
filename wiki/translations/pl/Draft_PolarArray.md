---
 GuiCommand:
   Name: Draft PolarArray
   Name/pl: Rysunek Roboczy: Szyk biegunowy
   MenuLocation: Modyfikacja , Narzędzia szyku , Szyk biegunowy
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Version: 0.19
   SeeAlso: Draft_OrthoArray/pl, Draft_CircularArray/pl, Draft_PathArray/pl, Draft_PathLinkArray/pl, Draft_PointArray/pl, Draft_PointLinkArray/pl
---

# Draft PolarArray/pl



## Opis

Polecenie <img alt="" src=images/Draft_PolarArray.svg  style="width:24px;"> **Szyk biegunowy** tworzy szyk z wybranego obiektu poprzez umieszczenie kopii wzdłuż obwodu. Polecenie może opcjonalnie utworzyć szyk [łączy](App_Link/pl.md), który jest bardziej wydajny niż zwykły szyk.

Narzędzie Przesuń może być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może być również używane dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md).

<img alt="" src=images/Draft_PolarArray_example.png  style="width:400px;"> 
*Szyk biegunowy.*



## Użycie

Zapoznaj się również z informacjami na stronie [Przyciąganie](Draft_Snap/pl.md).

1.  Opcjonalnie wybierz jeden obiekt.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_PolarArray.svg" width=16px> '''Szyk biegunowy'''**.
    -   Wybierz z menu opcję **Modyfikacja → Narzędzia szyku → <img src="images/Draft_PolarArray.svg" width=16px> Szyk biegunowy**.
3.  Otworzy się panel zadań **Szyk biegunowy**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
4.  Jeśli nie wybrano jeszcze żadnego obiektu: wybierz jeden obiekt.
5.  Wprowadź wymagane parametry w panelu zadań.
6.  Aby zakończyć polecenie, wykonaj jedną z poniższych czynności:
    -   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md) dla **Środek obrotu**.
    -   Naciśnij **Enter**.
    -   Naciśnij przycisk **OK**.



## Opcje

-   Wprowadź **Kąt zakresu szyku**, aby określić całkowity kąt szyku. Kąt jest dodatni w kierunku przeciwnym do ruchu wskazówek zegara.
-   Wprowadź **Liczba elementów**. Musi ona wynosić co najmniej {{Value|2}}. Maksymalna wartość, jaką można wprowadzić w panelu zadań to {{Value|99}}, ale wyższe wartości są możliwe poprzez zmianę właściwości **Ilość elementów polarnych** szyku.
-   Wybierz punkt w oknie [widoku 3D](3D_view/pl.md), zauważ, że to również zakończy polecenie, lub wpisz współrzędne dla **Środka obrotu**. Oś obrotu tablicy będzie przechodzić przez ten punkt. Zaleca się przesunięcie wskaźnika poza obszar okna [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Naciśnij przycisk **Zresetuj współrzędne punktu**, aby zresetować **Środek obrotu** do punktu początkowego.
-   Jeśli pole wyboru **Scal** jest zaznaczone, nakładające się elementy w szyku są scalane. Nie działa to w przypadku szyków łączy.
-   Jeśli pole wyboru **Szyk łączy** jest zaznaczone, tworzony jest szyk łączy zamiast zwykłego szyku. Szyk łączy jest bardziej wydajny, ponieważ jego elementami są obiekty [App Łącze](App_Link/pl.md).
-   Naciśnij **Esc** lub przycisk **Anuluj**, aby przerwać polecenie.



## Uwagi

-   Domyślną osią obrotu dla szyku jest dodatnia oś Z. Można to zmienić edytując właściwość **Oś**.
-   Szyk biegunowy może zostać przekształcony w [Szyk ortogonalny](Draft_OrthoArray/pl.md) lub [Szyk kołowy](Draft_CircularArray/pl.md) poprzez zmianę jego właściwości **Typ szyku**.
-   Szyk łączy nie może zostać przekształcony w zwykły szyk lub odwrotnie. Typ szyku musi być określony w czasie tworzenia.



## Właściwości

Zapoznaj się z informacjami zawartymi na stronie [Szyk ortogonalny](Draft_OrthoArray/pl#Właściwości.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).



### Szyk parametryczny 

Aby utworzyć parametryczny szyk biegunowy, należy użyć metody `make_array` *({{Version/pl|0.19}})* modułu Rysunek Roboczy. Metoda ta zastępuje przestarzałą metodę `makeArray`. Metoda `make_array` może tworzyć obiekty OrthoArrays środowiska Rysunek Roboczy, [Szyk ortogonalny](Draft_OrthoArray/pl.md) i [Szyk kołowy](Draft_CircularArray/pl.md). Dla każdego typu szyku dostępny jest jeden lub więcej elementów opakowujących.

Metoda podstawowa:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Opakowaniem dla tablic biegunowych jest:


```python
array = make_polar_array(base_object,
                         number=5, angle=360, center=App.Vector(0, 0, 0),
                         use_link=True)
```

-    `obiekt_bazowy`jest obiektem, który ma zostać użyty w szyku. Może to być również `Etykieta` *(ciąg znaków)* obiektu w bieżącym dokumencie.

-    `Ilość`jest liczbą elementów we wzorcu, włączając w to oryginalny obiekt.

-    `Kąt`to kąt łuku biegunowego w stopniach.

-    `Środek`jest wektorem definiującym środek wzorca.

-   Jeśli `use_link` ma wartość {{True/pl}}, utworzone elementy są [App: Łącze](App_Link/pl.md) zamiast zwykłych kopii.

-    `szyk`jest zwracany wraz z utworzonym obiektem szyku.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)
center = App.Vector(-1600, 0, 0)

array = Draft.make_polar_array(tri, 8, 270, center)
doc.recompute()
```



### Szyk nieparametryczny 

Aby utworzyć nieparametryczny szyk biegunowy, należy użyć metody `array` modułu Rysunek Roboczy. Metoda ta zwraca `Brak`.


```python
array(objectslist, center, angle, number)
```

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

tri = Draft.make_polygon(3, 600)
center = App.Vector(-1600, 0, 0)

Draft.array(tri, center, 270, 8)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PolarArray/pl
