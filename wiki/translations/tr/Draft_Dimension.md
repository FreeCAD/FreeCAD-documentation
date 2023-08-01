---
- GuiCommand:/tr
   Name:Draft Dimension
   Name/tr:Boyut
   MenuLocation:Taslak → Boyut
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Mimari](Arch_Workbench/tr.md)
   Shortcut:**D** **I**
   Version:0.18
   SeeAlso:[FlipDimension](Draft_FlipDimension/tr.md),[Teknik resim](TechDraw_Workbench/tr.md)
---

# Draft Dimension/tr


</div>

## Description


<div class="mw-translate-fuzzy">

## Açıklama

Boyut aracı, iki nokta arasındaki mesafeyi ölçen ve görüntüleyen bir nesne oluşturur; üçüncü bir nokta, boyut çizgisinin konumunu belirtir.


</div>


<div class="mw-translate-fuzzy">

Araç, doğrudan katı gövdelere tutturulmuş kenarları veya çizgileri ölçebilir; Gövde değişirse, boyut kendini günceller. Araç ayrıca [Yay](Draft_Arc/tr.md) veya [Doldur](Part_Fillet/tr.md), [Eskiz Dolgu oluştur](Sketcher_CreateFillet/tr.md) ve [Prça tasarım Dolgu](PartDesign_Fillet/tr.md) işlemleri ile üretilenler gibi eğrilik çapını veya yarıçapını da ölçebilir.


</div>


<div class="mw-translate-fuzzy">

Ortaya çıkan boyut 3D görünümüne yerleştirilir ve bir Taslak nesnesi olarak kabul edilir. Bu nesne, [Teknik resim Yeni Eskiz](TechDraw_DraftView/tr.md) veya [Teknik resim Yeni Yay](TechDraw_ArchView/tr.md) araçlarını kullanarak [Teknik resim tezgahı](TechDraw_Workbench/tr.md) sayfasında görüntülenebilir. Bu araçlar teknik çizimler hazırlamak içindir, bu yüzden boyutları 3D çizimde değil, sadece çizim sayfasında oluştururlar.


</div>

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


{{Caption | Üç nokta tarafından tanımlanan boyut}}


</div>

## Create

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

### Usage linear dimension 


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  
    {{Button | <img src="images/_Draft_Dimension.png_" width= 16px> Taslak Boyut}}düğmesine basın veya {{KEY | D}} ardından {{KEY | I}} tuşları.

2.  3D görünümünde bir noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın.

3.  3D görünümünde ikinci bir noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın. İlk iki nokta ölçülen mesafeyi tanımlar.

4.  3D görünümünde üçte birini tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> |Nokta ekle}} düğmesine basın. Son nokta, ölçüm çizgisinin konumunu tanımlar.


</div>

### Usage radial dimension 

