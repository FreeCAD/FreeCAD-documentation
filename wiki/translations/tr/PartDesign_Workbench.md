# <img alt="PartDesign workbench icon" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/tr


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

## Giriş

[Parça tasarım tezgahı](PartDesign_Workbench/tr.md) karmaşık katı parçaları modelleme için gelişmiş araçlar sağlar. Genel amaç olarak, üretilebilecek parçaların modellenmesi ve bu parçaların birleştirilerek ürün elde edilmesi hedeflenir. Bununla birlikte, oluşturulan katılar genel olarak [Mimari tasarım](Arch_Workbench/tr.md) , [FE analizi](FEM_Workbench/tr.md) veya 3D baskı gibi herhangi bir başka amaç için kullanılabilir .


</div>


<div class="mw-translate-fuzzy">

Parça tasarım tezgahı ve [Eskiz tezgahı](Sketcher_Workbench/tr.md) birbirleriyle bağlantılıdırlar. Kullanıcı normalde bir Eskiz oluşturur, sonra bir katı oluşturmak için [Kalınlık ver](PartDesign_Pad/tr.md) aracını kullanır ve ardından bu katı üzerinde istenen işlemler yapılır.


</div>


<div class="mw-translate-fuzzy">

[Parça tezgahı](Part_Workbench/tr.md), [Yapısal katı geometri](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (CSG) şekil oluşturma metodolojisi üzerine temellendiğinden, Part tasarım tezgahı, parametrik, özellik düzenleme metodolojisi kullanır; bu, temel bir katı, nihai şekil elde edilinceye kadar üstüne özellikler ekleyerek sırayla dönüştürülür. Bu işlemin daha ayrıntılı bir açıklaması için [özellik düzenleme](feature_editing/tr.md) sayfasına bakın ve ardından katı madde oluşturma işlemine başlamak için [Parça tasarım tezgahı ile basit bir parça](Creating_a_simple_part_with_PartDesign/tr.md) oluşturma bölümüne bakın .


</div>

A more detailed discussion of Part workbench versus Part Design workbench can be found here: [Part and Part Design](Part_and_PartDesign.md).

The bodies created with PartDesign are often subject to the [topological naming problem](Topological_naming_problem.md) which causes internal features to be renamed when the parametric operations are modified. This problem can be minimized by following the best practices described in the [feature editing](feature_editing.md) page, and by taking advantage of datum objects as support for sketches and features.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">

## Araçlar


<div class="mw-translate-fuzzy">

Parça Tasarım tezgahının araçlarının tümü , Parça tasarım tezgahını yüklediğinizde görünen **Parça Tasarımı** menüsünde ve Parça tasarım araç çubuğunda bulunur.


</div>

### Yapı araçları 


<div class="mw-translate-fuzzy">

Bu araçlar, Model ağacını düzenlemek için kullanılan araçlardır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_Part.png  style="width:32px;"> [Parça oluştur](Std_Part/tr.md): Aktif belgeye yeni bir Parça ekler veya varolan bir parçayı aktif hale getirir.
-   <img alt="" src=images/Group.svg  style="width:32px;"> [Grup oluştur](Std_Group/tr.md): Aktif belgenin Model ağacına bir Grup ekler.


</div>

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Group](Std_Group.md): adds a Group container in the active document, which allows organizing the objects in the [tree view](Tree_view.md).

### Parça Tasarım Yardım Araçları 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Body.png  style="width:32px;"> [Cisim oluştur](PartDesign_Body/tr.md): Aktif belge de yeni bir cisim oluşturur veya mevcut cismi etkinleştirir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_NewSketch.png  style="width:32px;"> [Eskiz oluştur](PartDesign_NewSketch/tr.md): Seçilen bir yüzey ya da düzlem üzerinde yeni bir eskiz oluşturur. Bu araç yürütülürken yüz seçilmezse, kullanıcıdan, Görevler panelinden bir düzlem seçmesi istenir. Arayüz daha sonra eskiz düzenleme modunda [Eskiz tezgahına](Sketcher_Workbench/tr.md) geçer.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.png  style="width:32px;"> [Eskizi düzenle](Sketcher_EditSketch/tr.md): Seçili eskizi düzenler.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.png‎  style="width:32px;"> [Eskizi yüze eşle](Sketcher_MapSketch/tr.md): Eskizleri önceden seçilen bir düzleme veya aktif cismin bir yüzüne eşler.


