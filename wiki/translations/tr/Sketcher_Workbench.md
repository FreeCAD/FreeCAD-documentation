# <img alt="Sketcher workbench icon" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/tr






## Giriş


<div class="mw-translate-fuzzy">

[Eskiz tezgahı](Sketcher_Workbench/tr.md); [Parça tasarım tezgahı](PartDesign_Workbench/tr.md), [Yapı tezgahı](Arch_Workbench/tr.md) ve diğer tezgahlarda kullanılmak üzere 2D geometriler üretir. Genel olarak, bir 2D geometrisi çoğu CAD modelinin başlangıç ​​noktası olarak kabul edilir, çünkü bir 2D çizimi, 3D şekli oluşturmak için \"ekstrüzyona sokulabilir\"; Önceden oluşturulmuş 3D şekillerin üstünde oyuklar, çıkıntılar veya ekstrüzyonlar gibi başka özellikler oluşturmak için başka 2D çizimler de kullanılabilir. [Parça Tezgahında](Part_Workbench/tr.md) tanımlanan katılarda, Boolean işlemleri ile birlikte Eskiz, üretken katı şekilli tasarımın çekirdeğini oluşturur.


</div>

Together with boolean operations defined in the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md), the Sketcher Workbench, or \"The Sketcher\" for short, forms the basis of the [constructive solid geometry](Constructive_solid_geometry.md) (CSG) method of building solids. Together with <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) operations, it also forms the basis of the [feature editing](Feature_editing.md) methodology of creating solids. But many other workbenches use sketches as well.


<div class="mw-translate-fuzzy">

Eskiz tezgahı, 2D şekillerin kesin geometrik tanımları izlemesine izin veren \"kısıtlamalara\" sahiptir. Bir kısıtlayıcı çözücü, 2D geometrinin kısıtlı boyutunu hesaplar ve çizim serbestlik derecelerinin etkileşimli olarak araştırılmasını sağlar.


</div>


<div class="mw-translate-fuzzy">

#### Eskiz nerelerde kullanılmaz 

Eskiz, 2D planlar üretmek için tasarlanmamıştır. Eskizler, katı bir özellik oluşturmak için kullanıldığında, otomatik olarak gizlenir. Kısıtlamalar yalnızca Eskiz düzenleme modunda görülebilir.


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*
Tamamen kısıtlanmış bir eskiz*

## Constraints


<div class="mw-translate-fuzzy">

#### Kısıtlama nedir 

