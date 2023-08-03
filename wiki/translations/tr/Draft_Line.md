---
 GuiCommand:
   Name: Draft Line
   Name/tr: Çizgi
   MenuLocation: Taslak , Çizgi
   Workbenches: Draft_Workbench/tr, Arch_Workbench/tr
   Shortcut: **L** **I**
   Version: 0.7
   SeeAlso: Draft Wire/tr,Draft Point/tr
---

# Draft Line/tr


</div>

## Description


<div class="mw-translate-fuzzy">

## Tanım

Çizgi aracı, tanımlanan iki nokta arasına bir çizgi çizer. [Tepsi](Draft_Tray/tr.md) deki [Çizgi stili](Draft_Linestyle/tr.md) setini kullanır. Çizgi aracı, iki noktadan sonra durması dışında, [Tel](Draft_Wire/tr.md) aracı gibi davranır.


</div>

A Draft Line is in fact a [Draft Wire](Draft_Wire.md) with only two points.

<img alt="" src=images/Draft_Line_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Çizgi, iki noktayla oluşturulur*


</div>

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  
    **<img src="images/Draft_Line.svg" width=16px> [Çizgi](Draft_Line/tr.md)**düğmesine basın veya **L** ardından **I** tuşları.

2.  3D görünümde bir ilk noktaya tıklayın veya bir koordinat yazın ve **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basın.

3.  3D görünümünde ikinci bir noktaya tıklayın veya bir koordinat yazın ve **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basın.


</div>

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Seçenekler

-   Verilen eksendeki ikinci noktayı kısıtlamak için ilk noktadan sonra **X**, **Y** veya **Z** tuşlarına basın.

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın.
    -   Noktanın kutupsal koordinatlarını \"Uzunluk\" ve \"Açı\" değerlerini vererek de tanımlayabilirsiniz. İşaretçiyi belirtilen açıyla sınırlamak için \"Açı\" nın yanındaki onay kutusunu tıklayın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg" width=16px> Nokta ekle** düğmesine basabilirsiniz.

-   **Göreceli**moduna geçmek için **R** tuşuna basın veya onay kutusunu tıklayın. Göreceli mod açıksa, ikinci noktanın koordinatları birincisine göredir; değilse, kesindir, kökenlerinden alınır (0,0,0).

-   **Devam**moduna geçmek için **T** tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, ikinci nokta verdikten sonra Satır aracı yeniden başlatılır ve böylece araç düğmesine tekrar basmadan başka bir satır parçası çizmenize izin verir.

-   [snapping](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, en yakın çeki konumuna yönlendirmek için çizim yaparken **Ctrl** tuşunu basılı tutun.

-   İlk noktanıza göre ikinci noktanızı yatay veya dikey olarak [constrain](Draft_Constrain/tr.md) çizerken **Shift** tuşunu basılı tutun.

-    **Ctrl**\+ **Z** tuşuna basınız veya sonuncuyu geri almak için {{button|<img src="images/Draft_UndoLine.png" width=12px> Undo}} düğmesine basınız. puan.

-   Geçerli komutu iptal etmek için **Esc** veya **Close** düğmesine basınız.


</div>

## Notes


<div class="mw-translate-fuzzy">

Ağaç görünümündeki öğeye çift tıklayarak veya **<img src="images/_Draft_Edit.svg_" width= 16px> [Düzenle](Draft_Edit/tr.md)** düğmesine basılarak çizgi düzenlenebilir. Ardından noktaları yeni bir konuma getirebilirsiniz.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box: **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Line](Part_Line.md) instead of a Draft Line.

## Properties


<div class="mw-translate-fuzzy">

## Özellikler

Bir Çizgi nesnesi [tel](Draft_Wire/tr.md) \'deki tüm özellikleri paylaşır, ancak bu özelliklerin yalnızca bazıları Çizgi için geçerlidir.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Çizgi aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
line = make_line(p1, p2)
line = make_line(LineSegment)
line = make_line(Shape)
```

-   Her biri `p1` ve `p2` noktaları arasında, her biri {{incode | FreeCAD.Vector}} ile milimetre cinsinden birimler arasında tanımlanan bir `Line` nesnesi oluşturur.
-   Bir `Part.LineSegment` \'dan bir `Line` nesnesi oluşturur.
-   Verilen `Shape` \'nin ilk köşesinden son köşesine kadar bir `Line` nesnesi oluşturur.

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 500, 0)
p3 = App.Vector(-250, -500, 0)
p4 = App.Vector(500, 1000, 0)

line1 = Draft.make_line(p1, p2)
line2 = Draft.make_line(p3, p4)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Line/tr
