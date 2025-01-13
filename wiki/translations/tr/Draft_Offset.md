---
 GuiCommand:
   Name: Draft Offset
   Name/tr: Ofsetle
   MenuLocation: Taslak , Ofsetle
   Workbenches: Draft_Workbench/tr, Arch_Workbench/tr
   Shortcut: **O** **S**
   SeeAlso: Part_Offset2D/tr
---

# Draft Offset/tr


</div>



## Tanım


<div class="mw-translate-fuzzy">

Ofset aracı seçilen nesneyi kendisine dik verilen belirli bir mesafeye (ofset) hareket ettirir.


</div>

<img alt="" src=images/Draft_Offset_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


{{Caption | Bir teli kenarlarından birinden belirli bir mesafeye kaydırmak}}


</div>




<div class="mw-translate-fuzzy">

## Nasıl Kullanılır 


</div>

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Offset yapmak istediğiniz nesneyi seçin.

2.  
    {{Button | <img src="images/_Draft_Offset.png_" width= 16px> [Ofset](Draft_Offset/tr.md)}}düğmesine basın veya {{KEY | O}} ardından {{KEY | S}} tuşlarına basın. Hiçbir nesne seçilmezse, birini seçmeye davet edilirsiniz.

3.  3D görünümde bir noktaya tıklayın veya bir mesafe yazın.


</div>



## Seçenekler

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts (for version 1.0).


<div class="mw-translate-fuzzy">

-   **Kopyalama**moduna geçmek için {{KEY | P}} tuşuna basın veya onay kutusunu tıklayın. Kopyalama modu açıksa, Ofset aracı orijinal şekli yerinde tutar, ancak seçilen noktada ölçeklendirilmiş bir kopya oluşturur.
-   Aynı zamanda geçiş modunu değiştirecek noktayı seçerken {{KEY | Alt}} tuşunu basılı tutun. {{KEY | Alt}} tuşuna basılı tutmak, ofset kopya yerleştirmeye devam etmenizi sağlar; İşlemi tamamlamak ve tüm ofset şekillerini görmek için {{KEY | Alt}} tuşunu serbest bırakın.
-   **OCC** moduna geçmek için \"OCC stili\" onay kutusunu tıklayın. Bu, segmentlerin uçlarında yuvarlatılmış kenarlarla özel olarak kapalı bir şekil üretecek olan bir çizgi parçasının her iki tarafından bir denge oluşturacaktır.

:   
    {{Emphasis | Note:}}Bu stilde orijinal bölümler kaldırılacak, bu nedenle orijinal kenarları korumak için kopyalama modunu kullanın.

-   [ snapping](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak en yakın çeki konumuna zorlamak için ofset yaparken {{KEY | Ctrl}} tuşunu basılı tutun.
-   Geçerli segment için belirtilen uzaklık mesafesini korumak için {{KEY | Shift}} tuşunu basılı tutun ve başka bir referans seçmekten kaçının.
-   Geçerli komutu iptal etmek için {{KEY | Esc}} veya {{button | Close}} tuşuna basınız; önceden yerleştirilmiş ofset kopyalar kalacaktır.


</div>

## Notes

-   To create an offset version of a [Draft BSpline](Draft_BSpline.md) its points are offset individually, and from the new points a new spline is calculated. This new spline is not parallel to the original spline. For an exact parallel offset of a [Draft BSpline](Draft_BSpline.md) the [Part Offset2D](Part_Offset2D.md) command should be used.
-   The Draft Offset command cannot handle [Draft BezCurves](Draft_BezCurve.md). Use the [Part Offset2D](Part_Offset2D.md) command instead.

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Ofset aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve python konsolundan kullanılabilir:


</div>


```python
offset_obj = offset(obj, delta, copy=False, bind=False, sym=False, occ=False)
```


<div class="mw-translate-fuzzy">

-   Vektör olarak tanımlanan verilen {{incode | delta}} verilen {{incode | delta}} telini ilk köşesine uygulayarak ofsetler.

-    {{incode | copy}}{{incode | True}} ise, orijinal nesneyi dengelemek yerine başka bir nesne oluşturulur.

-   Eğer {{incode | bind}} {{incode | True}} ise ve tel nesnesinin açık olması şartıyla, orijinal ve ofset tel uç noktalarına bağlanarak bir yüz oluşturacaklardır.
    -   Eğer {{incode | sym}} {{incode | True}} ise, {{incode | bind}} de {{incode | True}} olmalı ve ofset telin her iki tarafında da yapılmalı, toplam genişlik verilen vektörün uzunluğudur.

-    {{incode | occ}}{{incode | True}} ise, OCC stili ofsetini kullanacaktır: her iki taraftan ofset yapacak, sonra yeni telleri birbirine bağlayacak ve köşeleri yuvarlayacaktır.

-    {{incode | Offsetobj}}orijinal ofset nesnesiyle veya yeni kopyayla döndürülür.


</div>

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1500, 2000, 0)
p3 = App.Vector(4000, 0, 0)

wire = Draft.make_wire([p1, p2, p3])
doc.recompute()

vector = App.Vector(-200, 150, 0)
offset1 = Draft.offset(wire, vector, copy=True, bind=True, sym=True)
offset2 = Draft.offset(wire, 3*vector, copy=True)
offset3 = Draft.offset(wire, 6*vector, copy=True)
offset4 = Draft.offset(wire, 9*vector, copy=True)
offset5 = Draft.offset(wire, 1.5*vector, copy=True, occ=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Offset/tr
