---
- GuiCommand:/tr
   Name:Bezier eğrisi
   Name/tr:Bezier eğrisi
   MenuLocation:Taslak → Bezier eğrisi
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Yapı](Arch_Workbench/tr.md)
   Shortcut:B Z
   Version:0.14
---

# Draft BezCurve/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

Bezier eğrisi aracı, mevcut _ alır.


</div>


<div class="mw-translate-fuzzy">

Nesne, tek bir Bezier derece eğrisi olarak oluşturulur (nokta sayısı - 1). Bu, [Özellikler](Property/tr.md) kullanılarak yaratıldıktan sonra belirli bir dereceye kadar parçalı bir Bezier Eğrisi olarak değiştirilebilir. Bezier Eğrileri, {{KEY | <img src="images/_Draft_Edit.png_" width= 16px> [Düzenle](Draft_Edit/tr.md)}} kullanılarak düzenlenebilir.


</div>

The Draft BezCurve and the [Draft CubicBezCurve](Draft_CubicBezCurve.md) commands use **control points** to define the position and curvature of the spline. The [Draft BSpline](Draft_BSpline.md) command, on the other hand, specifies the **exact points** through which the curve will pass.

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;"> 
*Bézier curve defined by multiple points*


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_BezCurve_Example.png  style="width:400px;">

## Nasıl kullanılır 


</div>

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_BezCurve.svg" width=16px> [Draft BezCurve](Draft_BezCurve.md)** button.
    -   Select the **Drafting → Bézier tools → <img src="images/Draft_BezCurve.svg" width=16px> Bézier curve** option from the menu.