Boyutlar yerine, kısıtlamalar bir nesnenin serbestlik derecesini sınırlamak için kullanılır. Örneğin, kısıtlamaları olmayan bir çizgi 4 [Serbestlik Derecesine](#Degrees_Of_Freedom.md) (\" DOF \" olarak kısaltılır) sahiptir: yatay ya da dikey olarak hareket ettirilebilir, uzatılabilir ve döndürülebilir.


</div>

Yatay veya dikey bir sınırlama veya bir açı sınırlaması (başka bir çizgiye veya eksenlerden birine göre) uygulamak, dönme kapasitesini sınırlar ve böylece 3 serbestlik derecesine sahip olur. Çizginin herhangi bir noktasını, Orijin ile ilişkilendirmek 2 serbestlik derecesini ortadan kaldırır. Bir boyut sınırlaması uygulamak son serbestlik derecesini ortadan kaldıracaktır. Çizgi daha sonra **tamamen kısıtlı** olarak kabul edilir .


<div class="mw-translate-fuzzy">

Birden fazla nesne aralarında sınırlandırılabilir. İki çizgi, noktaları birbiriyle çakışan nokta kısıtı ile birleştirilebilir. Aralarında bir açı belirlenebilir veya dik olarak ayarlanabilir. Bir çizgi, bir yay veya bir daireye teğet olabilir vb. Birden fazla nesneyi içeren karmaşık bir Eskiz, çok sayıda farklı çözüme sahip olacak ve **tamamen kısıtlı** olması, bu olası çözümlerden yalnızca birinin uygulanan kısıtlamalara dayanarak ulaşıldığı anlamına gelir.


</div>


<div class="mw-translate-fuzzy">

İki tür kısıtlama vardır: geometrik ve boyutsal. Bunlar aşağıdaki [\'Araçlar\'](#The_tools.md) bölümünde ayrıntılı olarak açıklanmaktadır .


</div>

### Edit constraints 

When a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, and if the **Ask for value after creating a dimensional constraint** [preference](Sketcher_Preferences#Display.md) is selected (default), a dialog opens to edit its value.

![](images/Sketcher_Edit_Constraint.png )

You can enter a numerical value or an [expression](Expressions.md), and it is possible to name the constraint to facilitate its use in other expressions. You can also check the **Reference** checkbox to switch the constrain to [reference mode](Sketcher_ToggleDrivingConstraint.md).

To edit the value of an existing dimensional constraint do one of the following:

-   Double-click the constraint value in the [3D view](3D_view.md).
-   Double-click the constraint in the [Sketcher Dialog](Sketcher_Dialog.md).
-   Right-click the constraint in the Sketcher Dialog and select the **Change value** option from the context menu.

### Reposition constraints 

Dimensional constraints can be repositioned in the 3D view by dragging. Hold down the left mouse button over the constraint value and move the mouse. The symbols of geometric constraints are positioned automatically and cannot be moved.

## Profile sketches 

To create a sketch that can be used as a profile for generating solids certain rules must be followed:

-   The sketch must contain only closed contours. Gaps between endpoints, however small, are not allowed.
-   Contours can be nested, to create voids, but should not self-intersect or intersect other contours.
-   Contours cannot share edges with other contours. Duplicate edges must be avoided.
-   T-connections, that is more than two edges sharing a common point, or a point touching an edge, are not allowed.

These rules do not apply to construction geometry (default color blue), which is not shown outside edit mode, or if the sketch is used for a different purpose. Depending on the workbench and the tool that will use the profile sketch, additional restrictions may apply.

## Drawing aids 

The Sketcher Workbench has several drawing aids and other features that can help when creating geometry and applying constraints.

### Continue modes 

There are two continue modes: **Geometry creation \"Continue Mode\"** and **Constraint creation \"Continue Mode\"**. If these are checked (default) in the [preferences](Sketcher_Preferences#Display.md), related tools will restart after finishing. To exit a continuous tool press **Esc** or the right mouse button. This must be repeated if a continuous geometry tool has already received input. You can also exit a continuous tool by starting another geometry or constraint creation tool. Note that pressing **Esc** if no tool is active will exit sketch edit mode. Uncheck the **Esc can leave sketch edit mode** [preference](Sketcher_Preferences#General.md) if you often inadvertently press **Esc** too many times.

### Auto constraints 

In sketches that have **Auto constraints** checked (default) several constraints are applied automatically. The icon of a proposed automatic constraint is shown next to the cursor when it is placed correctly. Left-Clicking will then apply that constraint. This is a per-sketch setting that can be changed in the [Sketcher Dialog](Sketcher_Dialog#Constraints.md) or by changing the **Autoconstraints** [property](Property_editor.md) of the sketch.

The following constraints are applied automatically:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Coincident](Sketcher_ConstrainCoincident.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertical](Sketcher_ConstrainVertical.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangent](Sketcher_ConstrainTangent.md)

-    <small>(v1.0)</small> : <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) (line midpoint)

### Snapping


<small>(v0.21)</small> 

It is possible to [snap](Sketcher_Snap.md) to grid lines and grid intersection, to edges of geometry and midpoints of lines and arcs, and to certain angles. Please note that snapping does not produce constraints in and of itself. For example, only if [Auto constraints](#Auto_constraints.md) is switched on will snapping to an edge produce a [Point on object constraint](Sketcher_ConstrainPointOnObject.md). But just picking a point on the edge would then have the same result.

### On-View-Parameters 


<small>(v1.0)</small> 

Depending on the selected option in the [preferences](Sketcher_Preferences#General.md) only the dimensional On-View-Parameters or both the dimensional and the positional On-View-Parameters can be enabled. Positional parameters allow the input of exact coordinates, for example the center of a circle, or the start point of a line. Dimensional parameters allow the input of exact dimensions, for example the radius of a circle, or the length and angle of a line. On-View-Parameters are not available for all tools.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Determining the center point of a circle with the positional parameters enabled*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Determining the radius of a circle with the dimensional parameters enabled*

If values are entered and confirmed by pressing **Enter** or **Tab**, related constraints are added automatically. If two parameters are displayed at the same time, for example the X and Y coordinate of a point, it is possible to enter one value and pick a point to define the other. Depending on the object additional constraints may be required to fully constrain it. Constraints resulting from On-View-Parameters take precedence over those that may result from [Auto constraints](Sketcher_Dialog#Constraints.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Arc created by entering all On-View-Parameters with resulting automatically created constraints*

### Coordinate display 

If the **Show coordinates beside cursor while editing** [preference](Sketcher_Preferences#Display.md) is checked (default), the parameters of the current geometry tool (coordinates, radius, or length and angle) are displayed next to the cursor. This is deactivated while On-View-Parameters are shown.

## Selection methods 

While a sketch is in edit mode the following selection methods can be used:

### 3D view element selection 

As elsewhere in FreeCAD, an element can be selected in the [3D view](3D_view.md) with a single left mouse click. But there is no need to hold down the **Ctrl** key when selecting multiple elements. Holding down that key is possible though and has the advantage that you can miss-click without losing the selection. Edges, points and constraints can be selected in this manner.

### 3D view box selection 

Box selection in the 3D view works without using [Std BoxSelection](Std_BoxSelection.md) or [Std BoxElementSelection](Std_BoxElementSelection.md):

1.  Make sure that no tool is active.
2.  Do one of the following:
    -   Click in an empty area and drag a rectangle from left to right to select elements that lie completely inside the rectangle.
    -   Click in an empty area and drag a rectangle from right to left to also select elements that touch or cross the rectangle.

You can box-select edges and points, constraints cannot be box-selected.

### 3D view connected geometry selection 


<small>(v1.0)</small> 

Double-clicking an edge in the 3D view will select all edges directly and indirectly connected with that edge via endpoints. There is no need for the edges to be connected with [Coincident constraints](Sketcher_ConstrainCoincident.md), endpoints need only have the same coordinates.

### Sketcher Dialog selection 

Edges and points can also be selected from the Elements section of the [Sketcher Dialog](Sketcher_Dialog.md), and constraints from the Constraints section of that dialog.

## Copy, cut and paste 


<small>(v1.0)</small> 

The standard keyboard shortcuts, **Ctrl**+**C**, **Ctrl**+**X** and **Ctrl**+**V**, can be used to copy, cut and paste selected Sketcher geometry including related constraints. But these tools are also available from the **Sketch → Sketcher tools** menu. They can be used within the same sketch but also between different sketches or separate instances of FreeCAD. Since the data is copied to the clipboard in the form of Python code, it can be used in other ways too (e.g. shared on the forum).

## Tools


<div class="mw-translate-fuzzy">

## Araçlar

Eskiz Tezgahı araçlarının tümü, Eskiz Tezgahını yüklediğinizde görünen Eskiz menüsünde bulunur.


</div>

Some tools are also available from the [3D view](3D_view.md) context menu while a sketch is in edit mode, or from the context menus of the [Sketcher Dialog](Sketcher_Dialog.md).


<small>(v0.21)</small> 

: If a sketch is in edit mode the Structure toolbar is hidden as none of its tools can then be used.

### General

#### Sketcher toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.png‎‎  style="width:32px;"> [Eskiz oluştur](Sketcher_NewSketch/tr.md): Seçilen bir yüz veya düzlemde yeni bir eskiz oluşturur. Bu araç yürütülürken herhangi bir yüz seçilmezse, kullanıcıdan açılır pencereden bir düzlem seçmesi istenir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Eskizi düzenle](Sketcher_EditSketch/tr.md): Seçilen Eskiz\'i düzenler.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.png‎  style="width:32px;"> [Eskizi yüze eşle](Sketcher_MapSketch/tr.md): Bir katının seçilmiş bir yüzüne Eskizi eşler.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Eskizi uyarla](Sketcher_ReorientSketch/tr.md): Eskizin konumunu değiştirmek için kullanılır.


</div>


<div class="mw-translate-fuzzy">

-   [Eskizi kontrol et](Sketcher_ValidateSketch/tr.md): Farklı noktaların toleransını doğrulayın ve ayarlayın.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MergeSketch.png‎  style="width:32px;"> [Eskizleri birleştir](Sketcher_MergeSketches/tr.md): İki veya daha fazla eskizi birleştirin.<small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MirrorSketch.png‎  style="width:32px;"> [Eskizi Aynala](Sketcher_MirrorSketch/tr.md):Bir çizimi x ekseni, y ekseni veya orijini boyunca aynalayın. <small>(v0.16)</small> 


</div>

#### Sketcher Edit Mode toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_LeaveSketch.png  style="width:32px;"> [Eskizden çık](Sketcher_LeaveSketch/tr.md): Eskiz düzenleme modundan çıkar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSketch.png‎  style="width:32px;"> [Eskiz görünümü](Sketcher_ViewSketch/tr.md): Model görünümünü eskiz düzlemine dik olarak ayarlar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSection.png  style="width:32px;"> [Bölümü görüntüle](Sketcher_ViewSection/tr.md): Eskiz düzleminin önünde herhangi bir cismi geçici olarak gizleyen bir bölüm düzlemi oluşturur.<small>(v0.18)</small> 


</div>

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 

#### Other

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Stop operation](Sketcher_StopOperation.md): Stops any currently running geometry or constraint creation tool.



### Eskiz Geometrileri 

Bunlar nesne oluşturma araçlarıdır.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> [Nokta](Sketcher_CreatePoint/tr.md): Nokta çizer.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.png  style="width:32px;"> [Polyline (Çok noktalı çizgi)](Sketcher_CreatePolyline/tr.md): Birden çok çizgi parçasından oluşan bir çizgi çizer. Bir Polyline çizerken M tuşuna basmak, farklı polyline modları arasında geçiş yapar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Line.png  style="width:32px;"> [2 noktadan Çizgi](Sketcher_CreateLine/tr.md): İki nokta arasında Çizgi oluşturur. Çizgiler sonsuz serbestlik derecesine sahiptir.


</div>

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create arc:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Arc.png  style="width:32px;"> [Yay](Sketcher_CreateArc/tr.md): Merkez, yarıçap, başlangıç ​​açısı ve bitiş açısından bir yay parçası çizer.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateArc3Point.png  style="width:32px;"> [3 nokta ile yay çiz](Sketcher_Create3PointArc/tr.md): İki uç noktadan ve çevredeki başka bir noktadan bir yay parçası çizer.


</div>

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md): Creates an arc of ellipse.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Creates an arc of hyperbola.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Creates an arc of parabola.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle/ellipse:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> [Daire](Sketcher_CreateCircle/tr.md): Merkez nokta ve yarıçaptan bir daire çizer.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateCircle3Point.png  style="width:32px;"> [3 nokta ile daire](Sketcher_Create3PointCircle/tr.md): seçilen üç nokta üzerinden geçen bir daire çizer.


</div>

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Creates an ellipse by its center, an endpoint of one of its axes, and a point along the ellipse. <small>(v1.0)</small> : Or by both endpoints of one of its axes and a point along the ellipse.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Creates an ellipse by the endpoints of one of its axes and a point along the ellipse. <small>(v1.0)</small> : This is the same tool as [Ellipse by center](Sketcher_CreateEllipseByCenter.md) but with a different initial mode.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> [Dikdörtgen](Sketcher_CreateRectangle/tr.md): İki zıt noktadan bir dikdörtgen çizer.


</div>

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Centered rectangle](Sketcher_CreateRectangle_Center.md): Creates a centered rectangle. <small>(v1.0)</small> : This is the same tool as [Rectangle](Sketcher_CreateRectangle.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rounded rectangle](Sketcher_CreateOblong.md): Creates a rounded rectangle. Idem.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create regular polygon:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateTriangle.png  style="width:32px;"> [Üçgen](Sketcher_CreateTriangle/tr.md):Bir inşaat geometri dairesi içine bir eşkenar üçgen çizer. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateSquare.png  style="width:32px;"> [Kare](Sketcher_CreateSquare/tr.md): Bir inşaat geometri dairesi içine bir kare çizer. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreatePentagon.png  style="width:32px;"> [Beşgen](Sketcher_CreatePentagon/tr.md): Bir inşaat geometri dairesi içine bir beşgen çizer. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHexagon.png  style="width:32px;"> [Altıgen](Sketcher_CreateHexagon/tr.md): Bir inşaat geometri dairesi içine bir altıgen çizer. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHeptagon.png  style="width:32px;"> [Yedigen](Sketcher_CreateHeptagon/tr.md): Bir inşaat geometri dairesi içine bir yedigen çizer.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOctagon.png  style="width:32px;"> [Sekizgen](Sketcher_CreateOctagon/tr.md):Bir inşaat geometri dairesi içine bir sekizgen çizer. <small>(v0.15)</small> 


</div>

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Regular polygon](Sketcher_CreateRegularPolygon.md): Creates a regular polygon. The number of sides can be specified.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.png  style="width:32px;"> [Yuva](Sketcher_CreateSlot/tr.md): Bir yarım dairenin merkezini ve diğer bir yarım dairenin son noktasını seçerek ikisi arasında bir oval çizer.


</div>

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot.md): Creates an arc slot. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create B-spline:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline by control points](Sketcher_CreateBSpline.md): Creates a B-spline curve by control points. <small>(v1.0)</small> : Or by knot points.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Periodic B-spline by control points](Sketcher_CreatePeriodicBSpline.md): Creates a periodic (closed) B-spline curve by control points. <small>(v1.0)</small> : This is the same tool as [B-spline by control points](Sketcher_CreateBSpline.md) but with a different initial mode.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Creates a B-spline curve by knot points. Idem.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Creates a periodic (closed) B-spline curve by knot points. Idem.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [İnşaat modu](Sketcher_ToggleConstruction/tr.md): Eskiz geometrisini inşaat moduna değiştirir. İnşaat geometrisi mavi renkte gösterilir ve Eskiz düzenleme modunun dışına atılır.


