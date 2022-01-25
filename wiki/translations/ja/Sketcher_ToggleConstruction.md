---
- GuiCommand:/ja
   Name:Sketcher_ToggleConstruction
   Name/ja:Sketcher_ToggleConstruction
   Workbenches:[スケッチャー](Sketcher_Workbench/ja.md), [パートデザイン](PartDesign_Workbench/ja.md)
   MenuLocation:Sketch → Sketcher geometries → Toggle construction line
---

# Sketcher ToggleConstruction/ja


</div>

## 説明

このツールはスケッチ形状のコンストラクションモードのオン/オフを切り替えます。線、円弧、円と任意の形状タイプに対して使用することができます。

コンストラクション形状はスケッチャーの中でも重要なツールの一つです。3D操作でスケッチを扱う際にはコンストラクション形状は無視されます。


<div class="mw-translate-fuzzy">

スケッチ編集モードではコンストラクション形状は青く表示されスケッチが完全に拘束された場合でも緑色に変わりません。スケッチモードを終了するとコンストラクション形状はスクリーン上で非表示になります。


</div>


<div class="mw-translate-fuzzy">

**注意：** v0.13からコンストラクションラインを[PartDesign Revolve機能の回転軸として使用できるようになりました](PartDesign_Revolve/ja.md)。


</div>

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">


<div class="mw-translate-fuzzy">

## 使用方法

-   3Dビュー上で一つ以上のスケッチ形状を選択し、このツールをクリックするかメニューから起動します。





</div>

There are two ways of using this tool:

1.  Without having anything selected in the [3D view](3D_view.md):
    -   Invoke construction mode by clicking on the **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** or by using the **Sketch → Sketcher geometries → [<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> Toggle construction geometry** entry in the Sketcher menu.
    -   This will change the color for creating new geometric elements to blue.
    -   Newly created geometric elements will now be created in construction mode.
2.  With one or more geometric elements selected in the [3D view](3D_view.md)
    -   Invoke the Sketcher ToggleConstruction tool by clicking on the **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** or by selecting it from the menu
    -   The selected elements will now be changed to construction mode.
    -   Afterwards newly created elements will again be normal geometry.

## Example

Use Construction mode on some sketch elements,

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">

and once you **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [leave the sketcher editing mode](Sketcher_LeaveSketch.md)**, geometry that was turned into construction have become invisible in the [3D view](3D_view.md) (but are still present in the Sketcher editing mode).

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">

## Notes

-    **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Create Point](Sketcher_CreatePoint.md)**will always create points in construction mode regardless of the toolbar toggle state, select the desired points in the [3D view](3D_view.md) after creation and click **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** to change them to normal geometry. <small>(v0.19)</small> 





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/ja
