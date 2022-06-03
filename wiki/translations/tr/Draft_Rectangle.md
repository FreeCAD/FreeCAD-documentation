---
- GuiCommand   */tr
   Name   *Draft Rectangle
   Name/tr   *Dikdörtgen
   Workbenches   *[Taslak](Draft_Workbench/tr.md), [Mimari](Arch_Workbench/tr.md)
   MenuLocation   *Taslak → Dikdörtgen
   Shortcut   ***R** **E**
   Version/tr   *0.17
   SeeAlso   *[Elips](Draft_Ellipse/tr.md),[Parça Kutu](Part_Box/tr.md)
---

# Draft Rectangle/tr


</div>

## Description


<div class="mw-translate-fuzzy">

## Açıklama

Dikdörtgen aracı, geçerli belgede belirli bir noktaya bir dikdörtgen ekler. Taslak araç çubuğunda [Çizgi stili](Draft_Linestyle/tr.md) setini kullanır.


</div>

İsteğe bağlı olarak, dikdörtgenin her köşesine 45 derecelik bir pah veya dairesel bir fileto ekleyebilir ve dikdörtgeni eşit boyutlu satır ve sütunlardan oluşan bir diziye bölebilirsiniz.

<img alt="" src=images/Draft_Rectangle_example.jpg  style="width   *400px;">


<div class="mw-translate-fuzzy">


{{Caption | İki köşe noktası tarafından tanımlanan dikdörtgen}}


</div>

## Usage

See also   * [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  
    {{Button | <img src="images/_Draft_Rectangle.png_" width= 16px> [Dikdörtgen](Draft_Rectangle/tr.md)}}düğmesine basın veya {{KEY | R}} ardından {{KEY | E}} tuşları.

2.  3D görünümde bir ilk köşe noktasını tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın .

3.  3D görünümünde birincinin karşısındaki başka bir noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} tuşuna basın.

   *   İkinci nokta, X, Y veya Z eksenleriyle sınırlandırılmamalıdır, aksi takdirde elde edilen dikdörtgen yanlış biçimlendirilir.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Seçenekler

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında {{KEY | Enter}} tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basabilirsiniz.
-   **Göreceli** moduna geçmek için {{KEY | R}} tuşuna basın veya onay kutusunu tıklayın. Göreceli mod açıksa, ikinci noktanın koordinatları birincisine göredir; değilse, kesindir, kökenlerinden alınır (0,0,0).
-   **Devam** moduna geçmek için {{KEY | T}} tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, ikinci noktayı verdikten sonra Dikdörtgen aracı yeniden başlatılır, böylece araç düğmesine tekrar basmadan başka bir dikdörtgen çizebilirsiniz.
-   **Dolu** moduna geçmek için {{KEY | L}} tuşuna basın veya onay kutusunu tıklayın. Dolu modu açıksa, dikdörtgen dolgulu bir yüz oluşturur ({{PropertyData | Make Face}} `True`); değilse, dikdörtgen bir yüz oluşturmaz ({{PropertyData | Make Face}} `False`).
-   [Yakalama](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken {{KEY | Ctrl}} tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için {{KEY | Esc}} veya {{Button | Close}} düğmesine basınız.


</div>

## Notes


<div class="mw-translate-fuzzy">

Ağaç görünümündeki öğeye çift tıklayarak veya {{Button | <img src="images/_Draft_Edit.svg_" width= 16px> [Düzenle](Draft_Edit/tr.md)}} düğmesine basılarak dikdörtgen düzenlenebilir. Ardından noktaları yeni bir konuma getirebilirsiniz.


</div>

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates   * **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode   * **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Plane](Part_Plane.md) instead of a Draft Rectangle.

## Özellikler

See also   * [Property editor](Property_editor.md).

A Draft Rectangle object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Veri

-    {{PropertyData/tr|Length}}   * X ekseni yönündeki şeklin uzunluğunu belirtir.

-    {{PropertyData/tr|Height}}   * Y ekseni yönündeki şeklin yüksekliğini belirtir.

-    {{PropertyData/tr|Chamfer Size}}   * dikdörtgenin her bir köşesindeki 45 ° pahın diyagonal uzunluğunu belirtir.

-    {{PropertyData/tr|Fillet Radius}}   * dikdörtgenin her bir köşesindeki 90 ° \'lik fileto yarıçapını belirtir.

-    {{PropertyData/tr|Rows}}   * orijinal şeklin bölündüğü eşit boyutta satır sayısını belirtir; varsayılan olarak, 1 satır.

-    {{PropertyData/tr|Columns}}   * orijinal şeklin bölündüğü eşit boyutlu sütunların sayısını belirtir; varsayılan olarak, 1 sütun.

-    {{PropertyData/tr|Make Face}}   * şeklin bir yüz yapıp yapmamasını belirtir. Eğer `True` ise bir yüz yaratılır, aksi takdirde sadece çevre nesnenin bir parçası olarak kabul edilir.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView/tr|Pattern}}   * şeklin yüzünü doldurmak için bir [Desen](Draft_Pattern/tr.md) belirtir. Bu özellik yalnızca {{PropertyData/tr|Make Face}} `True` ise ve {{PropertyView/tr|Display Mode}} \"Düz Çizgiler\" ise çalışır.

-    {{PropertyView/tr|Pattern Size}}   * [Desen](Draft_Pattern/tr.md) \'in boyutunu belirtir.

-    {{PropertyView/tr|Texture Image}}   * şeklin yüzünde eşlenecek görüntü dosyasının yolunu belirtir. Bu özelliğin boşaltılması görüntüyü kaldıracak.

   *   Eşlemedeki çarpılmaları önlemek için dikdörtgen, görüntüyle aynı oranlara sahip olmalıdır.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.   ***

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Dikdörtgen aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve python konsolundan kullanılabilir   *


</div>


```python
rectangle = make_rectangle(length, height, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   X yönünde `length` ve Y yönünde `height`, milimetre cinsinden birimlerle `Rectangle` nesnesi oluşturur.
    -   Başka bir yerleşim belirtilmemişse uzunluk X eksenine paralel olacaktır.

-   Bir `placement` verilirse kullanılır; Aksi halde, şekil başlangıçta oluşturulur.

-    `face``True` ise, şekil bir yüz yapacaktır, yani dolu görünecektir.


</div>

Örnek   * 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle1 = Draft.make_rectangle(4000, 1000)
rectangle2 = Draft.make_rectangle(1000, 4000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 45))

rectangle3 = Draft.make_rectangle(3500, 250, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rectangle/tr