</div>



### Eskiz kısıtlamaları 


<div class="mw-translate-fuzzy">

Kısıtlamalar, uzunlukları tanımlamak, Eskiz öğeleri arasında kuralları belirlemek ve eskizleri dikey ve yatay eksenler boyunca kilitlemek için kullanılır. Bazı kısıtlamalar, [Yardımcı kısıtlamaların](Sketcher_helper_constraint.md) kullanılmasını gerektirir .


</div>

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): Is the context-sensitive constraint tool of the Sketcher Workbench. Based on the current selection, it offers appropriate dimensional constraints, but also geometric constraints. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_HorizontalDistance.png‎  style="width:32px;"> [Yatay uzunluk](Sketcher_ConstrainDistanceX/tr.md):İki nokta veya çizgi bitiş noktaları arasındaki yatay mesafeyi sabitler. Yalnızca bir öğe seçilirse, mesafe orijine ayarlanır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Dikey uzunluk](Sketcher_ConstrainDistanceY/tr.md): 2 nokta veya çizgi bitiş noktası arasındaki dikey uzunluğu sabitler. Yalnızca bir öğe seçilirse, uzunluk orijine ayarlanır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Uzunluk](Sketcher_ConstrainDistance.md): Seçili çizginin uzunluğunu sınırlayarak mesafeyi tanımlar veya aralarındaki uzunluğu sınırlayarak iki nokta arasını tanımlar.


