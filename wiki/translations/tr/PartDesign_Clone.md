---
- GuiCommand:/tr
   Name:Klon oluştur
   Workbenches:[Parça tasarım](PartDesign_Workbench/tr.md)
   MenuLocation:Parça tasarım → Klon oluştur
   Version:0.17
   SeeAlso:[Taslak Klon](Draft_Clone.md)
---

# PartDesign Clone/tr


</div>

## Tanım


<div class="mw-translate-fuzzy">

**Klon oluştur**,seçilen bir nesnenin bağlantılı bir kopyasını oluşturur. Katı olduğu sürece çoğu nesne türü kabul edilir. Klon oluştur\'un ana kullanımı, bir [Boolean](PartDesign_Boolean/tr.md) özelliği için başka bir tezgahta oluşturulan nesneyi kullanmaktır. Ayrıca bağlantılı kopyalar oluşturmak için de kullanılabilir.


</div>

![*Clone of the inner gear while being translated in 3D space as an independent object*](images/clone.png ) 
*Clone of the inner gear while being translated in 3D space as an independent object*

## Nasıl Kullanılır 


<div class="mw-translate-fuzzy">

1.  Model ağacında klonlanacak nesneyi seçin.

2.  
    **<img src=images/PartDesign_Clone.png style="width:24px"> '''Klon Oluştur'''**tuşuna basın.


</div>

## Özellikler


<div class="mw-translate-fuzzy">

-    **Base Feature**: klonun dayandığı orijinal nesneyi ayarlar. **...** basarak değiştirilebilir nesnelerin bir listesini görebilirsiniz.

-    **Placement**: 3D alanda Klonun yönünü ve konumunu tanımlar. [Yerleşim](Placement.md) bkz.

-    **Label**: Klon nesnesinin etiketidir. Gerekirse değiştirebilirsiniz.


</div>

## Sınırlamalar


<div class="mw-translate-fuzzy">

-   **Klon oluştur** ile yalnızca tek bir nesne kullanılabilir.
-   Sadece katı olan nesneler desteklenir. Bu nedenle, [Part container](Std_Part.md), [Part Compound](Part_MakeCompound.md) veya [Draft Array](Draft_Array.md) gibi [bileşikler](Glossary#Compound.md) desteklenmez.


</div>





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Clone/tr
