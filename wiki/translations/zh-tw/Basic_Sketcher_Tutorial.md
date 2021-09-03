


{{TutorialInfo/zh-tw
|Topic=草圖
|Level=初學者
|Time=60分鐘
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei] 及 vocx
|FCVersion=0.19
|Files=[https://forum.freecadweb.org/viewtopic.php?f=36&t=43594 草圖基本教學檔案更新]
}}

簡介

本教學由Drei原創，並由vocx重新編輯並製作插圖。

本教學主要介紹草圖工作台(Sketcher Workbench)的基本工作流程。

<img src=images/PartDesign_Pad.svg style="width:草圖工作台(Sketcher Workbench)是一獨立模組](Sketcher_Workbench.md)，可用於繪製2D(平面)物件。但是，它通常與 <img alt="Workbench_PartDesign.svg" src=images/Workbench_PartDesign.svg  style="width:24px;"> [零件設計工作台(PartDesign Workbench)結合使用](PartDesign_Workbench.md)。一個具有封閉輪廓外型的草圖通常用**[16px">[填充所選草圖](PartDesign_Pad.md)**來建立[實體物件](PartDesign_Body.md) .

讀者將會練習：

-   建立建構性(輔助製圖用)幾何圖元
-   建立真實幾何圖元
-   使用幾何拘束
-   使用基準面拘束
-   得到封閉的輪廓圖

深入了解草圖(Sketcher)，請參考[草圖參考](Sketcher_reference.md)

![](images/00_Sk01_Sketcher_fully_constrained_final.png ) *草圖的最終成果，所有幾何圖元完全拘束，包含用於輔助製圖的結構圖元.*

## 設定

1\. 開啟FreeCAD, 使用{{MenuCommand|檔案 → <img src=images/Std_New.svg style="width:16px"> [開新檔案](Std_New.md)}}新增一空白文件.

:   1.1. 使用 [工作台之間切換](Std_Workbench.md)，切換到[草圖工作台](Sketcher_Workbench.md), 或者從功能表 {{MenuCommand|[檢視](Std_View_Menu.md) → 工作台 → 草圖}}.

需要記住的一些動作:

-   按滑鼠右鍵，或在鍵盤上按一下 **Esc**，可在編輯模式下取消選擇目前啟用的工具。
-   離開草圖編輯模式，按一下[複合檢視/任務上方的](task_panel.md)**Close**按鈕，或按二次鍵盤的**Esc**按鍵。
-   要再次進入編輯模式，在<img src=images/Sketcher_EditSketch.svg style="width:樹狀檢視中該草圖名稱上點二下](tree_view.md) ；或點選該草圖，再按一下**[16px"> [編輯所選之草圖](Sketcher_EditSketch.md)**。

## 建立草圖

2\. 按一下**<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [建立新草圖](Sketcher_NewSketch.md)**。

:   2.1. 選擇草圖平面，即XY，XZ或YZ基準面三選一。您亦可選擇相反方向的基準面，或是平行偏移於選定基準面一定距離的平面做為新基準面。
:   2.2. 將使用預設平面和選項。
:   2.3. 按下**OK**開始建構該草圖。

您已進入草圖編輯模式。在其中，您能夠利用該工作台的大多數工具。


**註:**

[樹狀檢視將會切換至](tree_view.md)[任務面板](task_panel.md); 在此界面中將{{MenuCommand|「Edit controls」}}區塊展開，並確認{{MenuCommand|「自動拘束」}}已勾選。其他選項可以更改，包括網格的大小，以及是否要「格點快選」；本教學中我們將不使用「格點快選」並將格點顯示關閉。 在[任務面板的其他區塊](task_panel.md)，您可看到有哪些圖元及哪種拘束被套用。

<img alt="" src=images/01_Sk01_Sketcher_Task_panel.png  style="width:" height="400px;">


*草圖編輯器中[「任務面板」](task_panel.md)的上半部。*

## 建構用幾何圖元

3\. 建構用幾何圖元(建構線)是用來輔助畫出\"真實\"幾何圖元。離開草圖編輯模式後會顯示的圖形就是真實(一般)幾何圖元，而建構線只有在進入草圖編輯模式後才會顯示。因此，您可以根據需要使用任意數量的建構線來輔助繪製出實際輪廓圖。