</div>

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto radius/diameter](Sketcher_ConstrainRadiam.md): Fixes the radius of arcs and B-spline weight circles, and the diameter of circles.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Yarıçap](Sketcher_ConstrainRadius/tr.md):Yarıçapı kısıtlayarak, seçilen bir yayın veya dairenin yarıçapını tanımlar.
-   <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [İç Açı](Sketcher_ConstrainAngle/tr.md):Seçilen iki çizgi arasındaki iç açıyı tanımlar.


</div>

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diameter](Sketcher_ConstrainDiameter.md): Fixes the diameter of circles and arcs.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle.md): Fixes the angle between two edges, the angle of a line with the horizontal axis of the sketch, or the aperture angle of a circular arc.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.png‎  style="width:32px;"> [Kilit](Sketcher_ConstrainLock.md): Seçili öğeyi, kökene göre dikey ve yatay mesafeler ayarlayarak sınırlar ve böylece o öğenin konumunu kilitler. Bu kısıtlama mesafeleri daha sonra düzenlenebilir.


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): Creates a coincident constraint between points, fixes points on edges or axes, or creates a concentric constraint. It combines the [Coincident](Sketcher_ConstrainCoincident.md) and [Point on object](Sketcher_ConstrainPointOnObject.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> [Çakıştır](Sketcher_ConstrainCoincident/tr.md):Bir noktaya, bir veya daha fazla noktayı çakıştırır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnObject.png  style="width:32px;"> [Nesne üzerinde nokta](Sketcher_ConstrainPointOnObject/tr.md): Bir noktayı, çizgi, yay veya eksen gibi bir nesne üzerine çakıştırır.


</div>

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Horizontal/vertical constraints:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertical](Sketcher_ConstrainHorVer.md): Constrains lines or pairs of points to be horizontal or vertical, whichever is closest to the current alignment. It combines the [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Horizontal.png  style="width:32px;"> [Yatay](Sketcher_ConstrainHorizontal.md): Seçili çizgileri veya çoklu çizgi öğelerini gerçek bir yatay yönde sınırlar. Bu kısıtlamayı uygulamadan önce birden fazla nesne seçilebilir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Vertical.png  style="width:32px;"> [Dikey](Sketcher_ConstrainVertical/tr.md): Seçilen çizgileri veya çoklu çizgi öğelerini gerçek bir dikey yönlendirmeyle sınırlar. Bu kısıtlamayı uygulamadan önce birden fazla nesne seçilebilir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> [Paralel](Sketcher_ConstrainParallel.md): İki veya daha fazla çizgiyi paralel yaptırarak sınırlar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Perpendicular.png  style="width:32px;"> [Dik](Sketcher_ConstrainPerpendicular/tr.md): İki çizgiyi bir birine dik hale getirir veya bir yay uç noktasına bir çizgiyi dik olarak sınırlar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> [Teğet](Sketcher_ConstrainTangent/tr.md):Seçilen iki varlık arasında teğet bir kısıtlama veya iki çizgi parçası arasında bir eş doğrusal kısıtlama oluşturur. Bir çizgi segmenti, bu yay veya daireyle teğet olmak için doğrudan bir yay veya dairenin üzerinde olmak zorunda değildir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_EqualLength.png  style="width:32px;"> [Eşit](Sketcher_ConstrainEqual/tr.md): Seçilen iki çizimi birbirine eşitler. Eğer daireler veya yaylar seçilirse yarıçapları eşitlenir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> [Simetrik](Sketcher_ConstrainSymmetric/tr.md): Bir çizgi etrafında simetrik olarak iki nokta sınırlar veya seçilen ilk iki noktayı simetrik olarak seçilen üçüncü bir noktaya sınırlar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainBlock.png  style="width:32px;"> [Kısıtlama bloğu](Sketcher_ConstrainBlock.md): Temel olarak, tek bir kısıtlama ile yerinde bir geometrik elemanın bloklanmasını sağlar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_SnellsLaw.png  style="width:32px;"> [Snell yasası](Sketcher_ConstrainSnellsLaw/tr.md):Bir arayüzden geçen ışığı simüle etmek için bir kırılma yasasına uymak için iki satır kısıtlar. <small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Toggle constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstraint.png  style="width:32px;"> [Referans/Çizim değiştir](Sketcher_ToggleDrivingConstraint/tr.md):Araç çubuğunu veya seçilen kısıtlamaları referans moduna /çizim modundan değiştirir.<small>(v0.16)</small> 


</div>

  - <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activate/deactivate constraint](Sketcher_ToggleActiveConstraint.md): Activates or deactivates selected constraints.



