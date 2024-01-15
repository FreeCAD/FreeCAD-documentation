# PropertyLink: InList and OutList/pl
Zobacz artykuł [Właściwości](Property/pl.md) przed tą sekcją.



# PropertyLink

Oprócz skalarnych [Properties](Property/pl.md) cech, same cechy zawierają wskaźniki do siebie nawzajem. Wskaźniki te definiują [skierowany graf acykliczny](https://en.wikipedia.org/wiki/Directed_acyclic_graph), który określa zbiór i kolejność obiektów, które są ponownie obliczane w odpowiedzi na zmianę w jednym obiekcie. Ponownie obliczane są tylko te funkcje, które zależą od zmienionej funkcji.

Zależności są wyrażane za pomocą specjalnej klasy typów właściwości, a mianowicie PropertyLink:

-   PropertyLink: umożliwia powiązanie elementu z innym pojedynczym elementem w tym samym dokumencie.
-   PropertyLinkList: pozwala elementowi na powiązanie kilku elementów
-   PropertyLinkSub: pozwala elementowi łączyć pojedynczy element i dodatkowo odwoływać się do elementów podrzędnych. Przykład: Jeśli chcesz zamodelować kieszeń na potrzeby szkicu, ważne jest, aby wiedzieć, do którego elementu podrzędnego (np. Face6) powiązanego elementu należy ją zmapować.
-   PropertyLinkSubList: umożliwia powiązanie elementu z kilkoma elementami podrzędnymi kilku elementów.

Poniżej znajdują się podobne właściwości do łączenia cech różnych dokumentów. Jest to podstawowa część dla złożeń.

-   PropertyXLink
-   PropertyXLinkSub
-   PropertyXLinkSubList
-   PropertyXLinkList
-   PropertyXLinkContainer



## Przykład

Rozważmy klasę `BoxDimension`, która zapewnia podstawowe wymiary dla innej klasy `Box`. Chcielibyśmy, aby obiekt `Box` był ponownie obliczany za każdym razem, gdy zmieni się powiązany z nim `BoxDimension`:


```python
import FreeCAD
import Part

class BoxDimension:
  def __init__(self, obj):
    obj.addProperty("App::PropertyLength", "Length").Length = 1
    obj.addProperty("App::PropertyLength", "Width").Width = 1
    obj.addProperty("App::PropertyLength", "Height").Height = 1
    obj.Proxy = self

class Box:
  def __init__(self, obj):
    obj.addProperty("App::PropertyLink", "Dimensions").Dimensions = None
    obj.Proxy = self
  def execute(self, obj):
    if obj.Dimensions is None:
      return
    l = obj.Dimensions.Length
    w = obj.Dimensions.Width
    h = obj.Dimensions.Height
    obj.Shape = Part.makeBox(l, w, h)
```

Należy pamiętać, że jest to obiekt `Box`, który zawiera PropertyLink do obiektu `BoxDimension`. Użycie jest następujące:


```python
doc = App.newDocument()
dim = doc.addObject("App::FeaturePython", "BoxDimension")
box = doc.addObject("Part::FeaturePython", "Box")
dim_proxy = BoxDimension(dim)
box_proxy = Box(box)
box.ViewObject.Proxy = None
box.Dimensions = dim

dim.Length = 5
dim.Width = 3
dim.Height = 7
doc.recompute()
```

Ponieważ nasz `box` zależy od obiektu `dim`, zostanie on ponownie obliczony.



# Lista wejściowa i lista wyjściowa 

Dostęp do obiektów `PropertyLink` można uzyskać za pomocą właściwości Python przy użyciu nazwy, pod którą są zarejestrowane za pomocą `.addObject()`. Istnieje jednak inny sposób. Każda funkcja ma parę leniwie generowanych list o nazwach `InList` i `OutList`, które opisują odpowiednio wychodzące i przychodzące krawędzie DAG:

-    `InList`jest listą wszystkich funkcji, które \"zależą\" od bieżącego obiektu. Tak więc `dim.InList` będzie listą zawierającą nasz obiekt `box`.

-   Podobnie, `OutList` jest listą wszystkich funkcji, które \"zależą\" od bieżącego obiektu. Oznacza to, że `box.OutList` będzie listą zawierającą nasz obiekt `dim`.

Zauważ, że `InList` i `OutList` nie mają nic wspólnego z widokiem drzewa modelu dokumentu, który jest prezentowany w GUI. W dowolnym momencie rodzic w tym widoku drzewa może zawierać dzieci, które są częścią `InList`, `OutList` lub żadnego z nich.



---
⏵ [documentation index](../README.md) > PropertyLink: InList and OutList/pl
