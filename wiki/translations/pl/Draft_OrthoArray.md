---
 GuiCommand:
   Name: Draft OrthoArray
   Name/pl: Rysunek Roboczy: Szyk ortogonalny
   MenuLocation: Modyfikacja , Narzędzia szyku , Szyk ortogonalny
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Version: 0.19
   SeeAlso: Draft_PolarArray/pl, Draft_CircularArray/pl, Draft_PathArray/pl, Draft_PathLinkArray/pl, Draft_PointArray/pl, Draft_PointLinkArray/pl
---

# Draft OrthoArray/pl



## Opis

Polecenie <img alt="" src=images/Draft_OrthoArray.svg  style="width:24px;"> **Szyk ortogonalny** tworzy prostokątny *(3-osiowy)* szyk z wybranego obiektu. Polecenie może opcjonalnie utworzyć szyk [Łączy](App_Link/pl.md), który jest bardziej wydajny niż zwykły szyk.

Narzędzie Przesuń może być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może być również używane dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md).

<img alt="" src=images/Draft_Array_example.png  style="width:300px;"> 
*Szyk ortogonalny.*



## Użycie

1.  Opcjonalnie wybierz jeden obiekt.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_OrthoArray.svg" width=16px> '''Szyk ortogonalny'''**.
    -   Wybierz z menu opcję **Modyfikacja → Narzędzia szyku → <img src="images/Draft_OrthoArray.svg" width=16px> Szyk ortogonalny**.
