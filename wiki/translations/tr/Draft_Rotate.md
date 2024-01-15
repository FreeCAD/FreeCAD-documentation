---
 GuiCommand:
   Name: Draft Rotate
   Name/tr: Döndür
   MenuLocation: Taslak , Döndür
   Workbenches: Draft_Workbench/tr, Arch_Workbench/tr
   Shortcut: **R** **O**
   SeeAlso: Draft Move/tr, Draft Array/tr
   Version: 0.17
---

# Draft Rotate/tr


</div>



## Tanım


<div class="mw-translate-fuzzy">

Döndürme aracı, seçilen nesneleri bir referans noktasının etrafındaki belirli bir açıyla döndürür veya kopyalar.


</div>


<div class="mw-translate-fuzzy">

Döndür aracı, [Taslak tezgahı](Draft_Workbench/tr.md) veya [Eskiz tezgahı](Sketcher_Workbench/tr.md) ile oluşturulan 2D şekillerde kullanılabilir, ancak [Parça tezgahı](Part_Workbench/tr.md) ve [Mimari tezgahı](Arch_Workbench/tr.md) ile oluşturulanlar gibi birçok 3D nesne üzerinde de kullanılabilir.


</div>

<img alt="" src=images/Draft_Rotate_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


{{Caption | Bir merkez referans noktası kullanarak bir nesneyi, bir referans açısından başka bir açıyla döndürme}}


</div>




<div class="mw-translate-fuzzy">

## Nasıl kullanılır 


</div>

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Taşımak veya kopyalamak istediğiniz nesneleri seçin.

2.  
    {{Button | <img src="images/_Draft_Rotate.svg_" width= 16px> [Döndür](Draft_Rotate/tr.md)}}düğmesine basın veya {{KEY | R}} ardından {{KEY | O}} tuşlarına basın. Hiçbir nesne seçilmezse, birini seçmeye davet edilirsiniz.

3.  3D görünümde bir ilk noktaya tıklayın veya bir koordinat yazın ve {{Button | <img src="images/_Draft_AddPoint.svg_" width= 16px> Nokta ekle}} düğmesine basın. Bu, işlemin dönme ekseninin geçeceği temel noktası olarak işlev görür.

4.  3D görünümünde ikinci bir noktaya tıklayın veya taban açısını yazın. Bu, ilk nokta etrafında dönecek bir taban çizgisini tanımlar.

5.  3D görünümünde üçüncü bir noktaya tıklayın veya bir dönüş açısı yazın. Bu, taban çizgisinin ve dolayısıyla nesnelerin dönmesini gösterir.


</div>



## Seçenekler

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts (for version 0.22).


<div class="mw-translate-fuzzy">

-   Verilen eksendeki bir sonraki noktayı sınırlamak için bir noktadan sonra **X**, **Y** veya **Z** tuşlarına basın.
-   Koordinatları manuel olarak girmek için sayıları girin, ardından her bir X, Y ve Z bileşeni arasında **Enter** tuşuna basın. Noktayı yerleştirmek istediğiniz değerleri aldığınızda **<img src="images/_Draft_AddPoint.svg" width=16px> add point** düğmesine basabilirsiniz.
-   **Devam**moduna geçmek için **T** tuşuna basın veya onay kutusunu tıklayın. Devam modu açıksa, işlemi tamamladıktan sonra Döndürme aracı yeniden başlatılır ve böylece araç düğmesine tekrar basmadan nesneleri döndürmenizi veya kopyalamanızı sağlar.
-   **Kopyalama**moduna geçmek için **P** tuşuna basın veya onay kutusunu tıklayın. Kopyalama modu açıksa, Döndürme aracı orijinal şeklini yerinde tutacaktır, ancak üçüncü noktada ayarlanan açıyla bir kopya oluşturur. : Sırayla birkaç kopya yerleştirmek için hem **T** hem de **P** kullanabilirsiniz. Bu durumda, kopyalanan öğe en son yerleştirilen kopyadır.
-   Kopyalama moduna geçmek için ikinci noktadan sonra **Alt** tuşunu basılı tutun. Üçüncü noktaya tıkladıktan sonra **Alt** tuşunu basılı tutmak, aynı döndürme temel noktasını ve taban çizgisini kullanarak kopya yerleştirmeye devam etmenizi sağlar; İşlemi bitirmek ve tüm kopyaları görmek için **Alt** tuşunu bırakın.
-   [snapping](Draft_Snap/tr.md) noktanızı mesafeden bağımsız olarak en yakın çeki konumuna zorlamak için dönerken **Ctrl** tuşunu basılı tutun.
-   Bir sonraki noktanızı dönme baz noktasına göre yatay veya dikey olarak [constrain](Draft_Constrain/tr.md) konumuna döndürürken **Shift** tuşunu basılı tutun.
-   Geçerli komutu iptal etmek için **Esc** veya {{button|Close}} tuşuna basınız; önceden yerleştirilmiş kopyalar kalacaktır.


</div>

## Notes

-   An Object that is [attached](Part_EditAttachment.md) cannot be rotated with the Draft Rotate command. To rotate it either its **Support** object has to be rotated, or its **Attachment Offset** has to be changed.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To reselect the base objects after copying objects: **Edit → Preferences... → Draft → General → Select base objects after copying**.

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Döndür aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve python konsolundan kullanılabilir:


</div>


```python
rotated_list = rotate(objectslist, angle, center=Vector(0,0,0), axis=Vector(0,0,1), copy=False)
```


<div class="mw-translate-fuzzy">

-    `objectlist`içindeki nesnelerin temel noktasını verilen `angle` ile döndürür.

    -   
        `objectlist`
        
        , tek bir nesne veya bir nesne listesidir.

    -   Bir dönme temel noktası (`center`) ve `axis` verilirse, bunlar kullanılır; Aksi taktirde rotasyon orijine ve Z ekseni etrafına dayanır. : Dönme açısı, nesnenin taban noktasına göredir, yani bir nesne 45 derece döndürülürse ve ardından bir başka 45 derece döndürülürse, orijinal konumundan toplam 90 derece döndürülür.

-    `copy`ise `True` ise orijinal nesneleri döndürmek yerine kopyalar oluşturulur.

-    `rotatedlist`, orijinal döndürülmüş nesnelerle veya yeni kopyalarla birlikte döndürülür.

    -   
        `rotatedlist`
        
        , `objectlist` girişine bağlı olarak tek bir nesne veya nesne listesidir.


</div>

Örnek:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=300)
Draft.move(polygon1, App.Vector(1000, 0, 0))

# Rotation around the origin
angle1 = 45
rot2 = Draft.rotate(polygon1, angle1, copy=True)
rot3 = Draft.rotate(polygon1, 2*angle1, copy=True)
rot4 = Draft.rotate(polygon1, 4*angle1, copy=True)

polygon2 = Draft.make_polygon(3, radius=1000)
polygon3 = Draft.make_polygon(5, radius=500)
Draft.move(polygon2, App.Vector(2000, 0, 0))
Draft.move(polygon3, App.Vector(2000, 0, 0))

# Rotation around another point
angle2 = 60
cen = App.Vector(3100, 0, 0)
list2 = [polygon2, polygon3]
rot_list2 = Draft.rotate(list2, angle2, center=cen, copy=True)
rot_list3 = Draft.rotate(list2, 2*angle2, center=cen, copy=True)
rot_list4 = Draft.rotate(list2, 4*angle2, center=cen, copy=True)

doc.recompute()
```


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Rotate/tr
