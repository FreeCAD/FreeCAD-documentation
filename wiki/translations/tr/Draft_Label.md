---
- GuiCommand:/tr
   Name:Draft Label
   Name/tr:Etiket
   MenuLocation:Taslak → Etiket
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Mimari](Arch_Workbench/tr.md)
   Shortcut:**D** **L**
   SeeAlso:[Metin](Draft_Text/tr.md), [Şekil dizesi](Draft_ShapeString/tr.md)
   Version/tr:0.17
---

# Draft Label/tr


</div>



## Tanım


<div class="mw-translate-fuzzy">

Etiket aracı, 2 segmentli bir lider satırı ve bir ok içeren çok satırlı bir metin kutusu ekler. Komutu başlatırken bir nesne veya bir alt eleman (yüz, kenar veya tepe) seçilirse, Etiket, konum, uzunluk, alan, hacim veya malzeme de dahil olmak üzere seçilen öğenin belirli bir niteliğini görüntülemek için yapılabilir.


</div>

If an object or a sub-element (face, edge or vertex) is selected when starting the command, the text can be made to display one or two attributes of the selected element, including position, length, area, volume and material. The text will then be linked to the attributes and will update if their values change.


<div class="mw-translate-fuzzy">

Oksuz daha basit bir metin elemanı eklemek için [Metin](Draft_Text/tr.md) kullanın. Düz metin şekilleri oluşturmak için [Şekil dizesi](Draft_ShapeString/tr.md) ile [Parça Çıkar](Part_Extrude/tr.md) kullanın.


</div>

<img alt="" src=images/Draft_Label_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


{{Caption | Farklı yönelimleri, ipucu sembolleri ve bilgileri içeren çeşitli etiketler}}


</div>



## Nasıl Kullanılır 

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  
    {{Button | <img src="images/_Draft_Label.png_" width= 16px> [Etiket](Draft_Label/tr.md)}}düğmesine basın veya {{KEY | D}} ardından {{KEY | L}} tuşlarına basın.

2.  3D görünümde bir ilk noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın. Bu nokta hedefi gösterir (ok başı). Bu herhangi bir yerde olabilir, bir unsur olması gerekmez.

3.  3D görünümünde ikinci bir noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın. Bu nokta yatay veya dikey bir liderin başlangıcını gösterir.

4.  3D görünümünde üçüncü bir noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın. Bu nokta metnin temel noktasını gösterir.


</div>