1.  Optionally select a circular edge in the [3D view](3D_view.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an edge do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a circular edge in the [3D view](3D_view.md).
    -   Hold down the **Alt** key, select a circular edge in the [3D view](3D_view.md) and release the **Alt** key.
5.  To position the dimension line do one of the following:
    -   For a diameter dimension:
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   For a radial dimension:
        -   Hold down the **Shift** key and pick a point in the [3D view](3D_view.md).

### Usage angular dimension 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
2.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a first straight edge in the [3D view](3D_view.md). Repeat this to select a second straight edge.
    -   Hold down the **Alt** key, select two straight edges in the [3D view](3D_view.md) and release the **Alt** key.
4.  To position the dimension arc pick a point in the [3D view](3D_view.md).
5.  The displayed angle depends on the edges and the picked point.

### Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Seçenekler

-   Verilen eksendeki bir sonraki noktayı sınırlamak için bir noktadan sonra {{KEY | X}}, {{KEY | Y}} veya {{KEY | Z}} tuşlarına basın.
-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında {{KEY | Enter}} tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basabilirsiniz.
-   **Göreceli** moduna geçmek için {{KEY | R}} tuşuna basın veya onay kutusunu tıklayın. Göreceli mod açıksa, bir sonraki noktanın koordinatları bir öncekine göredir; değilse, kesindir, Eksenden alınır (0,0,0).
-   **Devam** moduna geçmek için {{KEY | T}} tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, son noktayı verdikten sonra Boyut aracı yeniden başlatılır ve araç düğmesine tekrar basmadan başka bir boyut çizmenize izin verilir; Aşağıdaki boyutlar önceki boyutun son noktasından başlayacak ve aynı temel çizgiyi paylaşacaktır.
-   [ Yakalama](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken {{KEY | Ctrl}} tuşunu basılı tutun.
-   Bir önceki noktaya göre [ Kısıtlama](Draft_Constrain/tr.md) bir sonraki noktanızı yatay veya dikey olarak çizerken ve çap ve yarıçap modları arasında geçiş yapmak için {{KEY | Shift}} tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için {{KEY | Esc}} veya {{Button | Close}} düğmesine basın ve **devam** boyutlarını bitirin; önceden yerleştirilmiş boyutlar kalacaktır.


</div>

## Convert

### Usage

1.  Select one or more [Std MeasureDistance](Std_MeasureDistance.md) objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  Each selected object is replaced by a non-parametric linear Draft Dimension.

## Notes


<div class="mw-translate-fuzzy">

Boyut, ağaç görünümündeki öğeye çift tıklayarak veya {{Button | <img src="images/_Draft_Edit.svg_" width= 16px> [Taslak Düzenle](Draft_Edit/tr.md)}} düğmesine basarak düzenlenebilir. Ardından noktaları yeni bir konuma getirebilirsiniz.


</div>



## Özellikler

See also: [Property editor](Property_editor.md).

A Draft Dimension object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data linear and radial dimension 


{{TitleProperty|Dimension}}


<div class="mw-translate-fuzzy">

### Veri

-    {{PropertyData | Start}}: ölçülecek mesafenin başlangıç noktasını belirtir.

-    {{PropertyData | End}}: ölçülecek mesafenin bitiş noktasını belirtir.

-    {{PropertyData | Dimline}}: boyut çizgisinin geçmesi gereken bir noktayı belirtir.

-    {{PropertyData | Distance}}: (salt okunur) ölçülen uzunluğu belirtir.

-    {{PropertyData | Diameter}}: `True` ise, bir çap boyutu görüntüler; aksi takdirde bir yarıçap boyutu görüntüler; Bu özellik yalnızca boyut dairesel bir yaya bağlıysa çalışır.


</div>


{{TitleProperty|Linear/radial dimension}}

-    **Direction|Vector**: specifies the direction of the measurement.

-    **Distance|Length**: (read-only) specifies the value of the measurement.

-    **End|VectorDistance**: specifies the end point of the measurement.

-    **Start|VectorDistance**: specifies the start point of the measurement.


{{TitleProperty|Radial dimension}}

-    **Diameter|Bool**: specifies if a radial dimension is displayed as a diameter dimension. If it changed the symbol used in **Override** must be updated manually (from {{Value|Ø}} to {{Value|R}} or vice versa). Not used for linear dimensions.

### Data angular dimension 


{{TitleProperty|Angular dimension}}

-    **Angle|Angle**: (read-only) specifies the value of the measurement.

-    **Center|VectorDistance**: specifies the center of the measurement.

-    **First Angle|Angle**: specifies the start angle of the measurement.

-    **Last Angle|Angle**: specifies the end angle of the measurement.


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension arc passes.

-    **Linked Geometry|LinkSubList|hidden**: not used.

-    **Normal|Vector|hidden**: specifies the normal of the plane of the dimension.

-    **Support|Link|hidden**: not used.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the dimension. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the dimension.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by the **Normal** of the measurement. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v0.21)</small> ).


{{TitleProperty|Graphics}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView | Ext Lines}}: Ölçüm noktalarından boyut çizgisine giden uzatma hatlarının maksimum uzunluğunu belirtir.

-    {{PropertyView | Ext Overshoot}}: uzantı çizgilerinin boyut çizgisinin ötesindeki ek uzunluğunu belirtir.

-    {{PropertyView | Dim Overshoot}}: boyut çizgisine eklenen ilave uzunluğu belirtir.

* {{PropertyView | Arrow Size}}: boyut çizgisinin sonunda görüntülenen sembolün boyutunu belirtir. 

-    {{PropertyView | Arrow Type}}: \"Çizgi\", \"Daire\", \"Ok\" veya \"Tik\" olabilen, boyut çizgisinin sonunda görüntülenen sembolün türünü belirtir.

-    {{PropertyView | Flip Arrows}}: sembollerin boyut çizgisinin uçlarında çevrilip çevrilmeyeceğini belirtir; sadece bu semboller ok ise işe yarar.

-    {{PropertyView | Font Name}}: metni çizmek için kullanılacak fontu belirtir. \"Arial\" gibi bir font adı, \"sans\", \"serif\" veya \"mono\" gibi bir varsayılan stil, \"Arial, Helvetica, sans\" gibi bir aile veya \"gibi bir stil içeren bir ad olabilir. Arial: \"Kalın. Belirtilen font sistemde bulunmuyorsa, bunun yerine genel olan kullanılır.

-    {{PropertyView | Font Size}}: harflerin boyutunu belirtir. Boyut nesnesi ağaç görünümünde oluşturulmuşsa ancak metin görünmüyorsa, görünene kadar metnin boyutunu artırın.

