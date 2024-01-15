---
 GuiCommand:
   Name: Draft Clone
   Name/pl: Draft: Klonuj
   MenuLocation: Modyfikacja , Klonuj
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **C** **L**
   SeeAlso: Draft_Scale/pl
---

# Draft Clone/pl



## Opis

Polecenie <img alt="" src=images/Draft_Clone.svg  style="width:24px;"> **Klonuj** tworzy połączone kopie, klony, wybranych obiektów. Kształt klonu jest parametryczny, będzie aktualizowany, jeśli zmieni się jego obiekt źródłowy. Ale klon ma swoją własną pozycję, obrót i skalę oraz własne [Edytor właściwości](Property_editor/pl.md). Dla obiektów [architektury](Arch_Workbench/pl.md) polecenie tworzy specjalny typ klonu: klon Arch.

Polecenie może być używane na obiektach 2D utworzonych za pomocą środowisk pracy [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale także na wielu obiektach 3D, takich jak te utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md). Klony obiektów 2D mogą być używane w [Zawartości](PartDesign_Body/pl.md) środowiska Projekt Części.

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;"> 
*Klon obok obiektu źródłowego.*



## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Clone.svg" width=16px> '''Klonuj'''**.
    -   Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Clone.svg" width=16px> Klonuj**.
    -   Użyj skrótu klawiaturowego: **C**, a następnie **L**.
3.  Jeśli nie wybrałeś jeszcze żadnego obiektu: wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt utworzony za pomocą polecenia Klon środowiska Rysunek Roboczy wywodzi się z [Część: Część na obiekt 2D](Part_Part2DObject/pl.md), obiektu [Część: Cecha](Part_Feature/pl.md) lub, jeśli tworzony jest Arch Clone, z typu obiektu źródłowego. Dziedziczy on wszystkie właściwości z tego obiektu. Klon pochodzący z jednego z dwóch pierwszych obiektów ma również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rysunek Roboczy}}

-    **Połącz|Bool**: określa, czy nakładające się kształty w klonie są łączone, czy nie.

-    **Obiekty|LinkListGlobal**: określa obiekty, które są klonowane.

-    **Skala|Vector**: określa współczynniki skali X, Y i Z.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć Klona użyj metody `make_clone` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `clone`.


```python
cloned_object = make_clone(obj, delta=None, forcedraft=False)
```

-    `obj`zawiera obiekty do sklonowania. Jest to pojedynczy obiekt lub lista obiektów.

-    `delta`to wektor przesunięcia, który zostanie zastosowany do klonu.

-   Jeśli `forcedraft` ma wartość {{False/pl}} i `obj` zawiera pojedynczy obiekt [architektury](Arch_Workbench/pl.md), tworzony jest klon Architektury. Ustaw właściwość `forcedraft` na wartość {{True/pl}}, aby zamiast tego utworzyć Klona środowiska Rysunek Roboczy.

-    `cloned_object`jest zwracany wraz z obiektem klonu.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(App.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

vector = App.Vector(2600, 500, 0)
cloned_object = Draft.clone([polygon1, polygon2], delta=vector)

cloned_object.Fuse = True

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Clone/pl