### Eskiz araçları 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet/chamfer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> [Kavis](Sketcher_CreateFillet/tr.md):Bir noktada birleştirilmiş iki çizgi arasında bir kavis yapar. Her iki çizgiyi de seçin veya köşe noktasına tıklayın, ardından aracı etkinleştirin.


</div>

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Chamfer](Sketcher_CreateChamfer.md): creates a chamfer between two non-parallel edges. This is the same tool as [Fillet](Sketcher_CreateFillet.md) but with a different initial mode. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Kırpma](Sketcher_Trimming/tr.md): Tıklanan noktaya göre bir çizgi, daire veya yay kırpar.


</div>

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Split](Sketcher_Split.md): Splits an edge while transferring most constraints.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Genişlet](Sketcher_Extend/tr.md): Bir çizgiyi veya bir yayı bir sınır çizgisine, yay, elips, elips yayına veya uzayda bir noktaya genişletir.<small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.png  style="width:32px;"> [Dış geometri](Sketcher_External/tr.md): Dış geometriye bağlı bir kenar oluşturur.


</div>

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> External geometry:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Create external projection geometry](Sketcher_Projection.md): Creates the projection edges of external geometry. <small>(v1.1)</small> 

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Create external intersection geometry](Sketcher_Intersection.md): Creates the intersection edges of external geometry with the sketch plane. <small>(v1.1)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Karbon kopya](Sketcher_CarbonCopy/tr.md):Başka bir çizimin geometrisini kopyalar.<small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.png‎  style="width:32px;"> [Eksen merkez noktasını seç](Sketcher_SelectOrigin.md): Eskizin eksen merkez noktasını seçer.<small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.png‎  style="width:32px;"> [Yatay ekseni seç](Sketcher_SelectHorizontalAxis.md): Eskizin yatay eksenini seçer.<small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.png‎  style="width:32px;"> [Dikey eksen seç](Sketcher_SelectVerticalAxis/tr.md): Eskizin dikey eksenini seçer.<small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Moves or optionally creates copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): Rotates or optionally creates rotated copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Scale transform](Sketcher_Scale.md): Scales or optionally creates scaled copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometry](Sketcher_Offset.md): Creates equidistant edges around selected edges. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.png‎  style="width:32px;"> [Simetri](Sketcher_Symmetry/tr.md): Seçilen bir çizgiye simetrik bir eskiz elemanı kopyalar. <small>(v0.16)</small> 


