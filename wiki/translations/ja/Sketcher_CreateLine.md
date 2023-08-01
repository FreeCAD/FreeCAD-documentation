# Sketcher CreateLine/ja
---
- GuiCommand:   Name: Sketcher CreateLine   Workbenches: [MenuLocation: Sketch - Sketcher geometries - Create line   Shortcut: L   SeeAlso: [[Sketcher CreatePolyline|Sketcher Polyline](Sketcher_Workbench___Sketcher]].md)---


</div>



## 説明


<div class="mw-translate-fuzzy">

このツールは3Dビュー上の二点をピックすることで直線を描画します。

このツールを起動するとマウスポインターが赤い直線アイコンのついた白い十字に変わります。またポインターの指す座標がリアルタイムに表示されます。


</div>

![](images/Sketcher_LineExample1.png‎ )

The created line object starts and ends at the given points, but the line is infinite regarding the constraints [Tangent](Sketcher_ConstrainTangent.md), [Point On Object](Sketcher_ConstrainPointOnObject.md) and [Internal Angle](Sketcher_ConstrainAngle.md). This means for example, that a point with the constraint [Point On Object](Sketcher_ConstrainPointOnObject.md) may not be located between the two given points but can lie outside of the two points on the extension of the drawn line.




<div class="mw-translate-fuzzy">

## 使用方法


</div>


<div class="mw-translate-fuzzy">

-   3Dビューの何もない領域または既存のオブジェクト上の点をピックします（タスクビューで自動拘束が有効になっている必要があります）。

-    **ESC**キーを押すか、右マウスボタンをクリックするとこの機能は解除されます。





</div>





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/ja
