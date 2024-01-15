# <img alt="Sketcher workbench icon" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/tr






## Giriş


<div class="mw-translate-fuzzy">

[Eskiz tezgahı](Sketcher_Workbench/tr.md); [Parça tasarım tezgahı](PartDesign_Workbench/tr.md), [Yapı tezgahı](Arch_Workbench/tr.md) ve diğer tezgahlarda kullanılmak üzere 2D geometriler üretir. Genel olarak, bir 2D geometrisi çoğu CAD modelinin başlangıç ​​noktası olarak kabul edilir, çünkü bir 2D çizimi, 3D şekli oluşturmak için \"ekstrüzyona sokulabilir\"; Önceden oluşturulmuş 3D şekillerin üstünde oyuklar, çıkıntılar veya ekstrüzyonlar gibi başka özellikler oluşturmak için başka 2D çizimler de kullanılabilir. [Parça Tezgahında](Part_Workbench/tr.md) tanımlanan katılarda, Boolean işlemleri ile birlikte Eskiz, üretken katı şekilli tasarımın çekirdeğini oluşturur.


</div>


<div class="mw-translate-fuzzy">

Eskiz tezgahı, 2D şekillerin kesin geometrik tanımları izlemesine izin veren \"kısıtlamalara\" sahiptir. Bir kısıtlayıcı çözücü, 2D geometrinin kısıtlı boyutunu hesaplar ve çizim serbestlik derecelerinin etkileşimli olarak araştırılmasını sağlar.


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*
Tamamen kısıtlanmış bir eskiz*

## Basics of constraint sketching 


<div class="mw-translate-fuzzy">

## Kısıtlı eskizin temelleri 

Eskizin nasıl çalıştığını anlamak için, onu \"geleneksel\" taslak ile karşılaştırmak faydalı olabilir.


</div>

#### Traditional Drafting 


<div class="mw-translate-fuzzy">

#### Geleneksel Taslak 

CAD taslağının geleneksel yolu eski [çizim tahtasından](http://en.wikipedia.org/wiki/Drawing_board) miras kalmıştır. [Ortogonal (2D) görünümler](http://en.wikipedia.org/wiki/Multiview_orthographic_projection) elle çizilir, teknik çizimler (aynı zamanda planlar olarak da bilinir) üretmek için tasarlanmıştır. Nesneler tam olarak istenen boyuta veya ölçülere çekilir. (0,0) \'dan başlayarak 100mm uzunluğunda yatay bir çizgi çizmek istiyorsanız, çizgi aracını etkinleştirin, ekrana tıklayın veya ilk nokta için (0,0) koordinatlarını girin, ardından ikinci bir tıklama yapın ikinci nokta koordinatlarını (100,0) girin. Veya çizginizi konumuna bakmadan çizer ve daha sonra hareket ettirirsiniz. Geometrilerinizi çizmeyi tamamladığınızda, onları ölçülendirirsiniz..


</div>

#### Constraint Sketching 


<div class="mw-translate-fuzzy">

#### Kısıtlı Eskiz 

**Eskiz** bu mantıktan uzaktır. Nesnelerin tam olarak istediğiniz gibi çizilmesi gerekmez, çünkü bunlar daha sonra kısıtlamalar ile tanımlanacaktır. Nesneler gelişigüzel bir şekilde çizilebilir ve kısıtlanmadıkları sürece değiştirilebilir. \"Yüzer\" durumunda ve hareket ettirilebilir, gerilebilir, döndürülebilir, ölçeklendirilebilir vb. Bu, tasarım sürecinde büyük esneklik sağlar.


</div>

#### What are constraints? 


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

#### What the Sketcher is not good for 


<div class="mw-translate-fuzzy">

#### Eskiz nerelerde kullanılmaz 

Eskiz, 2D planlar üretmek için tasarlanmamıştır. Eskizler, katı bir özellik oluşturmak için kullanıldığında, otomatik olarak gizlenir. Kısıtlamalar yalnızca Eskiz düzenleme modunda görülebilir.


</div>


<div class="mw-translate-fuzzy">

Çıktı almak için yalnızca 2D görünümler oluşturmanız gerekiyorsa ve 3D modeller oluşturmak istemiyorsanız, [Taslak tezgahını](Draft_Workbench/tr.md) inceleyin.


</div>

The tool [Draft2Sketch](Draft_Draft2Sketch.md) converts a Draft object to a Sketch object, and vice versa. Many tools that require a 2D element as input work with either type of object as an internal conversion is done automatically.

## Sketching Workflow 


<div class="mw-translate-fuzzy">

## Eskiz iş akışı 

Bir Eskiz her zaman 2 boyutludur (2D). Bir katı oluşturmak için, önce kapalı bir alandan oluşan 2D Eskiz\'i oluşturulur, daha sonra kalınlık ver veya Döndür komutlarıyla 3D boyut eklenir. Böylece 2D Eskiz\'den bir 3D katı oluşturulur.


</div>


<div class="mw-translate-fuzzy">

Eskiz, birbirine geçen bölümlere sahipse, bölüm üzerinde olmayan bir noktada veya bitişik bölümlerin bitiş noktaları arasında boşluk bulunan yerler, **Kalınlık ver**\' veya **Döndür** işlemleriyle bir katı oluşturmaz. Bu kuralın istisnası, Yapı (mavi) Geometri için geçerli olmamasıdır.


</div>


<div class="mw-translate-fuzzy">

Kapalı alanda daha küçük,alanla örtüşmeyen alanlara sahip olabiliriz. Bunlar, 3D katı oluşturulduğunda geçersiz olur.


</div>

Once a Sketch is fully constrained, the Sketch features will turn green; Construction Geometry will remain blue. It is usually \"finished\" at this point and suitable for use in creating a 3D solid. However, once the Sketch dialog is closed it may be worthwhile going to <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) and running **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Check geometry](Part_CheckGeometry.md)** to ensure there are no features in the Sketch which may cause later problems.

## Tools


<div class="mw-translate-fuzzy">

## Araçlar

Eskiz Tezgahı araçlarının tümü, Eskiz Tezgahını yüklediğinizde görünen Eskiz menüsünde bulunur.


</div>


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

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Stop operation](Sketcher_StopOperation.md): When in edit mode, stop the current operation, whether that is drawing, setting constraints, etc.



