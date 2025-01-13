# App DocumentObject/pl
## Wprowadzenie

<img alt="" src=images/Px.svg  style="width:32px;">

**Obiekt Dokumentu**, lub formalnie `App::DocumentObject`, jest klasą bazową wszystkich klas obiektów obsługiwanych w dokumencie.

Ogólnie rzecz biorąc, \"ObiektDokumentu\" to dowolna \"rzecz\", która może pojawić się w [widoku drzewa](Tree_view/pl.md) i która jest zapisywana i przywracana podczas otwierania dokumentu.

![](images/App_DocumentObject_example.png )



*Widok drzewa pokazujący różne obiekty w dokumencie. Każdy z nich jest "obiektem dokumentu", wywodzącym się z klasy bazowej `App::DocumentObject*.`

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami w programie FreeCAD.*



## Użycie

[Obiekt dokumentu](App_DocumentObject/pl.md) jest klasą wewnętrzną, więc nie może być tworzona z poziomu interfejsu graficznego, ani nie jest przeznaczona do samodzielnego użytku. Definiuje ona jedynie podstawowe zachowanie i właściwości obiektów w programie.

Niektóre z najważniejszych obiektów dokumentu to:

-   Klasa [App: Właściwości Python](App_FeaturePython/pl.md), pusty obiekt, który może być używany do różnych celów, w zależności od dodanych atrybutów.
-   Klasa [App: Cechy geometrii](App_GeoFeature/pl.md), podstawowy obiekt wszystkich obiektów geometrycznych, czyli obiektów posiadających atrybut [Umiejscowienie](Placement/pl.md), który definiuje ich pozycję w [widoku 3D](3D_view/pl.md).
-   Klasa [Część: cCecha](Part_Feature/pl.md), pochodna klasy App GeoFeature, i nadrzędna klasa obiektów z 2D i 3D [kształtami topologicznymi](Part_TopoShape/pl.md).
-   Klasa [Mesh Feature](Mesh_Feature/pl.md), pochodna klasy App GeoFeature, i nadrzędna klasa obiektów z [siatkami](Mesh_MeshObject/pl.md) 2D i 3D.



## Właściwości

Zobacz stronę [Właściwości](Property/pl.md) dla wszystkich typów właściwości, które mogą mieć obiekty tworzone skryptami.

Są to podstawowe właściwości, które posiadają zasadniczo wszystkie obiekty. Dostęp do tych właściwości można uzyskać z [Konsoli Python](Python_console/pl.md).

-    **Etykieta|String**: użytkownik może edytować nazwę tego obiektu, jest to dowolny ciąg znaków UTF8. Domyślnie jest to samo co `Nazwa`.

-    **Etykieta2|String**: dłuższy, użytkownik może edytować opis tego obiektu, jest to dowolny ciąg znaków UTF8, który może zawierać nowe linie. Domyślnie jest to pusty ciąg znaków {{value|""}}.

-    **Silnik wyrażeń|ExpressionEngine**: lista wyrażeń.

-    **Widoczność|Bool**: definiuje czy wyświetlać obiekt czy nie.

Dla obiektów pochodnych, tylko **Etykieta** będzie domyślnie wyświetlane w [edytorze właściwości](property_editor/pl.md). Pozostałe właściwości będą ukryte.



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część: właściwość](Part_Feature/pl.md).

Obiekt dokumentu tworzy się za pomocą metody `addObject()` dokumentu. Jednakże, ogólnie rzecz biorąc, nie ma potrzeby ręcznego tworzenia tego obiektu. Zazwyczaj lepiej jest podklasować jedną z bardziej złożonych klas, na przykład [App: Właściwości Python](App_FeaturePython/pl.md), [App: Cechy geometrii](App_GeoFeature/pl.md), [Część: Cecha](Part_Feature/pl.md), [Część: Część na obiekt 2D](Part_Part2DObject/pl.md), itd.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObject", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > App DocumentObject/pl