輪廓圖就是由(一般)線段、圓弧等圖元所構成的外型圖，如果要用於形成實體零件，此外型圖必須為封閉(圖形中沒有空白段)，所以將具有封閉外型的草圖稱為輪廓圖。

:   3.1. 按下**<img src="images/Sketcher_ToggleConstruction.svg" width=16px> [Toggle construction](Sketcher_ToggleConstruction.md)**，進入{{MenuCommand|建構線模式}}。
:   註：建構線模式中，工具列圖示中的線條為深藍色，在草圖中建構線圖元也是深藍色，一般模式中，工具列圖示中的線條為白色，在草圖中一般圖元也是白色。
:   3.2. 按下 **<img src="images/Sketcher_Line.svg" width=16px> [於草圖中建立線](Sketcher_CreateLine.md)**。
:   3.3. 在草圖中將滑鼠游標靠近**原點**，該點將高亮顯示並且在游標的右方將顯示<img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [共點(重疊)拘束](Sketcher_ConstrainCoincident.md)。
:   3.4. 點選一下該點(滑鼠左鍵)，然後移動游標準備建立一條新的直線。移動一下游標位置使線段長度大約{{Value|30 mm}}，再點一下(滑鼠左鍵)就會產生一新線段。在此步驟中的長度並不需要非常精確； 在後續步驟中將設定此線段的尺寸。
:   3.5. 重複步驟3.4，再繪製出四條大約呈星型的建構線(見下圖)。不需太在意他們的尺寸或位置，只需要將它們畫在四個像限。
:   3.6. 現在再按一下**<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** 切換建構線模式到一般模式。


**註1:**

此時**<img src="images/Sketcher_Line.svg" width=16px> [於草圖中建立線](Sketcher_CreateLine.md)**工具仍在作用中。這表示我們可以在 [3D view](3D_view.md) 中繼續點擊以繪製出更多的線段。如要離開**<img src="images/Sketcher_Line.svg" width=16px> [於草圖中建立線](Sketcher_CreateLine.md)**工具，按一下滑鼠右鍵或按一下鍵盤上的**Esc**鍵。By doing this the pointer won\'t create lines any more, it will just be a pointer allowing us to select the objects we just created. In this pointer mode we can pick and drag the endpoints of each line to adjust its placement.


**Note 2:**

do not press **Esc** a second time as this will exit the sketch edit mode. If you do this, re-enter the edit mode by double clicking on the sketch in the [tree view](tree_view.md).

Take a look at the [task panel](task_panel.md) again. The {{MenuCommand|Solver messages}} section already indicates that the sketch is under-constrained, and it mentions the number of **degrees of freedom**.

Look at the {{MenuCommand|Constraints}} and {{MenuCommand|Elements}} sections to see the new listed constraints and lines. Once your sketches have many elements, it may be difficult to select them in the [3D view](3D_view.md), so you can use these lists to select the object that you wish exactly.

<img alt="" src=images/02_Sk01_Sketcher_construction.png  style="width:" height="400px;">


*以原點為中心呈星型的建構線*

## Real geometry {#real_geometry}

Real geometry must make a closed shape if it is to be used as a profile that can be extruded by tools such as **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)**.

Make sure you are not in construction mode by clicking on **<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)**, if you have not previously exited this mode.

### Outer arcs {#outer_arcs}

4\. Create a circle.

:   4.1. Click on **<img src=images/Sketcher_Circle.svg style="width:16px"> [Create circle](Sketcher_CreateCircle.md)**.
:   4.2. Click on the **origin** of the sketch to position its center point.
:   4.3. Click anywhere in the [3D view](3D_view.md) to set the circumference radius as a distance from the origin. Make it approximately {{Value|8 mm}}. Again the dimension will be fixed later.

5\. Create a series of arcs.

