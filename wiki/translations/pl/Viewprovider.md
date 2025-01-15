# Viewprovider/pl
## Wprowadzenie

Dostawcy widoku to klasy, które definiują sposób, w jaki obiekty będą wyglądać w oknie [widoku drzewa](Tree_view/pl.md) i [widoku 3D](3D_view/pl.md), oraz jak będą współdziałać z niektórymi akcjami graficznymi, takimi jak [zaznaczanie](Selection_methods/pl.md) obiektów.

Uzupełniają one [obiekty tworzone skryptami](Scripted_objects/pl.md). Podczas gdy klasa bazowa obiektu skryptowego definiuje jego [właściwości](Property/pl.md) **dane**, viewprovider definiuje jego [właściwości](Property/pl.md) **widok**. Te właściwości widoku nie są istotnymi informacjami o obiekcie, ponieważ wskazują tylko powierzchowne informacje, takie jak szerokość linii, kolor linii, kolor powierzchni itp. W sesji terminalowej dostawca widoku nie jest ładowany, ponieważ nie będzie interfejsu do manipulowania tymi widocznymi właściwościami.

Podobnie jak w przypadku właściwości danych, właściwości widoku są dostępne z poziomu [edytora własciwości](Property_editor/pl.md).



## Dostawcy widoków Python 

Klasy viewprovider zazwyczaj zawierają w nazwie ciąg `ViewProvider`. Są one przypisywane do atrybutu `ViewObject` obiektu bazowego.

W tym przykładzie definiujemy dwie właściwości dla Dostawcy widoku, tylko jeśli właściwości jeszcze nie istnieją, i przypisujemy im wartości domyślne. Definiujemy również metodę `onChanged`, która jest uruchamiana za każdym razem, gdy zmienia się właściwość. Musimy przetestować właściwość według nazwy, a następnie wywołamy jedną z dwóch metod, które wykonają rzeczywistą pracę polegającą na aktualizacji wzorca lub ustawieniu jego rozmiaru. 
```python
# views/view_custom.py
class ViewProviderCustom:
    """Viewprovider of the custom object."""

    def __init__(self, vobj):
        self.Object = vobj.Object

        self._set_properties(vobj)
        vobj.Proxy = self

    def _set_properties(self, vobj):
        if not hasattr(vobj, "Pattern"):
            vobj.addProperty("App::PropertyEnumeration",
                             "Pattern",
                             "Custom",
                             "Defines a hatch pattern for this object.")
            vobj.Pattern = ["None", "diagonals", "cross", "brick"]

        if not hasattr(vobj, "PatternSize"):
            vobj.addProperty("App::PropertyFloat",
                             "PatternSize",
                             "Custom",
                             "Defines the size of the hatch pattern.")
            vobj.PatternSize = 1

    def onChanged(self, vobj, prop):
        if prop in "Pattern":
            self._set_pattern(vobj.Pattern)
        if prop in "PatternSize":
            self._set_size(vobj.PatternSize)

    def _set_pattern(self, pattern):
        ...

    def _set_size(self, size):
        ...
```

Normalnym przepływem pracy jest dodanie najpierw klasy proxy obiektu, na przykład `CustomObject`, a następnie dostawcy widoku, na przykład `ViewProviderCustom`. Viewprovider może być przypisany tylko wtedy, gdy zweryfikowaliśmy, że interfejs graficzny jest dostępny, ponieważ w przeciwnym razie atrybut `ViewObject` nie istnieje, a użycie tego elementu jako danych wejściowych dla naszej klasy będzie błędem. 
```python
import FreeCAD as App
import objects.custom as custom
import views.view_custom as view_custom

doc = App.newDocument()
obj = doc.addObject("Part::FeaturePython", "Custom")

custom.CustomObject(obj)

if App.GuiUp:
    view_custom.ViewProviderCustom(obj.ViewObject)
```



## Ikonki użytkownika 

Implementując metodę `getIcon`, można zdefiniować ikonkę, która będzie wyświetlana w [widok drzewa](Tree_view/pl.md) w górnej części [widoku połączonego](Combo_view/pl.md).

Wartością zwrotną może być pełna ścieżka do ikony. 
```python
import os
some_path = "/home/user/.FreeCAD/custom_icons"

class ViewProviderCustom:
    ...

    def getIcon(self):
        return os.path.join(some_path, "my_icon.svg")
```

Względna ścieżka do ikony w skompilowanym pliku zasobów. 
```python
import MyModule_rc.py

class ViewProviderCustom:
    ...

    def getIcon(self):
        return ":/icons/my_icon.svg"
```

Nieobrobiona [Ikona XPM](https://en.wikipedia.org/wiki/X_PixMap), która jest zasadniczo grafiką ASCII. 
```python
import MyModule_rc.py

class ViewProviderCustom:
    ...

    def getIcon(self):
        return """
               /* XPM */
               static char *Some_icon_xpm[] = {
               /* columns rows colors chars-per-pixel */
               "16 16 3 1 ",
               "  c None",
               ". c #D71414",
               "+ c #AA1919",
               /* pixels */
               "                ",
               "  +          +  ",
               " +.+        +.+ ",
               "  +.+      +.+  ",
               "   +        +   ",
               "      ++++      ",
               "     +....+     ",
               "     +...++     ",
               "     +..+++     ",
               "     +.++.+     ",
               "      ++++      ",
               "   +        +   ",
               "  +.+      +.+  ",
               " +.+        +.+ ",
               "  +          +  ",
               "                "
               };
               """
```

Zobacz różne przykłady na stronie [Własna ikona w widoku drzewa](Custom_icon_in_tree_view/pl.md).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Viewprovider/pl