### Eskiz Geometrileri 

Bunlar nesne oluşturma araçlarıdır.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePoint.png  style="width:32px;"> [Nokta](Sketcher_CreatePoint/tr.md): Nokta çizer.


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

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Circle.png  style="width:32px;"> [Daire](Sketcher_CreateCircle/tr.md): Merkez nokta ve yarıçaptan bir daire çizer.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateCircle3Point.png  style="width:32px;"> [3 nokta ile daire](Sketcher_Create3PointCircle/tr.md): seçilen üç nokta üzerinden geçen bir daire çizer.


</div>

-   <img alt="" src=images/Sketcher_Conics.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create conic:

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse by center](Sketcher_CreateEllipseByCenter.md): Draws an ellipse by center point, major radius point and minor radius point.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse by 3 points](Sketcher_CreateEllipseBy3Points.md): Draws an ellipse by major diameter (2 points) and minor radius point.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc of ellipse](Sketcher_CreateArcOfEllipse.md): Draws an arc of ellipse by center point, major radius point, starting point and ending point.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc of hyperbola](Sketcher_CreateArcOfHyperbola.md): Draws an arc of hyperbola.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc of parabola](Sketcher_CreateArcOfParabola.md): Draws an arc of parabola.

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> B-spline:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline by control points](Sketcher_CreateBSpline.md): Draws a B-spline curve by its control points.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Periodic B-spline by control points](Sketcher_CreatePeriodicBSpline.md): Draws a periodic (closed) B-spline curve by its control points.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Draws a B-spline curve by its knots. <small>(v0.21)</small> 

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Draws a periodic (closed) B-spline curve by its knots. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.png  style="width:32px;"> [Polyline (Çok noktalı çizgi)](Sketcher_CreatePolyline/tr.md): Birden çok çizgi parçasından oluşan bir çizgi çizer. Bir Polyline çizerken M tuşuna basmak, farklı polyline modları arasında geçiş yapar.


</div>

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateRectangle.png  style="width:32px;"> [Dikdörtgen](Sketcher_CreateRectangle/tr.md): İki zıt noktadan bir dikdörtgen çizer.


</div>

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Centered rectangle](Sketcher_CreateRectangle_Center.md): Draws a rectangle from a central point and an edge point. <small>(v0.20)</small> 

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rounded rectangle](Sketcher_CreateOblong.md): Draws a rounded rectangle from 2 opposite points. <small>(v0.20)</small> 

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

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Regular polygon](Sketcher_CreateRegularPolygon.md) : Draws a regular polygon by selecting the number of sides and picking two points: the center and one corner.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.png  style="width:32px;"> [Yuva](Sketcher_CreateSlot/tr.md): Bir yarım dairenin merkezini ve diğer bir yarım dairenin son noktasını seçerek ikisi arasında bir oval çizer.