</div>

### Parça Tasarım modelleme araçları 

#### Referans araçları 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Point.png  style="width:32px;"> [Referans noktası oluştur](PartDesign_Point/tr.md): Etkin gövde de bir referans noktası oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Line.png  style="width:32px;"> [Referans çizgisi oluştur](PartDesign_Line/tr.md): Etkin gövde de bir referans çizgisi oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Plane.png  style="width:32px;"> [Referans düzlemi oluştur](PartDesign_Plane/tr.md): Etkin gövde de bir referans düzlemi oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   ![ 32px](images/_PartDesign_CoordinateSystem.png ) [ Yerel bir koordinat sistemi oluştur](PartDesign_CoordinateSystem/tr.md):: aktif gövdede referans geometrisine bağlı yerel bir koordinat sistemi oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_ShapeBinder.png  style="width:32px;"> [Şekil bağlayıcı oluştur](PartDesign_ShapeBinder/tr.md): Etkin gövde de bir şekil bağlayıcı oluşturur.


</div>

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Create a sub-object(s) shape binder](PartDesign_SubShapeBinder.md): creates a shape binder to a subelement, like edge or face from another body, while retaining the relative position of that element. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Clone.png  style="width:32px;"> [Klon oluştur](PartDesign_Clone/tr.md): Seçilen cismin bir klonunu oluşturur.


</div>

#### Ekleme araçları 

Bunlar, temel özellikler oluşturmak veya mevcut bir katı gövdeye malzeme eklemek için kullanılan araçlardır.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> [Kalınlık ver](PartDesign_Pad/tr.md): Seçilen bir eskize kalınlık vererek bir katı oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Revolution.png  style="width:32px;"> [Döndür](PartDesign_Revolution/tr.md): Eskizi bir eksenin etrafında döndürerek bir katı oluşturur. Eskiz kapalı bir profil olmalıdır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_AdditiveLoft.png  style="width:32px;"> [Eskizlerle katı oluştur](PartDesign_AdditiveLoft/tr.md): İki veya daha fazla eskiz arasında geçiş yaparak sağlam bir yapı oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_AdditivePipe.png  style="width:32px;"> [Eskizi süpürerek katı oluştur](PartDesign_AdditivePipe/tr.md): Açık veya kapalı bir yol boyunca bir veya daha fazla eskiz süpürerek bir katı oluşturur.


</div>

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Additive helix](PartDesign_AdditiveHelix.md): creates a solid by sweeping a sketch along a helix. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   [Temel bir geometrik cisim ekle](PartDesign_CompPrimitiveAdditive/tr.md): Etkin gövdeye temel geometrik cisim(silindir, küp vb.) ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveBox.png  style="width:32px;"> [Kutu ekle](PartDesign_AdditiveBox/tr.md): Etkin gövdeye kutu ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveCylinder.png  style="width:32px;"> [Silindir ekle](PartDesign_AdditiveCylinder/tr.md): Etkin gövdeye silindir ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveSphere.png  style="width:32px;"> [Küre ekle](PartDesign_AdditiveSphere/tr.md): Etkin gövdeye küre ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveCone.png  style="width:32px;"> [Koni ekle](PartDesign_AdditiveCone/tr.md): Etkin gövdeye koni ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveEllipsoid.png  style="width:32px;"> [Elipsoit ekle](PartDesign_AdditiveEllipsoid/tr.md): Etkin gövdeye elipsoit ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveTorus.png  style="width:32px;"> [Halka ekle](PartDesign_AdditiveTorus/tr.md): Halka ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditivePrism.png  style="width:32px;"> [Prizma ekle](PartDesign_AdditivePrism/tr.md): Etkin gövdeye prizma ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_AdditiveWedge.png  style="width:32px;"> [Kama ekle](PartDesign_AdditiveWedge/tr.md): Kama ekler.


</div>

#### Çıkarma araçları 

