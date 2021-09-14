# Draft Workbench/tr




 

<img alt="Draft workbench icon" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introduction

## Giriş

Taslak Tezgahı, basit 2D nesneler çizmenize izin verir ve daha sonra bunları değiştirmek için birkaç araç sunar. Ayrıca, geometrinizin konumunu tam olarak kontrol etmek için bir çalışma düzlemi, bir ızgara ve bir bağlama sistemi tanımlamak için araçlar sağlar.

Oluşturulan 2D nesneler genel çizim için Inkscape veya Autocad\'e benzer bir şekilde kullanılabilir. Bu 2D şekiller ayrıca diğer tezgahlarla oluşturulan 3D nesnelerin temel bileşenleri olarak da kullanılabilir, örneğin, [Parça tezgahı](Part_Workbench/tr.md) ve [Mimari tezgah](Arch_Workbench/tr.md) gibi. Taslak nesnelerin [Eskiz tezgahı](Sketcher_Workbench/tr.md) \'na dönüştürülmesi de mümkündür; bu, şekillerden katı cisimlerin oluşturulması için [Parça tasarım tezgahı](PartDesign_Workbench/tr.md) ile de kullanılabileceği anlamına gelir.

FreeCAD öncelikle bir 3D modelleme uygulamasıdır ve bu nedenle 2D araçları diğer çizim programlarındaki kadar gelişmiş değildir. Öncelikli hedefiniz karmaşık 2D çizimler ve [DXF](DXF.md) dosyalarının üretimi ise ve 3D modellemeye gerek duymuyorsanız, teknik taslaklar için [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad),TurboCad ve diğerleri gibi özel bir yazılım programı düşünebilirsiniz.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## Çizim nesneleri 

Bunlar nesne oluşturma araçlarıdır.

-   <img alt="" src=images/Draft_Line.png  style="width:32px;"> [Çizgi](Draft_Line/tr.md): İki nokta arasında çizgi parçası çizer.
-   <img alt="" src=images/Draft_Wire.png  style="width:32px;"> [Tel](Draft_Wire/tr.md): Birden çok çizgi parçasından (bir çizgi) oluşan bir çizgi çizer.
-   <img alt="" src=images/Draft_Circle.png  style="width:32px;"> [Çember](Draft_Circle/tr.md): Merkez noktası ve yarıçapla bir çember çizer.
-   <img alt="" src=images/Draft_Arc.png  style="width:32px;"> [Yay](Draft_Arc/tr.md): Merkez, yarıçap, başlangıç ​​açısı ve bitiş açısından bir yay parçası çizer.
-   <img alt="" src=images/Draft_Ellipse.png  style="width:32px;"> [Elips](Draft_Ellipse/tr.md): İki köşe noktasından bir elips çizer.
-   <img alt="" src=images/Draft_Polygon.png  style="width:32px;"> [Çokgen](Draft_Polygon/tr.md):Merkezden, yarıçaptan ve yanlardan düzenli bir çokgen çizer.
-   <img alt="" src=images/Draft_Rectangle.png  style="width:32px;"> [Dikdörtgen](Draft_Rectangle/tr.md): İki köşe noktasından bir dikdörtgen çizer.
-   <img alt="" src=images/Draft_Text.png  style="width:32px;"> [Metin](Draft_Text/tr.md): Çok satırlı bir metin notu çizer.
-   <img alt="" src=images/Draft_Dimension.png  style="width:32px;"> [Boyut](Draft_Dimension/tr.md): Bir boyut notu çizer.
-   <img alt="" src=images/Draft_BSpline.png  style="width:32px;"> [BSpline](Draft_BSpline/tr.md): Bir nokta serisinden bir B-Spline çizer.
-   <img alt="" src=images/Draft_Point.png  style="width:32px;"> [Nokta](Draft_Point/tr.md): Bir nokta nesnesi ekler.
-   <img alt="" src=images/Draft_ShapeString.png  style="width:32px;"> [Şekil dizesi](Draft_ShapeString/tr.md): Belirli bir noktada bir metin dizesini temsil eden bir bileşik şekil ekler.
-   <img alt="" src=images/Draft_Facebinder.png  style="width:32px;"> [Yüz kaplama](Draft_Facebinder/tr.md): Mevcut nesnelerdeki seçilen yüzlerden yeni bir nesne oluşturur.
-   <img alt="" src=images/Draft_BezCurve.png  style="width:32px;"> [Bezier eğrisi](Draft_BezCurve/tr.md): Bir dizi noktadan bir Bezier eğrisi çizer.
-   <img alt="" src=images/Draft_Label.png  style="width:32px;"> [Etiket](Draft_Label/tr.md): Seçili öğeye işaret eden oklu bir etiket yerleştirir. {{Version/tr|0.17}}