</div>

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot.md): TBD. <small>(v0.22)</small> 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.png  style="width:32px;"> [Kavis](Sketcher_CreateFillet/tr.md):Bir noktada birleştirilmiş iki çizgi arasında bir kavis yapar. Her iki çizgiyi de seçin veya köşe noktasına tıklayın, ardından aracı etkinleştirin.


</div>

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their (virtual) intersection.

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.png  style="width:32px;"> [Kırpma](Sketcher_Trimming/tr.md): Tıklanan noktaya göre bir çizgi, daire veya yay kırpar.


</div>

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Split](Sketcher_Split.md): Splits an edge into two while keeping most of the constraints. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Genişlet](Sketcher_Extend/tr.md): Bir çizgiyi veya bir yayı bir sınır çizgisine, yay, elips, elips yayına veya uzayda bir noktaya genişletir.<small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.png  style="width:32px;"> [Dış geometri](Sketcher_External/tr.md): Dış geometriye bağlı bir kenar oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Karbon kopya](Sketcher_CarbonCopy/tr.md):Başka bir çizimin geometrisini kopyalar.<small>(v0.17)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.png  style="width:32px;"> [İnşaat modu](Sketcher_ToggleConstruction/tr.md): Eskiz geometrisini inşaat moduna değiştirir. İnşaat geometrisi mavi renkte gösterilir ve Eskiz düzenleme modunun dışına atılır.


</div>



### Eskiz kısıtlamaları 

Kısıtlamalar, uzunlukları tanımlamak, Eskiz öğeleri arasında kuralları belirlemek ve eskizleri dikey ve yatay eksenler boyunca kilitlemek için kullanılır. Bazı kısıtlamalar, [Yardımcı kısıtlamaların](Sketcher_helper_constraint.md) kullanılmasını gerektirir .

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): TBD. <small>(v0.22)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnPoint.png  style="width:32px;"> [Çakıştır](Sketcher_ConstrainCoincident/tr.md):Bir noktaya, bir veya daha fazla noktayı çakıştırır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_PointOnObject.png  style="width:32px;"> [Nesne üzerinde nokta](Sketcher_ConstrainPointOnObject/tr.md): Bir noktayı, çizgi, yay veya eksen gibi bir nesne üzerine çakıştırır.


</div>

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Constrain horizontally or vertically:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/Vertical](Sketcher_ConstrainHorVer.md): TBD. <small>(v0.22)</small> 


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

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): TBD. <small>(v0.22)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.png‎  style="width:32px;"> [Kilit](Sketcher_ConstrainLock.md): Seçili öğeyi, kökene göre dikey ve yatay mesafeler ayarlayarak sınırlar ve böylece o öğenin konumunu kilitler. Bu kısıtlama mesafeleri daha sonra düzenlenebilir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_HorizontalDistance.png‎  style="width:32px;"> [Yatay uzunluk](Sketcher_ConstrainDistanceX/tr.md):İki nokta veya çizgi bitiş noktaları arasındaki yatay mesafeyi sabitler. Yalnızca bir öğe seçilirse, mesafe orijine ayarlanır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_VerticalDistance.png  style="width:32px;"> [Dikey uzunluk](Sketcher_ConstrainDistanceY/tr.md): 2 nokta veya çizgi bitiş noktası arasındaki dikey uzunluğu sabitler. Yalnızca bir öğe seçilirse, uzunluk orijine ayarlanır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Length.png  style="width:32px;"> [Uzunluk](Sketcher_ConstrainDistance.md): Seçili çizginin uzunluğunu sınırlayarak mesafeyi tanımlar veya aralarındaki uzunluğu sınırlayarak iki nokta arasını tanımlar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_Radius.png  style="width:32px;"> [Yarıçap](Sketcher_ConstrainRadius/tr.md):Yarıçapı kısıtlayarak, seçilen bir yayın veya dairenin yarıçapını tanımlar.
-   <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> [İç Açı](Sketcher_ConstrainAngle/tr.md):Seçilen iki çizgi arasındaki iç açıyı tanımlar.


</div>

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diameter](Sketcher_ConstrainDiameter.md): Defines the diameter of an arc or circle.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Auto radius/diameter](Sketcher_ConstrainRadiam.md): Defines the radius of an arc, the diameter of a circle or the weight of a B-spline pole. <small>(v0.20)</small> 

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle.md): Defines the internal angle between two selected lines.

