# Viewprovider/it
## Introduzione

Le [Viewproviders](Viewprovider/it.md) sono classi che definiscono il modo in cui gli oggetti appariranno nella [Vista ad albero](tree_view/it.md) e nella [Vista 3D](3D_view/it.md), e come interagiranno con certe azioni grafiche come la [selezione](Selection_methods/it.md).

Completano gli [scripted objects](scripted_objects/it.md). Mentre la classe base dell\'oggetto con script definisce le suoe **data** [proprietà](property/it.md), il viewprovider definisce le **view** [proprietà](property/it.md). Queste proprietà della vista non sono informazioni essenziali dell\'oggetto, poiché indicano solo informazioni superficiali come larghezza della linea, colore della linea, colore del viso, ecc. In una sessione solo terminale, il viewprovider non viene caricato perché non ci sarà alcuna interfaccia per manipolare quelli visibili proprietà.

Come per le proprietà dei dati, le proprietà della vista sono accessibili dall\'[editor di proprietà](property_editor/it.md).



## View providers di Python 

Le classi viewprovider di solito includono `ViewProvider` nel loro nome. Sono assegnati sull\'attributo `ViewObject` dell\'oggetto di base.

In questo esempio definiamo due proprietà per il viewprovider, solo se le proprietà non esistono già, e assegniamo i relativi valori predefiniti. Definiamo anche il metodo `onChanged` che viene eseguito ogni volta che una proprietà cambia. Dobbiamo testare la proprietà per nome, quindi chiameremo uno dei due metodi che svolgeranno il lavoro effettivo di aggiornamento del modello o di impostazione della sua dimensione. 
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

Il normale flusso di lavoro consiste nell\'aggiungere prima la classe proxy dell\'oggetto, ad esempio, `CustomObject`, quindi il viewprovider, ad esempio, `ViewProviderCustom`. Il viewprovider può essere assegnato solo dopo aver verificato che l\'interfaccia grafica sia disponibile, altrimenti l\'attributo `ViewObject` non esiste e sarebbe un errore utilizzare questo elemento come input per la nostra classe. 
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



## Icone personalizzate 

Implementando il metodo `getIcon`, è possibile specificare l\'icona che verrà mostrata nella [vista ad albero](tree_view/it.md) nella parte superiore della [vista combinata](combo_view/it.md).

Il valore restituito può essere il percorso completo di un\'icona. 
```python
import os
some_path = "/home/user/.FreeCAD/custom_icons"

class ViewProviderCustom:
    ...

    def getIcon(self):
        return os.path.join(some_path, "my_icon.svg")
```

Il percorso relativo a un\'icona all\'interno di un file di risorse compilato. 
```python
import MyModule_rc.py

class ViewProviderCustom:
    ...

    def getIcon(self):
        return ":/icons/my_icon.svg"
```

Una raw [XPM icon](https://en.wikipedia.org/wiki/X_PixMap), che è essenzialmente ASCII art. 
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

Vedere vari esempi in [Icona personalizzata nella visualizzazione ad albero](Custom_icon_in_tree_view/it.md).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Viewprovider/it