## Annotation objects 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): draws a multi-line text annotation.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): draws a dimension annotation.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): places a label with an arrow pointing to a selected element.
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md): opens an editor to change the annotation style of these objects. <small>(v0.19)</small> 

### Nesneleri modifiye etme 

Bunlar mevcut nesneleri modifiye etmek için kullanılan araçlardır. Seçilen nesneler üzerinde çalışırlar, ancak hiçbir nesne seçilmezse, birini seçmeniz istenir.

Birçok işlem aracı (taşıma, döndürme, dizi vb.) katı nesneler üzerinde de çalışır ([ Parça tezgahı](Part_Workbench.md), [ Parça tasarım tezgahı](PartDesign_Workbench.md), [ Mimari tezgah](Arch_Tezgah.md), vb.).

-   <img alt="" src=images/Draft_Move.png  style="width:32px;"> [Taşı](Draft_Move/tr.md): Nesneleri bir konumdan diğerine taşır.
-   <img alt="" src=images/Draft_Rotate.png  style="width:32px;"> [Döndür](Draft_Rotate/tr.md): Nesneleri başlangıç ​​açısından bitiş açısına döndürür.
-   <img alt="" src=images/Draft_Offset.png  style="width:32px;"> [Ofsetle](Draft_Offset/tr.md): Bir nesnenin bölümlerini belirli bir mesafeden ofsetler.
-   <img alt="" src=images/Draft_Trimex.png  style="width:32px;"> [Kırp/Uzat (Trimex)](Draft_Trimex/tr.md): Bir nesneyi keser veya uzatır.
-   <img alt="" src=images/Draft_Upgrade.png  style="width:32px;"> [Yükselt](Draft_Upgrade/tr.md): Nesneleri daha yüksek seviyeli bir nesneye birleştirir.
-   <img alt="" src=images/Draft_Downgrade.png  style="width:32px;"> [Düşür](Draft_Downgrade/tr.md): Nesneleri daha düşük seviyeli nesnelere patlatır.
-   <img alt="" src=images/Draft_Scale.png  style="width:32px;"> [Ölçekle](Draft_Scale/tr.md): Seçili nesneleri temel bir noktaya göre ölçeklendirir.
-   <img alt="" src=images/Draft_Edit.png  style="width:32px;"> [Düzenle](Draft_Edit/tr.md): Seçilen bir nesneyi düzenler.
-   <img alt="" src=images/Draft_WireToBSpline.png  style="width:32px;"> [Telden BSpline çevir](Draft_WireToBSpline/tr.md): Bir teli B- Spline\'a çevirir (veya tersi).
-   <img alt="" src=images/Draft_AddPoint.png  style="width:32px;"> [Nokta ekle](Draft_AddPoint/tr.md): Bir tele veya B-Spline\'a bir nokta ekler.
-   <img alt="" src=images/Draft_DelPoint.png  style="width:32px;"> [Nokta sil](Draft_DelPoint/tr.md): Bir telden veya B-Spline\'dan bir nokta siler.
-   <img alt="" src=images/Draft_Shape2DView.png  style="width:32px;"> [2D görünüme çevir](Draft_Shape2DView/tr.md): Bir 3D nesnesinin düzleştirilmiş bir 2D görüntüsü olan bir 2D nesnesi oluşturur.
-   <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> [Taslak/Eskiz çevir](Draft_Draft2Sketch/tr.md):Bir Taslak nesnesini [Eskiz Tezgahı](Sketcher_Workbench/tr.md) çizimine dönüştürür ve bunun tersi de geçerlidir.
-   <img alt="" src=images/Draft_Array.png  style="width:32px;"> [Dizi](Draft_Array/tr.md): Seçilen nesnelerden kutupsal veya dikdörtgen bir dizi oluşturur.
-   <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> [Yol dizisi](Draft_PathArray/tr.md): Kopyaları yol boyunca yerleştirerek bir nesne dizisi oluşturur.
-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Nokta dizisi](Draft_PointArray/tr.md): Kopyaları belirli noktalara yerleştirerek bir dizi nesne yaratır. {{version/tr|0.18}}
-   <img alt="" src=images/Draft_Clone.png  style="width:32px;"> [Klonla](Draft_Clone/tr.md): Seçilen nesneleri klonlar.
-   <img alt="" src=images/Draft_PutOnSheet.png  style="width:32px;"> [Çizim](Draft_Drawing/tr.md): Seçilen nesneleri [Çizim Tezgahı](Drawing_Workbench/tr.md) sayfasına yazar.
-   <img alt="" src=images/Draft_Mirror.png  style="width:32px;"> [Yansıt](Draft_Mirror/tr.md): Seçilen nesneleri yansıtır.
-   <img alt="" src=images/Draft_Stretch.png  style="width:32px;"> [Uzat](Draft_Stretch/tr.md): Seçili nesneleri uzatır. {{Version/tr|0.17}}

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): clones the selected objects.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Array tools.
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Ortho Array](Draft_OrthoArray.md): creates an orthogonal array from the selected object. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar Array](Draft_PolarArray.md): creates an array in a polar pattern, that is, sweeping an angle. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Circular Array](Draft_CircularArray.md): creates an array in a circular pattern, that is, starting from a center and moving outwards radially. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md): creates an array of objects by placing the copies along a path.
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Path LinkArray](Draft_PathLinkArray.md): like <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md), but creates [App Links](App_Link.md) instead of regular copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array of objects by placing the copies at certain points.
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Point LinkArray](Draft_PointLinkArray.md): like <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md), but creates [App Links](App_Link.md) instead of regular copies. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): edits a selected object.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): enters an edit mode that allows editing different objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join.md): joins lines together into a single wire.
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split.md): splits a wire into two at a point.
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades objects into a higher-level object.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades objects into lower-level objects.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Wire to BSpline](Draft_WireToBSpline.md): converts a wire to a B-Spline and vice-versa.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): converts a Draft object to a [Sketcher Workbench](Sketcher_Workbench.md) Sketch and vice-versa.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Slope](Draft_Slope.md): changes the elevation slope of the currently selected [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Flip Dimension](Draft_FlipDimension.md): flips the orientation of the text of a [Draft Dimension](Draft_Dimension.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D View](Draft_Shape2DView.md): creates a 2D object which is a flattened 2D view of a 3D object.

