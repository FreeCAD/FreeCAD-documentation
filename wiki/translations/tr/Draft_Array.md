---
- GuiCommand:
   Name: Draft Array
   Name/tr: Dizi
   MenuLocation: Taslak -> Dizi
   Workbenches: Draft_Workbench/tr, Arch_Workbench/tr
   SeeAlso: Draft PathArray/tr,Draft PointArray/tr,Draft Clone/tr
---

# Draft Array/tr


</div>




<div class="mw-translate-fuzzy">

## Açıklama

Dizi aracı, seçilen bir nesneden ortogonal (3 eksen) veya bir kutupsal dizi oluşturur.


</div>

The <img alt="" src=images/Draft_Array.svg  style="width:24px;"> **Draft Array** command creates an orthogonal (3-axes) array from a selected object. The created array can be turned into a [polar array](Draft_PolarArray.md) or a [circular array](Draft_CircularArray.md) by changing its **Array Type** property.


<div class="mw-translate-fuzzy">

Bu araç, [Taslak tezgahı](Draft_Workbench/tr.md) ile oluşturulan 2D şekillerde kullanılabilir, ayrıca [Parça tezgahı](Part_Workbench/tr.md) ve [Parça tasarım tezgahı](PartDesign_Workbench/tr.md) ile oluşturulan birçok 3D nesne üzerinde de kullanılabilir.


</div>

This command is now obsolete. Use the [Draft OrthoArray](Draft_OrthoArray.md), [Draft PolarArray](Draft_PolarArray.md) or [Draft CircularArray](Draft_CircularArray.md) command instead.

## Usage


<div class="mw-translate-fuzzy">

## Nasıl kullanılır 

1.  Bir dizi yapmak istediğiniz nesneyi seçin.

2.  
    {{Button | <img src="images/_Draft_Array.svg_" width= 16px> [Dizi](Draft_Array/tr.md)}}düğmesine basın. Hiçbir nesne seçilmezse, birini seçmeye davet edilirsiniz.

3.  Dizi nesnesi hemen yaratılır. Oluşturulan kopyaların sayısını ve yönünü değiştirmek için dizinin özelliklerini değiştirmeniz gerekir.


</div>

## Properties


<div class="mw-translate-fuzzy">

## Özellikler

-    {{PropertyData | Base}}: Dizide çoğaltılacak nesneyi belirtir.

-    {{PropertyData | Array Type}}: \"ortho\" veya \"polar\" olmak üzere yaratılacak dizinin türünü belirtir.

-    {{PropertyData | Fuse}}: `True` ise ve kopyalar birbiriyle kesişirse, bunlar birlikte tek bir şekilde kaynaşırlar.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Betik


**Ayrıca bkz.:**

[Taslak API](Draft_API/tr.md) ve [FreeCAD Betik esasları](FreeCAD_Scripting_Basics/tr.md).


</div>


<div class="mw-translate-fuzzy">


{{Draft Tools navi/tr}}


{{Userdocnavi/tr}}


</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/tr
