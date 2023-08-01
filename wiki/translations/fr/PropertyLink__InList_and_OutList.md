# PropertyLink: InList and OutList/fr
Voir [Propriétés des objets](Property/fr.md) avant de lire cette section.

# PropertyLink

En plus des [Propriétés des objets](Property/fr.md) scalaires d\'une fonction, les fonctions elles-mêmes contiennent des pointeurs les unes vers les autres. Ces pointeurs définissent un [Graphe orienté acyclique](https://fr.wikipedia.org/wiki/Graphe_orient%C3%A9_acyclique) qui détermine l\'ensemble et l\'ordre des objets qui sont recalculés en réponse à la modification d\'un objet. Seules les caractéristiques qui dépendent d\'une fonction modifiée sont recalculées.

Les dépendances sont exprimées par une classe spéciale de types de propriétés, à savoir les PropertyLink :

-   PropertyLink : permet à une caractéristique de se lier à une autre fonction unique dans le même document.
-   PropertyLinkList : permet à un élément de lier plusieurs éléments.
-   PropertyLinkSub : permet à un élément de lier un élément unique et de référencer des sous-éléments supplémentaires. Exemple : Si vous voulez modéliser une poche pour l\'esquisse voulue, il est important de savoir sur quel sous-élément (par exemple, Face6) de la fonction liée elle doit être mappée.
-   PropertyLinkSubList : cela permet à une fonction de se lier à plusieurs sous-éléments de plusieurs fonctions.

Voici des propriétés similaires permettant de relier les fonctions de différents documents. C\'est la partie essentielle pour les assemblages.

-   PropertyXLink
-   PropertyXLinkSub
-   PropertyXLinkSubList
-   PropertyXLinkList
-   PropertyXLinkContainer

## Exemple

Considérons une classe `BoxDimension` qui fournit des dimensions de base pour une autre classe `Box`. Nous aimerions qu\'un objet `Box` soit recalculé chaque fois que son `BoxDimension` associé est modifié :


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

Remarquez que c\'est un objet `Box` qui contient le PropertyLink de l\'objet `BoxDimension`. L\'utilisation est la suivante :


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

Comme notre `box` dépend de l\'objet `dim`, il sera recalculé.

# InList et OutList 

On peut accéder aux objets `PropertyLink` à l\'aide d\'une propriété Python en utilisant le nom avec lequel ils sont enregistrés à l\'aide de `.addObject()`. Cependant, il existe un autre moyen. Chaque fonction possède une double liste générée simplement appelée `InList` et `OutList`, qui décrit les arêtes sortantes et entrantes du DAG, respectivement :

-   Une liste `InList` est une liste de toutes les fonctions qui *dépendent* de l\'objet courant. Ainsi, `dim.InList` sera une liste contenant notre objet `box`.
-   De même, une liste `OutList` est une liste de toutes les fonctions qui *dépendent* de l\'objet courant. C\'est-à-dire que `box.OutList` sera une liste contenant notre objet `dim`.

Remarquez que `InList` et `OutList` n\'ont *rien à voir* avec l\'arborescence du modèle de document qui est présentée dans l\'interface graphique. À tout moment, un parent dans cette arborescence peut contenir des enfants qui font partie de la `InList`, de la `OutList` ou d\'aucune des deux.



---
![](images/Button_right.svg) [documentation index](../README.md) > PropertyLink: InList and OutList/fr