## Draft Tray 

The [Draft Tray](Draft_Tray.md) allows selecting the working plane, defining style settings, toggling construction mode, and specifying the active layer or group.

![](images/Draft_tray_default.png )

Its tools are also available in the **Draft → Utilities** menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Select Plane](Draft_SelectPlane.md): selects the current Draft working plane.

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Draft Snap toolbar 

The Draft Snap toolbar allows selecting the active snap options. The buttons belonging to active options stay depressed. For general information about snapping see: [Draft Snap](Draft_Snap.md).

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Toggle snap](Draft_Snap_Lock.md): toggles [object snapping](Draft_Snap.md) globally on or off.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of line, arc and spline segments.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Midpoint](Draft_Snap_Midpoint.md): snaps to the middle point of line and arc segments.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Center](Draft_Snap_Center.md): snaps to the center point of circles, arcs and faces, [WP proxies](Draft_WorkingPlaneProxy.md) and [Building parts](Arch_BuildingPart.md)
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Angle](Draft_Snap_Angle.md): snaps to the special cardinal points of circles and arcs, at 45° and 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two line or arc segments. Hover the mouse over the two desired objects to activate their intersection snaps.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Perpendicular](Draft_Snap_Perpendicular.md): on line and arc segments, snaps perpendicularly to the latest point.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Extension](Draft_Snap_Extension.md): snaps on an imaginary line that extends beyond the endpoints of line segments. Hover the mouse over the desired object to activate its extension snap.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Parallel](Draft_Snap_Parallel.md): snaps on an imaginary line parallel to a line segment. Hover the mouse over the desired object to activate its parallel snap.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Special](Draft_Snap_Special.md): snaps on special points defined by the object.
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Near](Draft_Snap_Near.md): snaps to the closest point or edge on the nearest object.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Ortho](Draft_Snap_Ortho.md): snaps on imaginary lines that cross the last point, and extend at 0°, 45° and 90°.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Grid](Draft_Snap_Grid.md): snaps to the intersections of the grid lines, if the grid is visible.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Working plane](Draft_Snap_WorkingPlane.md): always places the snapped point on the current [working plane](Draft_SelectPlane.md), even if you snap to a point outside that working plane.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions while snapping.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle grid](Draft_ToggleGrid.md): toggles the visibility of the grid on or off.

