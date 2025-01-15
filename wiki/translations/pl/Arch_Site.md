---
 GuiCommand:
   Name: Arch Site
   Name/pl: Architektura: Teren
   MenuLocation: 3D / BIM , Teren
   Workbenches: Arch_Workbench/pl
   Shortcut: **S** **I**
   SeeAlso: 
---

# Arch Site/pl



## Opis

**Teren** środowiska Architektura to specjalny obiekt łączący właściwości standardowego obiektu grupy FreeCAD i obiektów Architektury. Jest szczególnie odpowiedni do reprezentowania całego terenu projektowego lub terenu. W pracy architektonicznej opartej na formacie IFC jest głównie używany do organizacji modelu, zawierając w sobie [budynki](Arch_Building/pl.md). Teren jest również wykorzystywany do zarządzania i wyświetlania fizycznego terenu oraz może obliczać objętości ziemi do dodania lub usunięcia.



## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów, które mają być zawarte w nowym terenie.
2.  Naciśnij przycisk **<img src="images/Arch_Site.svg" width=16px> '''Teren'''** lub naciśnij klawisze **S**, a następnie **I**.



## Opcje

-   Po utworzeniu terenu możesz dodać do niego obiekty, przeciągając je i upuszczając w widoku drzewa lub korzystając z przycisku **<img src="images/Arch_Add.svg" width=16px> [Połącz obiekty](Arch_Add/pl.md)**. To określa jedynie, które obiekty są częścią danego terenu, i nie ma wpływu na teren właściwy.
-   Możesz usunąć obiekty z terenu, przeciągając je i upuszczając poza niego w widoku drzewa lub korzystając z przycisku **<img src="images/Arch_Remove.svg" width=16px> [Usuń komponent](Arch_Remove/pl.md)**.
-   Możesz dodać obiekt terenu, edytując właściwość **Ukształtowanie terenu** obiektu terenu. Teren może być otwartą powłoką lub bryłą *({{Version/pl|0.21}})*.
-   Możesz dodać objętości do dodania lub odjęcia od podstawowego terenu, dwukrotnie klikając w teren, a następnie dodając obiekty do grup Dodawania lub Odejmowania. Obiekty muszą być bryłami.
-   Właściwość **wektor wyciągnięcia** może być używana do rozwiązania problemów, które mogą pojawić się, gdy teren jest otwartą powłoką, a są dodawane i / lub odejmowane elementy składowe obiektu. Aby wykonać te dodatki / odejmowania, otwarta powłoka jest wyciągana w bryłę, która jest następnie odpowiednio modyfikowana. W zależności od topologii terenu, ta ekstruzja może nie powieść się przy domyślnym wektorze ekstruzji. W takim przypadku można spróbować rozwiązać problem, zmieniając ten wektor na inny. Ta właściwość jest ignorowana, jeśli teren jest bryłą.



## Właściwości



### Dane

-    **Teren**: Podstawowy teren tego obiektu ukształtowania terenu.

-    **Adres**: Ulica i numer domu tego terenu.

-    **Kod pocztowy**: Kod pocztowy tego terenu.

-    **Miasto**: Miasto tego terenu.

-    **Kraj**: Kraj tego terenu.

-    **Szerokość geograficzna**: Szerokość geograficzna tego terenu.

-    **Długość geograficzna**: Długość geograficzna tego terenu.

-    **URL**: Adres URL, który pokazuje ten teren na mapie internetowej.

-    **Powierzchnia projekcji**: Powierzchnia rzutu tego obiektu na płaszczyźnie XY.

-    **Obwód**: Długość obwodu tego terenu.

-    **Objętość dodatkowa**: Objętość ziemi do dodania do tego terenu.

-    **Objętość odejmowania**: Objętość ziemi do usunięcia z tego terenu.

-    **Wektor ekstruzji**: Wektor wyciągnięcia do użycia podczas operacji logicznych.

-    **Usuń dzielnik**: Usuń dzielniki z wynikowej bryły.

-    **Kąt deklinacji**: Kąt między rzeczywistą Północą a kierunkiem Północy w tym dokumencie, czyli osi Y. Oznacza to, że domyślnie Północ wskazuje na oś Y, a Wschód na oś X. Kąt rośnie w kierunku przeciwnym do ruchu wskazówek zegara. Ta właściwość była wcześniej znana jako **Odchylenie na północ**.

