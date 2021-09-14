# Viewprovider/fr



## Introduction

Les [Viewproviders](Viewprovider/fr.md) sont des classes qui définissent l\'apparence des objets dans la [vue en arborescence](tree_view/fr.md) et la [vue 3D](3D_view/fr.md) et comment ces derniers interagiront avec certaines actions graphiques telles que la [sélection](selection/fr.md).

Elles complètent les [Objets définis par script](scripted_objects/fr.md). Alors que la classe de base de l\'objet scripté définit les [propriétés](property/fr.md) de ses **data**, le viewprovider définit les [propriétés](property/fr.md) de **view**. Ces propriétés de vue ne sont pas des informations essentielles de l\'objet car elles n\'indiquent que des informations superficielles telles que la largeur de ligne, la couleur de ligne, la couleur du visage, etc\... Dans un terminal uniquement, le fournisseur de vue (viewprovider) n\'est pas chargé car il n\'y aura pas d\'interface pour manipuler ces propriétés visibles.

Comme pour les propriétés de données, les propriétés de vue sont accessibles à partir de l\'[Éditeur de propriétés](Property_editor/fr.md).

## Fournisseurs de vues Python 

Les classes viewproviders incluent généralement `ViewProvider` dans leur nom. Elles sont attribuées à l\'attribut `ViewObject` de l\'objet de base.

Dans cet exemple, nous définissons deux propriétés pour le fournisseur de vues, uniquement si les propriétés n\'existent pas déjà et attribuons leurs valeurs par défaut. Nous définissons également la méthode `onChanged` qui s\'exécute chaque fois qu\'une propriété change. Nous devrons tester la propriété par son nom puis nous appellerons l\'une des deux méthodes qui effectueront le travail réel de mise à jour du modèle ou de définition de sa taille. 
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

Le flux de travail normal consiste à ajouter d\'abord la classe proxy de l\'objet, par exemple `CustomObject`, puis le viewprovider, par exemple, `ViewProviderCustom`. Le viewprovider ne peut être attribué que lorsque nous avons vérifié que l\'interface graphique est disponible, sinon l\'attribut `ViewObject` n\'existe pas et ce sera une erreur d\'utiliser cet élément comme entrée pour notre classe. 
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

## Icônes personnalisées 

En implémentant la méthode `getIcon`, vous pouvez spécifier l\'icône qui sera affichée dans la [vue en arborescence](tree_view/fr.md) dans la partie supérieure de la [Vue Combinée](Combo_view/fr.md).

La valeur de retour peut être le chemin d\'accès complet à une icône. 
```python
import os
some_path = "/home/user/.FreeCAD/custom_icons"

class ViewProviderCustom:
    ...

    def getIcon(self):
        return os.path.join(some_path, "my_icon.svg")
```

Le chemin relatif à une icône à l\'intérieur d\'un fichier de ressources compilé. 
```python
import MyModule_rc.py

class ViewProviderCustom:
    ...

    def getIcon(self):
        return ":/icons/my_icon.svg"
```

Une image brute [XPM icon](https://en.wikipedia.org/wiki/X_PixMap), essentiellement de l\'art ASCII. 
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

Voir divers exemples dans [Icône personnalisée dans l\'arborescence](Custom_icon_in_tree_view/fr.md).


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
