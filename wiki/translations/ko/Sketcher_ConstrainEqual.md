---
 GuiCommand:
   Name: Sketcher ConstrainEqual
   MenuLocation: Sketch , Sketcher constraints , Constrain equal
   Workbenches: Sketcher_Workbench/ko
   Shortcut: **E**
   SeeAlso: 
---

# Sketcher ConstrainEqual/ko



## 설명

스케치에서 <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> 동일구속 도구는 모서리가 동일한 길이(직선인 경우)나 동일한 곡률([B-조절곡선을](Sketcher_CreateBSpline/ko.md) 제외한 곡선일 경우)을 갖도록 구속합니다.



## 용법

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).



### [계속 모드](Sketcher_Workbench#Continue_modes.md) 

1.  선택된 것이 없는지 확인하세요.
2.  동일구속 도구를 호출하는 방법은 여러가지 입니다.
    -   
        **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> 동일구속
**
        
        버튼을 누릅니다.

    -   메뉴에서 **Sketch → Sketcher Constraints → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> 동일구속**을 선택합니다.

    -   
        <small>(v1.0)</small> 
        
        : [3D 보기영역에서](3D_view/ko.md) 마우스 오른쪽 버튼으로 클릭하여 상황 메뉴에서 **Constrain → <img src="images/Sketcher_ConstrainEqual.svg" width=16px> 동일구속**을 선택합니다.

    -   키보드 단축키: **E**를 사용합니다.
3.  커서가 동일구속 아이콘이 있는 십자 모양으로 변경됩니다.
4.  동일한 유형의 모서리 두 개를 선택합니다.
5.  구속이 적용됩니다.
6.  선택적으로 구속을 계속 진행합니다.
7.  마치려면 마우스 오른쪽 버튼을 클릭하거나 **Esc**를 누르거나 다른 형상 또는 다른 구속 도구를 시작하세요.



### 단일 실행 모드 

1.  동일한 유형의 두 개 이상의 모서리를 선택합니다.
2.  위에서 설명한 대로 동일구속 도구를 호출하거나 다음 추가 옵션을 사용하여 호출합니다.
    -   
        <small>(v1.0)</small> 
        
        : [3D 보기영역에서](3D_view/ko.md) 마우스 오른쪽 버튼을 클릭하여 상황 메뉴에서 **<img src="images/Sketcher_ConstrainEqual.svg" width=16px> 동일구속**을 선택합니다.
3.  선택 사항에 따라 하나 이상의 구속이 추가됩니다.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

[Sketcher scripting](Sketcher_scripting.md) 페이지에서는 `Edge1` 및 `Edge2`에 사용할 수 있는 값을 설명합니다. 파이썬 스크립트에서 제약 조건을 만드는 방법에 대한 추가 예제가 포함되어 있습니다.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/ko
