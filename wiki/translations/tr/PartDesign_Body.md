---
 GuiCommand:
   Name: Cisim Oluştur
   Icon: PartDesign_Body_Create_New.svg
   Workbenches: PartDesign Workbench/tr
   MenuLocation: Parça tasarım , Cisim Oluştur
   Version/tr: 0.17
   SeeAlso: Std Part/tr
---

# PartDesign Body/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

**Cisim Oluştur** Eskizler, veriler ve parça tasarım ile ilgili bir dizi [özellikleri](Glossary#Feature.md) içeren tek bir bitişik katı oluşturur. Özellikler tarafından referans olarak kullanılabilecek bir Orijin (standart düzlem ve eksenlerle) sağlar. Ayrıca, özel özellikleri taşımaya gerek kalmadan bir birim olarak serbestçe hareket ettirilebilir.


</div>

The Body provides an **Origin** object which includes local X, Y, and Z axes, and standard planes. These elements can be used as references to attach [sketches](Sketch.md) and [primitive objects](PartDesign_CompPrimitiveAdditive.md).

Do not confuse the <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md) with the <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Std Part](Std_Part.md). The first one is a specific object used in the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), intended to model a [single contiguous solid](PartDesign_Body#Single_contiguous_solid.md) by means of [PartDesign Features](PartDesign_Feature.md). The [Std Part](Std_Part.md) is a grouping object intended to create [assemblies](assembly.md); it is not used for modelling, just to arrange different objects in space. Multiple bodies, and other [Std Parts](Std_Part.md), can be placed inside a single [Std Part](Std_Part.md) to create a complex assembly.

![](images/PartDesign_Body_tree.png ) ![](images/PartDesign_Body_example.png ) 
*Left: the tree view showing the features that sequentially produce the final shape of the object. Right: the final object visible in the [3D view](3D_view.md).*

## Nasıl kullanılır 

If no previous solid is selected:

1.  Press the **<img src="images/PartDesign_Body.svg" width=16px> [Body](PartDesign_Body.md)** button. An empty Body is created and automatically becomes **[active](PartDesign_Body#Active_status.md)**.
2.  Now you can press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)** to create a [sketch](Sketch.md) in the Body that can be used with **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Pad](PartDesign_Pad.md)**.
3.  Alternatively, add a primitive [PartDesign Feature](PartDesign_Feature.md), for example, **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Additive box](PartDesign_AdditiveBox.md)**.

If a solid object is selected:

