---
- GuiCommand:/tr
   Name:Draft Move
   Name/tr:Taşı
   MenuLocation:Taslak → Taşı
   Workbenches:[Taslak](Draft_Workbench/tr.md), [Yapı](Arch_Workbench/tr.md)
   Shortcut:**M** **V**
   SeeAlso:[Dizi](Draft_Array/tr.md), [Yol dizisi](Draft_PathArray/tr.md)
   Version:0.7
---

# Draft Move/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

Taşı aracı, seçilen nesneleri bir noktadan diğerine taşır veya kopyalar.


</div>


<div class="mw-translate-fuzzy">

Taşı aracı, [Taslak tezgahı](Draft_Workbench/tr.md) veya [Eskiz tezgahı](Sketcher_Workbench/tr.md) ile oluşturulan 2D şekillerde kullanılabilir, ancak [Parça tezgahı](Part_Workbench/tr.md) ve [Yapı tezgahı](Arch_Tezgahı/tr.md) ile oluşturulanlar gibi birçok 3D nesne üzerinde de kullanılabilir.


</div>

<img alt="" src=images/Draft_Move_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


{{Caption | Bir nesneyi bir noktadan diğer bir noktaya taşıma}}


</div>

## Nasıl kullanılır 

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Taşımak veya kopyalamak istediğiniz nesneleri seçin.

2.  
    {{Button | <img src="images/_Draft_Move.svg_" width= 16px> [Taşı](Draft_Move/tr.md)}}düğmesine basın veya {{KEY | M}} ardından {{KEY | V}} tuşlarına basın. Hiçbir nesne seçilmezse, birini seçmeye davet edilirsiniz.

3.  3B görünümde bir ilk noktaya tıklayın veya bir [ koordinat](Draft_Coordinates/tr.md) yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> [ Nokta ekle](Draft_AddPoint/tr_.md)}} düğmesine basın. Bu işlemin temel noktası olarak görev yapar.

4.  3B görünümünde başka bir noktaya tıklayın veya bir [ koordinat](Draft_Coordinates/tr.md) yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> [ Nokta](Draft_AddPoint_.md)}} düğmesine basın. Bu, temel noktadaki yeni konumdur.


</div>

## Seçenekler

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

-   Verilen eksendeki bir sonraki noktayı sınırlamak için bir noktadan sonra {{KEY | X}}, {{KEY | Y}} veya {{KEY | Z}} tuşlarına basın.
-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında {{KEY | Enter}} tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> [ Nokta ekle](Draft_AddPoint_.md)}} düğmesine basabilirsiniz.
-   **Göreceli**moduna geçmek için {{KEY | R}} tuşuna basın veya onay kutusunu tıklayın. Göreceli mod açıksa, bir sonraki noktanın koordinatları sonuncusuna göre değişir; değilse, kesindir, kökenlerinden alınır (0,0,0).
-   **Devam**moduna geçmek için {{KEY | T}} tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, işlemi tamamladıktan sonra Taşı aracı yeniden başlatılır ve böylece araç düğmesine tekrar basmadan nesneleri yeniden taşımanıza veya kopyalamanıza olanak tanır.
-   **Kopyalama**moduna geçmek için {{KEY | P}} tuşuna basın veya onay kutusunu tıklayın. Kopyalama modu açıksa, Taşıma aracı orijinal şekli yerinde tutacak ancak ikinci noktada bir kopya oluşturacaktır. : Sırayla birkaç kopya yerleştirmek için hem {{KEY | T}} hem de {{KEY | P}} kullanabilirsiniz. Bu durumda, kopyalanan öğe en son yerleştirilen kopyadır.
-   Kopyalama moduna geçmek için ilk noktadan sonra {{KEY | Alt}} tuşunu basılı tutun. İkinci noktaya tıkladıktan sonra {{KEY | Alt}} tuşunun basılı tutulması kopya yerleştirmeye devam etmenizi sağlayacaktır; İşlemi bitirmek ve tüm kopyaları görmek için {{KEY | Alt}} tuşunu bırakın.
-   [ snapping](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak, [ snapping](Draft_Snap.md) noktasını zorlamak için hareket ederken {{KEY | Ctrl}} tuşunu basılı tutun.
-   Bir sonraki noktanızı yatay veya dikey olarak sonuncuya göre [ constrain](Draft_Constrain/tr.md) konumuna getirirken {{KEY | Shift}} tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için {{KEY | Esc}} veya {{button | Close}} tuşuna basınız; önceden yerleştirilmiş kopyalar kalacaktır.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be moved with the Draft Move command. To move it either its **Support** object has to be moved, or its **Attachment Offset** has to be changed.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates, lengths and angles: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial focus of the task panel to the **Length** input box: **Edit → Preferences... → Draft → General settings → Draft tools options → Set focus on Length instead of X coordinate**. Note that you must move the pointer in the [3D view](3D_view.md) for the change to take effect.
-   To store and reuse the same copy mode setting across commands: **Edit → Preferences... → Draft → General settings → Draft tools options → Global copy mode**.
-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General settings → Draft tools options → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Taşı aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


```python
moved_list = move(objectslist, vector, copy=False)
```


<div class="mw-translate-fuzzy">

-    {{incode | objectslist}}içindeki nesnelerin temel noktasını {{incode | vector}} ile gösterilen yer değiştirme ve yönlere göre hareket ettirir.

    -   
        {{incode | objectslist}}
        
        , tek bir nesne veya bir nesne listesidir. : Yer değiştirme vektörü, nesnenin temel noktasına göredir, yani bir nesne 2 birim ve sonra başka bir 2 birim hareket ettirilirse, toplamda 4 birim orijinal konumundan hareket etmiş olur.

-    {{incode | copy}}ise {{incode | True}} ise orijinal nesneleri taşımak yerine kopyalar oluşturulur.

-    {{incode | movedlist}}, orijinal taşınan nesnelerle veya yeni kopyalarla birlikte döndürülür. \*\* {{incode | movedlist}}, {{incode | objectslist}} girişine bağlı olarak tek bir nesne veya nesne listesidir.


</div>

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(5, radius=1000)
polygon2 = Draft.make_polygon(3, radius=500)
polygon3 = Draft.make_polygon(6, radius=220)

Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon1, App.Vector(500, 500, 0))
Draft.move(polygon2, App.Vector(1000, -1000, 0))
Draft.move(polygon3, App.Vector(-500, -500, 0))

list1 = [polygon1, polygon2, polygon3]

vector = App.Vector(-2000, -2000, 0)
list2 = Draft.move(list1, vector, copy=True)
list3 = Draft.move(list1, -2*vector, copy=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Move/tr