3.  Otworzy się panel zadań **Szyk prostokątny**. Więcej informacji znajduje się w sekcji [Opcje](#Opcje.md).
4.  Jeśli nie wybrano jeszcze żadnego obiektu: wybierz jeden obiekt.
5.  Wprowadź wymagane parametry w panelu zadań.
6.  Aby zakończyć polecenie, wykonaj jedną z następujących czynności:
    -   Kliknij w oknie [widoku 3D](3D_view/pl.md).
    -   Naciśnij **Enter**.
    -   Naciśnij przycisk **OK**.



## Opcje

-   Wprowadź **Liczbe elementów** dla kierunków X, Y i Z. Liczba ta musi wynosić co najmniej {{Value|1}} dla każdego kierunku.
-   Wprowadź **odstęp X**, aby określić przemieszczenie elementów w kierunku X. W przypadku tablicy prostokątnej wartości Y i Z muszą być równe {{Value|0}}.
-   Wprowadź **odstęp Y**, aby określić przemieszczenie elementów w kierunku Y. W przypadku tablicy prostokątnej wartości X i Z muszą mieć wartość {{Value|0}}.
-   Wprowadź **odstęp Z**, aby określić przemieszczenie elementów w kierunku Z. W przypadku tablicy prostokątnej wartości X i Y muszą mieć wartość {{Value|0}}.
-   Naciśnij przycisk **Reset X, Y or Z**, aby zresetować przemieszczenie w danym kierunku do wartości domyślnych.
-   Jeśli pole wyboru **Scal** jest zaznaczone, nakładające się elementy w tablicy są łączone. Nie działa to w przypadku szyków łączy.
-   Jeśli pole wyboru **Szyk łączy** jest zaznaczone, tworzony jest szyk Łączy zamiast zwykłego szyku. Szyk łączy jest bardziej wydajny, ponieważ jego elementami są obiekty [App: Łącze](App_Link/pl.md).
-   Naciśnij **Esc** lub przycisk **Anuluj**, aby przerwać polecenie.



## Uwagi

-   Szyk ortogonalny może zostać przekształcony w [Szyk biegunowy](Draft_PolarArray/pl.md) lub [Szyk kołowy](Draft_CircularArray/pl.md) poprzez zmianę jego właściwości **Typ szyku**.
-   Szyk łączy nie może zostać przekształcony w zwykły szyk lub odwrotnie. Typ szyku musi być określony w czasie tworzenia.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Polecenia Szyk ortogonalny, [Szyk biegunowy](Draft_PolarArray/pl.md) i [Szyk kołowy](Draft_CircularArray/pl.md) tworzą ten sam obiekt. Obiekt ten jest pochodną obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości *(z wyjątkiem niektórych właściwości widoku, które nie są dziedziczone przez szyki łączy)*. Poniższe właściwości są dodatkowe, chyba że zaznaczono inaczej:



### Dane


{{TitleProperty|Łącze}}

Właściwości w tej grupie są dostępne tylko dla szyków łączy. Więcej informacji można znaleźć na stronie [Std: Utwórz łącze](Std_LinkMake/pl#Właściwości.md).

-    **Skala|Float**
    

-    **Wektor skali|Vector|Ukryte**.

-    **Lista skali|VectorList**
    

-    **Lista widoczności|BoolList|Ukryte**
    

-    **Lista umiejscowienia|PlacementList|Ukryte**
    

-    **Lista elementów|LinkList|Ukryte**
    

-    **_ Link Touched|Bool|Ukryte**
    

-    **_ Child Cache|LinkList|Ukryte**
    

-    **Elementy kolorowe|LinkSubHidden|Ukryte**
    

-    **Przekształcenie łącza|Bool**
    


{{TitleProperty|Szyk kołowy}}

Właściwości w tej grupie są ukryte dla tablic ortogonalnych i biegunowych.

-    **Liczba okręgów|Integer**: określa liczbę okrągłych warstw. Musi wynosić co najmniej {{Value|2}}.

-    **Odległość promieniowa|Odległość**: określa odległość między okrągłymi warstwami.

-    **Symetria|Integer**: określa liczbę linii symetrii. Liczba ta zmienia rozmieszczenie elementów w tablicy.

-    **Odległość styczna|Distance**: określa odległość między elementami w tej samej warstwie kołowej. Musi być większa od zera.


{{TitleProperty|Obiekty}}

-    **Typ szyku|Enumeration**: określa typ szyku, który może być {{value|ortho}}, {{value|polar}} lub {{value|circular}}.

-    **Oś odniesienia|LinkGlobal**: określa obiekt i krawędź, które mają być używane zamiast właściwości **Axis** i **Center**. Nie używane dla tablic ortogonalnych.

-    **Baza|Link**: określa obiekt do powielenia w tablicy.

-    **Ilość|Integer**: *(tylko do odczytu)* określa całkowitą liczbę elementów w tablicy. {{VersionMinus/pl|0.20}}: Dostępne tylko dla szyku Łączy.

-    **Rozwiń szyk|Bool**: określa, czy rozwinąć szyk w oknie [Widoku drzewa](Tree_view/pl.md), aby umożliwić wybór jego poszczególnych elementów. Dostępne tylko dla szyków typu Link.

-    **Połącz|Bool**: określa, czy nakładające się elementy w tablicy mają być łączone, czy nie. Nie używane dla szyków typu Łącze.


{{TitleProperty|Szyk ortogonalny}}

Właściwości w tej grupie są ukryte dla tablic kołowych i biegunowych.

-    **Odstęp X|VectorDistance**: określa odstęp między elementami w kierunku X.

-    **Odstęp Y|VectorDistance**: określa odstęp między elementami w kierunku Y.

-    **Odstęp Z|VectorDistance**: określa odstęp między elementami w kierunku Z.

-    **Ilość X|Integer**: określa liczbę elementów w kierunku X. Musi wynosić co najmniej {{Value|1}}.

-    **Ilość Y|Integer**: określa liczbę elementów w kierunku Y. Musi mieć wartość co najmniej {{Value|1}}.

-    **Ilość Z|Integer**: określa liczbę elementów w kierunku Z. Musi mieć wartość co najmniej {{Value|1}}.


{{TitleProperty|Szyk biegunowy}}

Właściwości w tej grupie są ukryte dla szyków kołowych i szyków ortogonalnych.

-    **Kąt|Angle**: określa aperturę łuku kołowego. Użyj {{value|360&#176;}} dla pełnego okręgu.

-    **Odstęp osi|VectorDistance**: określa odstęp między elementami w kierunku **Axis**.

-    **Ilość Polar|Integer**: określa liczbę elementów w kierunku biegunowym.


{{TitleProperty|Układ biegunowy / kołowy}}

Właściwości w tej grupie są ukryte dla szyków ortogonalnych.

-    **Oś|Vector**: określa kierunek osi tablicy.

-    **Środek|VectorDistance**: określa punkt środkowy tablicy. Oś tablicy przechodzi przez ten punkt. W przypadku tablic kołowych jest to przesunięcie od **Umiejscowienia** obiektu **Baza**.



### Widok


{{TitleProperty|Łącze}}

Właściwości w tej grupie, z wyjątkiem właściwości dziedziczonej, są dostępne tylko dla szyków łączy. Więcej informacji można znaleźć na stronie [Std: Utwórz łącze](Std_LinkMake/pl#Właściwości.md).

-    **Styl kreślenia|Enumeration**
    

-    **Szerokość linii|FloatConstraint**
    

-    **Nadpisanie materiału|Bool**
    

-    **Rozmiar punktu|FloatConstraint**
    

-    **Wybieralny|Bool**: jest to właściwość dziedziczona, która pojawia się w grupie \"Wybór\" dla innych szyków.

-    **Kształt materiału|Material**.


{{TitleProperty|Podstawa}}

Właściwości w tej grupie, z wyjątkiem właściwości dziedziczonej, są dostępne tylko dla szyków łączy. Więcej informacji można znaleźć na stronie [Std: Utwórz łącze](Std_LinkMake/pl#Właściwości.md).

-    **Dostawca widoku elementu podrzędnego|PersistentObject|Ukryte**.

-    **Lista materiałów|MaterialList|Ukryte**
    

-    **Zastąp listę kolorów|ColorList|Ukryte**
    

-    **Zastąp listę materiałów|BoolList|Ukryte**
    

-    **Proxy|PythonObject|Ukryte**: jest to właściwość dziedziczona.


{{TitleProperty|Opcje wyświetlania}}

Właściwości w tej grupie są dziedziczone. Więcej informacji można znaleźć na stronie [Część: Cecha](Part_Feature/pl#Własności.md).

-    **Ramka otaczająca|Bool**: ta właściwość nie jest dziedziczona przez szyk łączy.

-    **Tryb wyświetlania|Enumeration**: dla szyku Łączy może to być {{value|Link}} lub {{value|ChildView}}. Dla innych szyków może to być: {{value|Cieniowany z krawędziami}}, {{value|Cieniowany}}, {{value|Szkieletowy}} lub {{value|Punkty}}.

-    **Pokaż w drzewie|Bool**
    

-    **Widoczność|Bool**
    


{{TitleProperty|Rysunek Roboczy}}

-    **Wzór|Enumeration**: niewykorzystane.

-    **Rozmiar wzoru|Float**: niewykorzystane.


{{TitleProperty|Styl obiektu}}

Właściwości w tej grupie nie są dziedziczone przez szyk łączy.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).



### Szyk parametryczny 

Aby utworzyć parametryczną tablicę ortogonalną, należy użyć metody `make_array` *({{Version/pl|0.19}})* modułu Rysunek Roboczy. Metoda ta zastępuje przestarzałą metodę `makeArray`. Metoda `make_array` może tworzyć obiekty OrthoArrays środowiska Rysunek Roboczy, [Szyk biegunowy](Draft_PolarArray/pl.md) i [Szyk kołowy](Draft_CircularArray/pl.md). Dla każdego typu szyku dostępny jest jeden lub więcej elementów opakowujących.

Metoda podstawowa:


```python
array = make_array(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)
```

Opakowaniem dla szyków ortogonalnych są:


```python
array = make_ortho_array(base_object,
                         v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0), v_z=App.Vector(0, 0, 10),
                         n_x=2, n_y=2, n_z=1,
                         use_link=True)
```


```python
array = make_ortho_array2d(base_object,
                           v_x=App.Vector(10, 0, 0), v_y=App.Vector(0, 10, 0),
                           n_x=2, n_y=2,
                           use_link=True)
```

Opakowaniem dla szyków prostokątnych są:


```python
array = make_rect_array(base_object,
                        d_x=10, d_y=10, d_z=10,
                        n_x=2, n_y=2, n_z=1,
                        use_link=True)
```


```python
array = make_rect_array2d(base_object,
                          d_x=10, d_y=10,
                          n_x=2, n_y=2,
                          use_link=True)
```

-    `base_object`jest obiektem, który ma być tablicowany. Może to być również `Etykieta` *(ciąg znaków)* obiektu w bieżącym dokumencie.

-    `v_x`, `v_y` i `v_z` są wektorami pomiędzy punktami bazowymi elementów w odpowiednich kierunkach.

-    `d_x`, `d_y` i `d_z` to odległości między punktami bazowymi elementów w odpowiednich kierunkach.

-    `n_x`, `n_y` i `n_z` są liczbami elementów w odpowiednich kierunkach.

-   Jeśli `use_link` ma wartość {{True/pl}}, utworzone elementy są [łącza](App_Link/pl.md) zamiast zwykłych kopii.

-    `szyk`jest zwracany wraz z utworzonym obiektem szyku.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

array = Draft.make_ortho_array2d(rect, v_x, v_y, 3, 4)
doc.recompute()
```



### Szyk nieparametryczny 

Aby utworzyć nieparametryczny szyk ortogonalny, należy użyć metody `array` modułu Rysunek Roboczy. Metoda ta zwraca `Brak`.


```python
array(objectslist, xvector, yvector, xnum, ynum)
array(objectslist, xvector, yvector, zvector, xnum, ynum, znum)
```

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rect = Draft.make_rectangle(1500, 500)
v_x = App.Vector(1600, 0, 0)
v_y = App.Vector(0, 600, 0)

Draft.array(rect, v_x, v_y, 3, 4)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft OrthoArray/pl
