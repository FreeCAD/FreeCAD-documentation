---
- GuiCommand:/tr
   Name:Std Part
   Name/tr:Parça Oluştur
   MenuLocation:None
   Workbenches:Hepsi
   Version:0.17
   SeeAlso:[Grup Oluştur](Std_Group.md), [Cisim Oluştur](PartDesign_Body.md)
---

# Std Part/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

**Parça** , bir grup nesnenin, tek bir birim olarak beraber hareket ettirilebilen, bir çok nesneyi bir arada tutan genel amaçlı konteynerdir. Parça, en çok Parça tasarım gövdeleri, Parça tezgahı nesneleri, Kafes nesneleri, vb. gibi FreeCAD nesnelerini içerebilir.


</div>


<div class="mw-translate-fuzzy">

Parça, eskizlerin ve diğer nesnelerin eklenebileceği yerel bir koordinat sistemi sağlar.


</div>

Although it is primarily intended for solid bodies, the Std Part can be used to manage any object that has a [Placement](Placement.md) property, so it can also contain [Mesh Features](Mesh_Feature.md), [sketches](Sketch.md), and other objects derived from the [App GeoFeature](App_GeoFeature.md) class.


<div class="mw-translate-fuzzy">

Parça, tüm tezgahlarda görüntülenen Yapı araç çubuğunda bulunur.


</div>