:   5.1. Click on **<img src=images/Sketcher_Arc.svg style="width:16px"> [Create arc](Sketcher_CreateArc.md)**.
:   5.2. Approach the endpoint of one of the construction lines, and click on it. This will set the center point of the circular arc to be <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> [coincident](Sketcher_ConstrainCoincident.md) with this line\'s endpoint.
:   5.3. Click once in the [3D view](3D_view.md) at an arbitrary location to set simultaneously the radius of the arc, and the first endpoint of it. Define an approximate radius of {{Value|8 mm}}.
:   5.4. Move the pointer in an anti-clockwise direction to trace an arc that has its concavity pointing towards the origin of the sketch. Click to set the final endpoint of the arc, defining a circular arc that approximately sweeps {{Value|180°}} or half a circle.
:   5.5. Repeat these steps with each construction line, so that each of them has a circular arc at its tip. We will call these O-arcs for outwards-arcs.

<img alt="" src=images/03_Sk01_Sketcher_outer_arcs.png  style="width:" height="400px;">


*Circular arcs added at the endpoints of the construction lines. Also a central circle.*

### Inner arcs {#inner_arcs}

6\. Create an arc between each pair of the previous O-arcs.

:   6.1. Still with the **<img src=images/Sketcher_Arc.svg style="width:16px"> [Create arc](Sketcher_CreateArc.md)** tool active, click somewhere between two O-arcs but further away from the origin of the sketch, to set the center point of a new arc.
:   6.2. Click somewhere close to the endpoint of one O-arc, and move the pointer to sweep another arc finishing close to another endpoint of a different O-arc, as if you were trying to join the endpoints. This time the concavity must point away from the origin.
:   6.3. Repeat these steps, so that each pair of O-arcs has a new arc between them. We will call these I-arcs for inwards-arcs.

To summarize, the O-arcs should have their curvature pointing outwards, and their concavity pointing towards the origin of the sketch; the I-arcs should have their curvature pointing inwards, and their concavity pointing away from the same origin.

<img alt="" src=images/04_Sk01_Sketcher_inner_arcs.png  style="width:" height="400px;">


*Circular arcs added between the first set of arcs placed.*

## Constraints

Take a look at the [task panel](task_panel.md) again. Due to the new geometrical elements that we have drawn, the {{MenuCommand|Solver messages}} section indicates even more **degrees of freedom**. A **degree of freedom** (DOF) indicates a possible movement of one element. For example, a point can be moved both in horizontal and vertical directions, so it has two degrees of freedom. A line is defined by two points, therefore in total it has four degrees of freedom. If we fix one of those points, then the entire system has only two degrees of freedom available; if we additionally fix the horizontal movement of the remaining point, we only have one degree of freedom left; and if we also fix the vertical movement of this point, then the last degree of freedom disappears, and the line cannot move from its position any more.

Up to now when we have drawn lines and curves, the sketcher has added automatic constraints for us, those that keep the lines tied to the origin, and the O-arcs tied to the construction lines. But we haven\'t added other explicit constraints so the geometrical shapes can still be moved in many directions. **Constraints are \"rules\" that tell us under which conditions a geometrical object can move and by how much.** They are used to eliminate the degrees of freedom so that the sketch has a stable shape. If we eliminate all degrees of freedom, then the sketch is **fully constrained**, and has a fixed shape, that is, its points cannot move at all. In general, it is a good idea to fully constrain sketches because this will result in stable models.

There are two principal types of constraints:

-    **Geometric constraints**define characteristics of the shapes without specifying exact dimensions, for example, horizontality, verticality, parallelism, perpendicularity, and tangency.

-    **Datum constraints**define characteristics of the shapes by specifying dimensions, for example, a numeric length or an angle.

## Geometric constraints {#geometric_constraints}

### Equal length and radius {#equal_length_and_radius}

7\. Geometrically constrain the lines and arcs.

:   7.1 Select all five construction lines. You only need to click once to select an element.
:   7.2. Press **<img src=images/Constraint_EqualLength.svg style="width:16px"> [Equal length](Sketcher_ConstrainEqual.md)**.
:   
    **Note:**this creates only four constraints. The constraints are chained, the first line has the same length as the second one, which has the same length as the third one, which again has the same length as the fourth one, which has the same length as the fifth one. So in this case, the first and the fifth have the same length.





