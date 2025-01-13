---
 GuiCommand:
   Name: Draft Label
   Name/pl: Rysunek Roboczy: Etykieta
   MenuLocation: Adnotacja , Etykieta
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
   Shortcut: **D** **L**
   Version: 0.17
   SeeAlso: Draft_Text/pl, Draft_ShapeString/pl
---

# Draft Label/pl



## Opis

Polecenie <img alt="" src=images/Draft_Label.svg  style="width:24px;"> **Etykieta** tworzy wielowierszowy tekst z dwu-segmentową linią prowadzącą i strzałką.

Jeśli obiekt lub element podrzędny (ściana, krawędź lub wierzchołek) jest zaznaczony podczas uruchamiania polecenia, obiekt tekstu może wyświetlać jeden lub dwa atrybuty wybranego elementu, w tym położenie, długość, powierzchnię, objętość i materiał. Tekst będzie wówczas powiązany z atrybutami i będzie aktualizowany w przypadku zmiany ich wartości.

Aby wstawić element tekstowy bez strzałki, należy użyć polecenia [Tekst](Draft_Text/pl.md).

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;"> 
*Różne etykiety z różnymi orientacjami, strzałkami i informacjami.*



## Użycie

Zapoznaj się również z informacjami na stronie: [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Opcjonalnie wybierz obiekt lub jego element podrzędny (wierzchołek, krawędź lub ścianę), którego atrybuty chcesz wyświetlić.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Label.svg" width=16px> '''Etykieta'''**.
    -   Wybierz z menu opcję **Opisy → <img src="images/Draft_Label.svg" width=16px> Etykieta**.
    -   Użyj skrótu klawiaturowego: **D**, a następnie **L**.
3.  Otworzy się panel zadań **Etykieta**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
4.  Jeśli wybrałeś element: wybierz opcję z rozwijanej listy **Typ etykiety**. Zobacz sekcję [Typ etykiety](#Typ_etykiety.md) poniżej.
5.  Wybierz pierwszy punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**. Ten punkt wskazuje cel *(główkę strzałki)*. Może to być dowolne miejsce, nie musi znajdować się na elemencie.
6.  Wybierz drugi punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**. Punkt ten wskazuje początek poziomego lub pionowego segmentu linii prowadzącej.
7.  Wybierz trzeci punkt w oknie [widoku 3D](3D_view/pl.md) lub wpisz współrzędne i naciśnij przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**. Punkt ten wskazuje punkt bazowy tekstu.



## Opcje

Skróty klawiaturowe jedno znakowe dostępne w panelu zadań można zmienić. Zobacz stronę [Preferencji](Draft_Preferences/pl.md). Skróty wymienione tutaj są skrótami domyślnymi.

-   Aby ręcznie wprowadzić współrzędne, wprowadź element X, Y i Z i naciśnij **Enter** po każdym z nich. Możesz też nacisnąć przycisk **<img src="images/Draft_AddPoint.svg" width=16px> Wprowadź punkt**, gdy uzyskasz żądane wartości. Zaleca się przesunięcie wskaźnika poza okno [widoku 3D](3D_view/pl.md) przed wprowadzeniem współrzędnych.
-   Wciśnij **R** lub kliknij pole wyboru **Względnie**, aby przełączyć tryb względny. Jeśli tryb względny jest włączony, współrzędne są względne do ostatniego punktu, jeśli jest dostępny, w przeciwnym razie są one względne do początku układu współrzędnych.
-   Naciśnij **G** lub kliknij pole wyboru **Globalnie**, aby przełączyć tryb globalny. Jeśli tryb globalny jest włączony, współrzędne odnoszą się do globalnego układu współrzędnych, w przeciwnym razie odnoszą się do układu współrzędnych [płaszczyzny roboczej](Draft_SelectPlane/pl.md).
-   Naciśnij **S**, aby włączyć lub wyłączyć [Przyciąganie](Draft_Snap/pl.md).
-   Naciśnij **Esc** lub przycisk **Zamknij**, aby przerwać polecenie.



## Typ etykiety 

Dostępne są następujące typy etykiet:

-    {{Value|Użytkownika}}: wyświetla zawartość **Tekst użytkownika**.

-    {{Value|Nazwa}}: wyświetla wewnętrzną nazwę obiektu docelowego. Nazwa wewnętrzna jest przypisywana podczas tworzenia obiektu i pozostaje niezmienna przez cały okres istnienia obiektu.

-    {{Value|Etykieta}}: wyświetla etykietę obiektu docelowego. Etykieta obiektu może zostać zmieniona przez użytkownika.

-    {{Value|Pozycja}}: wyświetla współrzędne punktu bazowego obiektu docelowego lub wierzchołka docelowego.

-    {{Value|Długość}}: wyświetla długość docelowego obiektu lub elementu podrzędnego.

-    {{Value|Powierzchnia}}: wyświetla obszar docelowego obiektu lub elementu podrzędnego.

-    {{Value|Objętość}}: wyświetla objętość obiektu docelowego.

-    {{Value|Znacznik}}: wyświetla atrybut `Znacznik` obiektu docelowego. Obiekty utworzone za pomocą środowiska pracy [BIM](BIM_Workbench/pl.md) mogą mieć ten atrybut.

-    {{Value|Materiał}}: wyświetla etykietę materiału obiektu docelowego.

-    {{Value|Etykieta + pozycja}},

-    {{Value|Etykieta + długość}},

-    {{Value|Etykieta + powierzchnia}},

-    {{Value|Etykieta + objętość}},

-    {{Value|Etykieta + materiał}}.



## Uwagi

-   Kierunek drugiego segmentu lidera określa wyrównanie tekstu. Jeśli segment jest poziomy i skierowany w prawo, tekst jest wyrównany do lewej i odwrotnie. Jeśli drugi segment jest skierowany pionowo w górę, tekst jest wyrównany do lewej. Jeśli jest skierowany pionowo w dół, tekst jest wyrównany do prawej.
-   Wersje robocze etykiet utworzone lub zapisane w [FreeCAD w wersji 0.21](Release_notes_0.21/pl.md) nie są kompatybilne wstecz.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Etykieta środowispa pracy Rysunek Roboczy wywodzi się z obiektu [App: FeaturePython](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Poniższe właściwości są dodatkowe, chyba że zaznaczono inaczej.



### Dane


{{TitleProperty|Etykieta}}

-    **Tekst użytkownika|StringList**: określa zawartość tekstu, jeśli **Typ etykiety** to {{Value|Użytkownika}}. Każda pozycja na liście reprezentuje nową linię tekstu.

-    **Typ etykiety|Enumeration**: określa typ informacji wyświetlanych przez etykietę. Zobacz sekcję [Typy etykiet](#Typ_etykiety.md).

-    **Umiejscowienie|Placement**: określa położenie tekstu w oknie [widoku 3D](3D_view/pl.md) i, o ile **Kierunek prosty** nie ma wartości {{Value|Użytkownika}}, także pierwszego segmentu prowadzącego, czyli segmentu, do którego dołączony jest tekst. Zobacz stronę [Umiejscowienie](Placement/pl.md).

-    **Tekst|StringList**: *(tylko do odczytu)* określa zawartość wyświetlanego tekstu. Każdy element na liście reprezentuje nową linię tekstu.


{{TitleProperty|Odniesienie}}

-    **Punkt|VectorList**: określa punkty lidera.

-    **Kierunek prosty|Enumeration**: określa kierunek pierwszego segmentu prowadzącego: {{Value|Użytkownika}}, {{Value|Poziomo}} lub {{Value|Pionowo}}.

-    **Odległość prosta|Distance**: określa długość pierwszego segmentu prowadzącego. Używane tylko jeśli **Kierunek prosty** ma wartość {{Value|Poziomo}} lub {{Value|Pionowo}}. Jeśli odległość jest dodatnia, linia pomocnicza zaczyna się od prawej strony tekstu, a tekst jest wyrównywany do prawej. W przeciwnym razie lider zaczyna od lewej strony tekstu, a tekst jest wyrównany do lewej.


{{TitleProperty|Cel}}

-    **Cel|LinkSub**: określa obiekt i opcjonalny element podrzędny, z którym powiązana jest etykieta.

-    **Punkt docelowy|Vector**: określa pozycję końcówki linii prowadzącej, do której przymocowana jest strzałka.



### Widok


{{TitleProperty|Adnotacja}}

-    **Styl adnotacji|Enumeration**: określa styl adnotacji zastosowany do etykiety. Zobacz stronę [Edytor stylów adnotacji](Draft_AnnotationStyleEditor/pl.md).

-    **Mnożnik skali|Float**: określa ogólny współczynnik skalowania zastosowany do etykiety.


{{TitleProperty|Opcje wyświetlania}}

-    **Tryb wyświetlania|Enumeration**: określa sposób wyświetlania tekstu. Jeśli wartością jest {{value|Świat}}, tekst będzie wyświetlany na płaszczyźnie zdefiniowanej przez jego **Umiejscowienie**. Jeśli jest to {{value|Ekran}}, tekst będzie zawsze skierowany w stronę ekranu. To jest własność dziedziczona. Wspomniane opcje to opcje o zmienionych nazwach *({{Version/pl|0.21}})*.


{{TitleProperty|Grafika}}

-    **Rozmiar strzałki|Length**: określa rozmiar symbolu wyświetlanego na końcu linii prowadzącej.

-    **Typ strzałki|Enumeration**: określa typ symbolu wyświetlanego na końcu wskaźnika, którym może być {{value|Punkt}}, {{value|Okrąg}}, {{value|Strzałka}}, {{value|Grot}} lub {{value|Grot-2}}.

-    **Ramka|Enumeration**: określa typ ramki rysowanej wokół tekstu. Dostępne opcje to {{Value|Brak}} lub {{Value|Prostokąt}}.

-    **Linia|Bool**: określa, czy ma być wyświetlana linia prowadząca. Jeśli ma wartość {{FALSE/pl}}, wyświetlane są tylko strzałka i tekst.

-    **Kolor linii|Color**: określa kolor linii prowadzącej i strzałki. Jest on również używany dla ramki.

-    **Szerokość linii|Float**: określa szerokość linii odniesienia. Jest używana także dla ramki.


{{TitleProperty|Tekst}}

-    **Nazwa czcionki|Font**: określa czcionkę używaną do rysowania tekstu. Może to być nazwa czcionki, taka jak {{value|Arial}}, domyślny styl, taki jak {{value|sans}}, {{value|serif}} lub {{value|mono}}, rodzina, taka jak {{value|Arial,Helvetica,sans}}, lub nazwa ze stylem, takim jak {{value|Arial:Bold}}. Jeśli podana czcionka nie zostanie znaleziona w systemie, zamiast niej zostanie użyta czcionka domyślna. <small>(v0.21)</small> 

-    **Rozmiar czcionki|Length**: określa rozmiar liter. Tekst może być niewidoczny w oknie [widoku 3D](3D_view/pl.md), jeśli ta wartość jest bardzo mała. <small>(v0.21)</small> .

-    **Wyrównanie|Enumeration**: określa poziome wyrównanie tekstu: {{value|Do lewej}}, {{value|Wyśrodkuj}} lub {{value|Do prawej}}. Używane tylko jeśli **Kierunek prosty** ma wartość {{Value|Użytkownika}}. W przeciwnym razie wyrównanie poziome jest oparte na znaku *(dodatnim lub ujemnym)* **Odległość prosta**.

-    **Odstępy między wierszami|Float**: określa współczynnik stosowany do domyślnej wysokości linii tekstu.

-    **Maksymalna liczba znaków|Integer**: określa maksymalną liczbę znaków w każdej linii tekstu.

-    **Wyrównanie tekstu|Enumeration**: określa pionowe wyrównanie tekstu: {{value|Do góry}}, {{value|Pośrodku}} lub {{value|W dół}}.

-    **Tekst Color|Color**: określa kolor tekstu.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć Etykietę środowiska pracy Rysunek Roboczy użyj metody `make_label` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeLabel`.


```python
label = make_label(target_point=App.Vector(0, 0, 0),
                   placement=App.Vector(30, 30, 0),
                   target_object=None, subelements=None,
                   label_type="Custom", custom_text="Label",
                   direction="Horizontal", distance=-10,
                   points=None)
```

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
doc.recompute()

p1 = App.Vector(-200, 1000, 0)
place1 = App.Placement(App.Vector(-1000, 1300, 0), App.Rotation())

label1 = Draft.make_label(p1, place1, target_object=rectangle, distance=500, label_type="Label")
label1.ViewObject.FontSize= 200

p2 = App.Vector(-200, 0, 0)
place2 = App.Placement(App.Vector(-1000, -300, 0), App.Rotation())

label2 = Draft.make_label(p2, place2, target_object=rectangle, distance=500, label_type="Custom",
                          custom_text="Beware of the sharp edges")
label2.ViewObject.FontSize= 200

p3 = App.Vector(1000, 1200, 0)
place3 = App.Placement(App.Vector(2000, 1800, 0), App.Rotation())

label3 = Draft.make_label(p3, place3, target_object=rectangle, distance=-500, label_type="Area")
label3.ViewObject.FontSize= 200

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label/pl
