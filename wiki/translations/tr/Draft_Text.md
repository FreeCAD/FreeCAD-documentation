---
- GuiCommand:/tr
   Name:Draft Text
   Name/tr:Metin
   Workbenches:[Taslak](Draft_Module/tr.md), [Mimari](Arch_Module/tr.md)
   MenuLocation:Taslak → Metin
   Shortcut:T E
   SeeAlso:[Etiket](Draft_Label/tr.md), [Şekil dizesi](Draft_ShapeString/tr.md)
   Version/tr:0.7
---


</div>

## Description


<div class="mw-translate-fuzzy">

## Açıklama

Metin aracı, geçerli belgede belirli bir noktaya bir metin parçası ekler. Taslak araç çubuğunda [Çizgi stili](Draft_Linestyle/tr.md) setini kullanır.


</div>


<div class="mw-translate-fuzzy">

Bir başlık ve ok içeren bir metin etiketi oluşturmak için [Etiket](Draft_Label/tr.md) öğesini kullanın. Düz metin veya 3D harfler oluşturmak için [Şekil dizesi](Draft_ShapeString/tr.md) ile [Parça Çıkar](Part_Extrude/tr.md) kullanın.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Metin kutusunu konumlandırmak için tek nokta gerekli*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md) and [Draft Snap](Draft_Snap.md).


<div class="mw-translate-fuzzy">

## Nasıl kullanılır {#nasıl_kullanılır}

1.  
    **<img src="images/_Draft_Text.png" width=16px> [Metin](Draft_Text/tr.md)**düğmesine basın veya **T** ardından **E** tuşları.

2.  3D görünümünde bir noktaya tıklayın veya bir [koordinat](Draft_Coordinates/tr.md) yazın ve **<img src="images/_Draft_AddPoint.svg" width=16px> [Nokta ekle](Draft_AddPoint/tr.md)** düğmesine basın.

3.  İstediğiniz metni girin, her satırda **Enter** tuşuna basın.

4.  İşlemi tamamlamak için **Enter** tuşuna iki kez basın.


</div>

## Seçenekler

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg" width=16px> [Nokta ekle](Draft_AddPoint/tr.md)** düğmesine basabilirsiniz.
-   Metni yerleştirirken, [Yakalama](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak en yakın çıtçıt konumuna zorlamak için **Ctrl** tuşunu basılı tutun.
-   Yeni bir metin satırı girmek için **Enter** veya **↓ Down arrow** tuşuna basınız.
-   Önceki metin satırını düzenlemek için **↑ Yukarı ok** tuşuna basınız.
-   Metni düzenlemeyi bitirmek için **Enter** veya **↓ Aşağı ok** tuşuna iki kez basın.
-   Geçerli komutu iptal etmek için **Esc** veya **Close** düğmesine basınız.


</div>

## Notes

-   Draft Texts created with [FreeCAD version 0.18](Release_notes_0.18.md) are not backward compatible.

## Özellikler

See also: [Property editor](Property_editor.md).

A Draft Text object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated.

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

### Veri

-    {{PropertyData/tr|Text}}: Metin bloğunun içeriğini dizelerin bir listesi olarak belirtir; listedeki her öğe, virgülle ayrılmış olarak, yeni bir satır belirtir.

-    {{PropertyData/tr|Position}}: metin bloğunun ilk satırının taban noktasını belirtir.

-    {{PropertyData/tr|Angle}}: metin bloğunun ilk satırının taban çizgisinin dönüşünü belirtir.

-    {{PropertyData/tr|Axis}}: döndürme için kullanılacak ekseni belirtir.


</div>

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the text. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the text.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|3D text}} the text will be displayed in a plane defined by its **Placement**. If it is {{value|2D text}} the text will always face the camera. This is an inherited property.


{{TitleProperty|Graphics}}

-    **Line Color|Color**: not used.

-    **Line Width|Float**: not used.


{{TitleProperty|Text}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView/tr|Display Mode}}: \"3D metin\" ise, metin başlangıçta XY düzleminde olacak şekilde sahne eksenlerine hizalanır; \"2D metin\" ise, metin her zaman kameraya dönük olacaktır.

-    {{PropertyView/tr|Font Name}}: metni çizmek için kullanılacak fontu belirtir. \"Arial\" gibi bir font adı, \"sans\", \"serif\" veya \"mono\" gibi bir varsayılan stil, \"Arial, Helvetica, sans\" gibi bir aile veya \"gibi bir stil içeren bir ad olabilir. Arial: \"Kalın. Belirtilen font sistemde bulunmuyorsa, bunun yerine genel olan kullanılır.

-    {{PropertyView/tr|Font Size}}: harflerin boyutunu belirtir. Metin nesnesi ağaç görünümünde oluşturulmuşsa, ancak hiçbir metin görünmüyorsa, görünene kadar metnin boyutunu artırın.

-    {{PropertyView/tr|Justification}}: metnin sola, sağa veya taban noktasının ortasına hizalanıp hizalanmayacağını belirtir.

-    {{PropertyView/tr|Line Spacing}}: metnin satırları arasındaki boşluğu belirtir.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Metin aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
text = make_text(string, placement=None, screen=False)
```


<div class="mw-translate-fuzzy">

-   Bir `Text` nesnesini, bir `FreeCAD.Vector` ile tanımlanmış bir `point` nesnesinde oluşturur.

-    `stringlist`bir dizedir veya bir dize listesidir; eğer bir liste ise, her eleman kendi satırında görüntülenir.

-    `screen``True` ise, metin her zaman kamera görüntüleme yönüne bakar, aksi takdirde sahne eksenleriyle aynı hizada olur ve XY düzleminde uzanır.


</div>


<div class="mw-translate-fuzzy">


`Text`

\'in görünüm özellikleri, niteliklerinin üzerine yazılarak değiştirilebilir; örneğin, `ViewObject.FontSize` üzerine, yeni boyutun milimetre cinsinden üzerine yazın.


</div>

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

t1 = "This is a sample text"
p1 = App.Vector(0, 0, 0)

t2 = ["First line", "second line"]
p2 = App.Vector(1000, 1000, 0)

text1 = Draft.make_text(t1, p1)
text2 = Draft.make_text(t2, p2)
text1.ViewObject.FontSize = 200
text2.ViewObject.FontSize = 200

zaxis = App.Vector(0, 0, 1)

t3 = ["Upside", "down"]
p3 = App.Vector(-1000, -500, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 180))
text3 = Draft.make_text(t3, place3)
text3.ViewObject.FontSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>


 
