---
 GuiCommand:
   Name: Draft PointArray
   Name/pl: Rysunek Roboczy: Szyk z punktów
   MenuLocation: Modyfikacja , Narzędzia szyku , Szyk z punktów<br>Modyfikacja , Szyk z punktów
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Version: 0.18
   SeeAlso: Draft_OrthoArray/pl, Draft_PolarArray/pl, Draft_CircularArray/pl, Draft_PathArray/pl, Draft_PointArray/pl, Draft_PointLinkArray/pl
---

# Draft PointArray/pl



## Opis

Polecenie <img alt="" src=images/Draft_PointArray.svg  style="width:24px;"> **Szyk z punktów** tworzy regularną tablicę z wybranego obiektu bazowego poprzez umieszczenie kopii w punktach obiektu punktowego. Użyj polecenia [Szyk powiązań w punktach](Draft_PointLinkArray/pl.md), aby utworzyć bardziej wydajną tablicę [Łączy](App_Link/pl.md). Z wyjątkiem typu tworzonego szyku, szyku łączy lub zwykłego szyku, polecenie [Szyk powiązań w punktach](Draft_PointLinkArray/pl.md) działa identycznie jak to polecenie.

Narzędzie Szyk z punktów może być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może być również używane dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [BIM](BIM_Workbench/pl.md).

Obiektem punktowym może być dowolny obiekt z kształtem i wierzchołkami *(w tym [Std: Część](Std_Part/pl.md) zawierający jeden lub więcej takich obiektów)*, a także [siatka](Mesh_Workbench/pl.md) i [chmura punktów](Points_Workbench/pl.md). Zduplikowane punkty w obiekcie punktowym są odfiltrowywane.

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;"> 
*Szyk z punktów.*



## Użycie

1.  Wybierz obiekt, który chcesz wyświetlić.
2.  Dodaj obiekt punktów do zaznaczenia.
3.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_PointArray.svg" width=16px> '''Szyk z punktów'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz opcję z menu **Modyfikacja → Narzędzia szyku → <img src="images/Draft_PointArray.svg" width=16px> Szyk z punktów**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Modyfikacja → <img src="images/Draft_PointArray.svg" width=16px> Szyk z punktów** z menu.
4.  Tablica zostanie utworzona.
5.  Opcjonalnie można zmienić [właściwości](#właściwości.md) tablicy w [edytorze właściwości](Property_editor/pl.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Szyk z punktów, środowiska Rysunek Roboczy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości *(z wyjątkiem niektórych właściwości Widoku, które nie są dziedziczone przez szyki Łączy)*. Poniższe właściwości są dodatkowe, chyba że zaznaczono inaczej:



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
    


{{TitleProperty|Obiekty}}

-    **Baza|Link**: określa obiekt do powielenia w szyku.

-    **Ilość|Integer**: *(tylko do odczytu)* określa liczbę elementów w szyku. Liczba ta jest określana przez liczbę punktów we właściwości **Obiekt punktowy**.

-    **Rozszerz szyk|Bool**: określa, czy tablica ma zostać rozszerzona w [Widok drzewa](Tree_view/pl.md), aby umożliwić wybór jej poszczególnych elementów. Dostępne tylko dla szyków łączy.

-    **Dodatkowe umiejscowienie|Placement**: : określa dodatkowe [Umiejscowienie](Placement/pl.md), przesunięcie i obrót dla każdego elementu w szyku.

-    **Połącz|Bool**: określa, czy nakładające się elementy w tablicy są łączone, czy nie. Nie używane dla tablic Łączy. {{Version/pl|1.0}}.

-    **Obiekt punktowy|Link**: określa obiekt, którego punkty są używane do pozycjonowania elementów w tablicy.



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

Aby utworzyć Szyk z punktów, należy użyć metody `make_point_array` ({{Version/pl|0.19}}) modułu Rysunek Roboczy. Metoda ta zastępuje przestarzałą metodę `makePointArray`.


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```

-    `base_object`jest obiektem, który ma być użyty w szyku. Może to być również `Etykieta` *(ciąg znaków)* obiektu w bieżącym dokumencie.

-    `point_object`jest obiektem zawierającym punkty. Może to być również `Etykieta` *(ciąg znaków)* obiektu w bieżącym dokumencie. Powinien mieć właściwość `Geomrtria`, `Łącze` lub `Komponenty` zawierające punkty.

-    `extra`to `App.Placement`, `App.Vector` lub `App.Rotation`, które przesuwają każdy element.

-   Jeśli właściwość `use_link` ma wartość {{True/pl}}, utworzone elementy są obiektami [App: Łącze](App_Link/pl.md) zamiast zwykłymi kopiami.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/pl