1.  Press the **<img src="images/PartDesign_Body.svg" width=16px> [Body](PartDesign_Body.md)** button. A new Body is created containing a single **Base Feature**. This Base Feature element is a simple reference to another object previously created or imported into the document. See [Base Feature](PartDesign_Body#Base_Feature.md) for more information. An existing Body or [PartDesign Feature](PartDesign_Feature.md) cannot be selected when pressing **<img src="images/PartDesign_Body.svg" width=16px> [Body](PartDesign_Body.md)**.

### Notes

-   If no Body currently exists when **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)** is pressed, a new Body will be automatically created. If a Body already exists, it has to be made active before using **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)**.
-   Double-click the Body in the [tree view](tree_view.md) or open the context menu (right-click) and select **Toggle active body** to activate or deactivate the Body. If another Body is active, it will be deactivated. See [active status](PartDesign_Body#Active_status.md) for more information.

## Özellikler

A [PartDesign Body](PartDesign_Body.md) (`PartDesign::Body` class) is derived from a [Part Feature](Part_Feature.md) (`Part::Feature` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [Part Feature](Part_Feature.md), the PartDesign Body has the following properties in the [property editor](property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Tip|Link**: the [PartDesign Feature](PartDesign_Feature.md) defined as \"Tip\", which is usually the last feature created in the Body. The Tip indicates the final shape of the Body, which is shown in the [3D view](3D_view.md) when **Display Mode Body** is set to `Tip`. See [Tip](PartDesign_Body#Tip.md) for more information.

-    **Base Feature|Link**: an external shape used as the first [PartDesign Feature](PartDesign_Feature.md) in the Body. It is usually set when dragging a solid object into an empty Body. If no solid is imported in this way, this property will be empty. See [Base Feature](PartDesign_Body#Base_Feature.md) for more information.

-    **Placement|Placement**: the position of the object in the [3D view](3D_view.md). The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md).

-    **Group|LinkList**: a list with the [PartDesign Features](PartDesign_Feature.md) in the Body.

#### Hidden properties Data 

-    **Origin|Link**: the [App Origin](App_OriginGroupExtension.md) object that is the positional reference for all elements listed in **Group**.

-    **_ Group Touched|Bool**: whether the group is touched or not.

Also the hidden properties described in [Part Feature](Part_Feature.md).

### View


<div class="mw-translate-fuzzy">

-    **Display Mode Body**: Ekranı iki mod arasında ayarlar:

    -   Üzerinden (varsayılan), cismin içindeki her şey (özellikler, veriler, eskizler vb.) görünür. Cismin içine özellikler eklemek ve düzenlemek için kullanılan moddur.
    -   Tip , ayarlanan tipe göre sadece vücudun şeklini gösterir; eskizler dahil diğer her şey görünümden gizlenir ve görüntülenemez. Pratik kullanım: \"Tip\", diğer tezgahlardan operasyonlar oluşturmak için cismin kenarlarının ve yüzlerinin seçimine izin verir.

-    **Tip**: Tip olarak tanımlanan özelliği görüntüler / ayarlar.

-    **Base Feature**: Temel özellik olarak kullanılan harici şekli görüntüler/ayarlar. Bir Parça tasarım özelliği temel özellik ise geçerli değildir.

-    **Placement**: Cismin 3D uzayda yönünü ve konumunu belirtir. [Yerleşim](Placement.md) bölümüne bakınız.

-    **Label**:Etiket işleme verilen addır. Bu ad, istediğiniz zaman değiştirilebilir.

-    **Group**:Cismin içindeki referans verilen nesneleri listeler.


</div>

-    **Display Mode Body|Enumeration**: sets the display mode specifically for the Body with one of two types.

    -   
        `Through`
        
        (default) exposes all objects inside the Body, that is, [sketches](Sketch.md), [PartDesign Features](PartDesign_Feature.md), datum objects, etc. This mode allows visualizing partial operations done inside the Body, and thus it is the recommended mode when adding and editing features. Select the specific feature, and the set **Visibility** to `True` or press the **Space** bar on the keyboard.

    -   
        `Tip`
        
        exposes only the final shape of the Body, which is defined by the **Tip** property. Everything else, including [sketches](Sketch.md), [partial features](PartDesign_Feature.md), datums, etc., is not displayed, even if they are visible in the [tree view](tree_view.md). This mode is recommended when the Body does not need to be modified further, so a fixed shape is shown. This mode is also recommended when you wish to select the sub-elements (vertices, edges, and faces) of the final shape to use with other workbenches\' tools.

## Body concept 

### Single contiguous solid 

A PartDesign Body is intended to model a single contiguous solid. The meaning of \"contiguous\" is an element made in one piece, with no moving parts, or disconnected solids. Examples of contiguous solids are those that are manufactured from a single piece of raw material by a process of casting, cutting, or milling. For example, a nut, a washer, and a bolt each consists of a single solid piece of steel with no moving parts, so each can be modelled by a PartDesign Body. Objects that are created by welding two pieces can also be modelled by a single Body as long as the weld joint is not intended to break apart.

Once these contiguous solids are put together in some type of arrangement, then they become an \"assembly\". In an assembly, the objects are not fused together, but they are simply \"stacked\" or placed next to each other, and remain individual parts.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*Left: three individual contiguous solids, each of them modelled by a PartDesign Body. Right: the individual Bodies put together in an assembly.*

### Feature editing 

A PartDesign Body is intended to work by creating an initial solid, either from a [sketch](Sketch.md) or from a [primitive shape](PartDesign_CompPrimitiveAdditive.md), and then modifying it through [\"features\"](PartDesign_Feature.md) to add or remove material from the previous shape. For a full explanation go to [feature editing](feature_editing.md).

A PartDesign Body will perform an automatic [fusion](Part_Fuse.md) (union) of the solid elements inside of it. This means that (1) partial solids should be touching when created, and (2) disconnected solids are not allowed.

<img alt="" src=images/PartDesign_Body_two_intersection.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_two_fusion.png  style="width:" height="200px;"> 
*Left: two individual solids that intersect each other. Right: a single PartDesign Body with two [additive features](PartDesign_Feature.md); they are automatically fused together, so instead of intersecting, they form a single contiguous solid.*

![](images/PartDesign_Body_non-contiguous.png ) 
*Left: two disconnected solids; this isn't a valid PartDesign Body. Right: two touching solids; this results in a valid PartDesign Body. The newer [feature](PartDesign_Feature.md) should always contact or intersect the previous feature so that it is fused to it, and becomes a single contiguous solid.*


**Note:**

other CAD programs like Catia allow discontiguous solids in the same \"Body\". As of v0.19, FreeCAD does not allow this. There has been discussions in the [FreeCAD forum](https://forum.freecadweb.org/index.php) about lifting this restriction but no concrete decision has been made. If you\'d like to know more or present different points of view, please discuss in the [forum](https://forum.freecadweb.org/index.php).

## Detailed explanation of the properties 


<div class="mw-translate-fuzzy">

### Aktif Durum 

Bir FreeCAD belgesi birden fazla Cisim içerebilir. Bu nedenle, belirli bir Cisme yeni bir özellik eklemek için aktif hale getirilmesi gerekir. Aktif bir gövde, ağaç görünümünde açık mavi bir arka plan rengiyle gösterilecektir. V0.18\'de, Model ağacındaki etiketi de koyu renkli olarak gösterilecektir.


</div>

An open document can contain multiple Bodies. To add a new feature to a specific Body, it needs to be made **active**. An active body will be displayed in the [tree view](tree_view.md) with the background color specified by the **Active container** value in the [preferences editor](Preferences_Editor#Colors.md) (by default, light blue). An active body will also be shown in bold text.

To activate or de-activate a Body:

-   Double click on it on the [tree view](tree_view.md), or
-   Open the context menu (right click) and select **Toggle active body**.


<div class="mw-translate-fuzzy">

Bir Cismi etkinleştirmek, aynı zamanda aktif çalışma tezgahı değilse, arayüzü otomatik olarak Parça tasarım tezgahına da geçirir.


</div>

![](images/PartDesign_Body_active.png )



*Document with two PartDesign Bodies, of which the second one is active.*


<div class="mw-translate-fuzzy">

### Orijin

Orijin, üç standart eksenden (X, Y, Z) ve üç standart düzlemden (XY, XZ ve YZ) oluşur. Eskizler bu düzlemlere eklenebilir. Parça içindeki tüm unsurlar Parça\'nın orijini ile ilişkilendirilir; bu, Parçanın, içerisindeki öğelerin yerleşimini etkilemeden, küresel koordinat sistemine göre hareket ettirilebileceği ve döndürülebileceği anlamına gelir.


</div>

The Origin consists of the three standard axes (X, Y, Z) and three standard planes (XY, XZ and YZ). [Sketches](Sketch.md) and other objects can be attached to these elements when creating them.

1.  Create the Body.
2.  If the Body is selected in the [tree view](tree_view.md), press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)**; the [task panel](task_panel.md) will open to allow selecting one of the planes.
3.  If the Body is not selected, select the Origin instead and make it visible in the [3D view](3D_view.md) by pressing the **Space** bar in the keyboard. Also expand the Origin object to see the axes and planes.
4.  Select one of the planes, either in the [tree view](tree_view.md) or in the [3D view](3D_view.md), then press **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [New sketch](PartDesign_NewSketch.md)**. The sketch will be created on the chosen plane.

The same process can be used when creating auxiliary datum geometry like [PartDesign Lines](PartDesign_Line.md), [PartDesign Planes](PartDesign_Plane.md), and [PartDesign CoordinateSystems](PartDesign_CoordinateSystem.md).


**Note:**

the Origin is an [App Origin](App_OriginGroupExtension.md) object (`App::Origin` class), while the axes and planes are objects of type `App::Line` and `App::Plane` respectively. Each of these elements can be hidden and unhidden individually with the **Space** bar; this is useful to choose the correct reference when creating other objects.


**Note 2:**

all elements inside the Body are referenced to the Body\'s Origin which means that the Body can be moved and rotated in reference to the global coordinate system without affecting the placement of the elements inside.

<img alt="" src=images/PartDesign_Body_Origin_tree.png ) ![](images/PartDesign_Body_Origin_view.png  style="width:" height="400px;">



*Left: PartDesign Body Origin in the [tree view](tree_view.md). Right: representation of the Origin elements in the [3D view](3D_view.md).*


<div class="mw-translate-fuzzy">

### Temel Özellik 

Temel özellik, tanım gereği Cisim\'de oluşturulan ilk Parça tasarım özelliğidir. Ancak, eski tezgahların ve diğer özelliklerin eklenebileceği bir temel özellik olarak, diğer tezgahlarda içe eklenen veya modellenen katı bir şekil kullanmak mümkündür.


</div>

The Base Feature is the first [PartDesign Feature](PartDesign_Feature.md) in the Body when the Body is based on another solid shape. This solid can be created by any workbench, or imported from an external file, for example, a STEP file.

![](images/PartDesign_Body_BaseFeature_tree.png ) 
*PartDesign Bodies, each of them with a single Base Feature, which are taken from previously created solids.*

To create the Base Feature:

1.  select a solid shape external to any Body, and
2.  press **[<img src=images/PartDesign_Body.svg style="width:16px"> [Body](PartDesign_Body.md)**; this will create a new Body with a single Base Feature.


**Note:**

you can\'t select an existing Body, or any of its [features](PartDesign_Feature.md), when pressing **[<img src=images/PartDesign_Body.svg style="width:16px"> [Body](PartDesign_Body.md)**.

If you already have a Body, you can create the Base Feature in this way:

-   in the [tree view](tree_view.md), pick an object, and drag and drop it inside the Body, or
-   in the [property editor](property_editor.md), edit the value of **Base Feature** by pressing the ellipsis **...**, and choosing an object from the list. In this case you can choose an existing Body to be the Base Feature.


**Note:**

dragging and dropping only works for Bodies which don\'t have a Base Feature already.


**Note 2:**

if the Body already has several features, when you drag and drop the external solid, the Base Feature will be created at the beginning of the list of features, that is, it will be added to the beginning of the **Group** property.

The Base Feature is entirely optional; it is only present when including an object from outside the Body. If no external solid is included, you can still build your shape using [sketches](Sketch.md), [pads](PartDesign_Pad.md), [primitive objects](PartDesign_CompPrimitiveAdditive.md), and other [PartDesign Features](PartDesign_Feature.md). In this case the **Base Feature** property remains empty.

![](images/PartDesign_Body_BaseFeature_Tip.svg )



*Left: PartDesign Body with a Base Feature that is taken from an external solid object, and many subsequent [PartDesign Features](PartDesign_Feature.md) on top. Right: Body which doesn't have an explicit Base Feature.*


**Note:**

If another PartDesign body is selected as a BaseFeature it must have a shape. If it is empty (no features, no BaseFeature, \...) this will result in error.


<div class="mw-translate-fuzzy">

### İpucu

İpucu, Cismin dışında kalan özelliktir. Ağacın altındaki son özelliğe otomatik olarak ayarlanır. Ancak bazen, Cisim ağacında daha önceki bir özelliğe geçmek için yararlı olabilir; o zaman daha önce eklenmiş olması gereken özellikleri eklemek mümkündür. Cisim ağacında, ipucu için ayarlanan özellik, içinde beyaz bir aşağı ok bulunan yeşil bir nokta görüntüler.


</div>

The Tip is the [PartDesign Feature](PartDesign_Feature.md) that is exposed outside the Body; that is, if another tool from any workbench (for example, **[<img src=images/Part_SimpleCopy.svg style="width:16px"> [Part SimpleCopy](Part_SimpleCopy.md)** or **[<img src=images/Part_Cut.svg style="width:16px"> [Part Cut](Part_Cut.md)**) needs to use the shape of the Body, it will use the shape of the Tip. Said in another way, the Tip is the final representation of the Body as if the parametric history didn\'t exist.

![](images/PartDesign_Body_Tip_final.svg )



*Left: PartDesign Body with full parametric history including intermediate features. Right: the Tip is the final shape that can be exported from the Body, while omitting the model's history.*

The Tip is automatically set to the last feature created in the Body. Nevertheless, it can also be set to any of the intermediate features by opening the [tree view](tree_view.md) context menu (right-click) and choosing **[<img src=images/PartDesign_MoveTip.svg style="width:16px"> [Set tip](PartDesign_MoveTip.md)**, or by changing the Body\'s **Tip** value in the [property editor](property_editor.md).

Changing the Tip in effect rolls back its history, making it possible to add features that should have been added earlier. It also exposes a different shape to external tools.


<div class="mw-translate-fuzzy">

Daha fazla detay için <img alt="" src=images/PartDesign_MoveTip.png  style="width:24px;"> [İpucu Taşı](PartDesign_MoveTip/tr.md) sayfasına bakınız.


</div>

![](images/PartDesign_Body_Tip_tree.png ) 
*Two PartDesign Bodies, each of them with [PartDesign Features](PartDesign_Feature.md). The Tip is the last feature in them, and is marked with an overlay symbol.*


<div class="mw-translate-fuzzy">

### Diğer tezgahlarla etkileşim 

Varsayılan olarak, bir Cisim altındaki nesneler seçilebilir ve bu elbette Parça tasarım\'daki özellikleri düzenlemek ve eklemek için gereklidir. Ancak , sonuçlar beklenmedik olabileceğinden, diğer tezgahlardan ([Parça](Part_Workbench.md) veya [Taslak](Draft_Workbench.md) gibi) işlemler oluşturmak için bir Cismin özelliklerini seçmek önerilmez; Her durumda, \"Bağlantılar izin verilen kapsam dışına çıkıldı\", şeklinde bir hata Rapor görünümünde görünecektir.


</div>

By default, [PartDesign Features](PartDesign_Feature.md) inside a Body are selectable, as this is required to edit and add more features with the [PartDesign Workbench](PartDesign_Workbench.md) tools. Nevertheless, selecting the individual features to use them with tools from other workbenches, like [Part](Part_Workbench.md) and [Draft](Draft_Workbench.md), is not advised, as the results may be unexpected; if this is done, in the [report view](Report_view.md) an error message may appear, **Links go out of the allowed scope**.


<div class="mw-translate-fuzzy">

Bu nedenle, diğer tezgahlarla etkileşimler için, Model ağacından yalnızca Cismin kendisi seçilmelidir. Gövde üzerinde belirli bir topoloji seçmenin gerekli olduğu durumlarda (tepe, kenar, yüz), Cismin Görüntüleme Modu Gövde görünümü özelliği, Geçiş (varsayılan) ile Uç arasında değiştirilebilir . Bu özelliğe Görünüm panelinden erişilebilir. Gelen Öneri modunda Gövde altında nesnelere erişimi (özellikler, veriler, eskizler) devre dışıdır; İpucu özelliği dışındaki her şey, hangi nesne görünür olarak ayarlanmış olursa olsun 3D görünümde gizlenir.


</div>


<div class="mw-translate-fuzzy">

Diğer tezgahlarda işlemler tamamlandıktan sonra, Cismi düzenleyebilmek için, **Cismi görüntüle modu** özelliğini sıfırlamayı unutmayın.


</div>

![](images/PartDesign_Body_Tip_Display_mode.svg )



*Left: when "Display Mode Body" is set to `Through* it is possible to select and perform operations with the individual [PartDesign Features](PartDesign_Feature.md); in general, this is not recommended. Right: when "Display Mode Body" is set to {{incode|Tip` all selections and operations done on the Body will be done on the Tip, making sure only the final shape of the Body is exposed.}}


<div class="mw-translate-fuzzy">

### Görünürlük Yönetimi 

Cismin görünürlüğü, içerdiği herhangi bir cismin görünürlüğünün yerini alır. Cisim gizliyse, görünürlükleri true olarak ayarlanmış olsa bile içerdiği nesneler de gizlenir. Bir seferde yalnızca bir özellik görünebilir. Gizli bir özellik seçmek ve boşluk çubuğuna basmak onu görünür hale getirecek ve daha önce görünen özelliği otomatik olarak gizleyecektir.


</div>

The Body\'s visibility supersedes the visibility of any object it contains. If the Body is hidden, the objects it contains will be hidden as well, even if their individual **Visibility** property is set to `True`.

Multiple [Sketches](Sketch.md) may be visible at one time, but only one [PartDesign Feature](PartDesign_Feature.md) (solid result) can be visible at a time. Selecting a hidden feature and pressing the **Space** bar in the keyboard will make it visible, and automatically hide the previously visible feature.

![](images/PartDesign_Body_Visibility.png ) 
*PartDesign Body: multiple [Sketches](Sketch.md) may be visible simultaneously, but only one solid [PartDesign Feature](PartDesign_Feature.md) may be visible at one time, whether it is the Tip or not.*

### Attachment

[PartDesign Features](PartDesign_Feature.md), just like [planar objects](Part_Part2DObject.md), can be attached to different planes, usually the standard planes defined by the Body\'s [Origin](PartDesign_Body#Origin.md), or to custom [PartDesign Planes](PartDesign_Plane.md).

[Sketches](Sketch.md) are normally attached to a plane when they are created. In similar way, [primitive features](PartDesign_CompPrimitiveAdditive.md) can also be attached. Attaching these objects to a plane allows them to be moved within the Body by changing their **Attachment Offset** property. For more information on the attachment modes see [Part EditAttachment](Part_EditAttachment.md).

A [PartDesign Feature](PartDesign_Feature.md) that is not attached will be shown with a red overlay symbol next to their icon in the [tree view](tree_view.md).

![](images/PartDesign_Body_Feature_attachment.png ) 
*PartDesign Body: [PartDesign Features](PartDesign_Feature.md) that are not attached to a plane or coordinate system will be shown with an overlay symbol next to their icon in the [tree view](tree_view.md).*

### Inheritance

A [PartDesign Body](PartDesign_Body.md) is formally an instance of the class `PartDesign::Body`, whose parent is [Part Feature](Part_Feature.md) (`Part::Feature` class) through the intermediate `Part::BodyBase` class, and is augmented with an Origin extension.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `PartDesign::Body* object is intended to build parametric 3D solids, and thus is derived from the basic {{incode|Part::Feature` object, and has an Origin to control the placement of the features used inside of it.}}

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the document

A PartDesign Body is created with the `addObject()` method of the document. Once a Body exists, [PartDesign Features](PartDesign_Feature.md) can be added to it with the `addObject()` or `addObjects()` methods of this Body.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj.Label = "Custom label"

feat1 = App.ActiveDocument.addObject("PartDesign::AdditiveBox", "Box")
feat2 = App.ActiveDocument.addObject("PartDesign::AdditiveCylinder", "Cylinder")

obj.addObjects([feat1, feat2])
App.ActiveDocument.recompute()
```

In a document that has many Bodies, the [active Body](PartDesign_Body#Active_status.md) can be set using the `setActiveObject` method of the `ActiveView`. The first argument is the fixed string `"pdbody"`, and the second argument is the Body object that should be made active. 
```python
import FreeCAD as App
import FreeCADGui as Gui

doc = App.newDocument()
obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("PartDesign::Body", "Body")

Gui.ActiveDocument.ActiveView.setActiveObject("pdbody", obj1)
App.ActiveDocument.recompute()
```





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Body/tr
