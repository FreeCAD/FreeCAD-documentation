# Std Group/ro
---
 GuiCommand:   Name: Std Group   MenuLocation: Tree View , Right click on the document name   , Draft_AddToGroup---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Această comandă vă permite să creați un grup în vizualizarea arborescentă.
Acesta poate fi folosit pentru organizarea structurii modelului dvs.


</div>

The Std Group tool is not defined by a particular workbench, but by the base system, thus it is found in the **structure toolbar** that is available in all [workbenches](Workbenches.md).

To group 3D objects as a single unit, with the intention of creating assemblies, use [Std Part](Std_Part.md) instead.


<div class="mw-translate-fuzzy">

<img alt="" src=images/group_with_objects.png  style="width:300px;">


</div>



*Various elements inside Std Groups in the tree view.*




<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

Faceți clic dreapta pe numele documentului dvs. FreeCAD în vizualizarea arborescentă și alegeți \"creare grup\".
Un grup va fi creat automat și va da pictograma unui director și a unui nume ales automat.
Puteți redenumi grupul făcând clic dreapta pe grup și selectând \"redenumiți\" sau folosind \"F2\" de pe tastatură.
Împingeți obiectele FreeCAD în grup sau scoateți-le din grup făcând clic pe obiectul dorit,
mențineți apăsat butonul stânga al mouse-ului și folosiți stilul drag & drop pentru a trage obiectul în noua locație dorită.
Atâta timp cât există un semn \"cerc cu linie diagonală\" - sub cursor, nu vă puteți lăsa obiectul aici.
De îndată ce semnul se schimbă într-un simbol \"plus\", este posibil să vă abandonați obiectul aici.


</div>



## Proprietăți

The [Std Group](Std_Group.md), internally called [App DocumentObjectGroup](App_DocumentObjectGroup.md) (`App::DocumentObjectGroup` class), is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class) and inherits all its properties.

The Std Group has the same properties as the [App FeaturePython](App_FeaturePython#Properties.md), which is the most basic instance of an [App DocumentObject](App_DocumentObject.md). It also has the following additional properties in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Label**: Numele grupului


</div>



## Script


<div class="mw-translate-fuzzy">

Următaorea comandaă adugă un nou grup în documentul activ:


</div>

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Std Group ([App DocumentObjectGroup](App_DocumentObjectGroup.md)) is created with the `addObject()` method of the document. Once a Group exists, other objects can be added to it with the `addObject()` or `addObjects()` methods.


```python
import FreeCAD as App

doc = App.newDocument()
group = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Group")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

group.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

This basic `App::DocumentObjectGroup` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

For [Python](Python.md) subclassing you should create a `App::DocumentObjectGroupPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

For example, a [FEM Analysis](FEM_Analysis.md) is an `App::DocumentObjectGroupPython` object with a custom icon and additional properties.



## Legături


<div class="mw-translate-fuzzy">

-   [Use case in Arch Tutorial](Arch_tutorial#Organizing_your_model.md)
-   [Document structure](Document_structure.md)
-   [Organizing your model](http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial#Organizing_your_model)


</div>



---
⏵ [documentation index](../README.md) > Std Group/ro
