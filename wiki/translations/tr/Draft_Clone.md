---
- GuiCommand:
   Name: Draft Clone
   Name/tr: Klonla
   MenuLocation: Taslak - Klonla
   Workbenches: [Taslak](Draft_Workbench/tr.md), [Yapı](Arch_Workbench/tr.md)
   Shortcut: **C** **L**
   SeeAlso: [Taşı](Draft_Move/tr.md), [Ölçek](Draft_Scale/tr.md)
---

# Draft Clone/tr


</div>

## Description


<div class="mw-translate-fuzzy">

## Açıklama

Taslak Klonlama aracı, seçilen bir şeklin bağlantılı kopyalarını oluşturur. Bu, eğer orijinal nesne şeklini ve özelliklerini değiştirirse, tüm klonların da değiştiği anlamına gelir. Bununla birlikte, her bir klon benzersiz konumunu, dönüşünü ve ölçeğini ve ayrıca şekil rengi, çizgi genişliği ve saydamlık gibi görünüm özelliklerini korur.


</div>


<div class="mw-translate-fuzzy">

Klonla aracı, [Taslak tezgahı](Draft_Workbench/tr.md) ile oluşturulan 2D şekillerde kullanılabilir, ancak [ Parça tezgahı](Part_Workbench/tr.md), [Parça tasarım tezgahı](PartDesign_Workbench/tr.md) ile oluşturulanlar gibi birçok 3D nesne üzerinde de kullanılabilir.


</div>

<img alt="" src=images/Draft_Clone_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Klonla Orijinal nesnenin yanındadır*


</div>

## Usage


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  Klonlamak istediğiniz nesneyi seçin.

2.  
    **<img src="images/Draft_Clone.svg" width=16px> [Klonla](Draft_Clone/tr.md)**düğmesine basın.


</div>

## Properties

See also: [Property editor](property_editor.md).

An object created with the Draft Clone command is derived from a [Part Part2DObject](Part_Part2DObject.md), a [Part Feature](Part_Feature.md) object or, if an Arch Clone is created, from the object type of the source object. It inherits all properties from that object. A clone derived from one of the first two objects also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

## Özellikleri

-    {{PropertyData | Nesneler}}: Klonlanan temel nesnelerin bir listesini belirtir.

-    {{PropertyData | Ölçek}}: Klon için her X, Y ve Z yönünde ölçeklendirme faktörünü belirtir.

-    {{PropertyData | Fuse}}: eğer `True` ve {{PropertyData | Nesneler}} birbiriyle kesişen birçok şekil içeriyorsa, ortaya çıkan klon onları birlikte tek bir şekilde birleştirir veya bir bileşik oluşturur Bunların {{Version/tr | 0.17}}


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Klonla aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
cloned_object = make_clone(obj, delta=None, forcedraft=False)
```


<div class="mw-translate-fuzzy">

-   Tek bir nesne veya nesne listesi olabilen `obj` içinden `cloned_object` oluşturur.

-   Eğer verilirse, `delta` yeni klonu temel nesnenin orijinal konumundan uzağa hareket ettiren bir `FreeCAD.Vector`.

-    `forcedraft``True` ise, elde edilen nesne, `obj` bir [Yapı tezgahı](Arch_Workbench/tr.md) olsa bile, bir Taslak klonu olacak ve bir Yapı klonu olmayacaktır.


</div>

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

place = App.Placement(App.Vector(1000, 0, 0), App.Rotation())
polygon1 = Draft.make_polygon(3, 750)
polygon2 = Draft.make_polygon(5, 750, placement=place)

vector = App.Vector(2600, 500, 0)
cloned_object = Draft.clone([polygon1, polygon2], delta=vector)

cloned_object.Fuse = True

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Clone/tr
