# Draft Snap/tr







{{TOCright}}

## Açıklama


<div class="mw-translate-fuzzy">

[Taslak tezgahı](Draft_Workbench/tr.md) araçları, imleçle 3D görünümü tıklatarak noktaları, mesafeleri, yarıçapları ve açıları grafiksel olarak seçmenize olanak sağlar.


</div>


<div class="mw-translate-fuzzy">

Yakalama çoğu [ Taslak tezgahı](Draft_Workbench/tr.md) ve [ Mimari Tezgah](Arch_Workbench/tr.md) araçlarıyla kullanılabilir ve {{Button | <img src="images/_Snap_Lock.svg_" width= 16px> [Yakalama aç/kapa](Draft_ToggleSnap/tr.md)}} düğmesi, yakalama araç çubuğunda bulunur ve bu düğmeye tıklayarak global olarak etkinleştirilebilir veya devre dışı bırakılabilir. {{MenuCommand | Görünüm → Araç Çubukları → Taslak Yakalama}} menüsü ile aktif hale getirilebilir. Her bir yakalama yöntemi, araç çubuğundaki ilgili düğmeye tıklayarak ayrı ayrı etkinleştirilebilir veya devre dışı bırakılabilir.


</div>

![](images/Draft_Snap_Endpoint_example.png )


<div class="mw-translate-fuzzy">


{{Caption | Çizgi yakalama başka bir satıra dikey olarak yakalar}}


</div>

## Snap tools 

These tools are available in the Draft Snap toolbar and in the [Draft snap widget](Draft_snap_widget.md).

Note that circular edges do not have to be full circles.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of straight and circular edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap Center](Draft_Snap_Center.md): snaps to the center point of faces and circular edges, and to the **Placement** point of [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular point on edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces or edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at 0°, 45°, 90° and 135°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap Working Plane](Draft_Snap_WorkingPlane.md): projects the snap point onto the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.


<div class="mw-translate-fuzzy">

### Gelişmiş yapışma 


</div>


<div class="mw-translate-fuzzy">

-   [Orto](Draft_Ortho/tr.md) ve [Uzantı](Draft_Extension/tr.md) gibi iki yakalama yöntemini birleştirerek, hayali çizgilerin kesişme noktasında bir nokta yakalama noktası oluşturacak şekilde ek yakalama konumları elde edilebilir.
-   Diğer yakalama yerleri, [Kısıtlama](Draft_Constrain/tr.md) kullanılarak, yani {{KEY | Shift}} tuşuna basılarak veya {{KEY | X}}, {{KEY | Y}} veya **Z** tuşuna basılarak elde edilebilir.
-   İmlecin geçerli konumuna bir \"tutma noktası\" eklemek için çizim yaparken {{KEY | Q}} tuşuna basın. Daha sonra ortogonal olarak bu tutma noktalarını ve ortogonal eksenlerinin kesişme noktalarını yakalayabilirsiniz. Eğer [Orta Nokta](Draft_Midpoint/tr.md) yakalama özelliği etkinse, iki tutma noktası arasındaki orta mesafeden de yakalayabilirsiniz. {{Version/tr | 0.17}}


</div>

![](images/Draft_Snap_example_cycling_1.png ) *Snap cycling 1: The red rectangle was created first therefore it has snap priority. Without snap cycling you cannot snap to the green rectangle where it is overlapped by the red rectangle.*

![](images/Draft_Snap_example_cycling_2.png ) *Snap cycling 2: After using the snap cycle key once the green rectangle receives snap priority. Snapping to the midpoint of the overlapped green edge is now possible.*

## Notes


<div class="mw-translate-fuzzy">

Aynı anda birçok yakalam yöntemi kullanmak, nesnelerinizi istenen pozisyonlara çekmek için faydalı olabilir, imleciniz sürekli olarak yanlış noktalara tutturulduğunda sorunlu olabilir. Bu durumda, o zaman yalnızca bir yakalama yöntemi kullanmayı deneyin.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

Note that after changing some preferences you must restart FreeCAD.


<div class="mw-translate-fuzzy">

## Seçenekler

-   ![ 32px](images/_Draft_ToggleGrid.png ) [ Izgara aç/kapa](Draft_ToggleGrid/tr.md): Çalışma düzlemi ızgarasını açar veya kapatır.
-   ![ 32px](images/_Snap_Lock.png ) [Yakalama aç/kapa](Draft_ToggleSnap/tr.md): Tüm çalışma ortamlarında yakalamayı açar veya kapatır.
-   Bir noktanın yakalama noktası olarak kabul edildiği maksimum mesafe [Seçeneklerde](Draft_Preferences/tr.md) belirtilir ve ayrıca **<nowiki>[</nowiki>** (artır) veya **<nowiki>]</nowiki>**(azalt) tuşuna basılarak anında değiştirilebilir.


</div>


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>


 