-    {{PropertyView | Flip Text}}: ölçümü gösteren metnin yönünün çevrilip çevrilmeyeceğini belirtir.

-    {{PropertyView | Text Position}}: orijine (0,0,0) atıfta bulunulan metnin mutlak koordinatlardaki konumunu belirtir; metni boyut çizgisinin yanında görüntülemek için bu özelliği varsayılan değerinde (0,0,0) bırakın.

-    {{PropertyView | Text Spacing}}: Metin ve boyut çizgisi arasındaki boşluğu belirtir.

-    {{PropertyView | Override}}: gerçek ölçüm yerine görüntülenecek özel bir metin belirtir. Ölçüm değerini görüntülemek için metnin içindeki {{incode | $ dim}} dizesini kullanın.

-    {{PropertyView | Decimals}}: ölçümde görüntülenecek ondalık basamak sayısını belirtir.

-    {{PropertyView | Show Unit}}: `True` ise, birim ölçümün sayısal değerinin yanında görüntülenir.

-    {{PropertyView | Unit Override}}: ölçümü \"örneğin\" km \",\" m \",\" cm \",\" mm \",\" mi \",\" ft \",\" in \"olarak ifade edeceği bir birim belirtir. ; varsayılan birimleri kullanmak için bu özelliği boş bırakın. {{Version/tr | 0.17}}


</div>


{{TitleProperty|Text}}

-    **Flip Text|Bool**: specifies whether to flip the orientation of the text.

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Override|String**: specifies a custom text to display instead of the actual measurement. Use the string {{value|$dim}} inside the text to include the measurement.

-    **Text Color|Color**: specifies the color of the text. <small>(v0.21)</small> 

-    **Text Position|VectorDistance**: specifies the position of the text in absolute coordinates. {{Value|[0, 0, 0]}} will display the text in its default position near the dimension line or arc.

-    **Text Spacing|Length**: specifies the space between the text and the dimension line or arc.


{{TitleProperty|Units}}

-    **Decimals|Integer**: specifies the number of decimal places to display for the measurement.

-    **Show Unit|Bool**: specifies whether to display the unit next to the numerical value of the measurement. Not used for angular dimensions.

-    **Unit Override|String**: specifies the unit in which to express the measurement, for example, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} or {{value|arch}} for arch units. Leave this blank to use the default unit. Not used for angular dimensions.

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Boyut aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```


<div class="mw-translate-fuzzy">

Kendisine iletilen argümanlara bağlı olarak, bu işlevi çağırmanın çeşitli yolları vardır:


</div>


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```


<div class="mw-translate-fuzzy">

-    {{incode | p1}}ve {{incode | p2}} noktaları arasındaki mesafeyi ölçerek doğrusal bir {{incode | Dimension}} oluşturur.

-    {{incode | object}}\'a bağlı, {{incode | i1}} ve {{incode | i2}} endeksli köşeleri arasındaki mesafeyi ölçen doğrusal bir {{incode | Dimension}} oluşturur.

-    {{incode | object}}\'a bağlı, {{incode | i1}}, ölçülecek eğri kenarının dizini ve {{incode | mode}} ya { Boyut türünü belirtmek için {incode \| \"radius\"}} veya {{incode | "çap"}}.

    -   İlk aramada {{incode | p3}} ve diğer ikisinde de {{incode | p4}}, boyut çizgisinin geçmesi gereken isteğe bağlı bir nokta belirtin.
    -   Tüm noktalar {{incode | FreeCAD.Vector}} ile tanımlanır.


</div>


<div class="mw-translate-fuzzy">

Açısal bir boyut oluşturmak için aşağıdaki işlevi kullanın:


</div>


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```


<div class="mw-translate-fuzzy">

-   Verilen {{incode | center}} noktasından, iki öğeli {{incode | angles}} listesinden ve arkasından gelen {{incode | p3}} noktasından açısal bir {{incode | Dimension}} oluşturur. gitmelisin.
    -   Eğer {{incode | angle1> angle2}} ise, görüntülenen açı {{incode | angle1 - angle2}} farkıdır; Aksi halde, ek açı gösterilir {{incode | 360 - (angle2 - angle1)}}.
    -   Açıları radyan cinsinden verilmelidir; {{incode | math.radians ()}} işlevi, derece olarak verilen açıları dönüştürmek için kullanılabilir.


</div>


<div class="mw-translate-fuzzy">


{{incode | Dimension}}

görünüm özellikleri niteliklerinin üzerine yazılarak değiştirilebilir; örneğin, {{incode | ViewObject.FontSize}} üzerine, yeni boyutun milimetre cinsinden üzerine yazın.


</div>

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension/tr
