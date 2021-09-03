---
- GuiCommand:/pl
   Name:Draft Facebinder
   Name/pl:Rysunek Roboczy: Łącznik kształtów
   MenuLocation:Kreślenie → Łącznik kształtu
   Workbenches:[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut:**F** **F**
   Version:0.14
---

## Opis

Polecenie <img alt="" src=images/Draft_Facebinder.svg  style="width:24px;"> **Łącznik kształtów** tworzy obiekt powierzchniowy z wybranych ścian. Łącznik kształtów jest parametryczny, będzie się aktualizował jeśli zmodyfikujesz jego obiekt źródłowy *(lub obiekty źródłowe)*.

Można go użyć do utworzenia wyciągnięcia z kolekcji powierzchni. Takie wytłoczenie może na przykład reprezentować wykończenie ściany w projekcie architektonicznym.

<img alt="" src=images/Draft_facebinder_example.jpg  style="width:400px;"> 
*Łącznik kształtu stworzony z powierzchni ścian*

## Użycie

1.  Wybierz jedną lub więcej ścian.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Facebinder.svg" width=16px> [Tworzy obiekt powiązania ścian ...](Draft_Facebinder/pl.md)**.
    -   Wybierz z menu opcję {{MenuCommand|Kreślenie → <img src="images/Draft_Facebinder.svg" width=16px> Łącznik kształtu}}.
    -   Użyj skrótu klawiaturowego: **F**, a następnie **F**.

## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Łącznik kształtu wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:

### Dane


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyData/pl|Powierzchnia|Area}}: (tylko do odczytu): określa całkowitą powierzchnię połączonych powierzchni w elemencie wiążącym.

-    {{PropertyData/pl|Wyciągnięcie|Distance}}: określa grubość wyciągnięcia w elemencie wiążącym.

-    {{PropertyData/pl|Ściany|LinkSubList}}: określa grubość wyciągnięć w elemencie wiążącym.

-    {{PropertyData/pl|Odsunięcie|Distance}}: określa odległość, jaka ma być zastosowana między elementem łączącym a oryginalnymi powierzchniami przed wyciągnięciem.

-    {{PropertyData/pl|Usuń rozdzielenie|Bool}}: Określa, czy usuwać linie podziału, które dzielą współpłaszczyznowe powierzchnie.

-    {{PropertyData/pl|Zszyj|Bool}}: Określa, czy wykonywać operację zespolenia topologicznego na elemencie wiążącym.

### Widok


{{TitleProperty|Rysunek Roboczy}}

-    {{PropertyView/pl|Wzór|Enumeration}}: określa [wzór](Draft_Pattern/pl.md), którym ma być wypełniona powierzchnia w elemencie wiążącym. Ta właściwość działa tylko wtedy, gdy {{PropertyData/pl|Utwórz ścianę}} ma wartość `True` i gdy {{PropertyView/pl|Tryb wyświetlania}} ma wartość {{value|Linie płaskie}}.

-    {{PropertyView/pl|Rozmiar wzoru|Float}}: określa rozmiar [wzoru](Draft_Pattern/pl.md).

## Tworzenie skryptów {#tworzenie_skryptów}

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć Łącznik kształtu użyj metody `make_facebinder` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeFacebinder`.


```python
facebinder = make_facebinder(selectionset)
```

-   Tworzy obiekt `facebinder` z podanego `selectionset`, który jest listą `SelectionObject` zwróconą przez `FreeCADGui.Selection.getSelectionEx()`. Pod uwagę brane są tylko wybrane powierzchnie.
    -   
        `selectionset`
        
        może być również `PropertyLinkSubList`.

Lista `PropertyLinkSubList` jest listą krotek; każda krotka zawiera jako pierwszy element `object`, a jako drugi element listę (lub krotkę) łańcuchów; łańcuchy te wskazują nazwy elementów podrzędnych (powierzchni) tego obiektu.


```python
PropertyLinkSubList = [tuple1, tuple2, tuple3, ...]
PropertyLinkSubList = [(object1, list1), (object2, list2), (object3, list3), ...]
PropertyLinkSubList = [(object1, ['Face1', 'Face4', 'Face6']), ...]
PropertyLinkSubList = [(object1, ('Face1', 'Face4', 'Face6')), ...]
```

Grubość obiektu Łącznika kształtu może być dodana poprzez nadpisanie jego atrybutu `Extrusion`, wartość jest wprowadzana w milimetrach.

Umiejscowienie elementu Łącznika kształtu można zmienić, nadpisując jego atrybut `Placement` lub indywidualnie nadpisując jego atrybuty `Placement.Base` i `Placement.Rotation`.

Przykład:


```python
import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

# Insert a solid box
box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

# selection = Gui.Selection.getSelectionEx()
selection = [(box, ("Face1", "Face6"))]
facebinder = Draft.make_facebinder(selection)
facebinder.Extrusion = 50

doc.recompute()

facebinder.Placement.Base = App.Vector(1000, -1000, 100)
facebinder.ViewObject.ShapeColor = (0.99, 0.99, 0.4)

doc.recompute()
```





 