#### Special constraints 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Constraint_SnellsLaw.png  style="width:32px;"> [Snell yasası](Sketcher_ConstrainSnellsLaw/tr.md):Bir arayüzden geçen ışığı simüle etmek için bir kırılma yasasına uymak için iki satır kısıtlar. <small>(v0.15)</small> 


</div>

#### Constraint tools 

The following tools can be used the change the effect of constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstraint.png  style="width:32px;"> [Referans/Çizim değiştir](Sketcher_ToggleDrivingConstraint/tr.md):Araç çubuğunu veya seçilen kısıtlamaları referans moduna /çizim modundan değiştirir.<small>(v0.16)</small> 


</div>

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activate/deactivate constraint](Sketcher_ToggleActiveConstraint.md): Enable or disable an already placed constraint.



### Eskiz araçları 


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


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_Ellipse_All.png‎  style="width:32px;"> [İç geometriyi göster/gizle](Sketcher_RestoreInternalAlignmentGeometry/tr.md):Seçilmiş bir elipsin, elips yayının/hiperbol/parabol veya B-spline\'ın gereksiz iç geometrisini kaybeder/siler.


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

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometry](Sketcher_Offset.md): Adds an equidistant outline around selected edges. <small>(v0.22)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): TBD. <small>(v0.22)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.png‎  style="width:32px;"> [Simetri](Sketcher_Symmetry/tr.md): Seçilen bir çizgiye simetrik bir eskiz elemanı kopyalar. <small>(v0.16)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.png‎  style="width:32px;"> [Klon](Sketcher_Clone/tr.md): Eskiz elemanını klonlar.<small>(v0.16)</small> 


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

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Remove axes alignment](Sketcher_RemoveAxesAlignment.md): Remove axes alignment while trying to preserve the constraint relationship of the selection. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_SelectionTypeInvalid.svg  style="width:32px;"> [Tüm geometriyi sil](Sketcher_DeleteAllGeometry/tr.md):Tüm geometriyi eskizden siler.<small>(v0.18)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Element_SelectionTypeInvalid.svg  style="width:32px;"> [Tüm kısıtlamaları sil](Sketcher_DeleteAllConstraints.md):Tüm kısıtlamaları çizimden siler. <small>(v0.18)</small> 


</div>



### Eskiz B-spline araçları 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Geometriyi B-spline\'a Dönüştür](Sketcher_BSplineApproximate/tr.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Derece arttır](Sketcher_BSplineIncreaseDegree/tr.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md): Decreases the degree (order) of a B-spline.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Düğüm çokluğunu arttır](Sketcher_BSplineIncreaseKnotMultiplicity/tr.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Düğüm çokluğunu azalt](Sketcher_BSplineDecreaseKnotMultiplicity/tr.md)


</div>

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into an existing B-spline. <small>(v0.20)</small> 

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Joins two curves at selected end points. <small>(v0.21)</small> 

### Sketcher visual 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.png‎  style="width:32px;"> [Sanal alana geç](Sketcher_SwitchVirtualSpace/tr.md): Kısıtlamaları **gizlemenizi** ve onları tekrar görünür hale getirmenizi sağlar.<small>(v0.17)</small>  <https://forum.freecadweb.org/viewtopic.php?f=9&t=26614> bakınız.


</div>


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

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Show/hide B-spline control point weight](Sketcher_BSplinePoleWeight.md): Shows or hides the display of the weights for the control points of a B-spline.

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): TBD. <small>(v0.22)</small> 

### Obsolete tools 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.png‎  style="width:32px;"> [CŞekli kapat](Sketcher_CloseShape/tr.md): Bitiş noktalarını çakıştırarak kısıtlanmış kapalı bir şekil oluşturur. <small>(v0.15)</small> 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.png‎  style="width:32px;"> \[\[Sketcher ConnectLines/tr\|

Kenarları Bağla\]\]: Uç noktalarını çakıştırarak eskiz elemanlarını bağlar.<small>(v0.15)</small> 


</div>




<div class="mw-translate-fuzzy">

### Seçenekler


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;"> [Seçenekler\...](Sketcher_Preferences/tr.md): Seçenekler, Eskiz araçlarında tek kullanımlıktır.


</div>

## Best Practices 


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

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. This is a 70-page long PDF document that serves as a detailed manual for the sketcher. It explains the basics of Sketcher usage, and goes into a lot of detail about the creation of geometrical shapes, and each of the constraints.
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


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/tr
