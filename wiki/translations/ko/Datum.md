# Datum/ko
## 소개

FreeCAD에서 \"기준도형(Datum)\"이라는 단어는 일반적으로 [부품설계 작업대에서](PartDesign_Workbench/ko.md) 보조 형상을 나타내는 데 사용됩니다. 이러한 기하학적 요소는 [몸통의](Body/ko.md) 최종 [형상의](Shape/ko.md) 일부를 구성하지는 않지만, [스케치](Sketch/ko.md) 및 다른 유형의 [도형특징에](Feature/ko.md) 대한 참조 및 지원으로 사용할 수 있습니다.

다음은 [Part Feature에서](Part_Feature.md) 파생된 `Part::Datum` 클래스에서 파생된 요소에 해당합니다.

-   [PartDesign Point](PartDesign_Point.md)
-   [PartDesign Line](PartDesign_Line.md)
-   [PartDesign Plane](PartDesign_Plane.md)
-   [PartDesign CoordinateSystem](PartDesign_CoordinateSystem.md)

다음은 [Part Feature에서](Part_Feature.md) 직접 파생됩니다.

-   [PartDesign ShapeBinder](PartDesign_ShapeBinder.md)
-   [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md)



## 용법

1.  [부품설계 작업대로](PartDesign_Workbench/ko.md) 전환합니다.

2.  
    **[<img src=images/PartDesign_Body.svg style="width:16px"> [몸통생성](PartDesign_Body/ko.md)**버튼을 누릅니다.

3.  몸통의 원점을 선택하고 키보드의 **Space** 바를 눌러 표시되도록 합니다.

4.  
    **[<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Plane](PartDesign_Plane.md)**를 눌러 평면 [task_panel을](task_panel.md) 엽니다.

5.  [3D 보기에서](3D_view/ko.md) 표준 평면 중 하나(예: XY 평면)를 클릭합니다. 그런 다음 **OK**를 눌러 작업 패널을 닫습니다.

6.  이제 [tree_view에서](tree_view.md) 새로 생성된 기준평면을 선택한 다음 **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [스케치 생성](PartDesign_NewSketch/ko.md)**버튼을 누릅니다.

7.  닫힌 와이어를 생성한 다음 **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)**를 사용하여 스케치를 돌출시키고 초기 고체를 생성합니다.

이제 [속성 편집기에서](property_editor/ko.md) 해당 속성을 변경하여 원하는 대로 기준평면을 이동하고 회전할 수 있으며 스케치와 패드는 새로운 [Placement를](Placement.md) 따릅니다.

여러분은 다른 스케치 및 도형특징과 함께 사용할 다른 유형의 기준도형을 추가할 수 있습니다.



## 보충 설명 

기준도형 객체는 [0.17버전에서](Release_notes_0.17/ko.md) 등장했기 때문에 [몸통(PartDesign Bodies)](PartDesign_Body/ko.md) 내부에서 사용되도록 의도되었습니다. 그러나 이는 다양한 [Part_EditAttachment을](Part_EditAttachment.md) 사용하는 유용한 \"참조\" 객체이므로 [부품설계 작업대](PartDesign_Workbench/ko.md) 외부에서 사용할 수 있어야 한다는 제안이 있었습니다. 이러한 방식으로 모든 작업대에서 특히 [조립품](Assembly/ko.md) 생성과 관련된 지원 형상으로 사용할 수 있습니다.

-   [Create and display local coordinate system](https://forum.freecadweb.org/viewtopic.php?f=10&t=2604)
-   [Datum objects in App::Part](https://forum.freecadweb.org/viewtopic.php?f=22&t=33654)
-   [Structure toolbar and datums](https://forum.freecadweb.org/viewtopic.php?t=42759)
-   [Local CS cannot be used in Part Wb?](https://forum.freecadweb.org/viewtopic.php?f=3&t=42960)


{{PartDesign Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Datum/ko