## Yararlı ek araçlar 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a Layer in the current document, to which objects can be added to control object visibility and color. It replaces Draft VisGroup. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Working Plane Proxy](Draft_WorkingPlaneProxy.md): create a proxy object to store the current [Working Plane](Draft_SelectPlane.md) position.
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle display mode](Draft_ToggleDisplayMode.md): switches the display mode of selected objects between \"Flat Lines\" and \"Wireframe\".
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Add to group](Draft_AddToGroup.md): quickly adds selected objects to an existing [Std Group](Std_Group.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group contents](Draft_SelectGroup.md): selects the contents of a selected [Std Group](Std_Group.md) or [Draft Layer](Draft_Layer.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): add selected objects to the Construction group.
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

## Additional tools 

Seçilen nesneye bağlı olarak ek araçlar, **Taslak → Araçlar** yoluyla veya sağ tıklama menüsünden ulaşılabilir.

-   <img alt="" src=images/Draft_SelectPlane.png  style="width:32px;"> [Çalışma düzlemini ayarla](Draft_SelectPlane/tr.md): Çalışma düzlemini standart bir görünümden veya seçilen bir yüze ayarlar.
-   <img alt="" src=images/Draft_FinishLine.png  style="width:32px;"> [Çizgiyi bitir](Draft_FinishLine/tr.md): Mevcut tel veya B-spline çizgisini kapatmadan sonlandırır.
-   <img alt="" src=images/Draft_CloseLine.png  style="width:32px;"> [Çizgiyi kapat](Draft_CloseLine/tr.md): Mevcut tel veya B-spline çizgisini kapatıp sonlandırır.
-   <img alt="" src=images/Draft_UndoLine.png  style="width:32px;"> [Çizgiyi geri al](Draft_UndoLine/tr.md): Çizginin son kısmını geri alır.
-   <img alt="" src=images/Draft_ToggleConstructionMode.png  style="width:32px;"> [İnşaat modunu değiştir](Draft_ToggleConstructionMode/tr.md):Taslak inşaat modunu açar veya kapatır.
-   <img alt="" src=images/Draft_ToggleContinueMode.png  style="width:32px;"> [Devam modunu değiştir](Draft_ToggleContinueMode/tr.md): Taslak devam modunu açar veya kapatır.
-   <img alt="" src=images/Draft_ApplyStyle.png  style="width:32px;"> [Stili uygula](Draft_Apply/tr.md): Geçerli stili ve rengi seçili nesnelere uygular.
-   <img alt="" src=images/Draft_ToggleDisplayMode.png  style="width:32px;"> [Ekran modunu değiştir](Draft_ToggleDisplayMode/tr.md): Seçili nesnelerin ekran modunu \"Düz Hatlar\" ve \"Tel Kafes\" arasında değiştirir.
-   <img alt="" src=images/Draft_AddToGroup.png  style="width:32px;"> [Gruba ekle](Draft_AddToGroup/tr.md): Seçilen nesneyi varolan bir gruba ekler.
-   <img alt="" src=images/Draft_SelectGroup.png  style="width:32px;"> [Grup içeriğini seç](Draft_SelectGroup/tr.md): Seçili bir grubun içeriğini seçer.
-   <img alt="" src=images/Draft_ToggleSnap.png  style="width:32px;"> [Yakalama aç/kapa](Draft_ToggleSnap/tr.md):Nesnenin [Nesne yakalamayı](Draft_Snap/tr.md) açar veya kapatır.
-   <img alt="" src=images/Draft_ToggleGrid.png  style="width:32px;"> [Izgarayı aç/kapa](Draft_ToggleGrid/tr.md):Izgaranın görünürlüğünü açar veya kapatır.
-   <img alt="" src=images/Draft_ShowSnapBar.png  style="width:32px;"> [Yakalama çubuğunu göster](Draft_ShowSnapBar/tr.md): [Yakalama](Draft_Snap/tr.md) araç çubuğunu gösterir veya gizler.
-   <img alt="" src=images/Draft_Heal.png  style="width:32px;"> [İyileştirme](Draft_Heal/tr.md): Çok eski dosyalarda bulunan sorunlu Taslak nesnelerini iyileştirir.
-   <img alt="" src=images/Draft_FlipDimension.png  style="width:32px;"> [Boyutu çevir](Draft_FlipDimension/tr.md):[Boyut](Draft_Dimension/tr.md) metninin yönünü çevirir .
-   <img alt="" src=images/Draft_VisGroup.png  style="width:32px;"> [VisGroup](Draft_VisGroup/tr.md): Geçerli belgede bir VisGroup oluşturur.
-   <img alt="" src=images/Draft_Slope.png  style="width:32px;"> [Eğim ver](Draft_Slope/tr.md): Seçili olan Taslak Çizgisi veya Taslak Kablosunun yükselme eğimini değiştirir. {{Version/tr|0.17}}
-   <img alt="" src=images/Draft_AutoGroup.png  style="width:32px;"> [Otomatik grup](Draft_AutoGroup/tr.md): Yeni nesneleri belirli bir gruba otomatik olarak yerleştirir.
-   <img alt="" src=images/Draft_SetWorkingPlaneProxy.png  style="width:32px;"> [Set Working Plane Proxy](Draft_SetWorkingPlaneProxy/tr.md): Geçerli [Çalışma düzlemi](Draft_SelectPlane/tr.md) konumunu depolamak için bir proxy nesnesi ekler.{{Version/tr|0.17}}
-   <img alt="" src=images/Draft_ToggleConstructionMode.png  style="width:32px;"> [İnşaat grubuna ekle](Draft_AddConstruction/tr.md): Seçili nesneyi inşaat grubuna ekler.{{Version/tr|0.17}}

