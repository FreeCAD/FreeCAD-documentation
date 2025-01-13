---
 GuiCommand:
   Name: Draft PathArray
   Name/pl: Rysunek Roboczy: Szyk po ścieżce
   MenuLocation: Modyfikacja , Narzędzia szyku , Szyk po ścieżce<br>Modyfikacja , Szyk po ścieżce
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Version: 0.14
   SeeAlso: Draft_OrthoArray/pl, Draft_PolarArray/pl, Draft_CircularArray/pl, Draft_PathLinkArray/pl, Draft_PointArray/pl, Draft_PointLinkArray/pl
---

# Draft PathArray/pl



## Opis

Polecenie <img alt="" src=images/Draft_PathArray.svg  style="width:24px;"> **Szyk po ścieżce** tworzy zwykły szyk z wybranego obiektu przez umieszczenie kopii wzdłuż ścieżki. Zamiast tego użyj polecenia [Szyk powiązań po ścieżce](Draft_PathLinkArray/pl.md), aby utworzyć bardziej wydajny szyk [powiązań](App_Link.md). Z wyjątkiem typu utworzonych szyków *(szyk powiązań lub zwykły szyk)*, polecenie [Szyk powiązań po ścieżce](Draft_PathLinkArray/pl.md) jest identyczne z tym poleceniem.

Oba polecenia mogą być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale można ich również użyć dla wielu typów obiektów 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [BIM](BIM_Workbench/pl.md).

<img alt="" src=images/Draft_PathArray_Example.png  style="width:400px;"> 
*Szyk po ścieżce*



## Użycie

