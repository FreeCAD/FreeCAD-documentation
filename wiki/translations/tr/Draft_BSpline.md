---
- GuiCommand:/tr
   Name:Draft BSpline
   Name/tr:BSpline
   MenuLocation:Taslak → BSpline
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Yapı](Arch_Workbench/tr.md)
   Shortcut:**B** **S**
   Version:0.7
   SeeAlso:[Tel](Draft_Wire/tr.md),[Bezier eğrisi](Draft_BezCurve/tr.md)
---

# Draft BSpline/tr

## Description


<div class="mw-translate-fuzzy">

## Açıklama

BSpline aracı, mevcut _ \'de ayarlanan [Çizgi stili](Draft_Linestyle/tr.md) alır.


</div>


<div class="mw-translate-fuzzy">

BSpline aracı, eğrinin geçeceği noktaları belirtir; Öte yandan, [Bezier eğrisi](Draft_BezCurve/tr.md) aracı, eğrinin yönünü tanımlamak için {{Emphasis | control points}} kullanır. Tam dairesel veya eliptik eğriler oluşturmak için, [Yay](Draft_Arc/tr.md) ve [Elips](Draft_Ellipse/tr.md) kullanın.


</div>

<img alt="" src=images/Draft_bspline_example.jpg  style="width:400px;"> 
*Spline birçok noktayla tanımlanır*

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  
    {{Button | <img src="images/_Draft_BSpline.png_" width= 16px> [BSpline](Draft_BSpline/tr.md)}}düğmesine basın veya {{KEY | B}} ardından {{KEY | S}} tuşuna basın

2.  3D görünümde bir ilk noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} tuşuna basın.

3.  3D görünümünde ek noktalara tıklayın veya bir koordinate yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın.

4.  Basımı tamamlamak için {{KEY | Esc}} veya {{Button | Kapat}} tuşuna basınız.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Seçenekler

-   Spline\'ı açık bırakmak için **A** veya **<img src="images/_Draft_FinishLine.png" width=12px> Çizgiyi bitir** düğmesine basın.

-    **O**ya veya **<img src="images/Draft_CloseLine.png" width=12px> Çizgiyi kapat** Spline kapatmak için düğmelerine basın. Bir yüz oluşturmak için son noktadan ilkine bir eğri eklenecektir. Bir yüz oluşturmak için en az üç nokta gerekir.

-   Önceden yerleştirilmiş eğri parçalarını kaldırmak için **W** veya **<img src="images/_Draft_Wipe.svg" width=12px> Kaldır** düğmesine basın, ancak spline\'ı son noktadan düzenlemeye devam edin.

-   Geçerli çalışma düzlemini en son yönde ayarlamak için **U** veya **<img src="images/_Draft_SelectPlane.svg" width=12px> [Set WP](Draft_SelectPlane/tr.md)** düğmesine basın puan.

-   Verilen eksendeki bir sonraki noktayı sınırlamak için bir noktadan sonra **X**, **Y** veya **Z** tuşlarına basın.

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basabilirsiniz.

-   **Göreceli**moduna geçmek için **R** tuşuna basın veya onay kutusunu tıklayın. Göreceli mod açıksa, bir sonraki noktanın koordinatları sonuncusuna göre değişir; değilse, kesindir, kökenlerinden alınır (0,0,0).

-   **Devam** moduna geçmek için **T** tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, spline\'ı bitirdikten sonra BSpline aracı yeniden başlatılır ve alet düğmesine tekrar basmadan bir tane daha çizmenize olanak sağlar.

-   **Dolu** moduna geçmek için **L** tuşuna basın veya onay kutusunu tıklayın. Dolu mod açıksa, kapalı bir eğri dolu bir yüz oluşturur ({{PropertyData/tr|Yüz yapmak}} `True`); Aksi halde, kapalı spline bir surat yapmaz ({{PropertyData/tr|Yüz yapmak}} `False`).

:   
    **Note:**Spline uygun bir yüz oluşturmayacağından kendisiyle kesiştiği takdirde doldurulmamalıdır. Spline doldurulur ancak şekli görünmüyorsa, spline\'ı görmek için {{PropertyData/tr|Yüz yapmak}} \'i `False`\' e manuel olarak ayarlayın.