:   7.3. Select all five O-arcs, those centered on an endpoint of a construction line.
:   7.4. Press **<img src=images/Constraint_EqualLength.svg style="width:16px"> [Equal length](Sketcher_ConstrainEqual.md)**.
:   7.5. Repeat with all I-arcs, those between the O-arcs.
:   
    **Note:**again the constraints are chained. Therefore all O-arcs will have the same radius, and all I-arcs will have the same radius. At this moment, the specific value of these lengths is not fixed. You may use the pointer to drag a point and see how the sketch is updated while respecting the constraints in place.





:   7.6. Select the construction line that is closest to the vertical axis.
:   7.7. Press **<img src=images/Constraint_Vertical.svg style="width:16px"> [Vertical](‎Sketcher_ConstrainVertical.md)** (optional). If you drew the construction line downwards over the Y axis, an automatic <img alt="" src=images/Constraint_PointOnObject.svg  style="width:32px;"> [Point on object constraint](Sketcher_ConstrainPointOnObject.md) was already placed, keeping the construction line vertical. In this case, no additional <img alt="" src=images/Constraint_Vertical.svg  style="width:32px;"> [Vertical constraint](‎Sketcher_ConstrainVertical.md) is necessary.


**Note:**

as you add constraints, overlay symbols indicating the type of constraint appear over the geometry in the [3D view](3D_view.md). If these symbols obfuscate your view, you can hide them by unchecking the constraint in the [task panel](task_panel.md). Also note that the number of degrees of freedom decreases after adding each constraint.


**Note 2:**

if you wish to temporarily disable the constraint, you may select it and press **<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [Toggle active constraint](Sketcher_ToggleActiveConstraint.md)**. When you want to apply it again, press again the same button.

<img alt="" src=images/05a_Sk01_Sketcher_equality_constraints_lines.png  style="width:" height="400px;"> <img alt="" src=images/05b_Sk01_Sketcher_equality_constraints_O-arcs.png  style="width:" height="400px;">

<img alt="" src=images/05c_Sk01_Sketcher_equality_constraints_I-arcs.png  style="width:" height="400px;">


*Sketch with equality constraints applied to the construction lines, and to the two sets of arcs.*

### Tangency

8\. Apply tangency to the arcs.

:   8.1. Select one endpoint of an O-arc and then the closest endpoint of the adjacent I-arc.
:   8.2. Press **<img src=images/Constraint_Tangent.svg style="width:16px"> [Tangent](Sketcher_ConstrainTangent.md)**. This makes the two adjacent arcs connect smoothly at their endpoints.
:   8.3. Repeat for all endpoints of the O-arcs and I-arcs to obtain a closed profile.


**Note:**

applying the tangential constraint very often will move the geometry around in order to produce a smooth connection. You may have to use the pointer to reposition the points a bit before applying the next tangential constraint. Try placing the endpoints in such a way that two arcs aren\'t too far apart, so they can be connected with a short line rather than a long line.

As of this step, we have now created a closed profile, as all arcs have been tied together. Now we can provide datum constraints to fix the shape of the sketch. While the dimensions of lines and arcs remain unfixed, we can drag the points of the sketch and observe how the entire sketch changes.

<img alt="" src=images/06_Sk01_Sketcher_tangency_constraints.png  style="width:" height="400px;">


*Sketch with tangential constraints applied to the arcs, which closes the shape.*

## Datum constraints {#datum_constraints}

These constraints specify the numerical distances between two points, and angles between two lines.

### Distances and angles {#distances_and_angles}

9\. Adjust the size of the construction lines.

:   9.1. Select the vertically constrained construction line.
:   9.2. Press **<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertical distance](Sketcher_ConstrainDistanceY.md)**.
:   9.3. Set the length to {{Value|30 mm}}. Because all construction lines are constrained to have the same length, all these lines adjust their sizes at the same time.

10\. Adjust the angle between the construction lines.

:   10.1. Select the vertical construction line and the construction line closest to it.
:   10.2. Press **<img src=images/Constraint_InternalAngle.svg style="width:16px"> [Angle](Sketcher_ConstrainAngle.md)**.
:   10.3. Set the angle to {{Value|72°}}.
:   10.4. Repeat the same procedure for each pair of construction lines, and use the same angle.
:   
    **Note:**at this stage, the sketch may have very few degrees of freedom left, meaning that its shape cannot be changed too much. If you attempt to add more constraints, these may cause a conflict with the previously added constraints. If this is the case, do not add these constraints, and proceed with the next steps.

