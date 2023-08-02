---
- GuiCommand:
   Name: Draft Ellipse
   Name/tr: Elips
   MenuLocation: Taslak -> Elips
   Workbenches: Draft_Workbench/tr, Arch_Workbench/tr
   Shortcut: **E** **L**
   SeeAlso: Draft Circle/tr, Draft Arc/tr
   Version: 0.7
---

# Draft Ellipse/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

Elips aracı, elipsin sığacağı dikdörtgen bir kutunun köşesini tanımlayarak iki nokta girerek mevcut [Çalışma düzlemi](Draft_SelectPlane/tr.md) içinde bir elips oluşturur. [Taslak Tepsi](Draft_Tray/tr.md) Görevler sekmesinde önceden ayarlanmış olan [Çizgi stili](Draft_Linestyle/tr.md) alır.


</div>


<div class="mw-translate-fuzzy">

Bu araç, başlangıç ve bitiş açılarını belirleyerek eliptik yaylar oluşturmak için de kullanılabilir. Çember ve dairesel yaylar oluşturmak için [Çember](Draft_Circle/tr.md) ve [Yay](Draft_Arc/tr.md) araçlarını kullanın. [BSpline](Draft_BSpline/tr.md) ve [Bezier eğrisi](Draft_BezCurve/tr.md) araçlarını kullanarak da bir eliptik veya dairesel yay yaklaştırabilirsiniz.


</div>

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


{{Caption | Dikdörtgen köşeleri tarafından tanımlanan elips}}


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  
    {{Button | <img src="images/_Draft_Ellipse.png_" width= 16px> [ Elips](Draft_Ellipse/tr.md)}}düğmesine basın veya {{KEY | E}} ardından {{KEY | L}} tuşları.

2.  3d görünümde bir ilk noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın.

3.  3D görünümünde ikinci bir noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın.


</div>

## Seçenekler

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basabilirsiniz.
-   **Göreceli**moduna geçmek için **R** tuşuna basın veya onay kutusunu tıklayın. Göreceli mod açıksa, ikinci noktanın koordinatları birincisine göredir; değilse, kesindir, kökenlerinden alınır (0,0,0).
-   **Devam**moduna geçmek için **T** tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, Elips aracı şekli tamamladıktan sonra yeniden başlatılır ve araç düğmesine tekrar basmadan bir tane daha çizmenize olanak sağlar.
-   **Dolu** moduna geçmek için **L** tuşuna basın veya onay kutusunu tıklayın. Dolu mod açıksa, elips dolu bir yüz oluşturur ({{PropertyData/tr|Make Face}} `True`); değilse, elips bir yüz oluşturmaz ({{PropertyData/tr|Make Face}} `False`).
-   [Yakalama](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken **Ctrl** tuşunu basılı tutun.
-   İlk noktanıza göre ikinci noktanızı yatay veya dikey olarak [Kısıtlama](Draft_Constrain/tr.md) çizerken **Shift** tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için **Esc** veya **Kapat** düğmesine basınız.


</div>

## Notes

-   A Draft Ellipse can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Ellipse](Part_Ellipse.md) instead of a Draft Ellipse.

## Özellikler

See also: [Property editor](Property_editor.md).

A Draft Ellipse object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Veri

-    {{PropertyData/tr|First Angle}}: elipsin ilk noktasının açısını belirtir; normalde 0°.

-    {{PropertyData/tr|Last Angle}}: elipsin son noktasının açısını belirtir; normalde 0°.

-    {{PropertyData/tr|Major Radius}}: elipsin ana yarıçapını belirtir.

-    {{PropertyData/tr|Minor Radius}}: elipsin küçük yarıçapını belirtir.

:   Her iki yarıçap da aynı değere sahipse, elips bir [Taslak Çember](Draft_Circle/tr.md) ile aynı görünür.

-    {{PropertyData/tr|Make Face}}: Elipsin bir yüz yapıp yapmayacağını belirtir. Eğer `True` ise bir yüz yaratılır, aksi takdirde sadece çevre nesnenin bir parçası olarak kabul edilir. Bu özellik, yalnızca şekil tam bir elips ise çalışır.

:   Tam bir elips olması için {{PropertyData/tr|First Angle}} ve {{PropertyData/tr|Last Angle}} aynı değere sahip olmalıdır; Aksi takdirde, eliptik bir yay görüntülenir. 0° ve 360° değerleri aynı olarak kabul edilir.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView/tr|Desen}}: şeklin yüzünü doldurmak için bir [Desen](Draft_Pattern/tr.md) belirtir. Bu özellik yalnızca {{PropertyData/tr|Yüz yapmak}} `True` ise ve {{PropertyView/tr|Ekran modu}} \"Düz Çizgiler\" ise çalışır.

-    {{PropertyView/tr|Desen boyutu}}: [Desen](Draft_Pattern/tr.md) \'inin boyutunu belirtir.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Elips aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```


<div class="mw-translate-fuzzy">

-   Milimetre cinsinden verilen büyük (`majradius`) ve küçük (`minradius`) yarıçapı ile bir `Ellipse` nesnesi oluşturur.
    -   Başka bir yerleşim yapılmazsa, büyük yarıçap (X ekseni) için daha büyük değer kullanılacaktır.
-   Bir `placement` verilirse kullanılır; Aksi halde, şekil başlangıçta oluşturulur.
-   Eğer `face` `True` ise, elips bir yüz yapacaktır, yani dolu görünecektir.


</div>

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Ellipse/tr