1.  Wybierz obiekt, który chcesz wyświetlić.
2.  Dodaj obiekt ścieżki do zaznaczenia. Zamiast tego można również wybrać krawędzie. Krawędzie muszą należeć do tego samego obiektu i muszą być połączone.
3.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_PathArray.svg" width=16px> '''Szyk po ścieżce'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz opcję z menu **Modyfikacja → Narzędzia szyku → <img src="images/Draft_PathArray.svg" width=16px> Szyk po ścieżce**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Modyfikacja → <img src="images/Draft_PathArray.svg" width=16px> Szyk po ścieżce** z menu.
4.  Szyk zostanie utworzony.
5.  Opcjonalnie można zmienić [właściwości](#Właściwości.md) szyku w [edytorze właściwości](Property_editor/pl.md).



## Wyrównanie

Wyrównanie elementów w Szyk po ścieżce zależy od właściwości szyku i orientacji obiektu źródłowego. Pozycja obiektu źródłowego jest ignorowana: dla celów szyku wartości {{Value|x}}, {{Value|y}} i {{Value|z}} są ustawione na {{Value|0}}. Jeśli właściwość **Wyrównaj** szyku jest ustawiona na wartość {{FALSE/pl}}, orientacja elementów szyku jest identyczna z orientacją obiektu źródłowego. Jeśli jest ustawiona na {{TRUE/pl}}, oś X lokalnego układu współrzędnych każdego umieszczonego elementu jest styczna do ścieżki. Osie Y i Z lokalnych układów współrzędnych zależą od właściwości **Tryb wyrównania** szyku. Inne właściwości szyku związane z wyrównaniem obejmują: **Wektor styczny**, **Wymuś pionowo** i **Wektor pionowy**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width:600px;"> 
*Trzy szyki oparte na tej samej nieplanarnej ścieżce. Od lewej do prawej: Wyrównanie ustawiono na {{false/pl*, Wyrównanie ustawiono na {{true/pl}} z trybem wyrównania Original i Wyrównaj ustawiono na {{true/pl}} z trybem wyrównania Frenet.}}.



### Tryb wyrównania 

Dostępne są trzy tryby:

#### Original

Ten tryb jest najbardziej zbliżony do pojedynczego **Tryb wyrównania** dostępnego w wersji 0.18. Opiera się on na stałym wektorze normalnym. Jeśli ścieżka jest płaska, wektor ten jest prostopadły do płaszczyzny ścieżki, w przeciwnym razie używany jest wektor domyślny, o dodatniej osi Z. Na podstawie tego wektora normalnego i lokalnego wektora stycznego *(lokalna oś X)* obliczany jest [iloczyn krzyżowy](https://en.wikipedia.org/wiki/Cross_product). Ten nowy wektor jest używany jako lokalna oś Z. Orientacja lokalnej osi Y jest określana na podstawie lokalnych osi X i Z.

#### Frenet

Tryb ten wykorzystuje lokalny wektor normalny wyprowadzony ze ścieżki przy każdym umieszczeniu elementu. Jeśli nie można określić tego wektora *(na przykład w przypadku odcinka prostego)*, zamiast niego używany jest wektor domyślny, ponownie dodatnia oś Z. Za pomocą tego wektora i lokalnego wektora stycznego lokalny układ współrzędnych jest określany przy użyciu tej samej procedury, co w poprzednim akapicie.



### Styczna

Tryb ten jest podobny do **Trybu wyrównania** {{Value|Original}}, ale obejmuje możliwość wstępnego obrócenia obiektu źródłowego poprzez określenie **Wektora stycznej**.



### Wymuś pionowo i Wektor pionowy 

Właściwości te są dostępne tylko wtedy, gdy **Tryb wyrównania** ma wartość {{Value|Original}} lub {{Value|Styczny}}. Jeśli właściowść **Wymuś pionowo** jest ustawione na {{TRUE/pl}}, lokalny układ współrzędnych jest obliczany w inny sposób. **Wektor pionowy** jest używany jako stały wektor normalny. Z tego wektora normalnego i lokalnego wektora stycznego *(lokalna oś X)* ponownie obliczany jest iloczyn krzyżowy. Ale teraz ten wektor jest używany jako lokalna oś Y. Orientacja lokalnej osi Z jest określana na podstawie lokalnych osi X i Y.

Użycie tych właściwości może być wymagane, jeśli jedna z krawędzi ścieżki jest *(prawie)* równoległa do domyślnej normalnej ścieżki.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Szyk po ścieżce środowiska Rysunek Roboczy wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości *(z wyjątkiem niektórych właściwości Widoku, które nie są dziedziczone przez szyki Łączy)*. Poniższe właściwości są dodatkowe, chyba że zaznaczono inaczej:



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
    


{{TitleProperty|Wyrównanie}}

-    **Wyrównaj|Bool**: określa, czy elementy w tablicy są wyrównane wzdłuż ścieżki, czy nie. Jeśli ma wartość {{FALSE/pl}}, wszystkie inne właściwości w tej grupie, z wyjątkiem **Dodatkowe przesunięcie**, nie mają zastosowania i są ukryte.

-    **Tryb wyrównania|Enumeration**: określa tryb wyrównania, który może być {{Value|Original}}, {{Value|Frenet}} lub {{Value|Stycznie}}.

-    **Koniec odsunięcia|Length**: określa długość od końca ścieżki do ostatniej kopii. Musi być mniejsza niż długość ścieżki minus **Początek odsunięcia**. {{Version/pl|0.21}}

-    **Dodatkowe przesunięcie|VectorDistance**: określa dodatkowe przemieszczenie dla każdego elementu wzdłuż ścieżki.

-    **Wymuś pionowo|Bool**: określa, czy zastąpić domyślny kierunek normalny wartością **Wektor pionowy**. Używane tylko jeśli **Tryb wyrównania** ma wartość {{Value|Original}} lub {{Value|Styczna}}.

-    **Przesunięcie początkowe|Length**: określa długość od początku ścieżki do pierwszej kopii. Musi być mniejsza niż długość ścieżki. {{Version/pl|0.21}}

-    **Wektor styczny|Vector**: określa wektor wyrównania. Używane tylko jeśli **Tryb wyrównania** jest {{Value|Styczna}}.

-    **Wektor pionowy|Vector**: określa nadpisanie domyślnego kierunku normalnego. Używane tylko jeśli właściwość **Wektor pionowy** ma wartość {{TRUE/pl}}.


{{TitleProperty|Obiekty}}

-    **Baza|LinkGlobal**: określa obiekt do powielenia w szyku.

-    **Ilość|Integer**: określa liczbę elementów w szyku.

-    **Rozwiń szyk|Bool**: określa, czy tablica ma zostać rozwinięta w [widoku drzewa](Tree_view/pl.md), aby umożliwić wybór jej poszczególnych elementów. Dostępne tylko dla szyków łączy.

-    **Scal|Bool**: określa, czy nakładające się elementy w tablicy są łączone, czy nie. Nie używane dla tablic Łączy. {{Version/pl|1.0}}

-    **Obiekt ścieżki|LinkGlobal**: określa obiekt, który ma być użyty dla ścieżki. Musi zawierać {{Value|Krawędzie}} w swoim [kształcie topologicznym](Part_TopoShape/pl.md).

-    **Elementy podżędne ścieżki|LinkSubListGlobal**: określa listę krawędzi **Obiektu ścieżki**. Jeśli zostanie podana, tylko te krawędzie są używane dla ścieżki.



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

Aby utworzyć Szyk po ścieżce, należy użyć metody `make_path_array` ({{Version/pl|0.19}}) modułu Rysunek Roboczy. Metoda ta zastępuje przestarzałą metodę `makePathArray`.


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```

-    `base_object`jest obiektem, który ma być użyty w szyku. Może to być również `Etykieta` *(ciąg znaków)* obiektu w bieżącym dokumencie.

-    `obiekt_ścieżki`jest obiektem ścieżki. Może to być również `Etykieta` *(ciąg znaków)* obiektu w bieżącym dokumencie.

-    `Ilość`jest liczbą elementów w tablicy.

-    `extra`jest wektorem, który przesuwa każdy element.

-    `Element podrzędny`jest listą krawędzi `obiekt_ścieżki`, na przykład `["Edge1", "Edge2"]`. Jeśli zostanie podana, tylko te krawędzie są używane dla ścieżki.

-   Jeśli `Wyrównaj` ma wartość {{True/pl}}, elementy są wyrównywane wzdłuż ścieżki w zależności od wartości właściwości `tryb_wyrównania`, która może mieć wartość `"Original"`, `"Frenet"` lub `"Styczna"`.

-    `tan_vector`jest wektorem jednostkowym, który definiuje lokalny kierunek styczny elementów wzdłuż ścieżki. Jest on używany, gdy właściwość `tryb_wyrównania` ma wartość `"Styczna"`.

-   Jeśli `Wymuś_pionowo` ma wartość {{True/pl}}, `vertical_vector` jest używany dla lokalnego kierunku Z elementów wzdłuż ścieżki. Jest on używany, gdy właściwość `tryb_wyrównania` ma wartość `"Original"` lub `"Styczna"`.

-   Jeśli `użyj_łaczy` ma wartość {{True/pl}}, utworzone elementy są obiektami [App: Łącze](App_Link/pl.md) zamiast zwykłych kopii.

-    `Szyk_ścieżki`jest zwracany wraz z utworzonym obiektem szyku.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(500, -1000, 0)
p2 = App.Vector(1500, 1000, 0)
p3 = App.Vector(3000, 500, 0)
p4 = App.Vector(4500, 100, 0)
spline = Draft.make_bspline([p1, p2, p3, p4])
obj = Draft.make_polygon(3, 500)

path_array = Draft.make_path_array(obj, spline, 6)
doc.recompute()

wire = Draft.make_wire([p1, -p2, -p3, -p4])
path_array2 = Draft.make_path_array(obj, wire, count=3, extra=App.Vector(0, -500, 0), subelements=["Edge2", "Edge3"], align=True, force_vertical=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/pl