## Seçenekler

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   \"Özel\", \"Ad\", \"Etiket\", \"Konum\", \"Uzunluk\", \"Alan\", \"hacim\" dahil \"Görüntülenecek bilgi türünü seçmek için {{Button | Label type}} tıklayın. \"başlık\" ve \"Malzeme\" olarak etiketleyin.
-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında {{KEY | Enter}} tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basabilirsiniz.
-   Etiketi yerleştirirken, [ Yakalama](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak en yakın çıtçıt konumuna zorlamak için {{KEY | Ctrl}} tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için {{KEY | Esc}} veya {{button | Close}} tuşuna basınız.


</div>




<div class="mw-translate-fuzzy">

## Etiket türleri 


</div>

The following label types are available:


<div class="mw-translate-fuzzy">

-    {{Emphasis | Custom:}}, {{PropertyData | Custom Text}} içeriğini görüntüler.

-    {{Emphasis | Name:}}hedef nesnenin dahili adını görüntüler; iç ad, yaratılış zamanında nesneye atanır ve nesnenin varlığı boyunca sabit kalır.

-    {{Emphasis | Label:}}hedef nesnenin etiketini görüntüler; Nesnenin etiketi kullanıcı tarafından herhangi bir zamanda değiştirilebilir.

-    {{Emphasis | Position:}}, hedef nesnenin taban noktasının, hedef köşenin veya varsa, hedef alt öğenin kütle merkezinin koordinatlarını görüntüler.

-    {{Emphasis | Length:}}, varsa, hedef alt öğenin uzunluğunu gösterir.

-    {{Emphasis | Area:}}, eğer varsa, hedef alt öğenin alanını gösterir.

-    {{Emphasis | Volume:}}, eğer varsa, hedef nesnenin hacmini gösterir.

-    {{Emphasis | Tag:}}, örneğin [Mimari](Arch_Workbench/tr.md) ile oluşturulan nesneler gibi bir özelliğe sahipse, hedef nesnenin {{incode | Tag}} özniteliğini görüntüler.

-    {{Emphasis | Material:}}, hedef nesnenin böyle bir özelliği varsa, hedef nesnenin malzemesinin etiketini görüntüler.


</div>

## Notes


<div class="mw-translate-fuzzy">


{{emphasis | Not:}}

yatay düz parçanın yönü, sağa veya sola doğru, metni otomatik olarak ters yöne hizalar. Lider dikey olarak yukarı çıkarsa, metin sola hizalanır; dikey olarak aşağı inerse, sağa hizalanır.


</div>



## Özellikler

See also: [Property editor](Property_editor.md).

A Draft Label object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data


{{TitleProperty|Label}}


<div class="mw-translate-fuzzy">

### Veri

-    {{PropertyData | Label Type}}: bu etiket tarafından gösterilen bilgilerin türünü belirtir (aşağıya bakın).

-    {{PropertyData | Custom Text}}: {{PropertyData | Label Type}} \"Özel\" olarak ayarlandığında veya etiket parametrik olmadığında görüntülenecek metin bloğunu belirtir. Metin dizelerin bir listesi olarak verilmiştir; listedeki her öğe, virgülle ayrılmış olarak, yeni bir metin satırı belirtir.

-    {{PropertyData | Text}}: (salt okunur), {{PropertyData | Label Type}} \'e bağlı olarak etiket tarafından görüntülenen gerçek metni gösterir.

-    {{PropertyData | Target Point}}: liderin ipucunun konumunu belirtir.

-    {{PropertyData | Straight Direction}}: Liderin düz segmentinin yönünü yatay veya dikey olarak belirtir.

-    {{PropertyData | Straight Distance}}: metnin taban noktasından başlayarak satırın düz bölümünün uzunluğunu belirtir. Mesafe pozitifse, lider metnin sağ tarafından başlar ve metin sağa hizalanır; Aksi takdirde, lider metnin solundan başlar ve metin sola hizalanır.

-    {{PropertyData | Position}}: metin bloğunun ilk satırının taban noktasını belirtir; aynı zamanda liderin nasıl çizildiğini de etkiler.

-    {{PropertyData | Angle}}: metin bloğunun ilk satırının taban çizgisinin dönüşünü belirtir; ayrıca liderin nasıl çizileceğini de etkiler, çünkü artık yatay veya dikey olmayacaktır.

-    {{PropertyData | Axis}}: döndürme için kullanılacak ekseni belirtir.


</div>


{{TitleProperty|Leader}}

-    **Points|VectorList**: specifies the points of the leader.

-    **Straight Direction|Enumeration**: specifies the direction of the first leader segment: {{Value|Custom}}, {{Value|Horizontal}} or {{Value|Vertical}}.

-    **Straight Distance|Distance**: specifies the length of the first leader segment. Only used if **Straight Direction** is {{Value|Horizontal}} or {{Value|Vertical}}. If the distance is positive, the leader starts from the right side of the text and the text aligns to the right. Otherwise the leader starts from the left side of the text and the text aligns to the left.


{{TitleProperty|Target}}

-    **Target|LinkSub**: specifies the object and optional subelement the label is linked to.

-    **Target Point|Vector**: specifies the position of the tip of the leader, which is where the arrow is attached.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the label. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the label.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by the **Placement** of the label. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v1.0)</small> ).


