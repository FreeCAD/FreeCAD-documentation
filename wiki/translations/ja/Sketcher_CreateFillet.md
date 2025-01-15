# Sketcher CreateFillet/ja
---
 GuiCommand:   Name: Sketcher CreateFillet   Workbenches: Sketcher Workbench   Sketcher|Shortcut: F   MenuLocation: Sketch , Sketcher geometries , Create fillet   SeeAlso: ---


</div>



## 説明


<div class="mw-translate-fuzzy">

このツールは一点でつながる二直線の間にフィレットを作成します。このツールを起動後、二直線を選択するか角をなす点をクリックしてください。


</div>


<small>(v1.0)</small> 

: If two straight edges connected by a [Coincident constraint](Sketcher_ConstrainCoincident.md) are filleted or chamfered, the corner point can optionally be preserved. The tool then adds a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both edges. Constraints connected to the corner point are transferred to the new point object.

![](images/SketcherCreateFilletExample.png‎ )




<div class="mw-translate-fuzzy">

## 使用方法


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   二直線ををつなぐ頂点をピックするか、二本の繋がった直線をクリックします。クリック位置と頂点との距離によってフィレットの半径が設定されます。

-    **ESC**キーを押すか、右マウスボタンをクリックするとこの機能をキャンセル、終了できます。





</div>

## Notes

-   The construction geometry arc of a chamfer is not visible outside the sketch. It cannot be deleted without breaking the geometry of the chamfer.
-   Some ([conic](Sketcher_Workbench#Sketcher_CompCreateConic.md)) curves may need to be [trimmed](Sketcher_Trimming.md) before they can be filleted.
-   The fillet radius depends on the selection method. If a [Coincident constraint](Sketcher_ConstrainCoincident.md) connecting two straight edges is selected, the fillet radius is derived from the length of the shortest edge. If two edges are selected the radius is the distance from the first clicked point to the (extended) intersection of the edges.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/ja