-    **Plik EPW**: Pozwala dołączyć plik EPW z [Strony internetowej danych EPW Ladybug](https://www.ladybug.tools/epwmap/) do tego terenu. Jest to konieczne do wyświetlania diagramów róż wiatru.



### Widok

-    **Diagram Słoneczny**: Pokazuje lub ukrywa diagram słoneczny.

-    **Kolor Diagramu Słonecznego**: Kolor diagramu słonecznego.

-    **Pozycja Diagramu Słonecznego**: Pozycja diagramu słonecznego.

-    **Skala Diagramu Słonecznego**: Skala diagramu słonecznego.

-    **Róża Wiatrów**: Pokazuje lub ukrywa diagram róży wiatrów *(wymaga wypełnionej właściwości danych **EPW File** oraz zainstalowanego modułu Python Ladybug - patrz poniżej)*.



## Typowy przepływ pracy 

Zacznij od stworzenia obiektu reprezentującego teren. Na przykład, można łatwo zaimportować dane siatki, które można przekształcić w kształt środowiska Część, korzystając z menu **Część → Utwórz kształt z siatki**. Następnie, utwórz obiekt typu Teren i ustaw jego właściwość **Ukształtowanie terenu** w stosunku do obiektu Część, którą właśnie utworzyliśmy:

![](images/Arch_site_example_01.jpg )

Utwórz objętości *(wymagane są bryły)* reprezentujące obszary, które mają zostać wykopane lub wypełnione. Kliknij dwukrotnie obiekt Teren w widoku drzewa i dodaj te objętości do grup Dodawanie lub Odejmowanie. Kliknij przycisk OK.

![](images/Arch_site_example_02.jpg )

Geometria terenu zostanie ponownie obliczona, a właściwości obszarów, obwodów i objętości zostaną ponownie obliczone.

![](images/Arch_site_example_03.jpg )



## Wykresy nasłonecznienia i wiatru 

Jeśli [Ladybug](https://www.ladybug.tools/ladybug.html) jest zainstalowany na Twoim systemie, Obiekty typu [teren](Arch_Site/pl.md) mogą wyświetlać diagram słoneczny i / lub różę wiatrów. W tym celu, właściwości **Longitude**, **Latitude** i **Declination** *(wcześniej **North Deviation**)* muszą być poprawnie ustawione, a wartości własciwości **Solar Diagram** lub **Wind Rose** ustawione na {{TRUE/pl}}.

**Uwaga**: Jeśli nie masz ododatku Ladybug, [pysolar](http://pysolar.org/) jest nadal obsługiwany do generowania wykresów słonecznych, ale nie róż wiatrów. Wymagany jest Pysolar 0.7 lub nowszy. Ladybug jest jednak znacznie potężniejszym narzędziem, które prawdopodobnie będzie częściej używane w przyszłości, więc zalecamy używanie go zamiast pysolar. Ladybug można zainstalować poprzez [pip](https://github.com/ladybug-tools/ladybug).

![](images/Freecad-solar-diagram.jpg )



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Teren** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```

-   Tworzy obiekt `Site` z `objectslist`, który jest listą obiektów, lub `baseobj`, który jest obiektem `Shape` lub `Terrain`.

Przykład: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall])
Site = Arch.makeSite([Building])

FreeCAD.ActiveDocument.recompute()
FreeCAD.Gui.ActiveDocument.ActiveView.viewIsometric()
```



### Wykres słoneczny 

Tak długo jak moduł `pysolar` jest obecny, diagram słoneczny może być dodany do terenu. Ustaw odpowiednią długość i szerokość geograficzną oraz kąty deklinacji, a także skalę odpowiednią do rozmiaru modelu.

Należy pamiętać, że wymagany jest Pysolar 0.7 lub nowszy, a ta wersja działa tylko w środowisku Python 3.


```python
Site.Longitude = -46.38
Site.Latitude = -23.33
Site.Declination = 30
#Site.Compass = True

Site.ViewObject.SolarDiagram = True
Site.ViewObject.SolarDiagramScale = 10000
FreeCAD.ActiveDocument.recompute()
```



### Wykres słoneczny niezależny od terenu 

Schemat słoneczny można utworzyć za pomocą poniższej funkcji, niezależnie od lokalizacji. 
```python
Node = makeSolarDiagram(longitude, latitude, scale=1, complete=False)
```

-   Tworzy diagram słoneczny jako węzeł Pivy, używając parametrów `longitude` i `latitude`, z opcjonalną wartością `scale`.
-   Jeśli własciwość `complete` jest ustawiona na {{True/pl}}, rysowanych jest 12 miesięcy, co pokazuje pełny układ słoneczny [analemma](https://en.wikipedia.org/wiki/Analemma).


```python
import FreeCADGui, Arch

Node = Arch.makeSolarDiagram(-46.38, -23.33, scale=10000, complete=True)
FreeCAD.Gui.ActiveDocument.ActiveView.getSceneGraph().addChild(Node)
```



---
⏵ [documentation index](../README.md) > Arch Site/pl
