---
- GuiCommand:
   Name:Sketcher MapSketch
   Name/tr:Eskizi yüze eşle
   Workbenches:[Sketcher](Sketcher_Workbench.md), [PartDesign](PartDesign_Workbench.md)
   MenuLocation:Part Design/Sketch - Map sketch to face...
   SeeAlso:[Create a new sketch](Sketcher_NewSketch.md)
---

# Sketcher MapSketch/tr


</div>

## Description


<div class="mw-translate-fuzzy">

## Tanım

Bu araç, mevcut bir eskizi şeklin yüzüne eşler. Bu eskizden oluşturulan parça tasarım özellikleri, ilave özellikler (kalınlık ver, Döndürerek) için alttaki katı ile kaynaşacak veya çıkarma özellikleri durumunda (Oyuk, Oluk) temeldeki katıdan çıkarılacaktır.


</div>

Lütfen bu aracın yeni eskizler oluşturmak için kullanılmadığını unutmayın. Yalnızca mevcut bir eskizi Bir katının yüzüne veya bir Parça tasarım özelliği ile eşleştirir veya yeniden eşler. Tipik kullanım durumları:

-   Eskiz, standart bir düzlemde (XY, XZ, YZ) oluşturulmuş ve onu bir katı yüzeyine eşlemek istiyorsanız.
-   Eskiz, bir katının belirli bir yüzünde eşleştirildi, ancak farklı bir yüzle eşlemeniz gerekiyorsa.
-   Bozuk bir modeli onarmak için

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">

## Usage


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

-   Bir parça tasarım özelliğinin veya bir katının yüzünü seçin.

-    **![](images/)[Eskizi_yüze_eşle](Sketcher_MapSketch.md)**tuşuna basın. (veya hangi tezgahın aktif olduğuna bağlı olarak Parça tasarım veya Eskiz menüsüne gidin)

-   Açılan **Eskiz Seç** iletişim penceresinde, Eşlenecek eskizi listeden seçin ve Tamam \'ı tıklayın.

-   Eskiz, düzenleme modunda otomatik olarak açılır.


</div>



## Bozuk bir modeli onarmak için kullanın 

Ezkizi yüze eşle, bozuk bir modeli onarmak için sıklıkla kullanılır.


<div class="mw-translate-fuzzy">

Yaygın kullanım durumlarından biri bağımlılık grafiğinin kırıldığı durumdur. (Bağımlılık grafiğini **Araçlar -> Bağımlılık grafiği** ile görüntüleyebilirsiniz.) Bu, model ağacınızın ortasındaki bir özelliği sildiğinizde olabilir. Aşağıdaki örnekte bir modeli kıracağız ve onaracağız.


</div>

Bu temel model. Bir yastığı, bir cebi ve o cebin içinde bir yastığı var. Bağımlılık grafiğinin doğrusal olduğuna dikkat edin.

![](images/JschremppFCADEdit1.png )

Şimdi cebi ve cebi oluşturan eskizleri sildik (Pocket ve Sketch001). Bağımlılık grafiğinin bozulduğunu unutmayın. Bu modeli onarmak için, Sketch002\'yi Pad\'in üst yüzüne takmak istiyoruz. Modelin görünümünde yanlış yüzü seçmenin kolay olacağını görebilirsiniz.

![](images/JschremppFCADEdit2.png )

Modeli onarmak için önce katıların görünürlüğünü değiştiriyoruz. Pad001\'i gizliyoruz ve Pad\'i görünür yapıyoruz.

![](images/JschremppFCADEdit3.png )

Şimdi Pad\'in üst yüzünü ve ardından eskizi yüze eşle \'yi seçiyoruz. Görüntülenen iletişim kutusunda Sketch002\'yi seçiyoruz. Modelimiz şimdi tamir edildi. Model görünümünde Pad001\'i görünür hale getirip Pad\'i gizliyoruz ve doğru modeli görüyoruz.

![](images/JschremppFCADEdit4.png )


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/tr