</div>

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md): Removes the axes alignment of selected edges by replacing [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) constraints with [Parallel](Sketcher_ConstrainParallel.md) and [Perpendicular](Sketcher_ConstrainPerpendicular.md) constraints.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_SelectionTypeInvalid.svg  style="width:32px;"> [Tüm geometriyi sil](Sketcher_DeleteAllGeometry/tr.md):Tüm geometriyi eskizden siler.<small>(v0.18)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_SelectionTypeInvalid.svg  style="width:32px;"> [Tüm kısıtlamaları sil](Sketcher_DeleteAllConstraints.md):Tüm kısıtlamaları çizimden siler. <small>(v0.18)</small> 


</div>

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copy in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Cut in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Paste in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).



### Eskiz B-spline araçları 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Geometriyi B-spline\'a Dönüştür](Sketcher_BSplineApproximate/tr.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Derece arttır](Sketcher_BSplineIncreaseDegree/tr.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md): Decreases the degree (order) of B-splines.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Düğüm çokluğunu arttır](Sketcher_BSplineIncreaseKnotMultiplicity/tr.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Düğüm çokluğunu azalt](Sketcher_BSplineDecreaseKnotMultiplicity/tr.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into a B-spline or increases the multiplicity of an existing knot.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Creates a B-spline by joining two existing B-splines or other edges. <small>(v0.21)</small> 

