---
- GuiCommand:/tr
   Name:Std Group
   Name/tr:Grup Oluştur
   MenuLocation:Ağaç görünüm → Belge üzerine sağ tıkla
   Workbenches:Hepsi
   Shortcut:
   SeeAlso:[Taslak grup seçme](Draft_SelectGroup.md), [Taslak gruba ekle](Draft_AddToGroup.md)
---

# Std Group/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

Bu komut, ağaç görünümünde bir grup oluşturmanıza olanak sağlar.
Modelinizin yapısını düzenlemek için kullanılabilir.


</div>

The Std Group tool is not defined by a particular workbench, but by the base system, thus it is found in the **structure toolbar** that is available in all [workbenches](Workbenches.md).

To group 3D objects as a single unit, with the intention of creating assemblies, use [Std Part](Std_Part.md) instead.


<div class="mw-translate-fuzzy">

<img alt="" src=images/group_with_objects.png  style="width:300px;">


</div>



*Various elements inside Std Groups in the tree view.*


<div class="mw-translate-fuzzy">

## Kullanım


</div>


<div class="mw-translate-fuzzy">

Ağaç görünümünde FreeCAD belgenizin adına sağ tıklayın ve \"grup\" seçeneğini seçin.
Bir grup otomatik olarak oluşturulacak ve bir dizin simgesi ve otomatik olarak seçilen bir isim verilecektir.
Grubu sağ tıklayıp \"yeniden adlandır\" ı seçerek veya klavyenizdeki \"F2\" yi kullanarak grubu yeniden adlandırabilirsiniz.
FreeCAD nesnelerini grubun içine itin veya istediğiniz nesneyi tıklatarak gruptan çıkarın,
farenin sol düğmesini basılı tutun ve nesneyi istediğiniz yeni konuma sürüklemek için sürükle ve bırak stilini kullanın.
İmlecin altına bir \"köşegen çizgisi olan bir daire\" olduğu sürece, nesnenizi buraya bırakamazsınız.
İşaret bir \"artı\" sembolüne döndüğü anda nesneyi buraya bırakmak mümkündür.


</div>

### Notes

-   The Group object does not affect the positions in the [3D view](3D_view.md) of the elements that it contains; it is essentially just a folder that is used to keep the [tree view](tree_view.md) organized.
-   The Group can also be created from the [Python console](Python_console.md), and sub-classed to create special \"groups\", as indicated in the [Scripting](Std_Group#Scripting.md) section.

## Özellikler

A _ (`App::DocumentObject` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [App FeaturePython](App_FeaturePython.md), which is the most basic instance of an [App DocumentObject](App_DocumentObject.md), the App DocumentObjectGroup has the **Group** property.

These are the properties available in the [property editor](property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](property_editor.md).

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Label**: Grubun ismi


</div>

#### Hidden properties Data 

-    **Proxy|PythonObject**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Std_Group#Scripting.md).

### View


{{TitleProperty|Base}}

See [App FeaturePython](App_FeaturePython.md) for the basic view properties.

#### Hidden properties View 

-    **Proxy|PythonObject**: a custom view provider class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](Std_Group#Scripting.md).

## Inheritance

A _ (`App::DocumentObject` class), and is augmented with a Group extension.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `App::DocumentObjectGroup* class is a simple container which uses the Group extension to be able to hold any type of object.`

## Betik


<div class="mw-translate-fuzzy">

Aşağıdaki komut aktif belgeye yeni grup ekler:


</div>

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Std Group ([App DocumentObjectGroup](App_DocumentObjectGroup.md)) is created with the `addObject()` method of the document. Once a Group exists, other objects can be added to it with the `addObject()` or `addObjects()` methods of this Group. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Group")

bod1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
bod2 = App.ActiveDocument.addObject("Part::Box", "Box")

obj.addObjects([bod1, bod2])
App.ActiveDocument.recompute()
```

This basic `App::DocumentObjectGroup` doesn\'t have a Proxy object so it can\'t be fully used for sub-classing.

Therefore, for [Python](Python.md) subclassing, you should create the `App::DocumentObjectGroupPython` object.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

For example, a [FEM Analysis](FEM_Analysis.md) is an `App::DocumentObjectGroupPython` object with a custom icon and additional properties.

## Linkler


<div class="mw-translate-fuzzy">

-   [Use case in Arch Tutorial](Arch_tutorial#Organizing_your_model/tr.md)
-   [Belge Yapısı](Document_structure/tr.md)
-   [Modelinizi düzenleyin](http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial#Organizing_your_model)


</div>





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Group/tr
