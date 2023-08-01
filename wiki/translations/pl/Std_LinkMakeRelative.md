---
- GuiCommand:
   Name:Std LinkMakeRelative
   Name/pl:Std: Utwórz łącze względne
   MenuLocation:brak
   Workbenches:wszystkie
   Version:0.19
   SeeAlso:[Część](Std_Part/pl.md), [Grupa](Std_Group/pl.md), [Utwórz łącze](Std_LinkMake/pl.md)
---

# Std LinkMakeRelative/pl



## Opis

Narzędzie **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> '''Utwórz łącze względne'''** tworzy [App Łącze](App_Link/pl.md) (klasa `App::Link`), podobnie jak narzędzie **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz łącze](Std_LinkMake/pl.md)**, ale najpierw działa na wybranych elementach podrzędnych i ustawia parametr **Przekształć łącze** na wartość {{TRUE/pl}}.



## Użycie

Przy użyciu zaznaczenia:

1.  Wybierz element podrzędny w oknie [widoku 3D](3D_view/pl.md), oznacza to wierzchołek, krawędź lub ścianę, lub dowolną ich kombinację. Te elementy podrzędne muszą należeć do jednego obiektu.
2.  Naciśnij przycisk **[<img src=images/Std_LinkMakeRelative.svg style="width:16px"> '''Utwórz łącze względne'''**. Utworzony obiekt ma taką samą ikonę jak oryginalny obiekt, ale posiada dwie strzałki wskazujące, że jest to link względny.

Bez zaznaczenia:

-   Jeśli żaden obiekt nie jest zaznaczony, to polecenie nic nie robi.
-   Jeśli obiekt jest zaznaczony tylko w oknie [Widoku drzewa](Tree_view/pl.md), ale żaden element podrzędny nie jest zaznaczony w oknie [Widoku 3D](3D_view/pl.md), to polecenie również nic nie robi.

<img alt="" src=images/Std_Link_tree_sublink_example.png ) ![](images/Std_Link_sublink_example.png  style="width:500px;">



*Oryginalna Zawartość i trzy linki utworzone z jej elementów podrzędnych, w tym krawędzi i ścian.*



## Właściwości

Polecenie to tworzy nowy obiekt [App: Łącze](App_Link/pl.md). Jego właściwości opisane są na stronie **[<img src=images/Std_LinkMake.svg style="width:16px"> [Utwórz łącze](Std_LinkMake/pl#Właściwości.md)**.

W szczególności właściwość **Przekształć łącze** jest ustawione na wartość {{TRUE/pl}}, więc właściwość **Umiejscowienie** staje się ukryte, a zamiast tego **Umiejscowienie łącza** kontroluje pozycję linku w odniesieniu do pozycji **Obiekt połączony**.



## Tworzenie skryptów 

Informacje ogólne znajdują się na stronie [Utwórz łącze](Std_LinkMake/pl.md).

Obiekt App Łącze jest tworzony za pomocą metody `addObject()` dokumentu. Aby zdefiniować łącze względne, jego metoda `setLink` jest używana do wybrania obiektu źródłowego i jednego lub więcej jego elementów podrzędnych. Następnie atrybut `LinkTransform` jest ustawiany na wartość {{True/pl}}.


```python
import FreeCAD as App

doc = App.newDocument()
body = App.ActiveDocument.addObject("Part::Box", "Box")

obj = App.ActiveDocument.addObject("App::Link", "Link")
obj.setLink(body, '', ['Edge1', 'Edge6', 'Edge7', 'Edge10', 'Face2', 'Face3'])
obj.LinkTransform = True
obj.LinkPlacement.Base = App.Vector(20, 20, 0)
App.ActiveDocument.recompute()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std LinkMakeRelative/pl