## Ek özellikler 

-   [ Koordinatlar](Draft_Coordinates/tr.md): Yeni bir nokta tanımlamak için 3B görünüme tıklamak yerine koordinatları girer.
-   [ Constraining](Draft_Constrain/tr.md): imleci bir önceki noktaya göre yatay veya dikey hareketlerle sınırlandırır.
-   [ Yakalama](Draft_Snap/tr.md): Mevcut nesnelerdeki veya ızgaradaki özel yerlere yeni noktalar yerleştirir.

## Tree view context menu 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Selection options 

If there is a selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D view context menu 

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Selection options 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Obsolete tools 

These commands are obsolete but still available:

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array.md): creates a polar or rectangular array from selected objects. {{Obsolete|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Seçenekler

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Seçenekler\...](Draft_Preferences/tr.md): Çalışma düzlemi ve çizim araçları için genel tercihler.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [İçe/Dışa aktar Seçenekleri](Import_Export_Preference/tr.md): Farklı dosya biçimlerinden içe ve dışa aktarma için mevcut seçenekler.

## Dosya formatları 

Taslak modül, FreeCAD\'e aşağıdaki dosya formatları için içe aktarıcı ve dışa aktarıcı sağlar:

-   [ Autodesk .DXF](Draft_DXF.md): 2D CAD uygulamaları ile oluşturulan [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) dosyalarını içe/dışa aktarır. Ayrıca bakınız [ FreeCAD ve DXF içe aktarma](FreeCAD_and_DXF_Import/tr.md).
-   [ Autodesk .DWG](Draft_DXF.md): [ ODA Dönüştürücüsü](Ekstra_python_modülleri_#_ODA_Dönüştürücüsü_(daha_önce_Teigha_Dönüştürücüsü).md) yardımcı programı yüklendiğinde, DWG dosyalarını DXF içe aktarıcısı aracılığıyla alır ve verir. Ayrıca bakınız [ FreeCAD ve DWG Alma](FreeCAD_and_DWG_Import.md).
-   [ SVG](Draft_SVG.md): vektör çizim uygulamaları ile oluşturulan [Ölçeklenebilir Vektör Grafikleri](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) dosyalarını içeri ve dışarı aktarır.
-   [ Open Cad formatı .OCA](Draft_OCA.md): potansiyel olarak yeni bir [CAD dosyası formatı](http://groups.google.com/group/open_cad_format) OCA / GCAD dosyalarını içe ve dışa aktarır.
-   [ Airfoil Data Format .DAT](Draft_DAT.md): [Airfoil profilleri](http://www.ae.illinois.edu/m-selig/ads/coord_database.html) \'nı açıklayan DAT dosyalarını içe aktarır.

### Install importers 

-   [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md): Imports and exports DWG files
-   [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md): Imports and exports DXF files

## Unit tests 


**See also:**

[Test Workbench](Test_Workbench.md).

To run the unit tests of the workbench execute the following from the operating system terminal. 
```python
freecad -t TestDraft
```

## Betik

Taslak modulu [Taslak API](Draft_API/tr.md) kullanarak, [Python](Python/tr.md) konsolunda ve [makrolar](macros/tr.md) da kullanabilirsiniz.

The workbench includes a module to create samples of all objects in a new document. <small>(v0.19)</small> 

Use this to test that all objects are produced correctly. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Inspecting the code of this module is useful to understand how to use the programming interface. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Where `$INSTALLDIR` is the toplevel directory where the software was installed; for example, in Linux it may be `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Test objects for the [Draft Workbench](Draft_Workbench.md).*

## Kılavuzlar

-   [Taslak Kılavuzu](Draft_tutorial/tr.md)
-   [Taslak Kılavuzu (Eski)](Draft_tutorial_Outdated/tr.md)
-   \[\[Draft\_ShapeString\_tutorial/tr\|

Şekil dizesi kılavuzu\]\]


{{docnav/tr
|[Görüntü Tezgahı](Image_Workbench/tr.md)
|[Mimari Tezgah](Arch_Workbench/tr.md)}}


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


 

[Category:Workbenches/tr](Category:Workbenches/tr.md) [Category:Workbenches](Category:Workbenches.md)