<img alt="" src=images/07a_Sk01_Sketcher_length_constraint.png  style="width:" height="400px;"> <img alt="" src=images/07b_Sk01_Sketcher_angle_constraint.png  style="width:" height="400px;">


*Sketch with length constraint applied to one vertical construction line (left), and angle constraints to three pairs of construction lines (right).*

### Radius

11\. Adjust the size of the arcs.

:   11.1. Select one of the O-arcs, centered on the endpoint of a construction line.
:   11.2. Press **<img src=images/Constraint_Radius.svg style="width:16px"> [Radius](Sketcher_ConstrainRadius.md)**.
:   11.3. Set the radius to {{Value|8 mm}}. Because all O-arcs are constrained to have the same radius, all these arcs adjust their sizes at the same time.
:   11.4. Select one of the I-arcs, between two O-arcs.
:   11.5. Press **<img src=images/Constraint_Radius.svg style="width:16px"> [Radius](Sketcher_ConstrainRadius.md)**.
:   11.6. Set the radius to {{Value|11 mm}}. Because all I-arcs are constrained to have the same radius, all these arcs adjust their sizes at the same time.

<img alt="" src=images/08a_Sk01_Sketcher_radius_1_constraint.png  style="width:" height="400px;"> <img alt="" src=images/08b_Sk01_Sketcher_radius_2_constraint.png  style="width:" height="400px;">


*Sketch with radius constraints applied to the outwards arcs (left), and inwards arcs (right).*


:   11.7. Finally, select the circle in the center of the sketch, press **<img src=images/Constraint_Radius.svg style="width:16px"> [Radius](Sketcher_ConstrainRadius.md)**, and set the value to {{Value|8 mm}}.

We should end up with a fully constrained sketch. It can be confirmed by noticing the change in color of the real geometry, and by the message that is shown in the [task panel](task_panel.md).

<img alt="" src=images/09_Sk01_Sketcher_fully_constrained.png  style="width:" height="400px;">


*Sketch with all geometrical and datum constraints applied.*

## Extrusion

12\. Now that we have a fully constrained sketch, it can be used to create a solid body.

:   12.1. Exit the sketch edit mode by pressing the **Close** button, or pressing **Esc** twice. The sketch should appear in the [tree view](tree_view.md) and the [3D view](3D_view.md).
:   12.2. Switch to the [PartDesign Workbench](PartDesign_Workbench.md).
:   12.3. With the sketch selected in the <img src=images/PartDesign_Body.svg style="width:tree view](tree_view.md), press **[16px"> [PartDesign Body](PartDesign_Body.md)**, choose the default XY-plane, and press **OK**. The sketch should appear now inside the Body.
:   12.4. Select the sketch, and then press **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)**, choose the default options, and press **OK** to create a solid extrusion.

<img alt="" src=images/09b_Sk01_Sketcher_fully_constrained_clean.png  style="width:" height="400px;"> <img alt="" src=images/10_Sk01_Sketcher_solid_extrusion.png  style="width:" height="400px;">


*Left: fully constrained sketch with only the most important constraints showing. Right: solid extrusion produced with [PartDesign Pad](PartDesign_Pad.md).*

## Additional information {#additional_information}

For a more in depth description of the sketcher, visit the [Sketcher Workbench](Sketcher_Workbench.md) documentation and also read the [Sketcher reference](Sketcher_reference.md).

Constraining a sketch can be done in many different ways. In general, it is recommended to use geometrical constraints first, and minimize the number of datum constraints, as this simplifies the task of the internal constraint solver. To investigate this, repeat this example, now adding the constraints in different order.

-   First constrain the construction lines before drawing the arcs.
-   Or constrain the size of the arcs before making them tangent.
-   Or set the angle of the construction lines before adding more elements.
-   Try using other construction geometry.


{{Tutorials navi

}} {{Sketcher Tools navi}} 