### Sketcher visual 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [DOF çözücü seç](Sketcher_SelectElementsWithDoFs/tr.md): Yeşil renkte geometriyi serbestlik dereceli (DOF), yani tamamen kısıtlanmayan şekilde vurgular.<small>(v0.18)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.png‎  style="width:32px;"> [Kısıtlamaları seç](Sketcher_SelectConstraints/tr.md): Eskiz elemanının kısıtlamalarını seçer. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.png‎  style="width:32px;"> [Kısıtlanmış öğeleri seç](Sketcher_SelectElementsAssociatedWithConstraints/tr.md): Eskizin kısıtlanmış öğelerini seçer.<small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.png‎  style="width:32px;"> [Gereksiz kısıtlamaları seç](Sketcher_SelectRedundantConstraints/tr.md): Eskizin gereksiz kısıtlamalarını seçer. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.png‎  style="width:32px;"> [Uyumsuz Kısıtlamaları seç](Sketcher_SelectConflictingConstraints/tr.md): Eskizin birbiriyle tutarsız olan kısıtlamalarını seçer.<small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): Shows or hides the circular helpers (underlying virtual circles) for arcs in all sketches. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Show/hide B-spline information layer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [ B-spline derecesini Göster / Gizle](Sketcher_BSplineDegree/tr.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [B-spline kontrol poligonunu Göster/Gizle](Sketcher_BSplinePolygon/tr.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [ B-spline eğrilik tepelerini Göster/Gizle](Sketcher_BSplineComb.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [B-spline düğüm çokluğunu Göster/Gizle](Sketcher_BSplineKnotMultiplicity/tr.md)


</div>

  - <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md): Shows or hides the B-spline control point weight in all sketches.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_Ellipse_All.png‎  style="width:32px;"> [İç geometriyi göster/gizle](Sketcher_RestoreInternalAlignmentGeometry/tr.md):Seçilmiş bir elipsin, elips yayının/hiperbol/parabol veya B-spline\'ın gereksiz iç geometrisini kaybeder/siler.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.png‎  style="width:32px;"> [Sanal alana geç](Sketcher_SwitchVirtualSpace/tr.md): Kısıtlamaları **gizlemenizi** ve onları tekrar görünür hale getirmenizi sağlar.<small>(v0.17)</small>  <https://forum.freecadweb.org/viewtopic.php?f=9&t=26614> bakınız.


</div>

### Obsolete tools 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.png‎  style="width:32px;"> [Klon](Sketcher_Clone/tr.md): Eskiz elemanını klonlar.<small>(v0.16)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.png‎  style="width:32px;"> [CŞekli kapat](Sketcher_CloseShape/tr.md): Bitiş noktalarını çakıştırarak kısıtlanmış kapalı bir şekil oluşturur. <small>(v0.15)</small> 