Bunlar, mevcut bir gövdeden materyal çıkarmak için kullanılan araçlardır.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Pocket.png  style="width:32px;"> [Oyuk](PartDesign_Pocket/tr.md): Seçilen eskize göre cismi oyar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Hole.png  style="width:32px;"> [Delik](PartDesign_Hole/tr.md): Seçilen eskize göre cisim üzerinde delik açar. Eskiz, bir veya daha fazla daire içermelidir.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Groove.png  style="width:32px;"> [Oluk](PartDesign_Groove/tr.md): Bir eskizi bir eksen etrafında döndürerek bir oluk oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_SubtractiveLoft.png  style="width:32px;"> [Eskizlerle çıkar](PartDesign_SubtractiveLoft/tr.md):İki veya daha fazla eskiz arasında geçiş yaparak katı bir şekil oluşturur ve onu aktif gövdeden çıkarır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_SubtractivePipe.png  style="width:32px;"> [Eskizi süpürerek çıkar](PartDesign_SubtractivePipe/tr.md): Açık veya kapalı bir yol boyunca bir veya daha fazla eskizi süpürerek katı bir şekil oluşturur ve onu aktif gövdeden çıkarır.


</div>

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtractive helix](PartDesign_SubtractiveHelix.md): creates a solid shape by sweeping a sketch along a helix and subtracts it from the active body. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   [Temel bir geometrik şekil çıkar](PartDesign_CompPrimitiveSubtractive/tr.md): Aktif gövdeye çıkarıcı bir cisim ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveBox.png  style="width:32px;"> [Kutu çıkar](PartDesign_SubtractiveBox/tr.md): Aktif gövdeye bir çıkarıcı kutu ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveCylinder.png  style="width:32px;"> [Silindir çıkar](PartDesign_SubtractiveCylinder/tr.md):Aktif gövdeye bir çıkarıcı silindir ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveSphere.png  style="width:32px;"> [Küre çıkar](PartDesign_SubtractiveSphere/tr.md): Aktif gövdeye bir çıkarıcı küre ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveCone.png  style="width:32px;"> [Koni çıkar](PartDesign_SubtractiveCone/tr.md) Aktif gövdeye bir çıkarıcı koni ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveEllipsoid.png  style="width:32px;"> [Elipsoit çıkar](PartDesign_SubtractiveEllipsoid/tr.md):Aktif gövdeye bir çıkarıcı elipsoit ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveTorus.png  style="width:32px;"> [Halka çıkar](PartDesign_SubtractiveTorus/tr.md): Aktif gövdeye bir çıkarıcı halka ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractivePrism.png  style="width:32px;"> [Prizma çıkar](PartDesign_SubtractivePrism/tr.md):Aktif vücuda bir çıkarıcı prizma ekler.


</div>


<div class="mw-translate-fuzzy">

:\*<img alt="" src=images/PartDesign_SubtractiveWedge.png  style="width:32px;"> ‎[Kama çıkar](PartDesign_SubtractiveWedge/tr.md):Aktif gövdeye bir çıkarıcı kama ekler.


</div>

#### Dönüştürme araçları 

Bunlar mevcut özellikleri dönüştürmek için kullanılan araçlardır. Hangi özellikleri dönüştüreceğinizi seçmenize izin vereceklerdir.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Mirrored.png  style="width:32px;"> [Yansıt](PartDesign_Mirrored/tr.md):Düzlem veya yüze bir veya daha fazla özellik yansıtır.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_LinearPattern.png  style="width:32px;"> [Doğrusal şablon](PartDesign_LinearPattern/tr.md): Bir veya daha fazla özelliğe dayalı doğrusal bir şablon oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_PolarPattern.png  style="width:32px;"> [Kutupsal şablon](PartDesign_PolarPattern/tr.md):Bir veya daha fazla özellikten oluşan kutupsal bir şablon oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_MultiTransform.png  style="width:32px;"> [Çoklu dönüştürme](PartDesign_MultiTransform/tr.md):Diğer dönüştürmelerin kombinasyonu ile bir şablon oluşturur.


</div>

#### Süsleme araçları 