2.  The **Bézier curve** task panel opens. See [Options](#Options.md) for more information.
3.  Pick the first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Pick additional points in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
5.  Press **Esc** or the **Close** button to finish the command.


<div class="mw-translate-fuzzy">

1.  
    {{KEY | <img src="images/_Draft_BezCurve.png_" width= 16px> [Bezier eğrisi](Draft_BezCurve/tr.md)}}düğmesine basın veya {{KEY | B}} ardından {{KEY | Z}} tuşlarına basın.

2.  3D görünümünde bir ilk noktaya tıklayın veya bir [ koordinat](Draft_Coordinates/tr.md) yazın

3.  3D görünümünde ek noktaya tıklayın veya bir [ koordinat](Draft_Coordinates/tr.md) yazın

4.  
    {{KEY | F}}veya {{KEY | C}} tuşuna basın veya son noktayı çift tıklayın veya eğriyi bitirmek ve kapatmak için ilk noktayı tıklayın.

## Seçenekler


</div>

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Spline\'ı bitirmek için {{KEY | F}} veya {{KEY | <img src="images/_Draft_FinishLine.png_" width= 12px> '''[Bitir](Draft_FinishLine_.md)'''}} düğmesine basın

-    {{KEY | C}}veya {{KEY | <img src="images/_Draft_CloseLine.png_" width= 12px> '''[Kapat](Draft_CloseLine/tr.md)'''}} düğmesine basın veya ilk noktaya tıklayın spline\'ı bitirin, ancak son nokta ile birincinin arasına son bir parça ekleyerek kapatın.

-   Verilen eksendeki bir sonraki noktayı sınırlamak için bir noktadan sonra {{KEY | X}}, {{KEY | Y}} veya {{KEY | Z}} tuşlarına basın.

-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında {{KEY | ENTER}} tuşuna basın.

-    {{KEY | R}}tuşuna basınız veya {{KEY | '''Göreceli'''}} düğmesini işaretlemek / işaretini kaldırmak için onay kutusuna tıklayınız. Göreceli mod açıksa, bir sonraki noktanın koordinatları da öncekine göredir. Olmazsa, mutlaktırlar, (0,0,0) başlangıç ​​noktasından alınırlar.

-    {{KEY | T}}tuşuna basınız veya {{KEY | '''Devam et'''}} düğmesini işaretlemek / işaretini kaldırmak için onay kutusuna tıklayınız. Devam modu açıksa, Bezier eğrisi aracı, bitirdikten veya kapattıktan sonra yeniden başlatılır ve Bezier eğrisi düğmesine tekrar basmadan bir tane daha çizmenize olanak sağlar.

-   [ snapping](Draft_Snap/tr.md) noktasını mesafeden bağımsız olarak, noktanızı en yakın anlık konuma zorlamak için çizim yaparken {{KEY | CTRL}} tuşuna basın.

-   Bir sonraki noktanızı yatay veya dikey olarak son noktaya göre [ constrain](Draft_Constrain/tr.md) çizerken {{KEY | SHIFT}} tuşuna basın.

-   Mevcut segmentleri kaldırmak ve spline\'ı en sondan başlatmak için {{KEY | W}} tuşuna basınız veya {{KEY | <img src="images/_Draft_Wipe.png_" width= 12px> '''Uzat'''}} tuşuna basınız. puan.

-   Son noktayı geri almak için {{KEY | CTRL}} + {{KEY | Z}} tuşuna basın veya {{KEY | <img src="images/_Draft_UndoLine.png_" width= 12px> '''[ Geri al](Draft_UndoLine/tr.md)'''}} tuşuna basın .

-   Geçerli Bezier eğrisi komutunu iptal etmek için {{KEY | ESC}} veya {{KEY | '''İptal'''}} düğmesine basın.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Sınırlamalar

-   Bu araç FreeCAD 0.14 versiyonundan önce kullanılamaz
-   Nokta Özelliği henüz özellikler listesinde görünmüyor.
-   OpenCascade, derece \> 25 sahip Bezier Eğrisi\'ni desteklemiyor. Bu pratikte bir sorun olmamalıdır.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.

## Özellikler

See also: [Property editor](Property_editor.md).

A Draft BezCurve object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Area|Area**: (read-only) specifies the area of the face of the curve. The value will be {{value|0.0}} if **Make Face** if `False` or the face cannot be created.

-    **Closed|Bool**: specifies if the curve is closed or not. If the curve is initially open this value is `False`, setting it to `True` will draw a segment to close the curve. If the curve is initially closed this value is `True`, setting it to `False` will remove the last segment and make the curve open.

-    **Continuity|IntegerList**: (read-only) specifies the continuity of the curve.

-    **Degree|Integer**: specifies the degree of the curve.

-    **Length|Length**: (read-only) specifies the total length of the curve.

-    **Make Face|Bool**: specifies if the curve makes a face or not. If it is `True` a face is created, otherwise only the perimeter is considered part of the object. This property only works if **Closed** is `True` and if the curve does not self-intersect.

-    **Points|VectorList**: specifies the control points of the curve in its local coordinate system.

### View


{{TitleProperty|Draft}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the end of the curve.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the end of the curve, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **End Arrow|Bool**: specifies whether to show a symbol at the end of the curve, so it can be used as an annotation line.

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the face of the closed curve. This property only works if **Make Face** is `True` and if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Betik


</div>


<div class="mw-translate-fuzzy">

## Betik 

Bezier eğrisi aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve python konsolundan kullanılabilir:


</div>


```python
bezcurve = make_bezcurve(pointslist, closed=False, placement=None, face=None, support=None, degree=None)
bezcurve = make_bezcurve(Part.Wire, closed=False, placement=None, face=None, support=None, degree=None)
```


<div class="mw-translate-fuzzy">

-   Verilen vektör listesinden bir Bezier eğrisi nesnesi oluşturun. Bir nokta listesi yerine, bir Parça Teli de geçebilirsiniz.


</div>

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(2000, 0, 0)
p4 = App.Vector(1500, -2000, 0)

bezcurve1 = Draft.make_bezcurve([p1, p2, p3, p4], closed=True)
bezcurve2 = Draft.make_bezcurve([p4, 1.3*p2, p1, 4.1*p3], closed=True)
bezcurve3 = Draft.make_bezcurve([1.7*p3, 1.5*p4, 2.1*p2, p1], closed=True)

doc.recompute()
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft BezCurve/tr