</div>

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their corner point. Not available in <small>(v1.0)</small> .


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.png‎  style="width:32px;"> \[\[Sketcher ConnectLines/tr\|

Kenarları Bağla\]\]: Uç noktalarını çakıştırarak eskiz elemanlarını bağlar.<small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.png‎  style="width:32px;"> [Kopyala](Sketcher_Copy/tr.md): Eskiz öğesini kopyalar.<small>(v0.16)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Taşı](Sketcher_Move/tr.md): Seçilen geometriyi, seçilen son noktayı referans alarak hareket ettirir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.png‎  style="width:32px;"> [Dikdörtgen dizi](Sketcher_RectangularArray/tr.md): Seçili eskiz öğelerinin dizisini oluşturur.<small>(v0.16)</small> 


</div>




<div class="mw-translate-fuzzy">

### Seçenekler


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Seçenekler\...](Sketcher_Preferences/tr.md): Seçenekler, Eskiz araçlarında tek kullanımlıktır.


</div>

## Best practices 


<div class="mw-translate-fuzzy">

## Öneriler

Her CAD kullanıcısı zaman içinde kendi çalışma tarzını geliştirir, ancak takip edilmesi gereken bazı genel prensipler vardır.


</div>


<div class="mw-translate-fuzzy">

-   Bir dizi basit eskizle çalışmak, tek bir karmaşık olandan daha kolaydır. Örneğin, temel 3D özelliği için bir ilk çizim oluşturulabilir (kalınlık ver veya bir döndürerek), ikincisi ise bir delik veya kesik içerebilir (oyuklar). Bazı detaylar, daha sonra 3D özellikler olarak gerçekleştirilmek üzere bırakılabilir. Çok fazla varsa, eskiziniz de kavislerden kaçınmayı seçebilir ve bunları 3D özellik olarak ekleyebilirsiniz.
-   Her zaman kapalı bir profil oluşturun, aksi halde çiziminiz düzgün olmaz ve bir dizi açık yüz oluşturur. Bazı nesnelerin katı oluşturmaya dahil edilmesini istemiyorsanız, inşaat modu aracıyla bunları inşaat elemanlarına çevirin.
-   Elle eklemeniz gereken kısıtlama sayısını sınırlandırmak için otomatik kısıtlamalar özelliğini kullanın.
-   Genel bir kural olarak, önce geometrik kısıtlamaları, ardından boyutsal kısıtlamaları uygulayın ve eskizinizi en son kilitleyin. Ancak unutmayın: kurallar çiğnenmek içindir. Eskizinizle ilgili sorun yaşıyorsanız, profilinizi tamamlamadan önce birkaç nesneyi kısıtlamak faydalı olabilir.
-   Mümkünse, eskizinizi kilit sınırlamasıyla başlangıç ​​noktasına (0,0) ortalayın. Çiziminiz simetrik değilse, noktalarından bir orijini bulun veya kilitleme mesafeleri için güzel yuvarlak sayılar seçin. V0.12\'de, harici sınırlamalar (eskiz kenarları gibi mevcut 3D geometriye veya diğer çizimlere sınırlama) uygulanmaz. Bu, aşağıdaki eskiz geometrisini ilk eskizinize göre bulmak için ilk eskizinize göre mesafeleri elle ayarlamanız gerektiği anlamına gelir. Orijine göre (25,75) bir kilit kısıtlaması (23.47,73.02) \'den daha kolay hatırlanır.
-   Uzunluk sınırlaması ile Yatay/Dikey uzunluk sınırlamaları arasında seçim yapma olanağınız varsa, ikincisini tercih edin. Yatay ve Dikey Mesafe kısıtlamaları hesaplamak daha kolaydır.
-   Genel olarak, kullanılacak en iyi kısıtlamalar şunlardır: Yatay ve Dikey Kısıtlamalar; Yatay ve Dikey Uzunluk Kısıtlamaları; Noktadan Noktaya Teğet. Mümkünse, bunların kullanımından kaçının: genel Uzunluk Kısıtlaması; Kenardan Kenara Teğet; Noktayı Çizgi Kısıtlamasına Onar; Simetri Kısıtlaması.


</div>




<div class="mw-translate-fuzzy">

## Kılavuzlar


</div>

-   [Sketcher Lecture](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. This is a more than 80 page PDF document that serves as a detailed manual for the Sketcher. It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.
-   [Basic Sketcher Tutorial](Basic_Sketcher_Tutorial.md) for beginners
-   [Sketcher Micro Tutorial - Constraint Practices](Sketcher_Micro_Tutorial_-_Constraint_Practices.md)
-   [Sketcher requirement for a sketch](Sketcher_requirement_for_a_sketch.md) Minimum requirement for a sketch and Complete determination of a sketch

## Scripting

The [Sketcher scripting](Sketcher_scripting.md) page contains examples on how to create constraints from Python scripts.

## Examples

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/tr
