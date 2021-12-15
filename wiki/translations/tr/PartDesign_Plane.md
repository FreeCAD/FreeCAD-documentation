---
- GuiCommand:/tr
   Name:PartDesign Plane
   Name/tr:Referans düzlemi oluştur
   Workbenches:[Parça tasarım](PartDesign_Workbench/tr.md)
   MenuLocation:Parça tasarım → Referans düzlemi oluştur
   Version:0.17
   SeeAlso:[Referans noktası oluştur](PartDesign_Point.md), [Referans çizgisi oluştur](PartDesign_Line.md)
---

# PartDesign Plane/tr


</div>

## Tanım

Eskizler veya diğer referans geometri için referans olarak kullanılabilecek bir **referans düzlemi** oluşturur. Eskizler referans düzlemlerine eklenebilir. ![](images/Datum_plane.png ) \"Referans Düzlemi, XY Düzlemi olarak referans düzlemi kullanılarak çizilen bir Silindir ile Küpün 3 köşesini geçiyor.\"


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 


</div>

A datum plane, as of FreeCAD 0.18, can only be created inside of a <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [Body](PartDesign_Body.md). Every body has an origin, which is hidden by default. To be able to refer to the origin base planes, make the the origin visible. You can do this before creating a datum plane.


<div class="mw-translate-fuzzy">

1.  
    **<img src="images/PartDesign_Plane.png" width=24px> '''Referans düzlemi oluştur'''**\'a basın.

2.  Düzlem parametrelerini tanımlayın. Kullanılabilir ek modları filtrelemek için 3D görünümünde bir ilk referans seçin.

3.  Seçilen referansa bağlı olarak, listede mevcut olan bir veya daha fazla ek mod olabilir. En muhtemel olanı otomatik olarak seçilir ve listede kalın harflerle gösterilir. Metin moduyla Ekli eki modu adıyla birlikte Parametreler panelin üst kısmında yeşil renkte görünür.

4.  Ek bir referans eklemek için sonraki **Referans** düğmesine basın. Bir kez basıldığında, etiket bir seçim yapılıncaya kadar **Seçiliyor\...** olarak değişir.

5.  Listeden bir ek mod seçin.

6.  Ek Ofset değerlerini tanımlayın.

7.  
    **Tamam**\'a basın.


</div>


<div class="mw-translate-fuzzy">

## Seçenekler


</div>


<div class="mw-translate-fuzzy">

Model ağacındaki Referans düzlemi etiketine çift tıklayın veya sağ tıklayın ve parametrelerini düzenlemek için bağlam menüsünde **Referans Düzenle** seçeneğini seçin . Ek mod ve Ek ofset hakkında daha fazla bilgi için[Ek](Part_EditAttachment.md) bkz.


</div>


<div class="mw-translate-fuzzy">

## Özellikler


</div>


<div class="mw-translate-fuzzy">

-    **MapMode**:Kullanılan ek modu listeler.

-    **Attachment Offset**:Ataşman yerleşimine atıfta bulunan bir dönüştürme (çeviri ve döndürme) uygular.

-    **Label**: Nesneye verilen ad, bu ad uygun şekilde değiştirilebilir.


</div>

-    **MapMode**: lists the attachment mode used.

-    **Attachment Offset**: applies a transformation (translation and rotation) in reference to the attachment placement.

-    **Label**: name given to the object, this name can be changed at convenience.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Plane/tr