The **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** tool is not defined by a particular workbench, but by the base system, thus it is found in the **structure toolbar** that is available in all [workbenches](Workbenches.md). To group objects arbitrarily without considering their position, use **[<img src=images/Std_Group.svg style="width:16px"> [Std Group](Std_Group.md)**; this object does not affect the placements of the elements that it contains, it is essentially just a folder that is used to keep the [Tree view](Tree_view.md) organized.

![](images/Std_Part-tree.png )![](images/Std_Part_example.png )



*Left: elements inside a Std Part in the [Tree view](Tree_view.md). Right: objects positioned in space, referred to the Origin of the Std Part.*


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 


</div>


<div class="mw-translate-fuzzy">

Araç çubuğundaki **<img src="images/Std_Part.png" width=24px> '''Parça'''** düğmesine basın. Parça otomatik olarak aktif hale gelir.

-   Etkinleştirmek veya devre dışı bırakmak için Model ağacındaki Parçayı çift tıklayın.
-   Parçaya nesneler eklemek için, Model ağacındaki Parçaların üzerine sürükleyip bırakın.
-   Nesneleri bir Parçadan çıkarmak için, bunları Parçaların dışına ve Model ağacının üstündeki belge etiketine sürükleyip bırakın.


</div>

## Notes

-   An object can only belong to a single Part.
-   3D operations like [Part Boolean](Part_Boolean.md) cannot be applied to Parts. For example, you cannot select two Parts, and perform a [Part Fuse](Part_Fuse.md) or [Part Cut](Part_Cut.md).

## Özellikler

The [Std Part](Std_Part.md), internally called [App Part](App_Part.md) (`App::Part` class), is derived from the [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class) and inherits all its properties. It also has several additional properties. Notably properties that help it manage information in the context of an assembly, for example, **Type**, **Id**, **License**, **LicenseURL** and **Group**.

These are the properties available in the [property editor](Property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](Property_editor.md).

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Id**: Parçanın ID\'si (Parça numarası). Bu alan isteğe bağlıdır.

-    **License**: Parçanın yayınlandığı lisans.

-    **License URL**:Lisans terimlerinin bulunabileceği Web adresi.

-    **Placement**:Parçaların 3D uzayda yönünü ve konumunu belirtir. [Yerleşim](Placement.md) bölümüne bakınız.

-    **Label**: Etiket, yapılan işleme verilen addır. Bu ad, istediğiniz zaman değiştirilebilir.

-    **Group**:Referans nesneleri listeler.


</div>

### View


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: {{value|Group}}.

-    **Show In Tree|Bool**: if it is `True`, the object appears in the [Tree view](Tree_view.md). Otherwise, it is set as invisible.

-    **Visibility|Bool**: if it is `True`, the object appears in the [3D view](3D_view.md); otherwise it is invisible. By default this property can be toggled on and off by pressing the **Space** bar in the keyboard.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**: {{value|Shape}} (default), {{value|BoundBox}}. If the option is {{value|Shape}}, the entire shape (vertices, edges, and faces) will be highlighted in the [3D view](3D_view.md); if it is {{value|BoundBox}} only the bounding box will be highlighted.

## Detailed explanation 


<div class="mw-translate-fuzzy">

### Aktif Durum 

Bir FreeCAD belgesi birden fazla Parça içerebilir. Bir seferde sadece bir Parça aktif olabilir. Ağaç görünümünde açık mavi bir arka plan rengiyle etkin olan kısım görüntülenecektir.


</div>

An open document can contain multiple Parts. But only one Part can be active. The active Part is displayed in the [tree view](Tree_view.md) with the background color specified by the **Active container** value in the [preferences editor](Preferences_Editor#Colors.md) (by default, light blue). It will also be shown with bold text.

To activate or de-activate a Part:

-   Double click on it on the [Tree view](Tree_view.md), or
-   Open the context menu (right click) and select **Toggle active part**.

![](images/Std_Part_active.png )



*Document with two Std Parts, of which the second one is active.*


<div class="mw-translate-fuzzy">

### Orijin

Orijin, üç standart eksenden (X, Y, Z) ve üç standart düzlemden (XY, XZ ve YZ) oluşur. Eskizler bu düzlemlere eklenebilir. Parça içindeki tüm unsurlar Parça\'nın orijini ile ilişkilendirilir; bu, Parçanın, içerisindeki öğelerin yerleşimini etkilemeden, küresel koordinat sistemine göre hareket ettirilebileceği ve döndürülebileceği anlamına gelir.


</div>

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). [Sketches](Sketch.md) and other objects can be attached to these elements when creating them.

![](images/Part_Origin_tree.png ) ![](images/Part_Origin_view.png )



*Left: Part Origin in the [Tree view](Tree_view.md). Right: representation of the Origin elements in the [3D view](3D_view.md).*


**Note:**

the Origin is an [App Origin](App_OriginGroupExtension.md) object (`App::Origin` class), while the axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar; this is useful to choose the correct reference when creating other objects.


**Note 2:**

all elements inside the Part are referenced to the Part\'s Origin which means that the Part can be moved and rotated in reference to the global coordinate system without affecting the placement of the elements inside.


<div class="mw-translate-fuzzy">

### Görünürlük Yönetimi 

Parçanın görünürlüğü, içerdiği herhangi bir nesnenin görünürlüğünün yerini alır. Parça gizlenirse, görünürlüğü true olarak ayarlanmış olsa bile içerdiği nesneler de gizlenir. Bir Parçanın içinde birden fazla nesne bir anda görülebilir.


</div>

The Part\'s visibility supersedes the visibility of any object it contains. If the Part is hidden, the objects it contains will be hidden as well, even if their individual **Visibility** property is set to `True`. If the Part is visible, then each object\'s **Visibility** determines whether the object is shown or not.

![](images/Part_Visibility_off.png ) ![](images/Part_Visibility_on.png ) 
*The visibility of the Std Part determines whether the objects grouped under it are shown in the [3D view](3D_view.md) or not. Left: the Part is hidden, so none of the objects will be shown in the [3D view](3D_view.md). Right: the Part is visible, so each object controls its own visibility.*

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) and [scripted objects](Scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document.

A Std Part ([App Part](App_Part.md)) is created with the `addObject()` method of the document. Once a Part exists, other objects can be added to it with the `addObject()` or `addObjects()` methods.


```python
import FreeCAD as App

doc = App.newDocument()
part = App.ActiveDocument.addObject("App::Part", "Part")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

part.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

You cannot create a scripted `App::Part`. However, you can add `App::Part` behavior to a scripted `Part::FeaturePython` object by using the following code:


```python
class MyGroup(object):
    def __init__(self, obj=None):
        self.Object = obj
        if obj:
            self.attach(obj)

    def __getstate__(self):
        return

    def __setstate__(self, _state):
        return

    def attach(self, obj):
        obj.addExtension("App::OriginGroupExtensionPython")
        obj.Origin = FreeCAD.ActiveDocument.addObject("App::Origin", "Origin")

    def onDocumentRestored(self, obj):
        self.Object = obj

class ViewProviderMyGroup(object):
    def __init__(self, vobj=None):
        if vobj:
            vobj.Proxy = self
            self.attach(vobj)
        else:
            self.ViewObject = None

    def attach(self, vobj):
        vobj.addExtension("Gui::ViewProviderOriginGroupExtensionPython")
        self.ViewObject = vobj

    def __getstate__(self):
        return None

    def __setstate__(self, _state):
        return None

App.ActiveDocument.addObject("Part::FeaturePython",
                             "Group",
                             group.MyGroup(),
                             group.ViewProviderMyGroup(),
                             True)
```





{{Std_Base_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Part/tr
