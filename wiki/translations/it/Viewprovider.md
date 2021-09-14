# Viewprovider/it



## Introduzione

Le **Viewprovider** sono delle classi che definiscono il modo in cui gli oggetti appariranno nella [vista ad albero](tree_view/it.md) e nella [vista 3D](3D_view/it.md) e come interagiranno con determinate azioni grafiche come la [selezione](selection/it.md).

They complement the [scripted objects](scripted_objects.md). While the base class of the scripted object defines its **data** [properties](property.md), the viewprovider defines it **view** [properties](property.md). These view properties are not essential information of the object, as they only indicate superficial information like line width, line color, face color, etc. In a terminal only session, the viewprovider is not loaded because there will be no interface to manipulate those visible properties.

Like with data properties, view properties are accessible from the [property editor](property_editor.md).

## Python view providers 

The viewproviders classes usually include `ViewProvider` in their name. They are assigned on the `ViewObject` attribute of the base object.

In this example, we define two properties for the viewprovider, only if the properties don\'t already exist, and assign their default values. We also define the `onChanged` method that runs every time a property changes. We need to test the property by name, and then we will call one of two methods that will do the actual work of updating the pattern or setting its size. 
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

The normal workflow is to first add the object proxy class, for example, `CustomObject`, and then the viewprovider, for example, `ViewProviderCustom`. The viewprovider can only be assigned when we have verified that the graphical interface is available, as otherwise the `ViewObject` attribute doesn\'t exist, and it will be an error to use this element as input for our class. 
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

## Custom icons 

By implementing the `getIcon` method, you can specify the icon that will be shown in the [tree view](tree_view.md) in the upper part of the [combo view](combo_view.md).

The return value can be the full path to an icon. 
```python
import os
some_path = "/home/user/.FreeCAD/custom_icons"

class ViewProviderCustom:
    ...

    def getIcon(self):
        return os.path.join(some_path, "my_icon.svg")
```

The relative path to an icon inside a compiled resource file. 
```python
import MyModule_rc.py

class ViewProviderCustom:
    ...

    def getIcon(self):
        return ":/icons/my_icon.svg"
```

A raw [XPM icon](https://en.wikipedia.org/wiki/X_PixMap), which is essentially ASCII art. 
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

See various examples in [Custom icon in tree view](Custom_icon_in_tree_view.md).


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
