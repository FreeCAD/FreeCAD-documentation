---
- GuiCommand:
   Name:PartDesign NewSketch
   Name/tr:Eskiz oluştur
   Workbenches:[PartDesign](PartDesign_Workbench/tr.md)
   MenuLocation:PartDesign → Eskiz oluştur
   Version:0.17
---

# PartDesign NewSketch/tr


</div>



## Tanım


<div class="mw-translate-fuzzy">

Bu araç yeni bir eskiz oluşturur, mevcut değilse taslak içeren yeni bir [Cisim oluşturur](PartDesign_Body/tr.md) ve oluşturulduktan sonra [Eskiz tezgahını](Sketcher_Workbench/tr.md) otomatik olarak açar.


</div>


<div class="mw-translate-fuzzy">

[Parça tasarım tezgahını](PartDesign_Workbench/tr.md) kullanarak modeller oluştururken , bu araç Eskiz tezgahında bulunan [Eskiz Oluştur](Sketcher_NewSketch/tr.md) aracına tercih edilmelidir .


</div>



## Nasıl kullanılır 


<div class="mw-translate-fuzzy">

1.  Parça tasarım araç çubuğunda **[<img src=images/PartDesign_NewSketch.png style="width:24px">** tuşuna basınız.

2.  Görevler panelinde, **Özellik seç** diyalogu açılır. Listede veya daha iyi görünürlük için yeniden yönlendirilebilecek 3D görünümündeki düzlemlerden birini seçin.

3.  
    **Tamam**tuşuna basın.

4.  Arayüz otomatik olarak Eskiz tezgahına geçer ve eskiz düzenlenebilir. Eskizden çıktıktan sonra, arayüz Parça tasarım tezgahına geri getirilir ve eskizden önce 3D görünüm durumuna geri yüklenir.

5.  Alternatif olarak, eskiz oluşturulmadan önce mevcut aktif yapı üzerindeki bir düzlem veya yüz seçilebilir, bu durumda eskiz anında oluşturulur.


</div>



## Seçenekler

-   Mevcut bir eskiz ekini değiştirmek için **Harita Modu** özelliğini değiştirin.( [Özellikler](#Properties.md) bkz.)

-   The *Select feature* Dialog defines the features of the new sketch

:   

    :   <img alt="" src=images/PartDesign.CreateSketch.SelectFeatureDialog.jpeg  style="width:300px;">
    :   *Select feature* dialog. These settings create a sketch on the XY plane and allow cross-references from other items of the same body

Dialog settings

-   Coordinate system box: defines the orientation of the sketch plane
-   Allow Used Features: *TBD*

:   Allow external features options

-   From other bodies of the same part: any elements used in the same body can be referenced
-   From different parts or free features: *TBD*
-   Make independent copy: all other elements will be separate copies, i.e. they will not change when the original changes.
-   Make dependent copy: the elements will be copies, but a dependency to the original elements is kept. This is basically using a [Shapebinder](PartDesign_ShapeBinder.md)
-   Create cross-reference: the linked elements will not be copies, but point to the original elements, e.g. a master sketch. Any changes are reflected to this sketch

To reference any items in the [Workbench Sketcher](Sketcher_Workbench.md) use the **<img src="images/Sketcher_External.svg" width=16px> [External Geometry](Sketcher_External.md)** and **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [CarbonCopy](Sketcher_CarbonCopy.md)** tools. Generally it is recommended to use other sketches as source for references rather than faces or edges, because they are less affected by the Topological Naming Issue.



## Özellikler


<div class="mw-translate-fuzzy">

-    **Map Mode**:Eskizin başka bir nesneye, genellikle bir düzlem veya yüze eklenme şekli, ancak başka tür nesneler olabilir. Bir **...** düğmesini görmek için alana bir kez tıklayın ve [Ek](Part_EditAttachment.md) iletişim kutusunu açmak için basın. Devre dışı bırakıldıysa, Yerleşim özelliği etkindir.

-    **Placement**: Çizimin 3D alanda yönünü kontrol eder; [yerleşime](Std_Placement/tr.md) bakınız. Eskiz Harita Modu özelliği üzerinden eklenmişse devre dışı bırakılır.


</div>








{{PartDesign Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign NewSketch/tr