-   [snapping](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken **Ctrl** tuşunu basılı tutun.
-   Bir sonraki noktanızı yatay veya dikey olarak son noktaya göre [sınırlamak](Draft_Constrain/tr.md) çizerken **Shift** tuşunu basılı tutun.
-   Son noktayı geri almak için **Ctrl** **Z** tuşuna basınız veya **<img src="images/Draft_UndoLine.png" width=12px> Geri alma** düğmesine basınız. .
-   Geçerli komutu iptal etmek için **Esc** veya **Close** tuşuna basınız; Önceden yerleştirilmiş eğri parçaları kalacaktır.


</div>

## Notes


<div class="mw-translate-fuzzy">

BSpline aracı [Tel](Draft_Wire/tr.md) aracı gibi davranır, ancak bölümlerinin her biri düz bir çizgi yerine eğridir. Birini diğerine dönüştürmek için [Telden BSpline çevir](Draft_WireToBSpline/tr.md) kullanın.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Özellikler

See also: [Property editor](Property_editor.md).

A Draft BSpline object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Veri

-    {{PropertyData/tr|Closed}}: Spline\'ın kapalı olup olmadığını belirtir. Spline başlangıçta açıksa, bu değer `False`; `True` olarak ayarlamak, spline\'ı kapatmak için bir eğri parçası çizecektir. Spline başlangıçta kapatılırsa, bu değer `True`; `False` olarak ayarlamak, son eğri parçasını kaldıracak ve spline\'ı açacaktır.

-    {{PropertyData/tr|Make Face}}: Spline\'ın bir surat yapıp yapmayacağını belirtir. Eğer `True` ise bir yüz yaratılır, aksi takdirde sadece çevre nesnenin bir parçası olarak kabul edilir. Bu özellik yalnızca {{PropertyData/tr|Closed}} `True` ise çalışır. : **Not:**, eğer spline uygun bir yüz oluşturmayacağından kendisiyle kesiştiğinde {{PropertyData/tr|Make Face}} ayarını `True` olarak ayarlamayın.

-    {{PropertyData/tr|Parameterization}}: BSpline\'ın şeklini etkiler.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Görünüm

-    {{PropertyView/tr|Arrow Size}}: spline sonunda görüntülenen sembolün boyutunu belirtir.

-    {{PropertyView/tr|Arrow Type}}: spline sonunda \"Dot\", \"Circle\", \"Arrow\" veya \"Tick\" olabilen sembol tipini belirtir.

-    {{PropertyView/tr|End Arrow}}: Spline\'ın son noktasında bir sembol gösterilip gösterilmeyeceğini belirtir, böylece bir açıklama satırı olarak kullanılabilir.

-    {{PropertyView/tr|Pattern}}: kapalı bir spline\'ın yüzünü doldurmak için bir [Draft Pattern](Draft_Pattern.md) belirtir. Bu özellik yalnızca {{PropertyData/tr|Make Face}} `True` ise ve {{PropertyView/tr|Display Mode}} \"Düz Çizgiler\" ise çalışır.

-    {{PropertyView/tr|Pattern Size}}: [Taslak Deseni](Draft_Pattern/tr.md) \'nin boyutunu belirtir.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

BSpline aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
bspline = make_bspline(pointslist, closed=False, placement=None, face=None, support=None)
bspline = make_bspline(Part.Wire, closed=False, placement=None, face=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Belirtilen nokta listesinden bir `BSpline` nesnesi oluşturur, `pointslist`.
    -   Listedeki her nokta, `FreeCAD.Vector` ile tanımlanır ve birim milimetre cinsinden tanımlanır.
    -   Alternatif olarak, giriş, noktaların çıkarıldığı bir `Part.Wire` olabilir.

-    `closed``True` ise veya ilk ve son noktalar aynıysa, tel kapanır.

-   Bir `placement` verilirse kullanılır; Aksi halde, şekil başlangıçta oluşturulur.

-   Eğer `face` `True` ise ve spline kapalıysa, spline bir yüz çizer, yani dolu görünür.


</div>


<div class="mw-translate-fuzzy">

Örnek:


</div>


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)

spline1 = Draft.make_bspline([p1, p2, p3], closed=False)
spline2 = Draft.make_bspline([p1, 2*p3, 1.3*p2], closed=False)
spline3 = Draft.make_bspline([1.3*p3, p1, -1.7*p2], closed=False)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BSpline/tr
