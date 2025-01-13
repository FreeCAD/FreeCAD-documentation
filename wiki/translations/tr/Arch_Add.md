---
 GuiCommand:
   Name: Arch Add
   Name/tr: Mimari Ekle
   MenuLocation: Mimari , Ekle
   Workbenches: Arch_Workbench/tr
   SeeAlso: Arch Remove/tr
---

# Arch Add/tr


</div>



## Açıklama


<div class="mw-translate-fuzzy">

Ekle aracı 4 tür işlem yapmanıza olanak sağlar:

-   [Parça Şekil](Part_Workbench/tr.md) tabanlı nesneler [Duvar](Arch_Wall/tr.md) veya [Yapı](Arch_Structure/tr.md) gibi bir Mimari bileşen ekleyin. Bu nesneler daha sonra Mimari bileşenin bir parçasını oluşturur ve şeklini değiştirmenize izin verir ancak genişlik ve yükseklik gibi temel özelliklerini korur
-   [ Kat](Arch_Floor/tr.md) gibi bir grup tabanlı Mimari nesneye [ Duvar](Arch_Wall/tr.md) veya [ Yapı](Arch_Structure/tr.md) gibi Mimari bileşenleri ekleyin
-   [Mimari Eksen](Arch_Axis/tr.md) \'ni [Yapısal nesneler](Arch_Structure/tr.md)\' e ekleyin
-   Nesneleri [Kesit Düzlemi](Arch_SectionPlane/tr.md) \'ne ekleyin.


</div>


<div class="mw-translate-fuzzy">

Bu aracın karşılığı [Mimari Kaldır](Arch_Remove/tr.md) aracıdır.


</div>

<img alt="" src=images/Arch_Add_example.jpg  style="width:640px;"> {{Caption | Bir duvara bileşen olarak eklenen bir kutu.}}




<div class="mw-translate-fuzzy">

## Nasıl kullanılır 


</div>


<div class="mw-translate-fuzzy">

1.  Önce eklenecek nesneleri , ardından \"Temel bileşen\" nesnesini (Temel bileşen nesnesinin seçtiğiniz son öğe olması gerekir) seçin

2.  
    {{KEY | <img src="images/_Arch_Add.png_" width= 16px> ''' Ekle '''}}düğmesine basın


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Arch_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">

Ekle aracı, aşağıdaki işlevi kullanarak [makrolar](macros/tr.md) ve [Python](Python/tr.md) konsolundan kullanılabilir:


</div>


:   
    
```python
    addComponents(objectsList, host)
    
```
    


<div class="mw-translate-fuzzy">

-    {{incode | objectsList}}içindeki belirli nesneleri verilen {{incode | host}} nesnesine ekler.

    -   
        {{incode | objectsList}}
        
        tek bir nesne veya bir nesne listesi olabilir.


</div>

Örnek:


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Add/tr
