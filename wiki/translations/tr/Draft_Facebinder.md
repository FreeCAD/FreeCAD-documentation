---
 GuiCommand:
   Name: Draft Facebinder
   Name/tr: Yüz kaplama
   Workbenches: Draft_Workbench/tr, Arch_Workbench/tr
   MenuLocation: Taslak , Yüz kaplama
   Shortcut: **F** **F**
   SeeAlso: Part Box/tr, Arch Wall/tr
   Version: 0.14
---

# Draft Facebinder/tr


</div>



## Açıklama


<div class="mw-translate-fuzzy">

Yüz kaplama aracı, katı bir nesnenin seçilen yüzlerinden bir yüzey nesnesi oluşturur. Parametriktir, yani eğer orijinal nesneyi değiştirirseniz, Facebinder buna göre güncellenir. Facebinder\'ı hareket ettirip döndürürseniz, orijinal yüzlere bağlı kalacaktır.


</div>


<div class="mw-translate-fuzzy">

Başka nesnelerden gelen bir yüz koleksiyonundan bir ekstrüzyon oluşturmak için kullanılabilir. Mimari tasarımda , örneğin duvar kağıdı veya duvar kaplaması gibi çeşitli duvarları kapsayan bir nesneyi inşa etmek tipik bir kullanımdır.


</div>

<img alt="" src=images/Draft_facebinder_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


{{Caption | Yüz kaplama ile katı duvarların yüzlerinden oluşturulmuş}}


</div>



## Nasıl kullanılır 


<div class="mw-translate-fuzzy">

1.  Bir yüz seçin veya {{KEY | Ctrl}} tuşunu basılı tutun ve katı nesnelerden birkaç yüz seçin.

2.  
    {{Button | <img src="images/_Draft_Facebinder.png_" width= 16px> [Taslak Yüz kaplama](Draft_Facebinder/tr_.md)}}düğmesine basın veya {{KEY | F}} ardından {{KEY | F}} tuşlarına basın.


</div>




<div class="mw-translate-fuzzy">

## Özellikler

### Veri

-    {{PropertyData | Extrusion}}: şeklin tüm yüzlerine uygulanacak bir ekstrüzyon kalınlığı belirtir.

-    {{PropertyData | Remove Splitter}}: `True` ise, Ekstrüzerin iç kavşaklarını ekstrüzyon sırasında birleştirmeye çalışır.

-    {{PropertyData | Sew}}: `True` ise, Ekstrüder üzerine ekstrüzyon sırasında topolojik bir dikiş işlemi gerçekleştirmeye çalışır.


</div>

See also: [Property editor](Property_editor.md).

A Draft Facebinder object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the total area of the linked faces of the facebinder.

-    **Extrusion|Distance**: specifies the extrusion thickness of the facebinder.

-    **Faces|LinkSubList**: specifies the linked faces of the facebinder.

-    **Offset|Distance**: specifies an offset distance to apply between the facebinder and the original faces, prior to extrusion.

-    **Remove Splitter|Bool**: Specifies whether to remove splitter lines that divide co-planar faces of the facebinder.

-    **Sew|Bool**: Specifies whether to perform a topological sewing operation on the facebinder.

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView | Pattern}}: şeklin yüzünü doldurmak için bir [Taslak Deseni](Draft_Pattern/tr.md) belirtir. Bu özellik yalnızca {{PropertyView | Display Mode}} \"Düz Çizgiler\" ise çalışır.

-    {{PropertyView | Pattern Size}}: [Taslak Deseni](Draft_Pattern/tr.md) \'nin boyutunu belirtir.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Yüz kaplama aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
facebinder = make_facebinder(selectionset)
```


<div class="mw-translate-fuzzy">

-   Bir {{incode | Facebinder}} nesnesini, {{incode | FreeCADGui.Selection.getSelectionEx()}} tarafından döndürülenler gibi {{incode | SelectionObject}} \'ların bir listesi olan verilen {{incode | choiceset}} nesnesinden oluşturur.
-   Sadece seçilen yüzler dikkate alınır.


</div>


```python
PropertyLinkSubList = [tuple1, tuple2, tuple3, ...]
PropertyLinkSubList = [(object1, list1), (object2, list2), (object3, list3), ...]
PropertyLinkSubList = [(object1, ['Face1', 'Face4', 'Face6']), ...]
PropertyLinkSubList = [(object1, ('Face1', 'Face4', 'Face6')), ...]
```


<div class="mw-translate-fuzzy">

Yüz kaplama kalınlığı {{incode | Extrusion}} özniteliğinin üzerine yazılarak eklenebilir; değer milimetre cinsinden girilir.


</div>


<div class="mw-translate-fuzzy">

Yüz kaplamanın yerleşimi, {{incode | Placement}} özniteliğinin üzerine yazarak veya {{incode | Placement.Base}} ve {{incode | Placement.Rotation}} özniteliklerinin üzerine yazılarak değiştirilebilir.


</div>

Örnek:


```python
import FreeCAD as App
import FreeCADGui as Gui
import Draft

doc = App.newDocument()

# Insert a solid box
box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

# selection = Gui.Selection.getSelectionEx()
selection = [(box, ("Face1", "Face6"))]
facebinder = Draft.make_facebinder(selection)
facebinder.Extrusion = 50

doc.recompute()

facebinder.Placement.Base = App.Vector(1000, -1000, 100)
facebinder.ViewObject.ShapeColor = (0.99, 0.99, 0.4)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Facebinder/tr
