---
- GuiCommand:/tr
   Name:PartDesign ShapeBinder
   Name/tr:Şekil bağlayıcı oluştur
   Workbenches:[Parça tasarım](PartDesign_Workbench/tr.md)
   MenuLocation:Parça tasarım → Şekil bağlayıcı oluştur
   Version:0.17
   SeeAlso:[klonla](PartDesign_Clone/tr.md)
---

# PartDesign ShapeBinder/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

Etkin Cisim içindeki seçili bir cismi bir referans **şekil bağlayıcı** oluşturur. Bir şekil bağlayıcı, başka bir cismin kenarlarına veya yüzlerine bağlanan bir referans nesnesidir. Kullanım örneği, iki farklı cisimde fitting kapaklı bir kutu oluşturmak olabilir. Şekil bağlayıcı nesnesi, 3D görünümünde yarı saydam sarı renkte görüntülenir.


</div>

Examples of use would be to build a box with fitting cover in two different bodies or to make holes that are aligned between different bodies.

<img alt="" src=images/Shapebinder_tree.png ) ![](images/Shapebinder_flow.png  style="width:600px;">


<div class="mw-translate-fuzzy">

\"Body.Pad004\'ten iki şekil seçildi ve referans nesneleri Body001.Sketch005\'te Body001.ShapeBinder ile dış geometri olarak mevcut.\"


</div>


<div class="mw-translate-fuzzy">

## Nasıl Kullanılır 


</div>


<div class="mw-translate-fuzzy">

1.  Hedef cismi aktif edin.(şekil bağlayıcı nesneye sahip olacak cisim)

2.  
    **<img src="images/PartDesign_ShapeBinder.png" width=24px> '''Şekil bağlayıcı oluştur'''**\'a basın.

3.  
    **Nesne**veya **Geometri ekle** tuşlarına basın.

4.  3D görünümünde, kopyalanacak nesneyi veya geometriyi seçin. Nesne, tüm cismi seçecek; Geometri ekle herhangi bir eleman seçecektir(köşe, kenar, yüz).

5.  Seçilen geometriyi kaldırmak için, **Geometriyi kaldır** düğmesine basın ve 3D görünümünde geometriyi seçin. İptal etmek için düğmeye tekrar basın.

6.  Alternatif olarak, Şekil bağlayıcı komutunu başlatmadan önce kopyalanacak cisim seçilebilir.

7.  
    **Tamam**\'a basın.


</div>

**Example**

:   The example uses the ShapeBinder feature to make a hole (with or without threads) through more than one body. Normally the Hole function of the Part Design workbench is limited to a single body. The example uses two cubes facing each other but misaligned in an arbitrary way. The holes are created with sketches containing a circle for every hole (the diameter is ignored by the hole function). When you copy the sketch to the other cube it will be at the same position in the local cube coordinate system. In the image this is shown by the white circle on the back cube. This is not what we want, because the hole at that position would not be aligned to the hole in the front cube.





:   

    :   ![](images/ShapeBinderThroughHole.png )
    :   *Example setup for showing HowTo make holes through different bodies. The white circle shows that copying sketches is not enough*

Here is how you use the ShapeBinder Feature to achieve it:

1.  Prepare a scene as per the above image. If you use the cubes from the [Part workbench](Part_Workbench.md), remember that you must put them into a \"body\" container. Each one in a single body container. Otherwise the [PartDesign](PartDesign_Workbench.md) functions would not work. If you build them from sketches the system should create body containers by default.
2.  Select the Properties Dialog Tab then Data to move the second cube to touch the first cube with a side displacement.
3.  Select the PartDesign workbench
4.  Create a sketch on the front face of the first cube and place a circle anywhere and close the sketch
5.  Select the sketch in the tree and press [Hole](PartDesign_Hole.md) function button. Before make sure the first body is the [active body](PartDesign_Body#Active_status.md) (double-click).
6.  Select a hole of appropriate size. The image above had also counterbore selected. Close the [Hole](PartDesign_Hole.md) function.

    :   Now the image should look as above. When you hide the first cube (select and press space) you can see that the hole does not reach the second cube. It will not, even when you select \"Through All\", or when you enter a really large distance in the [Hole](PartDesign_Hole.md) dialog. The hole dialog is always limited to a single body.
    :   Here is where our ShapeBinder comes in.
7.  First select the back cube. This is the target where the ShapeBinder will be added. It must be [actived](PartDesign_Body#Active_status.md) before, so be sure it has been double-clicked.
8.  In the tree select the sketch we used for the hole. It\'s important to not activate the first body.
9.  Select the shapeBinder function.

    :   A dialog should open. In the line \"Object\" the name of our sketch should be visible. If you had selected the function without selecting the sketch, you could press \"Object\" and then select the sketch from the list. It\'s recommended to select it first in order to get the right one, especially if you have many sketches with automatically generated names Sketch001,.. The \"Add Geometry\" is not useful for us, because we want to select the whole sketch. \"AddGeometry\" is used if only parts should be selected.
10. Press **OK** to close the dialog and check that a new item has been added to the tree of the second cube.

    :   When you toggle the visibility of the ShapeBinder it is shown yellow in the [3D view](3D_view.md). However it\'s on the wrong position, just as the white circle in the image above. That is because of the default setting for the Trace parameter.
11. In the PropertyView of the ShapeBinder in the Data tab set the **Trace Support** parameter to true. The default was false.

    :   With **Trace Support** true, the ShapeBinder in not affected by local transformations of the target body, e.g. our translations. The shape remains exactly where the original front object shape has been. Try moving the front object around and you can see that the ShapeBinder always follows to the new position.
    :   Unfortunately we can not select the ShapeBinder for a [Hole](PartDesign_Hole.md). Therefore we create a local sketch and use that for our hole in the second cube.
12. Select the front face of the back cube and create a new sketch (click **OK** for the suggestion in the dialog)
13. Make all geometry invisible and the ShapeBinder visible. Now you can use the external geometry function and select the circle in the shape binder. We need the center point of that circle.
14. Create a new circle and put it at the center point of the ShapeBinders circle. The radius is not important. The [Hole](PartDesign_Hole.md) function only uses the center points of the circles (note: single points are ignored by the Hole function, we must use circles)
15. Close the sketch and click [Hole](PartDesign_Hole.md). Set the dialog to the same values as the initial hole and press OK.

**Done.**

:   Now you have two linked holes in two different bodies. If you change the geometry or the positions of the holes, both holes will adapt. Only when you add a new hole, you need to update the sketch in the second cube for the second hole.





:   Notes:
:   that there is another way to create a ShapeBinder: with the back cube activated click the front face of the front cube and create a new sketch. A dialog will pop up where you select \"Dependent sketch\". This will actually create a shape binder. You can see the **Trace Support** parameter in the property window. It\'s a few clicks less than our procedure.
:   Also note that working with ShapeBinder with Sketches is only a subset of its capabilities. It\'s also possible to use parts of 3D geometry as seen in the example above.

## Seçenekler


<div class="mw-translate-fuzzy">

Model ağacındaki Şekil bağlayıcı etiketine çift tıklayın veya sağ tıklayın ve parametrelerini düzenlemek için bağlam menüsünde **Şekil bağlayıcı Düzenle** seçeneğini seçin.


</div>

## Özellikler


<div class="mw-translate-fuzzy">

-    **Label**:Nesneye verilen isimdir. Bu isim daha sonra değiştirilebilir.

-    **Trace Support**: Bu seçeneği true olarak ayarlayarak, Şekil bağlayıcı parçaların ve cisimlerin göreceli yerleşimlerini gözlemler.<small>(v0.18)</small> 


</div>

## Sınırlamalar


<div class="mw-translate-fuzzy">

-   Çoklu seçim desteklenmiyor. Her bir seçim için, Geometri ekle ve Geometriyi kaldır düğmelerine basılması gerekir.

Birden fazla seçim için bir geçici çözüm vardır: Şekil bağlayıcı\'yı oluşturmadan önce sahip olmak istediğiniz tüm öğeleri seçerseniz , başlangıç ​​listesinde görünürler.

-   Bir şekil bağlayıcı temel özellik olarak kullanılamaz.
-   Bir gövdede seçilen geometri bitişik olmalıdır.
-   Kopyalanacak gövde, komutu başlatmadan önce ilk olarak seçilirse veya **Nesne** düğmesi kullanılıyorsa, artık yalnızca belirli geometri öğelerini seçmek mümkün değildir.
-   Hedef cismin ve kopyalanan cismin göreceli yerleşimi dikkate alınmaz. Şekil bağlayıcı, kopyalanan cisimle aynı dahili koordinatları benimseyecektir. 0.18 sürümünden bu yana, bu davranışı göreceli yerleşimleri dikkate almak üzere değiştirmek için yeni bir \"İzleme Desteği\" özelliğine sahiptir.


</div>





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign ShapeBinder/tr
