

See [Properties](Property.md) before this section.

# PropertyLink

In addition to the scalar [Properties](Property.md) of an feature, the features themselves contain pointers to one another. These pointers define a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) that determines the set and ordering of objects that are recomputed in response to a change in one object. Only those features that depend on a changed feature are recomputed.

The dependencies are expressed via a special class of Property types, namely the PropertyLink:

-   PropertyLink: this allows a feature to link to another single feature within the same document.
-   PropertyLinkList: this allows a feature to link several features
-   PropertyLinkSub: this allows a feature to link a single feature and additionally reference sub-elements. Example: If you want to model a pocket for the needed sketch, then it\'s important to know on which sub-element (e.g. Face6) of the linked feature it must be mapped to.
-   PropertyLinkSubList: this allows a feature to link to several sub-elements of several features.

The following are similar properties for linking features of different documents. This is the core part for assemblies.

-   PropertyXLink
-   PropertyXLinkSub
-   PropertyXLinkSubList
-   PropertyXLinkList
-   PropertyXLinkContainer

## Example

Consider a class `BoxDimension` that provides basic dimensions for another class `Box`. We would like a `Box` object to be recomputed whenever its associated `BoxDimension` is changed:


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

Note that it is a `Box` object that contains the PropertyLink to the `BoxDimension` object. Usage is as follows:


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

Because our `box` depends on the `dim` object, it will be recomputed.

# InList and OutList 


`PropertyLink`

objects can be accessed using a Python property using the name that they are registered with using `.addObject()`. However there is another way. Every feature has a pair of lazily-generated lists called `InList` and `OutList` that describe the outgoing and incoming edges of the DAG, respectively:

-   An `InList` is a list of all features that *depend upon* the current object. So, `dim.InList` will be a list containing our `box` object.
-   Similarly, an `OutList` is a list of all features that *are depended upon* the current object. That is, `box.OutList` will be a list containing our `dim` object.

Note that `InList` and `OutList` have **nothing** to do with the tree view of the document model that is presented in the GUI. At any time, a parent in that tree view may contain children that are part of the `InList`, the `OutList`, or neither.