Bu araçlar seçilen kenarlara veya yüzlere bir işlem uygular.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Fillet.png  style="width:32px;"> [Yuvarla](PartDesign_Fillet/tr.md): Aktif gövdenin kenarlarını yuvarlar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Chamfer.png  style="width:32px;"> [Pah kır](PartDesign_Chamfer/tr.md): Aktif gövdenin kenarlarına pah kırar.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Draft.png  style="width:32px;"> [Taslak](PartDesign_Draft/tr.md): Aktif gövdenin seçilen yüzlerine taslak uygular.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Thickness.png  style="width:32px;"> [Kalınlık](PartDesign_Thickness/tr.md):Aktif gövdeden kalın bir kabuk oluşturur ve seçilen yüzleri açar.


</div>

#### Boolean


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Boolean.png  style="width:32px;"> [Boolean işlemi](PartDesign_Boolean/tr.md):Aktif gövdeye bir veya daha fazla cisim veya Parça tasarım kopyası alır ve bir Boolean işlemi uygular.


</div>

#### Ekstralar

Parça Tasarım menüsünde bulunan bazı ek işlevler:


<div class="mw-translate-fuzzy">

-   [Taşıma(Migrate)](PartDesign_Migrate.md): eski FreeCAD sürümleriyle oluşturulan dosyaları dönüştürür. Eğer dosya saf Parça tasarım özellik-tabanlıysa, dönüşüm başarılı olacaktır. Eğer dosya Parça/Parça tasarım/Taslak nesnelerinin karışımıysa, işlem genellikle başarısız olur.


</div>

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Sprocket](PartDesign_Sprocket.md): creates a sprocket profile that can be padded. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_InternalExternalGear.png  style="width:32px;"> [İçten Dişli Çark](PartDesign_InvoluteGear/tr.md): Bir Pad tarafından kullanılabilecek bir içten dişli çark profili oluşturur.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_WizardShaft.png  style="width:32px;"> [Mil tasarım sihirbazı](PartDesign_WizardShaft/tr.md): Değer tablosundan bir mil oluşturur. Mil üzerindeki kuvvetleri ve momentleri analiz etmeyi sağlar. Mil, düzenlenebilir bir döner kroki ile yapılır.


</div>


<div class="mw-translate-fuzzy">

### Bağlamsal menü araçları 


</div>

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Set tip](PartDesign_MoveTip.md): redefines the tip, which is the feature exposed outside of the Body.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Move object to other body](PartDesign_MoveFeature.md): moves the selected sketch, datum geometry or feature to another Body.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Move object after other object](PartDesign_MoveFeatureInTree.md): allows reordering of the Body tree by moving the selected sketch, datum geometry or feature to another position in the list of features.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_MoveTip.png  style="width:32px;"> [Uç Ayarla](PartDesign_MoveTip/tr.md): Gövde dışında açık kalmış uç kısmı yeniden tanımlar.


</div>

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Appearance](Std_SetAppearance.md): determines appearance of the whole part (color transparency etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Set colors](Part_FaceColors.md): assigns colors to part faces.


<div class="mw-translate-fuzzy">

### Seçenekler


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgParameter.png  style="width:32px;">[Seçenekler\...](PartDesign_Preferences/tr.md):Seçenekler, Parça tasarım araçlarından ulaşılabilir.


</div>

## Kılavuz


<div class="mw-translate-fuzzy">

-   [FreeCAD nasıl kullanılır(dili ingilizce)](http://help-freecad-jpg87.fr/), Mekanik tasarım hakkında içeriği zayıf bir site.
-   [Parça tasarım sürüm 0.17 ile basit bir parça tasarımı](Creating_a_simple_part_with_PartDesign/tr.md)
-   [Temel parça tasarım kılavuzu 017](Basic_Part_Design_Tutorial_017/tr.md)
-   [PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I/tr.md) (Güncellenmesi gerekiyor)
-   [PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II/tr.md) (Güncellenmesi gerekiyor)


</div>


<div class="mw-translate-fuzzy">


{{docnav/tr|[Parça tezgahı](Part_Workbench.md)|[CNC g-kodu tezgahı](Path_Workbench/tr.md)}}


{{Userdocnavi/tr}}


</div>


 {{PartDesign_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/tr
