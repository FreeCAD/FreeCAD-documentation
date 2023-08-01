---
- GuiCommand:
   Name:Path Helix
   Name/tr:CNC G-Kodu Helezon
   Workbenches:[CNC G-Kodu](Path_Workbench/tr.md)
   MenuLocation:CNC G-Kodu - Helezon
   Shortcut:
   SeeAlso:
---

# Path Helix/tr


</div>



## Açıklama


<div class="mw-translate-fuzzy">

Helezon komutu, İş\'e bir sarmal enterpolasyon İşlemi ekler. Saat yönünde Helezon enterpolasyon çıkışı (G2) G Kodu komutları. Saat yönünün tersine çıkış (G3) G Kodu komutları. Aşama Yüzdesi, eşmerkezli geçişi, Alet çapının yüzdesi olarak belirtir.


</div>



## Kullanımı


<div class="mw-translate-fuzzy">

-   CNC G-Kodu-\> menüsünden veya GUI Düğmesinden Helezon aracını seçin ve tuşuna basın.
-   Açılır seçim iletişim penceresinden bir Takım denetleyicisi seçin ve OK tuşuna basarak onaylayın.
-   İş Modelinde mevcut olan tüm delikler, Temel Geometri sekmesinde listelenen işlemler için uygun olacaktır. Listenin işleme yönelik deliklerle eşleştiğini doğrulayın ve gerekirse ekleme, etkinleştirme veya devre dışı bırakma ayarlarını yapın. Deliklerin duvar yüzlerini seçerek delikler eklenebilir.
-   Derinliklerin, Son Derinliklerin doğru olduğundan emin olun ve değilse düzeltin.
-   Yüksekliklerin, Güvenli ve Boşluk Yüksekliklerinin doğru olduğundan emin olun ve değilse ayarlayın.
-   İşlem sekmesinde, Başlangıç Noktası, Yön ve Adım Üstü yüzdesini belirtin.


</div>

## Options

Extra Offset adds a margin of material to be left unmachined. This is typically to allow a light finishing pass as a separate operation.

## Comments

-   Step Down is not respected exactly. It is always rounded to give a complete number of turns from Start Depth to Final Depth.
-   Similarly Step Over is not respected exactly. It is always rounded to give a number of equal steps.

The feedrate parameter is constant across all cuts and is based on the position of the tool\'s axis, thus actual feedrate of the cutting edge of the tool can vary considerably between the inner most cut and the outside surface. If the job dimensions produce a path diameter smaller than the tool diameter, this can lead to much faster cutting speeds than the feedrate given for the tool in the tool controller. This may need to considered when selecting \"feed and speeds\" for the job.

## Properties

### Data

Empty

### View

Empty

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Helix/tr