{{TitleProperty|Graphics}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView | Metin Yazı Tipi}}: metni çizmek için kullanılacak yazı tipini belirtir. \"Arial\" gibi bir font adı, \"sans\", \"serif\" veya \"mono\" gibi bir varsayılan stil, \"Arial, Helvetica, sans\" gibi bir aile veya \"gibi bir stil içeren bir ad olabilir. Arial: \"Kalın. Belirtilen font sistemde bulunmuyorsa, bunun yerine genel olan kullanılır.

-    {{PropertyView | Text Size}}: metnin boyutunu belirtir. Etiket nesnesi ağaç görünümünde oluşturulmuşsa ancak 3D görünümünde hiçbir metin görünmüyorsa, metnin boyutunu görünene kadar artırın.

-    {{PropertyView | Text Alignment}}: metnin taban çizgisinin öncüye göre dikey olarak hizalanmasını belirtir. Üst, orta veya alt olabilir.

-    {{PropertyView | Text Color}}: Bir RGB demetindeki metnin rengini belirtir (R, G, B).

-    {{PropertyView | Line Width}}: liderin genişliğini belirtir.

-    {{PropertyView | Çizgi Rengi}}: liderin rengini belirtir.

-    {{PropertyView | Arrow Size}}: liderin ucunda görüntülenen sembolün boyutunu belirtir.

-    {{PropertyView | Arrow Type}}: liderin ucunda görüntülenen, nokta, daire, ok veya kene olabilecek sembolün türünü belirtir.

-    {{PropertyView | Frame}}: \"Dikdörtgen\" ise, metnin etrafına bir çerçeve çizer.

-    {{PropertyView | Line}}: `True` ise, lider satır görüntülenecektir; Aksi halde, sadece baştaki metin ve sembol gösterilecektir.

-    {{PropertyView | Display Mode}}: \"3B metin\" ise, metin başlangıçta XY düzleminde olacak şekilde sahne eksenlerine hizalanır; \"2B metin\" ise, metin her zaman kameraya dönük olacaktır.


</div>


{{TitleProperty|Text}}

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead. <small>(v1.0)</small> 

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small. <small>(v1.0)</small> 

-    **Justification|Enumeration**: specifies the horizontal alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}. Only used if **Straight Direction** is {{Value|Custom}}. Otherwise the horizontal alignment is based on the sign (positive or negative) of **Straight Distance**.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Max Chars|Integer**: specifies the maximum number of characters on each line of the text.

-    **Text Alignment|Enumeration**: specifies the vertical alignment of the text: {{value|Top}}, {{value|Middle}} or {{value|Bottom}}.

-    **Text Color|Color**: specifies the color of the text.

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Etiket aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
label = make_label(target_point=App.Vector(0, 0, 0),
                   placement=App.Vector(30, 30, 0),
                   target_object=None, subelements=None,
                   label_type="Custom", custom_text="Label",
                   direction="Horizontal", distance=-10,
                   points=None)
```

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
doc.recompute()

p1 = App.Vector(-200, 1000, 0)
place1 = App.Placement(App.Vector(-1000, 1300, 0), App.Rotation())

label1 = Draft.make_label(p1, place1, target_object=rectangle, distance=500, label_type="Label")
label1.ViewObject.TextSize = 200

p2 = App.Vector(-200, 0, 0)
place2 = App.Placement(App.Vector(-1000, -300, 0), App.Rotation())

label2 = Draft.make_label(p2, place2, target_object=rectangle, distance=500, label_type="Custom",
                          custom_text="Beware of the sharp edges")
label2.ViewObject.TextSize = 200

p3 = App.Vector(1000, 1200, 0)
place3 = App.Placement(App.Vector(2000, 1800, 0), App.Rotation())

label3 = Draft.make_label(p3, place3, target_object=rectangle, distance=-500, label_type="Area")
label3.ViewObject.TextSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label/tr
